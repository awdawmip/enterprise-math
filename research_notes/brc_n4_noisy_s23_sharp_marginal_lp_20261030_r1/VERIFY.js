function verifyExact(){
  const B=x=>BigInt(x);
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t}return a||1n}
  function F(n,d=1){let a=B(n),b=B(d);if(b<0n){a=-a;b=-b}if(!b)throw Error("zero denominator");const g=gcd(a,b);return[a/g,b/g]}
  const a=(x,y)=>F(x[0]*y[1]+y[0]*x[1],x[1]*y[1]),neg=x=>F(-x[0],x[1]),sub=(x,y)=>a(x,neg(y)),mul=(x,y)=>F(x[0]*y[0],x[1]*y[1]),div=(x,y)=>F(x[0]*y[1],x[1]*y[0]),cmp=(x,y)=>{const d=x[0]*y[1]-y[0]*x[1];return d<0n?-1:d>0n?1:0},eq=(x,y)=>cmp(x,y)===0,abs=x=>cmp(x,F(0))<0?neg(x):x,max=(...z)=>z.reduce((x,y)=>cmp(x,y)>0?x:y),min=(...z)=>z.reduce((x,y)=>cmp(x,y)<0?x:y),fmt=x=>x[1]===1n?String(x[0]):x[0]+"/"+x[1];
  const Z=F(0),O=F(1),T=F(2),p=F(1,10),k=F(4,5),half=F(1,2),quarter=F(1,4);
  const qs=[F(1,6),F(1,3),quarter,quarter],rs=[[F(9,10),F(11,10)],[quarter,quarter],[F(1,5),F(9,5)],[T,T]];
  let Psum=Z,Qsum=Z,nLeaves=0;
  for(let i=0;i<4;i++)for(let j=0;j<2;j++)for(let t=0;t<2;t++){const pq=div(mul(qs[i],rs[i][j]),F(4)),qq=div(qs[i],F(4));if(cmp(pq,Z)<=0||cmp(qq,Z)<=0)throw Error("nonpositive leaf");Psum=a(Psum,pq);Qsum=a(Qsum,qq);nLeaves++}
  if(nLeaves!==16||!eq(Psum,O)||!eq(Qsum,O))throw Error("leaf normalization");
  function game(e,u,v){
    const q=div(a(u,v),T),d=mul(F(2,5),abs(sub(v,u))),rho=mul(k,sub(O,mul(T,e))),s=cmp(v,u);
    let E=Z,w=q,x=q,y=q;
    if(s!==0){
      E=max(Z,div(sub(d,mul(rho,q)),a(T,s>0?rho:neg(rho))),div(sub(d,mul(rho,sub(O,q))),sub(T,s>0?rho:neg(rho))));
      w=a(q,s>0?E:neg(E));
      const cap=mul(T,min(w,sub(O,w)));
      let z=Z;
      if(cmp(rho,Z)>0) z=min(cap,div(mul(T,max(Z,sub(d,E))),rho));
      x=a(w,s>0?neg(div(z,T)):div(z,T));
      y=a(w,s>0?div(z,T):neg(div(z,T)));
    }
    const aa=a(p,mul(k,e)),b=sub(O,aa),tp=a(mul(p,u),mul(sub(O,p),v));
    const pp=a(mul(aa,x),mul(b,y)),qq=div(a(x,y),T);
    if([x,y,w].some(z=>cmp(z,Z)<0||cmp(z,O)>0))throw Error("invalid decoder");
    if(!eq(max(abs(sub(pp,tp)),abs(sub(qq,q))),E))throw Error("not attaining sharp rate");
    return {E,R:div(E,F(4)),x,y};
  }
  let checked=0;
  for(let i=0;i<=4;i++)for(let j=0;j<=8;j++)for(let l=0;l<=8;l++){game(F(i,8),F(j,8),F(l,8));checked++}
  let ex=[
    [F(1,4),F(1,4),F(3,4),Z],
    [F(1,4),Z,F(1,2),F(1,96)],
    [F(1,4),F(9,10),O,F(1,320)],
    [F(1,4),Z,O,F(1,32)],
    [F(1,2),Z,O,F(1,20)],
    [F(1,4),O,F(9,10),F(1,480)]
  ];
  let lines=["PASS: "+nLeaves+" strictly-positive P/Q leaves normalized exactly; "+checked+" exact S23 noisy-sensor parameter triples."];
  for(const [e,u,v,expect] of ex){const z=game(e,u,v);if(!eq(z.R,expect))throw Error("rational witness wrong");lines.push(`EXACT eps=${fmt(e)},u=${fmt(u)},v=${fmt(v)}: R=${fmt(z.R)}; (x,y)=(${fmt(z.x)},${fmt(z.y)})`)}
  const f0=[F(3,4),F(1,8),Z,Z,F(1,8)],f1=[quarter,Z,F(3,8),F(3,8),Z];
  const K0=[O,Z,Z,Z,Z],K1=[Z,F(1,56),F(27,56),F(11,28),F(3,28)];
  const es=quarter,aa=a(p,mul(k,es)),bb=sub(O,aa),TP=f0.map((x,i)=>a(mul(p,x),mul(sub(O,p),f1[i]))),TQ=f0.map((x,i)=>div(a(x,f1[i]),T));
  const tv=(x,y)=>div(x.reduce((z,t,i)=>a(z,abs(sub(t,y[i]))),Z),T);
  const predP=K0.map((x,i)=>a(mul(aa,x),mul(bb,K1[i]))),predQ=K0.map((x,i)=>div(a(x,K1[i]),T));
  if(!eq(K1.reduce(a,Z),O)||!eq(tv(predP,TP),F(1,16))||!eq(tv(predQ,TQ),F(1,16)))throw Error("S2 primal witness");
  const lambda=F(5,12),h=[Z,Z,lambda,lambda,Z],t=[F(7,12),F(7,12),Z,Z,F(7,12)],M0=F(7,24),M1=M0;
  let obj=neg(a(M0,M1));
  for(let i=0;i<5;i++){
    if(cmp(h[i],Z)<0||cmp(h[i],lambda)>0||cmp(t[i],Z)<0||cmp(t[i],sub(O,lambda))>0)throw Error("S2 dual range");
    if(cmp(a(mul(aa,h[i]),div(t[i],T)),M0)>0||cmp(a(mul(bb,h[i]),div(t[i],T)),M1)>0)throw Error("S2 dual facet");
    obj=a(obj,a(mul(h[i],TP[i]),mul(t[i],TQ[i])));
  }
  if(!eq(obj,F(1,16)))throw Error("S2 dual objective");
  lines.push("PASS: lawful S2 u=1/4,v=3/4,eps=1/4,d=(1,0,0,1): exact rational primal=dual=1/16 BU, global marginal R=1/64.");
  lines.push("S23 terminal-Q at same eps,u,v: global marginal R=0. All-real proof and general finite-LP dual in PROOF.md.");
  return lines.join("\n")+"\n";
}
console.log(verifyExact());
