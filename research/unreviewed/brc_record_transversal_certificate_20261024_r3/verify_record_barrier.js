// EM BRC fixed auxiliary model, exact BigInt certificate; run: node verify_record_barrier.js
// Author-side only; no P000 native transfer, formal task/Driver authority or acceptance.
const verify = function verify() {
  const Q=[[1n,665n,1n,333n],[333n,333n,1n,333n],[1n,1n,1n,997n]];
  const edges=[[0,1],[1,2],[1,3],[2,3]], deg=[1n,3n,2n,2n], actions=[0,2,3];
  const T=[
    [690,684,676,661,635,588,503,354,111],
    [682,670,649,613,546,427,226,0,0],
    [661,632,580,486,323,61,0,0,0],
    [608,534,403,185,0,0,0,0,0],
    [467,289,8,0,0,0,0,0,0],
    [140,0,0,0,0,0,0,0,0],
    ...Array.from({length:10},()=>[1,0,0,0,0,0,0,0,0])
  ];
  const barriers=[
    [15,0,0,0,12],[2,5,60,1,2],[0,8,110,2,17],[3,3,184,1,2],
    [1,6,225,2,30],[2,4,322,2,60],[0,7,353,2,15],[3,2,402,2,139],
    [1,5,426,2,30],[2,3,485,2,66],[0,6,502,2,17],[3,1,533,2,176],
    [1,4,545,2,36],[2,2,579,2,86],[0,5,587,2,22],[3,0,607,2,353],
    [1,3,612,2,49],[2,1,631,2,129],[0,4,634,2,30],[1,2,648,2,73],
    [2,0,660,2,241],[0,3,660,2,44],[1,1,669,2,116],[0,2,675,2,68],
    [1,0,681,2,220],[0,1,683,2,112],[0,0,689,2,214]
  ];
  const records=[[4,2,7],[5,0,139],[4,0,466],[4,1,288]];
  function ensure(x,msg){if(!x)throw Error(msg);}
  const powMemo=new Map(),numMemo=new Map();
  function pow(x,n){const k=x.toString()+":"+n; if(!powMemo.has(k))powMemo.set(k,x**BigInt(n));return powMemo.get(k);}
  const pairWeights=Q.map(row=>edges.map(([i,j])=>row[i]+row[j]));
  const N=c=>c[0]+c[1]+c[2],key=c=>c.join(",");
  function numerator(c){
    const k=key(c);if(numMemo.has(k))return numMemo.get(k);
    let value=0n;
    for(let e=0;e<4;e++)value+=pow(pairWeights[0][e],c[0])*pow(pairWeights[1][e],c[1])*pow(pairWeights[2][e],c[2]);
    for(let i=0;i<4;i++)value-=deg[i]*pow(Q[0][i],c[0])*pow(Q[1][i],c[1])*pow(Q[2][i],c[2]);
    numMemo.set(k,value);return value;
  }
  function hall(c){
    const V=Array.from({length:4},(_,i)=>pow(Q[0][i],c[0])*pow(Q[1][i],c[1])*pow(Q[2][i],c[2]));
    const B=Array.from({length:4},(_,i)=>pow(pairWeights[0][i],c[0])*pow(pairWeights[1][i],c[1])*pow(pairWeights[2][i],c[2]));
    for(let a=0;a<3;a++){
      const demand=Array.from({length:4},(_,i)=>deg[i]*(1000n-Q[a][i])*V[i]);
      const cap=edges.map(([i,j],e)=>(1000n-Q[a][i]-Q[a][j])*B[e]);
      for(let mask=1;mask<16;mask++){
        let lhs=0n,rhs=0n;
        for(let e=0;e<4;e++)if((mask&(1<<edges[e][0]))||(mask&(1<<edges[e][1])))lhs+=cap[e];
        for(let i=0;i<4;i++)if(mask&(1<<i))rhs+=demand[i];
        if(lhs<rhs)return false;
      }
    }return true;
  }
  for(let a=0;a<16;a++)for(let b=0;b<9;b++){
    const t=T[a][b];
    ensure(hall([a,b,t]),"Hall threshold upper "+[a,b,t]);
    if(t)ensure(!hall([a,b,t-1]),"Hall threshold lower "+[a,b,t-1]);
  }
  for(const c of [[16,0,0],[0,9,0],[0,0,690]])ensure(hall(c),"Pure-axis Hall base "+c);
  const failures=new Set();
  for(let a=0;a<16;a++)for(let b=0;b<9;b++)for(let k=0;k<T[a][b];k++)failures.add(key([a,b,k]));
  ensure(failures.size===14102,"Failure count");
  const maxima=[...failures].map(s=>s.split(",").map(Number)).filter(c=>[0,1,2].every(i=>{
    const p=c.slice();p[i]++;return !failures.has(key(p));
  })).sort((a,b)=>key(a).localeCompare(key(b)));
  ensure(maxima.length===31,"Maxima count");
  const seen=new Set([...barriers.map(b=>key(b.slice(0,3))),...records.map(key)]);
  ensure(seen.size===31&&maxima.every(c=>seen.has(key(c))),"Maxima partition");
  function compare(p,c){ensure(p.every((x,i)=>x<=c[i]),"Prefix out of box");return numerator(p)*pow(1000n,N(c)-N(p))-numerator(c);}
  let bchecks=0,wchecks=0;
  const barrierEvidence=[];
  for(const [a,b,d,axis,level] of barriers){
    const target=[a,b,d]; ensure(level>=1&&level<=target[axis],"Layer range");
    let minimum=null,minPoint=null,count=0;
    for(let x=0;x<=a;x++)for(let y=0;y<=b;y++)for(let z=0;z<=d;z++){
      const p=[x,y,z];if(p[axis]!==level)continue;
      const gap=compare(p,target);ensure(gap>0n,"Barrier failed at "+[target,p]);
      if(minimum===null||gap<minimum){minimum=gap;minPoint=p;}
      count++;
    }
    bchecks+=count;
    barrierEvidence.push({terminal_count:target,axis_action:actions[axis],level,
      checked_points:count,min_gap_at:minPoint,min_gap_numerator:minimum.toString(),
      gap_denominator:"1000^"+N(target)});
  }
  ensure(bchecks===1094,"Barrier count");
  const recordEvidence=[];
  for(const target of records){
    const word="3".repeat(target[2])+"2".repeat(target[1])+"0".repeat(target[0]);
    let c=[0,0,0],minimum=null,minPoint=null;
    for(let t=0;t<word.length;t++){
      c[actions.indexOf(Number(word[t]))]++;
      if(t===word.length-1){ensure(key(c)===key(target),"Word terminal");continue;}
      const gap=-compare(c,target);ensure(gap>0n,"Prefix record at "+[target,c]);
      if(minimum===null||gap<minimum){minimum=gap;minPoint=c.slice();}
      wchecks++;
    }
    recordEvidence.push({terminal_count:target,block_word:`3^${target[2]} 2^${target[1]} 0^${target[0]}`,
      checked_prefixes:word.length-1,min_gap_at:minPoint,min_gap_numerator:minimum.toString(),
      gap_denominator:"1000^"+N(target)});
  }
  ensure(wchecks===916,"Witness count");
  function maskOccupancyNum(c){
    let mass=Array.from({length:16},(_,i)=>i===0?1n:0n);
    for(const a of [2,1,0])for(let t=0;t<c[a];t++){
      const nxt=Array(16).fill(0n);
      for(let mask=0;mask<16;mask++)if(mass[mask]!==0n)for(let i=0;i<4;i++)nxt[mask|(1<<i)]+=mass[mask]*Q[a][i];
      mass=nxt;
    }
    return edges.reduce((acc,[i,j])=>acc+mass[(1<<i)|(1<<j)],0n);
  }
  const crosscheck=new Map();
  for(const e of barrierEvidence)crosscheck.set(key(e.min_gap_at),e.min_gap_at);
  for(const e of recordEvidence){crosscheck.set(key(e.terminal_count),e.terminal_count);crosscheck.set(key(e.min_gap_at),e.min_gap_at);}
  for(const c of crosscheck.values())ensure(numerator(c)===maskOccupancyNum(c),"Mask mismatch "+c);
  ensure(crosscheck.size===32,"Mask coverage");
  return {schema:"EM_BRC_RECORD_TRANSVERSAL_EXACT_V1",status:"PASS",
    model:{labels:[0,1,2,3],actions,good_edges:edges,integer_weights_denominator:1000,weights:Q.map(r=>r.map(Number))},
    dependence:"Fixed-model Hall heredity and threshold description as specified; original Result not independently admitted",
    hall_threshold_columns:144,all_length_hall_failures:failures.size,maximal_hall_failures:31,
    barrier_certificate_count:barrierEvidence.length,barrier_inequalities:bchecks,
    ordered_record_witnesses:recordEvidence.length,strict_record_prefix_inequalities:wchecks,
    total_strict_inequalities:bchecks+wchecks,independent_mask_dp_crosschecks:crosscheck.size,
    maximal_fail_count_vectors:maxima,barriers:barrierEvidence,record_witnesses:recordEvidence,
    mathematical_status:"AUTHOR_PROVED_WITH_EXACT_INTEGER_CHECKS_UNREVIEWED_NOT_ADMITTED"};
};
console.log(JSON.stringify(verify(),null,2));
