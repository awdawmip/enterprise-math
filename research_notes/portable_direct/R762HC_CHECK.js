// R762HC standard-JavaScript exact checker. Run: node R762HC_CHECK.js
const evidence = (function checkerMain(){
  const assert=(cond,msg)=>{if(!cond)throw new Error(msg);};
  const n=6, axes=[0,1,2,3,4,5];
  const triples=[];
  for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)for(let k=j+1;k<n;k++) triples.push([i,j,k]);
  const vec=s=>axes.map(a=>s.includes(a)?1:0);
  const key=v=>v.join(",");
  const vectors=triples.map(vec), set=new Set(triples.map(key));
  assert(triples.length===20,"triple count");
  const perms=[];
  const permute=(a,b)=>{if(!b.length){perms.push(a);return;}for(let i=0;i<b.length;i++)permute([...a,b[i]],[...b.slice(0,i),...b.slice(i+1)]);};
  permute([],axes);
  assert(perms.length===720,"S6 size");
  for(const p of perms)for(const t of triples){
    const mapped=t.map(x=>p[x]).sort((a,b)=>a-b);
    assert(set.has(key(mapped)),"S6 triple covariance");
  }
  let pairInputs=0,stabilizerChecks=0;
  for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(i!==j){
    pairInputs++;
    const complement=axes.filter(x=>x!==i&&x!==j);
    assert(complement.length===4,"completion arity");
    const stabilizer=perms.filter(p=>p[i]===i&&p[j]===j);
    assert(stabilizer.length===24,"pair stabilizer S4");
    const orbit=new Set(stabilizer.map(p=>p[complement[0]]));
    assert(orbit.size===4,"transitive stabilizer");
    stabilizerChecks+=stabilizer.length;
  }
  function determinant(input){
    const a=input.map(row=>row.map(BigInt));const n=a.length;
    let sign=1n,previous=1n;
    for(let k=0;k<n-1;k++){
      let pivot=k;while(pivot<n&&a[pivot][k]===0n)pivot++;
      if(pivot===n)return 0n;
      if(pivot!==k){[a[k],a[pivot]]=[a[pivot],a[k]];sign=-sign;}
      const p=a[k][k];
      for(let i=k+1;i<n;i++){
        for(let j=k+1;j<n;j++){
          const num=a[i][j]*p-a[i][k]*a[k][j];
          assert(num%previous===0n,"Bareiss exact division");
          a[i][j]=num/previous;
        }
        a[i][k]=0n;
      }
      previous=p;
    }
    return sign*a[n-1][n-1];
  }
  const selected=[0,1,2,3,4,10];
  const sixMinor=determinant(axes.map(i=>selected.map(j=>vectors[j][i])));
  assert(sixMinor===-3n,"six by six rank witness");
  for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(i!==j){
    const remain=axes.filter(k=>k!==i&&k!==j),[a,b]=remain;
    const S=vec([i,a,b]),T=vec([j,a,b]);
    assert(axes.every(k=>S[k]-T[k]===(k===i?1:k===j?-1:0)),"difference generators");
  }
  const edges=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
  const stars=axes.slice(0,4).map(v=>edges.map(e=>e.includes(v)?1:0));
  const starMinor=determinant([0,1,2,3].map(i=>stars.map(x=>x[i])));
  assert(starMinor===2n,"STAR rank four witness");
  const branches=[...vectors,...vectors.map(x=>x.map(t=>-t))];
  const add=(a,b)=>a.map((v,i)=>v+b[i]);
  const twice=new Map();
  for(const a of branches)for(const b of branches){
    const k=key(add(a,b));twice.set(k,(twice.get(k)||0)+1);
  }
  const histogram=new Map();let total=0,Z4=0;
  for(const v of twice.values()){
    histogram.set(v,(histogram.get(v)||0)+1);
    total+=v;Z4+=v*v;
  }
  assert(total===1600&&twice.size===423&&twice.get("0,0,0,0,0,0")===40,"m2 DP");
  assert(Z4===11160,"m4 return count");
  const histObj=Object.fromEntries([...histogram].sort((a,b)=>a[0]-b[0]).map(([k,v])=>[String(k),v]));
  assert(JSON.stringify(histObj)==='{"1":40,"2":200,"4":90,"6":60,"12":30,"20":2,"40":1}',"histogram");
  const D=Array(6).fill(1),S=vec([0,1,2]),Sc=vec([3,4,5]);
  assert(key(add(S,Sc))===key(D),"complement depth");
  assert(key(add(S,S.map(x=>-x)))===key(Array(6).fill(0)),"zero depth");
  const relative=x=>x.map(v=>v-Math.min(...x));
  assert(key(relative(D))===key(relative(Array(6).fill(0))),"relative collision");
  return {
    schema:"R762HC_S6_TRIAD_GATE_AND_LATTICE_EVIDENCE_V1",
    frozen_scientific_commit:"a72226e2430ffa4786321ac86e7f0c599d5f0389",
    population:{native_axes:6,unoriented_unsigned_triples:20,axis_permutations:720,ordered_two_axis_inputs:pairInputs,stabilizer_size:24,stabilizer_tests:stabilizerChecks,completions_per_pair:4},
    lattice:{six_by_six_selected_column_indices:selected,six_by_six_determinant:sixMinor.toString(),integer_image:"{y in Z^6 : sum_i y_i = 0 (mod 3)}",smith_factors:[1,1,1,1,1,3],full_rank:6,k4_star_rank:4,k4_star_four_minor:starMinor.toString()},
    positive_brc:{signed_triple_branches_per_event:40,length_2_source_count:1600,length_2_endpoint_count:twice.size,length_2_multiplicity_histogram:histObj,length_2_zero_return:40,length_4_zero_return:Z4,odd_length_zero_return:0},
    observer_collision:{event_length:2,first_ordered_event_sequence:["+{0,1,2}","+{3,4,5}"],first_full_endpoint:D,second_ordered_event_sequence:["+{0,1,2}","-{0,1,2}"],second_full_endpoint:Array(6).fill(0),same_relative_readout:true},
    scope:"Candidate signed three-axis composite translations and S6 axis-label skeleton; NOT a native TRIADIC_CLOSURE_E admission or force-balance proof",
    verification:"AUTHOR_EXACT_ENUMERATION_PASS; INDEPENDENT_REVIEW_NOT_REVIEWED"
  };
})();
console.log(JSON.stringify(evidence, null, 2));
