"use strict";
// Exact rational author-side BRC six-source verification. Run: node VERIFY.js
const b=v=>BigInt(v);
const gcd=(a,c)=>{a=a<0n?-a:a;c=c<0n?-c:c;while(c){const t=a%c;a=c;c=t;}return a;};
function q(n,d=1n){n=b(n);d=b(d);if(d<0n){n=-n;d=-d;}if(d===0n)throw Error("zero denominator");const g=gcd(n,d);return [n/g,d/g];}
const rat=s=>{const p=String(s).split("/");return q(p[0],p[1]||"1");};
const plus=(x,y)=>q(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);
const neg=x=>[-x[0],x[1]],minus=(x,y)=>plus(x,neg(y));
const times=(x,y)=>q(x[0]*y[0],x[1]*y[1]);
const abs=x=>x[0]<0n?neg(x):x;
const cmp=(x,y)=>{const d=x[0]*y[1]-y[0]*x[1];return d<0n?-1:d>0n?1:0;};
const max=(x,y)=>cmp(x,y)>=0?x:y;
const fmt=x=>String(x[0])+"/"+String(x[1]);
const eq=(x,y)=>cmp(x,y)===0;
const assert=(ok,msg)=>{if(!ok)throw Error("FAIL "+msg);};
const zero=q(0),one=q(1),half=q(1,2);
const A=[0,0,0,1,1,1],B=[2,2,3,2,2,4],C=[5,6,7,8,9,10],G=[0,0,1,2,2,3];
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
const PAIRS=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12",
"12 13 23 24","23 34 12 13","24 34 12 14"];
const FREE=["2/5 0 2/5 1/5;2/5 2/5 0 1/5;3/5 0 0 2/5;2/5 2/5 0 1/5",
"1/2 1/2 0 0;1/2 0 0 1/2;0 0 1/2 1/2;0 0 1/2 1/2",
"3/5 2/5 0 0;2/5 2/5 1/5 0;1/3 43/105 3/35 6/35;1/7 2/35 2/5 2/5"];
const names=["D1","D2","D3","D4","D6","D7","D8","K1_old","K2_old","K3_repair"];
const fixed=PAIRS.map(s=>s.split(" ").map(w=>[1,2,3,4].map(j=>q([...w].filter(v=>Number(v)===j).length,2))));
const free=FREE.map(s=>s.split(";").map(row=>row.trim().split(/\s+/).map(rat)));
const kernels=[...fixed,...free];
for(const [i,D] of kernels.entries())assert(D.length===4&&D.every(row=>row.length===4&&eq(row.reduce(plus,zero),one)),"stochastic "+i);
function mix(rows){return M.map(w=>[0,1,2,3].map(j=>w.reduce((acc,c,k)=>plus(acc,times(q(c,20),rows[k][j])),zero)));}
const observedDecoders=kernels.map(D=>mix(G.map(i=>D[i])));
function prepare(t){
 const z=[rat("1/5"),rat("1/3"),t,zero,zero,one,one,zero,rat("1/5"),one,zero];
 const R=A.map((a,i)=>{const x=z[a],bb=z[B[i]],c=z[C[i]],r=minus(one,x),u=minus(one,bb);
   return [x,times(r,bb),times(times(r,u),c),times(times(r,u),minus(one,c))];});
 assert(R.every(row=>eq(row.reduce(plus,zero),one)),"source normalization");
 return mix(R);
}
function risk(P,Q){return P.reduce((largest,row,i)=>{
 const s=row.reduce((acc,p,j)=>plus(acc,abs(minus(p,Q[i][j]))),zero);
 return max(largest,times(half,s));
},zero);}
function risks(t){const P=prepare(t);return observedDecoders.map(Q=>risk(P,Q));}
const tStar=rat("5/11"),r0=risks(zero),rStar=risks(tStar),r1=risks(one),rOld=risks(rat("9/20"));
const min=arr=>arr.reduce((a,v)=>cmp(a,v)<=0?a:v);
assert(eq(r0[0],rat("1/2")),"D1 at 0");
assert(eq(rStar[0],rat("7/11")),"D1 at 5/11");
assert(eq(rStar[6],rat("7/11")),"D8 at 5/11");
assert(eq(r1[6],rat("1/2")),"D8 at 1");
assert(eq(min(rStar),rat("7/11")),"new witness");
assert(eq(min(rOld),rat("19/30")),"previous witness");
const P0=prepare(zero),P1=prepare(one),Pt=prepare(rat("1/4"));
for(let i=0;i<6;i++)for(let j=0;j<4;j++)
 assert(eq(Pt[i][j],plus(times(rat("3/4"),P0[i][j]),times(rat("1/4"),P1[i][j]))),"affine component "+i+","+j);
const result={
 pass:"PASS_BRC_S23_A_SIDE_RELEASE_EDGE_SHARP_SEVEN_ELEVENTHS_20261102",
 scientific_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
 decoder_bank_pin:"57a6db1d81068504cca2b3a6ea809a63555473d6",
 prior_6d_result_pin:"c02114d77f9686730566fee07ea7b654acd171c0",
 family:"(1/5,1/3,t,0,0;1,1,0,1/5,1,0), all real 0<=t<=1",
 sharp_parameter:"5/11",sharp_risk:"7/11",
 old_t:"9/20",old_risk:"19/30",exact_gain:"1/330",
 labels:names,risks_at_sharp:rStar.map(fmt),
 exact_endpoint_certificates:{
 D1_at_0:fmt(r0[0]),D1_at_5_11:fmt(rStar[0]),
 D8_at_5_11:fmt(rStar[6]),D8_at_1:fmt(r1[6])},
 upper_bound_left:"1/2 + 3*t/10, 0<=t<=5/11",
 upper_bound_right:"3/4 - t/4, 5/11<=t<=1",
 proof:"Six source distribution rows affine in t; for each fixed decoder its max-of-TV risk is convex. On each side its endpoint chord supplies the displayed upper bound, strictly below 7/11 away from t=5/11. Exact ten risks at t=5/11 supply the lower bound.",
 robustness:"For any z in the valid 11-cube, m_bank(z)>=7/11 - sum_j |z_j-W7_j|; the relative L1 ball of radius 1/330 has m_bank>19/30.",
 native_claim:false,independent_review:false
};
console.log(JSON.stringify(result,null,2));
