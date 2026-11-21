'use strict';
// R85: global minimality of R82 six cores at every p=23..38.
// R82 supplies universal sufficiency. This audits unique global witnesses.
const assert=require('node:assert/strict');
const A=[
 ['s4',[3,-4,1],[18,12,1,1]],
 ['s7',[6,-4,1],[1,1,1,24]],
 ['s10',[9,-5,1],[1,1,6,12]],
 ['s11',[10,-5,1],[1,1,1,1]],
 ['s16',[15,-6,1],[7,1,1,15]],
 ['b21',[21,-7,1],[1,179,153,15]],
 ['s27',[24,-14,3],[163,165,1809,388]]
];
const q=a=>Math.max(a.reduce((s,x)=>s+Math.max(0,x),0),a.reduce((s,x)=>s+Math.max(0,-x),0));
function gaps([x,y,z]){const v=[0,2*x+6*y+12*z,6*x+24*y+60*z,14*x+78*y+252*z];
return [0,1,2].flatMap(i=>Array.from({length:3-i},(_,k)=>Math.abs(v[i]-v[i+k+1])/2));}
function cost(a,w){const G=gaps(a),d=[w[0]+w[1],w[0]+w[2],w[0]+w[3],w[1]+w[2],w[1]+w[3],w[2]+w[3]];let n=BigInt(G[0]),m=BigInt(d[0]);
for(let i=1;i<6;i++)if(BigInt(G[i])*m>n*BigInt(d[i])){n=BigInt(G[i]);m=BigInt(d[i]);}return [n,m];}
const cmp=(a,b)=>a[0]*b[1]-b[0]*a[1];
function gcd(a,b){while(b)[a,b]=[b,a%b];return a;}
function frac([a,b]){let g=gcd(a,b);return String(a/g)+'/'+String(b/g);}
const out={schema:'X6_R85_FULL_DOMAIN_STRICT_GLOBAL_WINNERS_V1',source:'R82 universal sufficiency + R83 improved s16 weight',domains:{}};
for(const p of [26,38]){
const domain=[];
for(let x=-p;x<=p;x++)for(let y=-p;y<=p;y++)for(let z=-p;z<=p;z++){
const a=[x,y,z],f=a.find(t=>t!==0);if(f===undefined||f<0||q(a)>p)continue;domain.push(a);}
assert.equal(domain.length,p===26?31031:95133);
const winners=[];
for(const [id,a,w] of A.filter(x=>x[0]!== (p===26?'s27':'b21'))){
const v=cost(a,w);let tied=0,better=0,second=null;
for(const b of domain){const c=cost(b,w),sgn=cmp(c,v);
if(sgn===0n)tied++;if(sgn<0n)better++;
if(sgn>0n&&(second===null||cmp(c,second)<0n))second=c;}
assert.equal(tied,1,id+' tie at p='+p);assert.equal(better,0,id+' better at p='+p);
winners.push({id,a,w,optimal:frac(v),second:frac(second),unique_unoriented:tied});}
out.domains[p]={unoriented:domain.length,global_strict_winners:winners};
}
console.log(JSON.stringify(out,null,2));