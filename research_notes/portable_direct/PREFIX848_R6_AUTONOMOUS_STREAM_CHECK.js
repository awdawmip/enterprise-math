"use strict";
function runChecker() {
  function gcd(a,b){while(b){[a,b]=[b,a%b];}return a;}
  function tuples(p,W) {
    const N=W**p,adj=Array.from({length:N},()=>[]),powers=Array.from({length:p},(_,i)=>W**i);
    for(let u=0;u<N;u++){
      adj[u].push(u);
      for(let i=0;i<p;i++){const old=Math.floor(u/powers[i])%W;
        for(let x=0;x<W;x++)if(x!==old)adj[u].push(u+(x-old)*powers[i]);
      }
    }
    return adj;
  }
  function traces(adj,w){
    let t=adj.map((_,u)=>[u]);
    for(let j=1;j<w;j++){
      const n=[];for(const tr of t)for(const v of adj[tr[tr.length-1]])n.push(tr.concat(v));
      t=n;
    }return t;
  }
  function wordGood(word,paths){
    const seen=new Map();
    for(const tr of paths){
      const key=tr.map((u,i)=>u%word[i]).join(",");
      const out=tr[tr.length-1];
      if(seen.has(key)&&seen.get(key)!==out)return false;
      seen.set(key,out);
    }
    return true;
  }
  function product(A,w){
    let x=[[]];for(let i=0;i<w;i++){const y=[];for(const t of x)for(const m of A)y.push(t.concat(m));x=y;}return x;
  }
  function findCycle(words,w){
    const adj=new Map();
    for(const word of words){
      const from=word.slice(0,w-1).join(","),to=word.slice(1).join(",");
      if(!adj.has(from))adj.set(from,[]);
      adj.get(from).push(to);
    }
    const seen=new Set(),on=new Map(),stack=[];
    function dfs(v){
      seen.add(v);on.set(v,stack.length);stack.push(v);
      for(const u of adj.get(v)||[]){
        if(on.has(u)){
          const cycle=stack.slice(on.get(u));
          return cycle.map(x=>Number(x.split(",")[0]));
        }
        if(!seen.has(u)){const ans=dfs(u);if(ans)return ans;}
      }
      on.delete(v);stack.pop();return null;
    }
    for(const v of adj.keys())if(!seen.has(v)){const x=dfs(v);if(x)return x;}
    return null;
  }
  const certificates=[], sampleChecks=[];
  let wordsTested=0, pathsRead=0, goodWords=0;
  for(let p=2;p<=4;p++)for(const w of [2,3]){
    const W=2,N=2**p,paths=traces(tuples(p,W),w);
    for(const C of [1,2,6]){
      let optimum=null, period=null;
      const attempts=[];
      for(let B=0;B<=6;B++){
        const A=Array.from({length:2**B},(_,i)=>i+1).filter(q=>gcd(q,C)===1);
        const all=product(A,w),accepted=[];
        for(const word of all){
          const ok=wordGood(word,paths);wordsTested++;pathsRead+=paths.length;
          if(ok){accepted.push(word);goodWords++;}
        }
        const cyc=findCycle(accepted,w);
        attempts.push({B,moduli:A.length,possible_words:all.length,good_words:accepted.length,has_cycle:cyc!==null,cycle:cyc});
        if(cyc){optimum=B;period=cyc;break;}
      }
      if(optimum===null)throw Error("no feasible width");
      const sampleTimes=[1,4,9];
      for(const t of sampleTimes){
        let ok=true;
        for(let s=0;s<period.length;s++){
          const word=Array.from({length:w},(_,i)=>period[(s+i)%period.length]);
          if(!wordGood(word,paths))ok=false;
        }
        if(!ok)throw Error("cycle verification");
        sampleChecks.push({p,w,C,t,period,all_rotations_valid:true});
      }
      certificates.push({p,W,w,C,N,trajectories_per_window:paths.length,minimum_per_heartbeat_bits:optimum,witness_period:period,all_strictly_smaller_bitwidths_no_cycle:attempts.slice(0,-1).every(x=>!x.has_cycle),attempts});
    }
  }
  if(certificates.length!==18)throw Error("coverage gap");
  if(sampleChecks.some(x=>!x.all_rotations_valid))throw Error("invalid cycle");
  return {schema:"PREFIX848_AUTONOMOUS_DYNAMIC_STREAM_WINDOW_CHECK_V1",
    status:"ALL_EXACT_ASSERTIONS_PASSED",
    finite_scope:{p:[2,3,4],W:2,w:[2,3],C:[1,2,6],total_cases:18,max_width_searched:6},
    method:"Enumerate all Hamming-one state trajectories and every admissible w-long modulus word. Build the directed overlap graph on length-(w-1) modulus words; test for any directed cycle. For every B below optimum, absence of a directed cycle certifies impossibility of all infinite predetermined schedules.",
    summary:{cases:certificates.length,modulus_words_tested:wordsTested,trajectory_word_evaluations_upper_bound:pathsRead,accepted_words:goodWords,period_rotation_checks:sampleChecks.length},
    certificates,sampleChecks};
}
console.log(JSON.stringify(runChecker(),null,2));
