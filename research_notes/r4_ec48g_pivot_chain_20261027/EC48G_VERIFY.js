'use strict';
// EC48G exact finite verifier: all ternary 3x3 sign templates.
// Integer arithmetic throughout; w4 is 4 times a decoder probability.
// Execute: node EC48G_VERIFY.js
const assert=require('assert');
const key=r=>r.join('');
function classify(S){
  const a=S.map(r=>r.map(v=>v>=0?1:0));
  const b=S.map(r=>r.map(v=>v>0?1:0));
  const C=new Set(S.flatMap((r,h)=>r.includes(0)?[]:[key(a[h])]));
  const K=Math.max(new Set(a.map(key)).size,new Set(b.map(key)).size);
  const D=new Map();const category=[];
  for(let h=0;h<S.length;h++){
    if(!S[h].includes(0)){category.push('N');continue;}
    const aa=key(a[h]),bb=key(b[h]);
    if(C.has(aa)&&C.has(bb)){category.push('A');continue;}
    D.set(bb+'>'+aa,{from:bb,to:aa});category.push(bb+'>'+aa);
  }
  if(D.size!==2||C.size===0||K<C.size+1)return null;
  for(const c of C){
    const I=[...D.values()].filter(x=>x.to===c&&!C.has(x.from));
    const O=[...D.values()].filter(x=>x.from===c&&!C.has(x.to));
    if(I.length===1&&O.length===1&&I[0]!==O[0]){
      return {K,C,D,category,a,b,c,I:I[0],O:O[0]};
    }
  }
  return null;
}
function verify(S,z){
  const n=classify(S);if(!n)return false;
  const {K,C,category,a,b,c,I,O}=n;
  const q0=S.map((r,h)=>r.map((_,y)=>1+(5*h+7*y)%4));
  const P=S.map((r,h)=>r.map((s,y)=>(2+s)*q0[h][y]));
  const Q=S.map((r,h)=>r.map((s,y)=>2*q0[h][y]));
  const plus=S.reduce((v,r,h)=>v+r.reduce((w,s,y)=>w+(s===1?q0[h][y]:0),0),0);
  const masses=[0,0,0];
  for(let h=0;h<3;h++)for(let y=0;y<3;y++)if(S[h][y]===0){
    const name=category[h];const idx=name==='A'?0:name===key(I.from.split('').map(Number))+'>'+key(I.to.split('').map(Number))?1:2;
    assert(idx===0||name===I.from+'>'+I.to||name===O.from+'>'+O.to);
    masses[idx]+=Q[h][y];
  }
  const extraWord=(w)=>[...w].map(v=>4*Number(v));
  const Cbank=new Map([...C].map(w=>[w,extraWord(w)]));
  for(let phase=0;phase<3;phase++)for(let t=0;t<=4;t++){
    const extra=phase===0?extraWord(I.from):phase===1?
      [...I.from].map((v,j)=>4*Number(v)+t*(Number(I.to[j])-Number(v))):
      [...O.from].map((v,j)=>4*Number(v)+t*(Number(O.to[j])-Number(v)));
    assert(Cbank.size+1<=K);
    const w=[];
    for(let h=0;h<3;h++){
      const cat=category[h];
      if(cat==='N')w.push(Cbank.get(key(a[h])));
      else if(cat==='A')w.push(phase===0?a[h].map((v,y)=>(4-t)*b[h][y]+t*v):Cbank.get(key(a[h])));
      else if(cat===I.from+'>'+I.to)w.push(phase===2?Cbank.get(c):extra);
      else if(cat===O.from+'>'+O.to)w.push(phase===2?extra:Cbank.get(c));
      else throw Error('unrecognized transition '+cat);
    }
    let gain=0,tie=0;
    for(let h=0;h<3;h++)for(let y=0;y<3;y++){
      assert(w[h][y]>=0&&w[h][y]<=4);
      if(S[h][y]!==0)assert.equal(w[h][y],S[h][y]>0?4:0);
      gain+=(P[h][y]-Q[h][y])*w[h][y];
      if(S[h][y]===0)tie+=Q[h][y]*w[h][y];
    }
    assert.equal(gain,4*plus);
    const expected=phase===0?t*masses[0]:phase===1?4*masses[0]+t*masses[1]:4*(masses[0]+masses[1])+t*masses[2];
    assert.equal(tie,expected);
  }
  return true;
}
let qualified=0,total=0;
for(let index=0;index<3**9;index++){
  let x=index;const S=Array.from({length:3},()=>Array(3));
  for(let h=0;h<3;h++)for(let y=0;y<3;y++){S[h][y]=(x%3)-1;x=Math.floor(x/3);}
  total++;if(verify(S,index))qualified++;
}
assert.equal(total,19683);assert.equal(qualified,108);
const witness={P:[[1,3],[1,2],[2,3]],Q:[[1,1],[1,1],[1,1]],K_hull:2,K_seed:2,central_r:'1',face:'alpha-beta=1/6; beta in [1/3,2/3]'};
console.log(JSON.stringify({status:'PASS',total_templates:total,qualified_pivot_templates:qualified,exact_policies_checked:qualified*15,arithmetic:'integer',witness}));
