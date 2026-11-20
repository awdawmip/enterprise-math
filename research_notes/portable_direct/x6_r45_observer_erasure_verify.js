'use strict';
// X6 R45, deterministic, exact integer BRC history/future-language verifier.
// Run: node x6_r45_observer_erasure_verify.js
const x6r45Verify = function x6r45Verify() {
  "use strict";
  function check(ok, message) { if (!ok) throw Error(message); }
  function graph(p) {
    const first = [-1,-1,0,0];
    const id = s => s.join(",");
    const states = new Map([[id(first), first]]);
    const edges = new Map();
    const queue = [first];
    for (let head = 0; head < queue.length; head++) {
      const s=queue[head], [a,b,o,t]=s, from=id(s), successors=[];
      for (let k=0;k<2;k++) {
        if (s[k]!==-1) continue;
        for (let i=0;i<p;i++) {
          if (i===0 && o!==0) continue;
          const v=s.slice();v[k]=i;if(i===0)v[2]=k+1;
          successors.push([(k===0?"A":"B")+i,id(v)]);
          if(!states.has(id(v))) { states.set(id(v),v);queue.push(v); }
        }
      }
      if(o!==0) {
        const v=[a,b,0,t];successors.push(["R",id(v)]);
        if(!states.has(id(v))) {states.set(id(v),v);queue.push(v);}
      }
      if((a===-1)!==(b===-1) && o===0 && t===0) {
        const used=a!==-1?0:1;
        const v=[a,b,s[used]===0?used+1:0,1];
        successors.push(["T",id(v)]);
        if(!states.has(id(v))) {states.set(id(v),v);queue.push(v);}
      }
      edges.set(from,successors);
    }
    return {first:id(first),states,edges};
  }
  function label(x, mode) {
    if(x==="R"||x==="T"||mode==="named")return x;
    return mode==="source"?x[0]:"F";
  }
  function signatures(g, mode) {
    const cache=new Map(), active=new Set();
    function suffix(id) {
      if(cache.has(id))return cache.get(id);
      check(!active.has(id),"cycle detected "+id);
      active.add(id);
      const out=new Map([["",1]]);
      for(const [raw,to] of g.edges.get(id)) {
        for(const [w,n] of suffix(to)) {
          const key=label(raw,mode)+(w?"/"+w:"");
          out.set(key,(out.get(key)||0)+n);
        }
      }
      active.delete(id);cache.set(id,out);return out;
    }
    for(const id of g.states.keys()) suffix(id);
    return cache;
  }
  function summary(sig) {
    const supportGroups=new Map(), countGroups=new Map();
    for(const [id,m] of sig) {
      const w=Array.from(m.keys()).sort();
      const supp=JSON.stringify(w);
      const weighted=JSON.stringify(w.map(x=>[x,m.get(x)]));
      if(!supportGroups.has(supp))supportGroups.set(supp,[]);
      supportGroups.get(supp).push(id);
      if(!countGroups.has(weighted))countGroups.set(weighted,[]);
      countGroups.get(weighted).push(id);
    }
    let maxFirst=0, witness=null;
    const reps=Array.from(supportGroups.values()).map(g=>g[0]);
    for(let i=0;i<reps.length;i++)for(let j=i+1;j<reps.length;j++) {
      const x=sig.get(reps[i]), y=sig.get(reps[j]);
      const diff=Array.from(new Set([...x.keys(),...y.keys()])).filter(w=>x.has(w)!==y.has(w));
      check(diff.length>0,"non-distinct groups");
      diff.sort((a,b)=>a.split("/").length-b.split("/").length || a.localeCompare(b));
      const w=diff[0], len=w?w.split("/").length:0;
      if(len>maxFirst){maxFirst=len;witness={from:reps[i],to:reps[j],word:w};}
    }
    const boolClass=new Map(), weightedClass=new Map();
    let k=0;for(const group of supportGroups.values()){for(const id of group)boolClass.set(id,k);k++;}
    k=0;for(const group of countGroups.values()){for(const id of group)weightedClass.set(id,k);k++;}
    return {boolean:supportGroups.size,weighted:countGroups.size,depth:maxFirst,witness,boolClass,weightedClass};
  }
  const cases=[];
  for(let p=1;p<=8;p++) {
    const g=graph(p);
    check(g.states.size===2*p*p+8*p+5,"state count p="+p);
    const ss={};for(const mode of ["named","source","blind"])ss[mode]=signatures(g,mode);
    const sum={};for(const mode of ["named","source","blind"])sum[mode]=summary(ss[mode]);
    const want=p===1?{named:11,source:11,blind:7}:{named:13,source:13,blind:8};
    const depths={named:2,source:2,blind:p===1?3:2};
    for(const mode of ["named","source","blind"]){
      check(sum[mode].boolean===want[mode] && sum[mode].weighted===want[mode],"quotient mismatch p="+p+" "+mode);
      check(sum[mode].depth===depths[mode],"depth mismatch p="+p+" "+mode);
    }
    for(const s of g.states.keys())for(const t of g.states.keys()){
      check((sum.named.boolClass.get(s)===sum.named.boolClass.get(t))===(sum.source.boolClass.get(s)===sum.source.boolClass.get(t)),"port erasure changed quotient at p="+p);
      for(const mode of ["named","source","blind"])check((sum[mode].boolClass.get(s)===sum[mode].boolClass.get(t))===(sum[mode].weightedClass.get(s)===sum[mode].weightedClass.get(t)),"path multiplicity split boolean class p="+p+" "+mode);
    }
    const root=ss.named.get(g.first);
    check(root.size===4*p*p+16*p-3,"BRC word count");
    for(const mode of ["source","blind"]){
      let total=0;for(const n of ss[mode].get(g.first).values())total+=n;
      check(total===root.size,"projected history multiplicity mismatch");
    }
    const follow=arr=>{
      let at=g.first;
      for(const a of arr){const edge=g.edges.get(at).find(x=>x[0]===a);check(!!edge,"invalid example "+arr);at=edge[1];}
      return at;
    };
    const a0=follow(["A0"]),b0=follow(["B0"]);
    check(sum.blind.boolClass.get(a0)===sum.blind.boolClass.get(b0),"source symmetry lost");
    check(sum.source.boolClass.get(a0)!==sum.source.boolClass.get(b0),"source distinction lost");
    if(p>=2){
      const s=follow(["A0","R"]), t=follow(["A1"]);
      check(ss.source.get(s).has("T/R") && !ss.source.get(t).has("T/R"),"T/R witness");
      check(ss.blind.get(s).has("T/R") && !ss.blind.get(t).has("T/R"),"blind T/R witness");
    }
    cases.push({p,decorated_states:g.states.size,named_history_words:root.size,classes:{named:want.named,source:want.source,source_blind:want.blind},weighted_classes_match_boolean:true,maximum_shortest_distinguishing_event_length:{named:sum.named.depth,source:sum.source.depth,source_blind:sum.blind.depth},hardest_source_blind_witness:sum.blind.witness});
  }
  return {schema:"EM_X6_R45_OBSERVER_ERASURE_EXACT_VERIFICATION_V1",model:"R44 two named whole-triad sources with p named Ports; conditional R,T event law",p_tested:[1,2,3,4,5,6,7,8],projection_labels:{named:"Ai/Bi,R,T",source:"A/B,R,T",source_blind:"F,R,T"},semantics:"complete finite successful-event suffix languages and positive integer path multiplicities",checks:"All declared asserts passed across complete reachable state graphs, every suffix and all ordered state pairs; no formal native TRIADIC_CLOSURE_E admission implied",cases};
};
console.log(JSON.stringify(x6r45Verify(), null, 2));
