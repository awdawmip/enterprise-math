"use strict";
const assert=(cond,message)=>{if(!cond)throw Error(message);};
function binom(n,k){if(k<0||k>n)return 0n;k=Math.min(k,n-k);let x=1n;for(let j=1;j<=k;j++)x=x*BigInt(n-j+1)/BigInt(j);return x;}
function add(a,b){let r=Array(Math.max(a.length,b.length)).fill(0n);a.forEach((x,i)=>r[i]+=x);b.forEach((x,i)=>r[i]+=x);return r;}
function mul(a,b){let r=Array(a.length+b.length-1).fill(0n);a.forEach((x,i)=>b.forEach((y,j)=>r[i+j]+=x*y));return r;}
function K(i) {
 const d=[-binom(4,i)+binom(2,i-1),binom(5,i-1)-binom(5,i-2),binom(7,i-2),-binom(9,i-3)];
 let r=[0n];for(let j=1;j<=4;j++){let k=i+1-j;if(k<0)continue;let v=Array(i-1).fill(0n);for(let a=0;a<=k;a++)v.push(-d[j-1]*binom(k,a));r=add(r,v);}return r;
}
const kernels=Array.from({length:12},(_,i)=>K(i+1));
function shift(w){const z=Array(6).fill(0);for(const i of w)z[Math.floor((i-1)/2)]+=i%2?1:-1;return z;}
function weight(w){let r=[1n];for(const i of w)r=mul(r,kernels[i-1]);return r;}
function trunc(a,d){return Array.from({length:d+1},(_,i)=>(a[i]||0n).toString());}
function key(w,d){return [shift(w).join(","),w.reduce((a,b)=>a+b,0),trunc(weight(w),d).join(",")].join("|");}
function tag(w){let z=1n;for(const i of w)z=z*12n+BigInt(i-1);return z;}
function suffixes(max,alphabet,visit,w=[]){visit(w);if(w.length===max)return;for(const a of alphabet){w.push(a);suffixes(max,alphabet,visit,w);w.pop();}}
function run(){
 const wA=Array.from({length:14},(_,i)=>i%2?2:1),wB=Array.from({length:6},(_,i)=>i%2?4:3);
 assert(!wA.every((x,i)=>x===wB[i]),"distinct histories");
 assert(wA.reduce((a,b)=>a+b,0)===21&&wB.reduce((a,b)=>a+b,0)===21,"level21");
 assert(shift(wA).every(x=>x===0)&&shift(wB).every(x=>x===0),"native pure axis returns");
 assert(kernels[0][0]===2n&&kernels[1][1]===-1n&&kernels[2][2]===-8n&&kernels[3][3]===-11n,"source freeze leading coefficients");
 function valuation(a){return a.findIndex(x=>x!==0n);}
 const va=valuation(weight(wA)),vb=valuation(weight(wB));
 assert(va===7&&vb===15,"valuation target");
 const trial=[];
 for(let d=0;d<=7;d++){
   let equal=key(wA,d)===key(wB,d),future=0;
   suffixes(3,[1,2,3,4],v=>{
      if(d<=6){assert(key(wA.concat(v),d)===key(wB.concat(v),d),"future descent");future++;}
   });
   assert(equal===(d<=6),"boundary degree");
   trial.push({d,equivalent_now:equal,checked_future_suffixes:future});
 }
 const inverse=[];
 for(let d=0;d<=7;d++){
    let b=[1n,1n],inv=Array.from({length:d+1},(_,i)=>i%2===0?1n:-1n);
    let pr=trunc(mul(b,inv),d);assert(pr[0]==="1"&&pr.slice(1).every(x=>x==="0"),"B0 invertibility");
    inverse.push(d);
 }
 assert(tag(wA)!==tag(wB),"path tag distinguishes");
 return {schema:"EM_R619_SIGNED_BRC_TRUNCATED_FUTURE_QUOTIENT_V1",source_pin:"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",arithmetic:"exact JavaScript BigInt",K1:kernels[0].map(String),K2:kernels[1].map(String),
 K3:kernels[2].map(String),K4:kernels[3].map(String),wA:wA.join(","),wB:wB.join(","),level_s:21,
 endpoint:"0,0,0,0,0,0",valuation_K_wA:va,valuation_K_wB:vb,
 source_tags:[tag(wA).toString(),tag(wB).toString()],
 truncation_boundary:trial,unit_inverse_degrees:inverse,
 pass:"R619_SIGNED_BRC_FUTURE_JET_QUOTIENT_EXACT_PASS"};
}
if(typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(run(),null,2));
