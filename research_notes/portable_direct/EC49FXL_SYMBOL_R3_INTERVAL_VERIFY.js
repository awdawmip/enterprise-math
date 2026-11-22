"use strict";
// EC49FXL: 55 consecutive relative-phase sets, whole-activation symbol distance >= 3.
// Standalone: node EC49FXL_SYMBOL_R3_INTERVAL_VERIFY.js
// Frozen auxiliary science input: BRC16943. No external dependencies.
const mod=(x,n)=>(x%n+n)%n;
const W2=[4,5,13,19,35,40,43,44,46,47,53];
const W4=[3,5,7,10,14,15,21,23,24,31,33,36,54];
const X=[25,26,27,23,24], Y=[50,51,52,53,54], CUTOFF=[45,47,49,46,48];
function optimum(k) {
 if (k<=2) return 11;
 if (k<=4) return 13;
 if (k<=45) return 15;
 return Math.min(20,k-30);
}
function activationSet(k) {
 if(k<=2) return W2.slice();
 if(k<=4) return W4.slice();
 const S=[];
 for(let i=0;i<5;i++){
   if(k<=CUTOFF[i]) S.push(X[i],X[i]+55,Y[i]);
   else S.push(i,i+5,i+10,i+15);
 }
 return S.sort((a,b)=>a-b);
}
function symbolDistance(S,d,i,j) {
 let n=0;
 for(const t of S)
  if((t%5===i && t%11!==j) || (mod(d-t,5)===i && mod(d-t,11)!==j)) n++;
 return n;
}
function verify() {
 const rows=[];let evaluations=0;
 for(let k=1;k<=55;k++){
  const S=activationSet(k), expected=optimum(k);
  if(S.length!==expected || new Set(S).size!==expected || S.some(t=>t<0||t>=110))
   throw Error("Invalid site count/range at k="+k);
  let min=Infinity;
  for(let d=0;d<k;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++){
   const z=symbolDistance(S,d,i,j);
   evaluations++;min=Math.min(min,z);
   if(z<3) throw Error("Distance failure at "+JSON.stringify({k,d,i,j,z}));
  }
  if(min!==3)throw Error("Unexpected minimum at k="+k);
  if(k>=5) {
    const light=[];
    for(let i=0;i<5;i++)if(k<=CUTOFF[i]){
      light.push(i);
      for(const t of [X[i],X[i]+55,Y[i]])
       if(mod(2*t,55)<k)throw Error("Unsafe light self row "+JSON.stringify({k,i,t}));
    }
    for(let a=0;a<light.length;a++)for(let b=a+1;b<light.length;b++)
      if(X[light[a]]+X[light[b]]<k)
       throw Error("Light-pair collision "+JSON.stringify({k,a,b}));
    if(k>=46){
      const safe=Array.from({length:5},(_,i)=>{
        let z=0;for(let x=0;x<55;x++)if(x%5===i && mod(2*x,55)>=k)z++;
        return z;
      });
      const possibleLight=safe.filter(v=>v>=2).length;
      if(possibleLight!==light.length)throw Error("Lower-bound color count mismatch at k="+k);
    }
  }
  rows.push({k,minimum_activations:expected,minimum_observed_symbol_distance:min,sites:S});
 }
 if(evaluations!==84700)throw Error("Unexpected row count "+evaluations);
 const smallWitnesses=[2,4].map(k=>({
   k,
   sites:activationSet(k),
   min_over_missing_column_by_phase_and_color:
     Array.from({length:k},(_,d)=>
       Array.from({length:5},(_,i)=>
         Math.min(...Array.from({length:11},(_,j)=>symbolDistance(activationSet(k),d,i,j)))))
 }));
 const safeCounts=[45,46,47,48,49,50,51,55].map(k=>({
   k,
   safe_distinct_residues_by_color:Array.from({length:5},(_,i)=>{
    let c=0;for(let x=0;x<55;x++)if(x%5===i && mod(2*x,55)>=k)c++;
    return c;
   })
 }));
 return {
  schema:"EC49FXL_SYMBOL_R3_EXACT_VERIFICATION_V1",
  frozen_scientific_pin:"BRC16943",
  parent:"EC49FXK@168eca0a89415c3b2add265ba8a37727012b3b70",
  universe:"Z/110; left/right channel pair at each physical activation",
  metric:"symbol Hamming distance of full two-bit activation",
  requirement:"at least 3; corrects one unknown whole-activation error",
  quantifiers:"k=1..55; d in {0,...,k-1}; color i=0..4; missing column j=0..10",
  precise_integer_row_evaluations:evaluations,
  small_explicit_witnesses:smallWitnesses,
  self_row_lower_bound_safe_residue_counts:safeCounts,
  cost_profile:rows,
  result:"PASS",
  claim_strength:"AUTHOR_PROVED / EXACT_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED"
 };
}
if(typeof module!=="undefined" && require.main===module)
 process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
