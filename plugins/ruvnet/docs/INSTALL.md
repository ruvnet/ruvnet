# Enter the world of ruvnet

One entry point for stack discovery, federation and repository-specific harnesses.

[Explore the federation](https://x.ruv.io) · [RuFlo federation dashboard](https://ruflo-federation.ruv.chatgpt.site/) · [MetaHarness Studio](https://ruvnet.github.io/metaharness/)

## Claude Code: install the plugin

```text
/plugin marketplace add ruvnet/ruvnet
/plugin install ruvnet@ruvnet
```

Then ask: **Use the ruvnet-start skill to choose the smallest RuV Stack for my project.**

The plugin contains four skills and configures the hosted federation MCP connector. Follow the host's OAuth flow when requested. Restart or reload the plugin if the host has not discovered its skills. The optional local CLI/MCP companion below requires a separate dependency install; plugin installation does not run an npm hook.

Source: [Claude Code marketplace installation](https://code.claude.com/docs/en/plugin-marketplaces). This is a community repository marketplace, not a claim of inclusion in an official vendor directory.

## ChatGPT, Claude chat and Lovable

Add this remote MCP URL through the host's custom connector flow:

```text
https://x.ruv.io/mcp
```

| Host | Connection | Verify |
| --- | --- | --- |
| ChatGPT | Create a custom MCP app using the supported developer/plugin flow; choose OAuth and complete consent. Availability depends on the workspace. | Ask the connector to list federation channels, then read `pub:showcase`. |
| Claude chat | Add a custom connector with the MCP URL and authorize. | List channels and read one public channel. |
| Lovable | Open Connectors, choose MCP server, enter the URL, then Add & authorize. | Ask Lovable to read a public federation channel as build context. |

Keep write approvals enabled. OAuth does not turn a gateway signature into a personal Nostr signature. The gateway's public publishing tools require `swarm:publish`; personal signing uses the user's local key. Private traffic cannot be decrypted by the gateway.

Host sources: [ChatGPT developer mode](https://developers.openai.com/api/docs/guides/developer-mode), [Claude remote connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp), [Lovable custom MCP](https://docs.lovable.dev/integrations/custom-mcp).

A remote connection exposes the federation's existing tools. It does **not** upload these local skills or add `ruvnet_*` discovery tools to x.ruv.io. Use a supported skill/plugin import for host-native guidance. Lovable chat connectors provide build context, not runtime connectivity for a published application. No hosted service is deployed by this repository change.

## Local CLI and MCP companion

Requires Node.js 22 or newer. Review the source, then clone and install the locked dependencies without lifecycle scripts:

```bash
git clone https://github.com/ruvnet/ruvnet.git
cd ruvnet/plugins/ruvnet
npm ci --ignore-scripts
node bin/ruvnet.mjs catalog memory
node bin/ruvnet.mjs changes 5
node bin/ruvnet.mjs plan "Build a repository harness with persistent memory"
node bin/ruvnet.mjs connect chatgpt
```

For a reproducible rollout, check out the reviewed commit before `npm ci`; the lockfile pins dependencies but not your Git checkout. The package is currently private and source-installed. Do not use `npx @ruvnet/entrypoint` as though it were published to npm.

Generate a host-ready local stdio configuration with absolute paths:

```bash
node bin/ruvnet.mjs connect stdio
```

Copy the returned `config.mcpServers.ruvnet-guide` object into a host that supports local stdio servers, merging it with existing servers rather than overwriting the whole configuration. Start command: `node /absolute/path/to/ruvnet/plugins/ruvnet/bin/ruvnet.mjs mcp`.

| Local tool | Effect |
| --- | --- |
| `ruvnet_discover` | Search the dated catalog by exact keyword overlap. |
| `ruvnet_project` | Read a project, source links and its maturity boundary. |
| `ruvnet_changes` | Read the reviewed upstream snapshot with exact revisions and evidence links. |
| `ruvnet_plan` | Return an advisory SPARC/MetaHarness plan, without executing it. |
| `ruvnet_connect` | Return connection guidance; it does not change configuration. |

Resources: `ruv://catalog`, `ruv://changes`, `ruv://federation`. Prompt: `ruvnet-start` with a `goal` argument. The local process has no HTTP listener, network tools, shell execution or mutable memory. The changes resource is a reviewed snapshot rather than a live feed. A remote-only host cannot connect directly to local stdio.

## Codex repository marketplace

This repository also contains `.agents/plugins/marketplace.json` and a validated `.codex-plugin/plugin.json`. The Codex scaffold uses the catalog name `personal`; the separate Claude catalog is named `ruvnet`. Do not interchange the two schemas.

In a Codex build supporting repository marketplaces, add the cloned marketplace root:

```bash
codex plugin marketplace add /absolute/path/to/ruvnet
```

Then select the **RuV Stack / ruvnet** plugin from that marketplace in the host. This command was not exercised in the validation environment because the Codex CLI was unavailable. If another `personal` marketplace conflicts, use the direct skill or stdio route instead of overwriting an existing catalog. Administrators may need to import/publish a plugin before workspace use. GitHub publication is not vendor directory publication.

## Skills only

The portable skill folders are in `plugins/ruvnet/skills/`. Keep the plugin folder intact because skills reference its catalog and installation guide. Import that folder with the host's supported skill/plugin flow; copying only `SKILL.md` loses its references. The four skills are `ruvnet-start`, `ruvnet-federation`, `ruvnet-metaharness`, and `ruvnet-memory`.

## MetaHarness and evolution

Use the MetaHarness skill or `ruvnet plan` to define scope, budget, tests and rollback. Upstream documents these starting points:

```bash
npx metaharness score <repo>
npx metaharness my-bot --template vertical:coding --host claude-code
```

These are upstream command templates, not commands executed by this package. Confirm current help and pin a reviewed version before automation. Inspect generated files in isolation, then run the target's tests, security checks and held-out evaluations. Promotion requires measured improvement, no unacceptable regression, budget compliance and rollback. [MetaHarness guide](https://github.com/ruvnet/metaharness/blob/main/docs/USERGUIDE.md).

## Validate and remove

```bash
npm run check
npm audit
```

Acceptance: the official MCP SDK client can initialize the local server, call all four tools, read both resources and get the prompt; unknown paths and write-like arguments fail. For remote acceptance, list channels and read one; do not publish a test message without authorization.

To remove, uninstall the plugin through your host and remove only the `ruvnet-guide` local server entry. Revoke the federation OAuth grant if it is no longer needed. Removing a local plugin is not the same as revoking OAuth or deleting a personal Nostr key.
