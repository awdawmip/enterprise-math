'use strict';
/** Independent V8 implementation of exact EC49EP rank and native-prefix trie DP. */
const OPS={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const TOKENS=Object.keys(OPS), STATES=[['N',0],['N',1],['N',2],['A',0],['A',2],['B',0],['B',1],['AB',0],['BA',0]], OUTPUT=['N','A','B','AB','BA'];
const MOD=1000003;
function native(w){return [...w].flatMap(c=>OPS[c]);}
function key(w){let a=native(w);return Array.from({length:6},(_,j)=>a.filter(x=>x===j+1).length).join(',');}
function returning(w){const a=native(w);return [1,2,3,4,5,6].every(j=>a.filter(x=>x===j).length-a.filter(x=>x===-j).length===(j===1?2:0));}
function observe(w){const p=native(w);return STATES.map(([start,old])=>{
  let s=start,l=old;
  for(const x of p){if(l===1 && x===2){if(s==='N')s='A';else if(s==='B')s='BA';}
    if(l===2 && x===1){if(s==='N')s='B';else if(s==='A')s='AB';} l=x;}
  return OUTPUT.indexOf(s);
});}
function signature(w){return observe(w).join(',');}
function modpow(a,e){let p=1;while(e){if(e%2)p=p*a%MOD;a=a*a%MOD;e=Math.floor(e/2);}return p;}
function rank(sigs){const piv=Array(9).fill(null);let r=0;
  for(const s of sigs){const arr=s.split(',').map(Number);
    for(let b=0;b<5;b++){const col=arr.map(q=>Number(q===b));
      for(let i=0;i<9;i++){let z=col[i];if(z===0)continue;
        if(piv[i]){for(let j=i;j<9;j++)col[j]=((col[j]-z*piv[i][j])%MOD+MOD)%MOD;}
        else{const inv=modpow(z,MOD-2);piv[i]=col.map(x=>x*inv%MOD);r++;break;}
      }
    }
  }return r;}
function paths(h){let xs=[''];for(let j=0;j<h;j++)xs=xs.flatMap(x=>TOKENS.map(k=>x+k));return xs.filter(returning);}
const H={2:paths(2),3:paths(3),4:paths(4)};
const fibers={};for(let h=2;h<=4;h++){fibers[h]=new Map();for(const w of H[h]){const p=key(w);if(!fibers[h].has(p))fibers[h].set(p,[]);fibers[h].get(p).push(w);}}
function group(words){const g=new Map();for(const w of words){const t=signature(w);if(!g.has(t))g.set(t,[]);g.get(t).push(w);}return g;}
function minimalSets(sigs){const n=sigs.length,ans=[];
  for(let mask=1;mask<(1<<n);mask++){const sub=sigs.filter((s,i)=>(mask>>i)&1);
    if(rank(sub)===9 && sub.every(s=>rank(sub.filter(x=>x!==s))!==9))ans.push(sub);}
  return ans;}
function options3(p){const g=group(fibers[3].get(p)),out=[];
  function expand(ss,k,ws){if(k===ss.length){out.push(ws);return;}for(const w of g.get(ss[k]))expand(ss,k+1,ws.concat(w));}
  for(const ss of minimalSets([...g.keys()]))expand(ss,0,[]);return out;}
function prefixSet(words){let set=new Set();for(const w of words){let p=[];for(const x of native(w)){p.push(x);set.add(p.join(':'));}}return set;}
function trie(words){const root={children:new Map(),end:[]};for(const w of words){let t=root;for(const x of native(w)){
    if(!t.children.has(x))t.children.set(x,{children:new Map(),end:[]});t=t.children.get(x);}
    t.end.push(w);}return root;}
function dp(root,prior,sigs){const ids=new Map(sigs.map((s,i)=>[s,i]));
  function recurse(node,steps){let d=new Map([[0,{edges:0,words:[]}] ]);
    for(const w of node.end){const flag=1<<ids.get(signature(w));if(!d.has(flag))d.set(flag,{edges:0,words:[w]});}
    for(const [x,child] of node.children){const sub=recurse(child,steps.concat(x));const dest=new Map();
      for(const [a,pa] of d)for(const [b,pb] of sub){const m=a|b;
        const edges=pa.edges+pb.edges+(b===0 || prior.has(steps.concat(x).join(':'))?0:1);
        const prev=dest.get(m);if(!prev||edges<prev.edges)dest.set(m,{edges,words:pa.words.concat(pb.words)});}
      d=dest;
    }return d;
  }return recurse(root,[]);}
const base=['ce','de','ec','ed'], p0=key('ce');
if(H[2].length!==8||H[3].length!==51||H[4].length!==304||rank(base.map(signature))!==9||prefixSet(base).size!==28)throw Error('BASE_FAILED');
if(fibers[4].has(p0))throw Error('p0 appears at h4');
const p3full=[...fibers[3]].filter(([,ws])=>rank([...group(ws).keys()])===9).map(([p])=>p);
const p4full=[...fibers[4]].filter(([,ws])=>rank([...group(ws).keys()])===9).map(([p])=>p);
let cases=[],byS=new Map(),byMS=new Map(),nH3=0;
// All four h3 rank-nine p classes crossed with all nine h4 rank-nine p
// classes. Every fixed-p fiber is exactly enumerated, and all h4 transfer
// masks are evaluated by an independent signed-step weighted-prefix trie DP.
for(const p3 of p3full)for(const p4 of p4full){
  const label=p3===p0?'A':p3===p4?'B':'C', M=new Set([p0,p3,p4]).size;
  const gs=group(fibers[4].get(p4)),sig=[...gs.keys()],root=trie(fibers[4].get(p4)),masks=[];
  for(let m=1;m<1<<sig.length;m++)if(rank(sig.filter((_,i)=>m>>i&1))===9)masks.push(m);
  let minimum=new Map(),num3=0;
  for(const ws3 of options3(p3)){num3++;nH3++;const prev=prefixSet(base.concat(ws3)),t=dp(root,prev,sig);
    for(const m of masks){if(!t.has(m))continue;
      const value=t.get(m),e=prev.size+value.edges;
      const S=new Set(base.concat(ws3).map(signature).concat(sig.filter((_,i)=>(m>>i)&1))).size;
      const old=minimum.get(S);if(old===undefined||e<old)minimum.set(S,e);
      const ms=`${M}:${S}`;const ms0=byMS.get(ms);if(ms0===undefined||e<ms0)byMS.set(ms,e);
      if(M===2){const b=byS.get(S);if(b===undefined||e<b)byS.set(S,e);}
    }
  }
  cases.push({case:label,M,p3,p4,h3_options:num3,signature_types:sig.length,best:Object.fromEntries([...minimum].sort((a,b)=>a[0]-b[0]))});
}
const expected=JSON.stringify([[4,56],[6,46],[7,51],[8,74],[9,78],[10,82]]);
const actual=JSON.stringify([...byS].sort((a,b)=>a[0]-b[0]));
if(actual!==expected)throw Error(`DP disagreement ${actual}`);
const expectedAll={'2:4':56,'2:6':46,'2:7':51,'2:8':74,'2:9':78,'2:10':82,'3:4':44,'3:5':56,'3:6':54,'3:7':59,'3:8':68};
if(JSON.stringify(Object.fromEntries([...byMS].sort()))!==JSON.stringify(Object.fromEntries(Object.entries(expectedAll).sort())))throw Error('GLOBAL_M_S_TABLE_FAILED');
if(cases.length!==36||nH3!==1224)throw Error('FULL_CASE_COVERAGE_FAILED');
const examples=[
  {words:[base,['cef','def','ecf','edf'],['ceff','deff','ecff','edff']],target:[44,3,4]},
  {words:[base,['feg','gef'],['fegg','gefg']],target:[46,2,6]},
  {words:[base,['cec','ded','ecc','edd'],['cefg','degf','ecfg','edgf']],target:[56,2,4]}
];
for(const ex of examples){const ws=ex.words.flat(),e=prefixSet(ws).size,m=new Set(ws.map(key)).size,s=new Set(ws.map(signature)).size;
  if(JSON.stringify([e,m,s])!==JSON.stringify(ex.target))throw Error('WITNESS_RESOURCE_MISMATCH');
  for(const sub of ex.words){if(rank(sub.map(signature))!==9||new Set(sub.map(key)).size!==1||sub.some(w=>!returning(w)))throw Error('WITNESS_OBSERVER_MISMATCH');}
}
const multiH=[];
for(const Hmax of [3,4,5,6,8,16,32,64]){
  const horizonWords=[base],all=[...base];
  for(let h=3;h<=Hmax;h++){
    const ww=['feg'+'f'.repeat(h-3),'gef'+'f'.repeat(h-3)];
    if(rank(ww.map(signature))!==9||new Set(ww.map(key)).size!==1||ww.some(w=>!returning(w)))throw Error('NESTED_FAIL');
    all.push(...ww);horizonWords.push(ww);
  }
  const triple=[prefixSet(all).size,new Set(all.map(key)).size,new Set(all.map(signature)).size];
  if(JSON.stringify(triple)!==JSON.stringify([4*Hmax+30,Hmax-2,6]))throw Error('NESTED_TRIPLE_FAIL');
  multiH.push([Hmax,...triple]);
}
console.log(JSON.stringify({unit:'EC49EP',status:'PASS',implementation:'Independent JS/V8 native trie dynamic programming',
  word_counts:Object.fromEntries([2,3,4].map(h=>[h,H[h].length])),full_rank_fibers:{h3:p3full.length,h4:p4full.length},
  total_cases:cases.length,total_h3_options:nH3,minimum_by_M_S:Object.fromEntries([...byMS].sort()),minimum_by_S:Object.fromEntries([...byS].sort((a,b)=>a[0]-b[0])),
  frontier:examples.map(x=>x.target),nested_family_checks:multiH,all_case_minima:cases,rank_modulus:MOD,hadamard_bound:3**9},null,2));