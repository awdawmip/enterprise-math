"use strict";
// Exact self-contained BRC positive path-weight checks. No floating point.
const absI = x => x < 0n ? -x : x;
function gcd(a,b){a=absI(a); b=absI(b); while(b!==0n){const t=a%b;a=b;b=t;} return a;}
function F(a,b=1n){a=BigInt(a);b=BigInt(b);if(b===0n)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return {n:a/g,d:b/g};}
function plus(a,b){return F(a.n*b.d+b.n*a.d,a.d*b.d);}
function minus(a,b){return F(a.n*b.d-b.n*a.d,a.d*b.d);}
function times(a,b){return F(a.n*b.n,a.d*b.d);}
function over(a,b){return F(a.n*b.d,a.d*b.n);}
function mag(a){return F(absI(a.n),a.d);}
function eq(a,b){return a.n===b.n&&a.d===b.d;}
function le(a,b){return a.n*b.d<=b.n*a.d;}
function show(a){return a.d===1n?String(a.n):String(a.n)+"/"+String(a.d);}
function total(a){return a.reduce(plus,F(0));}
function tv(a,b){if(a.length!==b.length)throw Error("length mismatch");return over(total(a.map((v,i)=>mag(minus(v,b[i])))),F(2));}
function assert(ok,label){if(!ok)throw Error("failed "+label);}
const one=F(1),half=F(1,2),quarter=F(1,4);
function n1Full(law){return [law[0],law[1]];} // D=1 for 0, D=0 for 1
function n1Reduced(){return [half,half];} // P-weighted state-local decision
function n2Full(law){
  const out=[F(0),F(0),F(0)]; // (T=1,D=0),(T=2,D=1),(T=2,D=0)
  for(let i=0;i<2;i++){
    if(i===1){out[0]=plus(out[0],law[i]);continue;}
    for(let j=0;j<2;j++){
      const k=j===0?1:2;out[k]=plus(out[k],times(law[i],law[j]));
    }
  }
  return out;
}
function n2Reduced(){return [half,quarter,quarter];} // c1=1/2, d2=1/2
function run(){
  const p=[half,half],q=[F(3,4),F(1,4)];
  assert(eq(total(p),one)&&eq(total(q),one),"law normalization");
  const n1p=n1Full(p),n1q=n1Full(q),n1bar=n1Reduced();
  const delta1=minus(over(q[0],p[0]),over(q[1],p[1]));
  const n1tv=tv(n1q,n1bar), n1bound=over(delta1,F(4));
  assert(eq(total(n1p),one)&&eq(total(n1q),one),"N1 total masses");
  assert(eq(tv(n1p,n1bar),F(0)),"N1 P exact");
  assert(eq(delta1,one)&&eq(n1tv,quarter)&&eq(n1bound,quarter),"N1 sharpness");
  const n2p=n2Full(p),n2q=n2Full(q),n2bar=n2Reduced();
  assert(eq(total(n2p),one)&&eq(total(n2q),one)&&eq(total(n2bar),one),"N2 normalized");
  assert(eq(tv(n2p,n2bar),F(0)),"N2 P exact");
  // All z_t have one state, hence P transition-to-next-state mass is always 1.
  const lr1=[over(q[0],p[0]),over(q[1],p[1])];
  const lr2=[over(times(q[0],q[0]),times(p[0],p[0])),
             over(times(q[0],q[1]),times(p[0],p[1])),
             over(times(q[1],q[0]),times(p[1],p[0])),
             over(times(q[1],q[1]),times(p[1],p[1]))];
  const d1=minus(lr1[0],lr1[1]),d2=minus(lr2[0],lr2[3]);
  const weighted=over(plus(times(d1,n2p[0]),times(d2,plus(n2p[1],n2p[2]))),F(2));
  const n2tv=tv(n2q,n2bar);
  assert(eq(d1,one)&&eq(d2,F(2)),"N2 fiber oscillations");
  assert(eq(weighted,F(3,4))&&eq(n2tv,F(5,16))&&le(n2tv,weighted),"N2 theorem bound");
  return {
    schema:"EM_R1_N14_LR_OSC_EXACT_RATIONAL_CERT_V1",
    arithmetic:"JavaScript BigInt reduced fractions; no float",
    N1:{
      prefixes:3, P:path(p),Q:path(q),
      full_P:n1p.map(show),full_Q:n1q.map(show),
      reduced_P:n1bar.map(show),reduced_Q:n1bar.map(show),
      LR_oscillation:show(delta1),TV_Q:show(n1tv),
      sharp_bound:show(n1bound),bound_equality:eq(n1tv,n1bound)
    },
    N2:{
      prefixes:7,P:path(p),Q:path(q),
      full_P:n2p.map(show),full_Q:n2q.map(show),
      reduced_P:n2bar.map(show),reduced_Q:n2bar.map(show),
      LR_by_time:{t1:lr1.map(show),t2:lr2.map(show)},
      LR_oscillation_by_time:{t1:show(d1),t2:show(d2)},
      terminal_P_time_weights:["1/2","1/2"],TV_Q:show(n2tv),
      weighted_theorem_bound:show(weighted),bound_verified:le(n2tv,weighted)
    },
    verification_scope:"Two explicit finite IID positive-rational models, horizon one and two; universal theorem proved separately in PROOF.md.",
    status:"PASS_EXACT_BIGINT_RATIONAL"
  };
}
function path(law){return law.map(show);}
if(typeof require==="function" && typeof module==="object" && require.main===module){
  process.stdout.write(JSON.stringify(run(),null,2)+"\n");
}
