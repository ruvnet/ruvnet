#!/usr/bin/env node
import { VERSION, discover, project, changes, searchChanges, plan, connect } from '../lib/core.mjs';

async function main(args) {
  const [command, ...rest] = args;
  if (!command || command === 'help' || command === '--help') {
    console.log(`RuV Stack entrypoint ${VERSION}\n\nruvnet catalog [keywords]                                         Discover source-linked projects\nruvnet project <id>                                               Inspect one project with upstream provenance\nruvnet changes [limit] [project] [kind] [cursor] [snapshot-id]    Page one reviewed snapshot\nruvnet search [limit] [--min-raw-relevance 0..1] <keywords...>    Search reviewed changes by exact token overlap\nruvnet plan <goal>                                                Advisory MetaHarness integration plan\nruvnet connect <host>                                             chatgpt, claude, claude-code, lovable, codex, stdio\nruvnet mcp                                                        Local read-only MCP over stdio\n\nNo shell execution, repository writes, network calls or federation signing.\nHosted federation: ChatGPT https://x.ruv.io/chatgpt/mcp · other hosts https://x.ruv.io/mcp\nInstall: https://github.com/ruvnet/ruvnet/blob/main/docs/entrypoint/INSTALL.md`);
    return;
  }
  if (command === '--version' && !rest.length) return console.log(VERSION);
  if (command === 'mcp' && !rest.length) return (await import('../lib/mcp.mjs')).serve();
  let result;
  if (command === 'catalog') result = discover(rest.join(' '), 10);
  else if (command === 'changes' && rest.length <= 5) {
    const limit = rest.length ? Number(rest[0]) : 10;
    result = changes(limit, Date.now(), { ...(rest[1] === undefined ? {} : { project: rest[1] }), ...(rest[2] === undefined ? {} : { kind: rest[2] }) }, rest[3], rest[4]);
  }
  else if (command === 'search') {
    const parts = [...rest];
    const limit = /^\d+$/.test(parts[0] || '') ? Number(parts.shift()) : 10;
    const gateIndex = parts.indexOf('--min-raw-relevance');
    let minRawRelevance = 0;
    if (gateIndex !== -1) {
      if (parts.indexOf('--min-raw-relevance', gateIndex + 1) !== -1 || gateIndex + 1 >= parts.length) throw new Error('Invalid search threshold arguments');
      minRawRelevance = Number(parts[gateIndex + 1]);
      parts.splice(gateIndex, 2);
    }
    result = searchChanges(parts.join(' '), limit, {}, Date.now(), minRawRelevance);
  }
  else if (command === 'plan') result = plan(rest.join(' '));
  else if (command === 'project' && rest.length === 1) result = project(rest[0]);
  else if (command === 'connect' && rest.length === 1) result = connect(rest[0]);
  else throw new Error('Invalid command or arguments; run --help');
  console.log(JSON.stringify(result, null, 2));
}
main(process.argv.slice(2)).catch(error => { process.stderr.write(`${error.message}\n`); process.exitCode = 1; });
