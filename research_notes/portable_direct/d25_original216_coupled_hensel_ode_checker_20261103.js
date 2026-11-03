"use strict";
// D25 finite Hensel 3-strip third-order coupled differential certificate.
// Run with node d25_original216_coupled_hensel_ode_checker_20261103.js
function verifyD25CoupledODE(){
  const primes=[7,13,19,37,43,109,181,373];
  const mod=(x,m)=>((x%m)+m)%m;
  const inv=(x,m)=>{let a=mod(x,m),b=m,u=1n,v=0n;while(b){const q=a/b;[a,b]=[b,a-q*b];[u,v]=[v,u-q*v]}if(a!==1n)throw Error("nonunit");return mod(u,m)};
  const binom=(n,k)=>{let x=1n;for(let j=1;j<=k;j++)x=x*BigInt(n-j+1)/BigInt(j);return x};
  const cases=[];
  for(const p of primes){
    const r=(p-1)/6,a=2*r,b=3*r,c=4*r,P=BigInt(p),M=P**3n,
      i2=inv(2n,M),i3=inv(3n,M),i6=inv(6n,M),i9=inv(9n,M),i216=inv(216n,M);
    let jets=[[1n,0n,0n]],prod216=1n,W=0n;
    for(let k=0;k<p;k++){
      const ck=k<=c?jets[k]:[0n,0n,0n];
      const bin=mod(binom(2*k,k)**2n*binom(3*k,k)*prod216,M);
      if(mod(ck[0]+P*ck[1]+P*P*ck[2],M)!==bin)throw Error(`original mismatch p=${p} k=${k}`);
      W=mod(W+BigInt(6*k+1)*bin,M);
      if(k<c){
        const x=BigInt(k-b),y=BigInt(k-a),z=BigInt(k-c);
        const t0=mod(x*y*z,M),t1=mod(y*z*i2+x*z*i3+2n*x*y*i3,M),t2=mod(z*i6+y*i3+2n*x*i9,M);
        const d=inv(2n*BigInt(k+1)**3n,M);
        jets.push([mod(ck[0]*t0*d,M),mod((ck[1]*t0+ck[0]*t1)*d,M),mod((ck[2]*t0+ck[1]*t1+ck[0]*t2)*d,M)]);
      }
      prod216=mod(prod216*i216,M);
    }
    if(jets.length!==c+1)throw Error("jet length");
    let weightedJet=0n,checked=0;
    for(let k=0;k<=c+1;k++){
      const here=k<=c?jets[k]:[0n,0n,0n];
      const prev=k>0?jets[k-1]:[0n,0n,0n];
      const j=BigInt(k-1),x=j-BigInt(b),y=j-BigInt(a),z=j-BigInt(c);
      const q0=mod(x*y*z,M),
        q1=mod(y*z*i2+x*z*i3+2n*x*y*i3,M),
        q2=mod(z*i6+y*i3+2n*x*i9,M);
      const lhs=here.map(x=>mod(BigInt(k)**3n*x,M));
      const rhs=[mod(i2*q0*prev[0],M),mod(i2*(q0*prev[1]+q1*prev[0]),M),mod(i2*(q0*prev[2]+q1*prev[1]+q2*prev[0]),M)];
      if(k===0){if(here[0]!==1n||here[1]!==0n||here[2]!==0n)throw Error("origin")}
      else if(lhs.some((x,i)=>x!==rhs[i]))throw Error("ODE fails p="+p+" k="+k);
      if(k<=c)weightedJet=mod(weightedJet+BigInt(6*k+1)*mod(here[0]+P*here[1]+P*P*here[2],M),M);
      checked++;
    }
    if(weightedJet!==W)throw Error("weighted W mismatch");
    if(jets.slice(a+1).some(x=>x[0]!==0n)||jets.slice(b+1).some(x=>x[1]!==0n)||jets[a][0]%P===0n||jets[b][1]%P===0n||jets[c][2]%P===0n)throw Error("degree filtration wrong");
    cases.push({p,a,b,c,checked_original_positions:p,checked_differential_coefficients:checked,
      exact_degree_support:[a,b,c],final_boundary_jet_rhs:["0","0","0"],
      weighted_original_W_mod_p3:String(W),target_residual:(p%24===13||p%24===19)?String(mod(W-P,M)):"not_target"});
  }
  return {schema:"D25_FINITE_COUPLED_THIRD_ORDER_HENSEL_ODE_CERTIFICATE_V1",
    numerical_semantics:"Exact BigInt Z/(p^3), every p-unit inverted; polynomial proof in companion note. The ODE is tested coefficientwise to degree c+1, original binomial to k=p-1.",cases};
}
console.log(JSON.stringify(verifyD25CoupledODE(), null, 2));
