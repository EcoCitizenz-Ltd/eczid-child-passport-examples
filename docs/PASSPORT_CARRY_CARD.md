# ECZ-ID Passport Carry-Card v1.0

The Passport Carry-Card is a small, interoperable pointer envelope for carrying an ECZ-ID through repositories, packages, SDKs, plugins, services, CI and marketplaces.

It is deliberately **not** a copy of Resolver truth.

## Core rule

A card tells another tool **what ECZ-ID to resolve and where to resolve it**.

Current lifecycle state, assurance, evidence, bindings and authority must be re-checked from ECZ-ID canonical proof when a relying decision is made.

## Required fields

- `schema`: `eczid.passport-carry-card`
- `schema_version`: `1.0`
- `ecz_id`: stable ECZ-ID reference
- `passport_family`: `parent`, `agent`, `mcp`, `plugin`, `api`, `iot`, `sdk`, or `service-workload`
- `resolver_url`: HTTPS Resolver proof URL

Optional pointers include `machine_proof_url`, `parent_ecz_id`, `subject_url`, `badge_url`, `acquisition_url`, `source` and namespaced `extensions`.

## Repository convention

Use:

```text
.eczid/passport-card.json
```

A reference fixture may use `.eczid/passport-card.example.json` until a real child Passport has been issued.

Validate locally:

```bash
python scripts/validate_passport_card.py .eczid/passport-card.json
```

Reference examples use:

```bash
python scripts/validate_passport_card.py .eczid/passport-card.example.json --allow-example
```

## Frictionless flywheel

1. Use the asset for free without an ECZ-ID account.
2. If no Passport is configured, choose **Get a free [family] Passport**.
3. Acquisition opens with the relevant family/source context instead of forcing catalogue discovery.
4. After issuance, return to the originating asset.
5. Create/configure the local Carry-Card.
6. **Verify ECZ-ID** resolves current proof.
7. Add the Resolver-linked badge/reference to README, package, site, service, CI or marketplace listing.
8. Another developer or machine encounters that proof and can resolve it immediately.
9. That relying party can obtain its own relevant free Passport.
10. Paid capabilities appear only when they solve a contextual operating need.

No telemetry is required for this loop.

## Safety and truth boundaries

- The card does not mean safe, trusted, compliant, certified or approved.
- It does not create VERIFIED, ASSURED, BOUND or ENFORCED state.
- Payment or possession of a card is not proof.
- Do not put secrets or private environment data in a public card.
- Production card URLs use HTTPS.
- Treat extension content as untrusted.
- A badge is a doorway to Resolver proof, not proof by itself.

## Adapters

The same logical card can be referenced from package metadata, OCI labels, marketplace descriptions, HTML/service discovery, CI output and compatible Agent/MCP manifests.

Adapters should point to the card or Resolver rather than inventing a second ECZ-ID schema.

## Versioning

v1.x may add optional fields without breaking the required core.

A breaking required-field or semantic change requires a new major schema version.
