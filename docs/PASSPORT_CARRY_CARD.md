# ECZ-ID Passport Carry-Card v1.0

This repository includes the public interoperability profile for the ECZ-ID Passport Carry-Card.

The Carry-Card is a small pointer envelope that lets software carry an ECZ-ID reference without copying current Resolver state into the distribution asset.

## Required fields

- `schema`: `eczid.passport-carry-card`
- `schema_version`: `1.0`
- `ecz_id`: stable ECZ-ID reference
- `passport_family`: `parent`, `agent`, `mcp`, `plugin`, `api`, `iot`, `sdk`, or `service-workload`
- `resolver_url`: HTTPS Resolver proof URL

Optional fields are defined by the checked-in JSON Schema.

## Repository convention

Use:

```text
.eczid/passport-card.json
```

Reference fixtures may use:

```text
.eczid/passport-card.example.json
```

Validate locally:

```bash
python scripts/validate_passport_card.py .eczid/passport-card.json
```

Reference examples:

```bash
python scripts/validate_passport_card.py .eczid/passport-card.example.json --allow-example
```

## Verification rule

A Carry-Card is not proof by itself.

Current lifecycle state, assurance, evidence, bindings and authority must be checked through the canonical ECZ-ID Resolver or approved machine-readable proof endpoint when a relying decision is made.

## Public safety rules

- Do not put secrets or private environment data in a public card.
- Production URLs use HTTPS.
- Treat optional extension content as untrusted input.
- The card does not create VERIFIED, ASSURED, BOUND or ENFORCED state.
- Possession of a card does not mean safe, compliant, certified or approved.
- A Resolver-linked badge or reference is a pointer to proof, not proof by itself.

## Versioning

v1.x may add optional fields without breaking the required core.

A breaking required-field or semantic change requires a new major schema version.
