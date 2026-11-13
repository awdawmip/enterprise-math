// Exact BRC N=4 S23 bank-risk certificates on two B-side continuous faces.
// Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
// Fixed ten-decoder bank: 57a6db1d81068504cca2b3a6ea809a63555473d6.
// Author-side computation; no native CLAIM or independent review.
"use strict";
const N=6090000, check=(ok,msg)=>{if(!ok)throw Error("FAIL "+msg)};
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
 [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
const A=[0,0,0,1,1,1],B=[2,2,3,2,2,4],C=[5,6,7,8,9,10],G=[0,0,1,2,2,3];
const PAIRS=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12",
 "12 13 23 24","23 34 12 13","24 34 12 14"];
const K1="2/5 0 2/5 1/5;2/5 2/5 0 1/5;3/5 0 0 2/5;2/5 2/5 0 1/5";
const K2="1/2 1/2 0 0;1/2 0 0 1/2;0 0 1/2 1/2;0 0 1/2 1/2";
const K3="3/5 2/5 0 0;2/5 2/5 1/5 0;1/3 43/105 3/35 6/35;1/7 2/35 2/5 2/5";
const labels=["D1","D2","D3","D4","D6","D7","D8","K1_old","K2_old","K3_repair"];
const scale=q=>{const [p,d="1"]=String(q).split("/").map(Number),v=N*p/d;
 check(Number.isSafeInteger(v),"scale "+q);return v};
function mix(rows){return M.map((w,i)=>[0,1,2,3].map(j=>{
 const a=w.reduce((sum,c,k)=>sum+c*rows[k][j],0);
 check(a%20===0,"mix division "+i+","+j);return a/20;
}))}
function decoder(rows){check(rows.length===4 && rows.every(r=>r.length===4 &&
 r.every(v=>Number.isSafeInteger(v)&&v>=0)&&r.reduce((s,x)=>s+x,0)===N),"decoder stochastic");
 return mix(G.map(k=>rows[k]));}
const pair=s=>decoder(s.split(" ").map(w=>[1,2,3,4].map(j=>N*[...w].filter(v=>+v===j).length/2)));
const free=s=>decoder(s.split(";").map(w=>w.trim().split(/\s+/).map(scale)));
const bank=[...PAIRS.map(pair),free(K1),free(K2),free(K3)];check(bank.length===10,"bank");
function prepare(z){check(z.length===11 && z.every(v=>Number.isSafeInteger(v)&&v>=0&&v<=N),"policy");
 const src=A.map((a,i)=>{const x=z[a],b=z[B[i]],c=z[C[i]],mid=(N-x)*b/N,
 tail=(N-x)*(N-b)/N,last=tail*c/N;
 check([mid,tail,last].every(Number.isSafeInteger),"causal product "+i);
 const row=[x,mid,last,tail-last];check(row.every(v=>v>=0)&&row.reduce((s,v)=>s+v,0)===N,"source normalization");return row;
 });const P=mix(src);check(P.every(r=>r.reduce((s,v)=>s+v,0)===N),"observed normalization");return P;}
function risk2(P,Q){let mx=0;for(let i=0;i<6;i++){
 let t=0;for(let j=0;j<4;j++)t+=Math.abs(P[i][j]-Q[i][j]);
 if(t>mx)mx=t;
}return mx;}
const gcd=(a,b)=>b?gcd(b,a%b):a;
const frac=x=>{const d=gcd(x,2*N);return x/d+"/"+(2*N/d)};
const sixAxisNames=["s=z0","h=z6","k=z7","l=z8","r=z9","m=z10"];
const sAxis=["0","5/29","1/5","2/5","3/5","4/5","1"].map(scale);
const side=["0","1/5","2/5","3/5","4/5","1"].map(scale);
const dims=[sAxis.length,6,6,6,6,6],strides=[7776,1296,216,36,6,1];
const total=dims.reduce((a,b)=>a*b,1),R=new Uint32Array(total*10);
function vi(v){return v.reduce((x,a,i)=>x+a*strides[i],0)}
function policy(v){const z=[sAxis[v[0]],scale("1/3"),scale("9/20"),0,0,N,
 side[v[1]],side[v[2]],side[v[3]],side[v[4]],side[v[5]]];return prepare(z)}
