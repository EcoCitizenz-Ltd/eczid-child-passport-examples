# Child Passport Example Index

ECZ-ID has **seven current free machine Passport families**. This repository uses those seven families as the only child Passport taxonomy.

| Family | Current public type code | Example |
| --- | --- | --- |
| Agent | `AGENT_PASSPORT` | [Agent fixture](../.eczid/passport-card.example.json) |
| MCP | `MCP_PASSPORT` | [MCP fixture](../.eczid/examples/mcp.example.json) |
| Plugin | `PLUGIN_PASSPORT` | [Plugin fixture](../.eczid/examples/plugin.example.json) |
| API | `API_PASSPORT` | [API fixture](../.eczid/examples/api.example.json) |
| IoT | `IOT_DEVICE` | [IoT fixture](../.eczid/examples/iot.example.json) |
| SDK | `SDK_PASSPORT` | [SDK fixture](../.eczid/examples/sdk.example.json) |
| Service & Workload | `SERVICE_WORKLOAD_PASSPORT` | [Service & Workload fixture](../.eczid/examples/service-workload.example.json) |

Every checked-in identifier is a syntactically current **non-issued fixture**. It demonstrates the contract only and is not Resolver proof.

## Subjects and use cases are not extra Passport families

A current Passport may describe or relate to many real-world subjects and operating contexts. Examples include:

- AI models or datasets used by an Agent, API, SDK, Service or Workload;
- drones, robots, vehicles or industrial equipment represented through the appropriate IoT / Service & Workload / Agent context;
- software supply-chain packages represented through Plugin, SDK, API or Service & Workload identities;
- critical infrastructure, ports, rail, aviation, marine or telecom environments in which those machine identities operate;
- custody, financial authority, policy or operational relationships recorded as evidence/authority context rather than invented Passport families.

Those concepts may be useful **subject metadata, evidence, bindings, relationships, use cases or sector profiles**. They are not additional child Passport families and must not be encoded as catalogue-era ECZ-ID child type codes.

## Rule for new examples

Add an example only when it:

1. maps to one of the seven current Passport families;
2. uses the current parent/child identifier grammar;
3. uses canonical Resolver proof pointers;
4. is clearly marked non-issued unless it contains a legitimately issued ECZ-ID;
5. does not imply safety, certification, compliance, approval or inherited Parent assurance.
