"use strict";
// BRC N=4 fixed-noise fixed-D endpoint checker; exact BigInt rational arithmetic.
const gcd=(a,b)=>b===0n?(a<0n?-a:a):gcd(b,a%b);
function q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];}
const Z=q(0),O=q(1),H=q(1,2),two=q(2),ten=q(10),twenty=q(20);
const A=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const S=(a,b)=>q(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
const M=(a,b)=>q(a[0]*b[0],a[1]*b[1]);
const V=(a,b)=>q(a[0]*b[1],a[1]*b[0]);
const C=(a,b)=>a[0]*b[1]-b[0]*a[1];
const E=(a,b)=>C(a,b)===0n;
const B=a=>a[0]<0n?q(-a[0],a[1]):a;
const mx=(a,b)=>C(a,b)>=0n?a:b;
const mn=(a,b)=>C(a,b)<=0n?a:b;
const sum=a=>a.reduce(A,Z);
const tv=(a,b)=>V(sum(a.map((v,i)=>B(S(v,b[i])))),two);
const atoms=(u,d0,d1)=>[S(O,u),V(M(u,d0),two),V(M(u,S(O,d0)),two),V(M(u,d1),two),V(M(u,S(O,d1)),two)];
const terminal=(u,v,d00,d01,d10,d11)=>[atoms(u,d00,d01),atoms(v,d10,d11)];
const dist= f=>tv(f[0],f[1]);
const source={AU:[q(1,6),[q(9,10),q(11,10)]],AV:[q(1,3),[q(1,4),q(1,4)]],BU:[q(1,4),[q(1,5),q(9,5)]],BV:[q(1,4),[q(2),q(2)]]};
const leaves={P:[],Q:[]};
for(const [s,[w,rr]] of Object.entries(source))for(let j=0;j<2;j++)for(let k=0;k<2;k++){leaves.P.push({s,j,k,p:V(M(w,rr[j]),q(4))});leaves.Q.push({s,j,k,p:V(w,q(4))});}
for(const L of ["P","Q"]){if(leaves[L].length!==16||!E(sum(leaves[L].map(x=>x.p)),O)||leaves[L].some(x=>C(x.p,Z)<=0n))throw Error("source leaves");}
function direct(eps,f){const out={};for(const L of ["P","Q"]){let ar=[];for(let z=0;z<2;z++)for(let y=0;y<5;y++){let p=Z;for(let j=0;j<2;j++){const prior=sum(leaves[L].filter(x=>x.s==="BU"&&x.j===j).map(x=>x.p));p=A(p,M(M(prior,j===z?S(O,eps):eps),f[j][y]));}ar.push(p);}out[L]=ar;}return tv(out.P,out.Q);}
function expression(eps,f){const t=S(O,M(two,eps));return V(sum(f[0].map((a,i)=>mx(B(S(a,f[1][i])),M(t,A(a,f[1][i]))))),twenty);}
function bounds(eps,f){const t=S(O,M(two,eps)),d=dist(f);return [V(mx(d,t),ten),V(A(d,M(t,S(O,d))),ten)];}
const upper=f=>f[0].every((a,i)=>E(a,f[1][i])||E(a,Z)||E(f[1][i],Z));
function lower(eps,f){const t=S(O,M(two,eps)),d=dist(f);return f[0].every((a,i)=>{const x=B(S(a,f[1][i])),y=M(t,A(a,f[1][i]));return C(d,t)>0?C(x,y)>=0n:C(d,t)<0?C(x,y)<=0n:E(x,y);});}
function run(){const values=[Z,H,O],levels=[Z,q(1,8),q(1,4),q(3,8),H];let tests=0;
 for(const u of values)for(const v of values)for(const d00 of values)for(const d01 of values)for(const d10 of values)for(const d11 of values){
  const f=terminal(u,v,d00,d01,d10,d11),d=dist(f);
  for(const eps of levels){const actual=direct(eps,f),want=expression(eps,f),[lo,hi]=bounds(eps,f);
   if(!E(actual,want)||C(actual,lo)<0n||C(actual,hi)>0n)throw Error("TV formula/bounds");
   if(C(eps,Z)>0n&&C(eps,H)<0n&&C(d,Z)>0n&&C(d,O)<0n&&E(actual,hi)!==upper(f))throw Error("upper iff");
   if(E(actual,lo)!==lower(eps,f))throw Error("lower iff");
   tests++;}}
 let witnesses=[];
 for(const [d,n] of [[q(1,4),4],[H,3],[q(3,4),5]]){
  const f=C(d,H)<0?terminal(M(two,d),M(two,d),O,O,O,Z):E(d,H)?terminal(O,O,O,O,O,Z):terminal(d,d,O,O,Z,Z);
  const count=f[0].filter((a,i)=>C(A(a,f[1][i]),Z)>0n).length;
  if(!E(dist(f),d)||count!==n||!upper(f)||!E(expression(q(1,4),f),bounds(q(1,4),f)[1]))throw Error("witness");
  witnesses.push(d[0]+"/"+d[1]+":"+n);}
 return "PASS_EXACT_BIGINT_BRC_N4_20261030 grid="+tests+" source_leaves=16 S2_support_D="+witnesses.join(",");
}
if(typeof module!=="undefined" && require.main===module)console.log(run());