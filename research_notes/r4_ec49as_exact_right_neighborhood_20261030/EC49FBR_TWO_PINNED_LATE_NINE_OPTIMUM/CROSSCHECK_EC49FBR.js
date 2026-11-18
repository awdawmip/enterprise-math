#!/usr/bin/env node
// Independent witness check for EC49FBR explicit operation words.
const fs=require('fs');
const report=JSON.parse(fs.readFileSync(__dirname+'/EXACT_REPORT_EC49FBR.json','utf8'));
const primitives={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const trans=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
const label=[0,0,4,1,16,32,8,2,0];
const alph='acdefg';
const clause={1:[0],4:[1],8:[2],2:[3],16:[0,1],32:[2,3]};
const assert=(x,m)=>{if(!x)throw Error(m)};
for(const rec of report.records){
 const chosen=rec.chosen;const all=new Set();const keys=new Set();const late=rec.M.slice(0,3).join(',');const low=rec.L.slice(0,3).join(',');
 for(let h=2;h<=9;h++){
  const words=chosen[String(h)];assert(Array.isArray(words)&&words.length,h+' missing');const rank=new Set();
  for(const item of words){
   const w=item.word; assert(w.length===h,`bad window ${h}: ${w}`);
   let state=0, pref='', positive=new Array(6).fill(0), displacement=new Array(6).fill(0);
   for(const op of w){
     const at=alph.indexOf(op);assert(at>=0,'bad operation');state=trans[state][at];assert(state!==8,`reject path ${w}`);
     for(const axis of primitives[op]){
       pref+=axis+',';all.add(pref);
       if(axis>0)positive[axis-1]++;
       displacement[Math.abs(axis)-1]+=axis>0?1:-1;
     }
   }
   const sig=label[state];assert(sig===item.signature,`wrong signature ${h} ${w}`);
   assert(displacement.join(',')==='2,0,0,0,0,0',`wrong endpoint ${w}`);
   assert(positive.slice(3).every(v=>v===0),`wrong last three ${w}`);
   const key=positive.slice(0,3).join(',');keys.add(key);
   if(h===4||h===5)assert(key===low,`bad early key ${w}`);
   if(h>=6)assert(key===late,`bad late key ${w}`);
   assert(clause[sig],`bad observation ${w}`);
   clause[sig].forEach(x=>rank.add(x));
  }
  assert(rank.size===4 && [0,1,2,3].every(v=>rank.has(v)),`incomplete clauses ${h}`);
 }
 assert(keys.size===5,`key budget ${keys.size}`);
 assert(all.size===rec.complete_union_edges,`wrong cost ${all.size}!=${rec.complete_union_edges}`);
 console.log(JSON.stringify({M:late,all_prefix_edges:all.size,distinct_cache_keys:keys.size,windows:8,rankClauses:32,status:'PASS'}));
}
