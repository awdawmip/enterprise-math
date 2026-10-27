#!/usr/bin/env node
"use strict";
/* PREFIX-286: provenance-preserving C4 BRC two-port instrument.
   Each (sigma,j) has b0=i^p a_j/2, b1=sigma a_{j-1}/2,
   all 4 ordered pairs are evaluated exactly; no native X6 legality inferred. */
const result=(function verifyPrefix286() {
  "use strict";
  const z=(r=0n,i=0n)=>({r,i}),sum=(a,b)=>z(a.r+b.r,a.i+b.i),
    neg=a=>z(-a.r,-a.i),mul=(a,b)=>z(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r),
    conj=a=>z(a.r,-a.i),norm=a=>a.r*a.r+a.i*a.i,
    eq=(a,b)=>a.r===b.r&&a.i===b.i;
  const P=[z(1n),z(0n,1n),z(-1n),z(0n,-1n)],ZERO=z();
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a||1n;};
  const F=(n,d)=>{if(d<0n){n=-n;d=-d}const g=gcd(n,d);return `${n/g}/${d/g}`;};
  const pairMass=branches=>{
    let re=0n,im=0n;
    for(const a of branches)for(const b of branches){const t=mul(a,conj(b));re+=t.r;im+=t.i;}
    if(im!==0n||re<0n)throw Error("BRC positivity/imaginary failure");
    return re;
  };
  const C=(a,d)=>{let v=ZERO;for(let j=0;j+d<a.length;j++)v=sum(v,mul(a[j],conj(a[j+d])));return v;};
  const Z=a=>a.reduce((s,x)=>s+norm(x),0n);
  const signature=a=>{const n=Z(a),c1=C(a,1),c2=C(a,2);return [F(c1.r,n),F(c1.i,n),F(c2.r,n),F(c2.i,n),F(norm(a[0]),n)].join("|");};
  const relative=a=>[F(a[1].r,a[0].r),F(a[1].i,a[0].r),F(a[2].r,a[0].r),F(a[2].i,a[0].r)].join("|");
  const coin=(a,p)=>{
    const phase=P[p],n=Z(a),output=[];
    for(const sign of [1n,-1n]){
      const port=[];
      for(let j=0;j<4;j++){
        const current=j<3?a[j]:ZERO,prior=j>0&&j-1<3?a[j-1]:ZERO;
        port.push(pairMass([mul(phase,current),sign===1n?prior:neg(prior)]));
      }
      output.push(port);
    }
    if(output.flat().reduce((s,x)=>s+x,0n)!==4n*n)throw Error("instrument completeness failed");
    if(output[0][1]!==pairMass([a[0],mul(phase,a[1])]))throw Error("BRC click is not Jp/2");
    const c1=C(a,1),right=2n*n+2n*mul(conj(phase),c1).r;
    if(output[0].reduce((s,x)=>s+x,0n)!==right)throw Error("port norm/autocorrelation failed");
    return {out:output,Z:n};
  };
  const families=new Map();let packets=0,reads=0,completions=0;
  for(let m0=1n;m0<=4n;m0++)for(let m1=1n;m1<=4n;m1++)for(let m2=1n;m2<=4n;m2++)
    for(let k1=0;k1<4;k1++)for(let k2=0;k2<4;k2++){
      const a=[z(m0),mul(z(m1),P[k1]),mul(z(m2),P[k2])];
      const byPhase=[];
      for(let p=0;p<4;p++){byPhase.push(coin(a,p));reads+=8;completions++;}
      const key=signature(a),bucket=families.get(key)||[];
      bucket.push({a,byPhase,relative:relative(a),m0,m1});
      families.set(key,bucket);packets++;
    }
  const equalOutputs=(x,y)=>x.out.flat().every((v,j)=>v*y.Z===y.out.flat()[j]*x.Z);
  let singular=0,ambiguous=0,exactGapChecks=0,phase0NoGo=0,phase1NoGo=0;
  for(const bucket of families.values()){
    const uniq=[...new Map(bucket.map(x=>[x.relative,x])).values()];
    if(uniq.length>2)throw Error("More than two normalized solutions");
    const first=uniq[0],singularHere=norm(first.a[0])===norm(first.a[2]);
    if(singularHere)singular++;
    if(uniq.length===2){
      if(!singularHere)throw Error("Nonsingular duplicate signature");
      ambiguous++;
      const second=uniq[1];
      const t=P.findIndex(w=>eq(mul(z(first.m0),w),first.a[2]));
      if(t<0)throw Error("t not in C4");
      const p=t===0?1:0;
      const U=first.byPhase[p],V=second.byPhase[p];
      const L=U.out[0][1]*V.Z-V.out[0][1]*U.Z,absolute=L<0n?-L:L;
      if(absolute===0n)throw Error("selected click not separating");
      const factor=(t===0||t===2)?1n:2n;
      if(absolute*factor!==4n*V.Z*first.m0*first.m1)throw Error("Exact half-J gap mismatch");
      exactGapChecks++;
      if(equalOutputs(first.byPhase[0],second.byPhase[0]))phase0NoGo++;
      if(equalOutputs(first.byPhase[1],second.byPhase[1]))phase1NoGo++;
    }
  }
  const A=coin([z(1n),P[1],z(1n)],1),B=coin([z(1n),P[3],z(1n)],1);
  if(A.out[0][1]!==0n||B.out[0][1]!==4n||A.Z!==3n||B.Z!==3n)throw Error("Concrete example mismatch");
  return {status:"PREFIX286_BRC_TWO_PORT_INSTRUMENT_EXACT_PASS",
    occupied_source_packets:packets,c4_settings_per_packet:4,output_ports:2,source_bins_per_port:4,
    exact_ordered_source_pair_readouts:reads,exact_global_mass_checks:completions,
    distinct_original_signatures:families.size,singular_signatures:singular,
    ambiguous_signatures:ambiguous,adaptive_full_instrument_distinctions:exactGapChecks,
    fixed_p0_full_output_indistinguishable_pairs:phase0NoGo,
    fixed_p1_full_output_indistinguishable_pairs:phase1NoGo,
    example:{first:"(1,i,1)",second:"(1,-i,1)",phase:"i",
      raw_port_plus_bin1_mass:[A.out[0][1].toString(),B.out[0][1].toString()],
      normalized_port_plus_bin1_probability:["0","1/3"],total_probability:"1"},
    arithmetic:"BigInt Gaussian integers; explicit full ordered-pair C4 BRC",native_status:"formal_model_only"};
})();
console.log(JSON.stringify(result,null,2));
