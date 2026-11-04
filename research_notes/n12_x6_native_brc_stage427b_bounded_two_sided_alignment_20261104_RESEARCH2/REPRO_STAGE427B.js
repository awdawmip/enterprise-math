#!/usr/bin/env node
'use strict';
const result = (function checker(){
 const D="ABCDEFGHIJKL", letters=["A","B","C"];
 const assert=(v,msg)=>{if(!v)throw Error(msg)};
 const vec=w=>{let e=[0,0,0,0,0,0];for(const a of w){let z=D.indexOf(a);assert(z>=0,"direction");e[z>>1]+=(z&1)?-1:1}return e};
 const adj=w=>{let v={};for(let i=1;i<w.length;i++){let k=w[i-1]+w[i];v[k]=(v[k]||0)+1}return v};
 const K=(p,q)=>{let k=0;for(let i=0;i<Math.min(p.length,q.length);i++)k+=+(p[i]===q[i]);return k};
 const sort=o=>JSON.stringify(o,Object.keys(o).sort());
 const same=(x,y)=>JSON.stringify(x)===JSON.stringify(y);
 const observe=(p,q)=>[p.length,q.length,vec(p),vec(q),sort(adj(p)),sort(adj(q)),K(p,q)];
 function initialize(p,q,A,P){
  const m=[p.length,q.length],w=[p,q],cut=m.map((x,s)=>Math.max(0,x-P[s]));
  const c=Math.min(...cut),h=Math.min(m[0]+A[0],m[1]+A[1]),stable=[{},{}];
  for(let s=0;s<2;s++)for(let k=c+1;k<=Math.min(h,cut[s]);k++)stable[s][k]=w[s][k-1];
  let base=K(p,q);
  for(let k=c+1;k<=Math.min(...m);k++)base-=+(p[k-1]===q[k-1]);
  return {A,P,cut,c,h,stable,base,anchor:cut.map((z,s)=>z?w[s][z-1]:null),
   tail:cut.map((z,s)=>w[s].slice(z).split("")),len:m, E:[vec(p),vec(q)],J:[adj(p),adj(q)],usedA:[0,0],usedP:[0,0]};
 }
 function letter(t,s,k){return k<=t.cut[s]?t.stable[s][k]:t.tail[s][k-t.cut[s]-1]}
 function read(t){
  let k=t.base;for(let i=t.c+1;i<=Math.min(...t.len);i++){
   let a=letter(t,0,i),b=letter(t,1,i);assert(a&&b,"missing alignment label");k+=+(a===b);
  }
  return [t.len[0],t.len[1],...t.E.map(x=>x.slice()),...t.J.map(x=>sort(x)),k];
 }
 function legal(t,o){
  if(o[0]==="A")return t.usedA[o[1]]<t.A[o[1]];
  if(o[0]==="P")return t.usedP[o[1]]<t.P[o[1]]&&t.tail[o[1]].length>0;
  if(o[0]==="SA")return [0,1].every(s=>t.usedA[s]<t.A[s]);
  if(o[0]==="SP")return [0,1].every(s=>t.usedP[s]<t.P[s]&&t.tail[s].length>0);
  if(o[0]==="C")return [0,1].every(s=>{
   let v=t.tail[s];return t.usedP[s]+2<=t.P[s]&&v.length>=2&&(D.indexOf(v[v.length-2])^1)===D.indexOf(v[v.length-1]);
  });
  throw Error("operation");
 }
 function rawLegal(p,q,t,o){
  let w=[p,q];
  if(o[0]==="A")return t.usedA[o[1]]<t.A[o[1]];
  if(o[0]==="P")return t.usedP[o[1]]<t.P[o[1]]&&w[o[1]].length>0;
  if(o[0]==="SA")return [0,1].every(s=>t.usedA[s]<t.A[s]);
  if(o[0]==="SP")return [0,1].every(s=>t.usedP[s]<t.P[s]&&w[s].length>0);
  if(o[0]==="C")return [0,1].every(s=>{
   let v=w[s];return t.usedP[s]+2<=t.P[s]&&v.length>=2&&(D.indexOf(v[v.length-2])^1)===D.indexOf(v[v.length-1]);
  });
  throw Error("operation");
 }
 function act(t,o){
  assert(legal(t,o),"illegal");let u=JSON.parse(JSON.stringify(t));
  const push=(s,x)=>{
   const z=u.tail[s],prev=z.length?z[z.length-1]:u.anchor[s];
   if(prev){const k=prev+x;u.J[s][k]=(u.J[s][k]||0)+1}
   z.push(x);u.len[s]++;const j=D.indexOf(x);u.E[s][j>>1]+=(j&1)?-1:1;u.usedA[s]++;
  };
  const pop=s=>{
   const z=u.tail[s],x=z.pop(),prev=z.length?z[z.length-1]:u.anchor[s];
   if(prev){let k=prev+x;u.J[s][k]--;if(!u.J[s][k])delete u.J[s][k]}
   u.len[s]--;const j=D.indexOf(x);u.E[s][j>>1]-=(j&1)?-1:1;u.usedP[s]++;
  };
  if(o[0]==="A")push(o[1],o[2]);
  if(o[0]==="P")pop(o[1]);
  if(o[0]==="SA"){push(0,o[1]);push(1,o[2])}
  if(o[0]==="SP"){pop(0);pop(1)}
  if(o[0]==="C"){pop(0);pop(0);pop(1);pop(1)}
  return u;
 }
 function plain(p,q,o){
  let w=[p,q];
  if(o[0]==="A")w[o[1]]+=o[2];
  if(o[0]==="P")w[o[1]]=w[o[1]].slice(0,-1);
  if(o[0]==="SA"){w[0]+=o[1];w[1]+=o[2]}
  if(o[0]==="SP")w=w.map(x=>x.slice(0,-1));
  if(o[0]==="C")w=w.map(x=>x.slice(0,-2));
  return w;
 }
 const ops=[];
 for(let s of [0,1]){for(let x of letters)ops.push(["A",s,x]);ops.push(["P",s])}
 for(let x of letters)for(let y of letters)ops.push(["SA",x,y]);ops.push(["SP"],["C"]);
 const words=["",...letters];for(let x of letters)for(let y of letters)words.push(x+y);
 let initial=0,visited=0,transitions=0,legalityChecks=0,maxWindow=0;
 const budgets=[[1,1,1,1],[2,1,1,2]];
 for(let [ap,aq,pp,pq] of budgets)for(let p of words)for(let q of words) {
  initial++;const t=initialize(p,q,[ap,aq],[pp,pq]),width=t.h-t.c;
  assert(width<=Math.max(ap+pp,aq+pq),"width theorem");maxWindow=Math.max(maxWindow,width);
  const queue=[[p,q,t]],seen=new Set;
  for(let idx=0;idx<queue.length;idx++){
   const [x,y,cur]=queue[idx],key=JSON.stringify([x,y,cur.usedA,cur.usedP]);
   if(seen.has(key))continue;seen.add(key);visited++;
   assert(same(read(cur),observe(x,y)),"observer "+key);
   for(let op of ops){
    const can=legal(cur,op);legalityChecks++;
    assert(can===rawLegal(x,y,cur,op),"legality "+key+" "+op);
    if(can){const nxt=act(cur,op),out=plain(x,y,op);
     assert(same(read(nxt),observe(...out)),"transition "+key+" "+op);transitions++;
     queue.push([...out,nxt]);
    }
   }
  }
 }
 let witnesses=[];
 for(let L of [1,2,7,32]){
  let p="AAABA"+"A".repeat(L),p2="ABAAA"+"A".repeat(L),q="AC";
  assert(same(observe(p,q),observe(p2,q)),"initial witness");
  assert(p.slice(-L)===p2.slice(-L),"suffix witness");
  let before=K(p,q),afterPop=K(p,"A"),z=[K(p,"AA"),K(p2,"AA")];
  assert(same(z,[2,1]),"split witness");witnesses.push({L,before,afterPop,afterReplace:z});
 }
 let directionalPairs=0;
 for(let x of D)for(let y of D) {
  const t=initialize("A","B",[1,1],[1,1]);
  let z=act(act(t,["A",0,x]),["A",1,y]);
  assert(same(read(z),observe("A"+x,"B"+y)),"12 direction check");directionalPairs++;
 }
 return {marker:"STAGE427B_BOUNDED_TWO_SIDED_ALIGNMENT_PASS",input:{alphabet:"A,B,C subset of native twelve directions",max_initial_length:2,budget_profiles:budgets},initial_pairs:initial,visited_states:visited,legality_checks:legalityChecks,legal_transitions:transitions,max_window:maxWindow,all_twelve_direction_append_pairs:directionalPairs,witnesses,
 frozen_pins:{global:"bf84bd7c61a2444b59b1da96be57df0e9ae47e53",em:"2af3fc484eb11060b69e0afc1b562bcaf5ad1419",p000_blob:"bcc2590d3168a28f72e8b9f0f9b1f76faadcd488"},scope:"finite exhaustive oracle plus independent symbolic argument; author-side unreviewed"};
})();
console.log(JSON.stringify(result,null,2));
