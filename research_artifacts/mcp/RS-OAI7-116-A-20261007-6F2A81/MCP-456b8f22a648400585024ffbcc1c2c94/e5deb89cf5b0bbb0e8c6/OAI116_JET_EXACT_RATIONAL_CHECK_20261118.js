#!/usr/bin/env node
"use strict";
// Exact rational regression for RS-OAI7-116-A. No dependencies.
// Run: node OAI116_JET_EXACT_RATIONAL_CHECK_20261118.js
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a||1n;};
const F=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];};
const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
const sub=(a,b)=>add(a,mul(b,F(-1)));
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1];
const show=a=>a[0]+"/"+a[1];
const Z=()=>F(0),O=()=>F(1);
const e0=d=>Array.from({length:d},(_,q)=>q===0?O():Z());
const J=(i,v)=>{const d=v.length,out=Array.from({length:d},Z);
  for(let r=1;r<d;r++){let s=Z();
    for(let q=0;q<r;q++)s=add(s,mul(v[q],F((r-q-1)%2?-1:1,BigInt(i)**BigInt(r-q))));
    out[r]=mul(s,F(1,r));
  } return out;
};
const T=(i,d)=>Array.from({length:d},(_,r)=>Array.from({length:d},(_,q)=>
  q<r?F((r-q-1)%2?-1:1,BigInt(r)*BigInt(i)**BigInt(r-q)):Z()));
const mv=(M,v)=>M.map(row=>row.reduce((s,a,j)=>add(s,mul(a,v[j])),Z()));
const via=(w,d,operator)=>w.slice().reverse().reduce((v,i)=>operator(i,v),e0(d));
const assertVec=(a,b,desc)=>{if(a.length!==b.length||!a.every((x,r)=>eq(x,b[r])))throw Error(desc+": "+a.map(show)+" vs "+b.map(show));};
let count=0;
for(let d=1;d<=8;d++){
  for(let i=1;i<=4;i++){
    const matrix=T(i,d);
    for(let q=0;q<d;q++){const v=Array.from({length:d},(_,j)=>j===q?O():Z());
      assertVec(J(i,v),mv(matrix,v),"basis d="+d+",i="+i+",q="+q);count++;
    }
  }
  let words=[[]],prev=[[]];
  for(let k=1;k<=3;k++){prev=prev.flatMap(w=>[1,2,3].map(i=>[...w,i]));words.push(...prev);}
  for(const w of words){
    assertVec(via(w,d,J),via(w,d,(i,v)=>mv(T(i,d),v)),"word d="+d+",w="+w);count++;
  }
}
const c=via([1,2],4,(i,v)=>mv(T(i,4),v)).map((a,r)=>sub(a,via([2,1],4,(i,v)=>mv(T(i,4),v))[r]));
assertVec(c,[F(0),F(0),F(0),F(-1,24)],"commutator");
if(!eq(T(1,1)[0][0],F(0)))throw Error("d=1 jet");
if(eq(T(1,1)[0][0],F(1)))throw Error("exception not distinguished");
assertVec(via([1],2,J),[F(0),F(1)],"one letter");
console.log("PASS exact equalities="+count);
console.log("commutator jet="+c.map(show));
console.log("d=1 jet T=[0], exceptional singleton hitting T=[1]");
