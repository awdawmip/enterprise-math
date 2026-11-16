// R762BZ. Exact, dependency-free verifier. Run: node R762BZ_TWO_FORCE_LIFT_VERIFY.js
const verifyR762BZ = function verifyR762BZ() {
  const A=[1,2,3,4,5,6], signs=[-1,1];
  const perms=(arr)=>arr.length?arr.flatMap((v,i)=>perms(arr.filter((_,j)=>j!==i)).map(t=>[v,...t])):[[]];
  const allPerm=perms(A);
  const frames=[];
  for (const a of A) for(const b of A) if(b!==a)
    for(const d of A) if(d!==a && d!==b)
      for(const sa of signs)for(const sb of signs)for(const sd of signs)
        frames.push([a,b,d,sa,sb,sd]);
  const key=f=>`${f[0]},${f[1]},${f[3]},${f[4]}`;
  const targets=(f)=>A.filter(y=>y!==f[0] && y!==f[1]);
  const legal=(f,y)=>Number(y!==f[2]);
  const fibers=new Map();
  for(const f of frames){const k=key(f);if(!fibers.has(k))fibers.set(k,[]);fibers.get(k).push(f)}
  if(frames.length!==960 || fibers.size!==120 || [...fibers.values()].some(v=>v.length!==8))throw Error("fiber count");
  let transportChecks=0;
  for(const p of allPerm){
    const map=new Map(A.map((v,i)=>[v,p[i]]));
    for(const f of frames){
      const g=[map.get(f[0]),map.get(f[1]),map.get(f[2]),f[3],f[4],f[5]];
      for(const y of targets(f)){
        if(legal(f,y)!==legal(g,map.get(y)))throw Error("equivariance");
        transportChecks++;
      }
    }
  }
  let stabilizerChecks=0;
  for(const a of A)for(const b of A)if(a!==b){
    const others=A.filter(x=>x!==a&&x!==b),orbit=new Set();
    for(const p of perms(others)){orbit.add(p[0]);stabilizerChecks++}
    if(orbit.size!==4)throw Error("S4 orbit");
  }
  function adaptive(states, queries, oracle){
    const cache=new Map();
    function depth(group){
      if(group.length<2)return 0;
      const k=group.join(",");
      if(cache.has(k))return cache.get(k);
      let best=Infinity;
      for(const q of queries){
        const yes=group.filter(i=>oracle(q,states[i])===1);
        const no=group.filter(i=>oracle(q,states[i])===0);
        if(yes.length&&no.length)best=Math.min(best,1+Math.max(depth(yes),depth(no)));
      }
      cache.set(k,best);return best;
    }
    return {depth:depth(states.map((_,i)=>i)),states:cache.size}
  }
  function fixed(states, queries,oracle){
    function subsets(n,k,from=0,cur=[],out=[]){
      if(cur.length===k){out.push([...cur]);return out}
      for(let i=from;i<n;i++){cur.push(i);subsets(n,k,i+1,cur,out);cur.pop()}
      return out;
    }
    for(let k=0;k<=queries.length;k++){
      let count=0;
      for(const set of subsets(queries.length,k)){
        const codes=new Set(states.map(s=>set.map(i=>oracle(queries[i],s)).join("")));
        if(codes.size===states.length)count++;
      }
      if(count)return {minimum:k,optimalCount:count};
    }
  }
  const cands=[3,4,5,6];
  const queries=cands.map(y=>`y${y}`);
  const oAxis=(q,c)=>Number(c!==Number(q.slice(1)));
  const axisA=adaptive(cands,queries,oAxis),axisF=fixed(cands,queries,oAxis);
  const fullStates=cands.flatMap(c=>signs.map(s=>[c,s]));
  const fullQueries=[...queries,"sign"];
  const oFull=(q,s)=>q==="sign"?Number(s[1]===1):oAxis(q,s[0]);
  const fullA=adaptive(fullStates,fullQueries,oFull),fullF=fixed(fullStates,fullQueries,oFull);
  if(axisA.depth!==3||axisF.minimum!==3||axisF.optimalCount!==4||fullA.depth!==4||fullF.minimum!==4||fullF.optimalCount!==4)throw Error("query optimum");
  let witnesses=0, signBlind=0;
  for(const fiber of fibers.values()){
    const seen=new Set(fiber.map(f=>`${f[2]},${f[5]}`));
    if(seen.size!==8)throw Error("signed fiber");
    for(const f of fiber)for(const g of fiber){
      if(f[2]!==g[2]){if(legal(f,f[2])===legal(g,f[2]))throw Error("distinguishing witness");witnesses++}
      else if(f[5]!==g[5]){for(const y of targets(f))if(legal(f,y)!==legal(g,y))throw Error("sign blindness");signBlind++}
    }
  }
  if(transportChecks!==2764800||stabilizerChecks!==720||witnesses!==5760||signBlind!==960)throw Error("global expected counts");
  return {
    schema:"ENTERPRISE_MATH_R762BZ_TWO_FORCE_LIFT_EXACT_EVIDENCE_V1",
    status:"AUTHOR_EXACT_FINITE_CHECK_PASSED_NOT_REVIEWED",
    task_id:"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
    scientific_input:"enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json",
    model:"CONDITIONAL_THREE_NAMED_SIGNED_PORTS_ON_SIX_DISTINCT_X6_LABELS",
    full_frames:frames.length,
    observed_signed_two_port_records:fibers.size,
    fiber_sizes:{"8":fibers.size},
    unused_axis_candidates:4,
    hidden_sign_variants:2,
    tested_S6_permutations:allPerm.length,
    exact_transport_checks:transportChecks,
    S4_stabilizer_checks:stabilizerChecks,
    one_step_distinguishing_pair_checks:witnesses,
    sign_blind_pair_checks:signBlind,
    availability_only:{classes:4,repair_bits:2,adaptive_worst_queries:axisA.depth,nonadaptive_minimum_queries:axisF.minimum,optimal_nonadaptive_query_sets:axisF.optimalCount,dp_states:axisA.states},
    availability_plus_sign:{classes:8,repair_bits:3,adaptive_worst_queries:fullA.depth,nonadaptive_minimum_queries:fullF.minimum,optimal_nonadaptive_query_sets:fullF.optimalCount,dp_states:fullA.states},
    native_event_license_verified:false,
    independent_review:"NOT_REVIEWED"
  };
};
console.log(JSON.stringify(verifyR762BZ(), null, 2));
