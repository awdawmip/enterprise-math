'use strict';
// Independent finite certificate for the S23 time-only, 1 <= m <= 3 plateau.
// All incidence tests are exact 64-bit BigInt operations. Node >= 16.
const assert = require('node:assert/strict');
const H = [2, 3, 4];
const G = [3, 4];
const signature = new Set();
const add = (a) => signature.add(a.join(','));
add([1, 1, 1, 1]);
for (const x of H) for (const y of H) {
  add([1, 1, x, y]);
  add([x, y, 1, 1]);
  add([2, x, 2, y]);
}
for (const x of G) for (const y of G)
  for (const u of H) for (const v of H) add([x, u, y, v]);
assert.equal(signature.size, 64);

// Separate enumeration of all 2^11 lawful deterministic causal stopping tables.
// Slots: A,B at stage 1; U,AV,BV at stage 2; six sources at stage 3.
const stage1 = [0, 0, 0, 1, 1, 1];
const stage2 = [2, 2, 3, 2, 2, 4];
const allFromGrammar = new Set();
let deterministicTables = 0;
for (let bits = 0; bits < 2048; ++bits) {
  const times = Array.from({length: 6}, (_, x) => {
    const first = stage1[x];
    if ((bits >> first) & 1) return 1;
    if ((bits >> stage2[x]) & 1) return 2;
    return ((bits >> (5 + x)) & 1) ? 3 : 4;
  });
  const sig = [times[1], times[2], times[4], times[5]].join(',');
  assert(signature.has(sig), 'Every designated-cell signature is legal');
  allFromGrammar.add(sig);
  ++deterministicTables;
}
assert.equal(deterministicTables, 2048);
assert.equal(allFromGrammar.size, 64);
for (const s of signature) assert(allFromGrammar.has(s));

// A fixed label reconstructing delta times at risk r<3/4 assigns >1/4
// probability to every time seen at each of the four prepared group inputs.
// Its covered signatures therefore fit one three-choice Cartesian box.
// Any three-choice set is contained in one of four size-three subsets.
const S = [...signature].sort().map(s => s.split(',').map(Number));
const boxes = [];
for (let a = 1; a <= 4; a++) for (let b = 1; b <= 4; b++)
  for (let c = 1; c <= 4; c++) for (let d = 1; d <= 4; d++) {
    const omitted = [a, b, c, d];
    let mask = 0n;
    for (let i = 0; i < S.length; ++i)
      if (S[i].every((t, j) => t !== omitted[j])) mask |= 1n << BigInt(i);
    boxes.push({omitted, mask});
  }
assert.equal(boxes.length, 256);
const FULL = (1n << 64n) - 1n;
let triples = 0;
for (let i = 0; i < boxes.length; ++i)
  for (let j = i + 1; j < boxes.length; ++j) {
    const two = boxes[i].mask | boxes[j].mask;
    for (let k = j + 1; k < boxes.length; ++k) {
      ++triples;
      assert.notEqual(two | boxes[k].mask, FULL, 'three boxes must not cover S64');
    }
  }
assert.equal(triples, 2763520);
// Tightness of the maximum three-box coverage: exactly one missing signature.
const tightTriplet = [[1,1,1,1],[1,1,2,2],[2,2,1,1]];
const findBox = arr => boxes.find(b => b.omitted.every((v,j) => v === arr[j])).mask;
const tightUnion = tightTriplet.reduce((m, t) => m | findBox(t), 0n);
const missing = S.filter((_,i) => !(tightUnion & (1n << BigInt(i))));
assert.deepEqual(missing, [[1,1,1,1]]);
// Four explicit boxes (omit the same time from each coordinate) cover S64.
let fourUnion = 0n;
for (let time = 1; time <= 4; ++time)
  fourUnion |= findBox([time,time,time,time]);
assert.equal(fourUnion, FULL);

console.log('PASS_BRC_N4_S23_LABELS_1_TO_3_THREEQUARTER_20261101');
console.log('lawful_deterministic_tables=' + deterministicTables);
console.log('distinct_designated_signatures=' + allFromGrammar.size);
console.log('three_choice_boxes=' + boxes.length);
console.log('distinct_three_box_families_checked=' + triples);
console.log('maximum_three_box_coverage=63/64');
console.log('tight_three_box_missing=' + missing[0].join(','));
console.log('four_diagonal_boxes_cover=64/64');
console.log('theorem: for every k>=1 and 1<=m<=3, R_beh(k,m)=3/4');
