// Exact integer observer-model certificate; source pin enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34
function verify(){
  "use strict";
  const N=1000,M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
  const A=[0,0,0,1,1,1],B=[2,2,3,2,2,4],C=[5,6,7,8,9,10],G=[0,0,1,2,2,3];
  const PAIRS=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12","12 12 24 34","12 13 23 24","23 34 12 13","24 34 12 14"];
  const FREES=["2/5 0 3/5 0;2/5 2/5 0 1/5;2/5 0 0 3/5;3/5 2/5 0 0","1/2 1/2 0 0;1/2 0 0 1/2;0 0 1/2 1/2;0 0 1/2 1/2","0 1/2 1/2 0;0 1 0 0;0 1 0 0;0 0 1/2 1/2"];
  const names=["D1","D2","D3","D4","D6","D7","D8","K1","K2","K3"];
  const check=(v,msg)=>{if(!v)throw Error(msg)};
  const scaled=x=>{const [p,q="1"]=String(x).split("/").map(Number);const y=N*p/q;check(Number.isSafeInteger(y),"nonintegral rational: "+x);return y;};
  const mix=rows=>M.map((weights,i)=>[0,1,2,3].map(j=>{const v=weights.reduce((sum,w,k)=>sum+w*rows[k][j],0);check(v%20===0,"mix: "+i);return v/20}));
  const kernel=rows=>{check(rows.length===4&&rows.every(row=>row.length===4&&row.every(x=>Number.isSafeInteger(x)&&x>=0)&&row.reduce((x,y)=>x+y,0)===N),"invalid kernel");return mix(G.map(k=>rows[k]));};
  const pair=s=>kernel(s.split(" ").map(word=>[1,2,3,4].map(j=>N*[...word].filter(c=>+c===j).length/2)));
  const free=s=>kernel(s.split(";").map(row=>row.trim().split(/\s+/).map(scaled)));
  const bank=[...PAIRS.filter((_,i)=>i!==4).map(pair),...FREES.map(free)];
  function prep(s,t,u){
    const z=[s,t,u,0,0,N,0,0,0,0,0];
    const sources=A.map((a,i)=>{
      const x=z[a],b=z[B[i]],c=z[C[i]];
      const mid=(N-x)*b/N,tail=(N-x)*(N-b)/N,third=tail*c/N;
      check([mid,tail,third].every(Number.isSafeInteger),"nonintegral causal source");
      return [x,mid,third,tail-third];
    });
    check(sources.every(row=>row.reduce((a,b)=>a+b,0)===N),"non-normalized original source");
    return mix(sources);
  }
  const risk2=(p,q)=>Math.max(...p.map((row,i)=>row.reduce((sum,v,j)=>sum+Math.abs(v-q[i][j]),0)));
  const riskMap=p=>Object.fromEntries(names.map((name,i)=>[name,risk2(p,bank[i])]));
  const p0=prep(600,300,0),pm=prep(600,300,500),p1=prep(600,300,1000);
  const expected=[[600,200,100,100],[600,200,90,110],[600,0,0,400],[300,350,0,350],[300,350,0,350],[300,0,0,700]];
  check(JSON.stringify(pm)===JSON.stringify(expected),"wrong six positive-source observed rows");
  const r0=riskMap(p0),rm=riskMap(pm),r1=riskMap(p1);
  const exactAtCenter=[1600,2000,2000,1400,1300,1420,1400,1400,1300,2000];
  check(names.every((n,i)=>rm[n]===exactAtCenter[i]),"wrong all-ten interior risks");
  check(r0.K2===1000&&rm.K2===1300&&rm.D6===1300&&r1.D6===1000,"wrong edge-cover endpoint risks");
  check(Math.min(...Object.values(rm))===1300,"wrong interior minimum");
  check(p0.every((row,i)=>row.every((v,j)=>2*pm[i][j]===v+p1[i][j])),"nonaffine edge");
  const cubeVertices=[];
  for(const s of [0,N])for(const t of [0,N])for(const u of [0,N]){
    const risk2Value=Math.min(...Object.values(riskMap(prep(s,t,u))));
    check(risk2Value<=1200,"cube vertex not covered at 3/5");
    cubeVertices.push({s:s/N,t:t/N,u:u/N,bank_risk2:risk2Value});
  }
  check(cubeVertices.length===8,"missing cube vertices");
  return {
    pass:"PASS_BRC_N4_S23_SHARED_CAUSAL_EDGE_UNIQUE_MAX_13_20_20261102",
    scientific_source_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
    population:"six separately labeled positive-weight sources AU0,AU1,AV,BU0,BU1,BV",
    bank:names,probability_scale:N,risk2_denominator:2*N,
    family:"z(s,t,u)=(s,t,u,0,0;1,0,0,0,0,0) for s,t,u in [0,1]",
    causal_edge:"s=3/5,t=3/10,0<=u<=1",
    prepared_six_at_u_half:pm,risk2_all_ten_at_u_half:rm,
    endpoint_risk2:{K2_at_0:r0.K2,K2_at_half:rm.K2,D6_at_half:rm.D6,D6_at_1:r1.D6},
    cube_vertices:cubeVertices,
    analytic_certificate:"For u<=1/2, K2 TV <= 1/2+3u/10; for u>=1/2, D6 TV <=4/5-3u/10, by convexity. Both strictly below 13/20 outside u=1/2. At u=1/2, all ten TV >=13/20.",
    exact_edge_maximum:"13/20",unique_maximizer:"u=1/2",
    open_region:"m(s,t,u)>=13/20-max(|s-3/5|,|t-3/10|)-|u-1/2|; region with loss<1/20 violates radius 3/5",
    status:"author exact integer certificate; unreviewed/not admitted"
  };
}
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(verify(),null,2));
