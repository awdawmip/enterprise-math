// EC49AF exact verifier; run: node VERIFY.mjs
// 2026-10-29; BigInt exact rational sample checks and constructive sharp upper witnesses.
const exactVerify = function exactVerify() {
  const G=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b!==0n){let t=a%b;a=b;b=t;}return a;};
  const R=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b===0n)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=G(a,b);return {n:a/g,d:b/g};};
  const add=(x,y)=>R(x.n*y.d+y.n*x.d,x.d*y.d);
  const sub=(x,y)=>R(x.n*y.d-y.n*x.d,x.d*y.d);
  const mul=(x,y)=>R(x.n*y.n,x.d*y.d);
  const div=(x,y)=>R(x.n*y.d,x.d*y.n);
  const cmp=(x,y)=>x.n*y.d<y.n*x.d?-1:x.n*y.d>y.n*x.d?1:0;
  const eq=(x,y)=>cmp(x,y)===0;
  const str=x=>x.d===1n?String(x.n):String(x.n)+"/"+String(x.d);
  const parse=s=>{let a=String(s).split("/");return R(a[0],a[1]||"1");};
  const min=(x,y)=>cmp(x,y)<0?x:y;
  const pos=x=>cmp(x,R(0))>0?x:R(0);
  const neg=x=>R(-x.n,x.d);
  const check=(x,msg)=>{if(!x)throw Error("exact failure: "+msg);};
  const Z=R(0), O=R(1), D0=R(59,576), STOP=R(1,8);
  const X=[[O,Z,Z,Z],[Z,O,Z,Z],[R(9,16),Z,R(1,16),Z]];
  const samples=["0","1/200","1/34","1/20","23/82","1/3","499/1000"];
  const summaries=[];
  for(const sample of samples) {
    const eta=parse(sample);
    const t=(w,u)=>add(R(1,2),mul(R((2*u-1)*(1-w)),eta));
    const raw=(s,w,u,z)=>mul(t(w,u),s==="P"?(w===z?R(1,6):R(1,12)):R(1,9));
    for(const src of ["P","Q"]) {
      let total=Z;
      for(let w=0;w<3;w++)for(let u=0;u<2;u++)for(let z=0;z<3;z++){
        const v=raw(src,w,u,z);check(cmp(v,Z)>0,"positive leaf "+src);total=add(total,v);
      }
      check(eq(total,O),"normalized "+src+" eta "+sample);
    }
    let c1=Z,c2=Z;
    for(let w=0;w<3;w++)for(let c=0;c<4;c++){
      c1=add(c1,mul(X[w][c],R(c>=2?2:1,3)));
      c2=add(c2,mul(X[w][c],R(1,3)));
    }
    check(eq(c1,R(43,48))&&eq(c2,R(7,8)),"fixed costs");
    const atoms=[];
    let totalP=STOP,totalQ=STOP;
    for(let c=0;c<4;c++)for(let u=0;u<2;u++)for(let z=0;z<3;z++){
      let p=Z,q=Z;
      for(let w=0;w<3;w++){
        p=add(p,mul(X[w][c],raw("P",w,u,z)));
        q=add(q,mul(X[w][c],raw("Q",w,u,z)));
      }
      if(eq(p,Z)&&eq(q,Z))continue;
      let d=sub(p,q),pure=(c===0&&z===1)||(c===1&&z!==1)||(c===2&&z!==2);
      atoms.push({c,u,z,p,q,d,pure});
      totalP=add(totalP,p);totalQ=add(totalQ,q);
      check(cmp(sub(mul(R(4),p),mul(R(3),q)),Z)>=0,"likelihood ratio");
      if(pure)check(eq(p,mul(R(3),neg(d)))&&cmp(d,Z)<0,"off-diagonal identity");
    }
    check(eq(totalP,O)&&eq(totalQ,O),"observation normalization");
    const pureNegative=atoms.filter(a=>a.pure);
    const pureCap=pureNegative.reduce((s,a)=>add(s,neg(a.d)),Z);
    check(eq(pureCap,D0),"eta-independent pure capacity");
    const h1=pos(div(sub(mul(R(34),eta),O),R(576)));
    const h2=pos(div(sub(mul(R(82),eta),R(23)),R(1152)));
    const impure1=atoms.find(a=>a.c===0&&a.u===1&&a.z===2);
    const impure2=atoms.find(a=>a.c===0&&a.u===0&&a.z===0);
    check(eq(pos(neg(impure1.d)),h1)&&eq(pos(neg(impure2.d)),h2),"sign thresholds");
    check(eq(impure1.p,div(sub(R(17),mul(R(2),eta)),R(192))),"P1");
    check(eq(impure2.p,div(sub(R(41),mul(R(46),eta)),R(384))),"P2");
    const negative=atoms.filter(a=>cmp(a.d,Z)<0);
    const positive=atoms.filter(a=>cmp(a.d,Z)>0);
    const D=positive.reduce((s,a)=>add(s,a.d),Z);
    const totalNeg=negative.reduce((s,a)=>add(s,neg(a.d)),Z);
    check(eq(D,totalNeg)&&eq(D,add(add(D0,h1),h2)),"D hinge formula");
    const r1=cmp(h1,Z)>0?div(impure1.p,h1):Z;
    const r2=cmp(h2,Z)>0?div(impure2.p,h2):Z;
    if(cmp(h1,Z)>0)check(cmp(r1,R(3))>0,"r1>3");
    if(cmp(h2,Z)>0)check(cmp(r2,r1)>0,"r2>r1");
    const upperByKnapsack=delta=>{
      let rem=delta,cost=Z;
      const sorted=negative.slice().sort((a,b)=>cmp(div(a.p,neg(a.d)),div(b.p,neg(b.d))));
      for(const a of sorted){
        const take=min(rem,neg(a.d));
        cost=add(cost,mul(take,div(a.p,neg(a.d))));
        rem=sub(rem,take);
      }
      check(eq(rem,Z),"knapsack filled");return sub(O,cost);
    };
    const upperFormula=delta=>{
      const pureTake=min(delta,D0);
      const other=pos(sub(delta,D0));
      const firstTake=min(other,h1);
      const secondTake=pos(sub(other,firstTake));
      check(cmp(secondTake,h2)<=0,"last segment fits");
      return sub(sub(sub(O,mul(R(3),pureTake)),mul(r1,firstTake)),mul(r2,secondTake));
    };
    const deltas=[Z,div(D0,R(2)),D0,add(D0,div(h1,R(2))),add(D0,h1),D];
    for(const d of deltas){
      check(cmp(d,D)<=0,"sample in feasible interval");
      check(eq(upperByKnapsack(d),upperFormula(d)),"sharp upper at "+sample+","+str(d));
    }
    // Full causal protocol: reject a uniform fraction of off-diagonal atoms only.
    for(const d of [Z,div(D0,R(3)),D0]){
      const fraction=div(d,D0);
      let pReject=Z,qReject=Z;
      for(const a of pureNegative){
        pReject=add(pReject,mul(fraction,a.p));
        qReject=add(qReject,mul(fraction,a.q));
      }
      check(eq(pReject,mul(R(3),d))&&eq(qReject,mul(R(4),d)),"global upper witness");
    }
    summaries.push({
      eta:sample,
      positive_observation_atoms:positive.length,
      negative_observation_atoms:negative.length,
      zero_discrimination_atoms:atoms.length-positive.length-negative.length,
      pure_negative_capacity:str(pureCap),
      extra_negative_capacities:[str(h1),str(h2)],
      fixed_prefix_max_discrimination:str(D),
      fixed_prefix_upper_alpha_at_D:str(upperFormula(D)),
      global_sharp_upper_witness_delta:str(D0)
    });
  }
  return {schema:"EC49AF_PARAMETRIC_PHASE_AND_GLOBAL_SHARP_EDGE_V1",
    checker:"JavaScript BigInt reduced rational arithmetic, executed from this identical function source",
    leaves_per_source:18,stage_costs:["43/48","7/8"],
    source_eta_domain:"0<=eta<1/2 (analytic; exact representative computations)",
    thresholds:["1/34","23/82"],
    fixed_prefix_discrimination_formula:"59/576 + max(34 eta - 1,0)/576 + max(82 eta - 23,0)/1152",
    all_behavioral_protocol_sharp_upper_edge:"alpha_max(delta)=1-3 delta for every 0<=delta<=59/576, all eta in domain",
    samples:summaries,
    status:"AUTHOR_PROVED / EXACT_BIGINT_SAMPLE_CHECK_PASS / UNREVIEWED / NOT_ADMITTED"};
};
console.log(JSON.stringify(exactVerify(),null,2));
