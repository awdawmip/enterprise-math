"use strict";
// PREFIX291 — exact provenance-labelled ordered BRC over candidate Q(i,sqrt(3)).
// Every bin coefficient is numerator in Z[i,sqrt(3)] / 4. No floats or pi.
const C=(a=0n,b=0n,c=0n,d=0n)=>[BigInt(a),BigInt(b),BigInt(c),BigInt(d)];
const add=(a,b)=>a.map((x,j)=>x+b[j]);
const neg=a=>a.map(x=>-x);
const sub=(a,b)=>add(a,neg(b));
const times=(a,b)=>[
 a[0]*b[0]+3n*a[1]*b[1]-a[2]*b[2]-3n*a[3]*b[3],
 a[0]*b[1]+a[1]*b[0]-a[2]*b[3]-a[3]*b[2],
 a[0]*b[2]+3n*a[1]*b[3]+a[2]*b[0]+3n*a[3]*b[1],
 a[0]*b[3]+a[1]*b[2]+a[2]*b[1]+a[3]*b[0]
];
const conj=a=>[a[0],a[1],-a[2],-a[3]];
const muln=(a,k)=>a.map(x=>x*BigInt(k));
const eq=(a,b)=>a.every((x,j)=>x===b[j]);
const ZERO=C(),ONE=C(1),I=C(0,0,1),R=C(0,1),TWO=C(2);
const phases=[ONE,I,neg(ONE),neg(I)];
function bins(q){
 const q2=times(q,q), A=C(1,1), B=C(1,-1);
 const leg=(src,label,coef)=>({src,label,coef});
 return [
  [leg(0,"E0.s0",TWO),leg(1,"E0.s1",muln(q,2))],
  [leg(1,"E1.s1",neg(TWO)),leg(2,"E1.s2",muln(q,2))],
  [leg(0,"D0.C0.s0",B),leg(1,"D0.C0.s1",neg(times(q,B))),leg(0,"D0.C1.s0",A),leg(2,"D0.C1.s2",times(q2,A))],
  [leg(0,"D1.C0.s0",A),leg(1,"D1.C0.s1",neg(times(q,A))),leg(0,"D1.C1.s0",B),leg(2,"D1.C1.s2",times(q2,B))],
  [leg(0,"D2.C2.s0",TWO),leg(2,"D2.C2.s2",neg(muln(q2,2)))]
 ];
}
function amplitude(legs,a){
 let s=ZERO;
 for(const L of legs)s=add(s,times(L.coef,a[L.src]));
 return s;
}
function ordered(legs,a,b){
 let v=ZERO,n=0;
 for(const u of legs)for(const w of legs){
   n++;
   // u and w retain the original source and complement-leg provenance.
   v=add(v,times(times(u.coef,a[u.src]),conj(times(w.coef,b[w.src]))));
 }
 return {v,n};
}
function inner(a,b){
 let v=ZERO;
 for(let j=0;j<3;j++)v=add(v,times(a[j],conj(b[j])));
 return v;
}
function verify(flag,label){if(!flag)throw Error("EXACT_BRC_FAIL:"+label)}
function run(){
 let cases=0,binsRead=0,pairs=0,norm=0,cross=0,decode=0,basis=0;
 const choices=[ZERO,ONE,neg(ONE),I,neg(I),add(ONE,I)];
 for(const q of phases){
  const B=bins(q), q2=times(q,q);
  for(let j=0;j<3;j++)for(let k=0;k<3;k++){
    const u=[ZERO,ZERO,ZERO],w=[ZERO,ZERO,ZERO];u[j]=ONE;w[k]=ONE;
    let total=ZERO;
    for(const L of B)total=add(total,ordered(L,u,w).v);
    verify(eq(total,muln(inner(u,w),16)),"basis/"+j+"/"+k);
    basis++;
  }
  for(const a0 of choices)for(const a1 of choices)for(const a2 of choices){
   const a=[a0,a1,a2],b=[a2,a0,a1];
   let mn=ZERO,cr=ZERO;
   for(const L of B){
    const x=ordered(L,a,a),y=ordered(L,a,b);
    verify(eq(x.v,times(amplitude(L,a),conj(amplitude(L,a)))),"bin_mass");
    verify(x.v[2]===0n&&x.v[3]===0n,"nonnegative_mass_real_type");
    mn=add(mn,x.v);cr=add(cr,y.v);
    binsRead++;pairs+=x.n+y.n;
   }
   verify(eq(mn,muln(inner(a,a),16)),"mass_conservation");
   verify(eq(cr,muln(inner(a,b),16)),"cross_isometry");
   const X=sub(a0,times(q,a1));
   const Y=add(a0,times(q2,a2));
   const Z=sub(a0,times(q2,a2));
   const d0=amplitude(B[2],a),d1=amplitude(B[3],a),d2=amplitude(B[4],a);
   verify(eq(add(d0,d1),muln(add(X,Y),2)),"decode_sum");
   verify(eq(sub(d1,d0),muln(times(R,sub(X,Y)),2)),"decode_difference");
   verify(eq(d2,muln(Z,2)),"decode_third");
   cases++;norm++;cross++;decode++;
  }
 }
 const q=I,B=bins(q),a=[ONE,I,ONE],b=[ONE,neg(I),ONE];
 const E=a1=>add(ordered(B[0],a1,a1).v,ordered(B[1],a1,a1).v);
 const ea=E(a),eb=E(b),za=inner(a,a),zb=inner(b,b);
 verify(eq(ea,ZERO)&&eq(eb,C(32))&&eq(za,C(3))&&eq(zb,C(3)),"witness");
 return {
   schema:"EM_PREFIX291_QISQRT3_ORDERED_BRC_JS_V1",
   status:"PASS",source_packets:216,phase_cases:cases,
   five_bin_ordered_BRC_mass_checks:binsRead,
   ordered_source_pair_terms_mass_plus_cross:pairs,
   norm_equalities:norm,cross_packet_equalities:cross,
   inverse_codeword_equalities:decode,universal_basis_gram_equalities:basis,
   scalar_domain:"CANDIDATE_Q(i,sqrt3),NOT_NATIVE_ADMITTED",
   q_i_witness:{a:"0",b:"2/3"},
   native_Hn_detector:"NOT_EXECUTED",project_admission:"UNREVIEWED_NOT_ADMITTED"
 };
}
if(typeof require!=="undefined" && typeof module!=="undefined" && require.main===module)
  console.log(JSON.stringify(run(),null,2));
