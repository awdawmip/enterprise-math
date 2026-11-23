#!/usr/bin/env node
'use strict';
// EC49FXX — exact integer witness checking. Frozen scientific input BRC16943.
const must=(p,s)=>{if(!p)throw Error(s)},mod=(n,m)=>(n%m+m)%m,gcd=(a,b)=>b?gcd(b,a%b):a;
const inv=(a,m)=>{for(let x=1;x<m;x++)if(mod(a*x,m)===1)return x;throw Error('inverse')};
const slopes={'0,0':[3],'0,1':[0,3,4,5],'1,0':[2,3,4,5],'1,1':[2,3]};
function P(h,n){h=mod(h,10);n=mod(n,10);if(h%5===0&&n%5===0)return false;
const s=h%5===0?5:mod(n*inv(h%5,5),5);return slopes[`${h%2},${n%2}`].includes(s)}
const reps=new Map();
for(let a=0;a<10;a++)for(let c=0;c<10;c++)if(gcd(gcd(a,c),10)===1){
let x=-1,y=-1; outer:for(let xx=0;xx<10;xx++)for(let yy=0;yy<10;yy++)if(mod(c*xx-a*yy+1,10)===0){x=xx;y=yy;break outer}
let u=0;for(let t=0;t<10;t++)if(P(x+a*t,y+c*t))u|=1<<t;
reps.set(`${a},${c}`,{x,y,u})}
must(reps.size===72&&new Set([...reps.values()].map(s=>s.u)).size===50,'50 supports');
function norm(a,c){
const b=a+c,e=inv(a,b),h0=(a*e-1)/b,n0=e-h0,{x,y,u}=reps.get(`${a%10},${c%10}`);
let t0=-1;for(let t=0;t<10;t++)if(mod(h0+a*t-x,10)===0&&mod(n0+c*t-y,10)===0){t0=t;break}
must(t0>=0,'normalization');
const L0=9*(h0+a*t0)+10*(n0+c*t0),L1=9*a+10*c;
const z=mod(L1,11)===0?null:mod(-L0*inv(mod(L1,11),11),11);
must(z!==null||mod(L0,11)!==0,'degenerate factor');
return {a,b,c,u,z,h0,n0,t0}}
const states=new Map();
for(let b=2;b<=139;b++)for(let a=1;a<b;a++)if(gcd(a,b)===1){
const s=norm(a,b-a),k=`${s.u}/${s.z}`;if(!states.has(k))states.set(k,s)}
must(states.size===600,'600 states');
function spec(s){const U=Array.from({length:10},(_,i)=>s.u>>i&1),V=Array.from({length:11},(_,i)=>Number(s.z!==i));
const a=Array.from({length:10},(_,t)=>U.reduce((q,x,j)=>q+x*U[mod(t-j,10)],0));
const v=Array.from({length:11},(_,t)=>V.reduce((q,x,j)=>q+x*V[mod(t-j,11)],0));
return a.flatMap(x=>v.map(y=>2*(U.reduce((p,q)=>p+q,0)*V.reduce((p,q)=>p+q,0)-x*y))).join(',')}
const fibers=new Map();for(const s of states.values()){const k=spec(s);if(!fibers.has(k))fibers.set(k,[]);fibers.get(k).push(s)}
const pairs=[];for(const f of fibers.values()){
must(f.length===1||f.length===2,'spectrum fiber');
if(f.length===2){must(f[0].z===f[1].z,'pair factor');
pairs.push({G:f[0].u^f[1].u,z:f[0].z,H:Math.max(f[0].b,f[1].b)})}}
must(fibers.size===478&&pairs.length===122,'pair census');
const mask=a=>a.reduce((m,j)=>m|1<<j,0);
const groups=[{id:'A',rows:[1,4,6,9]},{id:'B',rows:[2,7]},{id:'C',rows:[3,8]}].map(g=>({...g,G:mask(g.rows)}));
must(groups.every(g=>pairs.some(p=>p.G===g.G&&p.H<=22)),'early minimal group');
must([...new Set(pairs.map(p=>p.G))].every(G=>groups.some(g=>(G&g.G)===g.G)),'support inclusion');
const cert={
5:{46:[0,0,320,17,528,0,512,336,81,528],51:[0,0,320,80,0,0,1031,336,81,264],53:[0,0,0,65,0,0,4,655,81,1441]},
6:{46:[0,512,336,81,528,0,512,336,81,528],51:[0,0,336,81,0,0,1543,336,81,264],53:[0,0,80,81,0,0,68,625,81,1952]},
7:{41:[0,528,336,1089,512,0,528,337,1091,528],45:[0,512,320,19,528,0,528,993,83,528],46:[0,512,320,80,528,0,528,1896,1904,528]},
8:{41:[0,528,337,1091,528,0,528,337,1091,528],45:[0,528,272,83,528,0,528,1849,83,528],46:[0,528,320,80,528,0,528,2024,1906,528]},
9:{35:[0,529,305,29,512,0,529,817,93,528],37:[0,0,785,89,512,0,648,817,91,870],43:[0,528,336,1112,512,0,696,379,1113,768]},
10:{35:[0,529,817,93,528,0,529,817,93,528],37:[0,0,817,91,512,0,664,817,91,870],43:[0,528,336,1113,512,0,760,891,1113,768]}};
const layout=masks=>masks.flatMap((m,j)=>Array.from({length:11},(_,z)=>(m>>z&1)?[j,z]:null).filter(Boolean));
const uniform=r=>[1,2,3].flatMap(j=>Array.from({length:r+1},(_,z)=>[j,z]));
const holes=(G,H)=>new Set(pairs.filter(p=>p.G===G&&p.H<=H&&p.z!==null).map(p=>p.z));
const lower=(H,r)=>3*r+groups.reduce((s,g)=>s+Number(r>g.rows.length*(11-holes(g.G,H).size)),0);
const dist=(s,p)=>s.reduce((v,[j,z])=>v+Number((p.G>>j&1)!==0&&p.z!==z),0);
const steps={};let comparisons=0,cases=0;
for(let r=5;r<=10;r++){let prior=-1;steps[r]=[];
for(let H=22;H<=139;H++){
const ends=Object.keys(cert[r]).map(Number).sort((a,b)=>a-b),end=ends.find(x=>x>=H);
const sites=end===undefined?uniform(r):layout(cert[r][end]),low=lower(H,r);
must(sites.length===low,`cost H=${H} r=${r}`);
must(new Set(sites.map(p=>p.join(','))).size===sites.length,'duplicate site');
for(const p of pairs)if(p.H<=H){must(dist(sites,p)>=r,`distance H=${H} r=${r}`);comparisons++}
if(low!==prior){steps[r].push([H,low]);prior=low}cases++}}
let direct=0;for(const s of states.values())for(let t=0;t<110;t++){
const h=s.h0+s.a*(s.t0+t),n=s.n0+s.c*(s.t0+t);
must((P(h,n)&&mod(9*h+10*n,11)!==0)===((s.u>>(t%10)&1)!==0&&s.z!==t%11),'direct C11');direct++}
console.log(JSON.stringify({schema:'EC49FXX_EXACT_STAIRCASE_V1',pin:'BRC16943',result:'ALL_PASS',states:states.size,spectra:fibers.size,equal_spectrum_pairs:pairs.length,original_C11_checks:direct,height_distance_cases:cases,layout_pair_comparisons:comparisons,explicit_endpoint_witnesses:18,transitions:steps,certificates:cert,review:'NOT_REVIEWED',native_transfer:'NOT_CLAIMED'},null,2));
