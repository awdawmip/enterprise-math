"use strict";
function verify(){
  "use strict";
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
  function F(a,b=1){a=BigInt(a);b=BigInt(b);if(b===0n)throw Error("div0");if(b<0n){a=-a;b=-b;}let g=gcd(a,b);return {n:a/g,d:b/g};}
  const A=(a,b)=>F(a.n*b.d+b.n*a.d,a.d*b.d), M=(a,b)=>F(a.n*b.n,a.d*b.d);
  const S=(a,b)=>F(a.n*b.d-b.n*a.d,a.d*b.d), V=(a,b)=>F(a.n*b.d,a.d*b.n);
  const C=(a,b)=>{let n=a.n*b.d-b.n*a.d;return n<0n?-1:n>0n?1:0;};
  const EQ=(a,b)=>C(a,b)===0, Z=F(0), ONE=F(1), eps=F(1,1000), eta=F(1,1000), lam=F(1,22);
  const SHOW=a=>a.d===1n?String(a.n):a.n+"/"+a.d;
  function need(q,s){if(!q)throw Error("FAIL "+s);}
  const nd={};
  function root(id,p,q){nd[id]={id,t:1,p,q,ch:[]};}
  function child(id,parent,p1,q1,one){
    const n=nd[parent],p=M(n.p,one?p1:S(ONE,p1)),q=M(n.q,one?q1:S(ONE,q1));
    nd[id]={id,t:n.t+1,p,q,ch:[]};n.ch.push(id);
  }
  root("A",F(1,3),F(2,3));root("B",F(2,3),F(1,3));
  child("A0","A",F(1,2),F(1,4),false);child("A1","A",F(1,2),F(1,4),true);
  child("B0","B",F(1,4),F(1,2),false);child("B1","B",F(1,4),F(1,2),true);
  for(const [s,p,q] of [["A0",F(1,2),F(2,5)],["A1",F(1,2),F(1,4)],["B0",F(1,2),F(3,5)],["B1",F(2,3),F(1,3)]]){
    child(s+"0",s,p,q,false);child(s+"1",s,p,q,true);
  }
  const names=Object.keys(nd),nodes=names.map(x=>nd[x]);
  for(const n of nodes)n.lr=V(n.p,n.q);
  const keys=[];
  for(const n of nodes)if(!keys.some(k=>k.t===n.t&&EQ(k.lr,n.lr)))keys.push({t:n.t,lr:n.lr});
  keys.sort((a,b)=>a.t-b.t||C(a.lr,b.lr));
  const keyIndex=n=>keys.findIndex(k=>k.t===n.t&&EQ(k.lr,n.lr));
  need(nodes.length===14&&keys.length===12,"node/key count");
  need(EQ(nd.A1.lr,nd.B1.lr)&&EQ(nd.A1.lr,ONE),"time2 collision");
  need(EQ(nd.A11.lr,nd.B11.lr)&&EQ(nd.A11.lr,F(2)),"time3 collision");
  need(EQ(A(nd.A11.p,nd.B11.p),F(7,36)),"positive branch P mass");
  need(EQ(A(A(nd.A11.p,nd.A11.q),A(nd.B11.p,nd.B11.q)),F(7,24)),"time deficit BRC mass");
  for(const n of nodes){
    need(C(n.p,Z)>0&&C(n.q,Z)>0,"positive history "+n.id);
    if(n.ch.length){
      let ps=Z,qs=Z;
      for(const ch of n.ch){ps=A(ps,nd[ch].p);qs=A(qs,nd[ch].q);}
      need(EQ(ps,n.p)&&EQ(qs,n.q),"normalized "+n.id);
    }
  }
  function rates(n,t,kap){
    let p=A(A(F(1,5),F(t,20)),V(F(t+1,100),n.lr));
    let q=A(S(F(2,5),F(t,30)),M(F(t+2,200),n.lr));
    if(t===2&&n.id==="A1")p=A(p,eps);
    if(t===2&&n.id==="B1")p=S(p,eps);
    if(t===3&&n.id==="A11"){p=A(p,kap);q=A(q,eta);}
    if(t===3&&n.id==="B11"){p=A(p,kap);q=S(q,eta);}
    return [p,q];
  }
  for(const kap of [eps,M(eps,F(75,44))]){
    for(const n of nodes)for(const t of n.t===3?[3,4]:[n.t]){
      let [p,q]=rates(n,t,kap);
      need(C(p,Z)>0&&C(p,ONE)<0&&C(q,Z)>0&&C(q,ONE)<0,"positive errors "+n.id+"/"+t);
    }
  }
  function stops(bits,kind){
    const out=[];
    function visit(id){
      const n=nd[id],j=kind==="LR"?keyIndex(n):names.indexOf(id);
      if(n.t===3){out.push([n,(bits[j]===1)?3:4]);return;}
      if(bits[j]===1){out.push([n,n.t]);return;}
      for(const ch of n.ch)visit(ch);
    }
    visit("A");visit("B");
    return out;
  }
  function stats(st){
    let rp=Z,tp=Z,tq=Z,m=Z;
    for(const [n,t] of st){
      tp=A(tp,M(n.p,F(t)));tq=A(tq,M(n.q,F(t)));
      if(t===2&&n.id==="A1")rp=A(rp,n.p);
      if(t===2&&n.id==="B1")rp=S(rp,n.p);
      if(t===3&&(n.id==="A11"||n.id==="B11"))m=A(m,n.p);
    }
    need(EQ(tp, tp)&&EQ(tq,tq),"bounded fractions");
    const d=S(F(8),A(tp,tq)),f=S(rp,M(lam,d));
    return {f,m,d,rp};
  }
  const bestFull=new Map(),bestLR=new Map();
  function bitsFromInt(i,len){return Array.from({length:len},(_,j)=>(i>>(len-1-j))&1);}
  let lrPts={};
  for(const [kind,total,table] of [["FULL",1<<names.length,bestFull],["LR",1<<keys.length,bestLR]]){
    for(let i=0;i<total;i++){
      const st=stops(bitsFromInt(i,kind==="LR"?keys.length:names.length),kind);
      const {f,m}=stats(st), k=SHOW(m);
      if(!table.has(k)||C(f,table.get(k))>0)table.set(k,f);
      if(kind==="LR"&&[0,1,2,4,1028].includes(i))lrPts[i]=st;
    }
  }
  function checkMap(table,expected,label){
    need(table.size===expected.length,label+" group number");
    for(const [m,f] of expected)need(table.has(m)&&EQ(table.get(m),F(f[0],f[1])),label+" mass "+m);
  }
  checkMap(bestFull,[["0",[3,22]],["1/12",[-1,176]],["1/9",[17,132]],["7/36",[-7,528]]],"FULL");
  checkMap(bestLR,[["0",[0,1]],["1/12",[-25,176]],["1/9",[-19,132]],["7/36",[-7,528]]],"LR");
  function support(table,rho){
    let top=null;
    for(const [s,f] of table){const m=s.includes("/")?F(...s.split("/").map(Number)):F(Number(s));let x=A(f,M(rho,m));if(top===null||C(x,top)>0)top=x;}
    return top;
  }
  for(const [r,fl,lr,gap] of [
    [F(0),F(3,22),Z,F(3,22)],
    [F(3,44),F(3,22),Z,F(3,22)],
    [F(1),F(95,396),F(287,1584),F(31,528)],
    [F(75,44),A(F(17,132),V(F(75,44),F(9))),A(M(F(7,36),F(75,44)),F(-7,528)),Z],
    [F(2),A(M(F(7,36),F(2)),F(-7,528)),A(M(F(7,36),F(2)),F(-7,528)),Z]
  ]){
    let a=support(bestFull,r),b=support(bestLR,r);
    need(EQ(a,fl)&&EQ(b,lr)&&EQ(S(a,b),gap),"support at rho "+SHOW(r));
  }
  function observation(st,kap){
    let obs=[Z,Z,Z,Z];
    for(const [n,t] of st){const [p,q]=rates(n,t,kap);
      obs=[A(obs[0],M(n.p,p)),A(obs[1],M(n.q,q)),A(obs[2],M(n.p,F(t))),A(obs[3],M(n.q,F(t)))];
    }
    return obs;
  }
  function scriptedStop(ids){
    const out=[];
    function visit(id){let n=nd[id];if(ids[id]!==undefined){out.push([n,ids[id]]);return;}if(n.t===3){out.push([n,4]);return;}for(const ch of n.ch)visit(ch);}
    visit("A");visit("B");return out;
  }
  const Ostar=observation(scriptedStop({A1:2,B11:3}),eps);
  const expected=[F(509,1200),F(16597,54000),F(32,9),F(65,18)];
  need(Ostar.every((x,i)=>EQ(x,expected[i])),"full four-vector witness");
  const other=observation(scriptedStop({A11:3,B11:3}),eps);
  need(other.every((x,i)=>EQ(x,[F(879,2000),F(64567,216000),F(137,36),F(281,72)][i])),"LR supporting witness");
  const integerLHS=o=>S(S(M(F(17424000),o[0]),M(F(870408),o[2])),M(F(173448),o[3]));
  const lhs=integerLHS(Ostar), rhs=F(3668533);
  need(EQ(lhs,F(3669556))&&EQ(S(lhs,rhs),F(1023)),"integer separator");
  const base=observation(lrPts[0],eps);
  const cols=[1,2,4,1028].map(i=>observation(lrPts[i],eps).map((x,j)=>S(x,base[j])));
  function det4(c){
    let mat=Array.from({length:4},(_,r)=>Array.from({length:4},(_,j)=>c[j][r])),det=ONE;
    for(let j=0;j<4;j++){
      let k=j;while(k<4&&EQ(mat[k][j],Z))k++;
      need(k<4,"affine rank");
      if(k!==j){[mat[k],mat[j]]=[mat[j],mat[k]];det=S(Z,det);}
      let pv=mat[j][j];det=M(det,pv);
      for(let i=j+1;i<4;i++){let coeff=V(mat[i][j],pv);for(let h=j;h<4;h++)mat[i][h]=S(mat[i][h],M(coeff,mat[j][h]));}
    }
    return det;
  }
  need(EQ(det4(cols),F(1,12960000000)),"full-rank LR convex hull");
  const gap=M(eps,F(31,528)),norm=F(11659,11000),dist=V(gap,norm);
  need(EQ(dist,F(31,559632)),"L_infinity bound");
  return [
    "ENTERPRISE_MATH_R5_EXACT_UNIFORM_STAGE3_P_COMPENSATION",
    "model_nodes=14; LR_keys=12; FULL_binary_policies=16384; LR_binary_policies=4096",
    "BRC_P_mass_A11_B11=7/36; BRC_PplusQ_time_deficit=7/24",
    "FULL_max_intercepts_by_m=0:3/22;1/12:-1/176;1/9:17/132;7/36:-7/528",
    "LR_max_intercepts_by_m=0:0;1/12:-25/176;1/9:-19/132;7/36:-7/528",
    "support_gap/epsilon=3/22 for 0<=rho<=3/44; 25/176-rho/12 for 3/44<=rho<=75/44; 0 for rho>=75/44 (admissible kernels)",
    "rho=1: FULL_support/epsilon=95/396; LR_support/epsilon=287/1584; gap=31/528",
    "FULL_witness_O="+Ostar.map(SHOW).join(","),
    "LR_support_witness_O="+other.map(SHOW).join(","),
    "LR_integer_inequality=17424000 eP - 870408 TP - 173448 TQ <= 3668533",
    "FULL_integer_lhs="+SHOW(lhs)+"; right="+SHOW(rhs)+"; integer_gap=1023",
    "LR_affine_dim=4; determinant="+SHOW(det4(cols)),
    "distance_Linf_lower_bound="+SHOW(dist),
    "PASS_EXACT_R5_UNIFORM_STAGE3_COMPENSATION_ENVELOPE"
  ].join("\n")+"\n";
}
console.log(verify().trimEnd());
