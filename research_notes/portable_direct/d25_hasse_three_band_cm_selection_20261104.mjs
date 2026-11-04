// Exact finite-field certificate for the 2304 Gauss -> Legendre Hasse pullback.
// Run: node d25_hasse_three_band_cm_selection_20261104.mjs
// Independent finite tests accompany the all-prime argument in the Markdown proof.
function mod(n,p) { return ((n%p)+p)%p; }
function pow(a,n,p) { let x=1; for(;n>0;n=Math.floor(n/2),a=mod(a*a,p)) if(n%2) x=mod(x*a,p); return x; }
function inv(a,p) { return pow(mod(a,p),p-2,p); }
function binomTable(n,p) {
  const B=[[1]];
  for(let r=1;r<=n;r++) {
    const row=Array(r+1).fill(1);
    for(let k=1;k<r;k++) row[k]=mod(B[r-1][k-1]+B[r-1][k],p);
    B.push(row);
  }
  return B;
}
function checkPolynomial(p) {
  const q=(p-5)/8, L=5*q+3, m=(p-1)/2, d=4*L;
  if (!Number.isInteger(q)) throw Error("Prime outside 5 mod 8");
  const B=binomTable(d,p), f=[1];
  for(let k=0;k<L;k++)
    f.push(mod(f[k]*(8*k+1)*(8*k+3)*inv(64*(k+1)*(k+1),p),p));
  const lhs=Array(d+1).fill(0);
  let power16=1;
  for(let k=0;k<=L;k++) {
    const c=mod(f[k]*power16,p), n=d-4*k;
    for(let i=0;i<=2*k;i++) {
      const a=mod(c*(i%2?-1:1)*B[2*k][i],p);
      for(let j=0;j<=n;j++) lhs[k+i+j]=mod(lhs[k+i+j]+a*B[n][j],p);
    }
    power16=mod(power16*16,p);
  }
  const rhs=Array(d+1).fill(0);
  for(let k=0;k<=m;k++) {
    const a=mod(B[m][k]*B[m][k],p);
    rhs[k]=mod(rhs[k]+a,p);
    rhs[p+k]=mod(rhs[p+k]-6*a,p);
    rhs[2*p+k]=mod(rhs[2*p+k]+a,p);
  }
  for(let i=0;i<=d;i++)
    if(lhs[i]!==rhs[i]) throw Error("Polynomial mismatch at p="+p+" coefficient="+i);
  return {p,coefficients:d+1};
}
function jacobiJet(p) {
  const q=(p-5)/8, B=binomTable(3*q+1,p);
  let value=0, jet=0, power9=1;
  const oneOver9=inv(9,p);
  for(let k=0;k<=q;k++) {
    const term=mod(B[q][k]*B[3*q+1][k]*power9,p);
    value=mod(value+term,p);
    jet=mod(jet+k*term,p);
    power9=mod(power9*oneOver9,p);
  }
  return {p,value,jet};
}
const cases=[5,13,29,37,53,61,101,109];
const polynomial=cases.map(checkPolynomial);
const jets=[5,13,29,37,53,373].map(jacobiJet);
for(const x of jets) {
  if(x.p%24===13 && (x.value!==0 || x.jet===0))
    throw Error("Inert jet check failed at p="+x.p);
  if(x.p%24===5 && x.value===0)
    throw Error("Split nonzero check failed at p="+x.p);
}
const report={
  result:"PASS",
  polynomial_prime_count:polynomial.length,
  polynomial_coefficient_count:polynomial.reduce((s,x)=>s+x.coefficients,0),
  polynomial, jets,
  arithmetic:"Exact modular integers; finite verification only"
};
console.log(JSON.stringify(report));
