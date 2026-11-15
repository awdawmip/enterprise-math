#!/usr/bin/env node
'use strict';
function reproduce(){
  const facets=[[-1,-1,-1,-2],[-1,-1,1,-2],[-1,1,-1,-2],[-1,1,1,-2],[1,-1,-1,-2],[1,-1,1,-4],[1,1,-1,-4],[1,1,1,-2]];
  const P=[];
  for(let h=-2;h<=2;h++)for(let u=-2;u<=2;u++)for(let v=-2;v<=2;v++)
    if(facets.every(([a,b,c,t])=>a*h+b*u+c*v>=t))P.push([h,u,v]);
  const check=(condition,why)=>{if(!condition)throw Error(why)};
  check(P.length===33,"33 points");
  const pairs=new Map();
  for(let i=0;i<P.length;i++)for(let j=i;j<P.length;j++){
    const key=P[i].map((v,k)=>v+P[j][k]).join(",");
    pairs.set(key,[...(pairs.get(key)||[]),[i,j]]);
  }
  const ids=new Set();
  for(const ps of pairs.values())if(ps.length===1){ids.add(ps[0][0]);ids.add(ps[0][1])}
  const F=[...ids].sort((a,b)=>a-b).map(i=>P[i]);
  check(F.length===25,"25 forced");
  const B=F.filter(([h,u,v])=>u<2).map(([h,u,v])=>({h,d:2-u,v}));
  check(B.length===23,"23 positive deficit");
  const e=B.filter(x=>x.h===0&&x.d===1&&x.v===1);
  check(e.length===1,"unique zero slack");
  const L=B.filter(x=>!(x.h===0&&x.d===1&&x.v===1))
    .map(x=>({...x,s:2*x.d-1-x.v,b0:x.h+x.d-x.v,b1:x.h+x.d-x.v,optional:0}));
  L.push({h:0,d:2,v:0,s:3,b0:2,b1:1,optional:1});
  check(L.length===23,"23 nonzero slack letters");
  const slack=new Map();
  for(const x of L){
    check(x.s>0&&x.b0>=0&&x.b1>=0&&x.b0<=2*x.s&&x.b1<=2*x.s,"slack/bounds");
    slack.set(x.s,(slack.get(x.s)||0)+1);
  }
  check(JSON.stringify([...slack].sort((a,b)=>a[0]-b[0]))===JSON.stringify([[1,3],[2,4],[3,6],[4,4],[5,3],[6,2],[7,1]]),"slack distribution");
  const sorted=(m)=>[...m].filter(([x,c])=>c!==0).sort((a,b)=>Number(a[0])-Number(b[0]));
  const layer=(r,j)=>{
    const dp=Array.from({length:r},()=>new Map());
    dp[0].set(0,1);
    for(const item of L){
      for(let s=item.s;s<r;s++){
        for(const [b,c] of dp[s-item.s]){
          const key=b+(j===0?item.b0:item.b1);
          dp[s].set(key,(dp[s].get(key)||0)+c);
        }
      }
    }
    const acc=new Map();
    for(const part of dp)for(const [b,c] of part)acc.set(b,(acc.get(b)||0)+c);
    return sorted(acc);
  };
  const missing=(D,r,j)=>{
    const dp=Array.from({length:D+1},()=>new Map());
    dp[0].set("0,0,0",1);
    for(const item of B)for(let d=item.d;d<=D;d++){
      for(const [key,c] of [...dp[d-item.d]]){
        const [m,v,h]=key.split(",").map(Number);
        const next=[m+1,v+item.v,h+item.h].join(",");
        dp[d].set(next,(dp[d].get(next)||0)+c);
      }
    }
    const n=2*D-r, acc=new Map();
    for(let k=0;k<=Math.floor(D/2);k++)for(const [key,c] of dp[D-2*k]){
      const [m,v,h]=key.split(",").map(Number);
      if(v<0||n>=k+m+v)continue;
      const H=h-v-(j===1?k:0);
      acc.set(H,(acc.get(H)||0)+c);
    }
    return sorted(acc);
  };
  const rows=[],knownC=[1,4,14,42,113,279,651,1437,3040],knownT=[0,0,0,1,4,14,43,117,293];
  for(let r=1;r<=9;r++){
    const D=Math.max(2,2*r-2),a=layer(r,0),b=layer(r,1);
    const match=(x,y,delta)=>JSON.stringify(x.map(([h,c])=>[h-delta,c]))===JSON.stringify(y);
    check(match(a,missing(D,r,0),D)&&match(b,missing(D,r,1),D),"D exact enumeration r="+r);
    check(match(a,missing(D+1,r,0),D+1)&&match(b,missing(D+1,r,1),D+1),"D+1 exact enumeration r="+r);
    const C=a.reduce((s,x)=>s+x[1],0);
    check(C===knownC[r-1]&&b.reduce((s,x)=>s+x[1],0)===C,"C r="+r);
    check(a.length===2*r-1 && b.length===2*r-1 && a.every((x,i)=>x[0]===i&&x[1]>0) && b.every((x,i)=>x[0]===i&&x[1]>0),"support r="+r);
    const signed=a.map(([x,c])=>[x,c-(b.find(([y])=>y===x)||[x,0])[1]]).filter(x=>x[1]!==0);
    const T=signed.reduce((s,[x,c])=>s+x*c,0);
    check(T===knownT[r-1],"T r="+r);
    const m=Math.floor((r-1)/3),bits=Math.ceil(Math.log2(m+1));
    rows.push({r,first_valid_D:D,missing_count:C,optional_count_total:T,shifted_H_plus_D_A0:a,shifted_H_plus_D_A1:b,signed_A0_minus_A1:signed,distinct_H_bins:2*r-1,max_optional_count:m,minimal_extra_bits:bits});
  }
  check(JSON.stringify(rows[3].signed_A0_minus_A1)===JSON.stringify([[1,-1],[2,1]]),"sharp signed crossover");
  check(L.some(x=>x.h===-1&&x.d===1&&x.v===-2&&x.s===3&&x.b0===2&&x.optional===0),"forced optional twin");
  return {schema:"R749SQB_H_RESOLVED_BOUNDARY_V1",status:"PASS",frozen_scientific_pin:"a72226e2430ffa4786321ac86e7f0c599d5f0389",arithmetic:"exact integer count using Number; all counts and sums in safe integer range",independent_crosscheck:"Direct finite-deficit pattern DP vs truncated slack multivariate product; locally also tested independently in Python integers",first_grid_points:P.length,forced_types:F.length,positive_slack_types:L.length,slack_weights:[...slack].sort((a,b)=>a[0]-b[0]),r_range:[1,9],rows,review:"AUTHOR_EXACT_NOT_REVIEWED"};
}
console.log(JSON.stringify(reproduce(),null,2));
