function verify(){
  const popcnt = x=>{let n=0;while(x){x&=x-1;n++;}return n};
  const assert=(yes,msg)=>{if(!yes)throw Error("R762BL assertion: "+msg)};
  const triples=[];
  for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)for(let c=b+1;c<6;c++)triples.push([a,b,c]);
  assert(triples.length===20,"20 triples");
  const cuts=[];
  for(let S=1;S<63;S++)if(S<(S^63)){
    let mask=0;
    for(let i=0;i<20;i++){const T=triples[i],k=T.reduce((s,v)=>s+((S>>v)&1),0);if(k>0&&k<3)mask|=1<<i}
    cuts.push({S,mask})
  }
  assert(cuts.length===31,"31 nontrivial cuts modulo complement");
  const minRows=Array(11).fill(100),optCount=Array(11).fill(0),witness=Array(11).fill(0),regularCount=Array(11).fill(0),hist=Array(11).fill(0);
  for(let H=0;H<(1<<20);H++){
    let d=20;
    for(const v of cuts){const z=popcnt(H&v.mask);if(z<d)d=z;if(d===0)break}
    assert(d>=0&&d<=10,"distance cap");
    hist[d]++;
    let m=popcnt(H);
    for(let q=0;q<=d;q++){
      if(m<minRows[q]){minRows[q]=m;optCount[q]=1;witness[q]=H}
      else if(m===minRows[q])optCount[q]++;
    }
    if((m&1)===0){
      const q=m/2;
      if(q<=10){
        const degrees=Array(6).fill(0);
        for(let i=0;i<20;i++)if((H>>i)&1)for(const v of triples[i])degrees[v]++;
        if(degrees.every(x=>x===q))regularCount[q]++;
      }
    }
  }
  assert(hist.reduce((a,b)=>a+b,0)===1<<20,"subset coverage");
  const expectedRows=[0,3,4,6,8,10,12,14,16,18,20];
  const expectedCounts=[1,480,75,330,780,1044,780,330,75,10,1];
  const expectedHist=[5944,51945,177522,305965,291301,158031,48795,8307,735,30,1];
  assert(JSON.stringify(minRows)===JSON.stringify(expectedRows),"minimal rows");
  assert(JSON.stringify(optCount)===JSON.stringify(expectedCounts),"optimal counts");
  assert(JSON.stringify(hist)===JSON.stringify(expectedHist),"distance histogram");
  for(let q=2;q<=10;q++)assert(regularCount[q]===optCount[q],"regular designs q="+q);
  assert(regularCount[1]===10,"degree-one designs are two disjoint triples");
  const chartStates=[];
  for(let code=0;code<243;code++){
    let x=code,z=[0];
    for(let j=0;j<5;j++){z.push(x%3-1);x=Math.floor(x/3)}
    chartStates.push(z)
  }
  let exactRowComparisons=0,minimumObservedDistance=20;
  const reads=chartStates.map(z=>triples.map(T=>{
    const a=T.map(i=>z[i]);const lo=Math.min(...a);return a.map(x=>x-lo).join(",");
  }));
  for(let a=0;a<243;a++)for(let b=a+1;b<243;b++){
    const diff=chartStates[a].map((v,i)=>v-chartStates[b][i]);
    let d1=0,d2=0;
    for(let i=0;i<20;i++){
      const T=triples[i];
      const equality=diff[T[0]]===diff[T[1]]&&diff[T[1]]===diff[T[2]];
      d1+=!equality;
      d2+=reads[a][i]!==reads[b][i];
      exactRowComparisons++;
    }
    assert(d1===d2,"can3 row equality");
    if(d2<minimumObservedDistance)minimumObservedDistance=d2;
  }
  assert(minimumObservedDistance===10,"complete 20-row minimum distance");
  const completeCuts=[1,3,7].map(S=>({partition_size:popcnt(S),crossing_rows:popcnt(cuts.find(c=>c.S===S).mask)}));
  assert(JSON.stringify(completeCuts.map(x=>x.crossing_rows))===JSON.stringify([10,16,18]),"cut sizes");
  const thresholds=Array.from({length:11},(_,q)=>({q,min_rows:minRows[q],number_of_optimal_designs:optCount[q],witness_bitmask:"0x"+witness[q].toString(16),witness_rows:triples.filter((T,i)=>(witness[q]>>i)&1).map(T=>T.map(x=>x+1).join("")),regular_hypergraph_count:regularCount[q]}));
  return {schema:"R762BL_EXACT_COORDINATE_TRIAD_ROW_CODE_EVIDENCE_V1",status:"EXACT_FINITE_CHECKED",source_pinned:"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",method:"complete 2^20 selection enumeration, 31 complementary cut classes, independently checked against normalized signed integer triples on 243 anchored chart states",triples:triples.map(T=>T.map(i=>i+1).join("")),number_of_observation_sets:1<<20,cut_representatives:31,distance_histogram:hist,thresholds,complete_design_cut_sizes:completeCuts,chart_states_checked:243,chart_pair_count:243*242/2,exact_row_comparisons:exactRowComparisons,complete_design_empirical_minimum_distance:minimumObservedDistance,proof_scope:"all Z^6/diagonal chart states by cut theorem; finite program checks all H and finite chart consistency; official triadic force event authorization not claimed",review:"NOT_REVIEWED"};
}

const report=verify();
console.log(JSON.stringify(report,null,2));
