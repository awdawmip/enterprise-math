/* Enterprise Math R698: exact separation/noise margin for the frozen R697 E* BRC probe menu.
 * Scope: 60 labeled paths with four-box capacities (24,18,6,12), known retained total s.
 * All arithmetic is integer; no floating-point scientific computation.
 * Input references: R697 commit 2c1c87f9f543aa8046aa847c30c5b7581caba64c.
 * Run: node R698_BRC_TWO_PROBE_NOISE_MARGIN.js
 */
'use strict';
const N=[24,18,6,12];
const boxes=Array.from({length:61},()=>new Map());
const sum=a=>a.reduce((x,y)=>x+y,0);
const sig=v=>[4*v[0]+5*v[1]+v[3],2*v[0]+2*v[2]+v[3]];
const same=(a,b)=>a.every((x,i)=>x===b[i]);
let count=0;
for(let e=0;e<=24;e++) for(let t=0;t<=18;t++) for(let c=0;c<=6;c++) for(let z=0;z<=12;z++) {
  const v=[e,t,c,z],s=sum(v); if(!s)continue;
  const [U,V]=sig(v),key=U+','+V;
  if(boxes[s].has(key)) throw Error('R697 injectivity violated');
  boxes[s].set(key,v);count++;
}
if(count!==43224)throw Error('histogram population');
const makeAtTotal=(s,lo,hi)=>{
  const v=lo.slice();let remainder=s-sum(v);
  if(remainder<0||s>sum(hi))throw Error('no witness total');
  for(let i=0;i<4;i++){const add=Math.min(remainder,hi[i]-v[i]);v[i]+=add;remainder-=add;}
  if(remainder)throw Error('failed bounded fill');
  return v;
};
const records=[];
let checkedNearPairs=0;
for(let s=1;s<=60;s++){
  const M=boxes[s],expected=s===60?null:(s>=3&&s<=57?1:2);
  let found=Infinity,example=null;
  for(const [key,v] of M){
    const [U,V]=key.split(',').map(Number);
    for(let du=-2;du<=2;du++)for(let dv=-1;dv<=1;dv++){
      if(du===0&&dv===0)continue;
      const other=M.get((U+du)+','+(V+dv));
      if(other){checkedNearPairs++;const q=Math.max(Math.abs(du),2*Math.abs(dv));
        if(q<found){found=q;example={left:v,right:other,deltaU:du,deltaV:dv};}
      }
    }
  }
  if(s===60){if(M.size!==1||found!==Infinity)throw Error('unique full box');}
  else if(found!==expected)throw Error('margin mismatch at '+s+': '+found);
  if(s>=3&&s<=57){
    const base=makeAtTotal(s,[0,1,2,0],[23,18,6,10]);
    const next=[base[0]+1,base[1]-1,base[2]-2,base[3]+2];
    const [u,v]=sig(base),[u1,v1]=sig(next);
    if(!M.has(u+','+v)||!M.has(u1+','+v1)||Math.abs(u-u1)!==1||v!==v1)throw Error('inner witness');
  }
  if([1,2,58,59].includes(s)){
    const base=makeAtTotal(s,[0,0,1,0],[24,18,6,11]);
    const next=[base[0],base[1],base[2]-1,base[3]+1];
    const [u,v]=sig(base),[u1,v1]=sig(next);
    if(!M.has(u+','+v)||!M.has(u1+','+v1)||Math.abs(u-u1)!==1||Math.abs(v-v1)!==1)throw Error('edge witness');
  }
  records.push({s,histogram_count:M.size,integer_scaled_probe_min_Linf:expected,witness:example});
}
const output={schema:'EM_R698_BRC_TWO_PROBE_NOISE_MARGIN_V1',status:'R698_ALL_EXACT_ASSERTIONS_PASS',
 frozen_candidate_source:'2c1c87f9f543aa8046aa847c30c5b7581caba64c',
 scope:'R697 E* static independent binary path gate candidate, known exact retained path count s, no native V29/V39 realization asserted',
 capacities:N,total_integer_configurations:count,
 raw_observers:'T3=U/(10s),T8=V/(5s), U=4e+5t+z, V=2e+2c+z',
 scaled_signature:'(U,2V)=(10s T3,10s T8)',
 min_separation_scaled_raw_chebyshev:{s_1_2_58_59:2,s_3_through_57:1,s_60:'single state'},
 sharp_uniform_abs_measurement_error_radius:{s_1_2_58_59:'1/(10s)',s_3_through_57:'1/(20s)',s_60:'no observation needed'},
 proof:'integer lattice spacing; kernel inversion of R697; for |DeltaU|=1, DeltaV=0 the bounded difference vectors are (1,-1,-2,2) or (-2,3,5,-6) up to sign; the first is feasible precisely for s=3..57, the second for s=8..52; c-z swap gives edge distance 2',
 checked_near_pairs:checkedNearPairs,by_s:records};
console.log(JSON.stringify(output,null,2));
