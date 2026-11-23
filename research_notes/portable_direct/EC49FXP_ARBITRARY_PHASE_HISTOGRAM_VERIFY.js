'use strict';
// Frozen auxiliary scientific pin BRC16943; all operations are exact integers.
function mod(a,n){return ((a%n)+n)%n;}

function phaseSet(input){return [...new Set(input.map(d=>mod(d,55)))].sort((a,b)=>a-b);}

function histogram(input){const h=[0,0,0,0,0];for(const d of phaseSet(input))h[d%5]++;return h;}

function localCost(r,s){return r+Number(s<Math.ceil(r/2))+Number(s<r-10);}

function optimal(r,input){
 const h=histogram(input);
 if(h.some(x=>x===0))throw new Error("domain: all five phase colors must occur");
 if(r>=21)return null;
 if(r<4)throw new Error("domain: 4<=r<=20");
 return 5*r+h.reduce((z,c)=>z+Number(c>=12-Math.ceil(r/2))+Number(c>=22-r),0);
}

function layout(r,input){
 const D=new Set(phaseSet(input)),sites=[];
 for(let i=0;i<5;i++){
  const safe=[],unsafe=[];
  for(let x=i;x<55;x+=5)(D.has(mod(2*x,55))?unsafe:safe).push(x);
  const s=safe.length,twolifts=a=>a.flatMap(x=>[x,x+55]);
  let take;
  if(2*s>=r)take=twolifts(safe).slice(0,r);
  else if(11+s>=r+1)take=[...twolifts(safe),...unsafe].slice(0,r+1);
  else take=twolifts([...safe,...unsafe]).slice(0,r+2);
  if(take.length!==localCost(r,s))throw new Error("local mismatch");
  sites.push(...take);
 }
 if((new Set(sites)).size!==sites.length||sites.length!==optimal(r,input))throw new Error("layout mismatch");
 return sites.sort((a,b)=>a-b);
}

function directCRT(input,sites){
 let minimum=Infinity,critical=null,rows=0;
 for(const d of phaseSet(input))for(let i=0;i<5;i++)for(let j=0;j<11;j++){
   let g=0;
   for(const t of sites)if((t%5===i&&t%11!==j)||(mod(d-t,5)===i&&mod(d-t,11)!==j))g++;
   if(g<minimum){minimum=g;critical={d,i,j};}
   rows++;
 }
 return {minimum,critical,rows};
}

function independentLocalDP(r,s){
 let states=new Map([["0:0",[0,0]]]);
 for(let ix=0;ix<11;ix++){
  const next=new Map();
  for(const [mass,erasure] of states.values())for(let n=0;n<=2;n++){
   const m=mass+n,e=ix<s?erasure:Math.max(erasure,n);
   next.set(m+":"+e,[m,e]);
  }
  states=next;
 }
 const valid=[...states.values()].filter(([m,e])=>m-e>=r).map(([m])=>m);
 return valid.length?Math.min(...valid):null;
}

function makeRandom(seed){let x=seed>>>0;return function(){x^=x<<13;x^=x>>>17;x^=x<<5;return x>>>0;};}

function run(){
 let dpChecks=0,cases=0,rows=0,maximumSiteCount=0;
 for(let r=4;r<=20;r++)for(let s=0;s<=10;s++){if(independentLocalDP(r,s)!==localCost(r,s))throw new Error("DP mismatch "+r+","+s);dpChecks++;}
 const rng=makeRandom(4923);
 for(let ix=0;ix<550;ix++){
  const D=[0,1,2,3,4],extras=1+rng()%51;
  for(let a=0;a<extras;a++)D.push(rng()%55);
  if(ix%7===0)for(const d of [...D])D.push(d+55);
  const r=4+rng()%17,S=layout(r,D),check=directCRT(D,S);
  if(check.minimum<r)throw new Error("invalid "+JSON.stringify({ix,r,check}));
  if(optimal(r,D)!==optimal(r,D.map(d=>d+55)))throw new Error("phase quotient failed");
  cases++;rows+=check.rows;maximumSiteCount=Math.max(maximumSiteCount,S.length);
 }
 const DA=[...Array.from({length:10},(_,ix)=>5*(ix+1)),1,2,3,4];
 const DB=[0,...Array.from({length:9},(_,ix)=>5*(ix+2)),1,2,3,4];
 const DI=Array.from({length:14},(_,ix)=>ix);
 const SA=layout(4,DA),checkA=directCRT(DA,SA),checkB=directCRT(DB,SA);
 if(!(optimal(4,DA)===21&&optimal(20,DA)===102&&optimal(4,DI)===20&&optimal(20,DI)===110&&optimal(4,DB)===21&&checkA.minimum===4&&checkB.minimum===3&&checkB.critical.d===0))throw new Error("counterexample mismatch");
 return {schema:"EC49FXP_ARBITRARY_PHASE_HISTOGRAM_CHECK_V1",frozen_science:"BRC16943",domain:"D subset Z/110 with projection covering five mod-5 residues; 4<=r<=20",method:"analytic five-color optimization with independent finite local-DP and direct integer CRT rows",dp_checks:dpChecks,seed:4923,arbitrary_phase_layouts:cases,direct_crt_rows:rows,max_sites:maximumSiteCount,example:{D_A:DA,D_B:DB,D_interval14:DI,phase_histogram_A:histogram(DA),N4_A:optimal(4,DA),N4_interval14:optimal(4,DI),N20_A:optimal(20,DA),N20_interval14:optimal(20,DI),witness_layout_A:SA,check_layout_A:checkA,check_layout_A_under_B:checkB},all_assertions:"PASS"};
}

console.log(JSON.stringify(run(),null,2));
