import fs from 'node:fs';
const home = 'taste-native/';
const copy = JSON.parse(fs.readFileSync(home+'copy-lint.json', 'utf8'));
const gate = fs.readFileSync(home+'gate.log','utf8');
const code = Number(fs.readFileSync(home+'gate-exit-code.txt', 'utf8'));
const last = gate.split(/\r?\n/).filter(x=>/^GATE: /.test(x)).at(-1) || '';
if (!Array.isArray(copy.files) || !copy.files.length) throw Error('Original copy-lint emitted no valid files');
if (!/^GATE: (FAIL|OPEN)\b/.test(last) || code!==1) throw Error('Original gate did not detect the intentionally flawed page: '+last);
if (/GATE: (ERROR|SETUP)/.test(gate)) throw Error('Original checker failed instead of detecting flaws');
const report = {
  upstream: 'Leonxlnx/taste-skill',
  original: true,
  native_node_chrome: true,
  pinned_commit: process.env.TASTE_PINNED_COMMIT,
  gate_exit_code: code,
  gate_verdict: last,
  copy_lint_files: copy.files.length,
  intended_fixture: 'public synthetic intentionally flawed page',
  workflow_runner: process.env.RUNNER_OS || 'unknown',
  timestamp: new Date().toISOString()
};
fs.writeFileSync(home+'native-result.json',JSON.stringify(report,null,2)+'\n');
console.log('PASS: original gate and original copy lint actually executed and found deliberate defects');
