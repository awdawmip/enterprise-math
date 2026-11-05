/* D25 signed fourth-digit / Clausen cubic source bridge; BigInt exact modular arithmetic.
 * Author-side witness; run: node d25_fourth_digit_clausen_cubic_source_20261105.js
 * Frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3.
 */
"use strict";
const mod=(a,m)=>(a%m+m)%m;
function inverse(a,m){
  let b=m,x=1n,y=0n;a=mod(a,m);
  while(b){let q=a/b;[a,b]=[b,a-q*b];[x,y]=[y,x-q*y];}
  if(a!==1n)throw Error("nonunit denominator");
  return mod(x,m);
}
function audit(p){
  const n=(p-1)/6,M=BigInt(p)**4n,P=BigInt(p),half=inverse(2n,M);
  const beta=[half,inverse(3n,M),mod(2n*inverse(3n,M),M)];
  const cut=[3*n,2*n,4*n], inv6=inverse(6n,M),inv8=inverse(8n,M),inv16=inverse(16n,M);
  let d=1n,h1=0n,h2=0n,h3=0n,r1=0n,r2=0n,r3=0n;
  let S=0n,A=0n,B=0n,C=0n,D=0n,E=0n,T=[0n,0n,0n,0n];
  let alpha=0n,bbeta=0n,gamma=0n, origTerm=1n,W=0n,gTerm=1n,g=0n,J=0n;
  for(let k=0;k<p;k++){
    const weight=BigInt(6*k+1),v=cut.filter(t=>k>t).length,base=mod(weight*d,M);
    const e2=mod((h1*h1-h2)*half,M);
    const e3=mod((h1*h1*h1-3n*h1*h2+2n*h3)*inv6,M);
    if(v===0){
      S=mod(S+base,M);A=mod(A+base*h1,M);C=mod(C+base*e2,M);T[0]=mod(T[0]+base*e3,M);
      alpha=mod(alpha+base*mod(3n*half*r1,M),M);
      bbeta=mod(bbeta+base*mod((9n*r1*r1+5n*r2)*inv8,M),M);
      gamma=mod(gamma+base*mod((9n*r1*r1*r1+15n*r1*r2+6n*r3)*inv16,M),M);
    }else if(v===1){B=mod(B+base,M);D=mod(D+base*h1,M);T[1]=mod(T[1]+base*e2,M);}
    else if(v===2){E=mod(E+base,M);T[2]=mod(T[2]+base*h1,M);}
    else T[3]=mod(T[3]+base,M);
    W=mod(W+weight*origTerm,M);
    if(k<=n){g=mod(g+gTerm,M);J=mod(J+BigInt(k)*gTerm,M);}
    if(k<p-1){
      let mult=1n;
      for(let j=0;j<3;j++){
        if(k===cut[j]) mult=mod(mult*beta[j],M);
        else {
          mult=mod(mult*BigInt(k-cut[j]),M);
          const x=mod(beta[j]*inverse(BigInt(k-cut[j]),M),M);
          h1=mod(h1+x,M);h2=mod(h2+x*x,M);h3=mod(h3+x*x*x,M);
        }
      }
      const t=BigInt(k+1);
      d=mod(d*mult*inverse(2n*t**3n,M),M);
      const z=inverse(t,M);
      r1=mod(r1+z,M);r2=mod(r2+z*z,M);r3=mod(r3+z*z*z,M);
      origTerm=mod(origTerm*BigInt(2*k+1)*BigInt(3*k+1)*BigInt(3*k+2)*inverse(36n*t**3n,M),M);
      if(k<n) gTerm=mod(gTerm*BigInt(k-n)*BigInt(k-2*n)*inverse(BigInt(2*k+2-p)*t,M),M);
    }
  }
  const psi=mod(g*(g+12n*J),M),Tsum=mod(T.reduce((a,b)=>a+b,0n),M);
  const F=mod(A+B-alpha,M),H=mod(C+D+E-bbeta,M),I=mod(Tsum-gamma,M);
  const diffShadow=mod(psi-S-P*alpha-P**2n*bbeta-P**3n*gamma,M);
  const diffShell=mod(W-S-P*(A+B)-P**2n*(C+D+E)-P**3n*Tsum,M);
  const diffBridge=mod(W-psi-P*F-P**2n*H-P**3n*I,M);
  if(diffShadow||diffShell||diffBridge)throw Error("source identity mismatch at p="+p);
  const residue=mod(W-psi,M);
  if(residue%P!==0n)throw Error("Q not divisible by p="+p);
  return {p,W:String(W),Psi:String(psi),Q:String(residue/P),
    F:String(F%(P**3n)),H:String(H%(P**2n)),I:String(I%P),
    gamma:String(gamma%P),T:T.map(a=>String(a%P))};
}
const observed=[];
for(let p=7;p<=373;p+=6){
  let prime=true;for(let d=2;d*d<=p;d++)if(p%d===0)prime=false;
  if(prime)observed.push(audit(p));
}
const expected={
  7:["350","1246","215","1"],
  13:["19786","7761","925","6"],
  19:["82327","123158","4710","7"],
  31:["655433","555055","3238","12"],
  37:["962444","1231323","43386","1"],
  73:["17894855","3306900","199835","50"],
  373:["11832087049","14593651483","44491459","70"]
};
for(const x of observed)if(expected[x.p]){
  const got=[x.W,x.Psi,x.Q,x.I];if(JSON.stringify(got)!==JSON.stringify(expected[x.p]))throw Error("published witness mismatch at p="+x.p);
}
console.log("PASS",observed.length,"primes p=1 mod 6, 7<=p<=373: three independent congruences mod p^4");
console.log(JSON.stringify(observed.filter(x=>expected[x.p]),null,2));
