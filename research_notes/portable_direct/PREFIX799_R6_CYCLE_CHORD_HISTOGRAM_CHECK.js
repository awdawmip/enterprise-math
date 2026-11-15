'use strict';
// PREFIX-799: exact finite verification for a cycle-chord parametrization of bounded integer source fibers.
// Node.js >= 18, no dependencies, integer Number arithmetic only (test inputs and outputs remain < 2^53).
const counters = { capacity_patterns: 0, fibers: 0, enumerated_tables: 0, accepted_chord_candidates: 0, tested_chord_candidates: 0, histogram_checks: 0, forest_opt_checks: 0, assertions: 0 };
function ok(cond, label) { counters.assertions++; if (!cond) throw Error('ASSERT_FAIL: ' + label); }
function dsu(n) {
  const p = Array.from({ length: n }, (_, i) => i);
  function root(i) { while (p[i] !== i) { p[i] = p[p[i]]; i = p[i]; } return i; }
  return { root, join(a, b) { a = root(a); b = root(b); if (a === b) return false; p[b] = a; return true; } };
}
function forest(b, c, K, sortHigh = true) {
  const es = K.map((v, i) => ({ v, i, a: Math.floor(i / c), z: b + i % c })).filter(e => e.v > 0);
  const uf = dsu(b + c), tree = [], chords = [];
  const sorted = es.slice().sort((x, y) => sortHigh ? y.v - x.v || x.i - y.i : x.i - y.i);
  for (const e of sorted) (uf.join(e.a, e.z) ? tree : chords).push(e.i);
  tree.sort((x, y) => x - y); chords.sort((x, y) => x - y);
  const rank = tree.length;
  return { tree, chords, rank, edges: es };
}
function treeCompletion(b, c, K, m, tree, chordValues) {
  const n = b + c, x = Array(K.length).fill(0), rem = m.slice(), adj = Array.from({ length: n }, () => []), active = new Set(tree);
  const endpoint = e => [Math.floor(e / c), b + e % c];
  for (const [e, v] of chordValues) { x[e] = v; const [a, z] = endpoint(e); rem[a] -= v; rem[z] -= v; }
  for (const e of tree) { const [a, z] = endpoint(e); adj[a].push(e); adj[z].push(e); }
  const degree = adj.map(edges => edges.length), queue = [];
  for (let v = 0; v < n; v++) if (degree[v] === 1) queue.push(v);
  for (let head = 0; head < queue.length; head++) {
    const v = queue[head]; if (degree[v] !== 1) continue;
    const e = adj[v].find(t => active.has(t));
    if (e === undefined) throw Error('leaf bookkeeping');
    const [a, z] = endpoint(e), u = a === v ? z : a;
    x[e] = rem[v]; rem[u] -= x[e]; rem[v] = 0;
    active.delete(e); degree[v]--; degree[u]--;
    if (degree[u] === 1) queue.push(u);
  }
  if (active.size !== 0 || rem.some(x => x !== 0)) return null;
  if (x.some((v, e) => v < 0 || v > K[e])) return null;
  return x;
}
function enumerateBox(K, fn) {
  const x = Array(K.length).fill(0);
  function rec(j) { if (j === K.length) return fn(x.slice()); for (let v = 0; v <= K[j]; v++) { x[j] = v; rec(j + 1); } }
  rec(0);
}
function margins(b, c, x) {
  const m = Array(b + c).fill(0);
  for (let e = 0; e < x.length; e++) { m[Math.floor(e / c)] += x[e]; m[b + e % c] += x[e]; }
  return m;
}
function weightedKey(x) {
  let a = 0, b = 0;
  for (let i = 0; i < x.length; i++) { a += x[i] * ((i * 5 + 3) % 11 - 5); b += x[i] * ((i * 7 + 1) % 13 - 6); }
  return a + ',' + b;
}
function add(hist, key) { hist.set(key, (hist.get(key) || 0) + 1); }
function histOf(tables) { const h = new Map(); for (const x of tables) add(h, weightedKey(x)); return [...h].sort((a, b) => a[0].localeCompare(b[0])); }
function enumerateChord(b, c, K, m, T) {
  const vals = new Map(), accepted = [];
  function visit(i) {
    if (i === T.chords.length) {
      counters.tested_chord_candidates++;
      const x = treeCompletion(b, c, K, m, T.tree, vals);
      if (x !== null) { counters.accepted_chord_candidates++; accepted.push(x); }
      return;
    }
    const e = T.chords[i]; for (let v = 0; v <= K[e]; v++) { vals.set(e, v); visit(i + 1); } vals.delete(e);
  }
  visit(0); return accepted;
}
function exhaustiveOptimality(b, c, K, chosen) {
  const es = chosen.edges, n = b + c, target = chosen.rank;
  let best = Infinity;
  for (let mask = 0; mask < (1 << es.length); mask++) {
    let cnt = 0; for (let i = 0; i < es.length; i++) cnt += (mask >> i) & 1;
    if (cnt !== target) continue;
    const uf = dsu(n); let valid = true, bound = 1;
    for (let i = 0; i < es.length; i++) {
      const e = es[i]; if ((mask >> i) & 1) { if (!uf.join(e.a, e.z)) { valid = false; break; } }
      else bound *= e.v + 1;
    }
    if (valid && bound < best) best = bound;
  }
  const actual = chosen.chords.reduce((p, e) => p * (K[e] + 1), 1);
  ok(best === actual, 'maximum-capacity forest minimizes chord-box product');
  counters.forest_opt_checks++;
}
function checkGrid(b, c, maxK) {
  const K = Array(b * c).fill(0);
  function runPattern(i) {
    if (i < K.length) { for (let k = 0; k <= maxK; k++) { K[i] = k; runPattern(i + 1); } return; }
    counters.capacity_patterns++;
    const T = forest(b, c, K); exhaustiveOptimality(b, c, K, T);
    const groups = new Map();
    enumerateBox(K, x => { const key = margins(b, c, x).join(','); if (!groups.has(key)) groups.set(key, []); groups.get(key).push(x); counters.enumerated_tables++; });
    for (const [key, direct] of groups) {
      counters.fibers++;
      const got = enumerateChord(b, c, K, key.split(',').map(Number), T);
      ok(got.length === direct.length, 'fiber size');
      const a = direct.map(x => x.join(',')).sort(), z = got.map(x => x.join(',')).sort();
      ok(JSON.stringify(a) === JSON.stringify(z), 'full source table fiber equivalence');
      ok(JSON.stringify(histOf(direct)) === JSON.stringify(histOf(got)), 'joint weighted histogram equality');
      counters.histogram_checks++;
    }
  }
  runPattern(0);
}
checkGrid(2, 2, 2);
checkGrid(2, 3, 2);
checkGrid(3, 3, 1);
console.log(JSON.stringify({ schema:'PREFIX799_R6_CYCLE_CHORD_HISTOGRAM_RESULTS_V1', status:'ALL_CHECKS_PASS', arithmetic:'exact safe integers in declared finite tested range', scopes:['all K in {0,1,2}^(2x2), every feasible margin fiber','all K in {0,1,2}^(2x3), every feasible margin fiber','all K in {0,1}^(3x3), every feasible margin fiber'], ...counters }, null, 2));
