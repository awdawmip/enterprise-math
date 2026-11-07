'use strict';
// EC49FAY: exact signed-native-X6 H6--H9 primitive-prefix optimum.
// Frozen science fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
const OPS={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const LETTERS='acdefg';
const TRANS=[
 [1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],
 [3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],
 [6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]
];
const SIGNATURE=[0,0,4,1,16,32,8,2,0];
const WITNESS={
 2:['fe','ge'],3:['feg','gef'],
 4:['fegc','fegd','gefc','gefd'],
 5:['feggf','gefgf'],
 6:['fegccc','fegddd','gefccc','gefddd'],
 7:['fegccfg','fegddgf','gefccfg','gefddgf'],
 8:['feggfgfc','feggfgfd','gefgfgfc','gefgfgfd'],
 9:['feggfgfgf','gefgfgfgf']
};
function primitive(word){const v=[];for(const c of word){if(!OPS[c])throw Error('invalid operation');v.push(...OPS[c]);}return v;}
function observer(word){let s=0;for(const c of word)s=TRANS[s][LETTERS.indexOf(c)];return SIGNATURE[s];}
function cache(word){const x=[0,0,0,0,0,0],v=[0,0,0,0,0,0];for(const q of primitive(word)){let i=Math.abs(q)-1;if(q>0)x[i]++;v[i]+=Math.sign(q);}return {key:x,displacement:v};}
function prefixes(words){const seen=new Set();for(const w of words){let s='';for(const v of primitive(w)){s+=String.fromCharCode(75+v);seen.add(s);}}return seen;}
function rank9(mask){return !!((mask&18)&&(mask&20)&&(mask&33)&&(mask&40));}
function generate(h){const r=9-h,f=h-5,g=h-5;if(r<0||f<0||g<0)throw Error('h out of range');
 const counts={a:0,e:1,c:0,d:0,f,g},res=[];
 function walk(w,left){if(!left){const b=observer(w);if(b && ((h===9 && (b===16||b===32))||(h<9 && (b===1||b===2||b===4||b===8))))res.push({word:w,signature:b,steps:primitive(w)});return;}
 for(const c of LETTERS){if(!counts[c])continue;counts[c]--;walk(w+c,left-1);counts[c]++;}}
 for(let c=0;c<=r;c++){counts.c=c;counts.d=r-c;walk('',h);}
 return res;
}
function verify(){
 let allWords=[],hist={},allKeys=new Set(),allSignatures=0;
 for(let h=2;h<=9;h++){
   const ws=WITNESS[h],keys=new Set(),prefix=prefixes(allWords.concat(ws));let mask=0;
   for(const w of ws){if(w.length!==h)throw Error('word length');const v=cache(w);if(v.displacement.join(',')!=='2,0,0,0,0,0')throw Error('bad endpoint '+w);if(v.key.slice(3).some(Boolean))throw Error('unexpected axis');let bit=observer(w);if(!bit)throw Error('bad signature');keys.add(v.key.join(','));allKeys.add(v.key.join(','));mask|=bit;allSignatures|=bit;}
   if(!rank9(mask))throw Error('rank9 '+h);
   hist[h]={word_count:ws.length,signature_mask:mask,keys:[...keys].sort(),total_prefix_edges:prefix.size};
   allWords.push(...ws);
 }
 const earlyWords=[2,3,4,5].flatMap(h=>WITNESS[h]);
 const early=prefixes(earlyWords),total=prefixes(allWords);
 if(early.size!==38||total.size!==112||allKeys.size!==5||allSignatures!==63)throw Error('witness mismatch');
 const earlyKeys=[...new Set(earlyWords.map(w=>cache(w).key.join(',')))].sort();
 const lateKey='6,4,1,0,0,0';
 for(let h=6;h<=9;h++)for(const w of WITNESS[h])if(cache(w).key.join(',')!==lateKey)throw Error('late key mismatch');
 const trie=[{edges:new Map(),terminal:0,free:true}],perH={};
 for(let h=6;h<=9;h++){
  const words=generate(h);perH[h]=words.length;const shift=h===9?12:4*(h-6);
  for(const word of words){
    const v=cache(word.word);if(v.key.join(',')!==lateKey||v.displacement.join(',')!=='2,0,0,0,0,0')throw Error('generator invalid');
    let i=0,p='';
    for(const a of word.steps){p+=String.fromCharCode(75+a);let j=trie[i].edges.get(a);if(j===undefined){j=trie.length;trie[i].edges.set(a,j);trie.push({edges:new Map(),terminal:0,free:early.has(p)})}i=j;}
    const bit=h===9?(word.signature===16?1:2):({1:1,2:2,4:4,8:8}[word.signature]);
    trie[i].terminal|=bit<<shift;
  }
 }
 let joins=0,maxStates=0;
 function dp(i){
  const node=trie[i];let state=new Map([[0,0]]);
  if(node.terminal)state.set(node.terminal,0);
  for(const j of node.edges.values()){
    const sub=dp(j),next=new Map();
    for(const [a,c] of state)for(const [b,d] of sub){const m=a|b,v=c+d;joins++;if(v<(next.get(m)??Infinity))next.set(m,v);}
    state=next;
  }
  if(i&&!node.free)for(const [mask,cost]of state)if(mask)state.set(mask,cost+1);
  if(state.size>maxStates)maxStates=state.size;
  return state;
 }
 const opt=dp(0),optimum=opt.get((1<<14)-1);
 if(optimum!==74||total.size-early.size!==optimum)throw Error('exact optimum/witness mismatch');
 if(opt.get(15)!==32||opt.get(255)!==44)throw Error('partial DP check');
 return {schema:'EC49FAY_H6_H9_FIXED_EARLY_EXACT_OPTIMUM_V1',verified_date:'2026-11-05',
 source_science_pin:'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 predecessor:'EC49FAX@f67f2dbe6fb39372c0256fa1d51855cc2717fb9a',
 explicit_witness:WITNESS,global_cache_key_count:allKeys.size,early_cache_keys:earlyKeys,late_cache_key:lateKey,
 early_prefix_edges:early.size,per_horizon_witness:hist,witness_total_edges:total.size,
 selected_late_candidate_words:perH,signed_primitive_trie_nodes:trie.length,
 finite_or_masks:1<<14,root_states:opt.size,maximum_subtree_dp_states:maxStates,
 dp_state_merge_checks:joins,
 exact_cost_h6:opt.get(15),exact_cost_h6_h7:opt.get(255),
 exact_cost_h6_h7_h8:opt.get(4095),exact_cost_h6_h7_h8_h9:optimum,
 fixed_early_family_optimum:early.size+optimum,
 method:'Complete endpoint multiset generation, exact 9-state observer, native signed primitive-prefix trie, exact OR/min-plus DP.',
 admission:'AUTHOR_EXACT_FINITE_UNREVIEWED'};
}
if(typeof module!=='undefined'){module.exports={verify};if(require.main===module)console.log(JSON.stringify(verify(),null,2));}
