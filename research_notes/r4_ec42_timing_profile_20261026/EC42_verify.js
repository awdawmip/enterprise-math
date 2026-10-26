'use strict';
// R4-EC42: independent exact-integer three-stage finite BRC observer check.
// All path counts are positive integers out of 8 per h/hypothesis.
// No floating point, solver dependency, physical propagation, or hidden sources.
const EX={
 a:{P:[3,3,1,1],Q:[1,1,3,3]},
 b:{P:[3,1,3,1],Q:[1,3,1,3]}
};
function options(){
 const out=[{act:'P'},{act:'Q'}];
 for(const x of ['P','Q'])for(const y of ['P','Q'])
   out.push({act:'C',terminal:[x,y]});
 return out;
}
function vector(h,first,locals){
 const out=[0,0,0,0], e=EX[h];
 for(let z1=0;z1<2;z1++)for(let z2=0;z2<2;z2++){
   const i=2*z1+z2, lp=e.P[i],lq=e.Q[i];
   let dec=first, depth=1;
   if(first==='C'){
     const node=locals[z1];
     if(node.act==='C'){dec=node.terminal[z2];depth=3}
     else {dec=node.act;depth=2}
   }
   if(dec==='Q')out[0]+=lp;
   if(dec==='P')out[1]+=lq;
   out[2]+=lp*depth;out[3]+=lq*depth;
 }
 return out;
}
function policies(h){
 const out=[{first:'P',v:vector(h,'P')},{first:'Q',v:vector(h,'Q')}];
 const ops=options();
 for(const x of ops)for(const y of ops){
   out.push({first:'C',v:vector(h,'C',[x,y]),local:[x,y]});
 }
 return out;
}
function dot(a,b){let t=0;for(let i=0;i<4;i++)t+=a[i]*b[i];return t}
function pairMin(A,B,n,coarse){
 let best=Infinity,count=0;
 for(const a of A)for(const b of B){
   if(coarse&&a.first!==b.first)continue;
   const v=dot(n,a.v)+dot(n,b.v);
   if(v<best)best=v;
   count++;
 }
 return {best,count};
}
function predicted(A,B,n){
 const s=8*(Math.min(n[0],n[1])+n[2]+n[3]);
 const ca=Math.min(...A.filter(p=>p.first==='C').map(p=>dot(n,p.v)));
 const cb=Math.min(...B.filter(p=>p.first==='C').map(p=>dot(n,p.v)));
 const ga=s-ca,gb=s-cb;
 return {full:2*s-Math.max(0,ga)-Math.max(0,gb),
         coarse:2*s-Math.max(0,ga+gb),ga,gb};
}
function assert(b,msg){if(!b)throw new Error(msg)}
function verify(){
 const A=policies('a'),B=policies('b');
 assert(A.length===38&&B.length===38,'policy cardinalities');
 for(const h of ['a','b']){
  for(const k of ['P','Q']){
   const vals=EX[h][k];
   assert(vals.every(x=>Number.isInteger(x)&&x>0),'positive source count');
   assert(vals.reduce((u,v)=>u+v,0)===8,'source normalization');
  }
 }
 function terminalPairs(h){
  return EX[h].P.map((p,i)=>p+','+EX[h].Q[i]).sort().join(';');
 }
 assert(terminalPairs('a')===terminalPairs('b'),'terminal Bayes profile equality');
 let normals=0,strict=0,positiveGuard=0;
 for(let i=-2;i<=2;i++)for(let j=-2;j<=2;j++)
 for(let k=-2;k<=2;k++)for(let l=-2;l<=2;l++){
   const n=[i,j,k,l],x=pairMin(A,B,n,false),
      y=pairMin(A,B,n,true),f=predicted(A,B,n);
   assert(x.count===1444&&y.count===1298,'policy enumeration');
   assert(x.best===f.full&&y.best===f.coarse,'support formula mismatch');
   assert(y.best>=x.best,'compression lowered minimum');
   normals++;
   if(y.best>x.best)strict++;
   positiveGuard+=Number(f.ga>0&&f.gb<0||f.gb>0&&f.ga<0);
   assert((y.best>x.best)===(f.ga>0&&f.gb<0||f.gb>0&&f.ga<0),
      'sign criterion mismatch');
 }
 const n=[6,6,1,1],x=pairMin(A,B,n,false),
   y=pairMin(A,B,n,true),f=predicted(A,B,n);
 assert(x.best===120&&y.best===128&&f.ga===8&&f.gb===-8,
   'precise separating normal');
 const ap=A.find(p=>p.first==='C'&&p.local[0].act==='P'&&p.local[1].act==='Q');
 const bp=B.find(p=>p.first==='P');
 const vv=ap.v.map((a,i)=>a+bp.v[i]);
 assert(vv.join(',')==='2,10,24,24','optimal four-observer vector');
 return {
  schema:'EM_R4_EC42_EXACT_REPORT_V1',research_unit:'R4-EC42',
  arithmetic:'exact integer source counts and integer normal supports',
  terminal_counts:EX,terminal_likelihood_pair_multisets_equal:true,
  policy_counts:{per_history:38,full:1444,compressed_first_stage:1298},
  enumeration:{normal_grid:'{-2,-1,0,1,2}^4',checked: normals,
    strict_support_gaps:strict,sign_equivalence_checks:normals,
    strict_sign_crossings:positiveGuard},
  witness:{normal_scaled_6:[6,6,1,1],first_stage_gains_scaled_48:[8,-8],
    full_cost_numerator_over_96:120,compressed_cost_numerator_over_96:128,
    strict_gap:'1/12',optimal_full_observer_vector:['1/8','5/8','3/2','3/2']},
  theorem_scope:'finite horizon; one-time first-stage compression; later full provenance; equal positive initial P/Q weights',
  evidence_class:'author mathematical derivation plus finite exact execution, not formal proof acceptance',
  native_X6_test:'NOT_PERFORMED',independent_Driver_review:'NOT_PERFORMED',test_status:'PASS'
 };
}
if(typeof module!=='undefined' && typeof require!=='undefined' && require.main===module)
 process.stdout.write(JSON.stringify(verify(),null,2)+'\n');
