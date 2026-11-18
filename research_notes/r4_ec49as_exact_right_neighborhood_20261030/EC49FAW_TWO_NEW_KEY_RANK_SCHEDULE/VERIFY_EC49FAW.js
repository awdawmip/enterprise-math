#!/usr/bin/env node
'use strict';
function run(){
const OP={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]}, ALPH="acdefg";
const seed=[[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[3,0],[4,0]], add={a:[0,0,0],c:[1,1,0],d:[1,1,0],e:[2,0,1],f:[1,0,0],g:[0,1,0]};
const tables={};for(const c of ALPH){let t=new Uint8Array(15);for(let v=0;v<15;v++){let s=Math.floor(v/3),p=v%3;for(const step of OP[c]){if(p===1&&step===2){if(s===0)s=1;else if(s===2)s=4;}else if(p===2&&step===1){if(s===0)s=2;else if(s===1)s=3;}p=step===1?1:step===2?2:0;}t[v]=3*s+p;}tables[c]=t;}
const init=Uint8Array.from(seed.map(([s,p])=>3*s+p)),apply=(v,c)=>{let u=new Uint8Array(9),t=tables[c];for(let i=0;i<9;i++)u[i]=t[v[i]];return u;},code=v=>{let x=0;for(let i=0;i<9;i++)x=5*x+Math.floor(v[i]/3);return x;},signature=w=>{let v=init;for(const c of w)v=apply(v,c);return code(v);};
const SIG=new Map(["de","ed","ce","ec","feg","gef"].map((w,i)=>[signature(w),1<<i]));
if(SIG.size!==6)throw Error("signature collision");
const rank=m=>Boolean((m&18)&&(m&20)&&(m&33)&&(m&40));
const masks=[],observations=[];
for(let h=2;h<=9;h++){
let map=new Map(),legal=0,allowed=0;
function walk(n,b,x,y,z,v){if(Math.abs(1-b)>h-n)return;if(n===h){legal++;let m=SIG.get(code(v))||0;if(m){allowed++;const k=[x,y,z].join(",");map.set(k,(map.get(k)||0)|m);}return;}
for(const c of ALPH){const [dx,dy,dz]=add[c];walk(n+1,b+(c==="e")-(c==="a"),x+dx,y+dy,z+dz,apply(v,c));}}
walk(0,0,0,0,0,init);masks[h]=map;
const raw=[];for(let x=0;x<=10;x++)for(let y=0;y<=10;y++)for(let z=1;z<=5;z++){let lo=Math.max(x-1,y+2*z-1),hi=x+y-1;if(lo<=h&&h<=hi)raw.push([x,y,z].join(","));}
observations.push({h,legal,allowed,raw_keys:raw.length,allowed_keys:map.size,single_rank9_keys:[...map.values()].filter(rank).length,raw_without_allowed_observer:raw.filter(k=>!map.has(k))});
}
const intervals=new Map();for(let x=0;x<=10;x++)for(let y=0;y<=10;y++)for(let z=1;z<=5;z++){const lo=Math.max(x-1,y+2*z-1),hi=x+y-1;if(Math.max(lo,4)<=Math.min(hi,9))intervals.set([x,y,z].join(","),[lo,hi]);}
const keys=[...intervals.keys()].sort(),rawpairs=[],rankpairs=[],rejected=[];
for(let i=0;i<keys.length;i++)for(let j=i+1;j<keys.length;j++){
const a=keys[i],b=keys[j],u=intervals.get(a),v=intervals.get(b);
if(![4,5,6,7,8,9].every(h=>(u[0]<=h&&h<=u[1])||(v[0]<=h&&h<=v[1])))continue;
rawpairs.push([a,b]);const fail=[4,5,6,7,8,9].filter(h=>!rank((masks[h].get(a)||0)|(masks[h].get(b)||0)));
if(fail.length)rejected.push({pair:[a,b],failed_horizons:fail,H4_mask:(masks[4].get(a)||0)|(masks[4].get(b)||0)});else rankpairs.push([a,b]);}
return {schema:"EC49FAW_TWO_KEY_RANK_SCHEDULE_V1",date:"2026-11-05",scientific_pin:"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",source_frontier:"EC49FAV@be512db5ebe0d9d6b6d801824600c2a50abb13b4",key_box:[10,10,5],raw_single_key_count:keys.length,raw_cover_pair_count:rawpairs.length,rank9_cover_pair_count:rankpairs.length,observation_census:observations,rejected_pairs:rejected,raw_cover_pairs:rawpairs,rank9_cover_pairs:rankpairs,scope:"Finite per-horizon rank-nine feasibility only; simultaneous native-prefix edge minimization is open"};
}
console.log(JSON.stringify(run(),null,2));
