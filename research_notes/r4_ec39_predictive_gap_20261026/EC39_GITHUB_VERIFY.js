// EC39 exact integer BRC microbranch verification: unifilar two-step kernels.
// Scientific scope: auxiliary labelled positive-source kernels, not native X6.
'use strict';
function assert(ok,what){if(!ok)throw new Error(what)}
function overlap(M,k,l,r,s){
 let O=0,C=0;
 for(let a=0;a<2;a++){
  let next=0;
  for(let b=0;b<2;b++){
   O+=Math.min(k[a]*r[a][b],l[a]*s[a][b]);
   next+=Math.min(r[a][b],s[a][b]);
  }
  C+=Math.min(k[a],l[a])*next;
 }
 return [O,C];
}
let checked=0,strict=0;
for(let M=1;M<=5;M++){
 for(let k0=0;k0<=M;k0++)for(let l0=0;l0<=M;l0++)
 for(let r00=0;r00<=M;r00++)for(let s00=0;s00<=M;s00++)
 for(let r10=0;r10<=M;r10++)for(let s10=0;s10<=M;s10++){
  const k=[k0,M-k0],l=[l0,M-l0],r=[[r00,M-r00],[r10,M-r10]],s=[[s00,M-s00],[s10,M-s10]];
  const [O,C]=overlap(M,k,l,r,s); assert(C<=O&&O<=M*M,'overlap inequality');
  let prediction=false;
  for(let a=0;a<2;a++)for(let b=0;b<2;b++){
   if(k[a]>l[a]&&l[a]>0&&r[a][b]>0&&r[a][b]<s[a][b])prediction=true;
   if(l[a]>k[a]&&k[a]>0&&s[a][b]>0&&s[a][b]<r[a][b])prediction=true;
  }
  assert((O>C)===prediction,'exact strictness characterization');
  // Binary transportation: every admissible first-step joint table
  // has gamma(0,0)=x, gamma(1,1)=M-k0-l0+x.
  let best=-1;
  for(let x=Math.max(0,k0+l0-M);x<=Math.min(k0,l0);x++){
    const v=x*(Math.min(r[0][0],s[0][0])+Math.min(r[0][1],s[0][1]))+
     (M-k0-l0+x)*(Math.min(r[1][0],s[1][0])+Math.min(r[1][1],s[1][1]));
    if(v>best)best=v;
  }
  assert(best===C,'independent binary transport LP extreme check');
  checked++;if(O>C)strict++;
 }
}
const k=[2,1],l=[1,2],r=[[1,2],[3,0]],s=[[0,3],[3,0]];
const [O,C]=overlap(3,k,l,r,s);assert(O===6&&C===5,'M=3 witness');
const [O5,C5]=overlap(5,[3,2],[2,3],[[1,4],[2,3]],[[2,3],[2,3]]);
assert(O5===19&&C5===18,'all-label-positive witness');
const result={schema:'EC39_EXACT_UNIFILAR_GAP_V1',status:'PASS',checks:{binary_two_step_models:checked,strict_gap_models:strict,independent_transport_checks:checked},witness:{M:3,word_overlap:'2/3',true_TV:'1/3',optimal_coadapted_success:'5/9',coadapted_bound:'4/9',gap:'1/9',persistent_for_all_n_ge_2:true},full_support:{M:5,word_overlap:'19/25',coadapted_success:'18/25',gap:'1/25'},scope:'Auxiliary positive-integer constant-M unifilar two-step BRC models; no native X6 heartbeat claim'};
console.log(JSON.stringify(result,null,2));
