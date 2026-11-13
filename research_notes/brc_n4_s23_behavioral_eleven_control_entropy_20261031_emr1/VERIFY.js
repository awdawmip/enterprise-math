"use strict";
const K=[
[10,10,0,0,0,0],
[9,11,0,0,0,0],
[0,0,20,0,0,0],
[0,0,0,10,10,0],
[0,0,0,2,18,0],
[0,0,0,0,0,20]
];
const inv4=[
[44,-40,0,0,0,0],
[-36,40,0,0,0,0],
[0,0,4,0,0,0],
[0,0,0,9,-5,0],
[0,0,0,-1,5,0],
[0,0,0,0,0,4]
];
const first=[0,0,0,1,1,1], second=[0,0,1,0,0,2];
const assert=(x,msg)=>{if(!x)throw Error(msg)};
for(let x=0;x<6;x++)for(let y=0;y<6;y++){
 const s=inv4[x].reduce((z,w,j)=>z+w*K[j][y],0);
 assert(s===(x===y?80:0),"inverse mismatch "+x+","+y);
}
const norm=Math.max(...inv4.map(row=>row.reduce((s,x)=>s+Math.abs(x),0)))/4;
assert(norm===21,"inverse infinity norm");
const prepared=new Array(2048);
const columns=[];
for(let mask=0;mask<2048;mask++){
 const theta=Array.from({length:11},(_,j)=>1+((mask>>j)&1));
 const latent=first.map((g,x)=>{
  const a=theta[g], b=theta[2+second[x]], c=theta[5+x];
  const p=[16*a,4*(4-a)*b,(4-a)*(4-b)*c,(4-a)*(4-b)*(4-c)];
  assert(p.reduce((a,b)=>a+b,0)===64,"terminal normalization");
  assert(p[0]===16*a && p[1]===4*(4-a)*b && p[2]===(4-a)*(4-b)*c,"triangular inverse");
  return p;
 });
 const p=K.map(row=>[0,1,2,3].map(t=>row.reduce((s,w,x)=>s+w*latent[x][t],0)));
 for(let i=0;i<6;i++)assert(p[i].reduce((a,b)=>a+b,0)===1280,"prepared normalization");
 for(let x=0;x<6;x++)for(let t=0;t<4;t++)
  assert(inv4[x].reduce((s,w,i)=>s+w*p[i][t],0)===80*latent[x][t],"source recovery");
 prepared[mask]=p.flatMap(row=>row.slice(0,3));
 if(mask>0 && (mask & (mask-1))===0)columns.push(prepared[mask].map((v,j)=>v-prepared[0][j]));
}
assert(columns.length===11,"one-step columns");
const modulus=65521;
const mod=x=>((x%modulus)+modulus)%modulus;
const pow=(a,n)=>{let z=1;for(;n>0;n=Math.floor(n/2),a=mod(a*a))if(n%2)z=mod(z*a);return z};
const A=Array.from({length:18},(_,i)=>columns.map(col=>mod(col[i])));
let rank=0;
for(let c=0;c<11;c++){
 let pivot=rank;while(pivot<18&&A[pivot][c]===0)pivot++;
 assert(pivot<18,"rank deficiency at "+c);
 [A[pivot],A[rank]]=[A[rank],A[pivot]];
 const inv=pow(A[rank][c],modulus-2);
 for(let j=c;j<11;j++)A[rank][j]=mod(A[rank][j]*inv);
 for(let i=rank+1;i<18;i++){
  const f=A[i][c];
  for(let j=c;j<11;j++)A[i][j]=mod(A[i][j]-f*A[rank][j]);
 }
 rank++;
}
assert(rank===11,"11d chart tangent rank");
const seen=new Set(prepared.map(row=>row.join(",")));
assert(seen.size===2048,"parameterized preparations not injective on grid");
for(let t=0;t<1024;t++){
 const i=(53*t+17)%2048, j=(97*t+313)%2048;
 const diff=Math.max(...prepared[i].map((v,p)=>Math.abs(v-prepared[j][p])));
 const a=((i^j)!==0)?1:0;
 assert(320*a<=168*diff,"Lipschitz consistency");
}
const report=[
"PASS_BRC_N4_S23_BEHAVIORAL_11D_ENTROPY_20261031",
"matrix_inverse_scaled4=OK",
"matrix_inverse_infinity_norm=21",
"two_level_randomized_parameter_vectors=2048",
"distinct_prepared_time_laws=2048",
"exact_mixture_inversions=49152",
"rank_mod_65521=11",
"lipschitz_pair_checks=1024",
"arbitrary_real_parameter_theorem=ANALYTIC_ONLY",
"native_P000_and_independent_review=NOT_CLAIMED"
].join("\n");
if(typeof console!=="undefined")console.log(report);
report;
