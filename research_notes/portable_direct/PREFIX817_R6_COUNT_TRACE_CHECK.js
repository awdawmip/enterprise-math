'use strict';
// Exact BigInt regression for PREFIX-817; no external dependencies.
const assert = require('node:assert/strict');
const bitcount = n => { let k=0; while(n){n &= n-1;k++;} return k; };
const eq = (a,b) => a.length === b.length && a.every((x,i)=>x===b[i]);
function states(m,q) {return Array.from({length:1<<m},(_,i)=>i).filter(x=>bitcount(x)<=q);}
function graph(m,q,alpha,beta) {
 const ss=states(m,q), N=ss.length, idx=new Map(ss.map((s,i)=>[s,i]));
 const Q=Array.from({length:N},()=>Array(N).fill(0n));
 for(let s=0;s<N;s++) for(let i=0;i<m;i++) {
   const active=!!(ss[s]&(1<<i));
   if(active) Q[s][idx.get(ss[s]^(1<<i))] += BigInt(beta[i]);
   else if(bitcount(ss[s])<q) Q[s][idx.get(ss[s]^(1<<i))] += BigInt(alpha[i]);
 }
 return {ss,Q};
}
function traceRows(m,q,alpha,beta,H) {
 const {ss,Q}=graph(m,q,alpha,beta), N=ss.length;
 let G=ss.map(s=>Array.from({length:q+1},(_,k)=>BigInt(bitcount(s)===k)));
 const series=[G];
 for(let h=1;h<=H;h++) {
   G=Array.from({length:N},(_,i)=>Array.from({length:q+1},(_,k)=>
     Q[i].reduce((v,w,j)=>v+w*series[h-1][j][k],0n)));
   series.push(G);
 }
 return {ss,series};
}
function* vectors(m) {for(let x=0;x<3**m;x++){let a=[],v=x;for(let i=0;i<m;i++){a.push(v%3);v=Math.floor(v/3);}yield a;}}
const res={schema:'PREFIX817_EXACT_INTEGER_REGRESSION_V1',arithmetic:'BigInt exact',q1_weight_patterns:0,q1_individual_states_checked:0,q1_horizon_vector_checks:0,q1_partition_pair_checks:0,generic_weight_patterns:0,generic_pairs_checked:0,generic_horizon_certificate_checks:0,late_distinguishing_witness:{m:3,q:2,alpha:[1,1,2],beta:[1,1,1],S:[0,1],T:[0,2],h0:[[0,0,1],[0,0,1]],h1:[[0,2,0],[0,2,0]],h2:[[2,0,6],[2,0,5]]}};
for(let m=1;m<=4;m++) for(const alpha of vectors(m)) for(const beta of vectors(m)) {
 const {ss,series}=traceRows(m,1,alpha,beta,8), A=alpha.reduce((a,b)=>a+b,0), B=alpha.reduce((a,v,i)=>a+v*beta[i],0);
 res.q1_weight_patterns++;
 for(let si=0;si<ss.length;si++) {
   const S=ss[si], isEmpty=S===0, bi=isEmpty?0:beta[Math.log2(S)];
   let p0=isEmpty?1n:0n,p1=isEmpty?0n:1n,pb=BigInt(bi);
   for(let h=0;h<=8;h++) {
     assert(eq(series[h][si],[p0,p1])); res.q1_horizon_vector_checks++;
     [p0,p1,pb]=[pb,BigInt(A)*p0,BigInt(B)*p0];
   }
   res.q1_individual_states_checked++;
 }
 for(let i=0;i<ss.length;i++) for(let j=i+1;j<ss.length;j++) {
   const same=ss[i]===0&&ss[j]===0 || ss[i]!==0&&ss[j]!==0&&beta[Math.log2(ss[i])]===beta[Math.log2(ss[j])];
   assert.equal(series.every(G=>eq(G[i],G[j])),same);
   res.q1_partition_pair_checks++;
 }
}
for(let m=1;m<=3;m++) for(let q=0;q<=m;q++) for(const alpha of vectors(m)) for(const beta of vectors(m)) {
 const N=states(m,q).length,{ss,series}=traceRows(m,q,alpha,beta,N+2);
 res.generic_weight_patterns++;
 for(let i=0;i<N;i++) for(let j=i+1;j<N;j++) {
   let same=true;
   for(let h=0;h<N;h++) if(!eq(series[h][i],series[h][j])){same=false;break;}
   if(same) for(let h=N;h<=N+2;h++) {
     assert(eq(series[h][i],series[h][j]));res.generic_horizon_certificate_checks++;
   }
   res.generic_pairs_checked++;
 }
}
const w=res.late_distinguishing_witness;
const {ss,series}=traceRows(w.m,w.q,w.alpha,w.beta,2);
const mask = ids=>ids.reduce((a,i)=>a|(1<<i),0);
for(let h=0;h<=2;h++) assert(eq(series[h][ss.indexOf(mask(w.S))],w["h"+h][0].map(BigInt)) && eq(series[h][ss.indexOf(mask(w.T))],w["h"+h][1].map(BigInt)));
res.all_assertions_passed=true;
process.stdout.write(JSON.stringify(res,null,2)+'\n');