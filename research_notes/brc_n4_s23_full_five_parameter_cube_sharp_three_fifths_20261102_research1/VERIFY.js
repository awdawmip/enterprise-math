// Exact BRC N=4 S23 five-real-parameter continuum certificate.
// Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
// Author-side research only; no native claim or independent review.
"use strict";
const N=16800000, R=6*N/5, n=10, side=n+1;
const check=(p,msg)=>{if(!p)throw Error(msg)};
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
 [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
const A=[0,0,0,1,1,1], B=[2,2,3,2,2,4], C=[5,6,7,8,9,10], G=[0,0,1,2,2,3];
const PAIRS=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12",
 "12 13 23 24","23 34 12 13","24 34 12 14"];
const K1="2/5 0 2/5 1/5;2/5 2/5 0 1/5;3/5 0 0 2/5;2/5 2/5 0 1/5";
const K2="1/2 1/2 0 0;1/2 0 0 1/2;0 0 1/2 1/2;0 0 1/2 1/2";
const K3r="3/5 2/5 0 0;2/5 2/5 1/5 0;1/3 43/105 3/35 6/35;1/7 2/35 2/5 2/5";
const names=["D1","D2","D3","D4","D6","D7","D8","K1_old","K2_old","K3_repair"];
const scale=q=>{const [a,b="1"]=String(q).split("/").map(Number);const x=N*a/b;
 check(Number.isSafeInteger(x),"not integer scaled "+q);return x};
function mix(rows){return M.map((w,i)=>[0,1,2,3].map(j=>{
 const s=w.reduce((a,t,k)=>a+t*rows[k][j],0);check(s%20===0,"source mix "+i);return s/20
}))}
function decoder(rows){check(rows.length===4 && rows.every(r=>r.length===4 &&
 r.every(v=>Number.isSafeInteger(v)&&v>=0) && r.reduce((s,v)=>s+v,0)===N),"kernel row");
 return mix(G.map(k=>rows[k]))}
const pair=s=>decoder(s.split(" ").map(w=>[1,2,3,4].map(j=>N*[...w].filter(v=>+v===j).length/2)));
const free=s=>decoder(s.split(";").map(w=>w.trim().split(/\s+/).map(scale)));
const bank=[...PAIRS.map(pair),free(K1),free(K2),free(K3r)];check(bank.length===10,"ten decoders");
function prepareScaled(z){check(z.length===11 && z.every(v=>Number.isSafeInteger(v)&&v>=0&&v<=N),"input");
 const src=A.map((a,i)=>{const x=z[a],b=z[B[i]],c=z[C[i]];
 const mid=(N-x)*b/N,tail=(N-x)*(N-b)/N,last=tail*c/N;
 check([mid,tail,last].every(Number.isSafeInteger),"source rational");return [x,mid,last,tail-last]});
 check(src.every(r=>r.every(x=>x>=0)&&r.reduce((a,x)=>a+x,0)===N),"source probability");
 return mix(src)}
const prepare=z=>prepareScaled(z.map(scale));
const risk2=(p,q)=>{let maximum=0;for(let i=0;i<6;i++){
 let value=0;for(let j=0;j<4;j++)value+=Math.abs(p[i][j]-q[i][j]);
 if(value>maximum)maximum=value}return maximum};
const minimum=p=>Math.min(...bank.map(q=>risk2(p,q)));
const raw={W:[1,0,0,0,1,0,0,0,0,0,0],J:[1,"1/3",0,0,0,0,0,0,0,1,0],
 A:["1/7",1,0,0,0,0,1,1,1,0,1],B:[1,"1/7",0,0,0,0,1,1,1,0,1],
 C:["1/7",1,0,0,0,1,0,0,0,0,0],X:[1,"1/15",0,0,0,0,1,1,1,0,1],
 Y:[1,0,0,0,0,0,0,0,1,1,1],Z:[0,1,0,1,0,1,1,0,0,0,0]};
