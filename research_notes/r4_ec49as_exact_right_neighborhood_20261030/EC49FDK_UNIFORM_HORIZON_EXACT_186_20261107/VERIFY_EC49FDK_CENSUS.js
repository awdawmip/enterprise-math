#!/usr/bin/env node
'use strict';
// Reproduce exact key/signature schedule census and verify FD K certificate (not a numeric DP replay).
const fs=require('fs'),crypto=require('crypto'),zlib=require('zlib');
const FDJ=require('../EC49FDJ_ONE_SWITCH_RANK9_174_20261107/VERIFY_EC49FDJ.js');
const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],
  [3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],
  [6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
const SIG=[0,0,4,1,16,32,8,2,0],MASKS=new Map();
const rank=m=>Boolean((m&18)&&(m&20)&&(m&33)&&(m&40));
function mask(h,key){
  const id=String(h)+':'+key;if(MASKS.has(id))return MASKS.get(id);
  const [x,y,z]=key.split(',').map(Number),b=x+y-h-1;
  let result=0,counts=[z-1,0,b,z,h+1-y-2*z,h+1-x];
  if(counts.some(t=>t<0)){MASKS.set(id,0);return 0}
  function dfs(n,s){
    if(n===h){result|=SIG[s];return}
    for(let i=0;i<6;i++)if(counts[i]>0 && T[s][i]!==8){
      counts[i]--;dfs(n+1,T[s][i]);counts[i]++;
    }
  }
  for(let c=0;c<=b;c++){counts[1]=c;counts[2]=b-c;dfs(0,0);}
  MASKS.set(id,result);return result;
}
function run(){
 const r=FDJ.compute();
 if(r.rank9_cover_pairs!==124||r.distinct_one_switch_assignments!==174)throw Error('FDJ changed');
 const all=[],oneSwitch=[];let fullSlots=0;
 const REQ={4:15,5:48,6:15,7:15,8:15,9:48};
 for(const p of r.all_rank9_pairs){
  const choices=[];
  for(let h=4;h<=9;h++){
    const c=[];if(rank(mask(h,p.early)))c.push('E');if(rank(mask(h,p.late)))c.push('L');
    if(!c.length)throw Error('Rank gap');choices.push(c);
  }
  function rec(h,s){
    if(h===6){
      const row={E:p.early.split(',').map(Number),L:p.late.split(',').map(Number),S:s};
      all.push(row);if(!s.includes('LE'))oneSwitch.push(row);
      if([...s].every((t,i)=>(mask(i+4,t==='E'?p.early:p.late)&REQ[i+4])===REQ[i+4]))fullSlots++;
      return;
    }
    for(const k of choices[h])rec(h+1,s+k);
  }
  rec(0,'');
 }
 if(all.length!==186||oneSwitch.length!==174||fullSlots!==16)throw Error('Classification changed');
 const b64=fs.readFileSync(require('path').join(__dirname,'EXACT_CERTIFICATE_186.json.gz.b64'),'utf8').trim();
 const payload=zlib.gunzipSync(Buffer.from(b64,'base64'));
 const cert=JSON.parse(payload.toString('utf8'));
 const key=x=>x.E.join(',')+'/'+x.L.join(',')+'/'+x.S;
 const ids=new Set(all.map(key));
 if(cert.length!==186||new Set(cert.map(key)).size!==186||!cert.every(x=>ids.has(key(x))))throw Error('Certificate scope mismatch');
 const exact=cert.filter(x=>x.kind==='EXACT'),lb=cert.filter(x=>x.kind==='LB_DROP_H8');
 if(exact.length!==164||lb.length!==22||Math.min(...exact.map(x=>x.result))!==112||Math.min(...lb.map(x=>x.result))!==146)throw Error('Certificate values changed');
 const sha=crypto.createHash('sha256').update(payload).update('\n').digest('hex');
 if(sha!=='046182aabca3ecd3db638d66a4fa54cbe991006de95aa964579a396459bc19b6')throw Error('Certificate digest mismatch');
 console.log(JSON.stringify({key_pairs:124,one_switch:oneSwitch.length,uniform_schedules:all.length,designated_24_slot:fullSlots,exact_cases:exact.length,projected_cases:lb.length,min_exact:112,min_projected_bound:146,certificate_sha256:sha}));
}
run();
