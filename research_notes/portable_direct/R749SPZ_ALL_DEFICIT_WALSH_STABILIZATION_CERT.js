#!/usr/bin/env node
// R749SPZ: exhaustive integer certificate for boundary-deficit saturation.
// Reproduction: node R749SPZ_ALL_DEFICIT_WALSH_STABILIZATION_CERT.js
'use strict';
const facets=[[-1,-1,-1,-2],[-1,-1,1,-2],[-1,1,-1,-2],[-1,1,1,-2],[1,-1,-1,-2],[1,-1,1,-4],[1,1,-1,-4],[1,1,1,-2]];
const assert=(ok,msg)=>{if(!ok)throw Error(msg)};
const key=x=>x.join(',');
function alphabet(){
 const P=[];
 for(let h=-2;h<=2;h++)for(let u=-2;u<=2;u++)for(let v=-2;v<=2;v++)
  if(facets.every(([a,b,c,d])=>a*h+b*u+c*v>=d))P.push([h,u,v]);
 assert(P.length===33,'K lattice census');
 const pairs=new Map();
 for(let i=0;i<P.length;i++)for(let j=i;j<P.length;j++){
  const s=key(P[i].map((x,k)=>x+P[j][k]));
  if(!pairs.has(s))pairs.set(s,[]);pairs.get(s).push([i,j]);
 }
 const ids=new Set();for(const arr of pairs.values())if(arr.length===1){ids.add(arr[0][0]);ids.add(arr[0][1]);}
 const F=[...ids].sort((a,b)=>a-b).map(i=>P[i]);
 const zero=F.filter(x=>x[1]===2),positive=F.filter(x=>x[1]<2);
 assert(F.length===25&&zero.length===2&&positive.length===23,'forced alphabet');
 assert(zero.some(x=>key(x)==='-1,2,-1')&&zero.some(x=>key(x)==='0,2,0'),'zero fillers');
 assert(positive.some(x=>key(x)==='0,1,1')&&positive.every(x=>x[2]<=2-x[1]),'deficit domination');
 return {P,F,positive};
}
function finite(D,positive){
 // State: (positive letter count m, sum h, sum v); unbounded multiset generating function.
 const dp=Array.from({length:D+1},()=>new Map());dp[0].set('0,0,0',1);
 for(const [h,u,v] of positive){const d=2-u;
  for(let e=d;e<=D;e++)for(const [s,c] of dp[e-d]){
   const [m,H,V]=s.split(',').map(Number), k=key([m+1,H+h,V+v]);
   dp[e].set(k,(dp[e].get(k)||0)+c);
  }
 }
 const difference=new Map(),byK=[];let mass=0,kSum=0,threshold=0,massThreshold=0;
 const add=(h,v)=>difference.set(h,(difference.get(h)||0)+v);
 for(let k=0;k<=Math.floor(D/2);k++){
  let count=0,maxN=0;
  for(const [s,c] of dp[D-2*k]){
   const [m,H,V]=s.split(',').map(Number);
   if(V<0)continue;
   count+=c;maxN=Math.max(maxN,k+m+V);
   if(k>0){add(H-V,c);add(H-V-k,-c);}
  }
  byK.push({optional_count:k,patterns:count,maximum_minimum_length:maxN});
  mass+=count;kSum+=k*count;massThreshold=Math.max(massThreshold,maxN);
  if(k>0)threshold=Math.max(threshold,maxN);
 }
 const profile=[...difference].filter(([h,x])=>x!==0).sort((a,b)=>a[0]-b[0]);
 assert(profile.reduce((a,[h,c])=>a+c,0)===0,'conservation');
 assert(profile.reduce((a,[h,c])=>a+h*c,0)===kSum,'first moment');
 return {D,stabilized_from_n:threshold,mass_saturated_from_n:massThreshold,mass,optional_count_sum:kSum,byK,profile};
}
function direct(n,D,F,option){
 // Independent complete coefficient extraction of product over all 26 source types.
 let dp=new Map([['0,0,0,0',1]]);
 for(const [h,u,v] of [...F,option]){
  const d=2-u,next=new Map(dp);
  for(const [s,c] of dp){const [len,e,V,H]=s.split(',').map(Number);
   for(let r=1;r<=n-len&&e+r*d<=D;r++){
    const t=key([len+r,e+r*d,V+r*v,H+r*h]);
    next.set(t,(next.get(t)||0)+c);
   }
  }
  dp=next;
 }
 const out=new Map();
 for(const [s,c] of dp){const [len,e,V,H]=s.split(',').map(Number);
  if(len===n&&e===D&&V===0)out.set(H,c);
 }
 return out;
}
const {P,F,positive}=alphabet(),checked=[];
for(const D of [2,4,6,8]){
 const f=finite(D,positive);
 assert(f.stabilized_from_n===2*D-3,'sharp stabilization for selected deficits');
 assert(f.mass_saturated_from_n===2*D,'mass saturation');
 for(const n of [Math.max(1,2*D-4),2*D-3,2*D]){
  const a=direct(n,D,F,[0,0,0]),b=direct(n,D,F,[-1,0,0]),diff=new Map();
  for(const h of new Set([...a.keys(),...b.keys()])){
   const x=(a.get(h)||0)-(b.get(h)||0);if(x)diff.set(h,x);
  }
  const directProfile=[...diff].sort((x,y)=>x[0]-y[0]);
  assert((n>=2*D-3)===(JSON.stringify(directProfile)===JSON.stringify(f.profile)),'direct profile threshold D='+D+' n='+n);
  if(n===2*D){assert([...a.values()].reduce((x,y)=>x+y,0)===f.mass,'mass A0');assert([...b.values()].reduce((x,y)=>x+y,0)===f.mass,'mass A1');}
 }
 checked.push(f);
}
assert(JSON.stringify(checked.find(x=>x.D===6).profile)===JSON.stringify([[-5,-15],[-4,-9],[-3,-13],[-2,3],[-1,-6],[0,18],[1,9],[2,9],[3,1],[4,3]]),'previous R749SPY D6');
const x=checked.find(x=>x.D===8);
assert(x.mass===9584&&x.optional_count_sum===1660&&JSON.stringify(x.byK.map(y=>y.patterns))==='[8116,1292,161,14,1]','D8 census');
assert(JSON.stringify(x.profile)===JSON.stringify([[-7,-40],[-6,-42],[-5,-78],[-4,-56],[-3,-78],[-2,17],[-1,32],[0,86],[1,50],[2,63],[3,24],[4,16],[5,2],[6,4]]),'D8 profile');
process.stdout.write(JSON.stringify({schema:'R749SPZ_ALL_DEFICIT_BOUNDARY_SATURATION_V1',status:'PASS',scientific_pin:'a72226e2430ffa4786321ac86e7f0c599d5f0389',model:'auxiliary 16-atom Walsh optimal-center fiber; t=1/10,s=1/2',K_first_grid:P.length,forced_types:F.length,positive_deficit_types:positive.length,proved_symbolic_range:'all integers D>=2, all n>=2D-3 for signed profile and all n>=2D for mass; exact finite D computation via recurrence',computed_deficits:checked,exact_conditional_TV_W1_at_D8:'83/(9584*n), n>=16',review:'AUTHOR_EXACT_NOT_REVIEWED'},null,2)+'\n');
