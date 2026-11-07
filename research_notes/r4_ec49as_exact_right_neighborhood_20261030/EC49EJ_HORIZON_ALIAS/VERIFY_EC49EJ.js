#!/usr/bin/env node
"use strict";
const verify=function verify(){
 const OP={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
 const S=[["N",0],["N",1],["N",2],["A",0],["A",2],["B",0],["B",1],["AB",0],["BA",0]],B=["N","A","B","AB","BA"];
 const path=w=>[...w].flatMap(k=>OP[k]);
 const positive=z=>Array.from({length:6},(_,i)=>z.filter(k=>k===i+1).length);
 const displacement=z=>Array.from({length:6},(_,i)=>z.filter(k=>k===i+1).length-z.filter(k=>k===-(i+1)).length);
 const types=w=>S.map(([state,last])=>{for(const k of path(w)){if(last===1&&k===2){if(state==="N")state="A";else if(state==="B")state="BA"}else if(last===2&&k===1){if(state==="N")state="B";else if(state==="A")state="AB"}last=k}return B.indexOf(state)});
 const cols=w=>{const v=types(w);return B.map((_,j)=>v.reduce((n,k,i)=>n|(j===k?(1<<i):0),0))};
 const rank=columns=>{const piv=Array(9).fill(0);let r=0;for(let c of columns){for(let j=8;j>=0;j--){if(!(c&(1<<j)))continue;if(piv[j])c^=piv[j];else{piv[j]=c;r++;break}}}return r};
 const words=(e,t,q,r)=>{const f=t-r,g=q-r,tail="a".repeat(e-1)+"e".repeat(e-1)+"f".repeat(f)+"g".repeat(g);if(r)return ["ce"+"c".repeat(r-1)+tail,"ec"+"c".repeat(r-1)+tail,"de"+"d".repeat(r-1)+tail,"ed"+"d".repeat(r-1)+tail];const base="e".repeat(e)+"a".repeat(e-1),out=[base+"f".repeat(f)+"g".repeat(g)];if(f)out.push("f"+base+"f".repeat(f-1)+"g".repeat(g));if(g)out.push("g"+base+"f".repeat(f)+"g".repeat(g-1));return out};
 const weights=[[2,3,5,7,11,13],[3,4,7,11,13,17]];
 let total=0,multifibers=0;const hist={5:0,7:0,9:0};
 for(let e=1;e<=3;e++)for(let t=0;t<=5;t++)for(let q=0;q<=5;q++){let m=Math.min(t,q),p=[2*e+t,q,e,0,0,0];if(m)multifibers++;
  for(let r=0;r<=m;r++){const h=2*e-1+t+q-r,wset=words(e,t,q,r),observations=[];
   for(const w of wset){const z=path(w),pc=positive(z);
    if(w.length!==h||JSON.stringify(pc)!==JSON.stringify(p)||JSON.stringify(displacement(z))!==JSON.stringify([2,0,0,0,0,0])||z.length!==2*p.reduce((a,b)=>a+b,0)-2)throw Error("native path/count mismatch");
    for(const x of weights){let a=1n,b=1n;for(let i=0;i<6;i++){a*=BigInt(x[i])**BigInt(pc[i]);b*=BigInt(x[i])**BigInt(p[i])}if(a!==b)throw Error("BRC factor mismatch")}
    observations.push(...cols(w));
   }
   const expected=r?9:5+2*(t>0)+2*(q>0),actual=rank(observations);
   if(actual!==expected)throw Error("fiber rank mismatch "+JSON.stringify({e,t,q,r,actual,expected}));
   hist[actual]++;total++;
  }
 }
 if(total!==273||multifibers!==75)throw Error("finite range incomplete");
 for(let m=1;m<=8;m++)for(let r=0;r<=m;r++){const ww=words(1,m,m,r),p=[m+2,m,1,0,0,0];if(rank(ww.flatMap(cols))!==9||ww.some(w=>path(w).length!==4*m+4||JSON.stringify(positive(path(w)))!==JSON.stringify(p)))throw Error("infinite-family witness");}
 const e2=["ce","ec","de","ed"],e3=["feg","gef"];if(rank(e2.flatMap(cols))!==9||rank(e3.flatMap(cols))!==9)throw Error("collision rank");
 return {status:"PASS",source:"self-contained V8/Node JS, integer GF(2) rank (rank 9 also implies Q rank 9), exact native signed X6 and BigInt positive-BRC monomials",finite_parameters:{p3_e:[1,3],t_p1_minus_2e:[0,5],p2:[0,5]},fiber_horizon_checks:total,multi_horizon_fibers:multifibers,rank_distribution:hist,collision:{p:[3,1,1,0,0,0],h2_words:e2,h3_words:e3,h2_rank:9,h3_rank:9,primitive_steps_per_word:8,X:"120",Y:"756"},unbounded_alias_witness_m_range:[1,8],proof_scope:"Analytic full-domain result in README; checked finite range only"};
};
console.log(JSON.stringify(verify(),null,2));
