#!/usr/bin/env python3
"""Regression tests for the current seven-family Carry-Card contract."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_passport_card.py"
PARENT = "ECZ-ZZ-EXAMPL"

FAMILIES = {
    "agent": ("AGENT_PASSPORT", "A1B2C3"),
    "mcp": ("MCP_PASSPORT", "B2C3D4"),
    "plugin": ("PLUGIN_PASSPORT", "C3D4E5"),
    "api": ("API_PASSPORT", "D4E5F6"),
    "iot": ("IOT_DEVICE", "E5F6G7"),
    "sdk": ("SDK_PASSPORT", "F6G7H8"),
    "service-workload": ("SERVICE_WORKLOAD_PASSPORT", "G7H8J9"),
}


def card(family: str) -> dict:
    type_code, suffix = FAMILIES[family]
    ecz_id = f"{PARENT}::{type_code}-{suffix}"
    encoded = quote(ecz_id, safe="")
    return {
        "schema": "eczid.passport-carry-card",
        "schema_version": "1.0",
        "ecz_id": ecz_id,
        "passport_family": family,
        "resolver_url": f"https://resolver.ecocitizenz.org/p/{encoded}",
        "machine_proof_url": f"https://api.ecocitizenz.com/api/p/{encoded}.json",
        "parent_ecz_id": PARENT,
        "subject_url": "https://example.test",
    }


class ValidatorContractTests(unittest.TestCase):
    def run_card(self, value: dict, *, allow_example: bool = False) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "card.json"
            path.write_text(json.dumps(value), encoding="utf-8")
            cmd = [sys.executable, str(VALIDATOR), str(path)]
            if allow_example:
                cmd.append("--allow-example")
            return subprocess.run(cmd, text=True, capture_output=True, check=False)

    def test_all_seven_current_families_pass(self) -> None:
        for family in FAMILIES:
            with self.subTest(family=family):
                result = self.run_card(card(family))
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_eighth_family_is_rejected(self) -> None:
        value = card("agent")
        value["passport_family"] = "robot"
        result = self.run_card(value)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unsupported passport_family", result.stderr)

    def test_catalogue_era_code_is_rejected(self) -> None:
        value = card("agent")
        value["ecz_id"] = f"{PARENT}::AGENT-A1B2C3"
        result = self.run_card(value)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("requires child type code 'AGENT_PASSPORT'", result.stderr)

    def test_family_type_mismatch_is_rejected(self) -> None:
        value = card("api")
        value["passport_family"] = "mcp"
        result = self.run_card(value)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("requires child type code 'MCP_PASSPORT'", result.stderr)

    def test_parent_mismatch_is_rejected(self) -> None:
        value = card("sdk")
        value["parent_ecz_id"] = "ECZ-ZZ-OTHERS"
        result = self.run_card(value)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must match the parent encoded", result.stderr)

    def test_legacy_resolver_route_is_rejected(self) -> None:
        value = card("mcp")
        value["resolver_url"] = f"https://resolver.ecocitizenz.org/passport/{value['ecz_id']}"
        result = self.run_card(value)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("canonical human Resolver route", result.stderr)

    def test_example_fixture_requires_explicit_flag(self) -> None:
        value = card("plugin")
        value["extensions"] = {"example_fixture": True}
        denied = self.run_card(value)
        self.assertNotEqual(denied.returncode, 0)
        allowed = self.run_card(value, allow_example=True)
        self.assertEqual(allowed.returncode, 0, allowed.stderr)


if __name__ == "__main__":
    unittest.main()
