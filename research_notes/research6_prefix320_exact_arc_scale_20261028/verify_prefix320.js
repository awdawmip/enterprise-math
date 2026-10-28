"use strict";
/* PREFIX-320. Exact BigInt/Gaussian rational labelled BRC and full rational-arc cover. */
const certificate = (function exactChecker() {
  const abs=x=>x<0n?-x:x;
  function gcd(a,b){a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a||1n;}
  function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return {n:n/g,d:d/g};}
  const add=(a,b)=>F(a.n*b.d+b.n*a.d,a.d*b.d),neg=a=>F(-a.n,a.d),sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>F(a.n*b.n,a.d*b.d),div=(a,b)=>F(a.n*b.d,a.d*b.n);
  const eq=(a,b)=>a.n===b.n&&a.d===b.d,cmp=(a,b)=>a.n*b.d-b.n*a.d,ord=(a,b)=>cmp(a,b)<0n?-1:cmp(a,b)>0n?1:0;
  const fmt=a=>a.d===1n?String(a.n):`${a.n}/${a.d}`,parse=s=>{let p=String(s).split("/");return F(p[0],p[1]??1);};
  const C=(x=0,y=0)=>[F(x),F(y)],CC=(x,y)=>[x,y];
  const ca=(a,b)=>CC(add(a[0],b[0]),add(a[1],b[1])),cn=a=>CC(neg(a[0]),neg(a[1]));
  const cs=(a,b)=>ca(a,cn(b)),cj=a=>CC(a[0],neg(a[1]));
  const cm=(a,b)=>CC(sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0])));
  const cd=(a,r)=>CC(div(a[0],r),div(a[1],r)),ce=(a,b)=>eq(a[0],b[0])&&eq(a[1],b[1]);
  const norm=a=>add(mul(a[0],a[0]),mul(a[1],a[1])),str=a=>a.map(fmt);
  const check=(v,m)=>{if(!v)throw Error(m);};
  const A=[[C(4),C(4),C()],[C(),C(-4),C(4)],[C(-5,3),C(),C(-3,1)],[C(-2,-2),C(4,4),C(2,2)],[C(-2),C(),C(5,2)]];
  const b0=[C(-2),C(0,-2),C(1)],b2=[C(0,2),C(2),C(0,-1)],t0=CC(F(-7,14),F(3,14)),t2=CC(F(-7,14),F(-3,14));
  let reads=0,pairs=0;
  function brc(state,j,ref){
    const paths=state.map((v,k)=>[`source:${k+1}`,cd(cm(A[j][k],v),F(8))]);
    if(ref==="1")paths.push(["reference:1",C(1)]);
    else if(ref==="i")paths.push(["reference:i",C(0,1)]);
    else check(ref==="0","reference");
    let q=C();
    for(const [tag,v] of paths)for(const [tag2,w] of paths)q=ca(q,cm(v,cj(w)));
    check(eq(q[1],F(0))&&cmp(q[0],F(0))>=0n,"BRC mass positive real");
    reads++;pairs+=paths.length*paths.length;return q[0];
  }
  function observe(state){
    const q={};
    for(const ref of ["0","1","i"])q[ref]=A.map((_,j)=>brc(state,j,ref));
    const amplitudes=A.map((_,j)=>CC(div(sub(sub(q["1"][j],q["0"][j]),F(1)),F(2)),
      div(sub(sub(q["i"][j],q["0"][j]),F(1)),F(2))));
    return {q,amplitudes};
  }
  const B0=observe(b0),B2=observe(b2),c=B0.amplitudes,d=B2.amplitudes;
  const EC=[C(-1,-1),CC(F(1,2),F(1)),CC(F(7,8),F(-5,8)),CC(F(7,4),F(-1,4)),CC(F(9,8),F(1,4))];
  const ED=[C(1,1),CC(F(-1),F(-1,2)),CC(F(-5,8),F(-7,8)),CC(F(7,4),F(1,4)),CC(F(1,4),F(-9,8))];
  const EQ=[F(2),F(5,4),F(37,32),F(25,8),F(85,64)];
  for(let j=0;j<5;j++)check(ce(c[j],EC[j])&&ce(d[j],ED[j])&&eq(B0.q["0"][j],EQ[j])&&eq(B2.q["0"][j],EQ[j]),"BRC shape port");
  const a0=b0.map(v=>cm(t0,v)),a2=b2.map(v=>cm(t2,v)),P0=observe(a0),P2=observe(a2);
  const delta=P0.amplitudes.map((v,j)=>cs(v,P2.amplitudes[j]));
  const DE=[C(1,1),CC(F(-6,7),F(-6,7)),CC(F(-3,7),F(-1,14)),C(0,1),CC(F(-1,4),F(-11,28))];
  for(let j=0;j<5;j++){
    check(ce(delta[j],DE[j])&&eq(P0.q["0"][j],P2.q["0"][j]),"witness amplitudes and Q0");
    for(const v of delta[j])check(cmp(v,F(-1))>=0n&&cmp(v,F(1))<=0n,"ten reference bands");
  }
  const sqdist=a0.reduce((v,x,k)=>add(v,norm(cs(x,a2[k]))),F(0));
  check(eq(sqdist,F(240,49))&&eq(norm(t0),F(29,98))&&eq(norm(t2),F(29,98)),"witness scale and risk");
  const rup=F(33999,62500),T=div(F(1),rup);
  check(cmp(mul(rup,rup),F(29,98))>0n,"upper scale above witness");
  const rows=[];
  for(let j=0;j<5;j++){
    rows.push([c[j][0],neg(c[j][1]),neg(d[j][0]),d[j][1]]);
    rows.push([c[j][1],c[j][0],neg(d[j][1]),neg(d[j][0])]);
  }
  function circle(t){const t2=mul(t,t),den=add(F(1),t2);return [div(sub(F(1),t2),den),div(mul(F(2),t),den)];}
  function rotate(p,q){let a=p;for(let k=0;k<q;k++)a=[neg(a[1]),a[0]];return a;}
  const cache=new Map();
  function triangle(q,a,b){
    const key=`${q},${fmt(a)},${fmt(b)}`;
    if(cache.has(key))return cache.get(key);
    const p=rotate(circle(a),q),r=rotate(circle(b),q);
    const det=sub(mul(p[0],r[1]),mul(p[1],r[0]));
    check(cmp(det,F(0))>0n,"outward tangent triangle");
    const v=[div(sub(r[1],p[1]),det),div(sub(p[0],r[0]),det)];
    const tri=[p,r,v];cache.set(key,tri);return tri;
  }
  function separator(row,Z,W){
    const zv=Z.map(z=>add(mul(row[0],z[0]),mul(row[1],z[1])));
    const wv=W.map(w=>add(mul(row[2],w[0]),mul(row[3],w[1])));
    const min=arr=>arr.reduce((x,y)=>cmp(x,y)<0n?x:y),max=arr=>arr.reduce((x,y)=>cmp(x,y)>0n?x:y);
    const lo=add(min(zv),min(wv)),hi=add(max(zv),max(wv));
    if(cmp(lo,T)>0n)return ["+",lo];
    if(cmp(hi,neg(T))<0n)return ["-",hi];
    return null;
  }
  const stack=[];
  for(let qz=0;qz<4;qz++)for(let qw=0;qw<4;qw++)stack.push([qz,F(0),F(1),qw,F(0),F(1)]);
  const leaves=[];let splits=0;
  while(stack.length){
    const [qz,a,b,qw,e,f]=stack.pop(),Z=triangle(qz,a,b),W=triangle(qw,e,f);
    let witness=null;
    for(let k=0;k<10;k++){
      const ans=separator(rows[k],Z,W);
      if(ans){witness=[k,ans[0],ans[1]];break;}
    }
    if(witness){leaves.push([qz,fmt(a),fmt(b),qw,fmt(e),fmt(f),witness[0],witness[1],fmt(witness[2])]);continue;}
    check(++splits<100000,"unresolved cover");
    if(cmp(sub(b,a),sub(f,e))>=0n){
      const mid=div(add(a,b),F(2));
      stack.push([qz,a,mid,qw,e,f],[qz,mid,b,qw,e,f]);
    } else {
      const mid=div(add(e,f),F(2));
      stack.push([qz,a,b,qw,e,mid],[qz,a,b,qw,mid,f]);
    }
  }
  const groups=Array.from({length:16},()=>[]);
  for(const leaf of leaves){
    const [qz,sa,sb,qw,se,sf,k,sign,bound]=leaf;
    const a=parse(sa),b=parse(sb),e=parse(se),f=parse(sf);
    const proof=separator(rows[k],triangle(qz,a,b),triangle(qw,e,f));
    check(proof!==null&&proof[0]===sign&&eq(proof[1],parse(bound)),"leaf bound exact readback");
    groups[4*qz+qw].push([a,b,e,f]);
  }
  for(let j=0;j<16;j++){
    const rects=groups[j],pool=new Map();
    for(const val of [F(0),F(1),...rects.flatMap(x=>[x[0],x[1]])])pool.set(fmt(val),val);
    const xs=[...pool.values()].sort(ord);
    check(eq(xs[0],F(0))&&eq(xs[xs.length-1],F(1)),"quarter endpoint");
    for(let i=1;i<xs.length;i++){
      const l=xs[i-1],r=xs[i];
      const ys=rects.filter(v=>cmp(v[0],l)<=0n&&cmp(v[1],r)>=0n).map(v=>[v[2],v[3]]);
      ys.sort((a,b)=>ord(a[0],b[0]));
      let cursor=F(0);
      for(const [start,end] of ys){check(eq(start,cursor),"gap/overlap in cover");cursor=end;}
      check(eq(cursor,F(1)),"root rectangle uncovered");
    }
  }
  check(leaves.length===556&&splits===540&&reads===60&&pairs===820,"scoped exact audit");
  return {
    schema:"PREFIX320_RATIONAL_ARC_BRC_CERTIFICATE_V1",
    verdict:"PASS_AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED",
    global_snapshot:"aa049ca1798f16f4b7d0c9465dd30057b5a91229",
    enterprise_math_snapshot:"52594434191ce4db3377c3988171665da451a262",
    A_over_8:A.map(row=>row.map(str)),b0:b0.map(str),b2:b2.map(str),
    c_from_source_tagged_BRC:c.map(str),d_from_source_tagged_BRC:d.map(str),
    rcrit_lower:"sqrt(58)/14",rcrit_upper_strict:fmt(rup),
    exact_squared_gap:fmt(sub(mul(rup,rup),F(29,98))),
    rational_strip_threshold:fmt(T),
    quadrants:16,splits,leaves:leaves.length,nodes:splits+leaves.length,
    independent_exact_coverage_sweep:"PASS",
    rows:rows.map(row=>row.map(fmt)),leaf_certificate:leaves,
    witness_a0:a0.map(str),witness_a2:a2.map(str),
    witness_port_amplitude_differences:delta.map(str),
    witness_common_report:{
      Q0:P0.q["0"].map(fmt),
      Q1:P0.q["1"].map((v,j)=>fmt(div(add(v,P2.q["1"][j]),F(2)))),
      Qi:P0.q["i"].map((v,j)=>fmt(div(add(v,P2.q["i"][j]),F(2))))
    },
    witness_MEB_squared:"60/49",
    mixed_two_shape_same_scale_MEB_squared_upper_strict:fmt(mul(F(9),mul(rup,rup))),
    source_tagged_BRC_reads:reads,ordered_source_labelled_path_pairs:pairs,
    native_X6_Detector_bridge:"UNPROVEN"
  };
})();
if (typeof process !== "undefined" && process.stdout) process.stdout.write(JSON.stringify(certificate, null, 2)+"\n");
