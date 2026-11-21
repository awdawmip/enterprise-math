'use strict';
// X6 R82 exact integer and positive-rational verifier; no external packages.
const S22=[[3,-4,1],[6,-4,1],[9,-5,1],[10,-5,1],[15,-6,1],[21,-7,1]];
const S27=[[3,-4,1],[6,-4,1],[9,-5,1],[10,-5,1],[15,-6,1],[24,-14,3]];
const W22=[[18,12,1,1],[1,1,1,24],[1,1,6,12],[1,1,1,1],[1447,167,166,1850],[1,179,153,15]];
const W27=[[18,12,1,1],[1,1,1,24],[1,1,6,12],[1,1,1,1],[1447,167,166,1850],[163,165,1809,388]];
function assert(x,info){if(!x)throw Error(info);}

function q(a){return Math.max(a.reduce((s,x)=>s+Math.max(x,0),0),a.reduce((s,x)=>s+Math.max(-x,0),0));}

function gaps([x,y,z]){const v=[0,2*x+6*y+12*z,6*x+24*y+60*z,14*x+78*y+252*z];const g=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)g.push(Math.abs(v[i]-v[j])/2);return g;}

function dominates(g,h){return g.every((v,i)=>v<=h[i]);}

function domain(p,callback){for(let x=-p;x<=p;x++)for(let y=-p;y<=p;y++)for(let z=-p;z<=p;z++){if(x===0&&y===0&&z===0)continue;if((x||y||z)<0)continue;const a=[x,y,z];if(q(a)<=p)callback(a);}}

function coverage(p,S){const G=S.map(gaps),counts=Array(S.length).fill(0),miss=[];let total=0;domain(p,a=>{total++;let g=gaps(a),i=G.findIndex(s=>dominates(s,g));if(i<0)miss.push(a);else counts[i]++;});return{p,canonical_domain_size:total,signed_domain_size:2*total,first_dominance_witness_counts:counts,uncovered:miss};}

function less([a,b],[c,d]){return a*d<c*b;}

function maxFrac(xs){return xs.reduce((a,b)=>less(a,b)?b:a);}

function cost(g,w){const ds=[w[0]+w[1],w[0]+w[2],w[0]+w[3],w[1]+w[2],w[1]+w[3],w[2]+w[3]];return maxFrac(g.map((v,i)=>[BigInt(v),BigInt(ds[i])]));}

function gcd(a,b){while(b!==0n){const t=a%b;a=b;b=t;}return a;}

function fmt([a,b]){const d=gcd(a,b);return String(a/d)+"/"+String(b/d);}

function witnesses(S,W){return W.map((w,i)=>{const vals=S.map(a=>cost(gaps(a),w));assert(vals.every((v,j)=>j===i||less(vals[i],v)),"non-strict core witness "+i);let other=vals.filter((_,j)=>j!==i).reduce((a,b)=>less(a,b)?a:b);return{a:S[i],w,eta:fmt(vals[i]),runner_up:fmt(other)};});}

function run(){const c26=coverage(26,S22),c38=coverage(38,S27);assert(c26.canonical_domain_size===31031 && c26.uncovered.length===0,"26-P domain coverage");assert(c38.canonical_domain_size===95133 && JSON.stringify(c38.uncovered)==="[[21,-7,1]]","38-P unique exception");assert(JSON.stringify(c26.first_dominance_witness_counts)==="[29463,1385,43,131,2,7]","26-P allocation");assert(JSON.stringify(c38.first_dominance_witness_counts)==="[91611,3140,97,266,3,15]","38-P allocation");const w=[163,165,1809,388],v26=S22.map(a=>cost(gaps(a),w)).reduce((a,b)=>less(a,b)?a:b),v27=S27.map(a=>cost(gaps(a),w)).reduce((a,b)=>less(a,b)?a:b);assert(fmt(v26)==="1/328"&&fmt(v27)==="3/986","sharp transition");return{schema:"X6_R82_PORT23_38_EXACT_SIX_CORE_SWAP_V1",source_pin:"a72226e2430ffa4786321ac86e7f0c599d5f0389",model:"conditional D4 positive-count four-channel BRC observer",coverage:[c26,c38],cores:{p23_to26:S22,p27_to38:S27},strict_core_witnesses:{p23_to26:witnesses(S22,W22),p27_to38:witnesses(S27,W27)},q26_to27:{w,eta26:fmt(v26),eta27:fmt(v27)},symbolic_exception:"For a=(21,-7,1), every positive weight satisfies min(F((10,-5,1)),F((24,-14,3))) <= F(a), proved symbolically in paper.",review:"AUTHOR_COMPUTATION_NOT_INDEPENDENTLY_REVIEWED"};}
process.stdout.write(JSON.stringify(run(),null,2)+'\n');
