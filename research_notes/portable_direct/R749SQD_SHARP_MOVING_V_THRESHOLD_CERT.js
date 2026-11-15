#!/usr/bin/env node
'use strict';
function verifySharp(){
 const fs=[[-1,-1,-1,-2],[-1,-1,1,-2],[-1,1,-1,-2],[-1,1,1,-2],[1,-1,-1,-2],[1,-1,1,-4],[1,1,-1,-4],[1,1,1,-2]];
 const P=[];for(let h=-2;h<=2;h++)for(let u=-2;u<=2;u++)for(let v=-2;v<=2;v++)if(fs.every(([a,b,c,t])=>a*h+b*u+c*v>=t))P.push([h,u,v]);
 const pm=new Map();for(let i=0;i<P.length;i++)for(let j=i;j<P.length;j++){const key=P[i].map((x,k)=>x+P[j][k]).join(","),old=pm.get(key)||[];old.push([i,j]);pm.set(key,old);}
 const idx=new Set();for(const ps of pm.values())if(ps.length===1){idx.add(ps[0][0]);idx.add(ps[0][1]);}
 const F=[...idx].map(i=>P[i]),B=F.filter(x=>x[1]<2).map(([h,u,v])=>({h,d:2-u,v}));
 if(P.length!==33||F.length!==25||B.length!==23)throw Error("source reconstruction");
 const L=B.filter(x=>!(x.h===0&&x.d===1&&x.v===1)).map(x=>({...x,s:2*x.d-1-x.v,b0:x.h+x.d-x.v,b1:x.h+x.d-x.v}));
 L.push({h:0,d:2,v:0,s:3,b0:2,b1:1});
 if(L.length!==23||!L.some(x=>x.d===2&&x.v===2&&x.s===1)||!L.some(x=>x.d===1&&x.v===0&&x.s===1))throw Error("sharp witnesses");
 for(const x of L)if(x.d>2*x.s||x.d-x.v>x.s)throw Error("slack inequality");
 const lp=(t,j)=>{
  if(t<=0)return new Map();
  const dp=Array.from({length:t},()=>new Map());dp[0].set(0,1);
  for(const x of L)for(let s=x.s;s<t;s++)for(const [b,c] of dp[s-x.s]){
   const h=b+(j?x.b1:x.b0);dp[s].set(h,(dp[s].get(h)||0)+c);
  }
  const out=new Map();for(const row of dp)for(const [h,c] of row)out.set(h,(out.get(h)||0)+c);return out;
 };
 const direct=(D,r,J,j)=>{
  const dp=Array.from({length:D+1},()=>new Map());dp[0].set("0,0,0",1);
  for(const x of B)for(let d=x.d;d<=D;d++)for(const [key,c] of [...dp[d-x.d]]){
   const [m,v,h]=key.split(",").map(Number),a=[m+1,v+x.v,h+x.h].join(",");
   dp[d].set(a,(dp[d].get(a)||0)+c);
  }
  const n=2*D-r,out=new Map();
  for(let k=0;k<=Math.floor(D/2);k++)for(const [key,c] of dp[D-2*k]){
   const [m,v,h]=key.split(",").map(Number),alpha=v-J;
   if(alpha<0||m+k+alpha<=n)continue;
   const H=h-alpha-(j?k:0);out.set(H,(out.get(H)||0)+c);
  }
  return out;
 };
 const sorted=m=>JSON.stringify([...m].filter(p=>p[1]).sort((a,b)=>a[0]-b[0]));
 const cases=[];let comparisons=0,strict=0;
 for(const J of [-3,-2,-1,0,1,2,3,4])for(let r=1;r<=6;r++){
  const t=r-J;if(t<=0)continue;
  const minD=Math.max(2,2*(t-1),J+t-1);
  for(let j=0;j<=1;j++){
   const predicted=lp(t,j);
   for(const D of [minD,minD+1]){
    const target=new Map([...predicted].map(([b,c])=>[b+J-D,c]));
    if(sorted(target)!==sorted(direct(D,r,J,j)))throw Error(`theorem fail J=${J} r=${r} D=${D}`);
    comparisons++;
   }
   if(minD>2){
    const lower=minD-1,target=new Map([...predicted].map(([b,c])=>[b+J-lower,c]));
    if(sorted(target)===sorted(direct(lower,r,J,j)))throw Error("sharpening false");
    strict++;
   }
  }
  cases.push({J,r,t,sharp_D_min:minD,missing_mass:[...lp(t,0).values()].reduce((a,b)=>a+b,0)});
 }
 return {schema:"R749SQD_SHARP_NONZERO_V_THRESHOLD_V1",status:"PASS",scientific_pin:"a72226e2430ffa4786321ac86e7f0c599d5f0389",arithmetic:"exact integer unbounded-multiset DP, safe integer range in enumerated domain",J_range:[-3,4],r_range:[1,6],case_count:cases.length,at_and_after_threshold_comparisons:comparisons,previous_threshold_failure_checks:strict,sharp_witnesses:[{d:2,v:2,s:1},{d:1,v:0,s:1}],cases,proof_status:"AUTHOR_EXACT_NOT_REVIEWED"};
}
console.log(JSON.stringify(verifySharp(),null,2));
