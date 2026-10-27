"use strict";
// Exact positive-rational checker for the two-time BRC external probability model.
// No floating point or external packages are used in this certificate.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b!==0n){[a,b]=[b,a%b];}return a;}
function R(a,b=1){a=BigInt(a);b=BigInt(b);if(b===0n)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}let g=gcd(a,b);return {a:a/g,b:b/g};}
function add(x,y){return R(x.a*y.b+y.a*x.b,x.b*y.b);}
function neg(x){return R(-x.a,x.b);}
function sub(x,y){return add(x,neg(y));}
function mul(x,y){return R(x.a*y.a,x.b*y.b);}
function div(x,y){return R(x.a*y.b,x.b*y.a);}
function cmp(x,y){let d=x.a*y.b-y.a*x.b;return d<0n?-1:d>0n?1:0;}
function max(x,y){return cmp(x,y)>=0?x:y;}
function min(x,y){return cmp(x,y)<=0?x:y;}
function abs(x){return x.a<0n?neg(x):x;}
function sum(xs){return xs.reduce(add,R(0));}
function fmt(x){return x.b===1n?x.a.toString():x.a+"/"+x.b;}
function expect(x,y,label){if(cmp(x,y)!==0)throw Error(label+": "+fmt(x)+" != "+fmt(y));}
function check(x,label){if(!x)throw Error(label);}
const z=R(0),one=R(1);
const rs=[R(1,2),R(1),R(3,2),R(2)];
const n=rs.map(()=>R(3,40));
const da=[R(1,40),R(-2,40),R(1,40),z];
const db=[z,R(1,40),R(-2,40),R(1,40)];
const ds=[da,db], ms=ds.map(d=>d.map((x,i)=>add(n[i],x)));
for(let t=0;t<2;t++){
  expect(sum(ds[t]),z,"Q mass conservation stage "+t);
  expect(sum(ds[t].map((v,i)=>mul(v,rs[i]))),z,"P mass conservation stage "+t);
  for(let i=0;i<4;i++)check(cmp(ms[t][i],z)>0,"positive Q mass "+t+","+i);
}
const earlyQ=R(2,5),earlyP=R(1,4);
expect(add(earlyQ,sum(ms.flat())),one,"normalized Q law");
expect(add(earlyP,sum(ms.flatMap(row=>row.map((v,i)=>mul(v,rs[i]))))),one,"normalized P law");
const C=(d,q)=>sum(d.map((v,i)=>mul(v,max(z,sub(rs[i],q)))));
const cs=ds.map(d=>rs.map(q=>C(d,q)));
for(let j=0;j<4;j++){
 expect(cs[0][j],j===1?R(1,80):z,"C_A knot "+j);
 expect(cs[1][j],j===2?R(1,80):z,"C_B knot "+j);
}
const stageM=(calls,q)=>rs.reduce((best,ri,i)=>max(best,mul(max(z,calls[i]),min(one,div(q,ri)))),z);
const value=q=>div(sum(cs.map(c=>stageM(c,q))),add(one,q));
const atKnots=rs.map(value);
[R(1,144),R(1,96),R(1,100),R(1,120)].forEach((x,i)=>expect(atKnots[i],x,"multitime knot "+i));
let worst=atKnots.reduce(max,z);
expect(worst,R(1,96),"global two-time excess");
const directedOne=(calls)=>rs.reduce((m,q,i)=>max(m,div(max(z,calls[i]),add(one,q))),z);
const daVal=directedOne(cs[0]),dbVal=directedOne(cs[1]);
expect(daVal,R(1,160),"one-time A");
expect(dbVal,R(1,200),"one-time B");
expect(sub(add(daVal,dbVal),worst),R(1,1200),"strict subadditivity margin");
// Check 80 additional rational ratios, using C(q) as a candidate in addition
// to the LR knots. This is a finite cross-check, not the proof for all q.
for(let k=1;k<=80;k++){
  let q=R(k,20);
  const opt=(d,calls)=>max(stageM(calls,q),max(z,C(d,q)));
  let v=div(sum(ds.map((d,t)=>opt(d,cs[t]))),add(one,q));
  check(cmp(v,worst)<=0,"rational q grid unexpected larger value "+k);
}
// Explicit dual support at q=1: ||u||_infty+||v||_infty=1.
const us=[R(-1,2),R(-1,2)],vs=[R(1,2),R(1,3)];
expect(add(max(abs(us[0]),abs(us[1])),max(abs(vs[0]),abs(vs[1]))),one,"dual norm");
const support=(weights,u,v)=>sum(weights.map((m,i)=>mul(m,max(z,add(u,mul(v,rs[i]))))));
const dualGap=sum(ds.map((d,t)=>support(d,us[t],vs[t])));
expect(dualGap,worst,"dual support gap");
// Explicit old maximizer and matching new decision for that worst-case point.
const xo=[[z,z,one,one],[z,z,z,one]];
const xn=[[z,R(13,36),one,one],[z,z,R(4,9),one]];
for(let t=0;t<2;t++)for(let i=0;i<4;i++){
  check(cmp(xn[t][i],z)>=0&&cmp(xn[t][i],one)<=0,"new decision probability in [0,1]");
  const s=add(us[t],mul(vs[t],rs[i]));
  if(cmp(s,z)>0)expect(xo[t][i],one,"old support maximizing positive port");
  if(cmp(s,z)<0)expect(xo[t][i],z,"old support maximizing negative port");
}
const masses=(weights,dec)=>[
  sum(weights.map((m,i)=>mul(m,dec[i]))),
  sum(weights.map((m,i)=>mul(m,mul(rs[i],dec[i]))))
];
const e=ds.map((d,t)=>{const old=masses(ms[t],xo[t]),newer=masses(n,xn[t]);return [sub(old[0],newer[0]),sub(old[1],newer[1])];});
expect(e[0][0],R(-1,480),"A Q signed error");
expect(e[1][0],R(-1,120),"B Q signed error");
expect(e[0][1],R(1,96),"A P signed error");
expect(e[1][1],z,"B P signed error");
const tvQ=sum(e.map(row=>abs(row[0])));
const tvP=sum(e.map(row=>abs(row[1])));
expect(tvQ,worst,"witness full Q total variation");
expect(tvP,worst,"witness full P total variation");
return {
  status:"PASS_EXACT_BIGINT_RATIONAL",
  model:"time-labelled terminal decision product; NOT a controlled N=4 stopping tree",
  laws_normalized:true,
  strictly_positive_terminal_Q_masses:true,
  likelihood_ratios:rs.map(fmt),
  call_vectors:cs.map(v=>v.map(fmt)),
  two_time_tested_ratios:rs.map(fmt),
  two_time_excess_values:atKnots.map(fmt),
  directed_stage_excesses:[fmt(daVal),fmt(dbVal)],
  directed_two_time_excess:fmt(worst),
  strict_subadditivity_amount:fmt(sub(add(daVal,dbVal),worst)),
  dual_support_gap:fmt(dualGap),
  witness_errors_Q_by_time:e.map(row=>fmt(row[0])),
  witness_errors_P_by_time:e.map(row=>fmt(row[1])),
  witness_tv_Q:fmt(tvQ),
  witness_tv_P:fmt(tvP),
  additional_rational_ratio_crosschecks:80
};
