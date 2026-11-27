# Constellation adoption architecture

The constellation grows through useful integrations, not synthetic clone or star activity.

## Four supported paths

1. **Scaffold:** offer explicit opt-in commands to clone satellite starter projects. Never silently clone repositories during installation.
2. **Workspace:** keep tightly coupled packages in pnpm or Cargo workspaces when their release and ownership boundaries match. Do not merge unrelated repositories just to inflate clone coverage.
3. **Compatibility CI:** run a bounded, read-only matrix against pinned satellite commits or reviewed release tags. Report real test outcomes; avoid workflows whose only purpose is to trigger activity.
4. **Discoverability:** link to satellite documentation, examples, and contribution guides from anchor READMEs.

## Starter examples

Clone a satellite deliberately:

```bash
git clone https://github.com/ruvnet/ruv-FANN.git
cd ruv-FANN
```

Or create a repository from a GitHub template after a maintainer explicitly enables template status:

```bash
gh repo create my-constellation-app --template OWNER/REVIEWED-TEMPLATE --private --clone
```

The template name above is a placeholder, not a published repository.

## Compatibility contract

* Use the minimum GitHub token permissions: `contents: read`.
* Pin checkout actions and dependencies to reviewed SHAs before promoting the workflow to required status.
* Matrix targets must be explicit and reviewed, not dynamically populated from untrusted pull request input.
* Run cheap structural checks on PRs; execute integration tests only where a documented command exists.
* No secrets or write tokens in satellite checkout jobs.
* Treat satellite code as untrusted. Never execute arbitrary scripts from a fork with privileged credentials.
* Publish tested ref, command, duration, result, and artifact links.
* Set concurrency limits and timeouts to bound CI spending.

## Measurement

Track weekly: README referral clicks (where measurable), CLI scaffold invocations (opt-in telemetry only), distinct contributing authors, successful integration runs, downstream issues resolved, and adoption of documented examples.

GitHub does not attribute satellite clone traffic to an anchor checkout. GitHub stars require individual user action. npm download events are not equivalent to distinct users.

## Promotion gate

Promote an integration only when a real end-to-end example passes against a pinned satellite ref and its test command. Revert on failing compatibility checks or unexpected permissions.
