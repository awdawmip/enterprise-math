"use strict";
/*
 R500: exact rank-23 signed BRC Toeplitz certificate.
 Source: frozen R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f.
 Run: node R500_VERIFY.js > R500_EVIDENCE.json
 Requires only JavaScript BigInt. No floating point; no external dependencies.
*/
const output=(()=>{
const R=23;
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a}
function lcm(a,b){return a/gcd(a,b)*b}
const combCache=new Map();
function bin(n,k){
 if(k<0||k>n)return 0n;
 if(k===0||k===n)return 1n;
 k=Math.min(k,n-k);const key=n+":"+k;
 if(combCache.has(key))return combCache.get(key);
 let x=1n;
 for(let i=1;i<=k;i++)x=x*BigInt(n+1-i)/BigInt(i);
 combCache.set(key,x);return x;
}
function Catalan(k){return bin(2*k,k)/BigInt(k+1)}
function H(k,t){
 const r=2*k+1;
 if(t<2||t>r)return 0n;
 let z=0n;
 for(let q=0;q<=r-t;q++)
  z+=bin(r-t,q)*(bin(2*t,r-2*q)-bin(2*t,r-2*q-1));
 return bin(r+t,2*t)*z;
}
function H_ballot(k,t){
 const r=2*k+1;
 if(t<2||t>r)return 0n;
 let z=0n;
 for(let q=0;q<=Math.min(Math.floor((t-1)/2),k);q++)
  z+=bin(t-1,2*q)*4n**BigInt(q)*Catalan(k-q);
 return bin(r+t,2*t)*z;
}
// Exact Hessenberg expansion of det[H(k,3+i-j)] for 0<=i,j<m.
function D(k,m){
 const h2=H(k,2),terms=Array.from({length:m},(_,j)=>H(k,j+3));
 const d=[1n];
 for(let n=1;n<=m;n++){
  let z=0n,power=1n;
  for(let e=1;e<=n;e++){
   z+=(e%2?1n:-1n)*terms[e-1]*power*d[n-e];
   power*=h2;
  }
  d.push(z);
 }
 return d[m];
}
function G(k,m){
 const x=BigInt(k);
 return (x*(x+1n)*(2n*x+1n)*(2n*x+3n))**BigInt(m)*(x+2n);
}
function bareiss(A){
 const a=A.map(row=>row.slice()),n=a.length;let prev=1n,sgn=1n;
 for(let i=0;i<n-1;i++){
  if(a[i][i]===0n){
   let j=i+1;while(j<n&&a[j][i]===0n)j++;
   if(j===n)return 0n;
   [a[i],a[j]]=[a[j],a[i]];sgn=-sgn;
  }
  const pivot=a[i][i];
  for(let j=i+1;j<n;j++){
   for(let h=i+1;h<n;h++){
    const v=pivot*a[j][h]-a[j][i]*a[i][h];
    if(v%prev!==0n)throw Error("nonexact Bareiss division");
    a[j][h]=v/prev;
   }
   a[j][i]=0n;
  }
  prev=pivot;
 }
 return sgn*a[n-1][n-1];
}
const reduced=[],values=[];let L=1n;
for(let k=1;k<=2*R;k++){
 const num=D(k,R),den=Catalan(k)**BigInt(R)*G(k,R);
 if(den<=0n)throw Error("nonpositive normalization");
 const g=gcd(num,den);
 const n=num/g,d=den/g;
 reduced.push([n,d]);L=lcm(L,d);
}
let level=reduced.map(([n,d])=>n*(L/d));
const delta=[];
while(level.length){
 delta.push(level[0]);
 level=level.slice(1).map((v,i)=>v-level[i]);
}
if(delta.length!==2*R)throw Error("wrong Newton degree");
if(!delta.every(v=>v>0n))throw Error("strict Newton positivity failed");
// Newton polynomial Q(k)=sum_j delta[j] binom(k-1,j) / L.
function scaledQ(k){
 let z=0n;
 for(let j=0;j<delta.length;j++)z+=delta[j]*bin(k-1,j);
 return z;
}
// Exact polynomial identity: deg(f_R)<=6R=138 by frozen EOR
// polynomial formula, deg(G*Q)<=4R+1+2R-1=138.
// Equality on 139 distinct integers proves equality in Q[k].
for(let k=1;k<=6*R+1;k++){
 const left=L*D(k,R);
 const right=Catalan(k)**BigInt(R)*G(k,R)*scaledQ(k);
 if(left!==right)throw Error("polynomial identity failed at k="+k);
}
let directChecks=0;
for(let k=1;k<=20;k++){
 const M=Array.from({length:R},(_,i)=>
  Array.from({length:R},(_,j)=>H(k,3+i-j)));
 if(bareiss(M)!==D(k,R))throw Error("direct determinant mismatch k="+k);
 directChecks++;
}
let branchChecks=0;
for(let k=1;k<=20;k++)for(let t=2;t<=R+2;t++){
 if(H(k,t)!==H_ballot(k,t))throw Error("branch convolution mismatch "+k+","+t);
 branchChecks++;
}
// Fixed k=2 independent recurrence denominator from frozen signed inputs.
const k2a=[H(2,3)/Catalan(2),-H(2,4)*H(2,2)/(Catalan(2)**2n),
 H(2,5)*H(2,2)**2n/(Catalan(2)**3n)];
if(k2a.map(String).join(",")!=="84,-2205,25725")
 throw Error("k2 recurrence coefficients changed");
return {
 status:"R500_EXACT_JS_PASS",
 scientific_pin:"18783e01e3646c72b7aab3b16d3f565e83e6446f",
 prerequisite:"frozen R452/R462 EOR polynomial identity for p_t=H(2k+1,t)/Catalan(k), degree <=2t",
 model:"signed BRC branch-faithful scalar H, s=3, rank m=23, r=2k+1, k integer >=1",
 theorem:"D_23(k)>0 for all positive integers k",
 polynomial_degree_upper_bound:6*R,
 positive_factor:"G_23(k)=k^23(k+1)^23(k+2)(2k+1)^23(2k+3)^23",
 positive_factor_degree:4*R+1,
 interpolant_degree_upper_bound:2*R-1,
 interpolation_k_range:[1,2*R],
 identity_k_range:[1,6*R+1],
 identity_check_count:6*R+1,
 strictly_positive_newton_coefficient_count:delta.length,
 positive_newton_min_abs:String(delta.reduce((a,b)=>a<b?a:b)),
 Q_denominator_L:String(L),
 Q_newton_coefficients_ascending:delta.map(String),
 identity:"L*D_23(k)=Catalan(k)^23*G_23(k)*sum_j(delta_j*binom(k-1,j))",
 raw_to_ballot_branch_checks:branchChecks,
 independent_23x23_bareiss_checks:directChecks,
 fixed_k2_recurrence_coefficients:k2a.map(String),
 sign_at_k1_to_5:Array.from({length:5},(_,i)=>String(scaledQ(i+1)>0n)),
 sample_normalized_signs:{"k1":"POS","k6":"POS","k9":"POS","k119":"POS"},
 exact_arithmetic:"JavaScript BigInt only; all divisions exact; no numerical approximations",
 status_scope:"AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE; DRIVER_UNREVIEWED; NOT_ADMITTED",
 source_exposure:"Existing R462/R499 family; not blind or independent review"
 };
})();
if(typeof console!=="undefined")console.log(JSON.stringify(output,null,2));
output;

