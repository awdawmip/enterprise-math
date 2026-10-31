"use strict";
// Finite, exact-integer audit; no floating point and no hidden random sampling.
// Public channel: (Decision, BU sensor Z), with stop time erased.
const raw = {
 Q:{AU:[10,10],AV:[20,20],BU:[15,15],BV:[15,15]},
 P:{AU:[9,11],AV:[5,5],BU:[3,27],BV:[30,30]}
};
const prepared = [
 {S:"AU",B:"Q",w:[10,10]}, {S:"AU",B:"P",w:[9,11]},
 {S:"AV",B:"Q",w:[10,10]}, {S:"AV",B:"P",w:[10,10]},
 {S:"BU",B:"Q",w:[10,10]}, {S:"BU",B:"P",w:[2,18]},
 {S:"BV",B:"Q",w:[10,10]}, {S:"BV",B:"P",w:[10,10]}
];
const classes={AU:[0,1],AV:[2,2],BU:[3,4],BV:[5,5]};
const fL={AU:[19,21],AV:[20,20],BU:[0,0],BV:[0,0]};
const fR={AU:[0,0],AV:[0,0],BU:[8,32],BV:[20,20]};
function check(x,msg){if(!x)throw Error(msg);}
function zero(){return [0,0,0,0,0,0];}
function addWeighted(out,v,n){for(let i=0;i<6;i++)out[i]+=n*v[i];}
function sum(x){return x.reduce((a,b)=>a+b,0);}
function absDistance(x,y){let a=0;for(let i=0;i<6;i++)a+=Math.abs(x[i]-y[i]);return a;}
for (const b of ["P","Q"]) {
 let mass=0, count=0;
 for(const s of ["AU","AV","BU","BV"])for(let j=0;j<2;j++)for(let k=0;k<2;k++){
  const x=raw[b][s][j];check(x>0,"nonpositive leaf");mass+=x;count++;
 }
 check(mass===240 && count===16,"16-leaf normalization");
}
for(const x of prepared){
 check(sum(x.w)===20,"prepared row mass");
 let reference=(x.S==="AU"||x.S==="AV")?fL:fR;
 let overlap=0;
 for(let j=0;j<2;j++)overlap+=Math.min(reference[x.S][j],4*x.w[j]);
 check(overlap===40,"two-code source overlap != 1/2");
 if(x.S==="BU")for(let j=0;j<2;j++){
  check([4,16][j]<=3*x.w[j],"BU one-third source domination");
 }
}
// Six public atoms: (P,bottom),(Q,bottom),(P,0),(P,1),(Q,0),(Q,1).
function kernel(s,j,second,mask,eps8){
 const out=zero();
 const action=(s==="AU"||s==="BU")?second%3:(s==="AV"?Math.floor(second/3)%3:Math.floor(second/9)%3);
 if(action!==0){out[action===1?0:1]=8;return out;}
 const d=(mask>>classes[s][j])&1; // 0=P,1=Q
 if(s!=="BU"){out[d]=8;return out;}
 const z0=(j===0)?8-eps8:eps8;
 out[d===0?2:4]=z0;
 out[d===0?3:5]=8-z0;
 return out;
}
const Hstar=6, HstarMask=32; // AU,BU continue; AV time-2 stop Q; BV continue and time-3 Q.
for(const eps8 of [0,1,2,4]){
 const au=kernel("AU",0,Hstar,HstarMask,eps8);
 const av=kernel("AV",0,Hstar,HstarMask,eps8);
 const bu=kernel("BU",0,Hstar,HstarMask,eps8);
 check(au[0]===8 && av[1]===8 && bu[0]===0 && bu[1]===0 && bu[2]+bu[3]===8,
       "H* three disjoint public support sets");
}
let comparisons=0, max1=0, max2=0;
const epsValues=[0,1,2,4];
for(const eps8 of epsValues)for(let second=0;second<27;second++)for(let mask=0;mask<64;mask++){
 const ker={};
 for(const s of ["AU","AV","BU","BV"])ker[s]=[
  kernel(s,0,second,mask,eps8), kernel(s,1,second,mask,eps8)
 ];
 // One-code decoder r_H: [delta(P,bottom)+delta(Q,bottom)+H#nu_BU]/3,
 // where nu_BU(J=0,1)=(4,16)/20. Numerator on denominator 480.
 const r1=[160,160,0,0,0,0];
 addWeighted(r1,ker.BU[0],4);
 addWeighted(r1,ker.BU[1],16);
 check(sum(r1)===480,"one-code decoder not normalized");
 const r2L=zero(),r2R=zero();
 for(const s of ["AU","AV","BU","BV"])for(let j=0;j<2;j++){
  addWeighted(r2L,ker[s][j],fL[s][j]);
  addWeighted(r2R,ker[s][j],fR[s][j]);
 }
 check(sum(r2L)===640 && sum(r2R)===640,"two-code decoder not normalized");
 for(const x of prepared){
  const true160=zero();
  for(let j=0;j<2;j++)addWeighted(true160,ker[x.S][j],x.w[j]);
  check(sum(true160)===160,"prepared public output not normalized");
  // Scale actual /160, one /480, two /640 to common denominator 1920.
  const truth=true160.map(v=>12*v);
  const one=r1.map(v=>4*v);
  const two=(x.S==="AU"||x.S==="AV"?r2L:r2R).map(v=>3*v);
  const a1=absDistance(truth,one),a2=absDistance(truth,two);
  // TV = sum(abs)/3840. Thresholds 2/3 and 1/2 are 2560 and 1920.
  check(a1<=2560,"one-code bound violated");
  check(a2<=1920,"two-code bound violated");
  if(a1>max1)max1=a1;
  if(a2>max2)max2=a2;
  comparisons+=2;
 }
}
check(comparisons===110592,"comparison count");
check(max1===2560 && max2===1920,"sharpness witness not attained");
const report={
 status:"PASS_BRC_N4_NO_TIME_KEEP_Z_ALL_LAWFUL_R1_R2_20261031",
 exact_arithmetic:"integer on common output denominator 1920",
 model:"two laws, each 16 strictly positive leaves; eight prepared inputs",
 tested_subfamily:"27 time-2 deterministic action patterns x 64 lawful time-3 class decisions",
 policies_per_error:1728, epsilon_values:["0","1/8","1/4","1/2"],
 inputs_per_policy:8, public_output_atoms:6,
 comparisons, max_one_code_tv:"2/3", max_two_code_tv:"1/2",
 scope:"finite deterministic S23 subfamily; continuous eps and all stochastic S23/S2 proved analytically"
};
if(typeof console!=="undefined"&&typeof console.log==="function")console.log(JSON.stringify(report));
