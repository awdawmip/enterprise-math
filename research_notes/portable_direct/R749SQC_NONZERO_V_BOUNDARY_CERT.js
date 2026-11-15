#!/usr/bin/env node
'use strict';
function calcV(){
 const facets=[[-1,-1,-1,-2],[-1,-1,1,-2],[-1,1,-1,-2],[-1,1,1,-2],[1,-1,-1,-2],[1,-1,1,-4],[1,1,-1,-4],[1,1,1,-2]];
 const P=[];
 for(let h=-2;h<=2;h++)for(let u=-2;u<=2;u++)for(let v=-2;v<=2;v++)
  if(facets.every(([a,b,c,t])=>a*h+b*u+c*v>=t))P.push([h,u,v]);
 if(P.length!==33)throw Error("first grid");
 const pairs=new Map();
 for(let i=0;i<P.length;i++)for(let j=i;j<P.length;j++){
  const key=P[i].map((x,k)=>x+P[j][k]).join(",");
  const l=pairs.get(key)||[];l.push([i,j]);pairs.set(key,l);
 }
 const forced=new Set();
 for(const ps of pairs.values())if(ps.length===1){forced.add(ps[0][0]);forced.add(ps[0][1]);}
 const F=[...forced].sort((a,b)=>a-b).map(i=>P[i]);
 if(F.length!==25)throw Error("forced sources");
 const B=F.filter(([h,u,v])=>u<2).map(([h,u,v])=>({h,d:2-u,v}));
 if(B.length!==23||B.filter(x=>x.h===0&&x.d===1&&x.v===1).length!==1)throw Error("unique e");
 const L=B.filter(x=>!(x.h===0&&x.d===1&&x.v===1)).map(x=>({...x,s:2*x.d-1-x.v,b0:x.h+x.d-x.v,b1:x.h+x.d-x.v}));
 L.push({h:0,d:2,v:0,s:3,b0:2,b1:1});
 if(L.length!==23||L.some(x=>x.s<1||x.d>2*x.s||x.d-x.v>2*x.s||x.b0<0||x.b0>2*x.s||x.b1<0||x.b1>2*x.s))throw Error("slack bounds");
 const layer=(t,j)=>{
  if(t<=0)return new Map();
  const dp=Array.from({length:t},()=>new Map());dp[0].set(0,1);
  for(const x of L)for(let s=x.s;s<t;s++)for(const [b,c] of dp[s-x.s]){
   const y=b+(j===0?x.b0:x.b1);dp[s].set(y,(dp[s].get(y)||0)+c);
  }
  const out=new Map();for(const part of dp)for(const [b,c] of part)out.set(b,(out.get(b)||0)+c);
  return out;
 };
 const actual=(D,r,J,j)=>{
  const dp=Array.from({length:D+1},()=>new Map());dp[0].set("0,0,0",1);
  for(const x of B)for(let d=x.d;d<=D;d++)for(const [key,c] of [...dp[d-x.d]]){
   const [m,v,h]=key.split(",").map(Number),k=[m+1,v+x.v,h+x.h].join(",");
   dp[d].set(k,(dp[d].get(k)||0)+c);
  }
  const n=2*D-r,out=new Map();
  for(let k=0;k<=Math.floor(D/2);k++)for(const [key,c] of dp[D-2*k]){
   const [m,v,h]=key.split(",").map(Number),alpha=v-J;
   if(alpha<0||k+m+alpha<=n)continue;
   const H=h-alpha-(j===1?k:0);out.set(H,(out.get(H)||0)+c);
  }
  return out;
 };
 const sorted=m=>[...m].filter(x=>x[1]).sort((a,b)=>a[0]-b[0]);
 const cases=[];let checks=0;
 for(const J of [-2,-1,0,1,2])for(let r=1;r<=6;r++){
  const t=r-J,D0=Math.max(2,Math.max(0,J)+2*Math.max(0,t-1));
  for(let D=D0;D<=D0+1;D++)for(let j=0;j<=1;j++){
   const expected=sorted(new Map([...layer(t,j)].map(([h,c])=>[h+J-D,c])));
   const observed=sorted(actual(D,r,J,j));
   if(JSON.stringify(expected)!==JSON.stringify(observed))throw Error(`Mismatch ${J} ${r} ${D} ${j}`);
   checks++;
  }
  const counts=sorted(layer(t,0)).reduce((n,x)=>n+x[1],0);
  cases.push({J,r,t,D_min:D0,missing_count:counts,checked_D:[D0,D0+1]});
 }
 const C=[0,1,4,14,42,113,279,651,1437];
 for(const p of cases)if(p.t>=0&&p.t<C.length&&p.missing_count!==C[p.t])throw Error("mass");
 return {schema:"R749SQC_NONZERO_V_BOUNDARY_V1",status:"PASS",frozen_scientific_pin:"a72226e2430ffa4786321ac86e7f0c599d5f0389",model:"auxiliary 16-atom signed Walsh center",method:"exact integer positive-slack bivariate DP vs independent finite-deficit multiset DP",first_grid_points:P.length,forced_source_types:F.length,nonzero_slack_types:L.length,checks,case_count:cases.length,cases,scope:"J=-2..2, r=1..6, D_min and D_min+1, both alphabets",author_status:"AUTHOR_EXACT_NOT_REVIEWED"};
}
console.log(JSON.stringify(calcV(),null,2));
