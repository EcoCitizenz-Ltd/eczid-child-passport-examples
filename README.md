# ECZ-ID Child Passport Examples

![ECZ-ID Child Passport parent and child identity visual](https://raw.githubusercontent.com/EcoCitizenz-Ltd/.github/main/assets/repository-visuals/eczid-child-passport-examples.jpg)

## One Parent. Seven free machine-identity Passport families. Resolvable proof.

An organisation may operate many digital and physical machine surfaces. ECZ-ID separates the accountable Parent from each specific machine identity so relying parties can review the organisational anchor and the operational surface independently.

## Current launch model

```text
Parent Passport
      |
      +-- Agent Passport               AGENT_PASSPORT
      +-- MCP Passport                 MCP_PASSPORT
      +-- Plugin Passport              PLUGIN_PASSPORT
      +-- API Passport                 API_PASSPORT
      +-- IoT Passport                 IOT_DEVICE
      +-- SDK Passport                 SDK_PASSPORT
      +-- Service & Workload Passport  SERVICE_WORKLOAD_PASSPORT
```

All seven child Passport identities are free.

Paid products add assurance, authority, monitoring, evidence, capacity, tooling and professional services. They do **not** turn the child Passport identity into a paid product, and Parent strength is not automatically inherited by a child machine Passport.

## Start here

- [Get a free Passport](https://trustops.ecocitizenz.com/start?utm_source=github&utm_medium=repository&utm_campaign=child-passports&utm_content=get-free-passport&ecz_source=github&ecz_surface=eczid-child-passport-examples&intent=free-passport)
- [Developer Gateway](https://developers.ecocitizenz.com?utm_source=github&utm_medium=repository&utm_campaign=child-passports&utm_content=developers&ecz_source=github&ecz_surface=eczid-child-passport-examples)
- [View EcoCitizenz's current public Resolver record](https://resolver.ecocitizenz.org/p/ECZ-GB-RBS1NW)

---

## Passport Carry-Card v1.0

This repository provides a public reference implementation of the ECZ-ID **Passport Carry-Card** interoperability profile.

Reference files:

- [Public interoperability guide](docs/PASSPORT_CARRY_CARD.md)
- [JSON Schema](passport-card.schema.json)
- [Agent example](.eczid/passport-card.example.json)
- [Other six family examples](.eczid/examples/)
- [Validator](scripts/validate_passport_card.py)
- [Regression tests](scripts/test_validate_passport_card.py)

Validate the Agent fixture:

```bash
python scripts/validate_passport_card.py .eczid/passport-card.example.json --allow-example
```

Run the full contract regression suite:

```bash
python -m unittest scripts/test_validate_passport_card.py
```

Every checked-in ECZ-ID is a **syntactically current but deliberately non-issued fixture**. The example flag is required precisely so a fixture cannot be mistaken for production proof.

Current proof must always be re-checked through Resolver.

---

## Current child identifier grammar

```text
{parent_ecz_id}::{CURRENT_TYPE_CODE}-XXXXXX
```

Example shape only:

```text
ECZ-ZZ-EXAMPL::AGENT_PASSPORT-A1B2C3
```

The example above is not issued.

Canonical proof pointers URL-encode the complete identifier:

```text
Human:   https://resolver.ecocitizenz.org/p/{URL-encoded ecz_id}
Machine: https://api.ecocitizenz.com/api/p/{URL-encoded ecz_id}.json
```

Historical catalogue-era child codes are not current Passport family identifiers.

---

## Passport families

**Agent Passport** — agent identity and accountable operator/authority context.

**MCP Passport** — MCP server identity and operator/tool relationship context.

**Plugin Passport** — plugin/extension/app identity and publisher relationship.

**API Passport** — API identity, operator and endpoint/dependency context.

**IoT Passport** — IoT product/model/fleet identity and lifecycle relationship.

**SDK Passport** — SDK/publisher/package/repository identity and provenance relationship.

**Service & Workload Passport** — enduring service/workload identity and provider/cloud relationship. A container image, pod, replica, process or region is not automatically a separate Passport.

See [the example index](examples/README.md) for how other domain concepts map to these seven families without inventing extra Passport types.

---

## Identity is not approval

A resolvable child identity can improve accountability and evidence review.

It does not automatically mean safe, certified, compliant, approved, VERIFIED, ASSURED, BOUND or ENFORCED.

A missing public record is not automatically unsafe or untrusted; an unreadable Resolver is not silently converted into absence.

[View current public identity and evidence](https://resolver.ecocitizenz.org/p/ECZ-GB-RBS1NW)
