#!/usr/bin/env node
// EC49FXW / BRC16943: exact integer arithmetic, no solver or floats.
"use strict";
const mod=(x,m)=>(x%m+m)%m;
const gcd=(a,b)=>b?gcd(b,a%b):a;
const inv=(a,m)=>{for(let x=1;x<m;x++)if(mod(a*x,m)===1)return x;throw Error("inverse")};
const need=(ok,msg)=>{if(!ok)throw Error(msg)};
const slopes={"0,0":[3],"0,1":[0,3,4,5],"1,0":[2,3,4,5],"1,1":[2,3]};
function P(h,n){h=mod(h,10);n=mod(n,10);if(h%5===0&&n%5===0)return false;
 const s=h%5===0?5:mod(n*inv(h%5,5),5);return slopes[`${h%2},${n%2}`].includes(s)}
const rep=new Map();
for(let a=0;a<10;a++)for(let c=0;c<10;c++)if(gcd(gcd(a,c),10)===1){
 let x,y;outer:for(x=0;x<10;x++)for(y=0;y<10;y++)if(mod(c*x-a*y+1,10)===0)break outer;
 let u=0;for(let t=0;t<10;t++)if(P(x+a*t,y+c*t))u|=1<<t;
 rep.set(`${a},${c}`,{x,y,u});}
need(rep.size===72&&new Set([...rep.values()].map(z=>z.u)).size===50,"50 supports");
function norm(a,c){const b=a+c,e=inv(a,b),h0=(a*e-1)/b,n0=e-h0;
 const {x,y,u}=rep.get(`${a%10},${c%10}`);let t0=-1;
 for(let t=0;t<10;t++)if(mod(h0+a*t-x,10)===0&&mod(n0+c*t-y,10)===0){t0=t;break}
 need(t0>=0,"normalization");const L0=9*(h0+a*t0)+10*(n0+c*t0),L1=9*a+10*c;
 const hole=mod(L1,11)===0?null:mod(-L0*inv(mod(L1,11),11),11);
 need(hole!==null||mod(L0,11)!==0,"degeneracy");return {u,hole,a,b,c,t0,h0,n0}}
const states=new Map();
for(let b=2;b<=139;b++)for(let a=1;a<b;a++)if(gcd(a,b)===1){const s=norm(a,b-a),k=`${s.u}/${s.hole}`;if(!states.has(k))states.set(k,s)}
need(states.size===600,"600 states");
function spectrum(s){const U=Array.from({length:10},(_,i)=>s.u>>i&1),V=Array.from({length:11},(_,i)=>Number(s.hole!==i));
 const av=Array.from({length:10},(_,t)=>U.reduce((v,x,j)=>v+x*U[mod(t-j,10)],0));
 const vv=Array.from({length:11},(_,t)=>V.reduce((v,x,j)=>v+x*V[mod(t-j,11)],0));
 return av.flatMap(x=>vv.map(y=>2*(U.reduce((a,b)=>a+b,0)*V.reduce((a,b)=>a+b,0)-x*y))).join(",")}
const fibers=new Map();for(const s of states.values()){const k=spectrum(s);if(!fibers.has(k))fibers.set(k,[]);fibers.get(k).push(s)}
const pairs=[];for(const f of fibers.values())if(f.length===2){need(f[0].hole===f[1].hole,"fiber factor");pairs.push({G:f[0].u^f[1].u,z:f[0].hole,B:Math.max(f[0].b,f[1].b)})}else need(f.length===1,"fiber size");
need(fibers.size===478&&pairs.length===122,"spectrum census");
const mask=rows=>rows.reduce((m,j)=>m|(1<<j),0),A=mask([1,4,6,9]),B=mask([2,7]),C=mask([3,8]);
need((A&B)===0&&(A&C)===0&&(B&C)===0,"disjoint");
need([A,B,C].every(G=>pairs.some(p=>p.G===G&&p.B<=22)),"early disjoint obstructions");
need([...new Set(pairs.map(p=>p.G))].every(G=>[A,B,C].some(m=>(G&m)===m)),"all supports contain a minimal group");
const thresholds={};for(const [label,G] of [["A",A],["B",B],["C",C]]){
 thresholds[label]=Math.max(...Array.from({length:11},(_,z)=>Math.min(...pairs.filter(p=>p.G===G&&p.z===z).map(p=>p.B))))}
