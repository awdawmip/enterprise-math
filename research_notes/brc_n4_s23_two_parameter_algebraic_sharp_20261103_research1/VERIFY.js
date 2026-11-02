"use strict";
const runCheck = function runCheck(){
"use strict";
const absN=x=>x<0n?-x:x;
function gcd(a,b){a=absN(a);b=absN(b);while(b){let c=a%b;a=b;b=c;}return a;}
function F(a,b=0n,d=1n){a=BigInt(a);b=BigInt(b);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){a=-a;b=-b;d=-d;}const g=gcd(gcd(a,b),d);return [a/g,b/g,d/g];}
const Q=(n,d=1)=>F(BigInt(n),0n,BigInt(d));
const rat=str=>{const [n,d="1"]=String(str).split("/");return Q(n,d);};
const alpha=F(0,1), Z=Q(0), O=Q(1), HALF=Q(1,2);
const add=(x,y)=>F(x[0]*y[2]+y[0]*x[2],x[1]*y[2]+y[1]*x[2],x[2]*y[2]);
const neg=x=>F(-x[0],-x[1],x[2]);
const sub=(x,y)=>add(x,neg(y));
const mul=(x,y)=>F(x[0]*y[0]-46000n*x[1]*y[1],x[0]*y[1]+x[1]*y[0]+634n*x[1]*y[1],x[2]*y[2]);
function sgn(x){const p=x[0]+317n*x[1],z=-x[1];if(p===0n)return z>0n?1:z<0n?-1:0;if(z===0n)return p>0n?1:-1;const sp=p>0n?1:-1,sz=z>0n?1:-1;if(sp===sz)return sp;const delta=p*p-54489n*z*z;return delta===0n?0:delta>0n?sp:sz;}
const cmp=(x,y)=>sgn(sub(x,y)),eq=(x,y)=>cmp(x,y)===0;
const abs=x=>sgn(x)<0?neg(x):x, max=(x,y)=>cmp(x,y)>=0?x:y;
const sum=arr=>arr.reduce(add,Z),fmt=x=>`(${x[0]}${x[1]>=0n?"+":""}${x[1]}*alpha)/${x[2]}`;
function check(ok,msg){if(!ok)throw Error("FAIL "+msg);}
const ss=mul(alpha,Q(1,250)),tt=mul(alpha,Q(1,184)),R=sub(O,mul(alpha,Q(1,230)));
check(eq(sub(mul(alpha,alpha),mul(Q(634),alpha)),Q(-46000)),"field relation");
check(cmp(ss,Z)>0&&cmp(ss,O)<0&&cmp(tt,Z)>0&&cmp(tt,O)<0,"interior");
const A=[0,0,0,1,1,1],B=[2,2,3,2,2,4],C=[5,6,7,8,9,10],G=[0,0,1,2,2,3];
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
const PAIRS=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12","12 13 23 24","23 34 12 13","24 34 12 14"];
const FREE=["2/5 0 2/5 1/5;2/5 2/5 0 1/5;3/5 0 0 2/5;2/5 2/5 0 1/5","1/2 1/2 0 0;1/2 0 0 1/2;0 0 1/2 1/2;0 0 1/2 1/2","3/5 2/5 0 0;2/5 2/5 1/5 0;1/3 43/105 3/35 6/35;1/7 2/35 2/5 2/5"];
const names=["D1","D2","D3","D4","D6","D7","D8","K1_old","K2_old","K3_repair"];
const fixed=PAIRS.map(p=>p.split(" ").map(w=>[1,2,3,4].map(k=>Q([...w].filter(x=>Number(x)===k).length,2))));
const free=FREE.map(str=>str.split(";").map(row=>row.trim().split(/\s+/).map(rat)));
const decoders=[...fixed,...free];
check(decoders.every(D=>D.length===4&&D.every(row=>row.length===4&&eq(sum(row),O))),"stochastic kernels");
function mix(rows){return M.map(w=>[0,1,2,3].map(j=>sum(w.map((val,k)=>mul(Q(val,20),rows[k][j])))));}
const observedD=decoders.map(d=>mix(G.map(i=>d[i])));
function prepare(s,t){const v=[Q(1,5),s,t,Z,Z,O,O,Z,Q(1,5),O,Z];const rows=A.map((ai,i)=>{let x=v[ai],b=v[B[i]],c=v[C[i]],omx=sub(O,x),omb=sub(O,b);return [x,mul(omx,b),mul(mul(omx,omb),c),mul(mul(omx,omb),sub(O,c))];});check(rows.every(row=>eq(sum(row),O)),"normalized source");return mix(rows);}
function risk(P,QD){let m=Z;for(let i=0;i<6;i++){const v=mul(HALF,sum(P[i].map((a,j)=>abs(sub(a,QD[i][j])))));m=max(m,v);}return m;}
function risks(s,t){const P=prepare(s,t);return observedD.map(d=>risk(P,d));}
const witness=risks(ss,tt),min=arr=>arr.reduce((a,b)=>cmp(a,b)<=0?a:b);
check(eq(min(witness),R),"sharp lower witness");
for(const i of [0,6,7,8])check(eq(witness[i],R),"active labels "+names[i]);
check(cmp(R,Q(7,11))>0,"strict improvement");
const old=risks(Q(1,3),Q(5,11));check(eq(min(old),Q(7,11)),"old witness");
const xs=[...Array.from({length:11},(_,i)=>Q(i,10)),ss].sort(cmp),ys=[...Array.from({length:11},(_,i)=>Q(i,10)),tt].sort(cmp);
check(xs.length===12&&ys.length===12,"grid nodes");
const vertex=xs.map(x=>ys.map(y=>risks(x,y)));
const assignments=[],counts=Array(names.length).fill(0);
for(let i=0;i<11;i++)for(let j=0;j<11;j++){
  const endpoints=[vertex[i][j],vertex[i+1][j],vertex[i][j+1],vertex[i+1][j+1]];
  let pick=-1;
  for(let k=0;k<names.length;k++)if(endpoints.every(row=>cmp(row[k],R)<=0)){pick=k;break;}
  check(pick>=0,`uncovered cell ${i},${j}`);assignments.push(pick);counts[pick]++;
}
return {pass:"PASS_BRC_S23_2D_ALGEBRAIC_GLOBAL_SHARP_QUADRATIC_FIELD_20261103",
basis:"alpha=317-sqrt(54489), alpha^2-634*alpha+46000=0 (smaller real root)",
source_model:"six labeled causal sources, nonuniform M/20 and pinned 10 decoders as 20261102 VERIFY.js",
domain:"(1/5,s,t,0,0;1,1,0,1/5,1,0), all real 0<=s,t<=1",
s_star:fmt(ss),t_star:fmt(tt),R_star:fmt(R),
numeric:{s:(317-Math.sqrt(54489))/250,t:(317-Math.sqrt(54489))/184,r:(Math.sqrt(54489)-87)/230},
witness_risks:witness.map(fmt),old_min:fmt(min(old)),
exact_field_comparison:"For x=(a+b*alpha)/d, d>0, sign from p=a+317*b,q=-b and exact comparison p^2 vs 54489*q^2, with quadrant signs.",
interpolation:"P(s,t) is separately affine in s,t; within any rectangle it is a common nonnegative bilinear convex combination of its four endpoint source-tuples. Fixed-decoder TV/max convexity extends a four-corner bound.",
grid:"{0,1/10,...,1,s_star} x {0,1/10,...,1,t_star}",
verified_vertices:144,verified_cells:121,decoder_names:names,cell_choice_row_major:assignments,cell_decoder_counts:counts,
scope:"exact optimized worst error of the pinned ten-kernel bank on this 2D legal face; no reoptimization of three kernels",
frozen_scientific_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
prior_bank_pin:"57a6db1d81068504cca2b3a6ea809a63555473d6",
native_claim:false,independent_review:false};
};
console.log(JSON.stringify(runCheck(),null,2));
