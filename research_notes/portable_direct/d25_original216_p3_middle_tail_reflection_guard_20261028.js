function check_original216_tail(){
  const primes=[7,13,19,31,37,43,61,67,73,79,97,103,109,127,139,151,157,163,181,193,199,211,373];
  const assert=(test,message)=>{if(!test)throw Error(message);};
  const mod=(a,m)=>(a%m+m)%m;
  function choose(n,k){
    k=Math.min(k,n-k);let ans=1n;
    for(let i=1;i<=k;i++)ans=ans*BigInt(n-k+i)/BigInt(i);
    return ans;
  }
  function inverse(a,m){
    let [r,newr,t,newt]=[m,mod(a,m),0n,1n];
    while(newr!==0n){const q=r/newr;[r,newr]=[newr,r-q*newr];[t,newt]=[newt,t-q*newt];}
    assert(r===1n,"non-unit denominator");
    return mod(t,m);
  }
  function powmod(a,k,m){
    let ans=1n;a=mod(a,m);
    while(k>0n){if(k&1n)ans=ans*a%m;a=a*a%m;k>>=1n;}
    return ans;
  }
  const outputs=[];
  for(const p of primes){
    const m=(p-1)/6,P=BigInt(p),P2=P*P,P3=P2*P;
    assert(Number.isInteger(m),"prime class mismatch");
    const fact=[1n];for(let k=1;k<p;k++)fact.push(fact[k-1]*BigInt(k)%P);
    let inverse216=inverse(216n,P3),power216=1n,bulk=0n,tail=0n,discard=0n,full=0n;
    const observed=new Map();
    for(let n=0;n<p;n++){
      const central=choose(2*n,n)%P3;
      const multinomial=choose(3*n,n)%P3;
      const weighted=BigInt(6*n+1)*central%P3*central%P3*multinomial%P3*power216%P3;
      full=(full+weighted)%P3;
      if(n<=3*m)bulk=(bulk+weighted)%P3;
      else if(n<=4*m){
        assert(weighted%P2===0n,"middle tail not p2 integral");
        tail=(tail+weighted)%P3;observed.set(n,weighted/P2);
      }else{
        assert(weighted===0n,"high tail not p3 integral");
        discard=(discard+weighted)%P3;
      }
      power216=power216*inverse216%P3;
    }
    let reflected=0n,previous=0n;
    for(let r=0;r<m;r++){
      const denominator=fact[4*m+1+2*r]*fact[3*r+1]%P;
      const c=BigInt(3*(2*r+1))*powmod(216n,BigInt(2*m+r),P)%P*
        powmod(fact[2*m+r],5n,P)%P*inverse(denominator,P)%P;
      assert(c===observed.get(4*m-r),"coefficient reflection mismatch at p="+p+" r="+r);
      if(r>0){
        const j=r-1;
        const top=BigInt(2*j+3)*216n%P*powmod(BigInt(2*m+j+1),5n,P)%P;
        const bottom=BigInt(2*j+1)*BigInt(4*m+2+2*j)*BigInt(4*m+3+2*j)*
          BigInt(3*j+2)*BigInt(3*j+3)*BigInt(3*j+4)%P;
        assert(c===previous*top%P*inverse(bottom,P)%P,"reflection recurrence mismatch");
      }
      reflected=(reflected+c)%P;previous=c;
    }
    assert(tail%P2===0n&&tail/P2===reflected,"tail aggregate mismatch");
    assert((bulk+tail+discard)%P3===full,"full original cutoff mismatch");
    if(p%24===13||p%24===19)assert(full===P,"target finite fixture mismatch at p="+p);
    if(p===373){
      assert(bulk===14887176n&&tail===37008314n&&reflected===266n&&full===373n,
        "original p373 fixture mismatch");
      assert(mod(bulk-P,P3)/P2===107n,"p373 compensating bulk defect mismatch");
    }
    outputs.push([p,Number(reflected)]);
  }
  return {status:"PASS_D25_ORIGINAL216_P3_MIDDLE_TAIL_REFLECTION",cases:outputs.length,
    original_p373:373,bulk_p373:14887176,tail_p373:37008314,tail_digit_p373:266,
    bulk_digit_p373:107,modulus_p373:51895117,tail_digits:outputs};
}

if (typeof console !== 'undefined') console.log(JSON.stringify(check_original216_tail(),null,2));
