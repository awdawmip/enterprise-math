// EC49FXJ independent exact integer verifier (Node >=18)
// Run: node EC49FXJ_SYMBOL_TRANSVERSAL_VERIFY.js
const mod=(x,n)=>(x%n+n)%n;
const generateTransversals=function generateTransversals(){return [
Array.from({length:55},(_,i)=>i),
Array.from({length:55},(_,i)=>i+(i%2?55:0)),
Array.from({length:55},(_,i)=>i+(i%2?0:55)),
Array.from({length:55},(_,i)=>i+((i*7+3)%5<2?55:0))
];};
const activationSet=function activationSet(r){let m=r<=10?r+1:r+2;return Array.from({length:5},(_,i)=>Array.from({length:m},(_,a)=>i+5*a)).flat()};
const symbolDistance=function symbolDistance(S,d,i,j){let n=0;for(const t of S){if((mod(t,5)===i && mod(t,11)!==j)||(mod(d-t,5)===i && mod(d-t,11)!==j)) n++;}return n};
const runVerification=function runVerification(){
 const Dlist=generateTransversals(), rows=[];
 for(let r=1;r<=20;r++){
  const S=activationSet(r);let min=Infinity, checks=0;
  for(const D of Dlist) for(const d of D) for(let i=0;i<5;i++) for(let j=0;j<11;j++){
    const g=symbolDistance(S,d,i,j);if(g<r) throw Error(`FAILED r=${r} d=${d} i=${i} j=${j} got=${g}`);
    min=Math.min(min,g);checks++;
  }
  if(min!==r)throw Error(`FAILED equality r=${r}, observed=${min}`);
  const m=r<=10?r+1:r+2;
  if(S.length!==5*m)throw Error("Bad layout length");
  rows.push({required_symbol_distance:r,activations:S.length,minimum_observed_symbol_distance:min,checks});
 }
 let max=Infinity;for(let d=0;d<55;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++)max=Math.min(max,symbolDistance(activationSet(20),d,i,j));
 if(max!==20)throw Error("Full 110 activation metric maximum not 20");
 return {schema:"EC49FXJ_SYMBOL_TRANSVERSAL_VALIDATION_V1",frozen_scientific_pin:"BRC16943",parent:"EC49FXI",model:"P10/one-hole auxiliary Farey–CRT, known reference and complete indexed reflection spectra",metric:"two-bit physical activation symbol (union) Hamming distance",transversal_samples:4,transversal_definitions:["lower representative per mod55 class","even representative","odd representative","alternating modular representative"],rows,full_110_site_minimum_symbol_distance:max,total_inequality_checks:rows.reduce((s,x)=>s+x.checks,0)+55*5*11,algorithm:"Exact integer modulo 5/11; each of 4 antipodal transversals covers every residue mod55 once; proof extends to all 2^55 transversals since the predicate depends only on d mod55",status:"PASS",independent_mathematical_review:"NOT_REVIEWED"};
};
process.stdout.write(JSON.stringify(runVerification(),null,2)+"\n");
