# ECZ-ID Child Passport Examples

![ECZ-ID Child Passport parent and child identity visual](https://raw.githubusercontent.com/EcoCitizenz-Ltd/.github/main/assets/repository-visuals/eczid-child-passport-examples.jpg)

## One organisation can operate many independently reviewable machine identities.

An organisation may operate hundreds or thousands of digital and physical machine surfaces: APIs, agents, models, datasets, software releases, devices, robots, products, vehicles, drones and infrastructure.

Representing all of those surfaces only as the organisation loses useful detail.

Representing them without a stable organisational anchor loses accountability context.

ECZ-ID uses parent/child relationships to preserve both.

## Start here

- [Business Passport & Machine Identity](https://github.com/EcoCitizenz-Ltd/eczid-business-passport-machine-identity)
- [Developer Gateway](https://developers.ecocitizenz.com?utm_source=github&utm_medium=repository&utm_campaign=child-passports&utm_content=developers)
- [Start with TrustOps](https://trustops.ecocitizenz.com/start?utm_source=github&utm_medium=repository&utm_campaign=child-passports&utm_content=start)
- [View live Resolver proof](https://resolver.ecocitizenz.org/passport/ECZ-GB-RBS1NW)

---

## The pattern

```text
Business Passport
      |
      +-- Agent
      +-- API
      +-- Software
      +-- AI Model
      +-- Dataset
      +-- IoT Device
      +-- Product
      +-- Robot / Vehicle / Drone
      +-- Infrastructure
```

Each child answers a more specific question than the parent alone.

---

## Agent identity

Review questions:

- Which organisation operates the agent?
- Which agent identity is acting?
- Which tools and systems can it reach?
- Which authority has been delegated?
- Is its operator relationship still current?

[Agent Authority Toolkit](https://github.com/EcoCitizenz-Ltd/eczid-agent-authority-toolkit)

---

## API identity

Review questions:

- Who operates the API?
- Which production API is referenced?
- Which evidence is current?
- Which agents/services depend on it?
- What is the lifecycle or incident route?

[API Passport Starter](https://github.com/EcoCitizenz-Ltd/eczid-api-passport-starter)

---

## Software identity

Review questions:

- Which software or release is identified?
- Who publishes or operates it?
- Which evidence describes the release?
- Is SBOM or provenance evidence available?
- Has lifecycle state changed?

[Software Supply Chain Evidence](https://github.com/EcoCitizenz-Ltd/eczid-software-supply-chain-evidence)

---

## AI models and datasets

A model and the dataset it depends on answer different provenance questions.

Consider:

- operator / publisher
- identity
- version
- provenance
- declared relationships
- evidence timestamp
- lifecycle
- downstream dependencies

---

## IoT and connected devices

Consider:

- device identity
- operating organisation
- deployment context
- software / firmware identity
- authority
- network/service relationships
- lifecycle state

---

## Robotics, vehicles and drones

Autonomous and semi-autonomous machines can combine:

- physical identity
- software identity
- operator identity
- delegated authority
- location/context
- lifecycle state

The machine should be reviewable without confusing it with the organisation that operates it.

---

## Infrastructure

The same pattern can apply to industrial sites, critical infrastructure, ports, rail, aviation ground operations, marine operations and telecom infrastructure.

The principle remains:

> identify the specific operational surface while retaining the accountable parent relationship.

---

## Child identity design checklist

Before introducing a new machine identity type, ask:

- [ ] What distinct object or operational surface are we identifying?
- [ ] Who operates or owns it?
- [ ] Which parent identity should it link to?
- [ ] Which evidence is appropriate to publish?
- [ ] What must remain private?
- [ ] Which authority relationships matter?
- [ ] How does lifecycle state change?
- [ ] What indicates supersession or withdrawal?
- [ ] How can relying parties re-check it?
- [ ] What decisions remain outside the identity system?

---

## Identity is not approval

A resolvable child identity can improve accountability and evidence review.

It does not automatically mean safe, certified, compliant, approved or suitable for every relying party.

---

## Public operator proof

**ECZ-ID public identity evidence - ECZ-GB-RBS1NW**
[View current public identity and evidence](https://resolver.ecocitizenz.org/passport/ECZ-GB-RBS1NW)

---

## GitHub-native agent evidence review

For supported committed agent identity manifests and references, use the specialist **ECZ-ID Agent Trust** GitHub App:

[Install ECZ-ID Agent Trust](https://github.com/marketplace/ecz-id-agent-trust)

For broader supported MCP/agent configuration review, use:

[Install ECZ-ID MCP & Agent Check](https://github.com/marketplace/ecz-id-mcp-agent-check)

A child identity should still be evaluated in the context of its parent, its evidence and the relying party's own policy.
