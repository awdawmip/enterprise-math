'use strict';
// EC49FBB exact exhaustive signed-native-X6 H4/H5 mixed-key DP.
// Input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
const run=function research(){
const OPS={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]},L='acdefg';
const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]], S=[0,0,4,1,16,32,8,2,0];
const EARLY=['fe','ge','feg','gef'],pin='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab';
function prim(w){return [...w].flatMap(c=>OPS[c])}
function kd(w){let k=[0,0,0,0,0,0],d=[0,0,0,0,0,0];for(let n of prim(w)){let i=Math.abs(n)-1;if(n>0)k[i]++;d[i]+=(n>0?1:-1)}return {key:k.join(','),delta:d.join(',')}}
function obs(w){let s=0;for(let c of w)s=T[s][L.indexOf(c)];return S[s]}
function pref(w){let p='',a=[];for(let n of prim(w)){p+=String.fromCharCode(75+n);a.push(p)}return a}
function rank9(m){return !!((m&18)&&(m&20)&&(m&33)&&(m&40))}
const words={4:[],5:[]};
for(let h of [4,5]){function walk(w){if(w.length<h){for(let c of L)walk(w+c);return}let s=obs(w),{key,delta}=kd(w);if(s&&delta==='2,0,0,0,0,0')words[h].push({w,s,key,p:pref(w)})}walk('')}
const old=[...new Set(EARLY.map(w=>kd(w).key))],free=new Set(EARLY.flatMap(pref));
if(old.length!==3||free.size!==16||words[4].length!==206||words[5].length!==1062)throw Error('frozen baseline mismatch');
const newKeys=[...new Set([...words[4],...words[5]].map(w=>w.key))].filter(k=>!old.includes(k)).sort(), k9='6,4,1,0,0,0';
const longKeys=newKeys.filter(k=>{let [x,y]=k.split(',').map(Number);return x+y>=10});
if(longKeys.join('!')!==k9)throw Error('unexpected early-usable H9 key '+longKeys);
function solve(allowed){
const trie=[{children:new Map(),terminal:[],isFree:true}];
for(let h of [4,5])for(let word of words[h]){if(!allowed.has(word.key))continue;
 let i=0;for(let p of word.p){let j=trie[i].children.get(p);if(j===undefined){j=trie.length;trie[i].children.set(p,j);trie.push({children:new Map(),terminal:[],isFree:free.has(p)})}i=j;}
 trie[i].terminal.push({m:word.s<<(h===4?0:6),w:word.w});
}
let joins=0;
function dp(i){
 const node=trie[i];let st=new Map([[0,{cost:0,ws:[]}]]);
 for(let t of node.terminal){let v=st.get(t.m);if(!v||v.cost>0)st.set(t.m,{cost:0,ws:[t.w]});}
 for(let child of node.children.values()){
  const sub=dp(child),next=new Map();
  for(let [a,va] of st)for(let [b,vb] of sub){
   const m=a|b,c=va.cost+vb.cost;joins++;
   if(c<(next.get(m)?.cost??Infinity))next.set(m,{cost:c,ws:va.ws.concat(vb.ws)});
  }st=next;
 }
 if(i&&!node.isFree)for(let [m,v] of st)if(m)v.cost++;
 return st;
}
const root=dp(0);let best=null;
for(let [mask,v] of root)if(rank9(mask&63)&&rank9((mask>>6)&63)){
 const cost=16+v.cost;
 if(!best||cost<best.cost||(cost===best.cost && mask<best.mask))best={cost,mask,selected:v.ws};
}
if(best){
 let all=EARLY.concat(best.selected);if(new Set(all.flatMap(pref)).size!==best.cost)throw Error('signed-prefix witness cost');
 for(let w of best.selected){let {key,delta}=kd(w);if(!allowed.has(key)||delta!=='2,0,0,0,0,0'||!obs(w))throw Error('witness semantics')}
 best={cost:best.cost,mask4:best.mask&63,mask5:(best.mask>>6)&63,H4:best.selected.filter(w=>w.length===4).sort(),H5:best.selected.filter(w=>w.length===5).sort(),usedKeys:[...new Set(all.map(w=>kd(w).key))].sort()};
}
return {best,nodes:trie.length,rootStates:root.size,joins};
}
const one=[],two=[];
for(let k of newKeys){
 one.push({new_key:k,...solve(new Set(old.concat([k])))});
 if(k!==k9)two.push({new_key:k,...solve(new Set(old.concat([k,k9])))});
}
const eligible=r=>r.filter(x=>x.best).sort((a,b)=>a.best.cost-b.best.cost||a.new_key.localeCompare(b.new_key));
const a=eligible(one),b=eligible(two);
if(a.length!==7||b.length!==9||a[0].best.cost!==38||b[0].best.cost!==38)throw Error('census mismatch');
return {schema:'EC49FBB_FIXED_H23_MIXED_H45_H9_KEY_BUDGET_V1',model:'signed native X6, positive-step six-component complete cache keys, endpoint (+2,0,0,0,0,0), nine-state observer, six allowed signatures, rational rank9',scientific_input_pin:pin,ops:OPS,T,S,alphabet:L,early_words:EARLY,legal_counts:{H4:words[4].length,H5:words[5].length},early_keys:old,early_usable_new_keys:newKeys,H9_key_reusable_during_H45:longKeys,one_new:{tested:one.length,feasible:a.length,minimum:a[0].best.cost,optima:a.filter(r=>r.best.cost===a[0].best.cost),rows:one},two_new_with_H9_key:{tested:two.length,feasible:b.length,minimum:b[0].best.cost,optima:b.filter(r=>r.best.cost===b[0].best.cost),rows:two}};
};
if(require.main===module)console.log(JSON.stringify(run(),null,2));
module.exports={run};
