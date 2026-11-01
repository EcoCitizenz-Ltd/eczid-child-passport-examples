# ECZ-ID Passport Carry-Card v1.0

The Carry-Card is a small pointer envelope that lets software carry an ECZ-ID reference without copying current Resolver state into the distribution asset.

## Current identifier contract

Parent ECZ-ID:

```text
ECZ-CC-XXXXXX
```

Current child ECZ-ID:

```text
{parent_ecz_id}::{CURRENT_TYPE_CODE}-XXXXXX
```

The seven current free machine Passport family type codes are:

| `passport_family` | Child type code |
| --- | --- |
| `agent` | `AGENT_PASSPORT` |
| `mcp` | `MCP_PASSPORT` |
| `plugin` | `PLUGIN_PASSPORT` |
| `api` | `API_PASSPORT` |
| `iot` | `IOT_DEVICE` |
| `sdk` | `SDK_PASSPORT` |
| `service-workload` | `SERVICE_WORKLOAD_PASSPORT` |

There is no eighth child Passport family in this profile. Domain concepts such as robot, dataset, vehicle, critical infrastructure, policy or custody may be subjects, relationships, evidence or use-case metadata; they are not additional child type codes.

## Required fields

- `schema`: `eczid.passport-carry-card`
- `schema_version`: `1.0`
- `ecz_id`: current public parent or child ECZ-ID reference
- `passport_family`: `parent`, `agent`, `mcp`, `plugin`, `api`, `iot`, `sdk`, or `service-workload`
- `resolver_url`: canonical HTTPS human Resolver URL

Optional fields are defined by the checked-in JSON Schema.

If `parent_ecz_id` is carried for a child, it must match the parent encoded in the child ECZ-ID.

## Canonical proof pointers

URL-encode the complete ECZ-ID before placing it in a path.

Human Resolver:

```text
https://resolver.ecocitizenz.org/p/{URL-encoded ecz_id}
```

Machine proof:

```text
https://api.ecocitizenz.com/api/p/{URL-encoded ecz_id}.json
```

The legacy `/passport/{id}` route is not the current Carry-Card contract.

## Repository fixtures

The top-level fixture demonstrates Agent Passport. The other six family fixtures are under `.eczid/examples/`.

Every checked-in fixture is deliberately non-issued and carries:

```json
"extensions": { "example_fixture": true }
```

Validate fixtures only with the explicit example flag:

```bash
python scripts/validate_passport_card.py .eczid/passport-card.example.json --allow-example
```

A production card must use a legitimately issued ECZ-ID and must validate without relying on example-fixture semantics.

## Verification rule

A Carry-Card is not proof by itself.

Current lifecycle state, assurance, evidence, bindings and authority must be checked through the canonical ECZ-ID Resolver or approved machine-readable proof endpoint when a relying decision is made.

- no record / 404 = no public ECZ-ID proof found, not a danger verdict;
- unreadable Resolver = unreadable, not automatically absent;
- parent strength applies to the accountable Parent and is not automatically inherited by a child machine Passport.

## Public safety rules

- Do not put secrets or private environment data in a public card.
- Production URLs use HTTPS.
- Treat optional extension content as untrusted input.
- The card does not create VERIFIED, ASSURED, BOUND or ENFORCED state.
- Possession of a card does not mean safe, compliant, certified or approved.
- A Resolver-linked badge or reference is a pointer to proof, not proof by itself.

## Versioning

v1.x may add optional fields without breaking the required core. Corrections that align examples and validators to the already-current ECZ-ID identifier/Resolver contract do not create a new proof meaning.

A breaking required-field or Carry-Card semantic change requires a new major schema version.
