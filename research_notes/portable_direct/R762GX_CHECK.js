'use strict';
// R762GX: finite checker for the K4-STAR oriented Port candidate.
// Runtime: Node.js >=18; no dependencies beyond the standard library.
const assert = require('node:assert/strict');
const V = [0, 1, 2, 3];
const E = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
function parity(a) {
  let inversions = 0;
  for (let i=0; i<a.length; i++)
    for (let j=i+1; j<a.length; j++) if (a[i]>a[j]) inversions++;
  return inversions%2 ? -1 : 1;
}
function allPermutations(xs) {
  if (!xs.length) return [[]];
  const result = [];
  for (let i=0; i<xs.length; i++) {
    for (const tail of allPermutations(xs.filter((_,j)=>j!==i)))
      result.push([xs[i],...tail]);
  }
  return result;
}
function edge(v,u) { return [Math.min(v,u), Math.max(v,u)]; }
function axisIndex(v,u) {
  const e=edge(v,u);
  return E.findIndex(([a,b])=>a===e[0]&&b===e[1]);
}
function H(v) { return E.map(e=>e.includes(v)?1:0); }
function successor(v,u,chi) {
  assert(v!==u && (chi===1||chi===-1));
  const [a,b] = V.filter(w=>w!==v&&w!==u);
  return parity([v,u,a,b])===chi ? a : b;
}
function transition(v,u,chi,s) {
  assert(s===1||s===-1);
  const a=successor(v,u,chi);
  const b=V.find(w=>w!==v&&w!==u&&w!==a);
  const delta=H(v).map(q=>s*q);
  return {v,u,a,b,chi,s, nextPort:edge(v,a),
    nextU:a, delta, order:[u,a,b], tIncrement:1};
}
function permuteDelta(delta,p) {
  const ret=Array(6).fill(0);
  E.forEach(([v,u],i)=>{ret[axisIndex(p[v],p[u])]=delta[i];});
  return ret;
}
function choose(n,k) {
  if (k<0||k>n) return 0;
  let x=1;
  for(let j=1;j<=k;j++) x=x*(n-j+1)/j;
  return Math.round(x);
}
const perms=allPermutations(V);
assert.equal(perms.length,24);
let covarianceCases=0, stabilizerObstructions=0, triCycles=0;
for(const p of perms) for(const v of V) for(const u of V) {
  if(u===v) continue;
  for(const chi of [-1,1]) for(const s of [-1,1]) {
    const x=transition(v,u,chi,s);
    const y=transition(p[v],p[u],parity(p)*chi,s);
    assert.equal(y.nextU,p[x.nextU]);
    assert.deepEqual(y.nextPort,edge(p[v],p[x.a]));
    assert.deepEqual(y.delta,permuteDelta(x.delta,p));
    assert.deepEqual(y.order,x.order.map(w=>p[w]));
    assert.equal(y.tIncrement,x.tIncrement);
    covarianceCases++;
  }
}
for(const v of V) for(const u of V) {
  if(u===v) continue;
  const [a,b]=V.filter(w=>w!==v&&w!==u);
  const flip=V.slice(); flip[a]=b; flip[b]=a;
  assert.equal(parity(flip),-1);
  for(const chi of [-1,1]) {
    const next=successor(v,u,chi);
    assert.notEqual(flip[next],next);
    stabilizerObstructions++;
    let portU=u;
    for(let j=0;j<3;j++) portU=successor(v,portU,chi);
    assert.equal(portU,u);
    triCycles++;
  }
}
const orbit=new Set(perms.map(p=>`${p[0]},${p[1]},${parity(p)}`));
assert.equal(orbit.size,24);
const exactReturnCounts={};
for(let m=0;m<=10;m++) {
  let observed=0;
  // Choose one active vertex and one chirality; signs are BRC source labels.
  for(let mask=0;mask<2**m;mask++) {
    let portU=1, dx=Array(6).fill(0);
    for(let j=0;j<m;j++) {
      const s=(mask&(1<<j))?1:-1;
      const e=transition(0,portU,1,s);
      dx=dx.map((q,i)=>q+e.delta[i]); portU=e.nextU;
    }
    if(portU===1&&dx.every(q=>q===0)) observed++;
  }
  const predicted=m===0?1:(m%6===0?choose(m,m/2):0);
  assert.equal(observed,predicted);
  exactReturnCounts[m]=observed;
}
const witnessPlus=transition(0,1,1,1);
const witnessMinus=transition(0,1,-1,1);
assert.deepEqual(witnessPlus.nextPort,[0,2]);
assert.deepEqual(witnessMinus.nextPort,[0,3]);
assert.deepEqual(witnessPlus.delta,witnessMinus.delta);
// The second event with active endpoint 2 is available only from the plus state.
assert(witnessPlus.nextPort.includes(2));
assert(!witnessMinus.nextPort.includes(2));
const result={
  model:'R762GX_K4_STAR_PORT_ORIENTATION_CANDIDATE',
  permutations:perms.length,
  directed_port_inputs:12,
  oriented_port_states:24,
  signed_oriented_input_transitions:48,
  covariance_cases:covarianceCases,
  equivariant_turn_obstruction_cases:stabilizerObstructions,
  three_step_port_cycles:triCycles,
  oriented_port_single_S4_orbit:orbit.size===24,
  fixed_vertex_signed_return_counts_m_0_to_10:exactReturnCounts,
  six_step_full_cell_and_port_return_paths:20,
  observer_witness:{input_port:[0,1],active_vertex:0,sign:1,
    next_plus:witnessPlus.nextPort,next_minus:witnessMinus.nextPort,
    common_cell_increment:witnessPlus.delta},
  status:'PASS',
  scope:'Exhaustive finite S4/K4 combinatorics and fixed-active-vertex m<=10 enumeration; candidate dynamics only'
};
console.log(JSON.stringify(result,null,2));
