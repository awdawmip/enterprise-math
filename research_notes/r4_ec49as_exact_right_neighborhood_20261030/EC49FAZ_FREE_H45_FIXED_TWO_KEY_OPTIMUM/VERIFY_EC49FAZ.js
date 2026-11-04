'use strict';
// EC49FAZ: exact signed-native-X6 H4--H9 primitive-prefix optimum.
const OPS={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const LETTERS='acdefg';
const TRANS=[
 [1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],
 [3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],
 [6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]
];
const SIGNATURE=[0,0,4,1,16,32,8,2,0];
const ROOT={2:['fe','ge'],3:['feg','gef']};
const KEYS={4:[4,2,1],5:[4,2,1],6:[6,4,1],7:[6,4,1],8:[6,4,1],9:[6,4,1]};
const SHIFTS={4:0,5:4,6:6,7:10,8:14,9:18};
const REQUIRED={4:15,5:3,6:15,7:15,8:15,9:3};
function primitive(word){return [...word].flatMap(c=>OPS[c]);}
function observer(word){let s=0;for(const c of word)s=TRANS[s][LETTERS.indexOf(c)];return SIGNATURE[s];}
function cache(word){let k=new Array(6).fill(0),d=new Array(6).fill(0);for(const s of primitive(word)){let i=Math.abs(s)-1;if(s>0)k[i]++;d[i]+=Math.sign(s);}return {key:k,delta:d};}
function prefixes(words){let set=new Set();for(const w of words){let p='';for(let s of primitive(w)){p+=String.fromCharCode(75+s);set.add(p);}}return set;}
function generate(h,K){const [x,y,z]=K, r=x+y-h-1,f=h+1-y-2*z,g=h+1-x;
 if(r<0||f<0||g<0||z<1)return [];
 let res=[];const counts={a:z-1,e:z,c:0,d:0,f,g};
 function dfs(w,left){if(!left){let signature=observer(w);if(signature)res.push({word:w,signature,steps:primitive(w)});return;}
 for(const op of LETTERS){if(!counts[op])continue;counts[op]--;dfs(w+op,left-1);counts[op]++;}}
 for(let c=0;c<=r;c++){counts.c=c;counts.d=r-c;dfs('',h)}
 return res;}
function terminal_bit(h,s){const target=h===5||h===9?[16,32]:[1,2,4,8];let i=target.indexOf(s);return i>=0?(1<<(SHIFTS[h]+i)):0;}
function run(){let fixed=ROOT[2].concat(ROOT[3]);let free=prefixes(fixed);
 if(free.size!==16)throw Error('early edges mismatch');
 let trie=[{children:new Map(),bits:0,free:true}],counts={},sig={};
 for(let h=4;h<=9;h++){
  const all=generate(h,KEYS[h]);counts[h]=all.length;sig[h]={};
  for(let a of all){let bit=terminal_bit(h,a.signature);if(!bit)continue;
    sig[h][a.signature]=(sig[h][a.signature]||0)+1;
    const c=cache(a.word);if(c.delta.join(',')!=='2,0,0,0,0,0'||c.key.join(',')!==[...KEYS[h],0,0,0].join(','))throw Error('invalid generated '+a.word);
    let i=0,p='';for(let q of a.steps){p+=String.fromCharCode(75+q);let j=trie[i].children.get(q);if(j===undefined){j=trie.length;trie[i].children.set(q,j);trie.push({children:new Map(),bits:0,free:free.has(p),parent:i,step:q,depth:trie[i].depth+1||1});}i=j;}
    trie[i].bits|=bit;
  }
 }
 const full=(1<<20)-1;let merges=0,maxSize=0;
 function dp(v){let node=trie[v],states=new Map([[0,0]]);
   if(node.bits)states.set(node.bits,0);
   for(const j of node.children.values()){
      const sub=dp(j), next=new Map();
      for(const [a,ca] of states)for(const [b,cb] of sub){const x=a|b,y=ca+cb;merges++;if(y<(next.get(x)??Infinity))next.set(x,y);}
      states=next;
   }
   if(v&&!node.free)for(const [mask,cost] of states)if(mask)states.set(mask,cost+1);
   maxSize=Math.max(maxSize,states.size);
   return states;
 }
 const states=dp(0);const min=states.get(full);let targets={};for(let h=4;h<=9;h++){let mask=0;for(let j=4;j<=h;j++)mask|=REQUIRED[j]<<SHIFTS[j];targets[h]=states.get(mask)??null;}
 return {schema:'EC49FAZ_H23_FIXED_H45_KEY4_H69_KEY5_DP_V1',science_pin:'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',fixed_h2_h3:ROOT,late_cache_keys:KEYS,signature_mask_positions:SHIFTS,eligible_per_window:counts,eligible_signatures_per_window:sig,first_two_edges:free.size,trie_nodes:trie.length,state_merges:merges,max_subtree_states:maxSize,root_states:states.size,optimal_new_edges:min,optimal_total_edges:min===undefined?null:free.size+min,stage_marginals:targets};
}
if(require.main===module)console.log(JSON.stringify(run(),null,2));
module.exports={run,generate,observer,primitive,cache,prefixes,terminal_bit,ROOT,KEYS};
