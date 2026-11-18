'use strict';

// The proof over the integers is in anchored.md. This program independently
// checks the named transport and the dimension of the quotient over F_2.
const assert = require('node:assert/strict');
const axes = [0, 1, 2, 3, 4, 5];
const anchor = 5;

function combinations(items, size) {
  if (size === 0) return [[]];
  return items.flatMap((item, index) =>
    combinations(items.slice(index + 1), size - 1).map(tail => [item, ...tail]));
}
function support(labels) {
  return labels.reduce((mask, label) => mask | (1 << label), 0);
}
function endFrame(route) {
  let slots = route[0].slice();
  for (const target of [...route.slice(1), route[0]]) {
    const entering = target.filter(axis => !slots.includes(axis));
    assert.equal(entering.length, 1);
    slots = slots.map(axis => target.includes(axis) ? axis : entering[0]);
  }
  return slots;
}

const bottom = combinations(axes, 2).map(support);
const top = combinations(axes, 3).map(support);
const edges = [];
const edgeIndices = new Map();
const neighbors = new Map([...bottom, ...top].map(mask => [mask, []]));
function edgeKey(triple, pair) { return triple * 64 + pair; }
for (const triple of top) {
  for (const pair of bottom) {
    if ((triple & pair) !== pair) continue;
    const index = edges.length;
    edges.push([triple, pair]);
    edgeIndices.set(edgeKey(triple, pair), index);
    neighbors.get(triple).push([pair, index]);
    neighbors.get(pair).push([triple, index]);
  }
}
function bit(index) { return 1n << BigInt(index); }
const queue = [top[0]];
const treePaths = new Map([[top[0], 0n]]);
const treeEdges = new Set();
for (let cursor = 0; cursor < queue.length; cursor++) {
  const vertex = queue[cursor];
  for (const [other, edge] of neighbors.get(vertex)) {
    if (treePaths.has(other)) continue;
    treeEdges.add(edge);
    treePaths.set(other, treePaths.get(vertex) ^ bit(edge));
    queue.push(other);
  }
}
const chords = edges.map((_, index) => index).filter(index => !treeEdges.has(index));
const cycles = chords.map(edge => {
  const [upper, lower] = edges[edge];
  return treePaths.get(upper) ^ bit(edge) ^ treePaths.get(lower);
});
assert.deepEqual([queue.length, edges.length, chords.length], [35, 60, 26]);

function chordCoordinates(cycle) {
  return chords.reduce((vector, edge, index) =>
    (cycle & bit(edge)) ? vector | bit(index) : vector, 0n);
}
function swapAdjacent(mask, i) {
  const different = ((mask >> i) ^ (mask >> (i + 1))) & 1;
  return mask ^ (different << i) ^ (different << (i + 1));
}
function applySwap(cycle, i) {
  let image = 0n;
  edges.forEach(([upper, lower], index) => {
    if (cycle & bit(index)) {
      const key = edgeKey(swapAdjacent(upper, i), swapAdjacent(lower, i));
      image ^= bit(edgeIndices.get(key));
    }
  });
  return image;
}
const pivots = new Map();
function reduce(vector) {
  for (let i = chords.length - 1; i >= 0; i--) {
    if ((vector & bit(i)) && pivots.has(i)) vector ^= pivots.get(i);
  }
  return vector;
}
for (let i = 0; i < anchor - 1; i++) {
  for (const cycle of cycles) {
    const relation = reduce(chordCoordinates(cycle ^ applySwap(cycle, i)));
    if (relation) pivots.set(relation.toString(2).length - 1, relation);
  }
}
assert.equal(pivots.size, 25);

function classOf(route) {
  const vertices = route.map(support);
  let cycle = 0n;
  vertices.forEach((first, index) => {
    const next = vertices[(index + 1) % vertices.length];
    const pair = first & next;
    cycle ^= bit(edgeIndices.get(edgeKey(first, pair)));
    cycle ^= bit(edgeIndices.get(edgeKey(next, pair)));
  });
  return reduce(chordCoordinates(cycle));
}
let flat = 0;
const curved = {R: 0, T: 0, O: 0};
const curvedClasses = new Set();
for (const pair of combinations(axes, 2)) {
  for (const varying of combinations(axes.filter(axis => !pair.includes(axis)), 3)) {
    const route = varying.map(axis => [...pair, axis]);
    assert.deepEqual(endFrame(route), route[0]);
    assert.equal(classOf(route), 0n);
    flat++;
  }
}
for (const four of combinations(axes, 4)) {
  for (const common of four) {
    const [a, b, c] = four.filter(axis => axis !== common);
    const route = [[common, a, b], [common, b, c], [common, a, c]];
    assert.deepEqual(endFrame(route), [common, b, a]);
    curved[common === anchor ? 'R' : four.includes(anchor) ? 'T' : 'O']++;
    curvedClasses.add(classOf(route));
  }
}
assert.equal(flat, 60);
assert.deepEqual(curved, {R: 10, T: 30, O: 20});
assert.equal(curvedClasses.size, 1);
assert.ok(!curvedClasses.has(0n));
console.log(JSON.stringify({vertices: queue.length, edges: edges.length, fundamentalCycles: chords.length,
  coinvariantRelations: (anchor - 1) * chords.length, mod2RelationRank: pivots.size,
  mod2QuotientDimension: chords.length - pivots.size, flat, curved,
  curvedClasses: curvedClasses.size, curvedClassNonzero: true}, null, 2));
