const runExactCheck = function runExactCheck(){
  let assertions=0;
  const check=(p,m)=>{assertions++;if(!p)throw Error(m)};
  const mod=(x,n)=>((x%n)+n)%n;
  const add=(x,y)=>x.map((v,i)=>v+y[i]);
  const diff=(x,y)=>x.map((v,i)=>v-y[i]);
  const enc=x=>x.join(",");
  const basis=Array.from({length:3},(_,i)=>Array.from({length:6},(_,j)=>i===j?1:0));
  const a=basis.concat(basis.map(x=>x.map(v=>-v)));
  const states=[];
  for(const kind of ["S","I","O"])for(let r=0;r<6;r++)for(const e of [-1,1])states.push({kind,r,e,key:`${kind}:${r}:${e}`});
  const lookup=new Map(states.map(s=>[s.key,s]));
  const nextIndex=s=>mod(s.r+s.e,6);
  const cell=s=>s.kind==="S"?a[s.r]:s.kind==="I"?Array(6).fill(0):add(a[s.r],a[nextIndex(s)]);
  const targets=s=>s.kind==="S"?["I","O"].map(kind=>lookup.get(`${kind}:${s.r}:${s.e}`)):[lookup.get(`S:${nextIndex(s)}:${s.e}`)];
  const phase=s=>mod(2*s.e*s.r+(s.kind==="S"?0:1),12);
  check(states.length===36,"state count");
  const cellSet=new Set(states.map(s=>enc(cell(s))));
  check(cellSet.size===13,"distinct spatial Cells");
  let arrows=0;
  for(const s of states)for(const to of targets(s)){
    arrows++;
    let delta=diff(cell(to),cell(s));
    check(delta.reduce((z,v)=>z+Math.abs(v),0)===1,"nonprimitive transition "+s.key);
    check(phase(to)===mod(phase(s)+1,12),"clock noncommutation "+s.key);
    check(to.e===s.e,"chirality altered");
  }
  check(arrows===48,"arrow count");
  const memo=new Map();
  function traces(s,steps){
    let key=s.key+":"+steps;
    if(memo.has(key))return memo.get(key);
    let current=enc(cell(s));
    let out=steps===0?[current]:targets(s).flatMap(t=>traces(t,steps-1).map(w=>current+"|"+w));
    out=[...new Set(out)].sort();
    memo.set(key,out);
    return out;
  }
  let distinguish=[];
  for(let depth=0;depth<=2;depth++){
    const groups=new Set(states.map(s=>JSON.stringify(traces(s,depth))));
    distinguish.push(groups.size);
  }
  check(JSON.stringify(distinguish)===JSON.stringify([13,30,36]),"trace refinement counts");
  for(let i=0;i<states.length;i++)for(let j=i+1;j<states.length;j++)
    check(JSON.stringify(traces(states[i],2))!==JSON.stringify(traces(states[j],2)),"two-step equivalence");
  const root=e=>3*e;
  check(mod(root(1),6)===mod(root(-1),6),"C6 sign should alias");
  check(mod(root(1),12)!==mod(root(-1),12),"C12 sign separation");
  for(let e of [-1,1]){
    const fibers=Array(12).fill(0);
    for(const s of states.filter(s=>s.e===e))fibers[phase(s)]++;
    check(fibers.every((v,i)=>v===(i%2===0?1:2)),"oriented C12 fiber sizes");
    for(let r=0;r<6;r++){
      let s=lookup.get(`S:${r}:${e}`),initial=enc(cell(s));
      const steps=[];
      for(let t=1;t<=12;t++){
        s=(s.kind==="S")?lookup.get(`O:${s.r}:${e}`):targets(s)[0];
        steps.push(enc(cell(s)));
        if(t===6)check(enc(cell(s))===enc(a[mod(r+3,6)]),"half-turn endpoint");
      }
      check(enc(cell(s))===initial,"outer closed orbit");
      check(steps.length===12,"outer microsteps");
    }
  }
  const choose=(n,k)=>{let z=1;for(let i=1;i<=k;i++)z=z*(n+1-i)/i;return Math.round(z)};
  const populations={};
  for(const W of [1,2]){
    const M=6*W, all=new Set(), counts={};
    for(const e of [-1,1]){
      let local=new Set(), bins=Array(M+1).fill(0);
      for(let mask=0;mask<2**M;mask++){
        let r=0, trace=[enc(a[0])],inner=0;
        for(let t=0;t<M;t++){
          let nr=mod(r+e,6),useInner=Boolean(mask&(2**t));
          trace.push(enc(useInner?Array(6).fill(0):add(a[r],a[nr])));
          trace.push(enc(a[nr]));
          if(useInner)inner++;
          r=nr;
        }
        check(r===0,"periodic shell return");
        check(trace.length===12*W+1,"event length");
        const key=trace.join(";");
        check(!local.has(key),"branch trace collision");
        local.add(key);
        check(!all.has(key),"chirality trace collision");
        all.add(key);
        bins[inner]++;
      }
      check(local.size===2**M,"per-chirality BRC count");
      for(let j=0;j<=M;j++)check(bins[j]===choose(M,j),"pivot histogram");
      counts[e===1?"forward":"reverse"]={distinct_traces:local.size,pivot_histogram:bins};
    }
    check(all.size===2**(M+1),"total BRC traces at fixed event count");
    populations[`W${W}`]={primitive_events:12*W,distinct_traces:all.size,per_chirality:counts};
  }
  return {schema:"X6_TIME_BIDIRECTIONAL_36STATE_EXACT_CHECK_V1",scientific_status:"FINITE_EXACT_CHECK_ONLY",frozen_p000:"a72226e2430ffa4786321ac86e7f0c599d5f0389",states:states.length,native_arrows:arrows,distinct_cells:cellSet.size,cell_trace_distinction_horizon_0_1_2:distinguish,physical_event_phase_states:12,oriented_phase_pair_states:24,outer_only_oriented_states:24,fixed_length_live_bits:6,source_principal_root:{forward:3,reverse:-3,c6_indistinguishable:true,c12_distinguishable:true,static_under_fixed_sweep:true},population:populations,exact_assertions:assertions,mismatches:0};
};
console.log(JSON.stringify(runExactCheck(), null, 2));
