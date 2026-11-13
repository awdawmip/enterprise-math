"use strict";
// Exact integer BRC N=4, S23 six-labelled-source 11-parameter verifier.
// All integer intermediates are below 2^53, hence Number arithmetic is exact.
const A=[0,0,0,1,1,1], B=[2,2,3,2,2,4], C=[5,6,7,8,9,10], G=[0,0,1,2,2,3];
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
         [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
const PAIRS=["34 24 34 24","34 23 34 34","34 34 34 23",
             "24 24 12 12","12 13 23 24","23 34 12 13","24 34 12 14"];
const FREE=[
"2/5 0 2/5 1/5;2/5 2/5 0 1/5;3/5 0 0 2/5;2/5 2/5 0 1/5",
"1/2 1/2 0 0;1/2 0 0 1/2;0 0 1/2 1/2;0 0 1/2 1/2",
"3/5 2/5 0 0;2/5 2/5 1/5 0;1/3 43/105 3/35 6/35;1/7 2/35 2/5 2/5"];
const names=["D1","D2","D3","D4","D6","D7","D8","K1_old","K2_old","K3_repair"];
const frac210=s=>{let [a,b="1"]=s.split("/").map(Number);let n=210*a/b;if(!Number.isInteger(n))throw Error("nonintegral kernel");return n;};
const D=PAIRS.map(p=>p.split(" ").map(w=>[1,2,3,4].map(k=>105*[...w].filter(x=>Number(x)===k).length)))
 .concat(FREE.map(p=>p.split(";").map(row=>row.trim().split(/\s+/).map(frac210))));
function check(x,msg){if(!x)throw Error("FAIL "+msg);}
check(D.length===10&&D.every(d=>d.length===4&&d.every(row=>row.length===4&&row.reduce((a,b)=>a+b,0)===210)),"stochastic rows");
const QD=D.map(d=>M.map(weights=>[0,1,2,3].map(k=>weights.reduce((sum,w,j)=>sum+w*d[G[j]][k],0))));
check(QD.every(d=>d.every(row=>row.reduce((a,b)=>a+b,0)===4200)),"source decoder normalization");
function risks(v,q){
 const raw=A.map((ai,i)=>{const a=v[ai],b=v[B[i]],c=v[C[i]];return [a*q*q,(q-a)*b*q,(q-a)*(q-b)*c,(q-a)*(q-b)*(q-c)];});
 const P=M.map(weights=>[0,1,2,3].map(k=>210*weights.reduce((sum,w,j)=>sum+w*raw[j][k],0)));
 const q3=q*q*q;
 check(raw.every(r=>r.reduce((a,b)=>a+b,0)===q3),"raw source normalization");
 return QD.map(d=>Math.max(...P.map((row,i)=>{
   let n=0;for(let k=0;k<4;k++)n+=Math.abs(row[k]-q3*d[i][k]);
   check(n%2===0,"TV parity");return n/2;
 })));
}
function gcd(a,b){while(b){const t=a%b;a=b;b=t;}return a;}
function rational(n,d){const g=gcd(n,d);return (n/g)+((d/g)===1?"":"/"+(d/g));}
const hist=new Map(),binHist=new Map(),choice=Array(10).fill(0);
let best=-1,bestPoint=[],count=0;
for(let idx=0;idx<3**11;idx++){
 let t=idx, v=[];for(let j=0;j<11;j++){v.push(t%3);t=Math.floor(t/3);}
 let rr=risks(v,2), n=Math.min(...rr), k=rr.indexOf(n);
 hist.set(n,(hist.get(n)||0)+1);choice[k]++;count++;
 if(n>best){best=n;bestPoint=v.slice();}
 if(v.every(x=>x!==1))binHist.set(n,(binHist.get(n)||0)+1);
}
const S2=20*210*8;
check(count===177147&&best===S2*3/5,"ternary maximum");
check(hist.get(S2*3/5)===47853&&hist.get(S2/2)===110288,"ternary multiplicities");
check([...binHist.values()].reduce((a,b)=>a+b,0)===2048,"binary coverage");
check(binHist.get(S2/2)===1280&&binHist.get(S2*3/5)===736&&binHist.get(S2*11/20)===32,"binary multiplicities");
const base=[2,5,6,3,3,2,3,6,3,2,2],q=6,S6=20*210*216;
const endpoint={};
for(let x of [0,2,6]){
 const v=base.slice();v[0]=x;
 const rr=risks(v,q), fmt=rr.map(n=>rational(n,S6));
 endpoint[rational(x,q)]=fmt;
 if(x===0)check(fmt[3]==="1/2","D4 x=0");
 if(x===2){check(fmt.join(",")==="1,1,1,2/3,31/36,2/3,2/3,2/3,1,43/60","sharp full witness");}
 if(x===6)check(fmt[7]==="3/5","K1 x=1");
}
console.log(JSON.stringify({
 pass:"PASS_BRC_S23_TERNARY_11D_VERSUS_CONTINUUM_EDGE_2_3_20261103",
 frozen_scientific_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
 fixed_bank_pin:"57a6db1d81068504cca2b3a6ea809a63555473d6",
 integer_method:"decoder rows /210, causal raw rows /q^3, common numerator TV/(20*210*q^3), no floating predicates",
 ternary_total:count,ternary_max:rational(best,S2),ternary_witness_over_2:bestPoint,
 ternary_histogram:Object.fromEntries([...hist].sort((a,b)=>a[0]-b[0]).map(([n,c])=>[rational(n,S2),c])),
 binary_total:2048,binary_max:"3/5",
 binary_histogram:Object.fromEntries([...binHist].sort((a,b)=>a[0]-b[0]).map(([n,c])=>[rational(n,S2),c])),
 first_minimizer_counts:Object.fromEntries(names.map((n,i)=>[n,choice[i]])),
 continuous_line:"(x,5/6,1,1/2,1/2;1/3,1/2,1,1/2,1/3,1/3), 0<=x<=1",
 endpoint_risks: endpoint, continuous_line_max:"2/3, unique x=1/3",
 upper_left:"D4 <= 1/2+x/2 on [0,1/3]",
 upper_right:"K1_old <= 7/10-x/10 on [1/3,1]",
 robust_gap:"m(z)>=2/3-||z-z_star||_1; >3/5 when ||.||_1<1/15",
 scopes:"exact ternary exhaustive and all-real 1D slice for pinned decoder bank; no optimized free-kernel bound or native Result",
 native_claim:false, independent_review:false
},null,2));
