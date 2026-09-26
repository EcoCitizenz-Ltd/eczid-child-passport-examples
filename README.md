# ECZ-ID Child Passport Examples

![ECZ-ID Child Passport parent and child identity visual](https://raw.githubusercontent.com/EcoCitizenz-Ltd/.github/main/assets/repository-visuals/eczid-child-passport-examples.jpg)

## One Parent. Seven free machine-identity Passport families. Resolvable proof.

An organisation may operate many digital and physical machine surfaces. ECZ-ID separates the accountable Parent from each specific machine identity so relying parties can review the organisational anchor and the operational surface independently.

## Current launch model

```text
Parent Passport
      |
      +-- Agent Passport
      +-- MCP Passport
      +-- Plugin Passport
      +-- API Passport
      +-- IoT Passport
      +-- SDK Passport
      +-- Service & Workload Passport
```

All seven child Passport identities are free.

Paid products add assurance, authority, monitoring, evidence, capacity, tooling and professional services. They do **not** turn the child Passport identity into a paid product.

## Start here

- [Get a free Passport](https://trustops.ecocitizenz.com/start?utm_source=github&utm_medium=repository&utm_campaign=child-passports&utm_content=get-free-passport)
- [Developer Gateway](https://developers.ecocitizenz.com?utm_source=github&utm_medium=repository&utm_campaign=child-passports&utm_content=developers)
- [View live Resolver proof](https://resolver.ecocitizenz.org/passport/ECZ-GB-RBS1NW)

---

## Passport Carry-Card v1.0

This repository provides a public reference implementation of the ECZ-ID **Passport Carry-Card** interoperability profile.

Reference files:

- [Public interoperability guide](docs/PASSPORT_CARRY_CARD.md)
- [JSON Schema](passport-card.schema.json)
- [Example Card](.eczid/passport-card.example.json)
- [Validator](scripts/validate_passport_card.py)

Validate the example:

```bash
python scripts/validate_passport_card.py .eczid/passport-card.example.json --allow-example
```

A production Card replaces the EXAMPLE ECZ-ID with an issued Passport and uses the appropriate family. Current proof must be re-checked through Resolver.

---

## Passport families

**Agent Passport** — agent identity and accountable operator/authority context.

**MCP Passport** — MCP server identity and operator/tool relationship context.

**Plugin Passport** — plugin/extension/app identity and publisher relationship.

**API Passport** — API identity, operator and endpoint/dependency context.

**IoT Passport** — IoT product/model/fleet identity and lifecycle relationship.

**SDK Passport** — SDK/publisher/package/repository identity and provenance relationship.

**Service & Workload Passport** — enduring service/workload identity and provider/cloud relationship.

---

## Identity is not approval

A resolvable child identity can improve accountability and evidence review.

It does not automatically mean safe, certified, compliant, approved, VERIFIED, ASSURED, BOUND or ENFORCED.

[View current public identity and evidence](https://resolver.ecocitizenz.org/passport/ECZ-GB-RBS1NW)
