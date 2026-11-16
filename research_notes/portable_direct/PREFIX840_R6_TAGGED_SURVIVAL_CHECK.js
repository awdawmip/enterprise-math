'use strict';
// PREFIX-840: independent named-subset Q-only BRC transitions; exact BigInt regression.
const assert = require('assert').strict;
function* assignments(p, alphabet=[1,2,3]){
  for(let k=0;k<alphabet.length**p;k++){
    let x=k,w=[];for(let i=0;i<p;i++){w.push(alphabet[x%alphabet.length]);x=Math.floor(x/alphabet.length)}yield w;
  }
}
function popcount(x){let n=0;while(x){x&=x-1;n++}return n}
function channels(p,w,a,b,horizon){
  const all=(1<<p)-1;let state=new Map([[all*2,1n]]),out=[];
  for(let t=1;t<=horizon;t++){
    const next=new Map();
    for(const [key,mass] of state){
      const mask=Math.floor(key/2),mark=key&1,occ=popcount(mask)+mark;
      for(let i=0;i<p;i++)if(mask&(1<<i)){
        const to=(mask^(1<<i))*2+mark;
        next.set(to,(next.get(to)||0n)+mass*BigInt(w[i]));
      }
      if(mark){const to=mask*2;next.set(to,(next.get(to)||0n)+mass*BigInt(b))}
      if(!mark && occ<p){const to=mask*2+1;next.set(to,(next.get(to)||0n)+mass*BigInt(a))}
    }
    state=next;
    const wantMark=t%2===0?1:0,wantOccupancy=t%2===0?p:p-1;
    let G=0n;const Gi=Array(p).fill(0n);
    for(const [key,mass] of state){
      const mask=Math.floor(key/2),mark=key&1;
      if(mark===wantMark && popcount(mask)+mark===wantOccupancy){
        G+=mass;for(let i=0;i<p;i++)if(mask&(1<<i))Gi[i]+=mass;
      }
    }
    out.push({t,G,Gi});
  }
  return out;
}
let configurations=0,timeChecks=0,scalarChecks=0,recoveredChecks=0,sample=[];
for(let p=1;p<=5;p++)for(const w of assignments(p))for(let a=1;a<=3;a++)for(let b=1;b<=3;b++){
  configurations++;
  const e1=w.reduce((x,y)=>x+BigInt(y),0n);
  for(const {t,G,Gi} of channels(p,w,a,b,9)){
    timeChecks++;
    const c=BigInt(a)**BigInt(Math.floor(t/2))*BigInt(b)**BigInt(Math.floor((t-1)/2));
    assert.equal(G,c*e1);scalarChecks++;
    for(let i=0;i<p;i++){assert.equal(Gi[i],c*(e1-BigInt(w[i])));scalarChecks++}
    const restored=[];
    for(let i=0;i<p-1;i++){
      assert.equal((G-Gi[i])%c,0n);
      restored.push((G-Gi[i])/c);recoveredChecks++;
    }
    restored.push(G/c-restored.reduce((x,y)=>x+y,0n));
    assert.deepEqual(restored,w.map(BigInt));recoveredChecks++;
    if(p===3 && w.join(',')==='1,2,3' && a===2 && b===3 && [1,2,3,6].includes(t))
      sample.push({t,G:G.toString(),Gi:Gi.map(String)});
  }
}
console.log(JSON.stringify({
  schema:"PREFIX840_EXACT_BRC_TAGGED_ONE_DELETION_CHECK_V1",
  claim:"G(t)=c_t sum_i w_i; G_i(t)=c_t sum_{j!=i}w_j; p-1 named probes and G recover all named weights at any t>=1.",
  verified:{p_min:1,p_max:5,weight_alphabet:[1,2,3],a_values:[1,2,3],b_values:[1,2,3],
    time_range:[1,9],configurations,timeChecks,scalarChecks,recoveredChecks,
    assertions:"ALL_EXACT_ASSERTIONS_PASSED"},
  sample:{p:3,weights:[1,2,3],a:2,b:3,rows:sample}
},null,2));
