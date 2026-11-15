// Exact rational / quadratic-field evidence for the BRC N4 S23 three-control theorem.
// Node.js: node VERIFY.js. No npm dependencies; all comparisons are exact.
"use strict";
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
function q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];}
const q0=q(0),q1=q(1),qh=q(1,2);
const qa=(x,y)=>q(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);
const qn=x=>[-x[0],x[1]];
const qs=(x,y)=>qa(x,qn(y));
const qm=(x,y)=>q(x[0]*y[0],x[1]*y[1]);
const qc=(x,y)=>{const n=x[0]*y[1]-y[0]*x[1];return n<0n?-1:n>0n?1:0;};
const qabs=x=>x[0]<0n?qn(x):x;
const qe=(x,y)=>qc(x,y)===0;
const fm=x=>x[0].toString()+(x[1]===1n?"":"/"+x[1].toString());
const k=x=>[x,q0],ksqrt=[q0,q1],k0=k(q0);
const ka=(x,y)=>[qa(x[0],y[0]),qa(x[1],y[1])];
const kn=x=>[qn(x[0]),qn(x[1])];
const ksub=(x,y)=>ka(x,kn(y));
const km=(x,y)=>[qa(qm(x[0],y[0]),qm(q(43),qm(x[1],y[1]))),qa(qm(x[0],y[1]),qm(x[1],y[0]))];
function ksign(x){const sa=qc(x[0],q0),sb=qc(x[1],q0);if(!sa)return sb;if(!sb||sa===sb)return sa;const diff=qs(qm(x[0],x[0]),qm(q(43),qm(x[1],x[1])));const sd=qc(diff,q0);return sa*sd;}
const kc=(x,y)=>ksign(ksub(x,y));
const kabs=x=>ksign(x)<0?kn(x):x;
const ke=(x,y)=>kc(x,y)===0;
const OQ={zero:q0,one:q1,half:qh,cast:x=>x,add:qa,sub:qs,mul:qm,abs:qabs,cmp:qc};
const OK={zero:k0,one:k(q1),half:k(qh),cast:k,add:ka,sub:ksub,mul:km,abs:kabs,cmp:kc};
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
function prepared(a,b,c,O){
  const v=(n,d=1)=>O.cast(q(n,d)),h=v(1,2),one=O.one;
  function F(x,y,z){let s=O.sub(one,x),t=O.mul(s,O.sub(one,y));return [x,O.mul(s,y),O.mul(t,z),O.mul(t,O.sub(one,z))];}
  const sources=[F(a,b,h),F(a,b,h),F(a,O.zero,c),F(v(1,4),b,h),F(v(1,4),b,h),F(v(1,4),v(1,3),h)];
  return M.map(row=>Array.from({length:4},(_,i)=>row.reduce((acc,m,j)=>m?O.add(acc,O.mul(v(m,20),sources[j][i])):acc,O.zero)));
}
function dist(P,T,O){let best=O.zero;for(let i=0;i<6;i++){let z=O.zero;for(let j=0;j<4;j++)z=O.add(z,O.abs(O.sub(P[i][j],T[i][j])));z=O.mul(z,O.half);if(O.cmp(z,best)>0)best=z;}return best;}
function p(a,b,c){return prepared(a,b,c,OQ);}
const max=(x,y)=>qc(x,y)>=0?x:y;
const max4=(a,b,c,d)=>max(max(a,b),max(c,d));
const plus=(x,y)=>qa(x,y);
const omega=(A,B,C)=>max4(A,plus(plus(qm(q(7,8),A),qm(qh,B)),qm(A,B)),plus(plus(qm(q(7,8),A),qm(qh,C)),qm(A,C)),qm(q(3,4),B));
function assert(cond,msg){if(!cond)throw Error("FAILED: "+msg);}
const L=[q(1,2),q(7,8)],U=[q(1,8),q(1,2)],V=[q(1,2),q(7,8)];
let vertices=[];for(const a of L)for(const b of U)for(const c of V)vertices.push([a,b,c]);
const hullStrategies=[[q(1,2),q(1,8),q(7,8)],[q(1,2),q(1,2),q(1,2)],[q(7,8),q(1,8),q(7,8)],[q(7,8),q(1,2),q(1,2)]];
const weights=[q(4,9),q(1,18),q(2,9),q(5,18)];
const joint=hullStrategies.map(v=>p(...v));
const center=M.map((_,i)=>Array.from({length:4},(_,j)=>weights.reduce((z,w,h)=>qa(z,qm(w,joint[h][i][j])),q0)));
let maxHull=q0;for(const v of vertices)maxHull=max(maxHull,dist(p(...v),center,OQ));
assert(qe(maxHull,q(3,16)),"hull witness eight vertices");
const r=km(ksub(ksqrt,k(q(5))),k(q(1,8)));
const x=ksub(k(q(7,8)),r);
const y=ksub(k(qh),km(k(q(4,3)),r));
const t=km(k(q(2,27)),ka(ksqrt,k(q(4))));
assert(ke(ka(ka(km(k(q(32)),km(r,r)),km(k(q(40)),r)),k(q(-9))),k0),"quadratic root");
assert(kc(x,k(q(1,2)))>=0&&kc(x,k(q(7,8)))<=0,"lawful x");
assert(kc(y,k(q(1,8)))>=0&&kc(y,k(q(1,2)))<=0,"lawful y");
assert(kc(t,k(q(1,2)))>=0&&kc(t,k(q(7,8)))<=0,"lawful t");
const cLaw=prepared(x,y,t,OK);
let maxLaw=k0;for(const v of vertices){const Q=prepared(...v.map(k),OK);const d=dist(Q,cLaw,OK);if(kc(d,maxLaw)>0)maxLaw=d;}
assert(ke(maxLaw,r),"lawful radical center eight vertices");
assert(ke(ksub(k(q(7,8)),x),r),"lower event 1");
assert(ke(ksub(k(q(7,16)),km(ksub(k(q1),x),ksub(k(q1),y))),r),"lower event 2");
assert(ke(km(k(q(3,4)),ksub(k(qh),y)),r),"lower event 3");
const cases=[[q0,q0,q0],[q(1,800),q(1,800),q(1,800)],[q(1,8),q(1,8),q(1,8)],[q(1,1024),q(1,512),q(1,512)]];
const aa=[q(1,2),q(11,16),q(7,8)],bb=[q(1,8),q(5,16),q(1,2)],cc=[q(1,2),q(11,16),q(7,8)];
let comparisons=0,achieved=0;
for(const [A,B,C] of cases){
  const bound=omega(A,B,C);
  const witnesses=[
    dist(p(qh,q(1,8),qh),p(qs(qh,A),q(1,8),qh),OQ),
    dist(p(qh,q(1,8),qh),p(qs(qh,A),qs(q(1,8),B),qh),OQ),
    dist(p(qh,q(1,8),q(7,8)),p(qs(qh,A),q(1,8),qa(q(7,8),C)),OQ),
    dist(p(qh,q(1,8),qh),p(qh,qs(q(1,8),B),qh),OQ)
  ];
  let witnessed=q0;for(const val of witnesses)witnessed=max(witnessed,val);
  assert(qe(witnessed,bound),"attained full sharp anisotropic modulus");
  achieved++;
  for(const a of aa)for(const b of bb)for(const c of cc){
    const s=p(a,b,c);
    for(const da of [qn(A),q0,A])for(const db of [qn(B),q0,B])for(const dc of [qn(C),q0,C]){
      const z=p(qa(a,da),qa(b,db),qa(c,dc));
      assert(qc(dist(s,z,OQ),bound)<=0,"sample pointwise modulus");
      comparisons++;
    }
  }
}
const delta=q(1,800),eta=omega(delta,delta,delta),gap=ksub(r,k(q(3,16)));
const newMargin=ksub(gap,k(qm(q(4),eta)));
assert(qe(eta,q(1101,640000)),"isotropic exact modulus");
assert(kc(newMargin,k(q(1,4000)))>0,"improved neighborhood lower bound");
assert(qe(qs(q(43),qm(q(131141,20000),q(131141,20000))),q(2038119,400000000)),"squared rational margin");
const result={
  status:"PASS_BRC_N4_S23_SHARP_ANISOTROPIC_POINTWISE_MODULUS_20261101",
  arithmetic:"exact BigInt rational and Q(sqrt(43)); no floats",
  source_rows:6,source_branches:6,control_dimensions:3,
  original_strategy_grid:27,perturbation_offsets_per_strategy:27,
  complete_exact_sample_comparisons:comparisons,sharp_witness_cases:achieved,
  verified_base_hull_radius:fm(maxHull),verified_base_lawful_radius:"(sqrt(43)-5)/8",
  exact_isotropic_modulus_at_1_over_800:fm(eta),
  certified_open_box_delta:fm(delta),
  certified_gap_lower_bound:">1/4000",
  squared_margin_identity:"43-(131141/20000)^2=2038119/400000000>0",
  continuum_justification:"analytic coordinate range/modulus and multiaffine vertex maximum, not finite grid extrapolation",
  admission:"AUTHOR_EVIDENCE_ONLY_UNREVIEWED"
};
if(typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(result,null,2));
