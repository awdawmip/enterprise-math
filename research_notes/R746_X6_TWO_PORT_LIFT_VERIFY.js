"use strict";
// Exact finite checker; no dependencies, reproducible with node R746_X6_TWO_PORT_LIFT_VERIFY.js
const verifyR746=function verifyR746(){
  const assert=(v,m)=>{if(!v)throw new Error(m)};
  const permutations=a=>a.length?a.flatMap((v,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[v,...p])):[[]];
  const canonCycle=a=>{let k=a.indexOf(Math.min(...a));return [...a.slice(k),...a.slice(0,k)]};
  const sortedConf=a=>a.slice().sort((x,y)=>x[0]-y[0]);
  const key=(conf,cyc)=>JSON.stringify([sortedConf(conf),canonCycle(cyc)]);
  const all=new Map(),byPair=new Map(),states=[];
  for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)for(let c=b+1;c<6;c++)for(let mask=0;mask<8;mask++){
    const conf=[[a,mask&1?1:-1],[b,mask&2?1:-1],[c,mask&4?1:-1]];
    for(const cyc of [[a,b,c],[a,c,b]]){
      const e={conf,cyc:canonCycle(cyc)};states.push(e);all.set(key(conf,cyc),e);
      for(let omit=0;omit<3;omit++){
        const pair=conf.filter((_,i)=>i!==omit),pkey=JSON.stringify(pair);
        if(!byPair.has(pkey))byPair.set(pkey,[]);
        byPair.get(pkey).push(e);
      }
    }
  }
  assert(states.length===320&&all.size===320,"oriented C1 states");
  assert(byPair.size===60,"signed two-port observations");
  const fdist={};for(const [pkey,list] of byPair){
    const pair=JSON.parse(pkey),seen=new Set();fdist[list.length]=(fdist[list.length]||0)+1;
    for(const e of list){
      const hid=e.conf.find(x=>!pair.some(y=>y[0]===x[0]));
      const v=pair[0][0],successor=e.cyc[(e.cyc.indexOf(v)+1)%3];
      seen.add(JSON.stringify([hid,successor]));
    }
    assert(list.length===16&&seen.size===16,"16-valued injective repair");
  }
  const ps=permutations([0,1,2,3,4,5]);
  let cov=0;
  for(const [pkey,list] of byPair){
    const pair=JSON.parse(pkey);
    for(const e of list)for(const pi of ps){
      const c=sortedConf(e.conf.map(([axis,sgn])=>[pi[axis],sgn])),w=canonCycle(e.cyc.map(axis=>pi[axis]));
      const np=sortedConf(pair.map(([axis,sgn])=>[pi[axis],sgn]));
      assert(all.has(key(c,w)),"S6 acts on C1");
      assert(byPair.get(JSON.stringify(np)).some(x=>key(x.conf,x.cyc)===key(c,w)),"S6 fiber covariance");
      for(const [i] of pair){
        const successor=e.cyc[(e.cyc.indexOf(i)+1)%3],imageNext=w[(w.indexOf(pi[i])+1)%3];
        assert(pi[successor]===imageNext,"successor naturality");
      }
      cov++;
    }
  }
  const parts=[];
  for(let b=1;b<6;b++)for(let c=b+1;c<6;c++)parts.push([[0,b,c],[1,2,3,4,5].filter(v=>v!==b&&v!==c)]);
  assert(parts.length===10,"three-plus-three partitions");
  const decoKey=cycles=>JSON.stringify(cycles.map(canonCycle).sort((x,y)=>Math.min(...x)-Math.min(...y)));
  const decomp=new Map();
  for(const [A,B] of parts)for(const flipA of [false,true])for(const flipB of [false,true]){
    let first=flipA?[A[0],A[2],A[1]]:A,second=flipB?[B[0],B[2],B[1]]:B;
    const v=[first,second],k=decoKey(v);decomp.set(k,v);
  }
  assert(decomp.size===40,"oriented two-triad decomposition count");
  let decompCov=0;for(const v of decomp.values())for(const pi of ps){assert(decomp.has(decoKey(v.map(cyc=>cyc.map(i=>pi[i])))),"S6 decomposition covariance");decompCov++}
  return {schema:"EM_R746_C1_TWO_PORT_LIFT_EXACT_V1",status:"PASS",native_axes:6,oriented_c1_states:states.length,signed_two_port_observations:byPair.size,incidence_lifts:states.length*3,lift_fiber_distribution:fdist,min_repair_bits:4,permutations_S6:ps.length,projection_covariance_checks:cov,decomposition_three_plus_three:parts.length,oriented_six_force_decompositions:decomp.size,decomposition_covariance_checks:decompCov,verification:"exact finite integer enumeration and explicit S6 actions",native_V29_V39_executed:false};
};
console.log(JSON.stringify(verifyR746(),null,2));
