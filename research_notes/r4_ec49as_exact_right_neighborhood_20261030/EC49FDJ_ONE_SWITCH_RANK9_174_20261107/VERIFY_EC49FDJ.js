#!/usr/bin/env node
'use strict';
const OP={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const A='acdefg',COUNT={a:[0,0,0],c:[1,1,0],d:[1,1,0],e:[2,0,1],f:[1,0,0],g:[0,1,0]};
const SEED=[[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[3,0],[4,0]];
const check=(v,m)=>{if(!v)throw Error(m)},TABLE={};
for(let c of A){let t=new Uint8Array(15);for(let v=0;v<15;v++){
 let s=Math.floor(v/3),p=v%3;
 for(let d of OP[c]){
  if(p===1&&d===2){if(s===0)s=1;else if(s===2)s=4;}
  else if(p===2&&d===1){if(s===0)s=2;else if(s===1)s=3;}
  p=d===1?1:d===2?2:0;
 }t[v]=3*s+p;
}TABLE[c]=t}
const INITIAL=Uint8Array.from(SEED.map(([s,p])=>s*3+p));
function step(v,c){let a=new Uint8Array(9),t=TABLE[c];for(let i=0;i<9;i++)a[i]=t[v[i]];return a}
function code(v){let n=0;for(let i=0;i<9;i++)n=5*n+Math.floor(v[i]/3);return n}
function sig(w){let v=INITIAL;for(let c of w)v=step(v,c);return code(v)}
const SIG=new Map(['de','ed','ce','ec','feg','gef'].map((w,i)=>[sig(w),1<<i]));
check(SIG.size===6,'Signature collision');
const rank=m=>!!((m&18)&&(m&20)&&(m&33)&&(m&40));
function census(h){let map=new Map(),valid=0,allowed=0;
 function dfs(n,b,x,y,z,v){
  if(Math.abs(1-b)>h-n)return;
  if(n===h){valid++;let m=SIG.get(code(v))||0;if(m){
   allowed++;let k=[x,y,z].join(',');map.set(k,(map.get(k)||0)|m);
  }return;}
  for(let c of A){let [dx,dy,dz]=COUNT[c];
   dfs(n+1,b+(c==='e')-(c==='a'),x+dx,y+dy,z+dz,step(v,c));
  }
 }dfs(0,0,0,0,0,INITIAL);
 return {map,valid,allowed};
}
function compute(){
 const M={},observations=[];
 for(let h=2;h<=9;h++){let d=census(h);M[h]=d.map;
  observations.push({h,endpoint_words:d.valid,allowed_words:d.allowed,allowed_keys:d.map.size,
   single_rank9_keys:[...d.map.values()].filter(rank).length});
 }
 check(observations.map(x=>x.endpoint_words).join(',')==='8,51,304,1770,10224,58947,340064,1964862','Endpoint census mismatch');
 check(observations.map(x=>x.allowed_words).join(',')==='6,38,206,1062,5352,26644,131686,647930','Observation census mismatch');
 let intervals=new Map();
 for(let x=0;x<=10;x++)for(let y=0;y<=10;y++)for(let z=1;z<=5;z++){
  let lo=Math.max(x-1,y+2*z-1),hi=x+y-1;
  if(Math.max(4,lo)<=Math.min(9,hi))intervals.set([x,y,z].join(','),[lo,hi]);
 }
 check(intervals.size===158,'Full-key census mismatch');
 const K=[...intervals.keys()].sort(),pairs=[];
 let raw=0,rankPairs=0,schedules=0;
 const boundary={4:0,5:0,6:0,7:0,8:0},numOptions={0:0,1:0,2:0,3:0,4:0},patterns={},perH={};
 for(let h=4;h<=9;h++)perH[h]={early_only:0,late_only:0,both:0};
 for(let i=0;i<K.length;i++)for(let j=i+1;j<K.length;j++){
  const k1=K[i],k2=K[j],a=intervals.get(k1),b=intervals.get(k2);
  if(![4,5,6,7,8,9].every(h=>(a[0]<=h&&h<=a[1])||(b[0]<=h&&h<=b[1])))continue;
  raw++;
  if(![4,5,6,7,8,9].every(h=>rank((M[h].get(k1)||0)|(M[h].get(k2)||0))))continue;
  rankPairs++;
  const early=rank(M[4].get(k1)||0)?k1:k2, late=early===k1?k2:k1;
  check(rank(M[4].get(early)||0)&&!rank(M[4].get(late)||0),'H4 early ambiguous');
  check(rank(M[9].get(late)||0)&&!rank(M[9].get(early)||0),'H9 late ambiguous');
  let pattern='';
  for(let h=4;h<=9;h++){
   let e=rank(M[h].get(early)||0),l=rank(M[h].get(late)||0);
   check(e||l,'Mixed-key rank indispensable');
   if(e&&l){pattern+='*';perH[h].both++}
   else if(e){pattern+='E';perH[h].early_only++}
   else{pattern+='L';perH[h].late_only++}
  }
  let options=[];
  for(let s=4;s<=8;s++)if([4,5,6,7,8,9].every(h=>rank(M[h].get(h<=s?early:late)||0))){
   options.push(s);boundary[s]++;
  }
  check(options.length>0,'No one-switch schedule');
  numOptions[options.length]++;schedules+=options.length;
  patterns[pattern]=(patterns[pattern]||0)+1;
  pairs.push({early,late,rank_pattern:pattern,switch_after:options});
 }
 check(raw===128&&rankPairs===124&&schedules===174,'Expected 128/124/174');
 check(JSON.stringify(numOptions)===JSON.stringify({0:0,1:84,2:31,3:8,4:1}),'Options distribution mismatch');
 check(JSON.stringify(boundary)===JSON.stringify({4:9,5:49,6:66,7:50,8:0}),'Switch boundary count mismatch');
 return {schema:'EC49FDJ_ONE_SWITCH_RANK9_NORMAL_FORM_V1',
   date:'2026-11-07',frozen_scientific_pin:'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
   model:'Frozen signed native X6 BRC nine-state observer, fixed H2-H3 seed, two full later BRC keys, six original signatures',
   raw_single_keys:intervals.size,endpoint_cover_pairs:raw,rank9_cover_pairs:rankPairs,
   single_key_rank9_every_horizon:true,one_switch_exists_for_each_pair:true,
   distinct_one_switch_assignments:schedules,options_per_pair_distribution:numOptions,
   switch_after_horizon_counts:boundary,per_horizon:perH,rank_pattern_counts:patterns,
   observation_census:observations,all_rank9_pairs:pairs,
   scope:'Finite rank-nine key-availability classification; not prefix-cost optimality'};
}
if(typeof module!=='undefined'){
 if(require.main===module)console.log(JSON.stringify(compute(),null,2));
 module.exports={compute};
}
