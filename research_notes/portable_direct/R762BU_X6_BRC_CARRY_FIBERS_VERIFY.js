'use strict';
// Exact integer/Boolean verification of bounded-hop native X6 coordinate observation.
const assert=require('node:assert/strict');
const n=6, axes=[0,1,2,3,4,5];
const triples=[];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++)triples.push([i,j,k]);
const steps=[];for(let i=0;i<n;i++)for(const sign of [-1,1]){
  const v=Array(n).fill(0);v[i]=sign;steps.push(v);
}
const key=v=>v.join(',');
const vec=k=>k.split(',').map(Number);
const can=(z,S)=>{const a=S.map(i=>z[i]);const d=Math.min(...a);return a.map(v=>v-d);};
const sig=(z,H)=>H.map(S=>can(z,S).join(',')).join('|');
const can6=z=>can(z,axes).join(',');
function comp(H){
  const p=axes.slice();function root(x){while(p[x]!=x)x=p[x];return x;}
  for(const S of H)for(let k=1;k<3;k++)p[root(S[k])]=root(S[0]);
  return new Set(axes.map(root)).size;
}
let connected=0;let connTypes={};let disconnected=0;let oneExample;
for(let a=0;a<20;a++)for(let b=a+1;b<20;b++)for(let c=b+1;c<20;c++){
  const H=[triples[a],triples[b],triples[c]];
  if(comp(H)!=1){disconnected++;continue;}
  connected++;if(!oneExample)oneExample=H;
  const [A,B,C]=H.map(S=>new Set(S));
  const intersection=(X,Y)=>[...X].filter(x=>Y.has(x)).length;
  const pattern=[intersection(A,B),intersection(B,C),intersection(A,C)].sort().join('')+'T'+[...A].filter(x=>B.has(x)&&C.has(x)).length;
  connTypes[pattern]=(connTypes[pattern]||0)+1;
}
assert.equal(triples.length,20);
assert.equal(connected,480);
assert.equal(disconnected,660);
assert.deepEqual(connTypes,{'012T0':180,'111T0':120,'112T1':180});
// m-step paths are independently counted by exact integer DP, not by
// explicitly materializing 12^m ordered paths.
let states=new Map([[key(Array(n).fill(0)),1]]);
const budgets=[];let m3;
for(let m=0;m<=9;m++){
  const q=Math.floor(m/3)+1;
  const fibers=new Map();let sum=0;
  for(const [k,paths] of states){
    const z=vec(k), r=can6(z);
    if(!fibers.has(r))fibers.set(r,[]);
    fibers.get(r).push({z,paths});sum+=paths;
    assert.equal(z.reduce((a,b)=>a+Math.abs(b),0)<=m,true);
    assert.equal((m-z.reduce((a,b)=>a+Math.abs(b),0))%2,0);
  }
  assert.equal(sum,12**m);
  const sizes={};let max=0;let witnesses=[];
  for(const f of fibers.values()){
    max=Math.max(max,f.length);sizes[f.length]=(sizes[f.length]||0)+1;
    const residues=new Set(f.map(x=>((x.z[0]%q)+q)%q));
    assert.equal(residues.size,f.length,'modulus '+q+' failed at m='+m);
    if(f.length===q && witnesses.length===0) witnesses=f.map(x=>x.z);
  }
  assert.equal(max,q,'maximal fiber wrong at m='+m);
  budgets.push({m,q,maxFiber:max,endpoints:states.size,relativeClasses:fibers.size,paths:sum,distribution:sizes});
  if(m===3){
    assert.equal(states.size,304);assert.equal(fibers.size,284);
    const cl={};for(const f of fibers.values()){
      const type=f.length+':'+f.reduce((a,x)=>a+x.paths,0);cl[type]=(cl[type]||0)+1;
    }
    assert.deepEqual(cl,{'1:1':12,'1:3':120,'1:6':120,'1:33':12,'2:12':20});
    const fullSigMap=new Map();const quotientToFull=new Map();
    for(const [k] of states){
      const z=vec(k),f=sig(z,triples),r=can6(z);
      if(fullSigMap.has(f))assert.equal(fullSigMap.get(f),r);else fullSigMap.set(f,r);
      if(quotientToFull.has(r))assert.equal(quotientToFull.get(r),f);else quotientToFull.set(r,f);
    }
    assert.equal(fullSigMap.size,284);
    for(let a=0;a<20;a++)for(let b=a+1;b<20;b++)for(let c=b+1;c<20;c++){
      const H=[triples[a],triples[b],triples[c]];
      if(comp(H)!==1)continue;
      const local=new Map();
      for(const [k] of states){
        const z=vec(k),s=sig(z,H),r=can6(z);
        if(local.has(s))assert.equal(local.get(s),r);else local.set(s,r);
      }
      assert.equal(local.size,284);
    }
    m3={classes:cl,conditionalPaths:12**3,optimalTripleObserverFamilies:connected,fullSignatureFibers:fullSigMap.size,witnesses:[[[1,1,1,0,0,0],[0,0,0,-1,-1,-1]]]};
  }
  if(m===9)break;
  let next=new Map();
  for(const [k,count] of states){const z=vec(k);for(const e of steps){const zz=z.map((v,i)=>v+e[i]);const kk=key(zz);next.set(kk,(next.get(kk)||0)+count);}}
  states=next;
}
console.log(JSON.stringify({schema:'R762BU_EXACT_FINITE_VERIFIER_V1',inputs:{nativeAxes:6,steps:12,triples:20,maxSteps:9},observer:{minimalConnectedPanels:3,connectedTripletFamilies:480,disconnectedTripletFamilies:660,connectedPatterns:connTypes,example:oneExample.map(S=>S.map(i=>i+1))},m3,budgets},null,2));