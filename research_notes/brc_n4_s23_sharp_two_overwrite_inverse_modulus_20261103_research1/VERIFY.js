"use strict";
// Exact S23 positive-branch witness checker, frozen science at 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
// Run with: node VERIFY.js
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let r=a%b;a=b;b=r;}return a;}
function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return {n:n/g,d:d/g};}
const Z=Q(0),O=Q(1);
const add=(x,y)=>Q(x.n*y.d+y.n*x.d,x.d*y.d);
const sub=(x,y)=>Q(x.n*y.d-y.n*x.d,x.d*y.d);
const mul=(x,y)=>Q(x.n*y.n,x.d*y.d);
const div=(x,y)=>Q(x.n*y.d,x.d*y.n);
const abs=x=>Q(x.n<0n?-x.n:x.n,x.d);
const cmp=(x,y)=>x.n*y.d<y.n*x.d?-1:x.n*y.d>y.n*x.d?1:0;
const fmt=x=>x.d===1n?String(x.n):String(x.n)+"/"+String(x.d);
const A=[0,0,0,1,1,1],B=[2,2,3,2,2,4],C=[5,6,7,8,9,10];
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
const pairs=[[3,31],[7,27],[11,23],[15,19]];
function branch(a,b,c){let u=sub(O,a),v=mul(u,sub(O,b));return [a,mul(u,b),mul(v,c),mul(v,sub(O,c))];}
function obs(z,mask,beta){
 const raw=A.map((a,j)=>branch((mask&(1<<a))?beta:z[a],(mask&(1<<B[j]))?beta:z[B[j]],z[C[j]]));
 return M.map(row=>Array.from({length:4},(_,k)=>{
   let s=Z;for(let j=0;j<6;j++)if(row[j])s=add(s,mul(Q(row[j],20),raw[j][k]));return s;
 }));
}
function tv(p,q){let t=Z;for(let k=0;k<4;k++)t=add(t,abs(sub(p[k],q[k])));return div(t,Q(2));}
function d(z,w,pair,beta){let result=Z;for(let mask of [0,...pair]){
 const p=obs(z,mask,beta),q=obs(w,mask,beta);
 for(let i=0;i<6;i++){let t=tv(p[i],q[i]);if(cmp(t,result)>0)result=t;}
 }return result;
}
function verify(){
 const z=Array.from({length:11},(_,i)=>i<5?O:Z),w=z.slice();
 z[5]=O;w[6]=Q(19,21);
 const rows=[];
 for(let [n,den] of [[0,1],[1,4],[1,2],[3,4],[9,10],[1,1]]){
  let beta=Q(n,den),expected=div(mul(sub(O,beta),sub(O,beta)),Q(21));
  for(let pair of pairs){
   if(pair.filter(mask=>(mask&4)!==0).length!==1)throw Error("mask error");
   let value=d(z,w,pair,beta);
   if(cmp(value,expected)!==0)throw Error("bad exact result "+pair+" "+fmt(beta));
   rows.push({pair,beta:fmt(beta),value:fmt(value)});
  }
 }
 return {status:"PASS_BRC_S23_TWO_PROBE_SHARP_GLOBAL_MODULUS_20261103",
 science_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
 exact_rational_cases:rows.length,
 input_sup_distance:"1",
 witness:"first five coordinates all 1; z5=1,w5=0,z6=0,w6=19/21; other four coordinates zero",
 results:rows,
 proof_scope:"all real [0,1]^11 from symbolic lower bound plus sharp explicit witness",
 execution_scope:"24 exact BigInt-rational source-label-preserving witness evaluations",
 formal_review_or_claim:false};
}
if(typeof module!=="undefined" && require.main===module)console.log(JSON.stringify(verify(),null,2));
