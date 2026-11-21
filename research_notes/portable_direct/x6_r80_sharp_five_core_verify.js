'use strict';
// X6 R80 finite exhaustive certificate. Run: node x6_r80_sharp_five_core_verify.js
// Signed lattice box [-16,16]^3; exact integer gap dominance; BigInt exact rational comparison.
const certify = function certify(){
const S=[[3,-4,1],[3,-7,2],[6,-4,1],[9,-5,1],[10,-5,1]];
const profiles=[[18,12,1,1],[1,12,30,1],[1,1,1,24],[1,1,6,12],[1,1,1,1]];
const pairs=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
function q(v){return Math.max(v.reduce((s,x)=>s+Math.max(x,0),0),v.reduce((s,x)=>s+Math.max(-x,0),0))}
function gaps(a){const [x,y,z]=a,m=[0,2*x+6*y+12*z,6*x+24*y+60*z,14*x+78*y+252*z];return pairs.map(([i,j])=>{const n=Math.abs(m[i]-m[j]);if(n%2)throw Error("odd");return n/2})}
function cmp(a,b){const t=a[0]*b[1]-b[0]*a[1];return t<0n?-1:t>0n?1:0}
function cost(g,w){let ans=[0n,1n];for(let k=0;k<6;k++){let [i,j]=pairs[k],f=[BigInt(g[k]),BigInt(w[i]+w[j])];if(cmp(f,ans)>0)ans=f}return ans}
function gcd(a,b){while(b){let t=a%b;a=b;b=t}return a}
function frac(f){const d=gcd(f[0],f[1]);return (f[0]/d)+"/"+(f[1]/d)}
const gs=S.map(gaps),demand=S.map(q);
if(JSON.stringify(demand)!==JSON.stringify([4,7,7,10,11]))throw Error("q");
const all=[];
for(let x=-16;x<=16;x++)for(let y=-16;y<=16;y++)for(let z=-16;z<=16;z++){const a=[x,y,z];let d=q(a);if(d>16||d===0)continue;all.push({a,q:d,g:gaps(a)})}
const up15=all.filter(x=>x.q<=15);
if(up15.length!==12430||all.length!==14992)throw Error("domain count");
const dominationCounts=[0,0,0,0,0];
for(const item of up15){const k=gs.findIndex(g=>g.every((v,j)=>v<=item.g[j]));if(k<0)throw Error("uncovered "+item.a);dominationCounts[k]++}
const winners=[];
for(let k=0;k<5;k++){
 const w=profiles[k],target=cost(gs[k],w);let ties=[],second=null;
 for(const item of up15){const v=cost(item.g,w),c=cmp(v,target);if(c<0)throw Error("defeated "+k+" by "+item.a);if(c===0)ties.push(item.a);if(c>0&&(!second||cmp(v,second)<0))second=v}
 if(ties.length!==2||!ties.some(a=>JSON.stringify(a)===JSON.stringify(S[k]))||!ties.some(a=>JSON.stringify(a)===JSON.stringify(S[k].map(x=>-x))))throw Error("not unique ± "+k);
 winners.push({difference:S[k],q:demand[k],w,eta:frac(target),next_other_eta:frac(second),exact_minimizers:ties})
}
const edgeW=[1447,167,166,1850],special=[];
for(const p of [15,16]){
 let best=null,ties=[];
 for(const item of all){if(item.q>p)continue;let c=cost(item.g,edgeW);if(!best||cmp(c,best)<0){best=c;ties=[item.a]}else if(cmp(c,best)===0)ties.push(item.a)}
 special.push({p,eta:frac(best),minimizers:ties})
}
if(special[0].eta!=="1/333"||special[1].eta!=="1/336")throw Error("edge");
return {schema:"X6_R80_SHARP_FIVE_CORE_Q11_TO15_V1",model:"Conditional positive-count D=4 BRC star moment observer with unknown common offset and arbitrary positive weights",frozen_p000_commit:"a72226e2430ffa4786321ac86e7f0c599d5f0389",scope:{port_range:"11<=p<=15",difference_domain:"a in Z^3\\{0}, q(a)<=p",pair_gap_order:"12,13,14,23,24,34",all_signed_differences_q_at_most_15:up15.length,all_signed_differences_q_at_most_16:all.length},core_differences:S,core_gap_sextuples:gs,domination_counts_first_witness:dominationCounts,strict_winners:winners,first_next_port_transition:{weights:edgeW,values:special},independence:"Fresh exact finite enumeration from the definition, not from the R72 28-entry atlas",review:"AUTHOR_VERIFIED_NOT_INDEPENDENTLY_REVIEWED",native_x6_status:"OBSERVER_ONLY_NOT_NATIVE_TIME_DYNAMICS"};
};
console.log(JSON.stringify(certify(),null,2));
