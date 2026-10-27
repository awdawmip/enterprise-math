// EC48K: exact integer exhaustive certificate for one-bit horizon-two support equality.
// Run with Node.js: node VERIFY.js. Every numerator below has common denominator 12.
"use strict";
const assert = (p, why) => { if (!p) throw Error(why); };
const P=[3,1,1,3,2,2], Q=[1,3,3,1,2,2], hist=[0,0,1,1,2,2];
assert(P.reduce((a,b)=>a+b,0)===12 && Q.reduce((a,b)=>a+b,0)===12,"mass");
assert(P.every(x=>x>0)&&Q.every(x=>x>0),"strict positivity");
const weights=[];
for(const a of [-2,-1,0,1,2]) for(const b of [-2,-1,0,1,2])
 for(const c of [-1,0,1]) for(const d of [-1,0,1]) weights.push([a,b,c,d]);
weights.push([16,-16,-1,-1]); // 16 times J=(alpha-beta)-(tauP+tauQ)/16
const ternary = [];
for(let i=0;i<27;i++){let v=i;const ar=[];for(let h=0;h<3;h++){ar.push(v%3);v=Math.floor(v/3)}ternary.push(ar)}
function readout(first,terminalMask){
 const obs=[0,0,0,0];
 for(let i=0;i<6;i++){
  const action=first[hist[i]];
  const accept=action===2 ? ((terminalMask>>i)&1) : (action===1?1:0);
  const time=action===2?2:1;
  obs[0]+=P[i]*accept;obs[1]+=Q[i]*accept;
  obs[2]+=P[i]*time;obs[3]+=Q[i]*time;
 }
 return obs; // common denominator 12
}
const policies=[];
for(const first of ternary) for(let mask=0;mask<64;mask++) policies.push(readout(first,mask));
assert(policies.length===1728,"policy count");
function score(obs,w){return obs.reduce((s,x,i)=>s+x*w[i],0)}
function fullEnumerated(w){let m=-Infinity;for(const o of policies)m=Math.max(m,score(o,w));return m}
function oneBitConstructed(w){
 let optimum=0;
 const actions=[];
 for(let h=0;h<3;h++){
  let p=0,q=0,terminal=0;
  for(let i=0;i<6;i++)if(hist[i]===h){
   p+=P[i];q+=Q[i];
   terminal+=Math.max(0,w[0]*P[i]+w[1]*Q[i]);
  }
  const base=w[2]*p+w[3]*q;
  const stop=base+Math.max(0,w[0]*p+w[1]*q);
  const cont=2*base+terminal;
  const bit=cont>stop?1:0; // bit 1 = continue, 0 = optimal stop
  optimum+=Math.max(stop,cont); actions.push(bit);
 }
 // At t=1 bit 0 stops; accept iff w[0]*(P_h/Q_h)+w[1]>0.
 // At t=2 bit is ignored; accept iff w[0]*(P_i/Q_i)+w[1]>0.
 return {optimum,actions};
}
for(const w of weights){
 const brute=fullEnumerated(w), bit=oneBitConstructed(w).optimum;
 assert(brute===bit, "support mismatch "+JSON.stringify({w,brute,bit}));
}
const w=[16,-16,-1,-1], full=oneBitConstructed(w);
const bitPolicy=readout([2,2,0], (1<<0)|(1<<3));
assert(JSON.stringify(bitPolicy)===JSON.stringify([6,2,20,20]),"exact bit witness");
assert(full.optimum===24 && score(bitPolicy,w)===24,"full support");
let lrBest=-Infinity;
for(const firstAction of [0,1,2]){
 for(let mask=0;mask<64;mask++){
  // equal-ratio terminal bits can be pooled; this is a permissive upper bound.
  lrBest=Math.max(lrBest,score(readout([firstAction,firstAction,firstAction],mask),w));
 }
}
assert(lrBest===16,"LR-only support");
const report={
 schema:"EC48K_HORIZON2_ONE_BIT_SUPPORT_EXACT_V1",
 source_mass_denominator:12,
 P_numerators:P,Q_numerators:Q,history:hist,
 deterministic_full_policies:policies.length,
 support_vectors_tested:weights.length,
 exact_support_equalities:weights.length,
 explicit_objective_w_times_16:w,
 optimal_first_history_bits:full.actions,
 full_and_one_bit_score_times_192:full.optimum,
 LR_only_score_times_192:lrBest,
 explicit_one_bit_readout:{alpha:"1/2",beta:"1/6",tauP:"5/3",tauQ:"5/3"},
 full_J:"1/8",LR_only_J:"1/12",strict_improvement_over_LR:"1/24",
 scope:"Finite 3-history, 6-positive-leaf fixture. The all-finite-model theorem is proved symbolically in PROOF.md.",
 failures:0
};
console.log(JSON.stringify(report,null,2));
