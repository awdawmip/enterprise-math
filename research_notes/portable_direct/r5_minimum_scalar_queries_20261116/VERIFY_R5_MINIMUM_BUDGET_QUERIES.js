"use strict";
// Structural support check only; scalar-count injectivity is inherited from the pinned prior exact DP.
const verify = function verify(){
 function E(k){if(k>=214&&k<=221)return [3,8,9,10,27];if(k===222)return [27];if(k>=223&&k<=291)return [25,27];if(k>=293&&k<=314)return [15,17];if(k>=214&&k<=954)return [];throw new Error("budget out of domain")}
 const budgets=Array.from({length:954-214+1},(_,i)=>i+214);
 const union=(a,b)=>new Set([...a,...b]).size;
 let max1=0,max2=0,maxPairs=0,allPairs=0;
 for(let i=0;i<budgets.length;i++){
  max1=Math.max(max1,E(budgets[i]).length);
  for(let j=i+1;j<budgets.length;j++){
   allPairs++;const n=union(E(budgets[i]),E(budgets[j]));
   if(n>max2){max2=n;maxPairs=1}
   else if(n===max2){maxPairs++}
  }
 }
 const A=budgets.filter(k=>E(k).includes(3)),B=budgets.filter(k=>E(k).includes(25)),C=budgets.filter(k=>E(k).includes(15));
 const U=[3,8,9,10,15,17,25,27];
 function project(mask,k){const s=new Set(E(k));let bits=0;for(let i=0;i<U.length;i++)if((mask&(1<<i))&&s.has(U[i]))bits|=1<<i;return bits}
 const pair=new Set(),triple=new Set();
 for(let mask=0;mask<256;mask++){pair.add([project(mask,214),project(mask,294)].join(":"));triple.add([project(mask,214),project(mask,223),project(mask,294)].join(":"))}
 const out={input:"R5 derived 954-event optimizer-family effective-cut spectrum; K=214..954",budgets:budgets.length,unordered_pairs_checked:allPairs,max_single_support:max1,max_two_support:max2,two_support_maximizing_pairs:maxPairs,mandatory_windows:{A:[214,221],B:[223,291],C:[293,314]},structurally_eligible_triples:A.length*B.length*C.length,ideal_support_pair_214_294_signatures:pair.size,ideal_support_triple_214_223_294_signatures:triple.size,original_masks_per_certified_scalar_pair_signature:2**21,original_masks_per_certified_scalar_triple_signature:2**20};
 if(JSON.stringify([out.budgets,allPairs,max1,max2,maxPairs,out.structurally_eligible_triples,pair.size,triple.size])!==JSON.stringify([741,274170,5,7,176,12144,128,256]))throw new Error("exact structural check failed");
 return out;
};
console.log(JSON.stringify(verify(),null,2));
