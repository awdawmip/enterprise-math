"use strict";
function verify(){
  const ok=(x,m)=>{if(!x)throw Error(m)};
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a||1n};
  const F=(a,b=1)=>{a=BigInt(a);b=BigInt(b);ok(b!==0n,"zero denominator");if(b<0n){a=-a;b=-b;}const d=gcd(a,b);return {a:a/d,b:b/d}};
  const plus=(x,y)=>F(x.a*y.b+y.a*x.b,x.b*y.b);
  const times=(x,y)=>F(x.a*y.a,x.b*y.b);
  const over=(x,y)=>F(x.a*y.b,x.b*y.a);
  const sum=xs=>xs.reduce(plus,F(0));
  const same=(x,y)=>x.a===y.a&&x.b===y.b;
  const fmt=x=>x.b===1n?String(x.a):`${x.a}/${x.b}`;
  function inspect(p,q,prow,qrow){
    const n=p.length,m=prow[0].length;
    ok(p.length===q.length&&prow.length===n&&qrow.length===n,"shape");
    ok(same(sum(p),F(1))&&same(sum(q),F(1)),"first normalization");
    const LR=[],MUS=[],SIGN=[];
    for(let i=0;i<n;i++){
      ok(p[i].a>0n&&q[i].a>0n,"first positivity");
      ok(same(sum(prow[i]),F(1))&&same(sum(qrow[i]),F(1)),"row normalization");
      const vec=[];
      const hist=new Map();
      for(let j=0;j<m;j++){
        ok(prow[i][j].a>0n&&qrow[i][j].a>0n,"row positivity");
        const r=over(times(q[i],qrow[i][j]),times(p[i],prow[i][j]));
        vec.push(r);
        const k=fmt(r);const old=hist.get(k);
        hist.set(k,{r,m:old?plus(old.m,prow[i][j]):prow[i][j]});
      }
      const mu=[...hist.values()].sort((a,b)=>a.r.a*b.r.b<b.r.a*a.r.b?-1:1);
      const moment=sum(mu.map(x=>times(x.r,x.m)));
      ok(same(moment,over(q[i],p[i])),"LR martingale moment");
      LR.push(vec);MUS.push(mu);
      SIGN.push(JSON.stringify({v:vec.map(fmt),mu:mu.map(x=>[fmt(x.r),fmt(x.m)])}));
    }
    const uniqueR=new Set(LR.flat().map(fmt));
    return {LR,MUS,SIGN,profile:[1,new Set(SIGN).size,uniqueR.size],
      first_moment:LR.map((_,i)=>fmt(over(q[i],p[i])))};
  }
  const a=[F(1,2),F(1,2)];
  const Pa=[[F(1,3),F(2,3)],[F(2,3),F(1,3)]];
  const Qa=[[F(2,3),F(1,3)],[F(1,3),F(2,3)]];
  const sw=inspect(a,a,Pa,Qa);
  ok(JSON.stringify(sw.profile)===JSON.stringify([1,2,2]),"swap profile");
  ok(JSON.stringify(sw.MUS[0].map(x=>[fmt(x.r),fmt(x.m)]))===JSON.stringify(sw.MUS[1].map(x=>[fmt(x.r),fmt(x.m)])),"swap histogram");
  ok(sw.SIGN[0]!==sw.SIGN[1],"label incompatibility");
  const yesP=plus(times(a[0],Pa[0][0]),times(a[1],Pa[1][1]));
  const yesQ=plus(times(a[0],Qa[0][0]),times(a[1],Qa[1][1]));
  ok(same(yesP,F(1,3))&&same(yesQ,F(2,3)),"swap witness");
  const jP=[sum([times(a[0],Pa[0][0]),times(a[1],Pa[1][0])]),
            sum([times(a[0],Pa[0][1]),times(a[1],Pa[1][1])])];
  const jQ=[sum([times(a[0],Qa[0][0]),times(a[1],Qa[1][0])]),
            sum([times(a[0],Qa[0][1]),times(a[1],Qa[1][1])])];
  ok(jP.every((x,j)=>same(x,jQ[j])&&same(x,F(1,2))),"merged J law");
  for(const d0 of [F(0),F(1)])for(const d1 of [F(0),F(1)]){
    ok(same(sum([times(jP[0],d0),times(jP[1],d1)]),
            sum([times(jQ[0],d0),times(jQ[1],d1)])),"all 4 deterministic D(J) rules");
  }
  const p=[F(1,4),F(1,4),F(1,2)],q=[F(3,8),F(3,8),F(1,4)];
  const Pb=Array.from({length:3},()=>[F(1,2),F(1,2)]);
  const Qb=[[F(2,3),F(1,3)],[F(2,3),F(1,3)],[F(1,4),F(3,4)]];
  const sa=inspect(p,q,Pb,Qb);
  ok(JSON.stringify(sa.profile)===JSON.stringify([1,2,4]),"safe profile");
  ok(sa.SIGN[0]===sa.SIGN[1]&&sa.SIGN[0]!==sa.SIGN[2],"safe group");
  const P_target={T2:p[0],T2D1:times(p[0],Pb[0][0])};
  const Q_target={T2:q[0],T2D1:times(q[0],Qb[0][0])};
  const P_comp={T2:times(sum([p[0],p[1]]),F(1,2)),
                T2D1:times(times(sum([p[0],p[1]]),F(1,2)),Pb[0][0])};
  const Q_comp={T2:times(sum([q[0],q[1]]),F(1,2)),
                T2D1:times(times(sum([q[0],q[1]]),F(1,2)),Qb[0][0])};
  for(const k of ["T2","T2D1"]){ok(same(P_target[k],P_comp[k]),"safe P "+k);ok(same(Q_target[k],Q_comp[k]),"safe Q "+k);}
  return {
    status:"PASS_EXACT_BIGINT_RATIONAL",
    model_A:{ordered_prefixes:7,terminal_LR:sw.LR.map(row=>row.map(fmt)),
      equal_unlabelled_histograms:sw.MUS.map(row=>row.map(x=>[fmt(x.r),fmt(x.m)])),
      minimal_state_profile:sw.profile,full_T2_D1_P:fmt(yesP),full_T2_D1_Q:fmt(yesQ),
      full_Q_minus_P:fmt(plus(yesQ,F(-yesP.a,yesP.b))),
      merged_J_marginals_P_Q:jP.map(fmt),
      all_four_deterministic_terminal_decisions_have_P_equal_Q:true},
    model_B:{ordered_prefixes:10,first_stage_LR:sa.first_moment,
      terminal_LR:sa.LR.map(row=>row.map(fmt)),minimal_state_profile:sa.profile,
      merge_groups:[[0,1],[2]],full_and_quotient_P_T2:fmt(P_target.T2),
      full_and_quotient_Q_T2:fmt(Q_target.T2),
      full_and_quotient_P_T2_D1:fmt(P_target.T2D1),
      full_and_quotient_Q_T2_D1:fmt(Q_target.T2D1)},
    scope:"Two exactly specified finite positive rational laws; universal all-policy theorem is in PROOF.md; independent Driver/Lean/native X6 bridge pending"
  };
}
console.log(JSON.stringify(verify(),null,2));
