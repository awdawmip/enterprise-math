#!/usr/bin/env node
'use strict';
// Frozen EC49 model (scientific pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab).
// Author-side finite exact experiment: H2/H3 fixed, H9 key fixed (6,4,1),
// freely optimize H4-H6 using a single H4 key L plus K9; 5 full cache keys total.
const OPS={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const ORDER='acdefg';
const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],
[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],
[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
const S=[0,0,4,1,16,32,8,2,0], RANK=[18,20,33,40];
const EARLY={2:['fe','ge'],3:['feg','gef']}, HIGH='6,4,1,0,0,0', ALL=4095;
function native(w){return [...w].flatMap(c=>OPS[c]);}
function audit(w){let pos=[0,0,0,0,0,0],delta=[0,0,0,0,0,0],state=0;for(let c of w){state=T[state][ORDER.indexOf(c)];for(let n of OPS[c]){let i=Math.abs(n)-1;delta[i]+=n>0?1:-1;if(n>0)pos[i]++;}}return {key:pos.join(','),delta:delta.join(','),sig:S[state]};}
function fullRank(s){return RANK.every(v=>(s&v)!==0);}
function clause(s){return RANK.reduce((m,v,i)=>m|((s&v)?(1<<i):0),0);}
const valid={4:new Map(),5:new Map(),6:new Map()};
let allValid={4:0,5:0,6:0};
for(const h of [4,5,6]){
  function gen(w,pos,delta,st){if(w.length===h){if(delta[0]!==2||delta.slice(1).some(x=>x!==0)||S[st]===0)return;const k=pos.join(',');if(!valid[h].has(k))valid[h].set(k,[]);valid[h].get(k).push({w,sig:S[st]});allValid[h]++;return;}
    for(let i=0;i<ORDER.length;i++){let c=ORDER[i],p=pos.slice(),d=delta.slice();for(let n of OPS[c]){let k=Math.abs(n)-1;d[k]+=n>0?1:-1;if(n>0)p[k]++;}gen(w+c,p,d,T[st][i]);}}
  gen('',[0,0,0,0,0,0],[0,0,0,0,0,0],0);
}
const lowKeys=[...valid[4].entries()].filter(([k,words])=>fullRank(words.reduce((m,v)=>m|v.sig,0))).map(([k])=>k).sort();
function edges(words){const out=new Set();for(let w of words){let ns=native(w),s='';for(let a of ns){s+=a+',';out.add(s);}}return out;}
const baseWords=Object.values(EARLY).flat(), freeEdges=edges(baseWords);
function solve(low){const words={4:valid[4].get(low)||[],5:[...(valid[5].get(low)||[]),...(valid[5].get(HIGH)||[])],6:[...(valid[6].get(low)||[]),...(valid[6].get(HIGH)||[])]};
const nodes=[{ch:new Map(),term:0,terminal:[],free:true}];
function insert(w,mask,free){let v=0,ns=native(w);for(let step of ns){let child=nodes[v].ch.get(step);if(child===undefined){child=nodes.length;nodes[v].ch.set(step,child);nodes.push({ch:new Map(),term:0,terminal:[],free:false});}v=child;const key=ns.slice(0,ns.indexOf(step)+1); // free computed from fixed prefix set below
}if(mask){nodes[v].term|=mask;nodes[v].terminal.push(w);}}
for(const w of baseWords)insert(w,0,true);
for(let h=4;h<=6;h++)for(let {w,sig} of words[h])insert(w,clause(sig)<<(4*(h-4)),false);
// Mark free native edges by their exact signed prefix, not by operation spelling.
function mark(v,prefix){for(const [s,u] of nodes[v].ch){const p=prefix+s+',';nodes[u].free=freeEdges.has(p);mark(u,p);}}mark(0,'');
let dp=new Array(nodes.length),joins=0;
for(let u=nodes.length-1;u>=0;u--){let n=nodes[u],m=new Map([[0,0]]);if(n.term)m.set(n.term,0);
for(const child of n.ch.values()){let merged=new Map(),ch=dp[child];for(const [a,ca] of m)for(const [b,cb] of ch){let k=a|b,c=ca+cb;joins++;if(c<(merged.get(k)??1e8))merged.set(k,c);}m=merged;}
if(u!==0&&!n.free)for(const [a,c] of m)if(a)m.set(a,c+1);dp[u]=m;}
const cost=dp[0].get(ALL);
function reconstruct(u,target){let n=nodes[u],children=[...n.ch.values()];let rows=[new Map([[0,0]])];if(n.term)rows[0].set(n.term,0);for(let v of children){let m=new Map();for(const [a,ca] of rows.at(-1))for(const [b,cb] of dp[v]){let k=a|b,c=ca+cb;if(c<(m.get(k)??1e8))m.set(k,c);}rows.push(m);}
let mask=target;if(!n.free&&u&&mask){if(dp[u].get(target)!==rows.at(-1).get(target)+1)throw Error('edge');}let picked=[];
for(let i=children.length;i>=1;i--){let v=children[i-1],state=rows[i].get(mask),match=null;for(const [a,ca] of rows[i-1])for(const [b,cb] of dp[v])if((a|b)===mask&&ca+cb===state){match=[a,b];break;}
if(!match)throw Error('trace');picked.push(...reconstruct(v,match[1]));mask=match[0];}
if(mask){if(mask!==n.term||!n.terminal.length)throw Error('terminal');picked.push(n.terminal[0]);}return picked;}
const selected=(cost===undefined)?null:reconstruct(0,ALL);const cumulative=selected?edges([...baseWords,...selected]).size:null;
if(cost!==undefined&&cumulative!==freeEdges.size+cost)throw Error('backtrace_cost_mismatch');
if(selected){for(let h=4;h<=6;h++){let sig=0;for(let w of selected.filter(x=>x.length===h)){const a=audit(w);if(![low,HIGH].includes(a.key)||a.delta!=='2,0,0,0,0,0')throw Error('candidate mismatch');sig|=a.sig;}if(!fullRank(sig))throw Error('rank mismatch H'+h);}}
return {low_key:low,feasible:cost!==undefined,extra_edges:cost??null,total_edges:cumulative,word_counts:Object.fromEntries([4,5,6].map(h=>[h,words[h].length])),trie_nodes:nodes.length,joins,selected_words:selected?Object.fromEntries([4,5,6].map(h=>[h,selected.filter(w=>w.length===h).sort()])):null};}
const results=lowKeys.map(solve),best=results.filter(r=>r.feasible).sort((a,b)=>a.total_edges-b.total_edges)[0];
const report={schema:'EC49FBG_H456_5KEY_FIXED_H9_KEY_EXACT',scientific_pin:'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',assumptions:{fixed_H2:['fe','ge'],fixed_H3:['feg','gef'],fixed_H9_cache_key:[6,4,1,0,0,0],max_total_cache_keys:5,optimized_horizons:[4,5,6]},enumerated_legal_signature_words:allValid,early_prefix_edges:freeEdges.size,h4_rank9_cache_keys:lowKeys,results,best,status:'PASS'};
console.log(JSON.stringify(report,null,2));
