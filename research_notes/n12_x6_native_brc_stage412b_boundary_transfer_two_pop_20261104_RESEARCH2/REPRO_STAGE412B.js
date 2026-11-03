"use strict";
const chk=(v,m)=>{if(!v)throw Error(m)};
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const D="ABCDEFGHIJKL".split(""); // (A,B)=+/-E1; (C,D),...,(K,L)=+/-E2,...,+/-E6
function axis(c){const i=D.indexOf(c);chk(i>=0,"direction");return [Math.floor(i/2),i%2===0?1:-1]}
function endpoint(word){const z=Array(6).fill(0);for(const c of word){const [i,v]=axis(c);z[i]+=v}return z}
function fromStart(start,edges,counts){let z=endpoint(start);edges.forEach((e,i)=>{const [a,v]=axis(e[1]);z[a]+=v*counts[i]});return z}
function hist(w){const j={};for(let i=0;i+1<w.length;i++){const e=w.slice(i,i+2);j[e]=(j[e]||0)+1}return Object.keys(j).sort().map(e=>[e,j[e]])}
function obs(p,q){let k=0;for(let i=0;i<Math.min(p.length,q.length);i++)k+=p[i]===q[i]?1:0;return [p.length,q.length,endpoint(p),endpoint(q),hist(p),hist(q),k]}
function fiber(n){const f=[];for(let r=2;r<=n-3;r++)for(let s=r+2;s<=n-1;s++){const q="A".repeat(r-1)+"B"+"A".repeat(s-r-1)+"B"+"A".repeat(n-s);for(const i of [r,s])f.push(["A".repeat(i-1)+"B"+"A".repeat(n-i),q])}return f}
function classKey(p,q){if(p.endsWith("BA"))return q.endsWith("BABA")?"C0":"C1";if(q.endsWith("BAA"))return "C2";if(q.endsWith("BA"))return "C3";chk(q.endsWith("AAA"),"unrecognized suffix");return "C4"}
// Directed-edge residual transfer: each ordered NEXT DIRECTION is counted ONCE;
// never multiply by the number of interchangeable remaining edge copies.
function transfer(n){
 const edges=["AA","AB","BA"],P=[n-3,1,1],Q=[n-5,2,2],K=n-1;
 const zp=[n-2,0,0,0,0,0],zq=[n-4,0,0,0,0,0],memo=new Map();
 let visited=0,starts=0;
 function dp(a,b,rp,rq,k,tp,tq){
  if(k>K)return new Map();
  const remaining=rp.reduce((x,y)=>x+y,0);
  if(k+remaining<K)return new Map();
  if(!remaining)return rq.every(v=>v===0)&&k===K?new Map([[tp+"|"+tq,1n]]):new Map();
  const key=JSON.stringify([a,b,rp,rq,k,tp,tq]);
  if(memo.has(key))return memo.get(key);
  visited++;
  const out=new Map();
  for(let i=0;i<edges.length;i++)if(rp[i]&&edges[i][0]===a)
   for(let j=0;j<edges.length;j++)if(rq[j]&&edges[j][0]===b){
    const c=edges[i][1],d=edges[j][1],up=rp.slice(),uq=rq.slice();up[i]--;uq[j]--;
    const sub=dp(c,d,up,uq,k+(c===d?1:0),(tp+c).slice(-3),(tq+d).slice(-4));
    for(const [s,v] of sub)out.set(s,(out.get(s)||0n)+v);
   }
  memo.set(key,out);return out;
 }
 const suffix=new Map();
 for(const a of D)for(const b of D){
  if(!same(fromStart(a,edges,P),zp)||!same(fromStart(b,edges,Q),zq))continue;
  starts++;for(const [s,v] of dp(a,b,P,Q,a===b?1:0,a,b))suffix.set(s,(suffix.get(s)||0n)+v);
 }
 const classes={C0:0n,C1:0n,C2:0n,C3:0n,C4:0n};
 for(const [s,v] of suffix){const [p,q]=s.split("|");classes[classKey(p,q)]+=v}
 return {suffix,classes,visited,starts};
}
function trace(pair,actions){
 let [p,q]=pair,pops=2,cancels=1;
 for(const op of actions){
  if(op[0]==="POP"){chk(pops-->0&&q.length,"POP disabled");q=q.slice(0,-1)}
  else if(op[0]==="APP"){p+=op[1];q+=op[2]}
  else{
   chk(op[0]==="CANCEL"&&cancels-->0,"CANCEL budget");
   const valid=w=>w.endsWith("AB")||w.endsWith("BA");
   chk(valid(p)&&valid(q),"CANCEL disabled");p=p.slice(0,-2);q=q.slice(0,-2);
  }
 }
 return {p,q,observation:obs(p,q)};
}
function main(){
 const rows=[];
 for(const n of [5,6,7,8,9,10,11,12,13,14,16]){
  const T=transfer(n),counts=Object.values(T.classes),total=counts.reduce((a,b)=>a+b,0n);
  const expected=[1,n-5,2*(n-5),n-4,(n-5)*(n-6)].map(BigInt);
  chk(same(counts.map(String),expected.map(String)),"class counts n="+n);
  chk(total===BigInt((n-3)*(n-4)),"total n="+n);
  chk(T.starts===1,"endpoint-conditioned start n="+n);
  chk(T.suffix.size===(n===5?2:n===6?6:n===7?7:8),"safe suffix count n="+n);
  if(n<=10){
   const f=fiber(n),direct=new Map();
   chk(f.length===Number(total),"independent fiber n="+n);
   chk(f.every(([p,q])=>same(obs(p,q),obs(...f[0]))),"initial fiber n="+n);
   for(const [p,q] of f){const s=p.slice(-3)+"|"+q.slice(-4);direct.set(s,(direct.get(s)||0n)+1n)}
   chk(same([...direct].sort().map(([s,v])=>[s,String(v)]),[...T.suffix].sort().map(([s,v])=>[s,String(v)])),"enumeration versus transfer n="+n);
  }
  rows.push({n,fiber:String(total),safe_suffix_states:T.suffix.size,minimal_states:counts.filter(x=>x>0n).length,class_sizes:counts.map(String),memo_states:T.visited});
 }
 const C2=[["ABAAAA","ABABAA"],["AAABAA","ABABAA"]];
 const C3=[["ABAAAA","ABAABA"],["AABAAA","AABABA"]];
 const T2=[["POP"],["POP"],["APP","B","A"],["CANCEL"]];
 const T3=[["POP"],["POP"],["APP","B","B"],["CANCEL"]];
 chk(same(obs(...C2[0]),obs(...C2[1])),"C2 current obs");
 chk(same(obs(...C3[0]),obs(...C3[1])),"C3 current obs");
 const x2=trace(C2[0],T2),y2=trace(C2[1],T2);
 const x3=trace(C3[0],T3),y3=trace(C3[1],T3);
 chk(x2.observation[6]===3&&y2.observation[6]===2,"C2 K witness");
 chk(!same(x3.observation[5],y3.observation[5]),"C3 adjacency witness");
 chk(rows[0].minimal_states===2&&rows[1].minimal_states===4,"old quotients");
 return {
  status:"STAGE412B_BOUNDARY_TRANSFER_TWO_POP_PASS",
  numerical_semantics:"Exact BigInt counting, no floating point, no randomization",
  frozen_science:"GLOBAL@bf84bd7c61a2444b59b1da96be57df0e9ae47e53 EM@2af3fc484eb11060b69e0afc1b562bcaf5ad1419 P000_blob@bcc2590d3168a28f72e8b9f0f9b1f76faadcd488",
  results:rows,
  transfer_implementation_scope:"Sparse histograms Jp=(AA:n-3,AB:1,BA:1), Jq=(AA:n-5,AB:2,BA:2), endpoints and K=n-1. General full-12-direction recurrence proved in PROOF.",
  independent_full_fiber_enumeration_checked_n:"5..10",
  two_pop_one_cancel:{
   minimum_n_with_new_split:6,old_quotient:4,new_quotient:6,
   C2:{histories:C2,actions:T2,outputs:[{P:x2.p,Q:x2.q,K:x2.observation[6]},{P:y2.p,Q:y2.q,K:y2.observation[6]}]},
   C3:{histories:C3,actions:T3,outputs:[{P:x3.p,Q:x3.q,Q_J:x3.observation[5]},{P:y3.p,Q:y3.q,Q_J:y3.observation[5]}]}
  },
  proof_status:"AUTHOR_PROVED",independent_review:"PENDING",native_result:"NOT_ADMITTED"
 };
}
if(typeof process!=="undefined"&&process.stdout)process.stdout.write(JSON.stringify(main(),null,2)+"\n");
