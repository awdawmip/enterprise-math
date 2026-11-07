// Enterprise Math R5: exact BigInt rational envelope certificate.
// Run: node VERIFY.js (Node 20+; no external packages).
"use strict";
function verify() {
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
  function F(n,d=1){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
  const A=(x,y)=>F(x.n*y.d+y.n*x.d,x.d*y.d);
  const N=x=>F(-x.n,x.d);
  const S=(x,y)=>A(x,N(y));
  const M=(x,y)=>F(x.n*y.n,x.d*y.d);
  const V=(x,y)=>F(x.n*y.d,x.d*y.n);
  const C=(x,y)=>{const z=x.n*y.d-y.n*x.d;return z<0n?-1:z>0n?1:0;};
  const EQ=(x,y)=>C(x,y)===0;
  const SHOW=x=>x.d===1n?String(x.n):String(x.n)+"/"+String(x.d);
  function need(test,msg){if(!test)throw Error("FAIL "+msg);}
  const ZERO=F(0),ONE=F(1),eps=F(1,1000),eta=F(1,1000);
  const nodes={},roots=["A","B"];
  function root(id,p,q){nodes[id]={id,t:1,p,q,children:[]};}
  function child(id,parent,p1,q1,one){
    const n=nodes[parent],p=M(n.p,one?p1:S(ONE,p1)),q=M(n.q,one?q1:S(ONE,q1));
    nodes[id]={id,t:n.t+1,p,q,children:[]};n.children.push(id);
  }
  root("A",F(1,3),F(2,3));root("B",F(2,3),F(1,3));
  child("A0","A",F(1,2),F(1,4),false);child("A1","A",F(1,2),F(1,4),true);
  child("B0","B",F(1,4),F(1,2),false);child("B1","B",F(1,4),F(1,2),true);
  for(const [parent,p1,q1] of [
    ["A0",F(1,2),F(2,5)],["A1",F(1,2),F(1,4)],
    ["B0",F(1,2),F(3,5)],["B1",F(2,3),F(1,3)]
  ]){child(parent+"0",parent,p1,q1,false);child(parent+"1",parent,p1,q1,true);}
  const L=n=>V(n.p,n.q);
  function rates(n,t){
    const l=L(n);
    let p=A(A(F(1,5),F(t,20)),V(F(t+1,100),l));
    let q=A(S(F(2,5),F(t,30)),M(F(t+2,200),l));
    if(t===2&&n.id==="A1")p=A(p,eps);
    if(t===2&&n.id==="B1")p=S(p,eps);
    if(t===3&&n.id==="A11")q=A(q,eta);
    if(t===3&&n.id==="B11")q=S(q,eta);
    return [p,q];
  }
  need(Object.keys(nodes).length===14,"node count");
  need(EQ(A(nodes.A.p,nodes.B.p),ONE)&&EQ(A(nodes.A.q,nodes.B.q),ONE),"initial normalization");
  for(const n of Object.values(nodes)){
    need(C(n.p,ZERO)>0&&C(n.q,ZERO)>0,"positive cylinder "+n.id);
    if(n.children.length){
      const p=n.children.reduce((x,k)=>A(x,nodes[k].p),ZERO);
      const q=n.children.reduce((x,k)=>A(x,nodes[k].q),ZERO);
      need(EQ(p,n.p)&&EQ(q,n.q),"edge normalization "+n.id);
    }
    for(const t of n.t===3?[3,4]:[n.t]){
      const [p,q]=rates(n,t);
      need(C(p,ZERO)>0&&C(p,ONE)<0&&C(q,ZERO)>0&&C(q,ONE)<0,"positive error rates "+n.id+" "+t);
    }
  }
  for(const k of ["A1","B1"])need(EQ(L(nodes[k]),ONE),"time 2 LR collision "+k);
  for(const k of ["A11","B11"])need(EQ(L(nodes[k]),F(2)),"time 3 LR collision "+k);
  // Full-history witness: stop at time 2 only on A1; otherwise forced t4.
  let obs=[ZERO,ZERO,ZERO,ZERO];
  function collect(n,t){
    const [p,q]=rates(n,t);
    obs=[A(obs[0],M(n.p,p)),A(obs[1],M(n.q,q)),
         A(obs[2],M(n.p,F(t))),A(obs[3],M(n.q,F(t)))];
  }
  function walk(id){
    const n=nodes[id];
    if(n.t===2&&id==="A1"){collect(n,2);return;}
    if(n.t===3){collect(n,4);return;}
    for(const k of n.children)walk(k);
  }
  roots.forEach(walk);
  const expected=[F(2581,6000),F(551,1800),F(11,3),F(11,3)];
  need(obs.every((x,i)=>EQ(x,expected[i])),"full witness four-observer tuple");
  const R=S(S(S(obs[0],F(21,100)),V(obs[2],F(20))),V(obs[3],F(100)));
  const D=S(F(8),A(obs[2],obs[3]));
  need(EQ(R,F(1,6000))&&EQ(D,F(2,3)),"exact residual and time loss");
  function point(alpha,beta,a,b){
    const x=M(alpha,a),y=M(beta,b);
    return {u:V(S(x,y),F(6)),
      d:A(M(F(3),S(F(2),A(alpha,beta))),M(F(2,3),A(x,y)))};
  }
  const full=[],lr=[];
  for(let i=0;i<16;i++){
    const bit=j=>F((i>>j)&1);
    full.push(point(bit(0),bit(1),bit(2),bit(3)));
  }
  for(let i=0;i<8;i++){
    const bit=j=>F((i>>j)&1);
    lr.push(point(bit(0),bit(1),bit(2),bit(2)));
  }
  function val(v,lambda){return S(v.u,M(lambda,v.d));}
  function envelopeCheck(corners,kink,label){
    // The claimed line joins (0,1/6) and (kink,0).
    // Each corner line is below it at both endpoints. For lambda >= kink,
    // all corner lines are nonincreasing and nonpositive.
    for(const v of corners){
      need(C(v.d,ZERO)>=0,label+" nonnegative time loss");
      need(C(val(v,ZERO),F(1,6))<=0,label+" endpoint zero");
      need(C(val(v,kink),ZERO)<=0,label+" kink endpoint");
    }
  }
  envelopeCheck(full,F(1,4),"FULL");
  envelopeCheck(lr,F(1,22),"LR");
  const fw=point(ONE,ONE,ONE,ZERO);
  const lw=point(ONE,ZERO,ONE,ONE);
  const nw=point(ONE,ONE,ZERO,ZERO);
  need(EQ(fw.u,F(1,6))&&EQ(fw.d,F(2,3)),"FULL envelope witness");
  need(EQ(lw.u,F(1,6))&&EQ(lw.d,F(11,3)),"LR envelope witness");
  need(EQ(nw.u,ZERO)&&EQ(nw.d,ZERO),"never-stop envelope witness");
  const lambda=F(1,22);
  const optGap=S(val(fw,lambda),val(nw,lambda));
  need(EQ(optGap,F(3,22))&&EQ(val(lw,lambda),ZERO),"optimized gap");
  const LHS=S(S(M(F(22000),obs[0]),M(F(1099),obs[2])),M(F(219),obs[3]));
  need(EQ(LHS,F(4631))&&EQ(S(LHS,F(4628)),F(3)),"integer separator");
  const norm=S(F(53,50),V(eps,F(11)));
  const distance=V(M(eps,optGap),norm);
  need(EQ(norm,F(11659,11000))&&EQ(distance,F(3,23318)),"optimal-family distance");
  need(C(distance,F(1,10598))>0,"strict improvement over prior certificate");
  return [
    "R5_EXACT_BIGINT_RATIONAL_TIME_TRADEOFF",
    "natural_positive_nodes=14; time2_collision=A1=B1:L1; time3_collision=A11=B11:L2",
    "FULL_corner_count="+full.length+"; LR_corner_count="+lr.length,
    "FULL_support_u_minus_lambda_d=max(0,1/6-2lambda/3) for all lambda>=0",
    "LR_support_u_minus_lambda_d=max(0,1/6-11lambda/3) for all lambda>=0",
    "gap_piecewise=3lambda (0..1/22), 1/6-2lambda/3 (1/22..1/4), 0 (>=1/4)",
    "optimal_lambda=1/22; optimal_gap_over_epsilon=3/22",
    "full_witness_O="+obs.map(SHOW).join(","),
    "LR_inequality=22000 eP - 1099 TP - 219 TQ <= 4628",
    "FULL_witness_left="+SHOW(LHS)+"; right=4628; exact_integer_gap=3",
    "normalized_Linf_lower_bound="+SHOW(distance),
    "verified_exact_endpoint_envelopes=ALL_REAL_LAMBDA_NONNEGATIVE",
    "PASS_EXACT_R5_OPTIMAL_TIME_PENALTY_ENVELOPE"
  ].join("\n")+"\n";
}
const result=verify();
if(typeof console!=="undefined")console.log(result.trimEnd());
globalThis.__EM_R5_VERIFIER_OUTPUT=result;
