'use strict';
/* Exact labelled C4-BRC: 3 sources; 9 ordered source-pair products per event bin.
 * External unchanged coherent reference adds a 4th label and 16 ordered pairs.
 * All quantities are exact Gaussian integer pairs in safe JS integer range.
 */
const assert = require('node:assert/strict');
const ZERO=[0,0],ONE=[1,0],NEG=[-1,0],I=[0,1],NI=[0,-1];
const PH=[ONE,I,NEG,NI],V=[ZERO,ONE,NEG,I,NI,[1,1]];
function safe(x){assert(Number.isSafeInteger(x));return x;}
function plus(a,b){return [safe(a[0]+b[0]),safe(a[1]+b[1])];}
function star(a){return [a[0],-a[1]];}
function mul(a,b){return [safe(a[0]*b[0]-a[1]*b[1]),safe(a[0]*b[1]+a[1]*b[0])];}
function sum(v){return v.reduce(plus,ZERO);}
function eq(a,b){return a[0]===b[0]&&a[1]===b[1];}
function brc(paths){let z=ZERO,n=0;for(let j=0;j<paths.length;j++)for(let k=0;k<paths.length;k++){
 z=plus(z,mul(star(paths[j]),paths[k]));n++;
}assert(z[1]===0&&z[0]>=0);return {mass:z[0],pairs:n};}
function rows(q){return [[ONE,q,ZERO],[ZERO,NEG,q]];}
function read(rs,a){return rs.map(row=>brc(row.map((z,j)=>mul(z,a[j]))));}
function perms(a){return a.length?[...a.flatMap((x,j)=>perms(a.filter((_,k)=>j!==k)).map(y=>[x,...y]))]:[[]];}
function grid(a,n){return n===0?[[]]:grid(a,n-1).flatMap(xs=>a.map(x=>[...xs,x]));}
function mrow(row,p,u){const v=[ZERO,ZERO,ZERO];for(let j=0;j<3;j++)v[p[j]]=mul(row[j],u[j]);return v;}
function signature(m){return m.p.join('')+'|'+m.u.map(z=>z.join(',')).join(';');}
const mono=perms([0,1,2]).flatMap(p=>grid(PH,3).map(u=>({p,u})));
const W=[[ONE,ZERO,ZERO],[ZERO,ONE,ZERO],[ZERO,ZERO,ONE],
 [ONE,ONE,ZERO],[ONE,ZERO,ONE],[ZERO,ONE,ONE],
 [ONE,I,ZERO],[ONE,ZERO,I],[ZERO,ONE,I]];
const inputs=grid(V,3);
function run(){
 assert(mono.length===384&&W.length===9&&inputs.length===216);
 const results=[];let candidateCases=0,witnessBins=0,witnessPairs=0,rejected=0;
 let fullCases=0,fullBins=0,fullPairs=0,coeffs=0;
 for(const q of PH)for(const qp of PH){
  const r=mul(qp,star(q)),target=rows(qp),baseline=W.map(a=>read(target,a).map(z=>z.mass)),accepted=[];
  for(const a of mono){
   const out=rows(q).map(row=>mrow(row,a.p,a.u));
   let ok=true;
   for(let k=0;k<W.length;k++){
    const v=read(out,W[k]);candidateCases++;witnessBins+=2;witnessPairs+=18;
    if(v[0].mass!==baseline[k][0]||v[1].mass!==baseline[k][1]){rejected++;ok=false;break;}
   }
   if(ok)accepted.push({a,out});
  }
  assert(accepted.length===4);
  const expected=new Set(PH.map(u=>signature({p:[0,1,2],u:[u,mul(u,r),mul(u,mul(r,r))]})));
  assert.deepEqual(new Set(accepted.map(x=>signature(x.a))),expected);
  for(const {a,out} of accepted){
   for(let k=0;k<2;k++)for(let j=0;j<3;j++){
    assert(eq(out[k][j],mul(k===0?a.u[0]:a.u[1],target[k][j])));coeffs++;
   }
   for(const x of inputs){
    const lhs=read(out,x),rhs=read(target,x);
    assert(lhs[0].mass===rhs[0].mass&&lhs[1].mass===rhs[1].mass);
    fullCases++;fullBins+=4;fullPairs+=36;
   }
  }
  results.push({q:PH.indexOf(q),qp:PH.indexOf(qp),r,accepted:accepted.map(x=>x.a)});
 }
 assert(results.length===16&&rejected===6080&&fullCases===13824);
 const reference=PH.map(u=>({u,mass_num_over_four:brc([u,ZERO,ZERO,[2,0]]).mass}));
 assert.deepEqual(reference.map(z=>z.mass_num_over_four),[9,5,1,5]);
 return {schema:'EM_PREFIX301_C4_EVENT_MASS_STABILIZER_V1',status:'AUTHOR_SIDE_EXACT_PROOF_UNREVIEWED_NOT_ADMITTED',
  source_field:'Q(i)',phase_pairs:16,monomials_per_pair:384,probes:9,full_inputs:216,
  candidate_probe_cases:candidateCases,probe_event_readouts:witnessBins,probe_ordered_pairs:witnessPairs,
  rejected_with_witness:rejected,accepted_per_pair:4,accepted_total:64,
  coefficient_equalities:coeffs,full_input_cases:fullCases,full_event_readouts:fullBins,
  full_ordered_pairs:fullPairs,reference,exact_classes:results,native_model_law_id:null};
}
if(require.main===module)console.log(JSON.stringify(run(),null,2));
module.exports={run};