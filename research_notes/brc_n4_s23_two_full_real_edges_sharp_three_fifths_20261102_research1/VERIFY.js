// Exact BRC S23 certificate. Scientific source pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34
function verify(){
"use strict";
const N=50400,R3=6*N/5,R7=7*N/6;
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]], A=[0,0,0,1,1,1],B=[2,2,3,2,2,4],C=[5,6,7,8,9,10],G=[0,0,1,2,2,3];
const PAIRS=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12","12 12 24 34","12 13 23 24","23 34 12 13","24 34 12 14"];
const K1="2/5 0 3/5 0;2/5 2/5 0 1/5;2/5 0 0 3/5;3/5 2/5 0 0";
const K2="1/2 1/2 0 0;1/2 0 0 1/2;0 0 1/2 1/2;0 0 1/2 1/2";
const K3="0 1/2 1/2 0;0 1 0 0;0 1 0 0;0 0 1/2 1/2";
const assert=(v,s)=>{if(!v)throw Error(s)};
const val=s=>{let [a,b="1"]=String(s).split("/").map(Number),x=N*a/b;assert(Number.isSafeInteger(x),"fraction "+s);return x};
const mix=rows=>M.map((m,i)=>[0,1,2,3].map(j=>{let v=m.reduce((s,w,k)=>s+w*rows[k][j],0);assert(v%20===0,"mix "+i);return v/20}));
const kernel=rows=>{assert(rows.length===4&&rows.every(r=>r.length===4&&r.every(x=>x>=0)&&r.reduce((a,b)=>a+b,0)===N),"kernel");return mix(G.map(g=>rows[g]))};
const pair=s=>kernel(s.split(" ").map(t=>[1,2,3,4].map(j=>N*[...t].filter(x=>Number(x)===j).length/2)));
const free=s=>kernel(s.split(";").map(row=>row.trim().split(/\s+/).map(val)));
const fixed=PAIRS.filter((_,i)=>i!==4).map(pair),frees=[K1,K2,K3].map(free),bank=[...fixed,...frees];
function prepare(z){
z=z.map(val);assert(z.length===11&&z.every(v=>v>=0&&v<=N),"strategy");
return mix(A.map((a,i)=>{const x=z[a],b=z[B[i]],c=z[C[i]],tail=(N-x)*(N-b)/N,mid=(N-x)*b/N,last=tail*c/N;assert([tail,mid,last].every(Number.isSafeInteger),"causal");return [x,mid,last,tail-last]}));
}
const risk=(p,q)=>Math.max(...p.map((row,i)=>row.reduce((s,x,j)=>s+Math.abs(x-q[i][j]),0)));
const O=(s,t)=>[s,t,0,0,0,0,1,1,1,0,1], Zt=(s,t)=>[s,t,0,0,0,1,0,0,0,0,0],J=t=>prepare([1,t,0,0,0,0,0,0,0,1,0]);
const raw={W:[1,0,0,0,1,0,0,0,0,0,0],J:[1,"1/3",0,0,0,0,0,0,0,1,0],A:O("1/7",1),B:O(1,"1/7"),C:Zt("1/7",1),X:O(1,"1/15"),Y:[1,0,0,0,0,0,0,0,1,1,1],Z:[0,1,0,1,0,1,1,0,0,0,0]};
["00000000000","00000001000","00000000001","00101000000","00110000000","00101001000","00100000001","00100000000"].forEach((v,i)=>raw["T"+(i+1)]=[...v].map(Number));
raw.U=[..."00110000001"].map(Number);raw.V=[..."10000000000"].map(Number);raw.H=["1/4",1,0,0,0,1,0,0,0,0,0];raw.Hm=["1/5",1,0,0,0,1,0,0,0,0,0];
const pol=Object.fromEntries(Object.entries(raw).map(([n,z])=>[n,prepare(z)]));
assert(Object.keys(pol).length===20,"20 policies");
const minBank=Object.fromEntries(Object.entries(pol).map(([n,p])=>[n,Math.min(...bank.map(q=>risk(p,q)))]));
assert(Math.max(...Object.values(minBank))===R3&&Object.keys(minBank).length===20,"full-edge finite upper");
const H=s=>prepare([s,1,0,0,0,1,0,0,0,0,0]);
const ends={K2_J0:risk(J(0),frees[1]),K2_J2_5:risk(J("2/5"),frees[1]),K1_J2_5:risk(J("2/5"),frees[0]),K1_J1:risk(J(1),frees[0]),D4_H0:risk(H(0),fixed[3]),D4_H1_5:risk(H("1/5"),fixed[3]),K1_H1_5:risk(H("1/5"),frees[0]),K1_H1:risk(H(1),frees[0])};
assert(ends.K2_J0===N&&ends.K2_J2_5===N&&ends.K1_J2_5===R3&&ends.K1_J1===R3&&ends.D4_H0===N&&ends.D4_H1_5===R3&&ends.K1_H1_5===R3&&ends.K1_H1===R3,"J and H full-edge endpoints");
for(let k=0;k<=6;k++){
 assert(J(k+"/6").every((row,i)=>row.every((x,j)=>6*x===(6-k)*J(0)[i][j]+k*J(1)[i][j])),"affine J");
 assert(H(k+"/6").every((row,i)=>row.every((x,j)=>6*x===(6-k)*H(0)[i][j]+k*H(1)[i][j])),"affine H");
}
const core=["W","X","Y","Z","T5","U","V","Hm","J1","Jp"],P=core.map(n=>n==="J1"?J(1):n==="Jp"?J("1/5"):pol[n]);
const fixedMin=P.map(p=>Math.min(...fixed.map(q=>risk(p,q))));
assert(fixedMin.every(v=>v>=R3)&&Math.min(...fixedMin)===R3,"all ten need free below 3/5");
const forbidden=[];
for(let a=0;a<10;a++)for(let b=a+1;b<10;b++)for(let c=b+1;c<10;c++){
 const best=Math.max(...[0,1,2,3,4,5].map(i=>[0,1,2,3].reduce((s,j)=>s+Math.max(P[a][i][j],P[b][i][j],P[c][i][j]),0)-N));
 if(5*best>=9*N)forbidden.push([a,b,c]);
}
assert(forbidden.length===84,"84 exact forbidden triples");
let minimum=Infinity;
for(let n=0;n<3**10;n++){
 let x=n,lab=[];
 for(let i=0;i<10;i++){lab.push(x%3);x=Math.floor(x/3)}
 let hits=forbidden.reduce((v,[a,b,c])=>v+(lab[a]===lab[b]&&lab[b]===lab[c]?1:0),0);
 assert(hits>=1,"countercoloring "+n);minimum=Math.min(minimum,hits);
}
assert(minimum===1,"minimum monochromatic hits");
const gcd=(a,b)=>b?gcd(b,a%b):a,frac=x=>{let d=gcd(x,2*N);return x/d+"/"+(2*N/d)};
return{pass:"PASS_BRC_N4_S23_TWO_FULL_REAL_EDGES_SHARP_3_5_20261102",
scientific_source_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
probability_scale:N,total_variation_denominator:2*N,original_six_sources:["AU0","AU1","AV","BU0","BU1","BV"],shared_parameter:"b_U",
seven_fixed:["D1","D2","D3","D4","D6","D7","D8"],free_kernels:{K1,K2,K3},
twenty_discrete_min_risks:Object.fromEntries(Object.entries(minBank).map(([n,v])=>[n,frac(v)])),
twenty_discrete_max:frac(Math.max(...Object.values(minBank))),
two_continua_endpoints:Object.fromEntries(Object.entries(ends).map(([n,v])=>[n,frac(v)])),
analytic_two_edge_coverage:"K2 on [0,1/3], K1 on [1/3,1] by affine sources and TV convexity",
lower_core:core,lower_fixed_minima:Object.fromEntries(core.map((n,i)=>[n,frac(fixedMin[i])])),
triple_combinations:120,forbidden_triple_count:forbidden.length,three_label_assignments:3**10,min_forbidden_monochromatic_hits:minimum,
sharp_optimum:"3/5",prior_single_H_optimum:"7/12",increment:"1/60",status:"author exact computation; unreviewed/not admitted"};
}
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(verify(),null,2));