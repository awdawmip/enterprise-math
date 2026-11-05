#!/usr/bin/env node
"use strict";
// EC49FBH full finite H2-H6 key-schedule verifier. Native signed X6/BRC.
// Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab
// Node.js >=18; prints all 136 exact integer results.
const OP={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const ALPH="acdefg";
const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
const SIG=[0,0,4,1,16,32,8,2,0], CLAUSES=[18,20,33,40];
const rank=m=>CLAUSES.every(c=>(m&c)!==0), key=k=>k.join(",");
const early=["fe","ge","feg","gef"];
const native=w=>[...w].flatMap(c=>OP[c]);
const free=new Set();
for(const w of early){const p=native(w);for(let j=1;j<=p.length;j++)free.add(p.slice(0,j).join(","));}
if(free.size!==16)throw Error("early signed-prefix count");
const memo=new Map();
function reach(ct,s){
 const id=ct.join(",")+":"+s;
 if(memo.has(id))return memo.get(id);
 if(ct.every(x=>x===0))return SIG[s];
 let m=0;
 for(let i=0;i<6;i++)if(ct[i]>0){const c=ct.slice();c[i]--;m|=reach(c,T[s][i]);}
 memo.set(id,m);return m;
}
function reachKey(k,h){
 const [x,y,z]=k,a=z-1,e=z,r=x+y-h-1,f=h+1-y-2*z,g=h+1-x;
 if(Math.min(a,e,r,f,g)<0)return 0;
 let mask=0;for(let c=0;c<=r;c++)mask|=reach([a,c,r-c,e,f,g],0);
 return mask;
}
const Lkeys=[],Mkeys=[];
for(let x=0;x<=10;x++)for(let y=0;y<=10;y++)for(let z=1;z<=5;z++){
 const k=[x,y,z];
 if(rank(reachKey(k,4)))Lkeys.push(k);
 if(rank(reachKey(k,8))&&rank(reachKey(k,9)))Mkeys.push(k);
}
if(Lkeys.length!==9||Mkeys.length!==50)throw Error("rank-key classification changed");
const groups={4:new Map(),5:new Map(),6:new Map()};
for(const h of [4,5,6]){
 function rec(w,delta,pos,s){
  if(w.length===h){
   if(delta[0]!==2||delta.slice(1).some(x=>x!==0)||!SIG[s])return;
   const k=key(pos.slice(0,3)),g=groups[h].get(k)||[];
   g.push([w,SIG[s]]);groups[h].set(k,g);return;
  }
  for(let i=0;i<6;i++){
   const c=ALPH[i],d=delta.slice(),p=pos.slice();
   for(const st of OP[c]){const j=Math.abs(st)-1;d[j]+=st>0?1:-1;if(st>0)p[j]++;}
   rec(w+c,d,p,T[s][i]);
  }
 }
 rec("",Array(6).fill(0),Array(6).fill(0),0);
}
const totals=[4,5,6].map(h=>[...groups[h].values()].reduce((a,b)=>a+b.length,0));
if(totals.join(",")!=="206,1062,5352")throw Error("word candidates changed");
function sigmask(s){let m=0;for(let i=0;i<4;i++)if(s&CLAUSES[i])m|=1<<i;return m;}
function minimize(L,M){
 const nodes=[{ch:new Map(),terminal:0,prefix:""}];
 function ins(w,mask){
  let at=0,p=[];
  for(const st of native(w)){
   p.push(st);let j=nodes[at].ch.get(st);
   if(j===undefined){j=nodes.length;nodes[at].ch.set(st,j);nodes.push({ch:new Map(),terminal:0,prefix:p.join(",")});}
   at=j;
  }
  nodes[at].terminal|=mask;
 }
 for(const w of early)ins(w,0);
 for(const [idx,h] of [4,5,6].entries()){
  for(const [w,s] of (groups[h].get(key(L))||[]).concat(groups[h].get(key(M))||[]))ins(w,sigmask(s)<<(4*idx));
 }
 const dp=new Array(nodes.length);
 for(let i=nodes.length-1;i>=0;i--){
  const n=nodes[i];let states=new Map([[0,0]]);
  if(n.terminal)states.set(n.terminal,0);
  for(const c of n.ch.values()){
   const next=new Map();
   for(const [a,ca] of states)for(const [b,cb] of dp[c]){
    const m=a|b,v=ca+cb,old=next.get(m);
    if(old===undefined||v<old)next.set(m,v);
   }
   states=next;
  }
  if(i&&!free.has(n.prefix))for(const [m,v] of states)if(m)states.set(m,v+1);
  dp[i]=states;
 }
 const v=dp[0].get(4095);return v===undefined?null:16+v;
}
const pairs=[];
for(const L of Lkeys)for(const M of Mkeys){
 const s=L[0]+L[1];
 if(s<7&&!rank(reachKey(M,6)))continue;
 if(s<8&&!rank(reachKey(M,7)))continue;
 pairs.push({L,M,minH2H6:minimize(L,M)});
}
const feasible=pairs.filter(v=>v.minH2H6!==null);
const best=Math.min(...feasible.map(v=>v.minH2H6));
const winners=feasible.filter(v=>v.minH2H6===best);
if(pairs.length!==136||feasible.length!==124||best!==70||
 winners.length!==1||key(winners[0].L)!=="4,2,1"||key(winners[0].M)!=="6,4,1")
 throw Error("EC49FBH exact result mismatch");
console.log(JSON.stringify({schema:"EC49FBH_EXACT_INTEGER_CERTIFICATE",scientific_pin:"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
 H4_keys:9,H8_H9_rank_keys:50,necessary_pairs:136,feasible_pairs:124,
 eligible_candidate_counts:totals,minimum_H2_H6:best,unique_key_pair:winners[0],
 method:"ordered native signed-X6 primitive-word and 9-state DFA enumeration; exact OR/min-plus trie",pairs,status:"PASS"},null,2));