for(let a=0;a<7;a++)for(let b=0;b<6;b++)for(let c=0;c<6;c++)
for(let d=0;d<6;d++)for(let e=0;e<6;e++)for(let f=0;f<6;f++){
 const v=[a,b,c,d,e,f],p=policy(v),at=10*vi(v);
 for(let k=0;k<10;k++)R[at+k]=risk2(p,bank[k]);
}
const witness6=[2,5,0,1,5,0], witness5=[1,5,0,0,0,0];
const r6=Array.from({length:10},(_,k)=>R[10*vi(witness6)+k]);
const r5=Array.from({length:10},(_,k)=>R[10*vi(witness5)+k]);
const peak6=2*N*19/30,peak5=2*N*91/145;
check(Number.isInteger(peak6)&&Number.isInteger(peak5),"exact threshold");
check(Math.min(...r6)===peak6,"six-dimensional lower witness");
check(Math.min(...r5)===peak5,"five-dimensional lower witness");
function certificate(selectedAxes,limit){
 const cells=selectedAxes.map(i=>dims[i]-1),corners=2**selectedAxes.length;
 const strides0=selectedAxes.map(i=>strides[i]),offset=[];
 for(let bits=0;bits<corners;bits++){
  let off=0;for(let j=0;j<selectedAxes.length;j++)if((bits>>j)&1)off+=strides0[j];
  offset.push(10*off);
 }
 let totalCells=1;for(let c of cells)totalCells*=c;
 let max=0,maxCell=null,uncovered=0,choice="",counts=Array(10).fill(0);
 for(let linear=0;linear<totalCells;linear++){
  let v=linear,base=0;const cell=Array(cells.length);
  for(let j=cells.length-1;j>=0;j--){cell[j]=v%cells[j];v=Math.floor(v/cells[j]);base+=cell[j]*strides0[j]*10;}
  let best=2*N+1,bestK=-1;
  for(let k=0;k<10;k++){
   let worst=0;for(const off of offset){const q=R[base+off+k];if(q>worst)worst=q;}
   if(worst<best){best=worst;bestK=k;}
  }
  if(best>limit)uncovered++;
  if(best>max){max=best;maxCell=cell;}
  counts[bestK]++;choice+=String(bestK);
 }
 check(uncovered===0,"common decoder cell coverage "+selectedAxes+" misses "+uncovered);
 check(max===limit,"sharp cell bound "+selectedAxes+" got "+frac(max));
 return {parameter_indices:selectedAxes.map(i=>sixAxisNames[i]),grid_s:sAxis.map(v=>frac(2*v)),
 grid_other:side.map(v=>frac(2*v)),vertex_count:selectedAxes.reduce((a,i)=>a*dims[i],1),
 cell_count:totalCells,corners_per_cell:corners,maximum_common_decoder_corner_risk:frac(max),
 lexicographically_first_sharp_cell:maxCell,decoder_counts:Object.fromEntries(labels.map((l,i)=>[l,counts[i]])),
 chosen_decoder_index_per_cell_lexicographic:choice};
}
const five=certificate([0,1,2,3,5],peak5); // freeze z9 = 0
const six=certificate([0,1,2,3,4,5],peak6);
const result={pass:"PASS_BRC_S23_BSIDE_FIVE_AND_SIX_REAL_CUBES_EXACT_20261102",
 source_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",bank_pin:"57a6db1d81068504cca2b3a6ea809a63555473d6",
 model:"original six separately labeled sources; R_i=(x,(1-x)b,(1-x)(1-b)c,(1-x)(1-b)(1-c)); P=M R/20; G=(0,0,1,2,2,3)",
 fixed_bank:labels,integer_scale:N,tv_denominator:2*N,
 family6:"(s,1/3,9/20,0,0;1,h,k,l,r,m), all s,h,k,l,r,m in [0,1]",
 family5:"same but r=0; all s,h,k,l,m in [0,1]",
 sharp_six_real_value:"19/30",sharp_six_witness:"(s,h,k,l,r,m)=(1/5,1,0,1/5,1,0)",six_witness_decoder_risks:r6.map(frac),
 sharp_five_real_value:"91/145",sharp_five_witness:"(s,h,k,l,r,m)=(5/29,1,0,0,0,0)",five_witness_decoder_risks:r5.map(frac),
 separate_multiaffinity_and_tv_convexity:"Each entire six-row positive source mixture is a common tensor-product convex combination of the 2^d corners of each cell; each selected decoder is constant on the cell.",
 five_dimensional_certificate:five,six_dimensional_certificate:six,
 native_claim:false,independent_review:false};
console.log(JSON.stringify(result));
