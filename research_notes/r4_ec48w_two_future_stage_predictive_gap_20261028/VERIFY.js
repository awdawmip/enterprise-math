'use strict';
// EC48W: complete exact integer enumeration, 16 strictly positive P/Q atoms.
// Run: node VERIFY.js . No external packages, no native Heartbeat X6 claims.
const fs = require('node:fs');
const assert = require('node:assert/strict');
const C = 2; // continue; 0=stop/reject; 1=stop/accept
const r = [[1, 3], [3, 1]], p1 = [2, 3], q1 = [3, 2];
const p2 = [[1, 9], [5, 5]], q2 = [[9, 1], [5, 5]];
const gcd = (a,b) => b ? gcd(b,a%b) : a;
const atoms=[];
for(let h=0;h<2;h++)for(let j=0;j<2;j++)for(let z=0;z<2;z++)for(let v=0;v<2;v++){
  const P=r[h][j]*p1[z]*p2[h][v], Q=r[h][j]*q1[z]*q2[h][v];
  assert(P>0&&Q>0);
  const g=gcd(P,Q);
  atoms.push({h,j,z,v,P,Q,lr:`${P/g}/${Q/g}`});
}
assert.equal(atoms.length,16);
assert.equal(atoms.reduce((n,x)=>n+x.P,0),400);
assert.equal(atoms.reduce((n,x)=>n+x.Q,0),400);
for(let j=0;j<2;j++)for(let z=0;z<2;z++){
 const xs=atoms.filter(x=>x.j===j&&x.z===z);
 assert.equal(xs.reduce((n,x)=>n+x.P,0),200*p1[z]/5);
 assert.equal(xs.reduce((n,x)=>n+x.Q,0),200*q1[z]/5);
}
const keys=[...new Set(atoms.map(x=>`${x.z}:${x.v}:${x.lr}`))].sort();
assert.equal(keys.length,8);
for(const x of atoms)x.bit=keys.indexOf(`${x.z}:${x.v}:${x.lr}`);
function observe(first,second,mask){
 let a=0,b=0,tp=0,tq=0;
 for(const x of atoms){
  const d1=first[x.j];
  let T=1,accept=d1===1;
  if(d1===C){
   T++;
   const d2=second[x.z];
   if(d2===C){T++;accept=Boolean(mask&(1<<x.bit));}
   else accept=d2===1;
  }
  tp+=T*x.P;tq+=T*x.Q;
  if(accept){a+=x.P;b+=x.Q;}
 }
 return [a,b,tp,tq];
}
const score = o => 8*(o[0]-o[1])-o[2]-o[3]; // F_{1/8} numerator / 3200
function exhaustive(refined){
 let count=0,best=-Infinity,example=null;
 const firsts=refined?9:3;
 for(let n=0;n<firsts;n++){
  const first=refined?[Math.floor(n/3),n%3]:[n,n];
  for(let k=0;k<9;k++){
   const second=[Math.floor(k/3),k%3];
   for(let mask=0;mask<256;mask++){
    const o=observe(first,second,mask), v=score(o);count++;
    if(v>best){best=v;example={first,second,terminal_mask:mask,O_num:o};}
   }
  }
 }
 return {count,best,example};
}
const old=exhaustive(false),refined=exhaustive(true);
assert.equal(old.count,6912);assert.equal(refined.count,20736);
assert.equal(old.best,-800);assert.equal(refined.best,-560);
const witnessMask=atoms.reduce((bits,x)=>bits|(x.P>x.Q?1<<x.bit:0),0);
const witness=observe([0,2],[2,2],witnessMask);
assert.deepEqual(witness,[165,35,800,800]);
assert.equal(score(witness),-560);
const report={schema:'EC48W_EXACT_INTEGER_CERTIFICATE_V1',date:'2026-10-28',
 claim:'all one-step LR-threshold supports identical across J; two future decisions give strict one-state raw-region gap',
 denominator:400,terminal_observation_fibers:8,leaf_count:16,
 controller_counts:{old:old.count,refined_J_erased:refined.count},
 score_denominator:3200,optimal_score_numerators:{old:old.best,refined:refined.best,gap:refined.best-old.best},
 optimal_rationals:{old:'-1/4',refined:'-7/40',gap:'3/40'},
 witness:{t1_by_J:[0,2],t2_by_Z1:[2,2],t3_accept_if:'Lfull>1',O:['33/80','7/80','2','2']},
 leaf_rows:atoms.map(({h,j,z,v,P,Q,lr})=>({H:h?'B':'A',J:j,Z1:z,Z2:v,P_num:P,Q_num:Q,full_LR:lr})),
 status:'AUTHOR_EXACT_FINITE_PASS_UNREVIEWED_NOT_ADMITTED',native_X6_run:false,native_claim:false};
fs.writeFileSync('EXACT_REPORT_JS.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({controller_counts:report.controller_counts,optimal_rationals:report.optimal_rationals,witness:report.witness}));
