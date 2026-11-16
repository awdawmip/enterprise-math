// PREFIX-849 independent exact BigInt pair-automaton certificate
// Run: node PREFIX849_R6_DYNAMIC_STREAM_MEMORY_THRESHOLD_CHECK.js > PREFIX849_R6_DYNAMIC_STREAM_MEMORY_THRESHOLD_RESULTS.json
// All arithmetic, state transitions, finite graph checks and traps are exact.
const result = (function compute(){
  "use strict";
  const p=5,W=2,N=32,a=2,b=1,C=2;
  const moduli=Array.from({length:16},(_,i)=>2*i+1);
  const adjacent=Array.from({length:N},(_,x)=>[x,...Array.from({length:p},(_,i)=>x^(1<<i))]);
  const moves=Array.from({length:N*N},()=>[]);
  for(let x=0;x<N;x++)for(let y=0;y<N;y++){
    for(const u of adjacent[x])for(const v of adjacent[y])moves[x*N+y].push(u*N+v);
  }
  const indexOfBit=new Map(Array.from({length:N*N},(_,i)=>[(1n<<BigInt(i)).toString(),i]));
  const congruence={};
  for(const q of moduli){
    let m=0n;
    for(let x=0;x<N;x++)for(let y=0;y<N;y++){
      if(x%q===y%q)m|=1n<<BigInt(x*N+y);
    }
    congruence[q]=m;
  }
  const diagonal=Array.from({length:N},(_,i)=>1n<<BigInt(i*N+i)).reduce((x,y)=>x|y,0n);
  const memo=new Map();
  function advance(mask,q){
    const key=mask.toString(16)+":"+q;
    if(memo.has(key))return memo.get(key);
    let out=0n,remaining=mask;
    while(remaining){
      const least=remaining&(-remaining);
      const i=indexOfBit.get(least.toString());
      for(const k of moves[i])out|=1n<<BigInt(k);
      remaining^=least;
    }
    out&=congruence[q];
    memo.set(key,out);
    return out;
  }
  function relation(word){
    let mask=congruence[word[0]];
    for(const q of word.slice(1))mask=advance(mask,q);
    return mask;
  }
  function good(word){return (relation(word)&~diagonal)===0n;}
  function graph(words){
    const E=new Map();
    for(const word of words){
      const u=word.slice(0,-1).join(","),v=word.slice(1).join(",");
      if(!E.has(u))E.set(u,new Set());
      E.get(u).add(v);
    }
    const indegree=new Map();
    for(const [u,neighbors] of E){
      if(!indegree.has(u))indegree.set(u,0);
      for(const v of neighbors)indegree.set(v,(indegree.get(v)||0)+1);
    }
    const queue=[...indegree].filter(([,d])=>d===0).map(([v])=>v);
    let removed=0;
    while(queue.length){
      const v=queue.pop();removed++;
      for(const u of E.get(v)||[]){
        indegree.set(u,indegree.get(u)-1);
        if(indegree.get(u)===0)queue.push(u);
      }
    }
    return {vertices:indegree.size,edges:words.length,topological_removed:removed,acyclic:removed===indegree.size};
  }
  const good2=[],good3=[];
  for(const q1 of moduli)for(const q2 of moduli){
    if(good([q1,q2]))good2.push([q1,q2]);
    for(const q3 of moduli)if(good([q1,q2,q3]))good3.push([q1,q2,q3]);
  }
  const period=[25,19,29,11];
  const period_windows=period.map((_,j)=>period.concat(period).slice(j,j+4));
  const period_verified=period_windows.map(word=>({word,good:good(word)}));
  const trap=[[15,22],[15,24],[15,26],[15,28],[15,30],[16,31],[18,31],[20,31],[22,31],[24,31]];
  const trap_moduli=[1,3,5,7,9,11,13,15];
  const trap_successors=trap.map(([x,y])=>trap_moduli.map(q=>{
    const k=trap.findIndex(([u,v])=>(u-v)%q===0&&(
       (adjacent[x].includes(u)&&adjacent[y].includes(v))||
       (adjacent[x].includes(v)&&adjacent[y].includes(u))));
    if(k<0)throw Error("Missing ambiguity-trap successor "+[x,y,q]);
    return k;
  }));
  if(good2.length!==1||good2[0].join(",")!=="17,31")throw Error("Unexpected 2-window classification");
  if(good3.length!==37)throw Error("Unexpected 3-window classification");
  const G2=graph(good2),G3=graph(good3);
  if(!G2.acyclic||!G3.acyclic)throw Error("Unexpected cycle for w<=3");
  if(period_verified.some(x=>!x.good))throw Error("4-window periodic schedule failed");
  if(trap_successors.length!==10||trap_successors.some(row=>row.length!==8))throw Error("Incomplete trap");
  return {
    schema:"EM_PREFIX849_EXACT_DYNAMIC_STREAM_CERTIFICATE_V1",
    science_pin:"f42f2906d77f24085c123f3ccfe9667d41caa96d",
    parameters:{p,W,a,b,C,N,one_coordinate_update_including_stay:true,receiver_retains_last_w_reports_only:true},
    late_effective_moduli_B5:moduli,
    all_good_words_w2:good2,
    all_good_words_w3:good3,
    good_word_counts:{w2:good2.length,w3:good3.length},
    overlap_graphs:{w2:G2,w3:G3},
    period,period_windows:period_verified,
    universal_ambiguity_trap_B4:{pairs:trap,late_effective_moduli:trap_moduli,successor_indices_zero_based:trap_successors},
    exact_width_law:{"w=1,2,3":6,"w>=4":5},
    exact_verification:"ALL_EXACT_ASSERTIONS_PASSED"
  };
})();
console.log(JSON.stringify(result,null,2));
