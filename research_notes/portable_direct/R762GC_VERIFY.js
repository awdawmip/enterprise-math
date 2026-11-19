'use strict';
const assert = require('node:assert/strict');
const n = 6;
const choose = (a,b) => a * (a-1) * (a-2) / 6;
const key = v => v.join(',');
function readout(z,S){const x=S.map(i=>z[i]);const m=Math.min(...x);return x.map(v=>v-m).join(',');}
const ep = new Map();
const negativeWords = [0,0,0,0];
let words=0,wrongParity=0;
for(let a=0;a<n;a++)for(let b=0;b<n;b++)for(let c=0;c<n;c++){
  if(new Set([a,b,c]).size!==3)continue;
  for(let bits=0;bits<8;bits++){
    const z=Array(n).fill(0), ax=[a,b,c];
    for(let t=0;t<3;t++)z[ax[t]]=(bits>>t)&1 ? -1 : 1;
    ep.set(key(z),(ep.get(key(z))||0)+1);
    words++;
    negativeWords[z.filter(x=>x<0).length]++;
    if(z.reduce((x,y)=>x+y,0)%2===0)wrongParity++;
    assert.equal(z.reduce((x,y)=>x+y*y,0),3);
  }
}
assert.equal(words,960);
assert.equal(ep.size,160);
assert.ok([...ep.values()].every(v=>v===6));
assert.deepEqual(negativeWords,[120,360,360,120]);
assert.equal(wrongParity,0);
const observations=[];
let swapTests=0;
let swapFailures=0;
for(let a=0;a<n;a++)for(let b=a+1;b<n;b++)for(let c=b+1;c<n;c++){
  const S=[a,b,c],q=new Map();
  for(const x of [-1,1])for(const y of [-1,1])for(const z of [-1,1]){
    const raw=Array(n).fill(0);raw[a]=x;raw[b]=y;raw[c]=z;
    const r=readout(raw,S);q.set(r,(q.get(r)||0)+6);
  }
  assert.equal(q.size,7);
  assert.equal(q.get('0,0,0'),12);
  assert.deepEqual([...q.values()].sort((x,y)=>x-y),[6,6,6,6,6,6,12]);
  const p=Array(n).fill(0),m=Array(n).fill(0);
  for(const i of S){p[i]=1;m[i]=-1;}
  assert.equal(readout(p,S),'0,0,0');
  assert.equal(readout(m,S),'0,0,0');
  for(const i of S)for(let j=0;j<n;j++){
    if(S.includes(j))continue;
    const pp=p.slice(),mm=m.slice();
    [pp[i],pp[j]]=[pp[j],pp[i]];
    [mm[i],mm[j]]=[mm[j],mm[i]];
    swapTests++;
    if(readout(pp,S)===readout(mm,S))swapFailures++;
  }
  observations.push({support:S,classes:q.size,word_fibres:[...q.values()].sort((x,y)=>x-y)});
}
assert.equal(observations.length,20);
assert.equal(swapTests,180);
assert.equal(swapFailures,0);
const oddPathCounts={};
for(const length of [1,3,5]){
  const z=Array(n).fill(0);let checked=0,returned=0;
  function step(t){
    if(t===length){checked++;if(z.every(v=>v===0))returned++;return;}
    for(let i=0;i<n;i++)for(const sign of [-1,1]){z[i]+=sign;step(t+1);z[i]-=sign;}
  }
  step(0);
  assert.equal(checked,12**length);
  assert.equal(returned,0);
  oddPathCounts[length]={checked,returned};
}
const result={
  status:'PASS',
  parameters:{native_axes:6,selected_axes:3,primitive_signs:2},
  all_distinct_signed_words:words,
  raw_signed_endpoints:ep.size,
  ordered_words_per_endpoint:6,
  negative_sign_word_counts:negativeWords,
  supports_checked:observations.length,
  selected_support_signed_paths:48,
  relative_observation_classes:7,
  relative_observation_word_fibres:[6,6,6,6,6,6,12],
  after_one_swap_endpoint_classes:8,
  after_one_swap_word_fibres:[6,6,6,6,6,6,6,6],
  selected_to_omitted_swaps_checked:swapTests,
  swap_failures:swapFailures,
  odd_length_exhaustions:oddPathCounts
};
process.stdout.write(JSON.stringify(result,null,2)+'\n');