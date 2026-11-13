"use strict";
/* R501 exact rank-24 right-edge signed BRC scalar certificate.
   Frozen science input R462@18783e01e3646c72b7aab3b16d3f565e83e6446f.
   Execute: node R501_VERIFY.js > R501_EVIDENCE.json
   BigInt only, no dependencies; checks full polynomial identity and direct determinants. */
const R=24;
const gcd=(aa,bb)=>{let a=aa<0n?-aa:aa,b=bb<0n?-bb:bb;while(b){[a,b]=[b,a%b]}return a};
const lcm=(a,b)=>a/gcd(a,b)*b;
const cb=new Map();
function bin(n,k){if(k<0||k>n)return 0n;if(!k||k===n)return 1n;k=Math.min(k,n-k);const key=n+":"+k;if(cb.has(key))return cb.get(key);
 let x=1n;for(let i=1;i<=k;i++)x=x*BigInt(n+1-i)/BigInt(i);cb.set(key,x);return x}
const C=k=>bin(2*k,k)/BigInt(k+1);
function H(k,t){const r=2*k+1;if(t<2||t>r)return 0n;let s=0n;
 for(let q=0;q<=r-t;q++)s+=bin(r-t,q)*(bin(2*t,r-2*q)-bin(2*t,r-2*q-1));
 return bin(r+t,2*t)*s}
function H2(k,t){const r=2*k+1;if(t<2||t>r)return 0n;let s=0n;
 for(let q=0;q<=Math.min(Math.floor((t-1)/2),k);q++)s+=bin(t-1,2*q)*4n**BigInt(q)*C(k-q);
 return bin(r+t,2*t)*s}
function D(k,m){const p=H(k,2),h=Array.from({length:m},(_,i)=>H(k,i+3)),ds=[1n];for(let n=1;n<=m;n++){
 let s=0n,pp=1n;for(let e=1;e<=n;e++){s+=(e%2?1n:-1n)*h[e-1]*pp*ds[n-e];pp*=p}ds.push(s)}return ds[m]}
function G(k,m){const z=BigInt(k);return (z*(z+1n)*(2n*z+1n)*(2n*z+3n))**BigInt(m)*(z+2n)}
function diff(a){const out=[];let v=a.slice();while(v.length){out.push(v[0]);v=v.slice(1).map((x,i)=>x-v[i])}return out}
function N(delta,k,k0){let s=0n;for(let j=0;j<delta.length;j++)s+=delta[j]*bin(k-k0,j);return s}
function bareiss(A){const a=A.map(r=>r.slice()),n=a.length;let prev=1n,sign=1n;
 for(let i=0;i<n-1;i++){if(!a[i][i]){let j=i+1;while(j<n&&!a[j][i])j++;if(j===n)return 0n;[a[i],a[j]]=[a[j],a[i]];sign=-sign}
 let p=a[i][i];for(let j=i+1;j<n;j++){for(let h=i+1;h<n;h++){let v=p*a[j][h]-a[j][i]*a[i][h];
 if(v%prev)throw Error("nonexact Bareiss");a[j][h]=v/prev}a[j][i]=0n}prev=p}return sign*a[n-1][n-1]}
let L=1n;const fractions=[];
for(let k=1;k<=2*R;k++){const num=D(k,R),den=C(k)**BigInt(R)*G(k,R),g=gcd(num,den);
 if(den<=0n)throw Error("nonpositive G");fractions.push([num/g,den/g]);L=lcm(L,den/g)}
const delta=diff(fractions.map(([n,d])=>n*(L/d)));
if(delta.length!==2*R)throw Error("interpolant size mismatch");
let identityChecks=0;
for(let k=1;k<=6*R+1;k++){const left=L*D(k,R),right=C(k)**BigInt(R)*G(k,R)*N(delta,k,1);
 if(left!==right)throw Error("identity failed k="+k);identityChecks++}
const tail=diff(Array.from({length:2*R},(_,j)=>N(delta,19+j,1)));
if(tail.length!==48||!tail.every(x=>x<0n))throw Error("tail negativity certificate failed");
const before=Array.from({length:18},(_,i)=>N(delta,i+1,1));
if(!before.every(x=>x>0n))throw Error("finite positivity failed");
let direct=0;for(let k=1;k<=20;k++){const M=Array.from({length:R},(_,i)=>Array.from({length:R},(_,j)=>H(k,3+i-j)));
 if(bareiss(M)!==D(k,R))throw Error("Bareiss check k="+k);direct++}
let branch=0;for(let k=1;k<=20;k++)for(let t=2;t<=R+2;t++){if(H(k,t)!==H2(k,t))throw Error("BRC ballot mismatch");branch++}
const evidence={
 status:"R501_EXACT_JS_PASS",date:"2026-11-03",
 scientific_pin:"18783e01e3646c72b7aab3b16d3f565e83e6446f",
 predecessor:"R500@0e54475ed4443f6c6f0da06ed70a43b5d02f12cf",
 input:"r=2k+1; C_k=binom(2k,k)/(k+1); H_k(t)=binom(r+t,2t)[x^r](1-x)(1+x)^(2t)(1+x^2)^(r-t) for 2<=t<=r; otherwise H=0; D_24=det[H_k(3+i-j)]_0<=i,j<24",
 theorem:"D_24(k)>0 for 1<=k<=18; D_24(k)<0 for all integers k>=19",
 inherited_polynomial_prerequisite:"R452/R462: p_t(k)=H_k(t)/C_k in Q[k] and deg(p_t)<=2t",
 recurrence:"f_0=1; f_m=sum_(ell=1)^m (-1)^(ell-1) p_(ell+2) p_2^(ell-1) f_(m-ell)",
 polynomial_degree_upper_bound:144,
 G:"G_24(k)=k^24(k+1)^24(k+2)(2k+1)^24(2k+3)^24",
 G_degree:97,interpolant_degree_max:47,
 normalization_L:String(L),
 integer_identity:"L*D_24(k)=C_k^24*G_24(k)*sum_(j=0)^47(delta_j*binom(k-1,j))",
 newton_delta_at_k1:delta.map(String),
 finite_k1_to18_scaled_numerators:before.map(String),
 tail_shift_origin_k:19,
 tail_newton_coefficients:tail.map(String),
 tail_coefficient_count:tail.length,
 max_tail_coefficient:String(tail.reduce((a,b)=>a>b?a:b)),
 identity_grid:"k=1..145",identity_checks:identityChecks,
 independent_direct_24x24_Bareiss_checks:direct,
 original_BRC_to_ballot_checks:branch,
 exact_arithmetic:"JavaScript BigInt; exact divisions; no floating point",
 status_scope:"AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE; NO_NATIVE_CLAIM; DRIVER_UNREVIEWED; NOT_ADMITTED"
};
if(typeof console!=="undefined")console.log(JSON.stringify(evidence,null,2));
