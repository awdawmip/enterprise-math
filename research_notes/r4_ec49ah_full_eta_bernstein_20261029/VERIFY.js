// EC49AH independent exact BigInt Bernstein certificate. Run: node VERIFY.js
function run(){
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const z=a%b;a=b;b=z;}return a;};
  const R=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}if(d===0n)throw Error("division zero");let z=gcd(n,d);return {n:n/z,d:d/z};};
  const add=(a,b)=>R(a.n*b.d+b.n*a.d,a.d*b.d), neg=a=>R(-a.n,a.d);
  const sub=(a,b)=>add(a,neg(b)), mul=(a,b)=>R(a.n*b.n,a.d*b.d), div=(a,b)=>R(a.n*b.d,a.d*b.n);
  const cmp=(a,b)=>a.n*b.d<b.n*a.d?-1:a.n*b.d>b.n*a.d?1:0, eq=(a,b)=>cmp(a,b)===0;
  const max=(a,b)=>cmp(a,b)>=0?a:b, sum=a=>a.reduce(add,Z), s=a=>a.d===1n?`${a.n}`:`${a.n}/${a.d}`;
  const check=(v,m)=>{if(!v)throw Error("EC49AH exact rational assertion: "+m);};
  const Z=R(0),O=R(1),HALF=R(1,2),C1=R(43,48),C2=R(7,8),K=R(177,172);
  const E0=R(123,430),E1=HALF,MID=div(add(E0,E1),R(2)),H0=R(1193,16512),HS=R(25,192);
  const X=[[O,Z,Z,Z],[Z,O,Z,Z],[R(9,16),Z,R(1,16),Z]];
  const t=(w,u,e)=>add(HALF,mul(R((2*u-1)*(1-w)),e));
  const p=(w,u,z,e)=>mul(t(w,u,e),w===z?R(1,6):R(1,12));
  const q=(w,u,z,e)=>div(t(w,u,e),R(9));
  const atom=(x,c,u,z,e)=>sum([0,1,2].map(w=>mul(x[w][c],sub(p(w,u,z,e),mul(K,q(w,u,z,e))))));
  const mass=(x,c,u,e)=>div(sum([0,1,2].map(w=>mul(x[w][c],t(w,u,e)))),R(3));
  const lambda=e=>sub(div(e,R(2)),R(4,43));
  const h=e=>add(H0,mul(HS,e));
  const bquad=(A,B,C,j)=>j===0?add(add(mul(mul(A,E0),E0),mul(B,E0)),C):
    j===2?add(add(mul(mul(A,E1),E1),mul(B,E1)),C):
    add(add(mul(mul(A,E0),E1),mul(B,div(add(E0,E1),R(2)))),C);
  const V=[],unique=new Set();
  for(const b of [Z,R(1,16)])for(let i=0;i<3;i++)for(let j=0;j<3;j++)
    for(let labels=0;labels<8;labels++)for(let bl=0;bl<2;bl++){
      const rows=Array.from({length:3},()=>[Z,Z,Z,Z]);
      for(let w=0;w<3;w++){
        const stop=w===i?add(R(5,16),b):Z, bb=w===j?b:Z, al=(labels>>w)&1;
        rows[w][al]=sub(sub(O,stop),bb);
        rows[w][2+bl]=add(rows[w][2+bl],bb);
      }
      const key=rows.flat().map(s).join(",");
      if(!unique.has(key)){unique.add(key);V.push(rows);}
    }
  check(V.length===168,"vertex count");
  check(eq(lambda(E0),R(1,20))&&eq(lambda(E1),R(27,172)),"dual endpoints");
  const Hx=e=>sum([...Array(4).keys()].flatMap(c=>[0,1].flatMap(u=>[0,1,2].map(z=>max(Z,atom(X,c,u,z,e))))));
  for(const [e,w] of [[E0,R(113,1032)],[R(3,10),R(919,8256)],[E1,R(189,1376)]]){
    check(eq(h(e),w)&&eq(Hx(e),w),"X exact support");
  }
  for(const e of [Z,R(1,4),E0,R(3,10),R(2,5),R(499,1000)]){
    let pp=Z,qq=Z;
    for(let w=0;w<3;w++)for(let u=0;u<2;u++)for(let z=0;z<3;z++){
      const pv=p(w,u,z,e),qv=q(w,u,z,e);
      check(cmp(pv,Z)>0&&cmp(qv,Z)>0,"strict positive raw leaves");
      pp=add(pp,pv);qq=add(qq,qv);
    }
    check(eq(pp,O)&&eq(qq,O),"18 leaf probability normalization");
  }
  const values=[[],[],[]];
  for(const x of V){
    const first=sum(x.flatMap(row=>[row[0],row[1],mul(R(2),row[2]),mul(R(2),row[3])]));
    check(eq(div(first,R(3)),C1),"cost 1");
    const paid=sum([...Array(4).keys()].flatMap(c=>[0,1].map(u=>mass(x,c,u,E0))));
    check(cmp(paid,C2)>=0,"S feasible");
    for(let j=0;j<3;j++){
      const e=[E0,MID,E1][j];
      let out=sub(mul(lambda(e),C2),h(e));
      for(let c=0;c<4;c++)for(let u=0;u<2;u++){
        const obs=sum([0,1,2].map(z=>max(Z,atom(x,c,u,z,e))));
        const qb=mass(x,c,u,Z),qa=sub(mass(x,c,u,O),qb);
        const A=div(qa,R(2));
        const B=sub(div(qb,R(2)),mul(R(4,43),qa));
        const C=neg(mul(R(4,43),qb));
        const price=bquad(A,B,C,j);
        out=add(out,max(Z,sub(obs,price)));
      }
      check(cmp(out,Z)<=0,"Bernstein bound for vertex index "+V.indexOf(x)+" and coefficient "+j);
      values[j].push(out);
    }
  }
  const maxima=values.map(a=>a.reduce(max)),minimum=values.map(a=>a.reduce((a,b)=>cmp(a,b)<0?a:b));
  check(maxima.every(v=>eq(v,Z)),"sharp zero triple Bernstein maximum");
  const eqcounts=values.map(a=>a.filter(v=>eq(v,Z)).length);
  check(JSON.stringify(eqcounts)==="[20,20,168]","equality count");
  return {
    schema:"EC49AH_INDEPENDENT_BIGINT_BERNSTEIN_V1",
    exact_arithmetic:"native JavaScript BigInt reduced rational",
    interval:"123/430<=eta<1/2",
    multiplier:"lambda(eta)=eta/2-4/43",
    global_support:"1193/16512+(25/192)*eta",
    first_stage_vertices:V.length,
    indexed_vertex_choices:288,
    tested_Bernstein_coefficients:504,
    maxima:maxima.map(s),
    minima:minimum.map(s),
    equality_counts:eqcounts,
    check:"PASS_EXACT_EC49AH_BIGINT_BERNSTEIN",
    theorem_status:"AUTHOR_PROVED_UNREVIEWED_NOT_ADMITTED"
  };
}
console.log(JSON.stringify(run(),null,2));
