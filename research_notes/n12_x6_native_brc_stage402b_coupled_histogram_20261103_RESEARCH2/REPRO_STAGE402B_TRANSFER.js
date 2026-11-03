'use strict';
const assert = require('node:assert/strict');
const ALPH=[0,1], PAIRS=[[0,0],[0,1],[1,0],[1,1]], L=5, C=2;
function inv(x){return x^1;}
function sig(c,w,paired=true){
  if(!c)return w.length?['L',w.at(-1)]:['E'];
  const ok=w.length>1&&(paired?(inv(w.at(-1)[0])===w.at(-2)[0]&&inv(w.at(-1)[1])===w.at(-2)[1]):inv(w.at(-1))===w.at(-2));
  return [sig(c-1,w,paired),sig(c-1,w.slice(0,-1),paired),ok?sig(c-1,w.slice(0,-2),paired):['X']];
}
function obs(w){
  const p=w.map(x=>x[0]),q=w.map(x=>x[1]);
  const j=v=>{const a=[0,0,0,0];for(let i=1;i<v.length;i++)a[2*v[i-1]+v[i]]++;return a;};
  const z=v=>v.reduce((s,x)=>s+(x===0?1:-1),0);
  return JSON.stringify([w.length,z(p),z(q),j(p),j(q),w.filter(x=>x[0]===x[1]).length]);
}
function transfer(m){
  let d=new Map();d.set(JSON.stringify([[],[],[0,0,0,0],[0,0,0,0],0,0,0]),1n);
  for(let t=0;t<m;t++){
    const nd=new Map();
    for(const [s,n] of d){
      const [last,tail,jp,jq,zp,zq,k]=JSON.parse(s);
      for(const x of PAIRS){
        const pp=jp.slice(),qq=jq.slice();
        if(last.length){pp[2*last[0]+x[0]]++;qq[2*last[1]+x[1]]++;}
        const key=JSON.stringify([x,tail.concat([x]).slice(-L),pp,qq,zp+(x[0]===0?1:-1),zq+(x[1]===0?1:-1),k+(x[0]===x[1]?1:0)]);
        nd.set(key,(nd.get(key)||0n)+n);
      }
    }
    d=nd;
  }
  const distribution=new Map();
  for(const [state,n] of d){
    const [last,tail,jp,jq,zp,zq,k]=JSON.parse(state);
    const f=JSON.stringify([m,zp,zq,jp,jq,k]),g=JSON.stringify(sig(C,tail));
    const key=JSON.stringify([f,g]);distribution.set(key,(distribution.get(key)||0n)+n);
  }
  return distribution;
}
function brute(m){
  const distribution=new Map();
  function visit(w){
    if(w.length===m){const key=JSON.stringify([obs(w),JSON.stringify(sig(C,w))]);distribution.set(key,(distribution.get(key)||0n)+1n);return;}
    for(const p of PAIRS)visit(w.concat([p]));
  }
  visit([]);return distribution;
}
let comparisons=0,words=0;
for(let m=0;m<=6;m++){
  const a=transfer(m),b=brute(m);
  assert.equal(a.size,b.size);
  for(const [k,n] of b){assert.equal(a.get(k),n);comparisons++;}
  words+=4**m;
}
const Q=[[0,0,0,1,0,1],[0,0,1,0,0,1],[0,1,0,0,0,1]],P=[0,0,0,0,0,0];
const W=Q.map(q=>P.map((p,i)=>[p,q[i]]));
assert.equal(new Set(W.map(obs)).size,1);
const joint=W.map(w=>JSON.stringify(sig(2,w)));
const separate=W.map(w=>JSON.stringify([sig(2,w.map(t=>t[0]),false),sig(2,w.map(t=>t[1]),false)]));
assert.equal(new Set(joint).size,2);assert.equal(new Set(separate).size,3);
const full=transfer(6),f=obs(W[0]),classCounts=[];
for(const [s,n] of full){const [fiber,g]=JSON.parse(s);if(fiber===f)classCounts.push(n.toString());}
assert.deepEqual(classCounts.sort(),['1','2']);
let counts=new Map([[JSON.stringify([0,0,0,0,0,0]),1n]]);
for(let step=1;step<=6;step++){
  const next=new Map();
  for(const [v,n] of counts){const x=JSON.parse(v);for(let i=0;i<6;i++)for(const sign of [-1,1]){
    const y=x.slice();y[i]+=sign;const k=JSON.stringify(y);next.set(k,(next.get(k)||0n)+n);
  }}counts=next;
}
assert.equal(counts.get(JSON.stringify([6,0,0,0,0,0])),1n);
assert.equal(counts.get(JSON.stringify([2,0,0,0,0,0])),4665n);
console.log('STAGE402B_COUPLED_TRANSFER_PASS '+JSON.stringify({m_max:6,paired_words:words,class_count_comparisons:comparisons,witness:{m:6,K:4,total:3,joint_classes:2,independent_classes:3,joint_class_sizes:[2,1]},native_X6_BRC_N6_6E1:'1',native_X6_BRC_N6_2E1:'4665'}));
