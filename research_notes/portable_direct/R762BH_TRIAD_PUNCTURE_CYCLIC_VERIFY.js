"use strict";
// Exact finite certificate for R762BH. Node.js >=18; no dependencies.
function verify() {
  const assert=(ok,msg)=>{if(!ok)throw new Error("ASSERT: "+msg)};
  const choose3=[]; for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)for(let c=b+1;c<6;c++)choose3.push([a,b,c]);
  const rows=choose3.map(t=>t.reduce((s,i)=>s|(1<<i),0));
  const pc=x=>{let s=0;while(x){x&=x-1;s++}return s};
  const weight=(x,rr)=>rr.reduce((n,r)=>n+((pc(x&r))&1),0);
  const enumerator=rr=>{let h={};for(let x=0;x<64;x++){let w=weight(x,rr);h[w]=(h[w]||0)+1;}return h;};
  const rank=rr=>{let bs={};for(const r of rr){let x=r;while(x){let b=31-Math.clz32(x);if(bs[b]===undefined){bs[b]=x;break;}x^=bs[b];}}return Object.keys(bs).length};
  const sep=rr=>Math.min(...Array.from({length:63},(_,k)=>weight(k+1,rr)));
  assert(rows.length===20,"20 triples");
  const full=enumerator(rows);
  assert(JSON.stringify(full)===JSON.stringify({0:1,8:15,10:32,12:15,20:1}),"20 row enumerator");
  assert(rank(rows)===6 && sep(rows)===8,"[20,6,8]");
  const triple=(m)=>choose3[rows.indexOf(m)].map(i=>i+1).join("");
  const singletonRemovals={};
  for(let i=0;i<20;i++){
    const punct=rows.filter((_,j)=>j!==i),d=sep(punct);
    singletonRemovals[d]=(singletonRemovals[d]||0)+1;
    assert(rank(punct)===6 && d===7,"all 19-row codes [19,6,7]");
  }
  assert(singletonRemovals[7]===20,"single deleted all7");
  const exemplar19=enumerator(rows.slice(1));
  assert(JSON.stringify(exemplar19)===JSON.stringify({0:1,7:6,8:9,9:16,10:16,11:9,12:6,19:1}),"19-row enumerator");
  const pairRemovals={}, pairWitnessByIntersection={},pairCountsByIntersection={};
  for(let i=0;i<20;i++)for(let j=i+1;j<20;j++){
    const punct=rows.filter((_,k)=>k!==i&&k!==j),d=sep(punct);
    pairRemovals[d]=(pairRemovals[d]||0)+1;
    assert(d===6 && rank(punct)===6,"all 18-row codes [18,6,6]");
    const intersection=pc(rows[i]&rows[j]);
    const witnesses=Array.from({length:64},(_,x)=>x).filter(x=>pc(x)===4 && pc(x&rows[i])%2 && pc(x&rows[j])%2).length;
    pairCountsByIntersection[intersection]=(pairCountsByIntersection[intersection]||0)+1;
    const key=intersection+":"+witnesses;
    pairWitnessByIntersection[key]=(pairWitnessByIntersection[key]||0)+1;
  }
  assert(pairRemovals[6]===190,"all double deletions d6");
  assert(pairWitnessByIntersection["0:6"]===10 && pairWitnessByIntersection["1:2"]===90 && pairWitnessByIntersection["2:2"]===90 && Object.keys(pairWitnessByIntersection).length===3,"pair witnesses by overlap");
  const rotate=(r,s)=>{let out=0;for(let i=0;i<6;i++)if(r&(1<<i))out|=1<<((i+s)%6);return out};
  const remaining=new Set(rows),orbits=[];
  while(remaining.size){
    const m=Math.min(...remaining);
    const orbit=Array.from(new Set(Array.from({length:6},(_,i)=>rotate(m,i)))).sort((a,b)=>a-b);
    for(const r of orbit)remaining.delete(r);
    orbits.push(orbit);
  }
  orbits.sort((a,b)=>a.length-b.length || a[0]-b[0]);
  assert(orbits.length===4 && orbits.map(o=>o.length).join(",")==="2,6,6,6","C6 orbit sizes");
  const orbitClassification=[];
  for(let selection=0;selection<16;selection++){
    const subset=orbits.filter((_,i)=>selection&(1<<i)).flat();
    const observedRank=rank(subset),distance=sep(subset);
    orbitClassification.push({selector:selection.toString(2).padStart(4,"0"),query_count:subset.length,rank:observedRank,orientation_separation_distance:distance,weight_histogram:enumerator(subset)});
    if(selection!==15)assert(distance<=6,"proper C6 invariant family cannot correct three");
  }
  assert(orbitClassification[14].query_count===18 && orbitClassification[14].orientation_separation_distance===6,"18 C6 rows");
  return {
    schema:"R762BH_EXACT_TRIAD_PUNCTURE_ORBIT_EVIDENCE_V1",
    assumptions:"Conditional BG incidence observer A_T(x)=sum_{i in T}x_i mod 2 over F2, six labeled axes, all twenty candidate triples; no native TRIADIC_CLOSURE_E sign authorization asserted",
    full_code:{length:20,dimension:6,distance:8,weight_histogram:full},
    arbitrary_deleted_queries:{one_deleted:{cases:20,minimum_distance_histogram:singletonRemovals,rank_always:6,example_weight_histogram:exemplar19},two_deleted:{cases:190,minimum_distance_histogram:pairRemovals,rank_always:6}},
    pair_weight8_witness_count_by_triple_intersection:pairWitnessByIntersection,
    pair_type_counts:pairCountsByIntersection,
    cyclic_orbits:orbits.map((o,i)=>({id:i,size:o.length,triples:o.map(triple)})),
    orbit_union_classification:orbitClassification,
    conclusion:{minimum_queries_to_correct_three_bit_errors_without_symmetry:19,minimum_queries_with_cyclic_C6_orbit_invariance:20,all_18_probe_subsets_have_distance:6,all_19_probe_subsets_have_distance:7,verification:"Exact exhaustive integer and Boolean enumeration"},
    code_status:"EXACT_ENUMERATION_PASS",
    scientific_status:"AUTHOR_PROVED_AND_EXACT_CHECKED_NOT_REVIEWED"
  };
}
const evidence=verify();
console.log(JSON.stringify(evidence,null,2));
