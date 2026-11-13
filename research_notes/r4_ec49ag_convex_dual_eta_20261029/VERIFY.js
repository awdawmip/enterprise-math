// EC49AG: exact BigInt rational convex-dual certificate.
// Run: node VERIFY.js --write  (creates EXACT_REPORT.json and VERTEX_CERT.tsv).
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
const R=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}if(!d)throw Error("zero denominator");const g=gcd(n,d);return {n:n/g,d:d/g};};
const add=(a,b)=>R(a.n*b.d+b.n*a.d,a.d*b.d);
const neg=a=>R(-a.n,a.d);
const sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>R(a.n*b.n,a.d*b.d);
const div=(a,b)=>R(a.n*b.d,a.d*b.n);
const cmp=(a,b)=>a.n*b.d<b.n*a.d?-1:a.n*b.d>b.n*a.d?1:0;
const eq=(a,b)=>cmp(a,b)===0;
const plus=a=>cmp(a,Z)>=0?a:Z;
const min=(a,b)=>cmp(a,b)<0?a:b;
const max=(a,b)=>cmp(a,b)>0?a:b;
const s=a=>a.d===1n?String(a.n):String(a.n)+"/"+String(a.d);
const check=(ok,msg)=>{if(!ok)throw Error("EC49AG rational assertion: "+msg);};
const Z=R(0),ONE=R(1),K=R(177,172),LAM=R(1,20),C1=R(43,48),C2=R(7,8);
const KNOTS=[Z,R(13,998),R(1,4),R(123,430)], DIAG=R(3,10);
const X=[[ONE,Z,Z,Z],[Z,ONE,Z,Z],[R(9,16),Z,R(1,16),Z]];
const t=(w,u,e)=>add(R(1,2),mul(R((2*u-1)*(1-w)),e));
const P=(w,u,z,e)=>mul(t(w,u,e),w===z?R(1,6):R(1,12));
const Q=(w,u,z,e)=>div(t(w,u,e),R(9));
const atom=(x,c,u,z,e)=>{let result=Z;for(let w=0;w<3;w++)result=add(result,mul(x[w][c],sub(P(w,u,z,e),mul(K,Q(w,u,z,e)))));return result;};
const atoms=(x,e)=>{
  const phi=[],mass=[];
  for(let c=0;c<4;c++)for(let u=0;u<2;u++){
    const y=[0,1,2].map(w=>mul(x[w][c],t(w,u,e)));
    const Y=y.reduce(add,Z);
    let f=Z;
    for(let z=0;z<3;z++){
      const d=atom(x,c,u,z,e);
      check(eq(d,sub(div(y[z],R(12)),mul(R(4,129),Y))),"atom coefficient law");
      f=add(f,plus(d));
    }
    phi.push(f);mass.push(div(Y,R(3)));
  }
  return {phi,mass};
};
const sum=a=>a.reduce(add,Z);
const obj=(x,e)=>{
  const {phi,mass}=atoms(x,e);
  const dual=add(mul(LAM,C2),sum(phi.map((v,j)=>plus(sub(v,mul(LAM,mass[j]))))));
  return {dual,H:sum(phi),paid:sum(mass),phi,mass};
};
const prefix=(i,j,labels,bl,b)=>{
  const stop=add(R(5,16),b);
  const x=Array.from({length:3},()=>[Z,Z,Z,Z]);
  for(let w=0;w<3;w++){
    const h=w===i?stop:Z,bb=w===j?b:Z;
    x[w][labels[w]]=sub(sub(ONE,h),bb);
    x[w][2+bl]=add(x[w][2+bl],bb);
  }
  return x;
};
const bmass=x=>sum(x.map(row=>add(row[2],row[3])));
const cost1=x=>div(sum(x.flatMap(row=>[row[0],row[1],mul(R(2),row[2]),mul(R(2),row[3])])),R(3));
const verifyPrefix=x=>{
  check(x.length===3&&x.every(row=>row.length===4&&row.every(v=>cmp(v,Z)>=0)&&cmp(sum(row),ONE)<=0),"first-stage simplex");
  check(eq(cost1(x),C1),"first-stage exact budget");
  check(cmp(bmass(x),Z)>=0&&cmp(bmass(x),R(1,16))<=0,"high action bound");
};
const hx=e=>add(R(249,2752),add(mul(R(499,8256),plus(sub(e,R(13,998)))),mul(R(3,43),plus(sub(e,R(1,4))))));
const legal=(x,e)=>{
  const {phi,mass}=atoms(x,e);
  let rem=sub(sum(mass),C2),loss=Z;
  check(cmp(rem,Z)>=0,"legal paid mass");
  const indexes=[...Array(8).keys()].filter(i=>cmp(mass[i],Z)>0);
  indexes.sort((i,j)=>cmp(div(phi[i],mass[i]),div(phi[j],mass[j])));
  for(const i of indexes){
    const take=min(rem,mass[i]);
    loss=add(loss,mul(take,div(phi[i],mass[i])));
    rem=sub(rem,take);
    if(eq(rem,Z))break;
  }
  check(eq(rem,Z),"skip cost fulfilled");
  return sub(sum(phi),loss);
};
const xRoots=()=>{
  const out=[];
  for(let c=0;c<4;c++)for(let u=0;u<2;u++)for(let z=0;z<3;z++){
    const a=atom(X,c,u,z,Z),slope=sub(atom(X,c,u,z,ONE),a);
    if(!eq(slope,Z)){
      const root=div(neg(a),slope);
      if(cmp(root,Z)>0&&cmp(root,R(1,2))<0&&!out.some(v=>eq(v,root)))out.push(root);
    }
  }
  return out.sort(cmp).map(s);
};
function run(){
  const roots=xRoots();
  check(JSON.stringify(roots)===JSON.stringify(["13/998","1/4"]),"all X hinge roots");
  const vertices=[];
  for(const b of [Z,R(1,16)])for(let i=0;i<3;i++)for(let j=0;j<3;j++)
    for(let mask=0;mask<8;mask++)for(let bl=0;bl<2;bl++){
      const labels=[mask&1,(mask>>1)&1,(mask>>2)&1];
      const x=prefix(i,j,labels,bl,b);
      verifyPrefix(x);
      check(eq(bmass(x),b),"vertex high action mass");
      vertices.push({b,i,j,labels,bl,x});
    }
  check(vertices.length===288,"complete indexed endpoints");
  const unique=new Set(vertices.map(v=>v.x.flat().map(s).join(",")));
  check(unique.size===168,"168 distinct exact vertices");
  const expectedX=["249/2752","249/2752","3461/33024","113/1032","919/8256"];
  const expectedB0=["1801/20640","1801/20640","401/3840","113/1032","107/960"];
  const report=[];
  const rows=["eta\tb\tstop_history\tB_history\tA_labels\tB_label\tdual"];
  const etas=[...KNOTS,DIAG];
  for(let ni=0;ni<etas.length;ni++){
    const e=etas[ni];
    let pt=Z,qt=Z;
    for(let w=0;w<3;w++)for(let u=0;u<2;u++)for(let z=0;z<3;z++){
      const p=P(w,u,z,e),q=Q(w,u,z,e);
      check(cmp(p,Z)>0&&cmp(q,Z)>0,"strict positive raw leaves");
      pt=add(pt,p);qt=add(qt,q);
    }
    check(eq(pt,ONE)&&eq(qt,ONE),"18-leaf normalization");
    verifyPrefix(X);
    const xx=obj(X,e);
    check(eq(xx.paid,C2)&&eq(xx.dual,xx.H)&&eq(xx.H,hx(e)),"legal X equals hinge and dual");
    check(s(xx.H)===expectedX[ni],"X exact knot");
    const maxima={"0":null,"1/16":null},counts={"0":0,"1/16":0};
    let legal0=null;
    for(const v of vertices){
      const value=obj(v.x,e).dual,key=s(v.b);
      rows.push([s(e),key,v.i,v.j,v.labels.join(""),v.bl,s(value)].join("\t"));
      if(maxima[key]===null||cmp(value,maxima[key])>0){maxima[key]=value;counts[key]=0;}
      if(eq(value,maxima[key]))counts[key]++;
      if(key==="0"&&(eq(e,R(1,4))||eq(e,DIAG))){
        const lv=legal(v.x,e);
        legal0=legal0===null?lv:max(legal0,lv);
      }
    }
    check(s(maxima["0"])===expectedB0[ni],"b0 dual bound");
    check(eq(maxima["1/16"],xx.H),"b1 dual bound");
    if(ni<4)check(cmp(max(maxima["0"],maxima["1/16"]),xx.H)<=0,"certified knot upper bound");
    else {
      check(eq(sub(maxima["0"],xx.H),R(1,6880)),"eta3/10 dual-only excess");
      check(eq(legal0,R(13699,123840)),"eta3/10 legal endpoint optimum");
      check(eq(sub(xx.H,legal0),R(1,1440)),"eta3/10 legal gap");
    }
    if(eq(e,R(1,4)))check(eq(legal0,R(168127,1618176)),"eta1/4 b0 legal audit");
    report.push({
      eta:s(e),certified_knot:ni<4,X_support:s(xx.H),X_dual:s(xx.dual),
      b0_dual_max:s(maxima["0"]),b1_16_dual_max:s(maxima["1/16"]),
      b0_equal_max_count:counts["0"],b1_16_equal_max_count:counts["1/16"],
      dual_excess_over_X:s(sub(max(maxima["0"],maxima["1/16"]),xx.H)),
      legal_b0_endpoint_max:legal0===null?null:s(legal0)
    });
  }
  const result={
    schema:"EC49AG_CONVEX_LAGRANGE_CERTIFICATE_V1",date:"2026-10-29",
    model:"positive 18-leaf P/Q BRC causal fresh-coin observer",support:"alpha-(177/172)*beta",
    lambda:"1/20",C1:"43/48",C2:"7/8",
    certified_eta:"0<=eta<=123/430",
    formula:"249/2752+(499/8256)*[eta-13/998]_+ +(3/43)*[eta-1/4]_+",
    X_observation_hinge_roots:roots,unique_vertices:168,
    indexed_vertices_per_knot:288,certified_knot_count:4,
    certificate_tsv_rows:rows.length-1,
    checks:report,
    diagnostic:"At eta=3/10, excess 1/6880 is dual relaxation only; b0 legal endpoint max is 1/1440 below X.",
    status:"AUTHOR_EXACT_BIGINT_CHECK_PASS / ANALYTIC_CONVEXITY_PROOF / UNREVIEWED / NOT_ADMITTED"
  };
  return {result,tsv:rows.join("\n")+"\n"};
}
if(typeof require!=="undefined" && require.main===module){
  const fs=require("node:fs");
  const data=run();
  console.log(JSON.stringify(data.result,null,2));
  if(process.argv.includes("--write")){
    fs.writeFileSync("EXACT_REPORT.json",JSON.stringify(data.result,null,2)+"\n");
    fs.writeFileSync("VERTEX_CERT.tsv",data.tsv);
  }
}
