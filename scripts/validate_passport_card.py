#!/usr/bin/env python3
"""Validate the ECZ-ID Passport Carry-Card v1.0 interoperability core.

Zero third-party dependencies by design. This validates the current public
identifier family contract and canonical proof-pointer URLs. It does not
resolve an ECZ-ID or turn the card into proof; current state must be fetched
from the Resolver when a relying decision is made.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote, urlparse

PARENT_RE = re.compile(r"^ECZ-[A-Z]{2}-[0-9A-Z]{6}$")
CHILD_RE = re.compile(
    r"^(ECZ-[A-Z]{2}-[0-9A-Z]{6})::([A-Z0-9_]+)-([0-9A-Z]{6})$"
)

FAMILY_TYPE_CODES = {
    "agent": "AGENT_PASSPORT",
    "mcp": "MCP_PASSPORT",
    "plugin": "PLUGIN_PASSPORT",
    "api": "API_PASSPORT",
    "iot": "IOT_DEVICE",
    "sdk": "SDK_PASSPORT",
    "service-workload": "SERVICE_WORKLOAD_PASSPORT",
}

ALLOWED_FAMILIES = {"parent", *FAMILY_TYPE_CODES.keys()}

REQUIRED = {
    "schema",
    "schema_version",
    "ecz_id",
    "passport_family",
    "resolver_url",
}

URL_FIELDS = {
    "resolver_url",
    "machine_proof_url",
    "subject_url",
    "badge_url",
    "acquisition_url",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def is_https(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def canonical_urls(ecz_id: str) -> tuple[str, str]:
    encoded = quote(ecz_id, safe="")
    return (
        f"https://resolver.ecocitizenz.org/p/{encoded}",
        f"https://api.ecocitizenz.com/api/p/{encoded}.json",
    )


def validate_identifier(ecz_id: str, family: str) -> str | None:
    if family == "parent":
        if PARENT_RE.fullmatch(ecz_id) is None:
            fail("parent passport_family requires canonical parent ECZ-ID syntax")
        return None

    match = CHILD_RE.fullmatch(ecz_id)
    if match is None:
        fail(
            "child passport_family requires '<parent>::<CURRENT_TYPE_CODE>-<6 chars>' ECZ-ID syntax"
        )

    parent, type_code, _instance = match.groups()
    expected_type = FAMILY_TYPE_CODES[family]
    if type_code != expected_type:
        fail(
            f"passport_family '{family}' requires child type code '{expected_type}', got '{type_code}'"
        )
    return parent


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--allow-example",
        action="store_true",
        help="Allow a checked-in fixture explicitly marked extensions.example_fixture=true.",
    )
    args = parser.parse_args()

    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot read valid UTF-8 JSON: {exc}")

    if not isinstance(data, dict):
        fail("card root must be a JSON object")

    missing = sorted(REQUIRED - data.keys())
    if missing:
        fail(f"missing required fields: {', '.join(missing)}")

    if data["schema"] != "eczid.passport-carry-card":
        fail("schema must equal eczid.passport-carry-card")
    if data["schema_version"] != "1.0":
        fail("schema_version must equal 1.0")

    family = data["passport_family"]
    if family not in ALLOWED_FAMILIES:
        fail(f"unsupported passport_family: {family}")

    ecz_id = data["ecz_id"]
    if not isinstance(ecz_id, str):
        fail("ecz_id must be a string")
    child_parent = validate_identifier(ecz_id, family)

    extensions = data.get("extensions")
    if extensions is not None and not isinstance(extensions, dict):
        fail("extensions must be an object")
    is_example = isinstance(extensions, dict) and extensions.get("example_fixture") is True
    if is_example and not args.allow_example:
        fail("example fixture cannot be used as a production card; pass --allow-example only for tests/examples")

    for field in URL_FIELDS:
        if field in data:
            value = data[field]
            if not isinstance(value, str) or not is_https(value):
                fail(f"{field} must be an absolute HTTPS URL")

    expected_resolver, expected_machine = canonical_urls(ecz_id)
    if data["resolver_url"] != expected_resolver:
        fail(
            f"resolver_url must use the canonical human Resolver route: {expected_resolver}"
        )
    if "machine_proof_url" in data and data["machine_proof_url"] != expected_machine:
        fail(
            f"machine_proof_url must use the canonical machine proof route: {expected_machine}"
        )

    if "parent_ecz_id" in data:
        parent = data["parent_ecz_id"]
        if not isinstance(parent, str) or PARENT_RE.fullmatch(parent) is None:
            fail("parent_ecz_id must use canonical parent ECZ-ID syntax when present")
        if child_parent is not None and parent != child_parent:
            fail("parent_ecz_id must match the parent encoded in the child ECZ-ID")

    print(
        f"OK: {args.path} conforms to the current ECZ-ID Passport Carry-Card v1.0 interoperability core"
    )


if __name__ == "__main__":
    main()
