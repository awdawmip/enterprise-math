#!/usr/bin/env node
"use strict";
// Exact frozen signed K via original binomial formula, R462 theta=0.
const verifyR624=function verifyR624(){
 const assert=(c,m)=>{if(!c)throw Error(m)};
 const C=(n,k)=>{if(k<0||k>n||n<0)return 0n;let x=1n;for(let a=1;a<=k;a++)x=x*BigInt(n-a+1)/BigInt(a);return x;};
 function K(i){const d=[-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)];let v=Array(i+15).fill(0n);for(let r=1;r<=4;r++){const n=i+1-r;if(n<0)continue;for(let j=0;j<=n;j++)v[i-1+j]-=d[r-1]*C(n,j);}while(v.length>1&&v.at(-1)===0n)v.pop();return v;}
 const a=Array.from({length:12},(_,i)=>K(i+1)); const ord=a.map(v=>v.findIndex(x=>x!==0n)),lead=a.map(v=>String(v[ord[a.indexOf(v)]]));
 assert(ord.every((v,i)=>v===i),"BRC order");assert(lead.join(",")==="2,-1,-8,-11,6,53,106,119,83,36,9,1","BRC signed lead");
 assert(a[0].join(",")==="2,3"&&a[1].join(",")==="0,-1,4,4","BRC K1/K2");
 const value=(j,s,h)=>a[2*(j-1)+(s==="-"?1:0)][h]??0n;
 const sig=Array.from({length:6},(_,i)=>[String(value(i+1,"+",8)),String(value(i+1,"-",3))]);
 assert(JSON.stringify(sig)===JSON.stringify([["0","4"],["0","-11"],["5","0"],["561","0"],["83","0"],["0","0"]]),"sparse signature");
 const queries=["+","-"].flatMap(s=>Array.from({length:9},(_,h)=>({sign:s,degree:h})));
 let pairChecks=0;const wins=[];
 for(let i=0;i<18;i++)for(let j=i+1;j<18;j++){pairChecks++;const u=queries[i],v=queries[j],codes=Array.from({length:6},(_,k)=>`${value(k+1,u.sign,u.degree)},${value(k+1,v.sign,v.degree)}`);if(new Set(codes).size===6)wins.push([u,v]);}
 assert(pairChecks===153&&wins.length===1,"153 exhaustive pairs");assert(wins[0][0].sign==="+"&&wins[0][0].degree===8&&wins[0][1].sign==="-"&&wins[0][1].degree===3,"unique pair");
 const maxDeg=Math.max(...a.map(v=>v.length-1));let singles=0;
 for(let s of ["+","-"])for(let h=0;h<=maxDeg;h++){singles++;const c=Array.from({length:6},(_,i)=>String(value(i+1,s,h)));assert(new Set(c).size!==6,"one scalar works");}
 let perm=0;const seen=new Set();
 function rec(p,rem){if(!rem.length){perm++;const code=p.map(j=>sig[j].join(",")).join("|");assert(!seen.has(code),"orientation collision");seen.add(code);return;}for(let j=0;j<rem.length;j++)rec(p.concat(rem[j]),rem.filter((_,i)=>i!==j));}
 rec([],[0,1,2,3,4,5]);assert(perm===720&&seen.size===720,"S6 720");
 return {schema:"EM_R624_SPARSE_BRC_ORIENTATION_V1",status:"AUTHOR_SIDE_EXACT_COMPUTATION",science:{frozen_commit:"18783e01e3646c72b7aab3b16d3f565e83e6446f",K_source_blob:"7fa7a762f758b30c6090468ac43487daa34abad8",theta:"0",leading_coefficients:lead,orders:ord},two_channels:wins[0],axis_signatures:sig,coverage:{candidate_channels:18,pair_checks:pairChecks,winning_pairs:1,single_checks:singles,max_source_degree:maxDeg,orientations:perm,distinct_codes:seen.size},result:"R624_EXACT_SPARSE_TWO_PROBE_BRC_ORIENTATION_PASS"};
};
process.stdout.write(JSON.stringify(verifyR624(),null,2)+"\n");
