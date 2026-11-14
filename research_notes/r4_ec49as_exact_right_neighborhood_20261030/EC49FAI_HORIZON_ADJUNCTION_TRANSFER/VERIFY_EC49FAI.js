// EC49FAI: exact signed-X6 horizon-adjunction audit; Node.js, no external dependencies.
// Native operations and nine-history observer reproduce frozen SCREEN_H5_EC49EXJ.py,
// original Git blob 0e83eac43199e5854d462d1928aba6a146db5261.
// Author-side calculation only; no Source-native Result or Driver authority.
"use strict";
const OPS={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const HIST=[["N",0],["N",1],["N",2],["A",0],["A",2],["B",0],["B",1],["AB",0],["BA",0]];
const BUCKETS=["N","A","B","AB","BA"],T4=[1836687,1867942,1872656,1873981],T2=[1836425,1866380];
function signature(steps){
 let result=0,multiplier=1;
 for(const [initial,initialPrev] of HIST){
  let state=initial,prev=initialPrev;
  for(const s of steps){
   if(prev===1&&s===2){if(state==="N")state="A";else if(state==="B")state="BA";}
   else if(prev===2&&s===1){if(state==="N")state="B";else if(state==="A")state="AB";}
   prev=s; // use signed axis, not absolute axis
  }
  result+=BUCKETS.indexOf(state)*multiplier;multiplier*=5;
 }
 return result;
}
function words(h,key,typ){
 const [u,v,w]=key,r=u+v-h-1,na=w-1,nf=h+1-v-2*w,ng=h+1-u;
 if(Math.min(r,na,nf,ng)<0)return [];
 const target=(typ===4?T4:T2),counts={a:na,c:0,d:r,e:w,f:nf,g:ng},out=[];
 function rec(word){
  if(Object.values(counts).every(x=>x===0)){
   const steps=[...word].flatMap(c=>OPS[c]),s=signature(steps);
   if(target.includes(s))out.push({word,steps,signature:s});
   return;
  }
  for(const c of Object.keys(counts))if(counts[c]>0){counts[c]--;rec(word+c);counts[c]++;}
 }
 for(let nc=0;nc<=r;nc++){counts.c=nc;counts.d=r-nc;rec("");}
 return out;
}
function exactCover(masks,ncolors){
 let dp=Array(1<<ncolors).fill(999999);dp[0]=0;
 for(const mask of masks){
  const next=dp.slice();
  for(let s=0;s<dp.length;s++)next[s|mask]=Math.min(next[s|mask],dp[s]+1);
  dp=next;
 }
 if(dp[dp.length-1]===999999)throw Error("Mandatory signature missing");
 return dp[dp.length-1];
}
function main(){
 const key=[4,5,1],old=words(7,key,4),newer=words(8,key,2),next=words(9,key,4);
 if(old.length!==420||newer.length!==147||next.length!==0)throw Error("word-count regression");
 const oldColors=old.map(x=>({...x,color:T4.indexOf(x.signature)}));
 const all=oldColors.concat(newer.map(x=>({...x,color:4+T2.indexOf(x.signature)})));
 if(new Set(old.map(x=>x.signature)).size!==4||new Set(newer.map(x=>x.signature)).size!==2)throw Error("color coverage");
 for(const x of all)if(x.steps.length!==18)throw Error("signed length mismatch");
 const profile=[];
 for(let d=1;d<=18;d++){
  const pOld=new Map(),pBoth=new Map();
  for(const x of all){
   const p=x.steps.slice(0,d).join(",");
   if(x.color<4)pOld.set(p,(pOld.get(p)||0)|(1<<x.color));
   pBoth.set(p,(pBoth.get(p)||0)|(1<<x.color));
  }
  profile.push({depth:d,q_h7:exactCover([...pOld.values()],4),
   q_h7_h8:exactCover([...pBoth.values()],6),
   distinct_old_prefixes:pOld.size,distinct_combined_prefixes:pBoth.size});
 }
 for(const r of profile){
  const a=r.depth<=14?2:4,b=r.depth<=14?2:(r.depth===15?4:6);
  if(r.q_h7!==a||r.q_h7_h8!==b)throw Error("profile mismatch at "+r.depth);
 }
 return {
  status:"EXACT_INTEGER_ENUMERATION_PASS",
  scope:"Frozen signed-X6 primitive operations and T4/T2 observer; K=(4,5,1), h7/h8 and h9 raw feasibility.",
  frozen_science_commit:"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
  original_generator_blob:"0e83eac43199e5854d462d1928aba6a146db5261",
  cache_key:key,feasibility_interval_inclusive:[6,8],primitive_word_length:18,
  admissible_word_counts:{h7_T4:old.length,h8_T2:newer.length,h9_any_type:next.length},
  observer_signatures:{h7_T4:T4,h8_T2:T2},
  one_h8_word_per_observer:T2.map(t=>({signature:t,word:newer.find(x=>x.signature===t).word})),
  exact_prefix_cover_profile:profile,
  classification:"AUTHOR_FINITE_DERIVATION_UNREVIEWED_NOT_ADMITTED"
 };
}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module)
 process.stdout.write(JSON.stringify(main(),null,2)+"\n");
