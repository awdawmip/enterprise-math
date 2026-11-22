#!/usr/bin/env node
"use strict";
// R122 portable exact integer certificate for conditional four-positive-weight, six-pair BRC.
// Source input: R121 @8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd.
const verify = function verify(){
 const bank=[[1,0,0],[0,2,-1],[1,-3,1],[2,-3,1],[3,-1,0],[1,3,-1],[3,-4,1],[4,-1,0],[3,2,-1],[4,-4,1],[5,-1,0],[5,-4,1],[6,-1,0],[3,-7,2],[6,-4,1],[7,-1,0],[7,2,-1],[9,-5,1]];
 const q=([x,y,z])=>Math.max(Math.max(x,0)+Math.max(y,0)+Math.max(z,0),Math.max(-x,0)+Math.max(-y,0)+Math.max(-z,0));
 const gap=([x,y,z])=>{const h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z];return [Math.abs(h[1]-h[0]),Math.abs(h[2]-h[0]),Math.abs(h[3]-h[0]),Math.abs(h[2]-h[1]),Math.abs(h[3]-h[1]),Math.abs(h[3]-h[2])];};
 const all=[];for(let x=-10;x<=10;x++)for(let y=-10;y<=10;y++)for(let z=-10;z<=10;z++){if(!x&&!y&&!z)continue;let first=x||y||z;if(first<0)continue;let a=[x,y,z],p=q(a);if(p<=10)all.push({a,p,g:gap(a)});}
 const b=bank.map(a=>({a,p:q(a),g:gap(a)}));
 const counts=[],totals=[],sets=[],excluded=[],coverByPort=[];
 for(let p=1;p<=10;p++){
  const pool=all.filter(r=>r.p<=p),bankpool=b.filter(r=>r.p<=p),possible=[];
  let covered=0;
  for(const a of pool){const w=bankpool.find(row=>a.g.every((v,j)=>2*v>=3*row.g[j]));if(w){covered++;}else possible.push(a.a);}
  for(const a of pool){const full=pool.some(r=>a.g.every((v,j)=>2*v>=3*r.g[j]));const bankyes=bankpool.some(r=>a.g.every((v,j)=>2*v>=3*r.g[j]));if(full!==bankyes)throw Error("optimizer-bank completeness failed p="+p+" direction="+a.a);}
  counts.push(possible.length);totals.push(pool.length);excluded.push(covered);sets.push(possible);
 }
 const expectedPop=[6,27,73,154,280,461,707,1028,1434,1935],expectedCounts=[1,4,7,12,14,19,15,16,20,20];
 if(JSON.stringify(totals)!==JSON.stringify(expectedPop)||JSON.stringify(counts)!==JSON.stringify(expectedCounts))throw Error("unexpected finite census");
 const unique=[...new Set(sets.flat().map(v=>v.join(",")))].sort();
 if(unique.length!==31||excluded[9]!==1915)throw Error("union or exclusion mismatch");
 return {schema:"X6_R122_EXACT_SMALL_PORT_NEAR_EXCLUSION_V1",status:"PASS",date:"2026-11-23",model:"conditional four-positive-real-weight, six-pair BRC observation",definition:"g=(|h1-h0|,|h2-h0|,|h3-h0|,|h2-h1|,|h3-h1|,|h3-h2|); candidate a kept iff no feasible R121 bank b satisfies 2g_j(a)>=3g_j(b) for all six j",p_range:"1..10",population_counts:totals,candidate_counts:counts,excluded_counts:excluded,candidates_by_port:sets,union_candidates:unique,optimizer_bank:bank,check:"each of the 1935 full Port-10 vectors is included; full-pool versus 18-bank 3/2-exclusion predicates agree at all 10 Ports",scope:"The candidate sets are a necessary near-direction envelope, not an attained-realizability classification; only Port 1 is exact"};
};
console.log(JSON.stringify(verify(), null, 2));
