'use strict';
// X6 R81 independent finite exhaustive proof. Run: node x6_r81_ports16_22_two_sharp_six_cores_verify.js
// Six-coordinate exact integer domination of all feasible signed differences, plus strict BigInt rational winners.
const certify = function certify(){
const a16=[[3,-4,1],[3,-7,2],[6,-4,1],[9,-5,1],[10,-5,1],[15,-6,1]];
const a22=[[3,-4,1],[6,-4,1],[9,-5,1],[10,-5,1],[15,-6,1],[21,-7,1]];
const w16=[[18,12,1,1],[1,12,30,1],[1,1,1,24],[1,1,6,12],[1,1,1,1],[1447,167,166,1850]];
const w22=[[18,12,1,1],[1,1,1,24],[1,1,6,12],[1,1,1,1],[1447,167,166,1850],[1,179,153,15]];
const pairs=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
function q(a){return Math.max(a.reduce((s,x)=>s+Math.max(x,0),0),a.reduce((s,x)=>s+Math.max(-x,0),0))}
function gg(a){const [x,y,z]=a,m=[0,2*x+6*y+12*z,6*x+24*y+60*z,14*x+78*y+252*z];return pairs.map(([i,j])=>{const n=Math.abs(m[i]-m[j]);if(n%2)throw Error("odd moment gap");return n/2})}
function cmp(u,v){const x=u[0]*v[1]-v[0]*u[1];return x<0n?-1:x>0n?1:0}
function cost(g,w){let c=[0n,1n];for(let k=0;k<6;k++){const [i,j]=pairs[k],v=[BigInt(g[k]),BigInt(w[i]+w[j])];if(cmp(v,c)>0)c=v}return c}
function gcd(a,b){while(b){const t=a%b;a=b;b=t}return a}
function fmt(u){const d=gcd(u[0],u[1]);return (u[0]/d)+"/"+(u[1]/d)}
const all=[];for(let x=-22;x<=22;x++)for(let y=-22;y<=22;y++)for(let z=-22;z<=22;z++){
 const a=[x,y,z],d=q(a);if(!d||d>22)continue;all.push({a,q:d,g:gg(a)})}
if(all.length!==37994)throw Error("q22 count");
const records=[];
for(const [p,S,weights] of [[21,a16,w16],[22,a22,w22]]){
 const gs=S.map(gg),d=S.map(q),domain=all.filter(x=>x.q<=p);
 if(domain.length!==(p===21?33152:37994))throw Error("domain count "+p);
 if(d.some(x=>x>(p===21?16:22)))throw Error("invalid core");
 const assigned=Array(S.length).fill(0);
 for(const item of domain){const k=gs.findIndex(g=>g.every((v,i)=>v<=item.g[i]));if(k<0)throw Error("uncovered "+item.a+" p="+p);assigned[k]++}
 const winners=[];
 for(let k=0;k<S.length;k++){
  const w=weights[k],target=cost(gs[k],w);let ties=[],second=null;
  for(const item of domain){const v=cost(item.g,w),c=cmp(v,target);if(c<0)throw Error("counterwinner at "+p+" : "+item.a);
    if(c===0)ties.push(item.a);else if(!second||cmp(v,second)<0)second=v}
  if(ties.length!==2||!ties.some(a=>JSON.stringify(a)===JSON.stringify(S[k]))||!ties.some(a=>JSON.stringify(a)===JSON.stringify(S[k].map(x=>-x))))throw Error("not strict uniqueness "+p+" "+k);
  winners.push({a:S[k],q:d[k],w,eta:fmt(target),second:fmt(second),unique_minimizers_up_to_sign:true})
 }
 records.push({p_range:p===21?"16..21":"22 only",enumerated_at_p:p,domain_size:domain.length,core:S,gap_vectors:gs,demands:d,first_domination_witness_counts:assigned,strict_winners:winners})
}
const edgeW=[1,12,30,1];
const edge=records.map(r=>{const ds=r.gap_vectors;let best=null;for(const g of ds){const v=cost(g,edgeW);if(!best||cmp(v,best)<0)best=v}return fmt(best)});
if(JSON.stringify(edge)!==JSON.stringify(["15/31","6/13"]))throw Error("swap mismatch");
return {schema:"X6_R81_Q16_TO22_EXACT_MINIMAL_SIX_WITH_Q22_REPLACEMENT_V1",scientific_pin:"a72226e2430ffa4786321ac86e7f0c599d5f0389",model:"conditional D4 positive-count BRC 4-channel moment observer",proof_scope:"finite exhaustive integer coordinatewise domination, arbitrary positive real weights",results:records,sharp_q21_to22_witness:{weights:edgeW,eta_at_p21:edge[0],eta_at_p22:edge[1],swapped_essential_direction:"(3,-7,2) replaced by (21,-7,1) in the minimal core at Port22"},source_dependency:"No R72 atlas needed",review:"AUTHOR_EXACT_CHECK_NOT_INDEPENDENTLY_REVIEWED",native_x6_status:"OBSERVER_ONLY"};
};
console.log(JSON.stringify(certify(), null, 2));
