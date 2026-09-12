#!/usr/bin/env node
import { VERSION, discover, project, changes, plan, connect } from '../lib/core.mjs';

async function main(args) {
  const [command, ...rest] = args;
  if (!command || command === 'help' || command === '--help') {
    console.log(`RuV Stack entrypoint ${VERSION}\n\nruvnet catalog [keywords]    Discover source-linked projects\nruvnet project <id>          Inspect one project with upstream provenance\nruvnet changes [limit]       Reviewed upstream changes and evidence\nruvnet plan <goal>           Advisory MetaHarness integration plan\nruvnet connect <host>        chatgpt, claude, claude-code, lovable, codex, stdio\nruvnet mcp                   Local read-only MCP over stdio\n\nNo shell execution, repository writes, network calls or federation signing.\nHosted federation: https://x.ruv.io/mcp\nInstall: https://github.com/ruvnet/ruvnet/blob/main/docs/entrypoint/INSTALL.md`);
    return;
  }
  if (command === '--version' && !rest.length) return console.log(VERSION);
  if (command === 'mcp' && !rest.length) return (await import('../lib/mcp.mjs')).serve();
  let result;
  if (command === 'catalog') result = discover(rest.join(' '), 10);
  else if (command === 'changes' && rest.length <= 1) {
    const limit = rest.length ? Number(rest[0]) : 10;
    result = changes(limit);
  }
  else if (command === 'plan') result = plan(rest.join(' '));
  else if (command === 'project' && rest.length === 1) result = project(rest[0]);
  else if (command === 'connect' && rest.length === 1) result = connect(rest[0]);
  else throw new Error('Invalid command or arguments; run --help');
  console.log(JSON.stringify(result, null, 2));
}
main(process.argv.slice(2)).catch(error => { process.stderr.write(`${error.message}\n`); process.exitCode = 1; });
