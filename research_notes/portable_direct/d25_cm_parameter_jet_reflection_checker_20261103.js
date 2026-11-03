// D25 executed exact arithmetic checker, standard Node.js BigInt, original 216 recurrence.
function verify(){
  const mod=(a,m)=>((a%m)+m)%m;
  const inv=(a,m)=>{
    let [t,nt,r,nr]=[0n,1n,m,mod(a,m)];
    while(nr){let q=r/nr;[t,nt]=[nt,t-q*nt];[r,nr]=[nr,r-q*nr];}
    if(r!==1n)throw Error("not a unit");
    return mod(t,m);
  };
  const pow=(a,n,m)=>{let v=1n;for(a=mod(a,m);n>0n;n>>=1n,a=a*a%m)if(n&1n)v=v*a%m;return v;};
  const isPrime=n=>{for(let d=2;d*d<=n;d++)if(n%d===0)return false;return n>1;};
  let count=0;const witnesses={};
  for(let pi=13;pi<=2000;pi++){
    if(!isPrime(pi)||![13,19].includes(pi%24))continue;
    const p=BigInt(pi),m=p**3n,r=(pi-1)/6,inv36=inv(36n,m);
    const b=[1n];
    for(let k=0;k<pi-1;k++){
      const n=BigInt(k+1),term=BigInt(2*k+1)*BigInt(3*k+1)*BigInt(3*k+2);
      const ik=inv(n,m);
      b.push(b[k]*term%m*inv36%m*ik%m*ik%m*ik%m);
    }
    let z=1n,c=1n,j=0n,ell=0n,inv2=inv(2n,p);
    for(let k=0;k<=r;k++){
      const term=c*z%p;
      ell=(ell+term)%p;j=(j+BigInt(k)*term)%p;
      if(k<r){let kk=BigInt(k);c=c*BigInt(r-k)%p*BigInt(2*r-k)%p*pow(inv(kk+1n,p),2n,p)%p;z=z*inv2%p;}
    }
    if(ell!==0n||j===0n)throw Error("CM0 or simple-root failed at "+pi);
    let W=0n,D=0n,T=0n,C1=0n,Cw=0n,Wshift=0n,tk=1n;
    for(let k=0;k<pi;k++){
      let q=b[k]*b[pi-1-k]%m,weight=BigInt(6*k+1);
      W=(W+weight*b[k])%m;
      D=(D+BigInt(k)*weight*b[k])%m;
      T=(T+BigInt(k*(k-1))*weight*b[k])%m;
      C1=(C1+q)%m;Cw=(Cw+weight*q)%m;
      Wshift=(Wshift+weight*b[k]*tk)%m;
      tk=tk*(1n+p)%m;
    }
    if(D%p!==12n*j*j%p||T%p!==8n*j*j%p)throw Error("jet mismatch "+pi);
    if(mod(C1-10n*p*p,m)!==0n||mod(Cw+20n*p*p,m)!==0n)throw Error("3-port mismatch "+pi);
    if(mod(Wshift-W-p*D-4n*p*p*j*j,m)!==0n)throw Error("Taylor mismatch "+pi);
    if(mod(Wshift-W,p*p)!==mod(12n*p*j*j,p*p))throw Error("CM shift mismatch "+pi);
    if(pow(1n+p,p-1n,m)*C1%m!==C1)throw Error("reflection invariance mismatch "+pi);
    count++;
    if([13,19,373].includes(pi))witnesses[pi]={r,j:String(j),W:String(W),D_mod_p2:String(D%(p*p)),D_mod_p:String(D%p),T_mod_p:String(T%p),W_1plusp:String(Wshift),delta:String(mod(Wshift-W,m)),C1:String(C1),Cw:String(Cw)};
  }
  return {target_primes_tested:count,range:"13<=p<=2000, p mod24 in {13,19}",tests:["CM0","simple-root-nonzero","D=12j^2 modp","T=8j^2 modp","C1=10p² modp³","C(6k+1)=-20p² modp³","C(1+p)=C(1) modp³","W Taylor modp³"],status:"PASS",witnesses};
}
console.log(JSON.stringify(verify(),null,2));
