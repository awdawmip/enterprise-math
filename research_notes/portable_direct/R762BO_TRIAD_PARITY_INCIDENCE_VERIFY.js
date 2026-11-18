'use strict';
// R762BO exact finite checker (Node.js >=18). All arithmetic is integral.
const assert=require('node:assert/strict');
const fs=require('node:fs');
const axes=[0,1,2,3,4,5];
const steps=axes.flatMap(i=>[-1,1].map(s=>({i,s})));
const zero=()=>axes.map(()=>0);
function endpoint(w){const v=zero();for(const p of w)v[p.i]+=p.s;return v;}
function parity(v){return v.reduce((a,b)=>a+b,0)&1;}
function l1(v){return v.reduce((a,b)=>a+Math.abs(b),0);}
function key(w){return w.map(p=>String(p.i+1)+(p.s>0?'+':'-')).join(',');}
function distinct(w){return new Set(w.map(p=>p.i)).size===w.length;}
function cycleKey(w){
 const rotations=[w,[w[1],w[2],w[0]],[w[2],w[0],w[1]]];
 return rotations.map(key).sort()[0];
}
function* permutations(a,k=0){
 if(k===a.length){yield a.slice();return;}
 for(let j=k;j<a.length;j++){
  [a[k],a[j]]=[a[j],a[k]];
  yield* permutations(a,k+1);
  [a[k],a[j]]=[a[j],a[k]];
 }
}
const words=[];
for(const a of steps)for(const b of steps)for(const c of steps)words.push([a,b,c]);
assert.equal(words.length,1728);
let returns=0;
const l1hist={};
for(const w of words){
 const v=endpoint(w);
 assert.equal(parity(v),1);
 if(v.every(x=>x===0))returns++;
 const d=l1(v);l1hist[d]=(l1hist[d]||0)+1;
}
assert.equal(returns,0);
assert.deepEqual(l1hist,{1:396,3:1332});
const valid=words.filter(distinct);
assert.equal(valid.length,960);
const endpoints=valid.map(endpoint), endpointCounts=new Map();
const wordSigns={0:0,1:0,2:0,3:0};
for(let n=0;n<valid.length;n++){
 const v=endpoints[n];
 assert.equal(l1(v),3);
 assert.equal(v.reduce((s,x)=>s+x*x,0),3);
 const k=v.join(',');
 endpointCounts.set(k,(endpointCounts.get(k)||0)+1);
 const npositive=valid[n].filter(x=>x.s===1).length;
 wordSigns[npositive]++;
}
assert.equal(endpointCounts.size,160);
assert([...endpointCounts.values()].every(x=>x===6));
assert.deepEqual(wordSigns,{0:120,1:360,2:360,3:120});
let pairTests=0, pairReturns=0;
for(let a=0;a<valid.length;a++){
 let suffixes=0;
 for(let b=0;b<valid.length;b++){
  const left=endpoints[a],right=endpoints[b];
  const cancel=axes.every(i=>left[i]+right[i]===0);
  const negative=axes.every(i=>right[i]===-left[i]);
  assert.equal(cancel,negative);
  pairTests++;
  if(cancel){pairReturns++;suffixes++;}
 }
 assert.equal(suffixes,6);
}
assert.equal(pairTests,921600);
assert.equal(pairReturns,5760);
const perms=[...permutations(axes.slice())];
assert.equal(perms.length,720);
let transportTests=0;
for(const pi of perms)for(const w of valid){
 const moved=w.map(p=>({i:pi[p.i],s:p.s}));
 assert(distinct(moved));
 const v=endpoint(w),u=endpoint(moved);
 for(const i of axes)assert.equal(u[pi[i]],v[i]);
 transportTests++;
}
assert.equal(transportTests,691200);
const cycles=new Map(), representatives=new Map();
for(const w of valid){
 const k=cycleKey(w);
 if(!cycles.has(k))cycles.set(k,w);
 const positive=w.filter(p=>p.s===1).length;
 if(!representatives.has(positive))representatives.set(positive,w);
}
assert.equal(cycles.size,320);
const cyclesByPositive={0:0,1:0,2:0,3:0};
for(const w of cycles.values())cyclesByPositive[w.filter(p=>p.s===1).length]++;
assert.deepEqual(cyclesByPositive,{0:40,1:120,2:120,3:40});
for(const w of valid){
 const rot=[w[1],w[2],w[0]];
 assert.equal(cycleKey(w),cycleKey(rot));
}
let cycleOrbitTests=0;
for(const positive of [0,1,2,3]){
 const rep=representatives.get(positive),orb=new Set();
 for(const pi of perms){
  orb.add(cycleKey(rep.map(p=>({i:pi[p.i],s:p.s}))));
  cycleOrbitTests++;
 }
 assert.equal(orb.size,cyclesByPositive[positive]);
}
assert.equal(cycleOrbitTests,2880);
const sampleCell=[2,-1,0,7,-3,1], history=[valid[0]];
for(const event of [valid[1],valid[88],valid[959]]){
 const state={cell:sampleCell.slice(),history:history.concat([event])};
 assert.deepEqual(state.cell,sampleCell);
 assert.equal(state.history.length,2);
 assert.equal(key(state.history[1]),key(event));
}
const evidence={
 schema:'EM_R762BO_FINITE_EXACT_EVIDENCE_V1',date_utc:'2026-11-15',
 task:'RS-X6-TRIADIC-CLOSURE-DYNAMICS',
 arithmetic:'exact signed integer arithmetic and exhaustive finite enumeration',
 all_signed_three_step_words:words.length,all_three_step_returns:returns,
 all_three_step_l1_histogram:l1hist,
 distinct_axis_ordered_words:valid.length,
 distinct_axis_signed_endpoints:endpointCounts.size,
 paths_per_endpoint:6,
 positive_port_count_ordered_word_histogram:wordSigns,
 tested_ordered_two_block_pairs:pairTests,
 exact_two_block_returns:pairReturns,
 tested_S6_permutations:perms.length,
 signed_word_transport_assertions:transportTests,
 unrooted_directed_three_port_cycles:cycles.size,
 rooted_orders_per_oriented_cycle:3,
 directed_cycle_orbits_by_positive_port_count:cyclesByPositive,
 cycle_orbit_permutation_checks:cycleOrbitTests,
 independent_review:'NOT_REVIEWED',
 scope:'signed X6 coordinate parity and declared candidate directed three-Port relation, not an admitted native force law'
};
const body=JSON.stringify(evidence,null,2)+'\n';
if(process.argv[2])fs.writeFileSync(process.argv[2],body);
process.stdout.write(body);
