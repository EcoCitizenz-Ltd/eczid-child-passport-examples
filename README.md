# ECZ-ID Child Passport Examples

![ECZ-ID Child Passport parent and child identity visual](https://raw.githubusercontent.com/EcoCitizenz-Ltd/.github/main/assets/repository-visuals/eczid-child-passport-examples.jpg)

## One Parent. Seven free machine-identity Passport families. Resolvable proof.

An organisation may operate many digital and physical machine surfaces. ECZ-ID separates the accountable Parent from each specific machine identity so relying parties can review the organisational anchor and the operational surface independently.

## Current launch model

The ECZ-ID launch identity model is:

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

This repository is a reference implementation for the interoperable ECZ-ID **Passport Carry-Card**.

A Carry-Card is a compact pointer envelope that can move through repositories, SDKs, plugins, packages, CI, marketplaces and services. It identifies which ECZ-ID to resolve without copying current Resolver truth into every distribution surface.

Reference files:

- [Carry-Card specification](docs/PASSPORT_CARRY_CARD.md)
- [JSON Schema](passport-card.schema.json)
- [Example Card](.eczid/passport-card.example.json)
- [Validator](scripts/validate_passport_card.py)

Validate the example:

```bash
python scripts/validate_passport_card.py .eczid/passport-card.example.json --allow-example
```

A production Card replaces the EXAMPLE ECZ-ID with an issued Passport and uses the appropriate family.

## Frictionless distribution flywheel

```text
use a useful ECZ-ID asset for free
  -> Get a free relevant Passport
  -> return to the originating asset
  -> configure the Carry-Card
  -> Verify ECZ-ID through Resolver
  -> add Resolver-linked badge/reference
  -> another developer or machine encounters it
  -> resolves current proof
  -> obtains its own relevant free Passport
  -> repeats
```

This loop does not require telemetry.

---

## Agent Passport

Use for an AI/software agent whose operator, authority, tools, dependencies and lifecycle need an independently resolvable identity.

Review questions include who operates it, which authority is delegated, what tools/systems it can reach and whether those relationships remain current.

[Agent Authority Toolkit](https://github.com/EcoCitizenz-Ltd/eczid-agent-authority-toolkit)

## MCP Passport

Use for an MCP server whose operator, server identity, exposed tools/resources and relationships need resolvable proof.

MCP Passport identity is free. MCP Trust, MCP Assurance and related services remain separate paid operating layers where applicable.

## Plugin Passport

Use for a plugin/extension/app identity, publisher relationship, permissions/backend relationship and lifecycle.

## API Passport

Use for an API identity, operator, production endpoint and machine/service dependencies.

[API Passport Starter](https://github.com/EcoCitizenz-Ltd/eczid-api-passport-starter)

## IoT Passport

Use for an IoT product/model/fleet identity and its operator/lifecycle relationships. Individual device-instance capacity is handled separately from pooled AEC.

## SDK Passport

Use for an SDK/publisher/package/repository identity and provenance/distribution relationships.

## Service & Workload Passport

Use for enduring services and workloads, including provider/cloud bindings and non-human workload identity relationships.

---

## Child identity design checklist

Before configuring a child Passport, ask:

- [ ] Which of the seven Passport families represents the operational surface?
- [ ] Who operates or owns it?
- [ ] Which Parent should it link to?
- [ ] Which evidence is appropriate to publish?
- [ ] What must remain private?
- [ ] Which authority/binding relationships matter?
- [ ] How does lifecycle state change?
- [ ] What indicates suspension, revocation, supersession or withdrawal?
- [ ] How can relying parties re-check current proof?
- [ ] Which decisions remain outside ECZ-ID?

---

## Identity is not approval

A resolvable child identity can improve accountability and evidence review.

It does not automatically mean safe, certified, compliant, approved, VERIFIED, ASSURED, BOUND or ENFORCED.

Those terms must only be used when the relevant ECZ-ID state or live control actually supports them.

---

## Public operator proof

**ECZ-ID public identity evidence — ECZ-GB-RBS1NW**

[View current public identity and evidence](https://resolver.ecocitizenz.org/passport/ECZ-GB-RBS1NW)

---

## Distribution adapters

The Carry-Card may be referenced from package metadata, OCI/container labels, website/service discovery, CI output, marketplace descriptions and compatible Agent/MCP manifests.

The adapter never becomes canonical truth. Resolver remains the re-check point.

Human-facing documentation may be localized; ECZ-IDs, JSON keys, protocol tokens, SKUs, ReasonCodes, hashes, signatures and machine states remain language-neutral.
