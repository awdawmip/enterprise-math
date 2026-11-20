"use strict";
// X6 R46: reproducible exact positive-weight source-erasure BRC future verifier.
// Run: node x6_r46_source_weighted_erasure_verify.js
function x6r46Verify(){
"use strict";
const assert=(ok,msg)=>{if(!ok)throw Error(msg)};
function model(p){
 const first=[-1,-1,0,0],key=s=>s.join(","),states=[first], ids=new Map([[key(first),0]]),arcs=[];
 for(let h=0;h<states.length;h++){
  const s=states[h], [a,b,o,t]=s, e=[];
  function add(raw,to){
   const k=key(to);if(!ids.has(k)){ids.set(k,states.length);states.push(to)}
   e.push([raw,ids.get(k)]);
  }
  for(let k=0;k<2;k++){
   if(s[k]!==-1)continue;
   for(let i=0;i<p;i++){
    if(i===0&&o!==0)continue;
    const v=s.slice();v[k]=i;if(i===0)v[2]=k+1;
    add((k===0?"A":"B")+i,v);
   }
  }
  if(o!==0)add("R",[a,b,0,t]);
  if((a===-1)!==(b===-1) && o===0&&t===0){
   const used=a!==-1?0:1;add("T",[a,b,s[used]===0?used+1:0,1]);
  }
  arcs.push(e);
 }
 return {states,arcs};
}
function role(s){
 const [a,b,o,t]=s;
 if(a<0&&b<0)return "U";
 if(a>=0&&b>=0)return o?"D1":"D0";
 if(o)return t?"O1":"O0";
 if(t)return "C1";
 return (a>=0?a:b)===0?"C0":"Cn";
}
function series(g,alpha,beta){
 const cache=new Map(),act=new Set();
 function suffix(id){
  if(cache.has(id))return cache.get(id);
  assert(!act.has(id),"cycle");
  act.add(id);
  const out=new Map([["",1]]);
  for(const [raw,to] of g.arcs[id]){
   const lab=/^[AB]/.test(raw)?"F":raw,weight=raw[0]==="A"?alpha:raw[0]==="B"?beta:1;
   for(const [word,n] of suffix(to)){
    const w=lab+(word?"/"+word:"");
    out.set(w,(out.get(w)||0)+weight*n);
   }
  }
  act.delete(id);cache.set(id,out);return out;
 }
 return g.states.map((_,i)=>suffix(i));
}
const cases=[];
for(let p=1;p<=8;p++){
 const g=model(p), n=g.states.length;
 assert(n===2*p*p+8*p+5,"state count p "+p);
 const rootKey=s=>s.join(","),a0=g.states.findIndex(x=>rootKey(x)==="0,-1,1,0"),b0=g.states.findIndex(x=>rootKey(x)==="-1,0,2,0");
 assert(a0>=0&&b0>=0,"witness missing");
 for(const [alpha,beta] of [[1,1],[1,2],[2,3],[3,2],[1,3]]){
  const sig=series(g,alpha,beta), groups=new Map();
  for(let i=0;i<n;i++){
   const k=JSON.stringify([...sig[i]].sort((a,b)=>a[0].localeCompare(b[0])));
   if(!groups.has(k))groups.set(k,[]);
   groups.get(k).push(i);
  }
  const expected=alpha===beta?(p===1?7:8):(p===1?11:13);
  assert(groups.size===expected,"class count p "+p+" weights "+alpha+","+beta+" got "+groups.size);
  const traits=new Set();
  for(const group of groups.values()){
   const ts=new Set(group.map(id=>{
    const r=role(g.states[id]);
    const orient=(alpha===beta||["U","D0","D1"].includes(r))?"":(g.states[id][0]>=0?"A":"B");
    return r+":"+orient;
   }));
   assert(ts.size===1,"class failed trait "+p);
   traits.add([...ts][0]);
  }
  assert(traits.size===expected,"traits failed");
  const reps=[...groups.values()].map(g=>g[0]);
  let maxDepth=0;const hist={};
  for(let i=0;i<reps.length;i++)for(let j=i+1;j<reps.length;j++){
   const x=sig[reps[i]],y=sig[reps[j]];
   const words=[...new Set([...x.keys(),...y.keys()])];
   const diff=words.filter(w=>(x.get(w)||0)!==(y.get(w)||0));
   assert(diff.length>0,"distinct series unexpectedly equal");
   const depth=Math.min(...diff.map(w=>w===""?0:w.split("/").length));
   hist[depth]=(hist[depth]||0)+1;maxDepth=Math.max(maxDepth,depth);
  }
  assert(maxDepth===2,"sharp cutoff "+p);
  const eq=JSON.stringify([...sig[a0]].sort())===JSON.stringify([...sig[b0]].sort());
  assert(eq===(alpha===beta),"source symmetry p "+p);
  assert((sig[a0].get("F")||0)===(p-1)*beta && (sig[b0].get("F")||0)===(p-1)*alpha,"immediate F");
  if(p===1)assert(sig[a0].get("R/F")===beta && sig[b0].get("R/F")===alpha,"RF witness");
  const rootMass=[...sig[0].values()].reduce((x,y)=>x+y,0);
  const wantMass=1+(2*p+2)*(alpha+beta)+(4*p*p+12*p-8)*alpha*beta;
  assert(rootMass===wantMass,"weighted polynomial p "+p);
  cases.push({p,alpha,beta,states:n,classes:groups.size,max_depth:maxDepth,first_difference_pair_histogram:hist,total_root_weight:rootMass});
 }
}
return {schema:"X6_R46_SOURCE_WEIGHTED_ERASURE_BRC_V1",status:"PASS",scope:"R44 conditional whole-triad source/Port graph; positive exact BRC weights; F/R/T event observer",tested_ports:[1,2,3,4,5,6,7,8],weights:[[1,1],[1,2],[2,3],[3,2],[1,3]],theorem:{classes_equal:"p=1:7; p>=2:8",classes_unequal:"p=1:11; p>=2:13",sharp_weighted_distinguishing_horizon:2,root_mass:"1+(2p+2)(alpha+beta)+(4p^2+12p-8)alpha*beta"},checks:"complete reachable graph, exact integer finite suffix series, source-label erasure, all class pairs, role-orientation proof skeleton; physical admissibility and review remain open",cases};
}
console.log(JSON.stringify(x6r46Verify(),null,2));
