# R284KT — uniform evaluated arithmetic height and factorial carrier

2026-11-29. Author proof and exact BigInt checks, NOT_REVIEWED. Auxiliary R284 arithmetic, not native spatial transfer. Own prior frontier R284KS, historical Activity RA-B82240E8488EF5A1DA5186C4; current session recovery not confirmed (gateway BACKEND_IDENTITY_CHECK_UNAVAILABLE); no new identity, shared claim, or task mutation. Owner inventory r1-20261129-0000-leased-inventory last observed RUNNING. Global entries verified at main aec2c548ea43ef96c3e8b0c58545290502849ae7; global P000 V4 canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched projection; Source P000 V5, foundation projection, joint and heartbeat contracts, ACTIVE worldview, portable and current method read. Frozen science: KO 0c99ee610045cd1d36e9da996f257ae4afabc0be:research_notes/portable_direct/R284KO_FIXED_SUPPORT_FAMILY_AND_EVEN_DECIC_20261128.md; KS 57423d472d6d65475583b7239efc51154c183d65:research_notes/portable_direct/R284KS_FIRST_ORDER_MACRO_RESONANCE_THIN_STRIP_20261128.md; KR, JR pins inherited unchanged.

## 1. Exact factorial-normalized carrier

For integers s>=0, d>=8(s+4), d+s odd, set t=s+1, q0=(s-d)/2, u=(d+s)/2, r=R_u(d), and J=(d+s)(d+s+1), L=4s+2. Define positive odd a_j=3d+s+4-2j, b_j=d-s-2-2j for 0<=j<t. KO gives rho_i=(-1)^i prod_{j<i} a_j/b_j for 0<=i<=t. Write B=prod b_j, O=oddpart(t!), ell=oddpart(lcm(1,...,t)), A=ell B/O, T=binom(2s+2,s). Then A and T are positive integers and A rho_i and T R_s(i) are integers for all i=0,...,t (R_s(t)=0).

Proof: for an odd prime p, a length k arithmetic progression of step 2 or -2 contains at least floor(k/p^e) multiples of p^e for every e>=1, so its product is divisible by oddpart(k!). In particular O divides B. The product B rho_i (up to sign) is a prefix of length i of a_j and a suffix of length t-i of b_j. Its p-valuation is at least v_p(i!)+v_p((t-i)!). By Legendre's formula v_p(binom(t,i))<=floor(log_p t)=v_p(ell), since each summand in the difference of floors is zero or one. Thus O divides ell B rho_i; these are integer products and all odd, so no 2-adic issue. Separately R_s(i)=binom(2s+2,s-i)/T for 0<=i<=s. This proves the exact simultaneous normalization without dropping signed terms, branch positions, or endpoint contributions.

Use H=8 J L A T. By KO/KS exact observer formulas the normalized values H V/r,H Q/r,H A_observer/r are integers: the branch sum denominators divide A T and the quadratic weight denominator divides 4J. Here A_observer denotes KO's joint weighted sum, distinct from integer A above. Moreover H E/r is integral since E/r=(s-d)(2d+3)(s+2)/(4(d+s+1)L). H Z/r is integral even with q0 half-integral: H A_observer/r is a multiple of 2. W=A_observer+E and Z=q0 A_observer+Q+V, so the entire residual
Ntilde=2 H^2 C(q0,d)/r^2
is an integer. Equivalently with W_H=HW/r, Q_H=HQ/r,Z_H=HZ/r,
Ntilde=3(s-d)(2s+d+1)^2 W_H Q_H -32(3s-d+2) Z_H^2.

For every prime p>d+s+2, all factors of H are p-units: B has factors <=d, ell has primes <=t, O divides B, T has prime factors <=2s+2, J has factors <=d+s+1, and L=2(2s+1). KO's original carrier normalization likewise has only small prime factors: D(q0)*r is a product of factors of absolute value <=d+s+2 times a power of 2, as seen from KO's D_s and D_u*r, J,L. Thus v_p(P_d(q0))=v_p(Ntilde), with infinity convention for zero. If legal integer q is a zero of P_d, h_s=2q+d-s satisfies v_p(h_s)<=v_p(Ntilde) for every p>d+s+2 dividing h_s. This preserves the complete composite coordinate h_s and the large-prime valuation constraint, not merely its prime support. No claim for small primes or higher derivatives of the polynomial from this evaluated integer alone.

