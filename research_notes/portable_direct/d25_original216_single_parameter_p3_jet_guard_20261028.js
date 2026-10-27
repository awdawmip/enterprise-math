function check_original216_jet(){
 const primes=[7,13,19,31,37,43,61,67,73,211,373];
 const assert=(condition,message)=>{if(!condition)throw Error(message)};
 const mod=(a,m)=>(a%m+m)%m;
 function inverse(a,m){a=mod(a,m);let [r,R,t,T]=[m,a,0n,1n];while(R!==0n){const q=r/R;[r,R]=[R,r-q*R];[t,T]=[T,t-q*T];}assert(r===1n,"inverse nonunit");return mod(t,m)}
 function choose(n,k){k=Math.min(k,n-k);let z=1n;for(let j=1;j<=k;j++)z=z*BigInt(n-k+j)/BigInt(j);return z}
 function mul(a,b,q){return [a[0]*b[0]%q,(a[0]*b[1]+a[1]*b[0])%q,(a[0]*b[2]+a[1]*b[1]+a[2]*b[0])%q]}
 const results=[];
 for(const p of primes){
  const m=(p-1)/6,P=BigInt(p),q=P**3n,P2=P**2n;
  assert(Number.isInteger(m),"outside domain");
  const inv2=inverse(2n,q),inv3=inverse(3n,q), inv216=inverse(216n,q);
  let poly=[1n,0n,0n],total=[0n,0n,0n],byBand=Array.from({length:4},()=>[0n,0n,0n]);
  let pow216=1n,original=0n;
  for(let k=0;k<p;k++){
    if(k>0){
      const j=k-1;
      let f=[1n,0n,0n];
      for(const [a,c] of [[BigInt(j-3*m),inv2],[BigInt(j-2*m),inv3],[BigInt(j-4*m),2n*inv3%q]]) f=mul(f,[mod(a,q),c,0n],q);
      const d=inverse(2n*BigInt(k)**3n,q);
      poly=mul(poly,f,q).map(z=>z*d%q);
    }
    const band=k<=2*m?0:k<=3*m?1:k<=4*m?2:3;
    if(band>0)assert(poly[0]===0n,"jet constant not zero p="+p+" k="+k);
    if(band>1)assert(poly[1]===0n,"jet linear not zero p="+p+" k="+k);
    if(band>2)assert(poly[2]===0n,"jet quadratic not zero p="+p+" k="+k);
    const w=poly.map(z=>z*BigInt(6*k+1)%q);
    for(let a=0;a<=2;a++){byBand[band][a]=(byBand[band][a]+w[a])%q;total[a]=(total[a]+w[a])%q;}
    const c=choose(2*k,k)%q, t=choose(3*k,k)%q;
    const originalTerm=BigInt(6*k+1)*c%q*c%q*t%q*pow216%q;
    original=(original+originalTerm)%q;pow216=pow216*inv216%q;
  }
  const jet=(total[0]+P*total[1]+P2*total[2])%q;
  assert(jet===original,"jet/full mismatch p="+p);
  if(p%24===13||p%24===19)assert(original===P,"target finite fixture "+p);
  const tail=byBand[2][2]%P;
  if(p===373){
    assert(total[0]===15521276n,"J0 mismatch");
    assert(total[1]%P2===47909n,"J1 mismatch");
    assert(total[2]%P===133n,"J2 mismatch");
    assert(tail===266n,"highband mismatch");
    assert(byBand[0][2]%P===82n&&byBand[1][2]%P===158n,"band mismatch");
    const scaled=((total[0]+P*(total[1]%P2)-P)%q+q)%q;
    assert(scaled%P2===0n,"scaled integrality missing");
    assert(scaled/P2===240n,"scaled defect mismatch");
  }
  results.push({p,J0:Number(total[0]),J1_mod_p2:Number(total[1]%P2),J2_mod_p:Number(total[2]%P),high_jet2:Number(tail),jet_equals_full:true});
 }
 return {status:"PASS_D25_ORIGINAL216_SINGLE_PARAMETER_P3_JET",case_count:results.length,results}
}

if (typeof console !== 'undefined') console.log(JSON.stringify(check_original216_jet(),null,2));
