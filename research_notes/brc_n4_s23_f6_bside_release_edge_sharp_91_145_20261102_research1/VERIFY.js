// BRC N=4 S23 exact continuous six-parameter-subfamily certificate.
// Frozen scientific commit 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
// Reuses decoder bank exactly as published at 57a6db1d81068504cca2b3a6ea809a63555473d6.
// Author-side: no native CLAIM or independent mathematical review.
"use strict";
const N=487200, check=(x,m)=>{if(!x)throw Error("FAIL: "+m)};
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
 [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
const A=[0,0,0,1,1,1],B=[2,2,3,2,2,4],C=[5,6,7,8,9,10],G=[0,0,1,2,2,3];
const PAIRS=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12",
 "12 13 23 24","23 34 12 13","24 34 12 14"];
const K1="2/5 0 2/5 1/5;2/5 2/5 0 1/5;3/5 0 0 2/5;2/5 2/5 0 1/5";
const K2="1/2 1/2 0 0;1/2 0 0 1/2;0 0 1/2 1/2;0 0 1/2 1/2";
const K3="3/5 2/5 0 0;2/5 2/5 1/5 0;1/3 43/105 3/35 6/35;1/7 2/35 2/5 2/5";
const names=["D1","D2","D3","D4","D6","D7","D8","K1_old","K2_old","K3_repair"];
function sc(x){const p=String(x).split("/").map(Number),v=N*p[0]/(p[1]||1);check(Number.isSafeInteger(v),"scale "+x);return v}
function mix(r){return M.map((w,i)=>[0,1,2,3].map(j=>{const s=w.reduce((v,t,k)=>v+t*r[k][j],0);check(s%20===0,"mix "+i+","+j);return s/20}))}
function decoder(r){check(r.length===4&&r.every(x=>x.length===4&&x.every(v=>Number.isSafeInteger(v)&&v>=0)&&x.reduce((a,b)=>a+b,0)===N),"stochastic rows");return mix(G.map(k=>r[k]))}
function pair(s){return decoder(s.split(" ").map(w=>[1,2,3,4].map(j=>N*[...w].filter(x=>+x===j).length/2)))}
function free(s){return decoder(s.split(";").map(w=>w.trim().split(/\s+/).map(sc)))}
const bank=[...PAIRS.map(pair),free(K1),free(K2),free(K3)];check(bank.length===10,"bank");
function prep(z){check(z.length===11&&z.every(x=>Number.isSafeInteger(x)&&x>=0&&x<=N),"policy");const r=A.map((a,i)=>{
 const x=z[a],b=z[B[i]],c=z[C[i]],mid=(N-x)*b/N,tail=(N-x)*(N-b)/N,last=tail*c/N;
 check([mid,tail,last].every(Number.isSafeInteger),"causal product");
 const row=[x,mid,last,tail-last];check(row.every(v=>v>=0)&&row.reduce((s,v)=>s+v,0)===N,"source norm");return row;
});const p=mix(r);check(p.every(r=>r.reduce((s,v)=>s+v,0)===N),"mixed norm");return p}
function risk2(p,q){let r=0;for(let i=0;i<6;i++){let s=0;for(let j=0;j<4;j++)s+=Math.abs(p[i][j]-q[i][j]);r=Math.max(r,s)}return r}
const gcd=(a,b)=>b?gcd(b,a%b):a,frac=x=>{const g=gcd(x,2*N);return x/g+"/"+(2*N/g)};
const Z=s=>prep([sc(s),sc("1/3"),sc("9/20"),0,0,N,N,0,0,0,0]);
const ss=["0","1/4","1","5/29"], risks=Object.fromEntries(ss.map(s=>[s,bank.map(q=>risk2(Z(s),q))]));
function equal(name,r,p,q){check(r*q===2*N*p,name+" got "+frac(r))}
equal("D8-0",risks["0"][6],11,20);
equal("D8-quarter",risks["1/4"][6],53,80);
equal("K1-0",risks["0"][7],4,5);
equal("K1-quarter",risks["1/4"][7],11,20);
equal("K1-1",risks["1"][7],3,5);
equal("witness",Math.min(...risks["5/29"]),91,145);
check(risks["5/29"][6]===risks["5/29"][7]&&risks["5/29"][6]===Math.min(...risks["5/29"]),"witness equality");
check(11*29+9*5===16*29-20*5,"envelope intersection");
const mid=Z("1/8"),p0=Z("0"),pq=Z("1/4");
check(mid.every((r,i)=>r.every((v,j)=>2*v===p0[i][j]+pq[i][j])),"affine midpoint");
const output={
 pass:"PASS_BRC_S23_F6_BSIDE_RELEASE_EDGE_SHARP_91_OVER_145_20261102",
 source_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
 bank_pin:"57a6db1d81068504cca2b3a6ea809a63555473d6",
 family:"Z(s)=(s,1/3,9/20,0,0;1,1,0,0,0,0), 0<=s<=1",
 exact_bank_maximum:"91/145",unique_real_maximizer:"5/29",
 excess_over_previous_F5_bank:"4/145",scale:N,tv_denominator:2*N,
 bank_labels:names,
 endpoint_vectors:Object.fromEntries(ss.map(s=>[s,risks[s].map(frac)])),
 endpoint_D8_and_K1:Object.fromEntries(ss.map(s=>[s,{D8:frac(risks[s][6]),K1:frac(risks[s][7])}])),
 s_0_to_quarter_envelope:["11/20+9*s/20","4/5-s"],
 s_quarter_to_1_cover:"K1 endpoints 11/20, 3/5; TV convexity",
 all_real_proof:"All six preparations separately affine in s; TV convexity upper-bounds each decoder by endpoint chords. The two chords meet uniquely at 5/29 and all ten actual decoder risks there are >= 91/145.",
 exact_integer_checks:true,affine_midpoint_verified:true,
 finite_prior_F5_certificate_reused_not_recomputed:true,
 independent_review:false,native_claim:false
};
if(typeof process!=="undefined"&&process.stdout)process.stdout.write(JSON.stringify(output,null,2)+"\n");
