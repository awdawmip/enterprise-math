'use strict';
// Exact integer verification for R762BJ. No third-party modules.
const assert = require('node:assert/strict');
const pairs = [];
for (let i=2;i<=6;i++) for(let j=i+1;j<=6;j++) pairs.push([i,j]);
assert.equal(pairs.length,10);
const popcount = x => {let n=0; while(x){n+=x&1; x>>=1;}return n;};
const degree = mask => {const d=Array(7).fill(0);for(let k=0;k<10;k++)if((mask>>k)&1){const [i,j]=pairs[k];d[i]++;d[j]++;}return d;};
const cover = mask => degree(mask).slice(2).every(x=>x>0);
const canTolerate = (mask,e) => {const d=degree(mask);return d.slice(2).every(x=>x>e);};
const bruteTolerate = (mask,e) => {for(let del=0;del<1024;del++){if((del&mask)!==del||popcount(del)>e)continue;if(!cover(mask&~del))return false;}return true;};
const stats=[];
for(let e=0;e<=3;e++){
 let minimum=11, examples=0, total=0, witness=null;
 for(let mask=0;mask<1024;mask++){
  const criterion=canTolerate(mask,e), exhaustive=bruteTolerate(mask,e);
  assert.equal(criterion,exhaustive,`disagreement mask=${mask} erasures=${e}`);
  if(!criterion)continue;
  total++;
  const k=popcount(mask);
  if(k<minimum){minimum=k;examples=0;witness=mask;}
  if(k===minimum)examples++;
 }
 stats.push({erasure_budget:e,min_rows:minimum,optimal_families:examples,all_admissible_families:total,
  witness_triples:pairs.filter((_,k)=>(witness>>k)&1).map(([i,j])=>`1${i}${j}`)});
}
assert.deepEqual(stats.map(s=>[s.min_rows,s.optimal_families,s.all_admissible_families]),
 [[3,30,768],[5,12,253],[8,15,26],[10,1,1]]);
const obs=(z,i,j)=>{const h=Math.min(z[0],z[i-1],z[j-1]);return [z[0]-h,z[i-1]-h,z[j-1]-h];};
const recover=(mask,z)=>{
  const dif=Array(6).fill(null);dif[0]=0;
  for(let k=0;k<10;k++)if((mask>>k)&1){const [i,j]=pairs[k],r=obs(z,i,j);dif[i-1]=r[1]-r[0];dif[j-1]=r[2]-r[0];}
  return dif;
};
let coordinate_cases=0,translation_cases=0;
for(let n=0;n<729;n++){
 let x=n;const z=[];for(let j=0;j<6;j++){z.push(x%3-1);x=Math.floor(x/3);}
 for(let mask=0;mask<1024;mask++){
  const dif=recover(mask,z),d=degree(mask);
  for(let i=2;i<=6;i++)assert.equal(dif[i-1],d[i]>0?z[i-1]-z[0]:null);
  coordinate_cases++;
 }
 for(const t of [-5,7]){
  const shifted=z.map(a=>a+t);
  for(let k=0;k<10;k++){
    const [i,j]=pairs[k];assert.deepEqual(obs(z,i,j),obs(shifted,i,j));translation_cases++;
  }
 }
}
const evidence={schema:'R762BJ_EXACT_NATIVE_STAR_VERIFICATION_V1',subset_masks:1024,
  mask_erasure_pairs_checked:4096,three_level_states:729,coordinate_reconstructions:coordinate_cases,
  diagonal_shift_observer_checks:translation_cases,erasure_table:stats,
  coverage:'All 1024 labelled star subfamilies; all deletions of <=e rows for e=0..3; all {-1,0,1}^6 integer chart inputs for each subfamily; shifts -5,+7',
  proof_status:'Symbolic group/graph proof in accompanying research note; finite assertions are supporting tests',
  checks_passed:true};
console.log(JSON.stringify(evidence,null,2));