["00000000000","00000001000","00000000001","00101000000",
 "00110000000","00101001000","00100000001","00100000000"].forEach((s,i)=>raw["T"+(i+1)]=[...s].map(Number));
raw.U=[..."00110000001"].map(Number);raw.V=[..."10000000000"].map(Number);
raw.H=["1/4",1,0,0,0,1,0,0,0,0,0];raw.Hm=["1/5",1,0,0,0,1,0,0,0,0,0];
check(Object.keys(raw).length===20,"twenty policies");
const ps=Object.fromEntries(Object.entries(raw).map(([k,z])=>[k,prepare(z)]));
const maxOld=Math.max(...Object.values(ps).map(minimum));check(maxOld===R,"old finite bound "+maxOld);
const J=t=>prepare([1,t,0,0,0,0,0,0,0,1,0]);
const jChecks=[[0,8],["2/5",8],["2/5",7],[1,7]].map(([t,k])=>({t:String(t),decoder:names[k],risk2:risk2(J(t),bank[k])}));
check(jChecks.every(z=>z.risk2<=R),"full J edge endpoints");
const W4=prepare(["1/3",0,1,"1/2",0,1,0,0,0,0,0]);
const w4PerDecoder=bank.map(q=>risk2(W4,q));check(Math.min(...w4PerDecoder)===R,"W4 exact repair");
const Td=prepare(["19/50",0,"19/50",0,0,1,0,0,0,0,0]);
const tdRisk=minimum(Td);check(tdRisk<=R,"golden diagonal rational repair");
const core=["W","X","Y","Z","T5","U","V","Hm","J(1)","J(1/5)"];
const P=core.map(k=>k==="J(1)"?J(1):k==="J(1/5)"?J("1/5"):ps[k]);
check(P.every(p=>Math.min(...bank.slice(0,7).map(q=>risk2(p,q)))>=R),"lower core fixed coverage");
let forbidden=[];
for(let a=0;a<10;a++)for(let b=a+1;b<10;b++)for(let c=b+1;c<10;c++){
 let w=Math.max(...[0,1,2,3,4,5].map(i=>[0,1,2,3].reduce((v,j)=>v+
 Math.max(P[a][i][j],P[b][i][j],P[c][i][j]),0)-N));
 if(5*w>=9*N)forbidden.push([a,b,c])
}
check(forbidden.length===84,"forbidden triple count");
let minHits=Infinity;
for(let n0=0;n0<3**10;n0++){let a=n0,labels=[];for(let i=0;i<10;i++){labels.push(a%3);a=Math.floor(a/3)}
 let hits=0;for(const [x,y,z] of forbidden)if(labels[x]===labels[y]&&labels[y]===labels[z])hits++;
 check(hits>=1,"uncovered label assignment "+n0);if(hits<minHits)minHits=hits
}
const idx=(a,b,c,d,e)=>((((a*side+b)*side+c)*side+d)*side+e);
const vertexTotal=side**5, vrisk=new Uint32Array(vertexTotal*10);
const step=N/n;
let vertexMax=0,vertexMaxAt=null;
for(let a=0;a<=n;a++)for(let b=0;b<=n;b++)for(let c=0;c<=n;c++)for(let d=0;d<=n;d++)for(let e=0;e<=n;e++){
 const z=[a*step,b*step,c*step,d*step,e*step,N,0,0,0,0,0];
 const p=prepareScaled(z),pos=10*idx(a,b,c,d,e);let mn=2*N;
 for(let k=0;k<10;k++){const r=risk2(p,bank[k]);vrisk[pos+k]=r;if(r<mn)mn=r}
 if(mn>vertexMax){vertexMax=mn;vertexMaxAt=[a,b,c,d,e]}
}
check(vertexTotal===161051 && vertexMax<=R,"all F5 vertices");
let uncovered=0,cellBestMax=0,cellBestMaxAt=null,witness="";const cellCounts=Array(10).fill(0);
const offsets=[];for(let i=0;i<=1;i++)for(let j=0;j<=1;j++)for(let k=0;k<=1;k++)for(let l=0;l<=1;l++)for(let m=0;m<=1;m++)
 offsets.push(10*idx(i,j,k,l,m));
