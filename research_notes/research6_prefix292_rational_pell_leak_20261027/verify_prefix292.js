#!/usr/bin/env node
'use strict';
const verifyPrefix292 = function verifyPrefix292(){
  const fail=(x)=>{throw Error("BRC certificate failed: "+x)};
  const ok=(c,label)=>{if(!c)fail(label)};
  const g=(a=0n,b=0n)=>[BigInt(a),BigInt(b)],zero=g(),one=g(1),im=g(0,1);
  const plus=(a,b)=>g(a[0]+b[0],a[1]+b[1]),minus=(a,b)=>g(a[0]-b[0],a[1]-b[1]);
  const times=(a,b)=>g(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]);
  const conj=a=>g(a[0],-a[1]),sc=(a,n)=>g(a[0]*BigInt(n),a[1]*BigInt(n));
  const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1];
  const div=(a,n)=>{n=BigInt(n);ok(a[0]%n===0n&&a[1]%n===0n,"exact division");return g(a[0]/n,a[1]/n)};
  const sum=xs=>xs.reduce(plus,zero);
  const choice=[zero,one,g(-1),im,g(0,-1),g(1,1)];
  const phase=[one,im,g(-1),g(0,-1)];
  const pell=[[1,1],[5,3],[19,11],[71,41],[265,153]];
  const pair=(a,b)=>sum(a.map((v,k)=>times(v,conj(b[k]))));
  const label=(s,leg,c)=>({s,leg,c});
  function ports(u,p,r){
    const u2=times(u,u),T=2n*r;
    return {
      E0:[label(0,"E0.source0",g(T)),label(1,"E0.source1",sc(u,T))],
      E1:[label(1,"E1.source1",g(-T)),label(2,"E1.source2",sc(u,T))],
      D0:[label(0,"D0.source0",g(T)),label(1,"D0.source1",sc(u,p-r)),label(2,"D0.source2",sc(u2,r+p))],
      D1:[label(0,"D1.source0",g(T)),label(1,"D1.source1",sc(u,-r-p)),label(2,"D1.source2",sc(u2,r-p))],
      D2:[label(0,"D2.source0",g(T)),label(2,"D2.source2",sc(u2,-T))],
      LEAK:[label(1,"LEAK.source1",sc(u,2n)),label(2,"LEAK.source2",sc(u2,2n))]
    };
  }
  const amp=(legs,a)=>sum(legs.map(e=>times(e.c,a[e.s])));
  function brc(legs,a,b){
    let n=zero,terms=0;
    for(const x of legs)for(const y of legs){
      n=plus(n,times(times(x.c,a[x.s]),conj(times(y.c,b[y.s]))));
      terms++;
    }
    return [n,terms];
  }
  let cases=0,massBins=0,pairProducts=0,basis=0,allMass=0,cross=0,decodes=0,rankOne=0,Echecks=0,witness=0;
  for(let k=0;k<pell.length;k++){
    const [pi,ri]=pell[k],p=BigInt(pi),r=BigInt(ri),D=4n*r;
    ok(p*p-3n*r*r===-2n,"Pell");
    if(k){const [x,y]=pell[k-1];ok(pi===2*x+3*y&&ri===x+2*y,"Pell recurrence")}
    for(const u of phase){
      const out=ports(u,p,r),names=Object.keys(out);
      for(let j=0;j<3;j++)for(let h=0;h<3;h++){
        const a=Array.from({length:3},(_,t)=>t===j?one:zero);
        const b=Array.from({length:3},(_,t)=>t===h?one:zero);
        const gram=sum(names.map(n=>brc(out[n],a,b)[0]));
        ok(eq(gram,sc(pair(a,b),D*D)),"basis Gram");
        basis++;
      }
      for(const a0 of choice)for(const a1 of choice)for(const a2 of choice){
        const a=[a0,a1,a2],b=[a2,a0,a1];
        let m=zero,c=zero,e=zero,l=zero;
        for(const name of names){
          const legs=out[name],ma=brc(legs,a,a),cb=brc(legs,a,b);
          ok(eq(ma[0],times(amp(legs,a),conj(amp(legs,a)))),"ordered BRC");
          ok(ma[0][1]===0n&&ma[0][0]>=0n,"positive mass");
          m=plus(m,ma[0]);c=plus(c,cb[0]);
          if(name==="LEAK")l=ma[0];
          if(name==="E0"||name==="E1")e=plus(e,ma[0]);
          massBins++;pairProducts+=ma[1]+cb[1];
        }
        const total=sc(pair(a,a),D*D);
        ok(eq(m,total),"full isometry");ok(eq(c,sc(pair(a,b),D*D)),"cross coherence");
        allMass++;cross++;
        const d0=amp(out.D0,a),d1=amp(out.D1,a),d2=amp(out.D2,a);
        const s=plus(d0,d1),delta=div(sc(minus(d1,d0),r),p);
        const x=div(plus(s,delta),2n),y=div(minus(s,delta),2n);
        const w=minus(y,x),v0=plus(y,d2);
        const v2=times(conj(times(u,u)),minus(y,d2));
        const v1=times(conj(u),plus(minus(sc(w,2n),y),d2));
        ok(eq(v0,sc(a[0],D))&&eq(v1,sc(a[1],D))&&eq(v2,sc(a[2],D)),"coherent decoder");
        decodes++;
        const wp=div(times(w,conj(w)),r*r);
        ok(eq(l,wp)&&2n*l[0]*r*r<=total[0],"rank-one sharp bound");rankOne++;
        const ev0=plus(a[0],times(u,a[1])),ev1=plus(sc(a[1],-1n),times(u,a[2]));
        const expected=sc(plus(times(ev0,conj(ev0)),times(ev1,conj(ev1))),(D/2n)*(D/2n));
        ok(eq(e,expected),"unchanged E");Echecks++;
        cases++;
      }
      const strong=[zero,one,conj(u)];
      const leak=brc(out.LEAK,strong,strong)[0];
      const norm=sc(pair(strong,strong),D*D);
      ok(2n*leak[0]*r*r===norm[0],"attainment");
      witness++;
      if(eq(u,im)){
        const e=a=>plus(brc(out.E0,a,a)[0],brc(out.E1,a,a)[0]);
        ok(eq(e([one,im,one]),zero),"singular partner a");
        ok(eq(e([one,sc(im,-1n),one]),g(2n*D*D)),"singular partner b");
      }
    }
  }
  return {
    schema:"EM_PREFIX292_RATIONAL_PELL_BRC_CONNECTOR_VERIFIER_V1",status:"PASS",
    arithmetic:"BigInt Gaussian exact integers; common 4r denominator; all ordered source-leg pairs",
    finite_domain:"6 sources values per coordinate x 3 sources x 4 C4 phases x 5 Pell solutions",
    input_phase_pell_cases:cases,direct_bin_mass_checks:massBins,
    ordered_source_leg_pair_products_including_cross:pairProducts,
    basis_gram_equalities:basis,full_mass_equalities:allMass,
    cross_input_equalities:cross,coherent_decode_equalities:decodes,
    rank_one_leakage_equalities_and_bounds:rankOne,exact_E_event_equalities:Echecks,
    sharp_witnesses:witness,
    pell_solutions:pell.map(([p,r])=>({p,r,maximum_loss_fraction:`1/${2*r*r}`})),
    status_scope:"FORMAL_C4_BRC_ONLY; SOURCE_NATIVE_HN_NOT_TESTED; AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED"
  };
};
console.log(JSON.stringify(verifyPrefix292(),null,2));
