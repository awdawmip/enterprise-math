// R762FN: exact exhaustive source-matching BRC checker. Node >= 18; no dependencies.
import assert from 'node:assert/strict';

function perms(a) {
  if (a.length === 0) return [[]];
  const out = [];
  for (let i = 0; i < a.length; i++) {
    const tail = [...a.slice(0, i), ...a.slice(i + 1)];
    for (const p of perms(tail)) out.push([a[i], ...p]);
  }
  return out;
}
function factorial(n) {
  let p = 1;
  for (let i = 2; i <= n; i++) p *= i;
  return p;
}
function falling(k, t) { return factorial(k) / factorial(k - t); }
function bits(n) { return n < 2 ? 0 : Math.ceil(Math.log2(n)); }
function partnerTranscript(sigma, tau, t) {
  return JSON.stringify(Array.from({length:t}, (_,i) => [sigma[i],tau[i]]));
}
const results = [];
let checkedHistories = 0;
for (let k = 1; k <= 5; k++) {
  const permutations = perms(Array.from({length:k}, (_,i) => i));
  assert.equal(permutations.length, factorial(k));
  const population = factorial(k) ** 2;
  const grouped = Array.from({length:k+1}, () => new Map());
  for (const sigma of permutations) for (const tau of permutations) {
    checkedHistories++;
    for (let t = 0; t <= k; t++) {
      const key = partnerTranscript(sigma, tau, t);
      grouped[t].set(key, (grouped[t].get(key) || 0) + 1);
    }
    // Adaptive reconstruction: every one of the first k-1 A-token queries
    // reveals one event; the final unmatched B/C tokens pair with final A.
    const sigmaKnown = sigma.slice(0, k-1);
    const tauKnown = tau.slice(0, k-1);
    const finalB = Array.from({length:k},(_,i)=>i).find(i=>!sigmaKnown.includes(i));
    const finalC = Array.from({length:k},(_,i)=>i).find(i=>!tauKnown.includes(i));
    assert.deepEqual([...sigmaKnown,finalB], sigma);
    assert.deepEqual([...tauKnown,finalC], tau);
  }
  const horizons = [];
  for (let t = 0; t <= k; t++) {
    const expectedOutputs = falling(k,t)**2;
    const expectedFiber = factorial(k-t)**2;
    assert.equal(grouped[t].size, expectedOutputs);
    for (const actualFiber of grouped[t].values()) assert.equal(actualFiber,expectedFiber);
    assert.equal(expectedOutputs*expectedFiber,population);
    horizons.push({queried_a_tokens:t,distinct_transcripts:expectedOutputs,
      histories_per_transcript:expectedFiber,sharp_fixed_length_bits:bits(expectedOutputs)});
  }
  assert.equal(horizons[k-1].distinct_transcripts,population);
  if(k>=2) assert.equal(horizons[k-2].histories_per_transcript,4);
  results.push({k,source_histories:population,full_memory_bits:bits(population),horizons});
}
const evidence = {research_id:'R762FN',date:'2026-11-19',arithmetic:'exact finite integer counts; no floating-point state updates',
  candidate_model:'k distinctly named A/B/C positive native X6 legs per axis; one of each axis in each typed triad',
  k_range:[1,5],verified_histories:checkedHistories,results,status:'PASS',
  limitation:'Finite checker supports, but does not substitute for, the symbolic all-k proof.'};
console.log(JSON.stringify(evidence,null,2));
