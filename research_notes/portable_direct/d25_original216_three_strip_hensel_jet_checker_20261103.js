"use strict";
// Original 216 Hensel/binomial three-strip 2-jet exact checker.
// Run with Node.js: node d25_original216_three_strip_hensel_jet_checker_20261103.js
function runD25JetCertificate(){
  const primes=[7,13,19,37,43,109,181,373];
  const mod=(x,m)=>((x%m)+m)%m;
  const inv=(x,m)=>{let a=mod(x,m),b=m,u=1n,v=0n;while(b){const q=a/b;[a,b]=[b,a-q*b];[u,v]=[v,u-q*v]}if(a!==1n)throw Error("nonunit "+x);return mod(u,m)};
  const binom=(n,k)=>{let x=1n;for(let i=1;i<=k;i++)x=x*BigInt(n-i+1)/BigInt(i);return x};
  const cases=[];
  for(const p of primes){
    if(p%6!==1)throw Error("bad p class");
    const r=(p-1)/6,a=2*r,b=3*r,c=4*r,P=BigInt(p),m=P**3n;
    const i2=inv(2n,m),i3=inv(3n,m),i6=inv(6n,m),i9=inv(9n,m),i216=inv(216n,m);
    const fac=[1n];for(let j=1;j<p;j++)fac.push(mod(fac[j-1]*BigInt(j),m));
    const f=(j)=>fac[j],ifac=(j)=>inv(fac[j],m);
    const src=[0n,0n,0n,0n,0n,0n];
    let poly=[1n,0n,0n],inv216power=1n,W=0n,terms=0;
    for(let k=0;k<p;k++){
      const w=BigInt(6*k+1);
      const original=mod(binom(2*k,k)**2n*binom(3*k,k)*inv216power,m);
      const fromJet=mod(poly[0]+P*poly[1]+P*P*poly[2],m);
      if(original!==fromJet)throw Error("original mismatch p="+p+" k="+k);
      W=mod(W+w*original,m);terms++;
      if(k<=a){
        const ck=mod(BigInt(k%2===0?1:-1)*binom(b,k)*binom(a,k)*binom(c,k)*inv(2n**BigInt(k),m),m);
        let H=0n,K=0n;
        for(let j=0;j<k;j++){
          const x=inv(BigInt(j-b),m),y=inv(BigInt(j-a),m),z=inv(BigInt(j-c),m);
          H=mod(H+x*i2+y*i3+2n*z*i3,m);
          K=mod(K+x*x*i2*i2+y*y*i9+4n*z*z*i9,m);
        }
        const d1=mod(ck*H,m),d2=mod(ck*(H*H-K)*i2,m);
        if(poly[0]!==ck||poly[1]!==d1||poly[2]!==d2)throw Error("low factor mismatch p="+p+" k="+k);
        src[0]=mod(src[0]+w*ck,m);src[1]=mod(src[1]+w*d1,m);src[2]=mod(src[2]+w*d2,m);
      }else if(k<=b){
        const uk=mod(f(a)*f(k-a-1)*f(b)*f(c)*i3*ifac(b-k)*ifac(c-k)*ifac(k)**3n*inv(2n**BigInt(k),m),m);
        let H=0n;
        for(let j=0;j<k;j++){
          if(j!==a)H=mod(H+i3*inv(BigInt(j-a),m),m);
          H=mod(H+i2*inv(BigInt(j-b),m)+2n*i3*inv(BigInt(j-c),m),m);
        }
        if(poly[0]!==0n||poly[1]!==uk||poly[2]!==mod(uk*H,m))throw Error("middle factor mismatch p="+p+" k="+k);
        src[3]=mod(src[3]+w*uk,m);src[4]=mod(src[4]+w*uk*H,m);
      }else if(k<=c){
        const vk=mod(BigInt((b+k)%2===0?1:-1)*f(a)*f(b)*f(c)*f(k-a-1)*f(k-b-1)*i6*ifac(c-k)*ifac(k)**3n*inv(2n**BigInt(k),m),m);
        if(poly[0]!==0n||poly[1]!==0n||poly[2]!==vk)throw Error("upper factor mismatch p="+p+" k="+k);
        src[5]=mod(src[5]+w*vk,m);
      }else if(poly.some(x=>x!==0n))throw Error("triple terminal not zero p="+p+" k="+k);
      if(k===p-1)break;
      const x=BigInt(k-b),y=BigInt(k-a),z=BigInt(k-c),den=inv(2n*BigInt(k+1)**3n,m);
      const q0=mod(x*y*z,m),q1=mod(y*z*i2+x*z*i3+2n*x*y*i3,m),q2=mod(z*i6+y*i3+2n*x*i9,m);
      poly=[mod(poly[0]*q0*den,m),mod((poly[1]*q0+poly[0]*q1)*den,m),mod((poly[2]*q0+poly[1]*q1+poly[0]*q2)*den,m)];
      inv216power=mod(inv216power*i216,m);
    }
    const S0=src[0],S1=mod(src[1]+src[3],m),S2=mod(src[2]+src[4]+src[5],m);
    if(mod(S0+P*S1+P*P*S2,m)!==W)throw Error("sum mismatch p="+p);
    const target=p%24===13||p%24===19;
    const hW=mod(W-P*P*src[5],m);
    if(target && mod(hW-P,P*P)!==0n)throw Error("half first digit inconsistent");
    cases.push({p,r,checked_original_terms:terms,band_lengths:[a+1,b-a,c-b,p-1-c],
      W0_mod_p3:String(S0),W1_mod_p3:String(S1),W2_mod_p:String(S2%P),
      low_second_mod_p:String(src[2]%P),middle_second_mod_p:String(src[4]%P),upper_second_mod_p:String(src[5]%P),
      original_W_mod_p3:String(W),half_W_mod_p3:String(hW),
      half_second_digit_target:target?String(mod((hW-P)/(P*P),P)):"not_target",
      target_residue:target?String(mod(W-P,m)):"not_target"});
  }
  return {schema:"D25_ORIGINAL216_THREE_STRIP_BINOMIAL_HENSEL_2JET_CERTIFICATE_V1",arithmetic:"BigInt exact modular p^3; p-unit inverse; independent original binomial coefficient direct computation and three-strip factored Taylor formulas",cases};
}
console.log(JSON.stringify(runD25JetCertificate(), null, 2));
