"use strict";
/* R762AQ exact finite AK4 auxiliary observer/BRC-ordered-word verifier.
 * Node.js >= 18; no third-party dependencies, no floating point, no native X6 simulation.
 * Reproduces every finite closure and decision-tree integer reported in the paper.
 */
const assert=require("node:assert/strict");
const E="012", C="120", T="102";
const states=[[0,E],[1,E],[2,E],[0,"021"],[0,"102"],[0,"120"],[0,"201"],[0,"210"],null];
const N=states.length, live=(1<<8)-1, all=(1<<9)-1;
const key=s=>s===null?"U":s[0]+":"+s[1];
const index=new Map(states.map((s,i)=>[key(s),i]));
const compose=(p,q)=>[0,1,2].map(i=>p[Number(q[i])]).join("");
function step(i,letter){
  const s=states[i];
  if(s===null)return 8;
  const [r,h]=s;
  if(letter==="S")return h===E?index.get(key([(r+1)%3,E])):8;
  if(r!==0)return 8;
  if(letter==="C"||letter==="T")
    return index.get(key([0,compose(letter==="C"?C:T,h)]));
  throw Error("Unknown letter "+letter);
}
function observe(i){
  const s=states[i];
  if(s===null)return "U";
  const h=s[1], typ=h===E?"E":h==="120"||h==="201"?"C":"T";
  return (s[0]===0?"E":"C")+typ;
}
function runWord(i,word){for(const c of word)i=step(i,c);return observe(i)}
function pop(mask){let n=0;while(mask){mask&=mask-1;n++}return n}
function partitions(mask,v){
  const groups=new Map;
  for(let i=0;i<N;i++)if(mask&(1<<i)){
    const label=v[i];groups.set(label,(groups.get(label)||0)|(1<<i));
  }
  return [...groups.values()];
}
const gen=Object.fromEntries(["S","C","T"].map(letter=>
  [letter,states.map((_,i)=>step(i,letter))]));
const identity=states.map((_,i)=>i);
const maps=new Map([[identity.join(","),{map:identity,word:""}]]);
const queue=[identity];
for(let cursor=0;cursor<queue.length;cursor++){
  const old=queue[cursor], previous=maps.get(old.join(",")).word;
  for(const c of "SCT"){
    const next=old.map(j=>gen[c][j]), k=next.join(",");
    if(!maps.has(k)){maps.set(k,{map:next,word:previous+c});queue.push(next)}
  }
}
assert.equal(maps.size,75);
assert.equal(Math.max(...[...maps.values()].map(x=>x.word.length)),7);
const signatures=new Map;
for(const {map,word} of maps.values()){
  if(!word)continue;
  const vector=map.map(observe), k=vector.join(",");
  if(!signatures.has(k)||word.length<signatures.get(k).word.length)
    signatures.set(k,{word,vector});
}
const probes=[...signatures.values()];
assert.equal(probes.length,42);
const baseline=identity.map(observe).join(",");
assert.equal(new Set([...signatures.keys(),baseline]).size,43);
// Exact coset lemma: no ordered event word distinguishes all three elements of either parity coset.
for(const {map} of maps.values()){
  const out=map.map(observe);
  for(const coset of [[0,5,6],[3,4,7]]){
    assert(new Set(coset.map(i=>out[i])).size<=2);
  }
}
// Exhaustive alternative to the analytic two-probe lower bound.
for(const first of probes){
  const fiber=partitions(all,first.vector);
  assert(fiber.some(mask=>pop(mask)>1&&!probes.some(second=>
    partitions(mask,second.vector).length===pop(mask))));
}
const memo=new Map;
function optimum(mask,metric){
  if(pop(mask)<=1)return 0;
  const memoKey=metric+":"+mask;
  if(memo.has(memoKey))return memo.get(memoKey);
  let best=Number.POSITIVE_INFINITY;
  for(const {word,vector} of probes){
    const cells=partitions(mask,vector);
    if(cells.length<2)continue;
    const children=cells.map(m=>optimum(m,metric));
    const value=metric==="worst_queries"?1+Math.max(...children)
      :metric==="worst_letters"?word.length+Math.max(...children)
      :metric==="sum_queries"?pop(mask)+children.reduce((a,b)=>a+b,0)
      :pop(mask)*word.length+children.reduce((a,b)=>a+b,0);
    if(value<best)best=value;
  }
  assert(Number.isFinite(best));
  memo.set(memoKey,best);
  return best;
}
const metrics=["worst_queries","worst_letters","sum_queries","sum_letters"];
const results={};
for(const [name,mask] of [["live_8",live],["with_failure_9",all]]){
  results[name]=Object.fromEntries(metrics.map(m=>[m,optimum(mask,m)]));
}
assert.deepEqual(results.live_8,
  {worst_queries:3,worst_letters:3,sum_queries:17,sum_letters:19});
assert.deepEqual(results.with_failure_9,
  {worst_queries:3,worst_letters:3,sum_queries:19,sum_letters:21});
// Explicit adaptive policy: each terminal experiment is a fresh, independent copy.
function diagnose(i){
  let q=0,letters=0;
  const probe=w=>{q++;letters+=w.length;return runWord(i,w)};
  const r=probe("T");let guess;
  if(r==="EE")guess=4;
  else if(r==="U"){
    const s=probe("S");guess=s==="CE"?1:s==="EE"?2:s==="U"?8:-1;
  }else if(r==="ET"){
    const s=probe("S");
    if(s==="CE")guess=0;
    else if(s==="U"){
      const c=probe("C");guess=c==="EC"?5:c==="EE"?6:-1;
    }else guess=-1;
  }else if(r==="EC"){
    const ct=probe("CT");guess=ct==="EE"?3:ct==="EC"?7:-1;
  }else guess=-1;
  assert.equal(guess,i,"Incorrect policy leaf for state "+i);
  return {state_index:i,initial_state:states[i]===null?"U":key(states[i]),
    probes:q,event_letters:letters,identified:guess};
}
const leaves=states.map((_,i)=>diagnose(i));
for(const [name,n] of [["live_8",8],["with_failure_9",9]]){
  const sample=leaves.slice(0,n);
  assert.equal(Math.max(...sample.map(x=>x.probes)),3);
  assert.equal(Math.max(...sample.map(x=>x.event_letters)),3);
  assert.equal(sample.reduce((a,x)=>a+x.probes,0),results[name].sum_queries);
  assert.equal(sample.reduce((a,x)=>a+x.event_letters,0),results[name].sum_letters);
}
const output={
  research_unit:"R762AQ",model:"AK4 auxiliary; reset copies; terminal-only; no initial read",
  frozen_task_commit:"a72226e2430ffa4786321ac86e7f0c599d5f0389",
  exact_arithmetic:"finite integers, labeled ordered event histories, no floating-point",
  state_count:N,full_transformation_monoid:maps.size,
  nonempty_terminal_vectors:signatures.size,
  total_terminal_vectors_with_empty:signatures.size+1,
  max_shortest_word_length:7,
  exact_optimal_results:results,constructive_policy_leaves:leaves,
  universal_proof_scope:"all finite words via complete transformation closure",
  native_triadic_event_verified:false,driver_reviewed:false
};
process.stdout.write(JSON.stringify(output,null,2)+"\n");