for(let a=0;a<n;a++)for(let b=0;b<n;b++)for(let c=0;c<n;c++)for(let d=0;d<n;d++)for(let e=0;e<n;e++){
 const start=10*idx(a,b,c,d,e);let min=2*N,minIx=-1;
 for(let k=0;k<10;k++){
  let mx=0;for(const o of offsets){const r=vrisk[start+o+k];if(r>mx)mx=r}
  if(mx<min){min=mx;minIx=k}
 }
 if(min>R)uncovered++;
 if(min>cellBestMax){cellBestMax=min;cellBestMaxAt=[a,b,c,d,e]}
 check(minIx>=0,"no decoder selection");cellCounts[minIx]++;witness+=String(minIx)
}
check(uncovered===0 && witness.length===100000,"F5 cube certificate");
const center=prepare(["1/20","1/20","1/20","1/20","1/20",1,0,0,0,0,0]);
let sum=Array.from({length:6},()=>Array(4).fill(0));
for(let a=0;a<2;a++)for(let b=0;b<2;b++)for(let c=0;c<2;c++)for(let d=0;d<2;d++)for(let e=0;e<2;e++){
 const p=prepareScaled([a*step,b*step,c*step,d*step,e*step,N,0,0,0,0,0]);
 for(let i=0;i<6;i++)for(let j=0;j<4;j++)sum[i][j]+=p[i][j]
}
check(center.every((row,i)=>row.every((v,j)=>32*v===sum[i][j])),"F5 tensor midpoint identity");
const gcd=(a,b)=>b?gcd(b,a%b):a;
const frac=r=>{const g=gcd(r,2*N);return (r/g)+"/"+(2*N/g)};
const result={
 pass:"PASS_BRC_N4_S23_FIVE_PARAMETER_REAL_CUBE_SHARP_THREE_FIFTHS_20261102",
 source_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
 claim:"Seven fixed kernels plus three free stochastic kernels: sharp 3/5 over S18, all real J(t), all real F5(s,t,u,v,w)",
 F5:"(s,t,u,v,w;1,0,0,0,0,0)",
 scale:N,tv_denominator:2*N,decoder_names:names,free_kernel_rows:[K1,K2,K3r],
 new_step:"Replace ONLY previous three-parameter-bank K3 with K3r from prior W4 repair; retain old K1 and K2",
 old_policies:20,old_policies_max_min_risk:frac(maxOld),
 J_endpoint_proofs:jChecks.map(x=>({...x,risk:frac(x.risk2)})),
 W4_minimum:frac(Math.min(...w4PerDecoder)),W4_per_decoder_risk2:w4PerDecoder,
 golden_diagonal_rational_T19over50_risk:frac(tdRisk),
 lower_core:core,lower_forbidden_triples:forbidden.length,label_assignments_checked:3**10,
 minimum_monochromatic_hits:minHits,
 five_cube:{grid_denominator:n,real_dimension:5,vertices:vertexTotal,cells:100000,vertices_per_cell:32,
 maximum_vertex_min_risk:frac(vertexMax),maximum_vertex_min_risk_grid_point:vertexMaxAt,
 maximum_common_decoder_corner_risk:frac(cellBestMax),worst_cell_index:cellBestMaxAt,
 selected_decoder_counts:Object.fromEntries(names.map((name,i)=>[name,cellCounts[i]])),
 decoder_index_witness_100000_cells:witness,
 proof_bridge:"Separate affine dependence in all five parameters; each p(z) is a shared 32-corner convex combination on each closed cell; TV convexity with the SAME decoder closes real interior."},
 independent_review:false,native_claim:false
};
console.log(JSON.stringify(result));
