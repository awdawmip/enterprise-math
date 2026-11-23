'use strict';
// EC49FXQ: Exact finite r=3 whole-activation phase-pair obstruction under BRC16943.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const mod = (a,m) => ((a%m)+m)%m;
const allGroups = Array.from({length:5},(_,i)=>Array.from({length:55},(_,x)=>x).filter(x=>x%5===i));
function makeA(holes,singletons) {
  const A = new Set();
  for(let c=0;c<3;c++) for(const x of allGroups[c]) if(!holes[c].includes(x)) A.add(x);
  for(let c=3;c<5;c++) A.add(singletons[c]);
  return A;
}
const denseHoles={0:[0,45],1:[16,51],2:[22,37],3:[18,53],4:[19,54]};
const examples={
  good:makeA({0:[15,45],1:[1,36],2:[2,32]},{3:8,4:9}),
  bad:makeA({0:[25,45],1:[11,26],2:[22,37]},{3:53,4:29}),
  dense:new Set(allGroups.flatMap((group,i)=>group.filter(x=>!denseHoles[i].includes(x))))
};
function popcnt(n){let z=0;for(;n;n&=n-1)z++;return z;}
function analyze(A) {
  const h=Array.from({length:5},(_,c)=>[...A].filter(d=>d%5===c).length);
  assert(h.every(v=>v>=1));
  const T=allGroups.map(gr=>gr.filter(x=>!A.has((2*x)%55)));
  const forced=Array.from({length:5},(_,i)=>i).filter(i=>T[i].length<2);
  const H=Array.from({length:5},(_,i)=>i).filter(i=>T[i].length===2);
  const base=15+forced.length;
  for(let cost=0;cost<=H.length;cost++) {
    for(let upgradedMask=0;upgradedMask<(1<<H.length);upgradedMask++) {
      if(popcnt(upgradedMask)!==cost) continue;
      const upgraded=new Set(H.filter((_,index)=>(upgradedMask>>index)&1));
      const remaining=H.filter(i=>!upgraded.has(i));
      for(let assignment=0;assignment<(1<<remaining.length);assignment++) {
        const doubled=Object.fromEntries(remaining.map((i,pos)=>[i,T[i][(assignment>>pos)&1]]));
        let valid=true;
        for(let a=0;a<remaining.length;a++) for(let b=a+1;b<remaining.length;b++) {
          if(A.has((doubled[remaining[a]]+doubled[remaining[b]])%55)) valid=false;
        }
        if(valid) return {h,T,forced,H,base,tau:cost,optimum:base+cost,upgraded:[...upgraded],doubled};
      }
    }
  }
  throw new Error('No feasible repair witness');
}
function buildLayout(A,r){
  const S=[];
  for(let i=0;i<5;i++){
    const T=r.T[i];
    if(T.length===2 && !r.upgraded.includes(i)) {
      const x=r.doubled[i], y=T.find(v=>v!==x);
      S.push(x,x+55,y);
    } else if(T.length>=3) S.push(...T.slice(0,3));
    else S.push(...allGroups[i].slice(0,4));
  }
  assert.equal(S.length,r.optimum);
  assert.equal(new Set(S).size,S.length);
  return S;
}
function G(S,d,i,j) {
  return S.reduce((n,t)=>n+Number((t%5===i && t%11!==j)||(mod(d-t,5)===i && mod(d-t,11)!==j)),0);
}
function check(A,r,S) {
  let checks=0,min=110,argmin=null;
  for(const d of [...A].sort((a,b)=>a-b))for(let i=0;i<5;i++)for(let j=0;j<11;j++) {
    const g=G(S,d,i,j);checks++;
    if(g<min){min=g;argmin=[d,i,j];}
    assert(g>=3,'counterexample d='+d+' i='+i+' j='+j+' G='+g);
  }
  return {checks,min,argmin};
}
function collisionTable(A,r){
  const H=r.H;
  return H.flatMap((i,a)=>H.slice(a+1).map(j=>({pair:[i,j],
    cells:r.T[i].flatMap(x=>r.T[j].map(y=>({x,y,sum:(x+y)%55,forbidden:A.has((x+y)%55)})))})));
}
const report={scientific_pin:'BRC16943',model:'FROZEN_FAREY_CRT_WHOLE_ACTIVATION_SYMBOL',distance:3,examples:{},random_checks:{}};
for(const [key,A] of Object.entries(examples)){
  const r=analyze(A),S=buildLayout(A,r),v=check(A,r,S);
  assert.deepEqual(r.h,key==='dense'?[9,9,9,9,9]:[9,9,9,1,1]);
  assert.equal(r.optimum,{good:15,bad:16,dense:18}[key]);
  report.examples[key]={phase_residues:[...A].sort((a,b)=>a-b),histogram:r.h,safe_groups:r.T,
    obstructed_colors:r.H,base:r.base,additional_cost:r.tau,optimum:r.optimum,upgraded:r.upgraded,
    doubled:r.doubled,layout:S.sort((a,b)=>a-b),verification:v,collision_table:collisionTable(A,r)};
}
let rng=49230349;
function nextRand(){rng=(Math.imul(rng,1664525)+1013904223)>>>0;return rng;}
let total=0,nRows=0,maxExtra=0,dist={};
for(let trial=0;trial<350;trial++){
  const A=new Set();
  for(let i=0;i<5;i++){
    const n=1+nextRand()%11, bucket=[...allGroups[i]];
    for(let k=bucket.length-1;k>0;k--){const j=nextRand()%(k+1);[bucket[j],bucket[k]]=[bucket[k],bucket[j]];}
    for(let k=0;k<n;k++)A.add(bucket[k]);
  }
  const r=analyze(A),S=buildLayout(A,r),v=check(A,r,S);
  total++;nRows+=v.checks;maxExtra=Math.max(maxExtra,r.tau);dist[r.tau]=(dist[r.tau]||0)+1;
}
let denseCases=0,denseRows=0,denseMax=0,denseDist={};
for(let trial=0;trial<250;trial++){
  const A=new Set();
  for(let i=0;i<5;i++){
    const group=[...allGroups[i]];
    for(let k=group.length-1;k>0;k--){const j=nextRand()%(k+1);[group[j],group[k]]=[group[k],group[j]];}
    for(let k=0;k<9;k++)A.add(group[k]);
  }
  const r=analyze(A),S=buildLayout(A,r),v=check(A,r,S);
  denseCases++;denseRows+=v.checks;denseMax=Math.max(denseMax,r.tau);
  denseDist[r.tau]=(denseDist[r.tau]||0)+1;
}
report.random_checks={cases:total,rows:nRows,max_extra:maxExtra,extra_distribution:dist,seed:49230349,
  dense_cases:denseCases,dense_rows:denseRows,dense_max_extra:denseMax,dense_extra_distribution:denseDist};
const output=process.argv[2]||'EC49FXQ_SYMBOL_R3_PHASE_GRAPH_OUTPUT.json';
fs.writeFileSync(output,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:'PASS',example_costs:{good:report.examples.good.optimum,
  bad:report.examples.bad.optimum,dense:report.examples.dense.optimum},
  rows_verified:Object.values(report.examples).reduce((n,e)=>n+e.verification.checks,0)+nRows+denseRows,
  random:report.random_checks,output}));