## 2. Uniform height theorem

An elementary estimate ell<=8^t follows from lcm(1,...,n) dividing lcm(1,...,ceil(n/2))*binom(n,floor(n/2)): for a prime power p^e in (ceil(n/2),n], its contribution to the binomial valuation is one by the floor formula, and at most one such power per prime exists. Induct using binom<=2^n and n+3 ceil(n/2)<=3n for n>=3, checking n=1,2 separately. Also O>=t!/2^t, B<=d^t and T<=4^t. Using t! >= (t/e)^t (integral bound for log factorial),
A T <= (64 e d/t)^t.
On the wedge a_j/b_j<=6, hence |rho_i|<=6^t; 0<=R_s(i)<=1. There are t+1 terms, and the KO short observer gives |V/r|,|Q/r|<=8 d^3 6^t, |A_observer/r|<=48 d^3 6^t using absolute quadratic weight <=3, |E/r|<=d, |W/r|<=49 d^3 6^t, |Z/r|<=40 d^4 6^t. Since |q0|<=d/2, |4q0+3d+1|<=2d, |3q0+d+1|<=d, we obtain |C/r^2|<=60000 d^9 36^t. H<=32 d^3 A T. Therefore
|Ntilde| <= 2^27 d^15 (384 e d/t)^(2t).
For Ntilde nonzero, log |Ntilde| <= 27 log 2 +15 log d+2t log(384 e d/t).
In particular bit length O(log d+t log(d/t)+t), uniformly, and O(d) on the entire wedge, versus the unnormalized common-product bound O(t log d+log d). This is a bound for a specialized integer witness, not a bound on the coefficients of KO's polynomial N_s. It is constructive and does not assume nonvanishing; on the KR nonzero region it immediately bounds the total multiplicity of all primes p>d+s+2 dividing the observer by the log-height bound divided by log(d+s+2). No claim that this alone forces a qualifying prime or rules out the positive-budget zero. Per-evaluation arithmetic uses O(s) exact integer multiplications/divisions plus lcm gcd computations; operand bit lengths and their costs are not constant.

## 3. Executed exact verification

Every admissible pair 32<=d<=200 and 8(s+4)<=d was checked by comparing the compressed V,Q,A_observer against an independent full d+1 branch sum with both branch denominators cleared. The endpoint uses the exact KO closed formula in both descriptions. Five larger evaluations checked every exact division in the compressed carrier; they are not independent full-sum checks. Bit lengths report A versus B and H versus 8 J L B T (same T), not minimal reduced denominators. Finite zeros are reported only within this sample. The proof above covers all specified d,s independently of sample. Code and actual output:

