/* X6 Unit162 exact integer signed-axis cycle checker; Node.js 18+ */
const check = function check(){
  const d=6, lim=2, vectors=5**d;
  const T=x=>[-x[5],x[0],x[1],x[2],x[3],x[4]];
  const neg=x=>x.map(v=>-v);
  const eq=(a,b)=>a.every((v,i)=>v===b[i]);
  const sq=x=>x.reduce((v,a)=>v+a*a,0);
  const L=x=>x.reduce((v,a)=>v+Math.abs(a),0);
  const fact=n=>{let q=1n;for(let k=2;k<=n;k++)q*=BigInt(k);return q};
  const brc=x=>{let v=fact(L(x));for(const t of x)v/=fact(Math.abs(t));return v};
  const E=Array.from({length:12},(_,j)=>Array.from({length:6},(_,i)=>(i===j%6?(j<6?1:-1):0)));
  let e=E[0],orbit=[];
  for(let j=0;j<12;j++){orbit.push(e.join(","));e=T(e)}
  if(!eq(e,E[0]) || new Set(orbit).size!==12)throw Error("direction orbit not regular C12");
  let inspected=0, powerChecks=0, edgeChecks=0, maxL=0;
  for(let code=0;code<vectors;code++){
    let n=code,v=[];
    for(let j=0;j<d;j++){v.push(n%5-2);n=Math.floor(n/5)}
    let w=v;
    const b=brc(v),nmin=L(v),length=sq(v);
    maxL=Math.max(maxL,nmin);
    for(let k=0;k<12;k++){
      if(L(w)!==nmin||sq(w)!==length||brc(w)!==b)throw Error("BRC/metric violation "+code+" power "+k);
      if(k===6&&!eq(w,neg(v)))throw Error("T6 property failure");
      w=T(w);
      powerChecks++;
    }
    if(!eq(w,v))throw Error("T12 property failure");
    for(let j=0;j<12;j++){
      const s=E[j],ws=v.map((t,i)=>t+s[i]),Tv=T(v),Ts=T(s);
      if(!eq(T(ws),Tv.map((t,i)=>t+Ts[i])))throw Error("edge equivariance violation");
      edgeChecks++;
    }
    inspected++;
  }
  const witness=[2,1,-1,0,0,0];const orbitWitness=[];let w=witness;
  for(let k=0;k<12;k++){orbitWitness.push(w);w=T(w)}
  return {schema:"X6_UNIT162_C12_SIGNED_AXIS_AUTOMORPHISM_EXACT_CHECK_V1",date:"2026-11-19",scientific_pin:"59538f585d037d09ef687b28715c4bc1a3f9fe03",historical_source:"fd2bcff10ca6e147348b6c1236027fc0d2877df3",state_window:"[-2,2]^6",vector_count:inspected,power_invariance_checks:powerChecks,edge_equivariance_checks:edgeChecks,primitive_directions:12,regular_orbit_size:new Set(orbit).size,T6:"minus_identity",T12:"identity",max_tested_L1:maxL,witness:{z:witness,brc:brc(witness).toString(),orbit:orbitWitness},test_type:"EXACT_INTEGER_FINITE_CHECK_WITH_SEPARATE_ALL_INTEGER_PROOF",status:"PASS",execution:"actual V8 isolate run"};
};
const result=check();
console.log(JSON.stringify(result,null,2));
