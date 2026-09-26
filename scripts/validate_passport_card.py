#!/usr/bin/env python3
"""Validate the minimum ECZ-ID Passport Carry-Card v1.0 contract.

Zero third-party dependencies by design. This validates the interoperability
core and safety-sensitive URL rules. It does not resolve the ECZ-ID or turn
the card into proof; current proof must be fetched from the Resolver.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

ALLOWED_FAMILIES = {
    "parent",
    "agent",
    "mcp",
    "plugin",
    "api",
    "iot",
    "sdk",
    "service-workload",
}

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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--allow-example",
        action="store_true",
        help="Allow an EXAMPLE sentinel ECZ-ID in a checked-in reference fixture.",
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
    if data["passport_family"] not in ALLOWED_FAMILIES:
        fail(f"unsupported passport_family: {data['passport_family']}")

    ecz_id = data["ecz_id"]
    if not isinstance(ecz_id, str) or not ecz_id.startswith("ECZ-"):
        fail("ecz_id must be a non-empty ECZ-ID string")
    if "EXAMPLE" in ecz_id and not args.allow_example:
        fail("example ECZ-ID cannot be used as a production card")

    for field in URL_FIELDS:
        if field in data:
            value = data[field]
            if not isinstance(value, str) or not is_https(value):
                fail(f"{field} must be an absolute HTTPS URL")

    if "parent_ecz_id" in data:
        parent = data["parent_ecz_id"]
        if not isinstance(parent, str) or not parent.startswith("ECZ-"):
            fail("parent_ecz_id must be an ECZ-ID string when present")

    if "extensions" in data and not isinstance(data["extensions"], dict):
        fail("extensions must be an object")

    print(
        f"OK: {args.path} conforms to the ECZ-ID Passport Carry-Card v1.0 interoperability core"
    )


if __name__ == "__main__":
    main()
