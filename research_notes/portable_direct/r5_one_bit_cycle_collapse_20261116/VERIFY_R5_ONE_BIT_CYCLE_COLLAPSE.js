#!/usr/bin/env node
'use strict';
// Frozen input: 435e77af0d180eac32bd1f9c4c464bc4010b7551
// Pure finite/Boolean validation. No native X6 claim and no MILP solve.
const assert = require('node:assert/strict');
const pairs9 = [
 [127,127],[151,151],[175,175],[187,187],[215,215],[221,221],
 [223,223],[233,233],[235,235],[245,245],[247,247],[251,251],
 [341,341],[346,347],[350,351],[365,365],[366,367],[373,373],
 [378,379],[421,421],[426,427],[429,429],[438,439],[445,445],
 [446,447],[469,469],[474,475],[493,493],[494,495],[502,503],
 [508,509],[510,511]
];
function gcd(a,b){while(b){[a,b]=[b,a%b]}return a;}
function lcm(a,b){return a/gcd(a,b)*b;}
function powmap(f,n){
  let r=f.map((_,i)=>i);
  for(let t=0;t<n;t++)r=r.map(x=>f[x]);
  return r;
}
function idempotent(f){return f.every((v,i)=>f[v]===v);}
function allMaps(m){
  const out=[];
  for(let z=0;z<m**m;z++){
    let x=z, f=[];
    for(let j=0;j<m;j++){f.push(x%m);x=Math.floor(x/m);}
    out.push(f);
  }
  return out;
}
function cycleDecomposition(g0,g1){
  const m=g0.length, visited=new Set(), cycles=[];
  assert.equal(g1.length,m);
  assert(idempotent(g0)&&idempotent(g1));
  const next=z=>{
    const q=Math.floor(z/2), b=z%2;
    return 2*(b===0?g1[q]:g0[q])+(1-b);
  };
  for(let start=0;start<2*m;start++){
    if(visited.has(start))continue;
    const seen=new Map(), path=[];
    let at=start;
    while(!seen.has(at)&&!visited.has(at)){
      seen.set(at,path.length);path.push(at);at=next(at);
    }
    if(seen.has(at)){
      const cycle=path.slice(seen.get(at));
      assert(cycle.some(z=>z%2===0)&&cycle.some(z=>z%2===1));
      for(const z of cycle){
        const q=Math.floor(z/2),b=z%2;
        assert.equal((b===0?g0[q]:g1[q]),q);
      }
      cycles.push(cycle);
    }
    for(const z of path)visited.add(z);
  }
  const owner=new Map();
  cycles.forEach((cycle,i)=>cycle.forEach(z=>{
    const q=Math.floor(z/2);
    assert(!owner.has(q)||owner.get(q)===i, 'different cycles share a control state');
    owner.set(q,i);
  }));
  return cycles;
}
function mapAudit(){
  const results=[];
  for(let m=1;m<=4;m++){
    const maps=allMaps(m),L=Array.from({length:m},(_,i)=>i+1).reduce(lcm,1);
    let pairs=0,cycleCount=0,maxCycleLength=0;
    const normalized=maps.map(f=>powmap(f,L));
    assert(normalized.every(idempotent));
    for(const g0 of normalized)for(const g1 of normalized){
      const cs=cycleDecomposition(g0,g1);
      pairs++;cycleCount+=cs.length;
      for(const c of cs)maxCycleLength=Math.max(maxCycleLength,c.length);
    }
    results.push({m,L,ordered_function_pairs_checked:pairs,
      recurrent_alternating_cycles:cycleCount,max_phase_cycle_length:maxCycleLength});
  }
  assert.deepEqual(results.map(z=>z.ordered_function_pairs_checked),[1,16,729,65536]);
  assert.deepEqual(results.map(z=>z.recurrent_alternating_cycles),[1,20,1017,98176]);
  return results;
}
function adjacentCount(x,k){
  let s=0;
  for(let i=0;i<k;i++)s+=((x>>i)&1)*((x>>((i+1)%k))&1);
  return s;
}
function good(r,u,k=9,s=2){
  return (u & ~r)===0 && adjacentCount(r,k)-adjacentCount(u,k)<=s;
}
function sourceAudit(){
  const states=[], f0=[],f1=[], centres=[];
  for(const [a,b] of pairs9){
    const p=states.length;
    states.push({centre:a,pair:centres.length,bit:0});
    if(a===b){ f0.push(p);f1.push(p); }
    else {states.push({centre:b,pair:centres.length,bit:1});
      f0.push(p,p); f1.push(p+1,p+1);}
    centres.push([a,b]);
  }
  assert.equal(states.length,44);
  assert(idempotent(f0)&&idempotent(f1));
  const cycles=cycleDecomposition(f0,f1);
  const assigned=[];
  let memberships=0, transitions=0, wordChecks=0;
  for(let y=0;y<256;y++){
    const i=pairs9.findIndex(([a,b])=>good(a,2*y)&&good(b,2*y+1));
    assert(i>=0,'uncovered '+y);
    assigned.push(i);
    const [a,b]=pairs9[i];
    assert(good(a,2*y));assert(good(b,2*y+1));memberships+=2;
    const ids=states.map((s,j)=>s.pair===i?j:-1).filter(z=>z>=0);
    for(let bit=0;bit<=1;bit++){
      const q=ids[bit===0?0:ids.length-1];
      assert(good(states[q].centre,2*y+bit));
      // Every one of 2^d length-d words, for d=0..6.
      for(let d=0;d<=6;d++)for(let word=0;word<(1<<d);word++){
        let at=q, rawbit=bit;
        for(let t=0;t<d;t++){
          const b2=(word>>t)&1;
          at=b2===0?f0[at]:f1[at];rawbit=b2;
          assert(good(states[at].centre,2*y+rawbit));
          transitions++;
        }
        wordChecks++;
      }
    }
  }
  // The 88-state double-copy controller is valid but has non-idempotent resets.
  const n=states.length;
  const t0=Array.from({length:2*n},(_,z)=>2*f0[Math.floor(z/2)]+(1-z%2));
  const t1=Array.from({length:2*n},(_,z)=>2*f1[Math.floor(z/2)]+(1-z%2));
  assert(!idempotent(t0)&&!idempotent(t1));
  const h0=powmap(t0,2),h1=powmap(t1,2);
  assert(idempotent(h0)&&idempotent(h1));
  const doubledCycles=cycleDecomposition(h0,h1);
  // Reachable pair outputs are source-correct for every tail after normalization.
  let tailCycleChecks=0;
  for(let y=0;y<256;y++){
    const i=assigned[y], base=states.findIndex(s=>s.pair===i);
    let at=2*base, b=0;
    at=h0[at];
    const seen=new Map(),seq=[];
    while(!seen.has(2*at+b)){
      seen.set(2*at+b,seq.length);seq.push([at,b]);
      b=1-b;at=b===0?h0[at]:h1[at];
    }
    const loop=seq.slice(seen.get(2*at+b));
    assert(loop.some(z=>z[1]===0)&&loop.some(z=>z[1]===1));
    for(const [q,bit] of loop){
      assert(good(states[Math.floor(q/2)].centre,2*y+bit));
      tailCycleChecks++;
    }
  }
  return {k:9,s:2,tails:256,raw_masks:512,centres:centres.length,
    controller_states:n,inert_components:pairs9.filter(([a,b])=>a===b).length,
    paired_components:pairs9.filter(([a,b])=>a!==b).length,
    alternating_cycles:cycles.length,source_memberships:memberships,
    exhaustive_word_cases:wordChecks,word_transition_checks:transitions,
    nonidempotent_double_copy_states:2*n,doubled_idempotent_cycles:doubledCycles.length,
    alternating_cycle_tail_checks:tailCycleChecks,valid:true};
}
function main(){
  const result={schema:'R5_ONE_BIT_CYCLE_COLLAPSE_EVIDENCE_V1',
    frozen_science_pin:'435e77af0d180eac32bd1f9c4c464bc4010b7551',
    theorem:'N_dyn(k,{0},s)=W(k,s) for finite one-bit Set systems',
    status:'PASS_R5_ONE_BIT_CYCLE_COLLAPSE',
    finite_function_audit:mapAudit(),source_witness_audit:sourceAudit(),
    limitation:'Finite tests check algebraic cases and saved upper witness; universal result follows the standalone proof. W9=44 lower is inherited HiGHS-reported optimum, not a new exact unsat certificate.'};
  console.log(JSON.stringify(result,null,2));
}
main();
