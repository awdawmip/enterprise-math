"use strict";
// EC48B two-stage binary terminal decision, exact exhaustive finite checker.
// For each P,Q entry in {1,2} with H=3, Y=2, all support and tie comparisons
// use safe exact integers: |p_j q_i-p_i q_j|<=3.
function gcd(a,b){while(b){let t=a%b;a=b;b=t;}return a;}
function rawRatios(p,q){
  const m=new Map();
  for(let i=0;i<p.length;i++){let d=gcd(p[i],q[i]);let a=p[i]/d,b=q[i]/d;m.set(a+"/"+b,[a,b,i]);}
  return [...m.values()].sort((x,y)=>x[0]*y[1]-y[0]*x[1]);
}
function signaturePeak(p,q,H,Y) {
  let signatures=Array.from({length:H},()=>Array(Y).fill(1)),peak=1;
  for(const [a,b] of rawRatios(p,q)) {
    for(let h=0;h<H;h++)for(let y=0;y<Y;y++)if(p[h*Y+y]*b===q[h*Y+y]*a)signatures[h][y]=-1;
    peak=Math.max(peak,new Set(signatures.map(row=>row.join(","))).size);
  }
  return peak;
}
function edgeComponents(p,q,H,Y,K,i){
 const U=K*Y, M=1<<U,N=K**H;
 const D=p.map((v,j)=>v*q[i]-q[j]*p[i]);
 const optimum=D.reduce((s,x)=>s+Math.max(x,0),0);
 let totalTie=0;
 for(let j=0;j<D.length;j++)if(D[j]===0)totalTie+=q[j];
 const good=new Set(),tMass=new Map();
 for(let fc=0;fc<N;fc++){
  const fs=Array(H);
  for(let h=0;h<H;h++)fs[h]=Math.floor(fc/K**h)%K;
  for(let m=0;m<M;m++){
   let score=0,t=0;
   for(let h=0;h<H;h++)for(let y=0;y<Y;y++){
    const j=h*Y+y, bit=(m>>(fs[h]*Y+y))&1;
    score+=D[j]*bit;
    if(D[j]===0)t+=q[j]*bit;
   }
   if(score===optimum){const id=fc*M+m;good.add(id);tMass.set(id,t);}
  }
 }
 const visited=new Set(),intervals=[];
 for(const key of good){
  if(visited.has(key))continue;
  let stack=[key],lo=totalTie,hi=0;visited.add(key);
  while(stack.length){
   const z=stack.pop(),fc=Math.floor(z/M),m=z%M;
   lo=Math.min(lo,tMass.get(z));hi=Math.max(hi,tMass.get(z));
   for(let a=0;a<U;a++){
    const w=fc*M+(m^(1<<a));
    if(good.has(w)&&!visited.has(w)){visited.add(w);stack.push(w);}
   }
   for(let h=0;h<H;h++){
    const old=Math.floor(fc/K**h)%K;
    for(let v=0;v<K;v++)if(v!==old){
     const w=(fc+(v-old)*K**h)*M+m;
     if(good.has(w)&&!visited.has(w)){visited.add(w);stack.push(w);}
    }
   }
  }
  intervals.push([lo,hi]);
 }
 intervals.sort((a,b)=>a[0]-b[0]||a[1]-b[1]);
 let reach=0,complete=intervals.length>0;
 for(const [lo,hi] of intervals){if(lo>reach){complete=false;break;}reach=Math.max(reach,hi);}
 return {totalTie,intervals,complete:complete&&reach===totalTie,optimalVertices:good.size};
}
function decodeMask(m,len){return Array.from({length:len},(_,i)=>1+((m>>i)&1));}
function runAll(){
 const H=3,Y=2,K=2,maskmax=1<<(H*Y);
 const hist={},example={p:[1,1,1,1,1,2],q:[1,1,1,2,1,1]};
 let sourcePairs=0,eligible=0,faceChecks=0,multiCompFaces=0,gaps=0;
 for(let a=0;a<maskmax;a++)for(let b=0;b<maskmax;b++){
  const p=decodeMask(a,H*Y),q=decodeMask(b,H*Y);
  sourcePairs++;
  const k=signaturePeak(p,q,H,Y);hist[k]=(hist[k]||0)+1;
  if(k>K)continue;
  eligible++;
  for(const [x,y,i] of rawRatios(p,q)){
   const e=edgeComponents(p,q,H,Y,K,i);
   faceChecks++;
   if(e.intervals.length>1)multiCompFaces++;
   if(!e.complete)gaps++;
  }
 }
 const exK=signaturePeak(example.p,example.q,H,Y);
 const exIndex=2; // p/q = 1, equal-ratio group in displayed example
 const ex=edgeComponents(example.p,example.q,H,Y,K,exIndex);
 return {schema:"EM_EC48B_EXACT_FACE_COMPONENT_ENUM_V1",date:"2026-10-27",
  model:{H,Y,K,positive_integer_entry_domain:[1,2],normalized_each_law:true},
  totalPairs:sourcePairs,signaturePeakHistogram:hist,eligiblePairs:eligible,
  breakpointFaceChecks:faceChecks,multicomponentFaces:multiCompFaces,
  uncoveredFaces:gaps,example:{...example,kHull:exK,tieRawRatio:"1/1",...ex},
  proofScope:"Finite domain enumeration only; universal exact component theorem is established algebraically, not by this test."};
}
if(typeof process!=="undefined"&&process.stdout)process.stdout.write(JSON.stringify(runAll(),null,2)+"\n");
