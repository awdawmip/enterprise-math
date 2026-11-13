// EC49AJ independent arithmetic-implementation check in JavaScript BigInt.
// Run node VERIFY.js; exact fractions, no floating point or external packages.
const gcd=(a,b)=>{if(a<0n)a=-a;if(b<0n)b=-b;while(b){const r=a%b;a=b;b=r;}return a};
const R=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g}};
const add=(a,b)=>R(a.n*b.d+b.n*a.d,a.d*b.d),neg=a=>R(-a.n,a.d),sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>R(a.n*b.n,a.d*b.d),div=(a,b)=>R(a.n*b.d,a.d*b.n);
const cmp=(a,b)=>a.n*b.d<b.n*a.d?-1:a.n*b.d>b.n*a.d?1:0;
const mx=(a,b)=>cmp(a,b)>=0?a:b,eq=(a,b)=>cmp(a,b)===0;
const S=a=>a.d===1n?a.n.toString():a.n+'/'+a.d;
const Z=R(0),O=R(1),ETA=R(3,10),K=R(177,172),LAM=R(49,860),C20=R(7,8),C1=R(43,48);
const E=[Z,R(3,128),R(179,2592),R(3,32)];
const sum=xs=>xs.reduce(add,Z);
const chk=(ok,m)=>{if(!ok)throw Error('EC49AJ BigInt exact failure: '+m)};
const t=(w,u)=>add(R(1,2),mul(R((2*u-1)*(1-w)),ETA));
const P=(w,u,z)=>mul(t(w,u),w===z?R(1,6):R(1,12));
const Q=(w,u,z)=>div(t(w,u),R(9));
const q=(x,c,u)=>div(sum([0,1,2].map(w=>mul(x[w][c],t(w,u)))),R(3));
const d=(x,c,u,z)=>sum([0,1,2].map(w=>mul(x[w][c],sub(P(w,u,z),mul(K,Q(w,u,z))))));
const phi=(x,c,u)=>sum([0,1,2].map(z=>mx(Z,d(x,c,u,z))));
const H=x=>sum([0,1,2,3].flatMap(c=>[0,1].map(u=>phi(x,c,u))));
const dual=(x,e)=>{
 const parts=[];
 for(let c=0;c<4;c++)for(let u=0;u<2;u++)parts.push(mx(Z,sub(phi(x,c,u),mul(LAM,q(x,c,u)))));
 return add(mul(LAM,sub(C20,e)),sum(parts));
};
const Y=e=>[[sub(R(9,16),mul(R(6),e)),Z,add(R(1,16),mul(R(3),e)),Z],[Z,O,Z,Z],[O,Z,Z,Z]];
const templates=e=>{
 const B=add(R(1,16),mul(R(3),e)),out=[];
 for(const b of [Z,B])for(let i=0;i<3;i++)for(let j=0;j<3;j++)for(let al=0;al<8;al++)for(let bl=0;bl<2;bl++){
  const x=Array.from({length:3},()=>[Z,Z,Z,Z]);
  for(let w=0;w<3;w++){
   const stop=w===i?add(R(5,16),b):Z,bb=w===j?b:Z;
   x[w][(al>>w)&1]=sub(sub(O,stop),bb);
   x[w][2+bl]=add(x[w][2+bl],bb);
  }
  out.push(x);
 }return out;
};
const costs=(x,e,allBuy)=>{
 for(const row of x)chk(row.every(v=>cmp(v,Z)>=0)&&cmp(sum(row),O)<=0,'first stage row');
 const c1=div(sum(x.map(row=>sum([row[0],row[1],mul(R(2),add(row[2],row[3]))]))),R(3));
 const paid=sum([0,1,2,3].flatMap(c=>[0,1].map(u=>q(x,c,u))));
 chk(eq(c1,C1)&&cmp(paid,sub(C20,e))>=0,'first and second costs');
 if(allBuy)chk(eq(paid,sub(C20,e)),'exact bought sensor cost');
};
const sharp=e=>{
 const pieces=[[E[0],E[1],R(919,8256),neg(R(49,860))],
               [E[1],E[2],R(4451,41280),R(79,860)],
               [E[2],E[3],R(249,2752),R(59,172)]];
 for(const [a,b,v,slope] of pieces){
  if(cmp(a,e)<=0&&cmp(e,b)<=0)return add(v,mul(slope,e));
 }
 throw Error('out of validated interval');
};
let ps=Z,qs=Z;
for(let w=0;w<3;w++)for(let u=0;u<2;u++){
 chk(eq(sum([0,1,2].map(z=>P(w,u,z))),div(t(w,u),R(3))),'P marginal');
 chk(eq(sum([0,1,2].map(z=>Q(w,u,z))),div(t(w,u),R(3))),'Q marginal');
 for(let z=0;z<3;z++){
  const a=P(w,u,z),b=Q(w,u,z);chk(cmp(a,Z)>0&&cmp(b,Z)>0,'strictly positive leaf');
  ps=add(ps,a);qs=add(qs,b);
 }
}
chk(eq(ps,O)&&eq(qs,O),'full 18-leaf normalization');
const endpoints=[];
for(const e of E){
 const y=Y(e),target=sharp(e);
 costs(y,e,true);chk(eq(H(y),target),'sharp attaining source value');
 const vv=templates(e);chk(vv.length===288,'indexed templates count');
 const unique=new Set(vv.map(x=>x.flat().map(S).join(',')));
 chk(unique.size===(eq(e,E[3])?144:168),'distinct templates count');
 let hi=null,lo=null,ties=0;
 for(const x of vv){
  costs(x,e,false);const v=dual(x,e);
  chk(cmp(v,target)<=0,'dual inequality');
  if(hi===null||cmp(v,hi)>0)hi=v;
  if(lo===null||cmp(v,lo)<0)lo=v;
  if(eq(v,target))ties++;
 }
 chk(eq(hi,target),'sharp global dual equality');
 endpoints.push({epsilon:S(e),C2:S(sub(C20,e)),sharp_support:S(target),
   dual_max:S(hi),dual_min:S(lo),indexed:vv.length,distinct:unique.size,ties});
}
const change0=e=>d(Y(e),0,1,0),change2=e=>d(Y(e),0,1,2);
chk(eq(change0(Z),R(179,10320))&&eq(sub(change0(O),change0(Z)),neg(R(54,215))),'atom 0 slope');
chk(eq(change2(Z),neg(R(3,860)))&&eq(sub(change2(O),change2(Z)),R(32,215)),'atom 2 slope');
chk(eq(change0(E[2]),Z)&&eq(change2(E[1]),Z),'two exact sign roots');
console.log(JSON.stringify({
 schema:'EC49AJ_INDEPENDENT_BIGINT_CROSSCHECK_V1',source_normalized:'P=Q=1',
 lambda_dual:S(LAM),endpoints,
 sharp_pieces:['919/8256-49epsilon/860','4451/41280+79epsilon/860','249/2752+59epsilon/172'],
 result:'PASS_EXACT_BIGINT_AUTHOR_CROSSCHECK',
 independent_math_review:'NOT_PERFORMED',native_BRC_transfer:'NOT_CLAIMED'
},null,2));