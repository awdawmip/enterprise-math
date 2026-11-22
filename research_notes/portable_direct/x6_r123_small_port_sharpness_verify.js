#!/usr/bin/env node
"use strict";
// R123 full finite census on two exact positive integer weight vectors.
const verify=function verify(){
 const cases=[{p:2,w:[1,1,100,100],expected:[[0,2,-1],[1,-2,1],[1,0,0],[2,-1,0]],expectedEta:[48,101]},{p:10,w:[1,3,4,18],expected:[[1,-3,1],[1,0,0],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[9,-5,1],[9,-2,0]],expectedEta:[11,19]}];
 const port=([x,y,z])=>Math.max(Math.max(x,0)+Math.max(y,0)+Math.max(z,0),Math.max(-x,0)+Math.max(-y,0)+Math.max(-z,0));
 const gap=([x,y,z])=>{let h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z];return [Math.abs(h[1]),Math.abs(h[2]),Math.abs(h[3]),Math.abs(h[2]-h[1]),Math.abs(h[3]-h[1]),Math.abs(h[3]-h[2])]};
 const gcd=(x,y)=>y?gcd(y,x%y):x;
 const reduced=([x,y])=>{let z=gcd(x,y);return [x/z,y/z]};
 const less=(a,b)=>a[0]*b[1]<b[0]*a[1];
 const greater=(a,b)=>a[0]*b[1]>b[0]*a[1];
 const result=[];
 for(const spec of cases){
  let [A,B,C,D]=spec.w,den=[A+B,A+C,A+D,B+C,B+D,C+D],all=[];
  for(let x=-spec.p;x<=spec.p;x++)for(let y=-spec.p;y<=spec.p;y++)for(let z=-spec.p;z<=spec.p;z++){
    if(!x&&!y&&!z)continue; if((x||y||z)<0)continue;let a=[x,y,z];if(port(a)>spec.p)continue;
    let gg=gap(a),F=[0,1];
    for(let k=0;k<6;k++){let f=[gg[k],den[k]];if(greater(f,F))F=f}
    all.push({a,F:reduced(F)});
  }
  let eta=all[0].F;
  for(let r of all)if(less(r.F,eta))eta=r.F;
  let near=all.filter(r=>2*r.F[0]*eta[1]<3*eta[0]*r.F[1]).map(r=>({a:r.a,F:r.F}));
  let norm=v=>v.map(z=>z.join(",")).sort();
  if(JSON.stringify(norm(near.map(x=>x.a)))!==JSON.stringify(norm(spec.expected)))throw Error("direction list mismatch p="+spec.p);
  if(!(!less(eta,spec.expectedEta)&&!greater(eta,spec.expectedEta)))throw Error("eta mismatch p="+spec.p);
  result.push({port:spec.p,weights:spec.w,feasible_unoriented_directions:all.length,eta,threshold_3_over_2:reduced([3*eta[0],2*eta[1]]),strict_near_count:near.length,strict_near:near});
 }
 return {schema:"X6_R123_SMALL_PORT_SHARPNESS_EXACT_RATIONAL_V1",status:"PASS",date:"2026-11-23",cases:result,method:"full integer direction enumeration; exact integer cross-products for all six rational ratios",limits:"Port 2 upper bound is proved by R122; Port 10 witness proves count >=8, no global sharpness claimed"};
};
console.log(JSON.stringify(verify(),null,2));
