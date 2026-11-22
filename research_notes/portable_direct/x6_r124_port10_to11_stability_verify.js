#!/usr/bin/env node
"use strict";
// R124 exact six-pair finite verification. The unbounded proof is in the Markdown file.
const verify=function verify(){
 const cases=[10,11,22],w=[1n,3n,4n,18n],den=[4n,5n,19n,7n,21n,22n];
 const port=([x,y,z])=>Math.max(Math.max(x,0)+Math.max(y,0)+Math.max(z,0),Math.max(-x,0)+Math.max(-y,0)+Math.max(-z,0));
 const gap=([x,y,z])=>{const h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z];return [h[1]-h[0],h[2]-h[0],h[3]-h[0],h[2]-h[1],h[3]-h[1],h[3]-h[2]].map(t=>BigInt(Math.abs(t)))};
 const cmp=(a,b)=>a[0]*b[1]-b[0]*a[1];
 const gcd=(a,b)=>b===0n?a:gcd(b,a%b);
 const red=(a)=>{const z=gcd(a[0],a[1]);return [String(a[0]/z),String(a[1]/z)]};
 const score=(a)=>gap(a).reduce((v,g,i)=>cmp([g,den[i]],v)>0n?[g,den[i]]:v,[0n,1n]);
 const out=[];
 for(const p of cases) {
  const all=[];
  for(let x=-p;x<=p;x++)for(let y=-p;y<=p;y++)for(let z=-p;z<=p;z++){
   if(!(x||y||z) || (x||y||z)<0)continue;
   const a=[x,y,z];if(port(a)>p)continue;
   all.push({a,F:score(a)});
  }
  const eta=all.reduce((m,t)=>cmp(t.F,m)<0n?t.F:m,all[0].F);
  const near=all.filter(t=>2n*t.F[0]*eta[1]<3n*eta[0]*t.F[1]);
  const outside=all.filter(t=>2n*t.F[0]*eta[1]>=3n*eta[0]*t.F[1]);
  const maxNear=near.reduce((m,t)=>cmp(t.F,m)>0n?t.F:m,near[0].F);
  const minOutside=outside.reduce((m,t)=>cmp(t.F,m)<0n?t.F:m,outside[0].F);
  out.push({p,population:all.length,eta:red(eta),near:near.map(t=>({a:t.a,F:red(t.F)})),max_near_score:red(maxNear),min_outside_score:red(minOutside),min_outside_witnesses:outside.filter(t=>cmp(t.F,minOutside)===0n).map(t=>t.a)});
 }
 const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
 const expected=[[1,-3,1],[1,0,0],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[9,-5,1],[9,-2,0]];
 if(!eq(out[0].near.map(t=>t.a),expected) || !eq(out[0].eta,["11","19"]) || !eq(out[0].max_near_score,["19","22"]) || !eq(out[0].min_outside_score,["18","19"]))throw Error("p10 mismatch");
 if(!eq(out[1].eta,["1","4"])||!eq(out[1].near.map(t=>t.a),[[10,-5,1]])||out[1].population!==2541)throw Error("p11 mismatch");
 if(!eq(out[2].eta,["1","4"])||!eq(out[2].near.map(t=>t.a),[[10,-5,1]])||!eq(out[2].min_outside_score,["1","2"])||out[2].population!==18997)throw Error("p22 mismatch");
 if(port([10,-5,1])!==11 || !eq(gap([10,-5,1]).map(String),["1","0","1","1","0","1"])) throw Error("anchor mismatch");
 return {schema:"X6_R124_PORT10_TO11_ROBUST_COLLAPSE_EXACT_V1",status:"PASS",observer:"six positive pair capacities derived from four positive channel weights; unoriented integer triples modulo sign only",weight:w.map(String),capacities:den.map(String),anchor:[10,-5,1],anchor_port:11,anchor_gaps:gap([10,-5,1]).map(String),finite_replay:out,analytic_global_isolation:"For all nonzero integer a != +/-(10,-5,1), F_w0(a)>=1/2; proof is in the companion Markdown.",relative_stability:{all_p_ge_11:"rho <= 1/7",port10_and_all_larger:"rho < 1/362",port10_inside_margin:"1/362",port10_outside_margin:"1/23"},limitations:"Finite replay p=10,11,22; unbounded p>=11 comes from the written integer proof; no independent review and no native X6 dynamics"};
};
console.log(JSON.stringify(verify(),null,2));
