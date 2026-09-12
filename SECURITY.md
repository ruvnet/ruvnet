# Security policy

This profile repository contains documentation, inventories, provenance material, and an optional local CLI/MCP plugin in `plugins/ruvnet`. The companion is read only and has no network or shell execution tools. The separately hosted federation has its own authentication and publishing boundary.

For vulnerabilities in RuView, Ruflo, MetaHarness, RuVector, or another project, use the private security reporting mechanism in that project's repository when available. Do not publish exploitable details in this repository.

For a broken or malicious link, compromised package reference, exposed secret, or integrity issue in this profile repository, open a minimal report that avoids sensitive details and identifies the affected path. GitHub account or platform abuse should also be reported through GitHub's official reporting channels.

For the local plugin threat model and validation evidence, see [the entrypoint review](docs/entrypoint/VALIDATION.md). Report dependency or input-boundary issues without including credentials or exploitable private details.
