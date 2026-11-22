"use strict";
// EC49FXM: every consecutive D_k, whole-activation symbol distance >=4.
// Run: node EC49FXM_SYMBOL_R4_INTERVAL_VERIFY.js
const mod=(x,n)=>(x%n+n)%n;
const SMALL2=[1,3,4,9,10,13,14,19,25,27,33,40,43,50];
const SMALL4=[5,9,10,12,14,15,18,23,26,30,31,33,36,39,41,48,49];
function optimum(k){
 if(k<=2)return 14;
 if(k<=4)return 17;
 if(k<=45)return 20;
 return Math.min(25,k-25);
}
function safeResidues(k,i){
 const a=[];for(let x=0;x<55;x++)if(x%5===i&&mod(2*x,55)>=k)a.push(x);
 return a;
}
function activationSet(k){
 if(k<=2)return SMALL2.slice();
 if(k<=4)return SMALL4.slice();
 const S=[];
 for(let i=0;i<5;i++){
  const safe=safeResidues(k,i);
  if(safe.length>=2)for(const x of safe.slice(-2))S.push(x,x+55);
  else for(let h=0;h<5;h++)S.push(i+5*h);
 }
 return S.sort((a,b)=>a-b);
}
function symbolDistance(S,d,i,j){
 let n=0;for(const t of S)
 if((t%5===i&&t%11!==j)||(mod(d-t,5)===i&&mod(d-t,11)!==j))n++;
 return n;
}
function verify(){
 const rows=[];let checks=0;
 for(let k=1;k<=55;k++){
  const S=activationSet(k);
  if(S.length!==optimum(k)||new Set(S).size!==S.length||S.some(t=>t<0||t>=110))
   throw Error("Invalid witness k="+k);
  let min=1000;
  for(let d=0;d<k;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++){
   const z=symbolDistance(S,d,i,j);checks++;min=Math.min(min,z);
   if(z<4)throw Error("FAIL "+JSON.stringify({k,d,i,j,z}));
  }
  if(min!==4)throw Error("Unexpected minimum k="+k);
  rows.push({k,minimum_activations:S.length,minimum_observed_symbol_distance:min,sites:S});
 }
 if(checks!==84700)throw Error("Wrong row count");
 const smallWitnesses=[2,4].map(k=>({
  k,sites:activationSet(k),
  min_over_missing_column_by_phase_and_color:
   Array.from({length:k},(_,d)=>
    Array.from({length:5},(_,i)=>
     Math.min(...Array.from({length:11},(_,j)=>symbolDistance(activationSet(k),d,i,j)))))
 }));
 const safeCounts=[45,46,47,48,49,50,51,55].map(k=>({
  k,safe_distinct_residues_by_color:Array.from({length:5},(_,i)=>safeResidues(k,i).length)
 }));
 return {
  schema:"EC49FXM_SYMBOL_R4_EXACT_VERIFICATION_V1",
  frozen_scientific_pin:"BRC16943",
  parent:"EC49FXL@PR-2986",
  universe:"Z/110; physical activation is two-bit symbol",
  metric:"symbol Hamming distance",
  requirement:"at least 4; e.g. correct one unknown whole activation plus erase one known whole activation",
  quantifiers:"all 55 k; all d∈D_k; five colors i; eleven columns j",
  precise_integer_row_evaluations:checks,
  small_explicit_witnesses:smallWitnesses,
  self_row_lower_bound_safe_residue_counts:safeCounts,
  cost_profile:rows,
  result:"PASS",
  claim_strength:"AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED"
 };
}
if(typeof module!=="undefined"&&require.main===module)
 process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
