// EC49AI exact independent BigInt checker; run: node VERIFY.js
const run = () => {
  const gcd=(a,b)=>{if(a<0n)a=-a;if(b<0n)b=-b;while(b){const c=a%b;a=b;b=c;}return a;};
  const R=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};};
  const add=(a,b)=>R(a.n*b.d+b.n*a.d,a.d*b.d),neg=a=>R(-a.n,a.d);
  const sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>R(a.n*b.n,a.d*b.d),div=(a,b)=>R(a.n*b.d,a.d*b.n);
  const cmp=(a,b)=>a.n*b.d<b.n*a.d?-1:a.n*b.d>b.n*a.d?1:0;
  const eq=(a,b)=>cmp(a,b)===0;
  const Z=R(0),O=R(1),ETA=R(3,10),K=R(177,172),C1=R(43,48),C20=R(7,8),EMAX=R(3,128),L=R(49,860),H0=R(919,8256);
  const sum=xs=>xs.reduce(add,Z),max=(a,b)=>cmp(a,b)>=0?a:b;
  const str=a=>a.d===1n?`${a.n}`:`${a.n}/${a.d}`;
  const check=(ok,msg)=>{if(!ok)throw Error("EC49AI certificate failed: "+msg);};
  const t=(w,u)=>add(R(1,2),mul(R((2*u-1)*(1-w)),ETA));
  const P=(w,u,z)=>mul(t(w,u),w===z?R(1,6):R(1,12));
  const Q=(w,u,z)=>div(t(w,u),R(9));
  const mass=(x,c,u)=>div(sum([0,1,2].map(w=>mul(x[w][c],t(w,u)))),R(3));
  const d=(x,c,u,z)=>{
    let v=Z;
    for(let w=0;w<3;w++)v=add(v,mul(x[w][c],sub(P(w,u,z),mul(K,Q(w,u,z)))));
    return v;
  };
  const phi=(x,c,u)=>sum([0,1,2].map(z=>max(Z,d(x,c,u,z))));
  const H=x=>{let h=Z;for(let c=0;c<4;c++)for(let u=0;u<2;u++)h=add(h,phi(x,c,u));return h;};
  const dual=(x,e)=>{
    let v=mul(L,sub(C20,e));
    for(let c=0;c<4;c++)for(let u=0;u<2;u++){
      v=add(v,max(Z,sub(phi(x,c,u),mul(L,mass(x,c,u)))));
    }
    return v;
  };
  const X=[[O,Z,Z,Z],[Z,O,Z,Z],[R(9,16),Z,R(1,16),Z]];
  const Y=e=>[[sub(R(9,16),mul(R(6),e)),Z,add(R(1,16),mul(R(3),e)),Z],[Z,O,Z,Z],[O,Z,Z,Z]];
  const V=e=>{
    const vs=[],B=add(R(1,16),mul(R(3),e));
    for(const b of [Z,B])for(let i=0;i<3;i++)for(let j=0;j<3;j++)for(let lab=0;lab<8;lab++)for(let bl=0;bl<2;bl++){
      const x=Array.from({length:3},()=>[Z,Z,Z,Z]);
      for(let w=0;w<3;w++){
        const stop=w===i?add(R(5,16),b):Z,bb=w===j?b:Z,al=(lab>>w)&1;
        x[w][al]=sub(sub(O,stop),bb);
        x[w][2+bl]=add(x[w][2+bl],bb);
      }vs.push(x);
    }return vs;
  };
  const costs=(x,e,full)=>{
    for(const row of x){check(row.every(v=>cmp(v,Z)>=0),"negative probability");check(cmp(sum(row),O)<=0,"row >1");}
    let c1=Z,paid=Z;
    for(const row of x)c1=add(c1,add(add(row[0],row[1]),mul(R(2),add(row[2],row[3]))));
    c1=div(c1,R(3));
    for(let c=0;c<4;c++)for(let u=0;u<2;u++)paid=add(paid,mass(x,c,u));
    check(eq(c1,C1),"first-stage exact cost");
    check(cmp(paid,sub(C20,e))>=0,"insufficient paid mass");
    if(full)check(eq(paid,sub(C20,e)),"second-stage exact cost");
    return paid;
  };
  let ps=Z,qs=Z;
  for(let w=0;w<3;w++)for(let u=0;u<2;u++){
    let pz=Z,qz=Z;
    for(let z=0;z<3;z++){
      const a=P(w,u,z),b=Q(w,u,z);
      check(cmp(a,Z)>0&&cmp(b,Z)>0,"strictly positive raw leaves");
      ps=add(ps,a);qs=add(qs,b);pz=add(pz,a);qz=add(qz,b);
    }check(eq(pz,qz)&&eq(pz,div(t(w,u),R(3))),"fiber marginal equality");
  }
  check(eq(ps,O)&&eq(qs,O),"18-leaf normalization");
  const endpoints={};
  for(const e of [Z,EMAX]){
    const vs=V(e),unique=new Set(vs.map(x=>x.flat().map(str).join(",")));
    check(vs.length===288&&unique.size===168,"indexed/distinct vertices");
    const target=sub(H0,mul(L,e));
    let minimum=null,maximum=null,equalityCount=0;
    for(const v of vs){
      costs(v,e,false);const value=dual(v,e);
      if(minimum===null||cmp(value,minimum)<0)minimum=value;
      if(maximum===null||cmp(value,maximum)>0)maximum=value;
      if(eq(value,target))equalityCount++;
      check(cmp(value,target)<=0,"endpoint dual inequality");
    }
    const yy=Y(e);costs(yy,e,true);
    check(eq(H(yy),target)&&eq(maximum,target),"sharp global witness");
    endpoints[str(e)]={C2:str(sub(C20,e)),sharp_support:str(target),vertices_indexed:vs.length,vertices_distinct:unique.size,dual_max:str(maximum),dual_min:str(minimum),equality_indexed:equalityCount,primal_Y:str(H(yy))};
  }
  const mask=new Set(["0,0,2","0,1,0","1,0,1","1,1,1","2,0,0","2,1,0"]);
  for(let c=0;c<4;c++)for(let u=0;u<2;u++)for(let z=0;z<3;z++){
    const positive=mask.has(`${c},${u},${z}`);
    for(const e of [Z,EMAX])check(positive?cmp(d(Y(e),c,u,z),Z)>=0:cmp(d(Y(e),c,u,z),Z)<=0,"fixed Y terminal mask");
  }
  costs(X,Z,true);check(eq(H(X),H0),"X baseline");
  const paid=[];
  for(let c=0;c<4;c++)for(let u=0;u<2;u++){
    const q=mass(X,c,u);if(cmp(q,Z)>0)paid.push({c,u,q,ratio:div(phi(X,c,u),q)});
  }
  const low=paid.find(v=>v.c===0&&v.u===0);
  check(eq(low.q,R(13,60))&&eq(low.ratio,R(179,2236)),"X least marginal ratio");
  check(paid.every(v=>v===low||cmp(v.ratio,low.ratio)>0),"unique least marginal ratio");
  check(cmp(EMAX,low.q)<0,"X partial buy feasibility");
  const difference=sub(low.ratio,L);
  check(eq(difference,R(3,130))&&eq(mul(difference,EMAX),R(9,16640)),"strict Y-X separation");
  return {schema:"EC49AI_INDEPENDENT_BIGINT_COST_FACET_V1",model:"eta=3/10, C1=43/48, C2=7/8-eps, 0<=eps<=3/128; erased history; fresh independent coins",source_leaves:"18+18 positive, normalized; P/Q marginals matched",global_sharp_H:"919/8256-(49/860)*eps",lambda:"49/860",endpoint_certificates:endpoints,endpoint_distinct_vertex_inequalities:336,indexed_endpoints_checked:576,X_fixed_prefix_optimal_H:"919/8256-(179/2236)*eps",Y_minus_X:"(3/130)*eps",X_breakpoint:"C2=7/8",Y_mask:[...mask].sort(),independent_review:"NOT_PERFORMED",native_signed_BRC_or_X6_transfer:"NOT_CLAIMED",result:"PASS_EXACT_BIGINT_AUTHOR_UNREVIEWED"};
};
console.log(JSON.stringify(run(),null,2));
