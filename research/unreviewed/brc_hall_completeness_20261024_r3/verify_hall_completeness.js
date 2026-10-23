"use strict";
// Exact BRC Hall-completeness certificate; Node.js, arbitrary precision BigInt.
const W=[[1n,665n,1n,333n],[333n,333n,1n,333n],[1n,1n,1n,997n]];
const ACT=[0,2,3], E=[[0,1],[1,2],[1,3],[2,3]], DEG=[1n,3n,2n,2n], DEN=1000n;
const EXPECTED=[
 [690,684,676,661,635,588,503,354,111],
 [682,670,649,613,546,427,226,0,0],
 [661,632,580,486,323,61,0,0,0],
 [608,534,403,185,0,0,0,0,0],
 [467,289,8,0,0,0,0,0,0],
 [140,0,0,0,0,0,0,0,0],
 ...Array.from({length:10},()=>[1,0,0,0,0,0,0,0,0])];
function assert(x,s){if(!x)throw Error(s);}
function exact(c){
 let singles=[1n,1n,1n,1n], pairs=E.map(()=>1n);
 for(let a=0;a<3;a++){
  for(let i=0;i<4;i++)singles[i]*=W[a][i]**BigInt(c[a]);
  for(let e=0;e<4;e++)pairs[e]*=(W[a][E[e][0]]+W[a][E[e][1]])**BigInt(c[a]);
 }
 let margins=[],delta=[];
 for(let a=0;a<3;a++){
  let d=singles.map((x,i)=>DEG[i]*(DEN-W[a][i])*x);
  let cap=pairs.map((x,e)=>(DEN-W[a][E[e][0]]-W[a][E[e][1]])*x);
  for(let mask=1;mask<16;mask++){
   let ds=0n,cs=0n;
   for(let i=0;i<4;i++)if(mask&(1<<i))ds+=d[i];
   for(let e=0;e<4;e++)if(mask&(1<<E[e][0])||mask&(1<<E[e][1]))cs+=cap[e];
   margins.push(cs-ds);
  }
  delta.push(d.reduce((x,y)=>x+y,0n)-cap.reduce((x,y)=>x+y,0n));
 }
 return {margins,delta};
}
function hall(c){return exact(c).margins.every(v=>v>=0n);}
function threshold(a,b){
 let lo=0,hi=690;
 while(lo<hi){let mid=Math.floor((lo+hi)/2);if(hall([a,b,mid]))hi=mid;else lo=mid+1;}
 return lo;
}
function verify(){
 for(let j=0;j<3;j++){
  const axis=[16,9,690], c=[0,0,0];c[j]=axis[j];assert(hall(c),"positive axis");
  c[j]--;assert(!hall(c),"negative axis");
 }
 let T=Array.from({length:16},(_,a)=>Array.from({length:9},(_,b)=>threshold(a,b)));
 assert(JSON.stringify(T)===JSON.stringify(EXPECTED),"threshold rows mismatch");
 let n=0, failure=[];
 for(let a=0;a<16;a++)for(let b=0;b<9;b++){
  let t=T[a][b];
  assert(hall([a,b,t]),"threshold failed");
  if(t)assert(!hall([a,b,t-1]),"threshold predecessor");
  for(let k=0;k<t;k++){n++;failure.push([a,b,k]);}
 }
 assert(n===14102,"excluded count");
 const t=(a,b)=>a>=16||b>=9?0:T[a][b];
 let max=[];
 for(let a=0;a<16;a++)for(let b=0;b<9;b++){
  let k=T[a][b]-1;
  if(k>=0&&t(a+1,b)<=k&&t(a,b+1)<=k)max.push([a,b,k]);
 }
 assert(max.length===31,"maxima count");
 let w=[];
 for(let c of max){
  assert(!hall(c)&&[0,1,2].every(i=>hall(c.map((v,j)=>v+(j===i?1:0)))),"max frontier");
  let d=exact(c).delta;let i=d.findIndex(v=>v>0n);
  assert(i>=0,"missing positive witness");
  w.push({counts:c,absolute_prefix_round:c.reduce((s,v)=>s+v,0),
          positive_action:ACT[i],positive_numerator:d[i].toString(),
          denominator_power_of_1000:c.reduce((s,v)=>s+v,0)+1});
 }
 assert(w.filter(x=>x.positive_action===0).length===30&&w.filter(x=>x.positive_action===3).length===1,"witness action counts");
 assert(Math.max(...w.map(x=>x.absolute_prefix_round))===689,"last maximum length");
 for(let c of failure)assert(max.some(m=>c.every((v,j)=>v<=m[j])),"antichain coverage");
 function ieNum(c){
  let singles=DEG.map((_,i)=>W.reduce((x,row,a)=>x*row[i]**BigInt(c[a]),1n));
  let pairs=E.map(([i,j])=>W.reduce((x,row,a)=>x*(row[i]+row[j])**BigInt(c[a]),1n));
  return pairs.reduce((x,y)=>x+y,0n)-singles.reduce((x,y,i)=>x+DEG[i]*y,0n);
 }
 for(let c of [[2,0,0],[0,2,0],[0,0,2],[5,1,0],[0,0,689],[15,0,0],[0,3,1]])
 for(let a=0;a<3;a++)assert(ieNum(c.map((v,j)=>v+(j===a?1:0)))-DEN*ieNum(c)===exact(c).delta[a],"IE delta identity");
 return {
  schema:"EM_BRC_HALL_COMPLETENESS_AUTHOR_EVIDENCE_V1",
  arithmetic:"arbitrary precision exact integer",
  fixed_model:{actions:ACT,weights:W.map(row=>row.map(String)),good_edges:E},
  threshold_rows:T,pure_axis_first_hall:[16,9,690],
  hall_failures:14102,maximal_failures:31,
  maxima_all_have_positive_successor:true,all_failures_dominated_by_maxima:true,
  maximum_witness_absolute_round:690,
  independent_inclusion_exclusion_delta_checks:21,
  boundary_witnesses:w,
  theorem:"For all |c|>=2: H(c) iff all future occupancy increments are nonpositive",
  caveat:"Not a necessity theorem for future residual-R freezing or native P000 X6",
  status:"AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED"
 };
}
if(typeof process!=="undefined"&&process.stdout)process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
