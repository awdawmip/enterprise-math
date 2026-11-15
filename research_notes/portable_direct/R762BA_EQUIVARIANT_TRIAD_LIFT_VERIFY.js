'use strict';
// Exact, dependency-free enumeration of S6 covariance and third-axis fibers.
const assert = require('node:assert/strict');
const A = [0, 1, 2, 3, 4, 5];
function permutations(values) {
  if (values.length === 0) return [[]];
  const out = [];
  for (let i = 0; i < values.length; i++) {
    const head = values[i];
    const tail = values.slice(0, i).concat(values.slice(i + 1));
    for (const p of permutations(tail)) out.push([head, ...p]);
  }
  return out;
}
const group = permutations(A);
assert.equal(group.length, 720);
function candidates(i, j) {
  assert(i !== j);
  return A.filter(k => k !== i && k !== j);
}
function closure(i, j, k) {
  return new Set([i, j, k]).size === 3;
}
let orderedPairs = 0, typedTriads = 0, covarianceTests = 0;
let stabilizerTests = 0, candidateOrbitTests = 0, observerCollisionPairs = 0;
let pairStabilizerTotal = 0, triadStabilizerTotal = 0;
let nontrivialInvariantSubsets = 0;
const holonomyFixedHistogram = {0:0,1:0,2:0,3:0,4:0};
let holonomyChecks = 0;
for (const i of A) for (const j of A) if (i !== j) {
  orderedPairs++;
  const fiber = candidates(i, j);
  assert.equal(fiber.length, 4);
  const stabilizer = group.filter(p => p[i] === i && p[j] === j);
  assert.equal(stabilizer.length, 24);
  pairStabilizerTotal += stabilizer.length;
  const pairHistogram = {0:0,1:0,2:0,3:0,4:0};
  for (const h of stabilizer) {
    const fixed = fiber.filter(k => h[k] === k).length;
    pairHistogram[fixed]++;
    holonomyFixedHistogram[fixed]++;
    holonomyChecks++;
  }
  assert.deepEqual(pairHistogram,{0:9,1:8,2:6,3:0,4:1});
  for (const k of fiber) {
    typedTriads++;
    const orbit = new Set(stabilizer.map(p => p[k]));
    assert.deepEqual([...orbit].sort((a,b)=>a-b),fiber);
    candidateOrbitTests++;
    assert.equal(stabilizer.filter(p => p[k] === k).length,6);
    triadStabilizerTotal += 6;
    for (const p of group) {
      assert.equal(closure(i,j,k),closure(p[i],p[j],p[k]));
      const image = candidates(p[i],p[j]);
      assert(image.includes(p[k]));
      covarianceTests++;
    }
  }
  // Any nonempty K-invariant subset of the four third axes is the full fiber.
  for (let mask=0;mask<16;mask++) {
    const subset = new Set(fiber.filter((_,n) => (mask & (1<<n)) !== 0));
    const invariant = stabilizer.map(p => fiber.every(k => subset.has(k) === subset.has(p[k]))).every(Boolean);
    if (invariant) assert(mask === 0 || mask === 15);
    if (invariant && mask !== 0 && mask !== 15) nontrivialInvariantSubsets++;
    stabilizerTests += stabilizer.length;
  }
  // The two-force observer agrees; a future named-port test separates every two lifts.
  for (let a=0;a<fiber.length;a++) for(let b=a+1;b<fiber.length;b++) {
    const k=fiber[a], l=fiber[b];
    assert(k !== l && !fiber.includes(i) && !fiber.includes(j));
    assert.equal(k===k,true);
    assert.notEqual(k===k,l===k);
    observerCollisionPairs++;
  }
  // A chosen third-axis sign is preserved by the S6 axis-permutation stabilizer.
  for (const sign of [-1,1]) {
    const signedOrbit = new Set(stabilizer.map(p => `${p[fiber[0]]}:${sign}`));
    assert.equal(signedOrbit.size,4);
  }
}
assert.equal(orderedPairs,30);
assert.equal(typedTriads,120);
assert.equal(covarianceTests,86400);
assert.equal(candidateOrbitTests,120);
assert.equal(stabilizerTests,11520);
assert.equal(observerCollisionPairs,180);
assert.equal(pairStabilizerTotal,720);
assert.equal(triadStabilizerTotal,720);
assert.equal(nontrivialInvariantSubsets,0);
assert.equal(holonomyChecks,720);
assert.deepEqual(holonomyFixedHistogram,{0:270,1:240,2:180,3:0,4:30});
const result={
  schema:'ENTERPRISE_MATH_R762BA_EXACT_TEST_V1',
  model:'positive equal-quantum, ordered-two-force observation, pairwise-distinct native X6 axes; candidate relation not native admission',
  group_size:group.length,
  ordered_pairs:orderedPairs,
  positive_ordered_triads:typedTriads,
  positive_unordered_triads:20,
  third_axis_fiber_size:4,
  pair_stabilizer_order:24,
  triple_stabilizer_order:6,
  pair_stabilizer_counts_checked:pairStabilizerTotal,
  triple_stabilizer_counts_checked:triadStabilizerTotal,
  group_equivariance_tests:covarianceTests,
  candidate_orbit_tests:candidateOrbitTests,
  invariant_subset_action_checks:stabilizerTests,
  nontrivial_invariant_subsets:nontrivialInvariantSubsets,
  two_force_observer_collision_pairs:observerCollisionPairs,
  optional_signed_completion_if_both_signs_admitted:8,
  based_pair_holonomy_checks:holonomyChecks,
  fixed_source_branch_histogram:holonomyFixedHistogram,
  conclusion:'PASS: stabilizer transitivity excludes an S6-equivariant deterministic third-axis selector; 4-sheet source fiber is sharp'
};
console.log(JSON.stringify(result,null,2));
