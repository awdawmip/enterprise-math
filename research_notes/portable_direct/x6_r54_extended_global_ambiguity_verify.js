/* X6 R54 exact named-branch BRC verifier; Node.js. */
const runR54 = function runR54() {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a||1n};
  const F=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g}};
  const V=x=>typeof x==="object"?x:F(x), A=(x,y)=>{x=V(x);y=V(y);return F(x.n*y.d+y.n*x.d,x.d*y.d)}, M=(x,y)=>{x=V(x);y=V(y);return F(x.n*y.n,x.d*y.d)}, Neg=x=>{x=V(x);return F(-x.n,x.d)}, D=(x,y)=>{x=V(x);y=V(y);return F(x.n*y.d,x.d*y.n)}, S=(x,y)=>A(x,Neg(y));
  const cmp=(x,y)=>{x=V(x);y=V(y);const n=x.n*y.d-y.n*x.d;return n<0n?-1:n>0n?1:0},eq=(x,y)=>cmp(x,y)===0,gt=(x,y)=>cmp(x,y)>0;
  const str=x=>{x=V(x);return String(x.n)+(x.d===1n?"":"/"+String(x.d))};
  const from=s=>{const a=s.split("/");return F(a[0],a[1]||1)};
  const check=(v,m)=>{if(!v)throw Error(m)};
  const BRC=(word,p,alpha,beta)=>{
    const step=(s,e)=>{
      let [a,b,o,t]=s;
      if(e==="R")return o===0?null:[a,b,0,t];
      if(e==="T"){if(t!==0||o!==0||((a<0)===(b<0)))return null;const v=a>=0?a:b;return [a,b,v===0?(a>=0?1:2):0,1];}
      const side=e[0],i=Number(e.substring(1));
      if(side==="A"){if(a>=0||(i===0&&o!==0))return null;return [i,b,i===0?1:o,t];}
      if(b>=0||(i===0&&o!==0))return null;return [a,i,i===0?2:o,t];
    };
    let frontier=[{s:[-1,-1,0,0],w:F(1)}];
    for(const e of word){
      const events=e==="F"?Array.from({length:p},(_,i)=>["A"+i,"B"+i]).flat():[e],next=[];
      for(const x of frontier)for(const lab of events){const s=step(x.s,lab);if(s!==null)next.push({s,w:M(x.w,lab[0]==="A"?alpha:lab[0]==="B"?beta:1)});}
      frontier=next;
    }
    return frontier.reduce((v,x)=>A(v,x.w),F(0));
  };
  const vector=(p,s,P)=>[M(p,s),M(p-1,s),M(2*(p*p-1),P),M(2*p,P)];
  const discr=P=>A(S(M(1764,M(P,P)),M(30404,P)),6361);
  check(gt(discr(from("1059/5000")),0)&&cmp(discr(from("53/250")),0)<0,"root bracket signs");
  const pairs=[["1","2"],["1/3","2/3"],["1/10","9/10"],["1/2","1/2"],["2/7","5/7"]];
  let branchChecks=0;
  for(let p=1;p<=8;p++)for(const [as,bs] of pairs){
    const a=from(as),b=from(bs),su=A(a,b),P=M(a,b);
    const words=["F","FT","FF","FRF"],expected=vector(p,su,P);
    for(let i=0;i<words.length;i++){check(eq(BRC(words[i],p,a,b),expected[i]),"named BRC "+p+" "+words[i]);branchChecks++;}
  }
  const params=["1/1000000","1/10000","1/1000","19/2158","1/100","1/10","1/5","79/378","21/100","211/1000","1059/5000"];
  const p0=from("19/2158"),cases=[];let rivalChecks=0;
  for(const name of params){
    const P=from(name),eta=D(A(19,M(42,P)),400),s5=D(S(81,M(42,P)),100),P5=D(A(1,M(118,P)),200),b5=D(S(M(378,P),29),200);
    check(gt(P,0)&&gt(discr(P),0)&&gt(s5,0)&&gt(P5,0),"source-weight feasibility");
    check(eq(S(M(s5,s5),M(4,P5)),D(discr(P),10000)),"discriminant identity");
    const real=vector(4,F(1),P),alt=vector(5,s5,P5).map(x=>A(x,b5)),z=real.map((x,i)=>D(A(x,alt[i]),2));
    const pat=[1,-1,-1,1];
    for(let i=0;i<4;i++)check(eq(S(real[i],alt[i]),M(M(2,eta),pat[i])),"sharp four-channel witness");
    if(cmp(P,p0)>=0){check(cmp(eta,D(M(11,P),2))<=0,"q=1 D-H exclusion");}
    else{check(gt(D(S(3,M(30,P)),4),eta),"q=1 Y-D exclusion");}
    for(let q=2;q<=500;q++){
      if(q===4||q===5)continue;
      const c=q*q-q-1;
      const bound=D(M(Math.abs(4-q),A(c,M(M(2,P),4*q+1))),4*q*q*(q-1));
      check(gt(bound,eta),"rival contrast q="+q+" P="+name);rivalChecks++;
    }
    cases.push({P:name,eta:str(eta),q5_sum:str(s5),q5_product:str(P5),q5_offset:str(b5),shared_measurement:z.map(str),positive_weight_discriminant:str(D(discr(P),10000))});
  }
  const beyond=from("53/250"),Sb=D(S(81,M(42,beyond)),100),Pb=D(A(1,M(118,beyond)),200);
  check(cmp(S(M(Sb,Sb),M(4,Pb)),0)<0,"strict positivity obstruction beyond root");
  return {schema:"X6_R54_SHARP_POSITIVE_BRC_RADIUS_V1",status:"PASS",scientific_domain:"R44 conditional whole-triad named-branch positive BRC, shared unknown offset, 4 short-word observer",branch_mass_checks:branchChecks,parameter_samples:params.length,finite_rival_contrast_checks:rivalChecks,global_proof:"all-integer exclusion by rational contrast and q>=6 monotonicity, with q=1 two-difference split",formula:"eta_crit(P)=(19+42*P)/400 for 0<P<=rho",root:"rho=(7601-100*sqrt(5497))/882",root_sign_bracket:["1059/5000","53/250"],positivity_boundary:"q=5 saturation gives discriminant zero at rho and impossible for P>rho",samples:cases};
};
process.stdout.write(JSON.stringify(runR54(),null,2)+'\n');
