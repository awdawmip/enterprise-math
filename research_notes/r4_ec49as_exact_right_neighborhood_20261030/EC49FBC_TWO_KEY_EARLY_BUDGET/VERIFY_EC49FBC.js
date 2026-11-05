'use strict';
// EC49FBC exact exhaustive signed-native-X6 H4/H5 mixed-key DP.
// Input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
const OPS={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]},L='acdefg';
const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]], S=[0,0,4,1,16,32,8,2,0];
const EARLY=['de','ec','fe','feg','gef'];
const pin='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab';
function prim(w){return [...w].flatMap(c=>OPS[c]);}
function kd(w){let k=[0,0,0,0,0,0],d=[0,0,0,0,0,0];for(let n of prim(w)){let i=Math.abs(n)-1;if(n>0)k[i]++;d[i]+=(n>0?1:-1);}return {key:k.join(','),delta:d.join(',')};}
function obs(w){let s=0;for(let c of w)s=T[s][L.indexOf(c)];return S[s];}
function pref(w){let p='',a=[];for(let n of prim(w)){p+=String.fromCharCode(75+n);a.push(p);}return a;}
function rank9(m){return !!((m&18)&&(m&20)&&(m&33)&&(m&40));}
function getWords(h){let a=[];function walk(w){if(w.length<h){for(let c of L)walk(w+c);return;}let s=obs(w),{key,delta}=kd(w);if(s&&delta==='2,0,0,0,0,0')a.push({w,s,key,p:pref(w)});}walk('');return a;}
const words={4:getWords(4),5:getWords(5)};
const old=[...new Set(EARLY.map(w=>kd(w).key))].sort(),free=new Set(EARLY.flatMap(pref));
if(old.length!==2||free.size!==31||words[4].length!==206||words[5].length!==1062)throw Error('baseline mismatch '+old+' '+free.size);
const newKeys=[...new Set([...words[4],...words[5]].map(w=>w.key))].filter(k=>!old.includes(k)).sort();
const k9='6,4,1,0,0,0';
if(newKeys.filter(k=>{let [x,y]=k.split(',').map(Number);return x+y>=10}).join()!==k9)throw Error('H9 key early mismatch');
const fixedSignatures={2:EARLY.filter(w=>w.length===2).reduce((m,w)=>m|obs(w),0),3:EARLY.filter(w=>w.length===3).reduce((m,w)=>m|obs(w),0)};
if(!rank9(fixedSignatures[2])||!rank9(fixedSignatures[3]))throw Error('early rank mismatch');
function solve(allowed){
 const trie=[{children:new Map(),terminal:[],isFree:true}];
 for(let h of [4,5])for(let word of words[h]){
  if(!allowed.has(word.key))continue;
  let i=0;for(let p of word.p){let j=trie[i].children.get(p);if(j===undefined){j=trie.length;trie[i].children.set(p,j);trie.push({children:new Map(),terminal:[],isFree:free.has(p)})}i=j;}
  trie[i].terminal.push({m:word.s<<(h===4?0:6),w:word.w});
 }
 let joins=0;
 function dp(i){
   let node=trie[i];let st=new Map([[0,{cost:0,ws:[]}]]);
   for(let t of node.terminal){let v=st.get(t.m);if(!v||v.cost>0)st.set(t.m,{cost:0,ws:[t.w]});}
   for(let child of node.children.values()){
    let sub=dp(child),next=new Map();
    for(let [a,va] of st)for(let [b,vb] of sub){let m=a|b,c=va.cost+vb.cost; joins++;if(c<(next.get(m)?.cost??Infinity))next.set(m,{cost:c,ws:va.ws.concat(vb.ws)});}
    st=next;
   }
   if(i&&!node.isFree)for(let [m,v] of st)if(m)v.cost++;
   return st;
 }
 let root=dp(0),best=null;
 for(let [mask,v] of root)if(rank9(mask&63)&&rank9((mask>>6)&63)){
  let cost=31+v.cost;
  if(!best||cost<best.cost||(cost===best.cost&&mask<best.mask))best={cost,mask,selected:v.ws};
 }
 if(best){
  let all=EARLY.concat(best.selected);if(new Set(all.flatMap(pref)).size!==best.cost)throw Error('cost mismatch');
  best={cost:best.cost,mask4:best.mask&63,mask5:(best.mask>>6)&63,H4:best.selected.filter(w=>w.length===4).sort(),H5:best.selected.filter(w=>w.length===5).sort(),usedKeys:[...new Set(all.map(w=>kd(w).key))].sort()};
 }
 return {best,nodes:trie.length,rootStates:root.size,joins};
}
const single=newKeys.map(k=>({extra_key:k,...solve(new Set(old.concat([k])))}));
const feasible=single.filter(r=>r.best).sort((a,b)=>a.best.cost-b.best.cost||a.extra_key.localeCompare(b.extra_key));
const out={schema:'EC49FBC_FIXED_31_EDGE_H23_H45_SINGLE_ADDITIONAL_KEY',date:'2026-11-05',scientific_input_pin:pin,ops:OPS,T,S,early_words:EARLY,early_signature_masks:fixedSignatures,early_edges:free.size,old_keys:old,legal_counts:{H4:words[4].length,H5:words[5].length},new_key_count:newKeys.length,single_new:{tested:single.length,feasible:feasible.length,minimum:feasible[0]?.best.cost??null,best:feasible.filter(r=>r.best.cost===feasible[0].best.cost),rows:single},h9_necessary_key:'x+y>=10',early_h9_eligible_key:k9};
const pair=[]; const keyCandidates=newKeys.filter(k=>k!==k9);
for(let i=0;i<keyCandidates.length;i++)for(let j=i+1;j<keyCandidates.length;j++){
 const ka=keyCandidates[i],kb=keyCandidates[j];pair.push({additional_keys:[ka,kb],...solve(new Set(old.concat([ka,kb])))});
}
const pairFeasible=pair.filter(r=>r.best).sort((a,b)=>a.best.cost-b.best.cost);
out.two_new_reserved_h9={tested:pair.length,feasible:pairFeasible.length,minimum:pairFeasible[0]?.best.cost??null,best:pairFeasible.filter(r=>r.best.cost===pairFeasible[0].best.cost),rows:pair};
const pairPlusH9=[];
for(let i=0;i<keyCandidates.length;i++)for(let j=i+1;j<keyCandidates.length;j++){
 const ka=keyCandidates[i],kb=keyCandidates[j];pairPlusH9.push({additional_keys:[ka,kb,k9],...solve(new Set(old.concat([ka,kb,k9])))});
}
const plusFeasible=pairPlusH9.filter(r=>r.best).sort((a,b)=>a.best.cost-b.best.cost);
out.two_new_plus_early_h9={tested:pairPlusH9.length,feasible:plusFeasible.length,minimum:plusFeasible[0]?.best.cost??null,best:plusFeasible.filter(r=>r.best.cost===plusFeasible[0].best.cost),rows:pairPlusH9};
console.log(JSON.stringify(out,null,2));
