/* X6 R55 named BRC exact-rational author verifier. Run with Node.js. */
const runR55=function runR55(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a||1n};
 const F=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero divisor");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g}};
 const V=x=>(typeof x==="object"&&x!==null&&"n" in x)?x:F(x);
 const add=(x,y)=>{x=V(x);y=V(y);return F(x.n*y.d+y.n*x.d,x.d*y.d)};
 const neg=x=>{x=V(x);return F(-x.n,x.d)};
 const sub=(x,y)=>add(x,neg(y));
 const mul=(x,y)=>{x=V(x);y=V(y);return F(x.n*y.n,x.d*y.d)};
 const div=(x,y)=>{x=V(x);y=V(y);return F(x.n*y.d,x.d*y.n)};
 const cmp=(x,y)=>{x=V(x);y=V(y);const c=x.n*y.d-y.n*x.d;return c<0n?-1:c>0n?1:0};
 const str=x=>{x=V(x);return String(x.n)+(x.d===1n?"":"/"+String(x.d))};
 const check=(pred,msg)=>{if(!pred)throw Error(msg)};
 const polynomial=(word,p)=>{
   const step=(s,e)=>{
    const [a,b,o,t]=s;
    if(e==="R")return o===0?null:[a,b,0,t];
    if(e==="T"){
      if(t!==0||o!==0||((a<0)===(b<0)))return null;
      const v=a>=0?a:b;
      return [a,b,v===0?(a>=0?1:2):0,1];
    }
    const side=e[0], i=Number(e.substring(1));
    if(side==="A"){if(a>=0||(i===0&&o!==0))return null;return [i,b,i===0?1:o,t]}
    if(b>=0||(i===0&&o!==0))return null;
    return [a,i,i===0?2:o,t];
   };
   let frontier=[{s:[-1,-1,0,0],a:0,b:0}];
   for(const e of word){
    const events=e==="F"?Array.from({length:p},(_,i)=>["A"+i,"B"+i]).flat():[e],next=[];
    for(const f of frontier)for(const lab of events){
      const n=step(f.s,lab);
      if(n)next.push({s:n,a:f.a+(lab[0]==="A"?1:0),b:f.b+(lab[0]==="B"?1:0)});
    }
    frontier=next;
   }
   const map={};
   for(const f of frontier){const k=f.a+","+f.b;map[k]=(map[k]||0)+1;}
   return map;
 };
 const eqMap=(x,y)=>JSON.stringify(x)===JSON.stringify(y);
 let namedChecks=0;
 for(let p=1;p<=8;p++){
   const expected=[
      {"1,0":p,"0,1":p},
      p===1?{}:{"1,0":p-1,"0,1":p-1},
      p===1?{}:{"1,1":2*(p*p-1)},
      {"1,1":2*p}
   ];
   for(let i=0;i<4;i++){
     const a=polynomial(["F","FT","FF","FRF"][i],p);
     check(Object.keys(a).length===Object.keys(expected[i]).length && Object.entries(expected[i]).every(([k,v])=>a[k]===v),"named BRC polynomial p="+p+" i="+i+" actual "+JSON.stringify(a));
     namedChecks++;
   }
 }
 const roots={
   rho_below:F(21181,100000),rho_above:F(21183,100000),
   sigma_below:F(21467,100000),sigma_above:F(21469,100000)
 };
 const discR=x=>add(sub(mul(1764,mul(x,x)),mul(30404,x)),6361);
 const discS=x=>add(sub(mul(441,mul(x,x)),mul(6821,x)),1444);
 check(cmp(discR(roots.rho_below),0)>0&&cmp(discR(roots.rho_above),0)<0,"rho exact bracket");
 check(cmp(discS(roots.sigma_below),0)>0&&cmp(discS(roots.sigma_above),0)<0,"sigma exact bracket");
 const I=[F(7,25),F(57,200),F(29,100),F(147,500)];
 const II=[F(707,1000),F(71,100),F(18,25),F(729,1000)];
 let samples=[];
 for(const [zone,arr] of [["I",I],["II",II]]){
  for(const u of arr){
   const s=zone==="I"?sub(1,u):u;
   const P=zone==="I"?div(add(mul(5,mul(u,u)),3),16):mul(F(19,44),mul(s,s));
   const t=div(mul(s,s),4);
   check(cmp(P,roots.rho_above)>0&&cmp(P,F(23,100))<0,"parameter sample domain");
   if(zone==="I")check(cmp(P,roots.sigma_below)<0,"I below sigma bracket");
   if(zone==="II")check(cmp(P,roots.sigma_above)>0,"II above sigma bracket");
   const real=[mul(4,1),F(3),mul(30,P),mul(8,P)];
   const rival=[mul(5,s),mul(4,s),mul(48,t),mul(10,t)];
   const residual=real.map((x,i)=>sub(x,rival[i]));
   const range=sub(residual.reduce((a,b)=>cmp(a,b)>0?a:b),residual.reduce((a,b)=>cmp(a,b)<0?a:b));
   const eta=div(range,4);
   const expected=zone==="I"?div(sub(1,s),4):add(sub(s,F(3,4)),mul(F(21,38),P));
   check(cmp(eta,expected)===0,"exact candidate Chebyshev radius");
   check(cmp(eta,F(107,1000))<0,"uniform upper radius");
   check(cmp(mul(4,t),mul(s,s))===0,"positive equal-source boundary");
   if(zone==="I"){
    check(cmp(residual[0],residual[3])===0,"I upper pair");
    check(cmp(residual[1],residual[2])<=0&&cmp(residual[2],residual[0])<=0,"I ordering");
   }else{
    check(cmp(residual[2],residual[3])===0,"II upper pair");
    check(cmp(residual[1],residual[0])<=0&&cmp(residual[0],residual[2])<=0,"II ordering");
   }
   for(const q of [2,3,6,7,8,20,100]){
     const cq=q*q-q-1;
     const lower=div(mul(Math.abs(q-4),add(cq,mul(mul(2,P),4*q+1))),4*q*q*(q-1));
     check(cmp(lower,eta)>0,"other-port exclusion q="+q);
   }
   samples.push({regime:zone,P:str(P),rival_sum:str(s),rival_product:str(t),eta_critical:str(eta),residual_without_bias:residual.map(str)});
  }
 }
 const result={
   schema:"X6_R55_POST_RHO_GLOBAL_PORT_AMBIGUITY_V1",
   status:"PASS",
   theorem_scope:"R44 conditional named whole-triad positive-BRC four-word observer, true p=4, S=1, rho<=P<=23/100; shared unknown bias and per-channel absolute error",
   rho:"(7601-100*sqrt(5497))/882",
   sigma:"(6821-95*sqrt(4873))/882",
   upper_P:"23/100",
   radius_regime_I:"sqrt((16P-3)/5)/4 for rho<=P<=sigma",
   radius_regime_II:"2*sqrt(11P/19)-3/4+21P/38 for sigma<=P<=23/100",
   named_branch_polynomial_checks:namedChecks,
   rational_parameter_witnesses:samples.length,
   exact_root_sign_brackets:{rho:["21181/100000","21183/100000"],sigma:["21467/100000","21469/100000"]},
   finite_rival_bounds_checked_per_sample:[2,3,6,7,8,20,100],
   symbolic_coverage:"Proof in accompanying markdown handles all real P in closed interval, all positive competing weights and every integer q !=4; this finite test does not replace the proof",
   independent_review:"NOT_REVIEWED",
   native_p000_R_T_admission:"UNPROVED_CONDITIONAL_GRAMMAR"
 };
 return result;
};
process.stdout.write(JSON.stringify(runR55(),null,2)+'\n');