need(JSON.stringify(thresholds)===JSON.stringify({A:52,B:58,C:64}),"eleven-hole thresholds");
const witness={
51:{
1:[[7,6],[8,6],[9,9]],
2:[[2,6],[3,6],[4,9],[7,6],[8,6],[9,9]],
3:[[2,6],[3,6],[4,9],[6,9],[7,6],[7,8],[8,4],[8,6],[9,9]],
4:[[1,9],[2,6],[2,8],[3,4],[3,6],[4,9],[6,9],[7,6],[7,8],[8,4],[8,6],[9,9]]},
57:{
1:[[7,6],[8,0],[9,8],[9,9]],
2:[[2,6],[3,0],[7,6],[8,0],[9,8],[9,9],[9,10]],
3:[[2,6],[3,0],[6,0],[6,9],[7,4],[7,6],[8,0],[8,6],[9,3],[9,7]],
4:[[2,4],[2,6],[3,0],[3,6],[6,0],[6,6],[7,4],[7,6],[8,0],[8,6],[9,5],[9,7],[9,10]]},
63:{
1:[[7,4],[7,5],[8,0],[9,1],[6,7]],
2:[[3,0],[6,7],[7,4],[7,5],[7,6],[8,0],[9,1],[9,2]],
3:[[3,0],[7,4],[7,5],[7,6],[7,8],[8,0],[8,6],[9,1],[9,4],[9,7],[9,10]],
4:[[3,0],[3,6],[6,3],[6,10],[7,3],[7,4],[7,5],[7,6],[7,8],[8,0],[8,6],[9,0],[9,4],[9,7]]},
64:Object.fromEntries([1,2,3,4].map(r=>[r,[1,2,3].flatMap(j=>Array.from({length:r+1},(_,v)=>[j,v]))]))
};
let layoutChecks=0;const certificate={};
for(const [height,levels] of Object.entries(witness))for(const [level,sites] of Object.entries(levels)){
 const H=Number(height),r=Number(level),expected=3*r+Number(H>=52)+Number(H>=58)+Number(H>=64);
 need(sites.length===expected&&new Set(sites.map(p=>p.join(","))).size===expected,`site count ${height}:${level}`);
 let cnt=0;for(const p of pairs)if(p.B<=H){
  const d=sites.filter(([j,v])=>(p.G>>j&1)!==0&&p.z!==v).length;
  need(d>=r,`distance ${height}:${level}: ${p.G}/${p.z}=${d}`);cnt++;layoutChecks++}
 certificate[`${height}:${level}`]={minimum:expected,number_of_genuine_pair_constraints:cnt,sites};}
let direct=0;for(const s of states.values())for(let t=0;t<110;t++){
 const h=s.h0+s.a*(s.t0+t),n=s.n0+s.c*(s.t0+t);
 const actual=P(h,n)&&mod(9*h+10*n,11)!==0;
 const product=(s.u>>(t%10)&1)!==0&&s.hole!==t%11;
 need(actual===product,"direct C11 mismatch");direct++}
console.log(JSON.stringify({schema:"EC49FXW_HEIGHT_R1_R4_EXACT_CERTIFICATE_V1",frozen_input:"BRC16943",result:"ALL_PASS",
 scope:"full indexed reflection spectrum known; genuine normalized Farey anchors b<=B; fixed Boolean sites, Hamming separation r=1..4",
 theorem:{"22<=B<=51":"3r","52<=B<=57":"3r+1","58<=B<=63":"3r+2","B>=64":"3r+3"},
 support_sets:{A:[1,4,6,9],B:[2,7],C:[3,8]},thresholds,
 states:states.size,spectra:fibers.size,doubleton_pairs:pairs.length,original_C11_checks:direct,endpoint_layout_checks:layoutChecks,
 endpoint_certificate:certificate,review:"NOT_REVIEWED",native_X6_transfer:"NOT_CLAIMED"},null,2));
