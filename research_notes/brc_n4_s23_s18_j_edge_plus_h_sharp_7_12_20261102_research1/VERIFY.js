function verify(){
  "use strict";
  const N=50400,RN=7*N/6;
  const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
  const A=[0,0,0,1,1,1],B=[2,2,3,2,2,4],C=[5,6,7,8,9,10],G=[0,0,1,2,2,3];
  const PAIRS=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12","12 12 24 34","12 13 23 24","23 34 12 13","24 34 12 14"];
  const K1="5/12 0 7/12 0;5/12 5/12 0 1/6;5/12 0 1/6 5/12;5/12 55/126 0 37/252";
  const K2="1/2 1/2 0 0;1/2 0 0 1/2;0 0 1/2 1/2;0 0 1/2 1/2";
  const K3="0 1/2 1/2 0;0 1 0 0;0 1 0 0;0 0 1/2 1/2";
  function assert(x,message){if(!x)throw Error(message)}
  function val(s){let [a,b="1"]=String(s).split("/").map(Number);let x=N*a/b;assert(Number.isSafeInteger(x),"non-integral input "+s);return x}
  function mix(rows){return M.map((m,i)=>[0,1,2,3].map(j=>{let num=m.reduce((tot,w,s)=>tot+w*rows[s][j],0);assert(Number.isSafeInteger(num/20),"mixture "+i);return num/20}))}
  function kernel(rows){assert(rows.length===4 && rows.every(row=>row.length===4 && row.every(x=>x>=0) && row.reduce((a,b)=>a+b,0)===N),"kernel stochastic");return mix(G.map(g=>rows[g]))}
  function pair(s){return kernel(s.split(" ").map(token=>[1,2,3,4].map(j=>N*[...token].filter(t=>Number(t)===j).length/2)))}
  function free(s){return kernel(s.split(";").map(row=>row.trim().split(/\s+/).map(val)))}
  const fixed=PAIRS.filter((_,i)=>i!==4).map(pair), frees=[K1,K2,K3].map(free), bank=[...fixed,...frees];
  function prepare(z){
    z=z.map(val);assert(z.length===11 && z.every(x=>x>=0&&x<=N),"strategy");
    const src=A.map((a,s)=>{
      const x=z[a],b=z[B[s]],c=z[C[s]],remaining=N-x,q=remaining*(N-b)/N,t=q*c/N,second=remaining*b/N;
      assert([q,t,second].every(Number.isSafeInteger),"causal rational");
      return [x,second,t,q-t];
    });return mix(src);
  }
  function risk(p,q){return Math.max(...p.map((row,i)=>row.reduce((sum,x,j)=>sum+Math.abs(x-q[i][j]),0)))}
  function j(t){return prepare([1,t,0,0,0,0,0,0,0,1,0])}
  function O(s,t){return [s,t,0,0,0,0,1,1,1,0,1]}
  function Zt(s,t){return [s,t,0,0,0,1,0,0,0,0,0]}
  const raw={
    W:[1,0,0,0,1,0,0,0,0,0,0],J:[1,"1/3",0,0,0,0,0,0,0,1,0],
    A:O("1/7",1),B:O(1,"1/7"),C:Zt("1/7",1),X:O(1,"1/15"),
    Y:[1,0,0,0,0,0,0,0,1,1,1],Z:[0,1,0,1,0,1,1,0,0,0,0]
  };
  const OFF=["00000000000","00000001000","00000000001","00101000000","00110000000","00101001000","00100000001","00100000000"];
  OFF.forEach((bits,i)=>raw["T"+(i+1)]=[...bits].map(Number));
  raw.U=[..."00110000001"].map(Number);raw.V=[..."10000000000"].map(Number);
  raw.H=["1/4",1,0,0,0,1,0,0,0,0,0];
  const pol=Object.fromEntries(Object.entries(raw).map(([n,z])=>[n,prepare(z)]));
  const minrisk=Object.fromEntries(Object.entries(pol).map(([n,p])=>[n,Math.min(...bank.map(q=>risk(p,q)))]));
  assert(Object.keys(minrisk).length===19,"19 policies");
  assert(Math.max(...Object.values(minrisk))===RN && Object.values(minrisk).every(x=>x<=RN),"S18+H sharp upper");
  const endpoint={K2_J0:risk(j(0),frees[1]),K2_J1_3:risk(j("1/3"),frees[1]),K1_J1_3:risk(j("1/3"),frees[0]),K1_J1:risk(j(1),frees[0])};
  assert(Object.values(endpoint).every(x=>x<=RN),"real J endpoints");
  assert([0,1,2,3].every(k=>{
    const t=j(`${k}/3`),p0=j(0),p1=j(1);
    return t.every((row,i)=>row.every((x,l)=>3*x===(3-k)*p0[i][l]+k*p1[i][l]));
  }),"affine J prepared rows");
  const core=["W","B","Y","Z","T5","U","V","H","J1","Jm"];
  const coreP=core.map(n=>n==="J1"?j(1):n==="Jm"?j("1/6"):pol[n]);
  const fixedMin=coreP.map(p=>Math.min(...fixed.map(q=>risk(p,q))));
  assert(Math.min(...fixedMin)===RN && fixedMin.every(x=>x>=RN),"all ten need free below 7/12");
  const forbidden=[];let potential=0;
  for(let a=0;a<core.length;a++)for(let b=a+1;b<core.length;b++)for(let c=b+1;c<core.length;c++){
    potential++;
    const best=Math.max(...[0,1,2,3,4,5].map(i=>[0,1,2,3].reduce((sum,k)=>sum+Math.max(coreP[a][i][k],coreP[b][i][k],coreP[c][i][k]),0)-N));
    if(best*12>=21*N)forbidden.push([a,b,c]);
  }
  assert(potential===120 && forbidden.length===87,"triple certificate counts");
  let assignments=0,minHits=Infinity;
  for(let code=0;code<3**core.length;code++){
    let x=code,labels=[];
    for(let i=0;i<core.length;i++){labels.push(x%3);x=Math.floor(x/3)}
    const hits=forbidden.reduce((s,[a,b,c])=>s+(labels[a]===labels[b]&&labels[b]===labels[c]?1:0),0);
    assert(hits>=1,"missing lower coloring "+code);
    minHits=Math.min(minHits,hits);assignments++;
  }
  assert(assignments===59049 && minHits===1,"all colorings");
  const next=prepare(["1/5",1,0,0,0,1,0,0,0,0,0]);
  const nextRisks=bank.map(q=>risk(next,q));
  assert(Math.min(...nextRisks)*5===6*N,"H(1/5) bank risk 3/5");
  assert([...Object.values(pol),...bank,j(0),j(1)].every(p=>p.every(row=>row.every(x=>x>=0)&&row.reduce((s,x)=>s+x,0)===N)),"stochastic mixed row");
  const gcd=(a,b)=>b?gcd(b,a%b):a;
  const ratio=x=>{const d=gcd(x,2*N);return x/d+"/"+(2*N/d)};
  return {
    pass:"PASS_BRC_N4_S23_S18_FULL_J_EDGE_PLUS_H_SHARP_7_12_20261102",
    scientific_source_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
    integer_probability_scale:N,total_variation_denominator:2*N,sharp_radius:"7/12",
    original_six_sources:["AU0","AU1","AV","BU0","BU1","BV"],shared_parameter:"b_U",
    seven_fixed_decoders:["D1","D2","D3","D4","D6","D7","D8"],
    three_free_kernels:{K1,K2,K3},
    S18_plus_H_min_risks:Object.fromEntries(Object.entries(minrisk).map(([k,v])=>[k,ratio(v)])),
    J_edge_endpoint_risks:Object.fromEntries(Object.entries(endpoint).map(([k,v])=>[k,ratio(v)])),
    real_J_certificate:"K2 covers every real t in [0,1/3]; K1 covers every real t in [1/3,1] by TV convexity",
    lower_core:core,lower_fixed_min_risks:Object.fromEntries(core.map((n,i)=>[n,ratio(fixedMin[i])])),
    lower_forbidden_triples:forbidden.length,all_triples:potential,
    all_three_label_allocations_checked:assignments,min_monochromatic_bad_triples:minHits,
    next_bank_counterexample:"H(1/5)=(1/5,1,0,0,0;1,0,0,0,0,0)",
    next_bank_all_risks:nextRisks.map(ratio),next_bank_min_risk:ratio(Math.min(...nextRisks)),
    arithmetic:"safe exact integers; all divisions checked; original six positive-source mixtures",
    evidence_status:"AUTHOR_EXACT_COMPUTATION_UNREVIEWED_NOT_ADMITTED"
  };
}
if(typeof require!=='undefined' && require.main===module){console.log(JSON.stringify(verify(),null,2));}