```javascript
function experiment(){
 const gcd=(a,b)=>{while(b){let r=a%b;a=b;b=r}return a<0n?-a:a};
 const div=(a,b)=>{if(b===0n||a%b!==0n)throw Error("nonexact division");return a/b};
 const bits=n=>(n<0n?-n:n).toString(2).length;
 const choose=(n,k)=>{let z=1n;for(let i=1n;i<=k;i++)z=div(z*(n-i+1n),i);return z};
 function evaluate(D,S,check){
  const d=BigInt(D),s=BigInt(S),t=s+1n,J=(d+s)*(d+s+1n),L=4n*s+2n;
  if(d<8n*(s+4n)||(d+s)%2n!==1n)throw Error("domain");
  let B=1n,o=1n,l=1n;
  const bs=[],as=[];
  for(let j=0n;j<t;j++){let a=3n*d+s+4n-2n*j,b=d-s-2n-2n*j;as.push(a);bs.push(b);B*=b;let z=j+1n;while(z%2n===0n)z/=2n;o*=z;l=l/gcd(l,z)*z}
  const A=div(B,o)*l,T=choose(2n*s+2n,s),H=8n*J*L*A*T;
  let r=A,c=T,prev=0n,V=0n,Q=0n,An=0n;
  for(let i=0;i<=S+1;i++){
   let k=BigInt(i);
   if(i){r=div(-r*as[i-1],bs[i-1]);c=div(c*(s-k+1n),s+k+2n)}
   let v=(d-k+1n)*(k+1n)*r*c,b=(d-k+1n)*k*r*prev;
   V+=v;Q+=b;An+=(s-d+2n*k)*(3n*d+s-2n*k+4n)*(v+b);prev=c;
  }
  V*=8n*J*L;Q*=8n*J*L;An*=2n*L;
  let E=div(H*(s-d)*(2n*d+3n)*(s+2n),4n*(d+s+1n)*L),W=An+E,Z=div((s-d)*An,2n)+Q+V;
  let N=3n*(s-d)*(2n*s+d+1n)**2n*W*Q-32n*(3n*s-d+2n)*Z*Z;
  if(check){
   // Independent complete d+1 support, with both branches cleared.
   const raw=v=>{let u=Array(D+1),tail=1n,pre=1n;u[D]=1n;for(let k=D-1;k>=0;k--)u[k]=u[k+1]*(v+2n*BigInt(k+3));tail=u[0];for(let k=0;k<=D;k++){u[k]*=pre;pre*=v-2n*BigInt(k)}return [tail,u]};
   const [,U]=raw(d+s),[Dn,Rs]=raw(2n*s);let v=0n,b=0n,a=0n;
   for(let k=0;k<=D;k++){let K=BigInt(k),i=D-k,I=BigInt(i);let f=(K+1n)*(I+1n)*U[k]*Rs[i],g=i?(K+1n)*I*U[k]*Rs[i-1]:0n;v+=f;b+=g;a+=(d+s-2n*K)*(d+s+2n*K+4n)*(f+g)}
   let den=U[D]*Dn;
   if(V*den!==H*v||Q*den!==H*b||An*4n*J*den!==H*a)throw Error("full carrier mismatch "+D+","+S);
  }
  return {d:D,s:S,B_bits:bits(B),A_bits:bits(A),H_bits:bits(H),oldH_bits:bits(8n*J*L*B*T),N_bits:bits(N),sign:N===0n?0:N>0n?1:-1};
 }
 let count=0,zero=0,strict=0;
 for(let d=32;d<=200;d++)for(let s=0;8*(s+4)<=d;s++)if((d+s)%2){let r=evaluate(d,s,true);count++;zero+=+(r.sign===0);strict+=+(r.A_bits<r.B_bits)}
 const samples=[[1000,99],[4000,399],[16000,1599],[16000,1713],[64000,6399]].map(([d,s])=>evaluate(d,s,false));
 return {full_checks:count,zero_in_finite_checks:zero,strict_denominator_bit_reductions:strict,samples};
}
console.log(JSON.stringify(experiment(),null,2));
```

```json
{
  "full_checks": 935,
  "zero_in_finite_checks": 0,
  "strict_denominator_bit_reductions": 553,
  "samples": [
    {
      "d": 1000,
      "s": 99,
      "B_bits": 965,
      "A_bits": 666,
      "H_bits": 894,
      "oldH_bits": 1192,
      "N_bits": 1829,
      "sign": 1
    },
    {
      "d": 4000,
      "s": 399,
      "B_bits": 4657,
      "A_bits": 2733,
      "H_bits": 3566,
      "oldH_bits": 5489,
      "N_bits": 7183,
      "sign": 1
    },
    {
      "d": 16000,
      "s": 1599,
      "B_bits": 21825,
      "A_bits": 10988,
      "H_bits": 14225,
      "oldH_bits": 25062,
      "N_bits": 28511,
      "sign": 1
    },
    {
      "d": 16000,
      "s": 1713,
      "B_bits": 23334,
      "A_bits": 11565,
      "H_bits": 15031,
      "oldH_bits": 26800,
      "N_bits": 30115,
      "sign": 1
    },
    {
      "d": 64000,
      "s": 6399,
      "B_bits": 100097,
      "A_bits": 44075,
      "H_bits": 56918,
      "oldH_bits": 112940,
      "N_bits": 113906,
      "sign": 1
    }
  ]
}
```

## 4. Next

Retain the whole vector of evaluated witnesses for adjacent support coordinates and exploit common factorial normalization across s; seek a bound for joint exceptional-prime mass sharper than summing separate log-height estimates. Alternatively use KS thin strip for certified candidate enumeration and explicit second-order error. Original positive-budget all-integer exclusion remains at d<=3200 as previously reported, unchanged. No independent review, formal Result or Foundation admission.
