'use strict';
// EC49FBA: exhaustive signed-X6 H4/H5 key schedules, with fixed H2/H3.
// Original scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
const OPS={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]}, L='acdefg';
const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
const S=[0,0,4,1,16,32,8,2,0], EARLY=['fe','ge','feg','gef'];
function primitive(w){return [...w].flatMap(c=>OPS[c]);}
function observer(w){let s=0;for(const c of w)s=T[s][L.indexOf(c)];return S[s];}
function keydelta(w){let key=[0,0,0,0,0,0],delta=[0,0,0,0,0,0];for(const x of primitive(w)){const i=Math.abs(x)-1;if(x>0)key[i]++;delta[i]+=Math.sign(x);}return {key,delta};}
function key(w){return keydelta(w).key.join(',');}
function pref(w){let p='',out=[];for(const x of primitive(w)){p+=String.fromCharCode(75+x);out.push(p);}return out;}
function rank9(mask){return Boolean((mask&18)&&(mask&20)&&(mask&33)&&(mask&40));}
const free=new Set(EARLY.flatMap(pref));if(free.size!==16)throw Error('early prefixes');
const D={4:new Map(),5:new Map()};
for(const h of [4,5]){
 function walk(w){if(w.length<h){for(const c of L)walk(w+c);return;}
  const signature=observer(w);if(!signature)return;
  const {key:k,delta}=keydelta(w);if(delta.join(',')!=='2,0,0,0,0,0')return;
  const code=k.join(',');if(!D[h].has(code))D[h].set(code,[]);
  D[h].get(code).push({w,s:signature,p:pref(w)});
 }
 walk('');
}
const feasible={};for(const h of [4,5])feasible[h]=[...D[h]].filter(([k,ws])=>rank9(ws.reduce((a,w)=>a|w.s,0))).map(([k])=>k).sort();
function optimize(k4,k5){
 const trie=[{children:new Map(),bits:0,words:[],free:true}];
 for(const [h,k] of [[4,k4],[5,k5]])for(const word of D[h].get(k)){
  let i=0;
  for(const p of word.p){const x=p.charCodeAt(p.length-1)-75;let j=trie[i].children.get(x);
   if(j===undefined){j=trie.length;trie[i].children.set(x,j);trie.push({children:new Map(),bits:0,words:[],free:free.has(p)});}i=j;
  }
  const bit=word.s<<(h===4?0:6);trie[i].bits|=bit;trie[i].words.push({w:word.w,bit});
 }
 function dp(i){const node=trie[i];let states=new Map([[0,{cost:0,ws:[]}]]) ;
  for(const {w,bit} of node.words)states.set(bit,{cost:0,ws:[w]});
  for(const j of node.children.values()){
   const sub=dp(j),next=new Map();
   for(const [a,va] of states)for(const [b,vb] of sub){const m=a|b,c=va.cost+vb.cost;
    if(c<(next.get(m)?.cost??Infinity))next.set(m,{cost:c,ws:va.ws.concat(vb.ws)});
   }
   states=next;
  }
  if(i&&!node.free)for(const [m,v] of states)if(m)v.cost++;
  return states;
 }
 let options=[];for(const [mask,v] of dp(0))if(rank9(mask&63)&&rank9((mask>>6)&63))options.push({cost:16+v.cost,mask,w4:v.ws.filter(x=>x.length===4).sort(),w5:v.ws.filter(x=>x.length===5).sort()});
 if(!options.length)throw Error('missing feasible schedule');options.sort((a,b)=>a.cost-b.cost||a.mask-b.mask);
 const best=options[0],witness=[...EARLY,...best.w4,...best.w5];
 const cost=new Set(witness.flatMap(pref)).size;
 if(cost!==best.cost)throw Error('witness mismatch '+k4+'/'+k5);
 for(const [k,ws] of [[k4,best.w4],[k5,best.w5]])for(const w of ws){let z=keydelta(w);if(z.key.join(',')!==k||z.delta.join(',')!=='2,0,0,0,0,0')throw Error('cache/endpoint witness');}
 return {key4:k4,key5:k5,edges:best.cost,words4:best.w4,words5:best.w5,mask4:best.mask&63,mask5:(best.mask>>6)&63};
}
function run(){const rows=[];for(const k4 of feasible[4])for(const k5 of feasible[5])rows.push(optimize(k4,k5));
 rows.sort((a,b)=>a.edges-b.edges||a.key4.localeCompare(b.key4)||a.key5.localeCompare(b.key5));
 const best=rows.filter(r=>r.edges===rows[0].edges);
 const same=rows.filter(r=>r.key4===r.key5),late=rows.filter(r=>r.key5==='6,4,1,0,0,0');
 const budget=rows.filter(r=>r.key4===r.key5||r.key5==='6,4,1,0,0,0');
 const old=rows.find(r=>r.key4==='4,2,1,0,0,0'&&r.key5==='4,2,1,0,0,0');
 if(feasible[4].length!==9||feasible[5].length!==17||rows.length!==153||best.length!==4||best[0].edges!==24||old.edges!==38||budget[0].edges!==38||late[0].edges!==90)throw Error('exact census mismatch');
 return {schema:'EC49FBA_FIXED_H23_H45_SINGLE_KEY_EACH_EXACT_V1',science_pin:'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',scope:'fixed H2/H3; one complete positive-step cache key per H4 and H5; all native endpoint +2 and rank nine',feasible_key_counts:{4:feasible[4].length,5:feasible[5].length},feasible_keys:feasible,schedules:rows.length,overall_min:rows[0].edges,overall_optima:best,same_key_schedules:same.length,same_key_min:same[0].edges,late_reusable_h5_schedules:late.length,late_reusable_h5_min:late[0],budget_necessary_schedules:budget.length,budget_necessary_min:budget[0].edges,baseline_421:old,all_schedule_costs:rows.map(r=>({k4:r.key4,k5:r.key5,edges:r.edges}))};
}
if(require.main===module)console.log(JSON.stringify(run(),null,2));
module.exports={run};
