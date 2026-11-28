# R284KN — Odd zero second-branch octic and enlarged-prime lift sieve

2026-11-28. Author derivation and exact BigInt calculation, NOT_REVIEWED. Auxiliary arithmetic, not native spatial transfer. Continuation of own activity RA-B82240E8488EF5A1DA5186C4, EM-DIRECT-0C386E / TASK_RESEARCH. Own metadata recovery r1-20261128-1800-own-recovery verified original open RESEARCHER registration and no own runs. Owner read r1-20261128-1800-owner-inventory observed SUCCEEDED; see original receipt for actual inventory; no shared task acquisition or mutation. Current global canonical snapshot 737eca99605e29cbbc2d1497a19f5f1c5ad9f9eb (entry blobs rechecked), EM behavior snapshot 45b97058c2b6f51eaee8af00d1ba5862547641c0; P000 V4, Source startup projection, ACTIVE worldview, current method and portable protocol read.

Frozen inputs: JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md; KD 544d7a97fa075fe62848ae1cf27acdb9bdc7df19:research_notes/portable_direct/R284KD_FINITE_BRIDGE_AND_MODULAR_FALLBACK_20261128.md (root interval as carried in KM); KM 08f07c05a0d67a4ca8c7bb616d8166ff0ec2cf4f:research_notes/portable_direct/R284KM_HALF_INTEGER_POLE_LIFTS_20261128.md. Compare KG 0c5c18b5e6725fcdebad3c12b9ebec33659ba12f (u=0 and n=-1) and JO 81cc0f06a4cf0209733a50284362f9bb1e8aded9 (negative pole offsets); neither of those stated formulas is the n=0 odd fiber below. No exhaustive novelty or independent review claim. All formulas use JR full observers with E.

## 1. Exact regular fiber at n=0 (odd d)

For odd integer d>=3 put q0=-d/2, u=d/2, n=2q+d=0. Write r=R_u(d), s=R_u(d-1). Both are nonzero since u is half-integral and denominators are positive. Exactly R_0(0)=1, R_0(l)=0 for l>=1. Hence V=(d+1)r and Q=d*s, with s/r=(3d+4)/(2-d). Only k=d and k=d-1 contribute to A, so with J=d(d+1):
 A/r=[(-d/2)(3d/2+2)(d+1)+(1-d/2)(3d/2+1)*d*(3d+4)/(2-d)]/J
     =(2d+1)(3d+4)/(4(d+1)).
 The full E/r=-d(2d+3)/(4(d+1)), so W/r=d+1 exactly.
 Z/r=q0*A/r+V/r+Q/r
     =-(2d+1)(3d^3+6d^2+16d+16)/(8(d-2)(d+1)).
Substitute in C=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2. This gives
 C(q0,d)/r^2=F8(d)/(4(d-2)(d+1)^2),
 F8(d)=6d^2(d+1)^5(3d+4)+(2d+1)^2(3d^3+6d^2+16d+16)^2
      =54d^8+294d^7+981d^6+2136d^5+3406d^4+4266d^3+3544d^2+1536d+256.
In particular F8>0, and the full endpoint contribution is needed for the W cancellation. This is a fixed-degree observer obtained by exact support compression, not a small-residual approximation.

Let A_d=prod_{i=0}^{d-1}(d-2i) (signed odd integer), D_n=(d+2)!/2, D=JL D_u D_n, L=2. Since D_u*r=2^{-d}A_d, the integer-polynomial carrier satisfies the exact dyadic identity
 P_d(-d/2) = d^2 ((d+2)!)^2 A_d^2 F8(d) / [2^{2d+2}(d-2)].
For d odd>=3, each prime factor outside F8 on the right is <=d+2 (the denominator d-2 also has this property). Thus for every odd prime p>d+2,
 v_p(P_d(-d/2))=v_p(F8(d)).
For even d, support may vanish; no odd-fiber formula is asserted there.

## 2. Unbounded necessary condition and exception count

P_d belongs to Z[q]; G(h)=P_d((h-d)/2) belongs to Z[1/2][h]. For a legal integer root q, set h=2q+d. Polynomial integrality gives G(h)-G(0) in h Z[1/2]. Therefore
 p>d+2, p|h => v_p(h)<=v_p(F8(d)).
This remains valid when a rational observer has a pole modulo p: the proof uses the cleared polynomial, not division by a nonunit. If p does not divide F8 the entire p-fiber is excluded. In fact v_p(P_d(q))=v_p(F8(d)) whenever v_p(h)>v_p(F8(d)).
The coefficientwise comparison F8(d)<(2d+3)^8 gives at most seven distinct exceptional primes p>2d+3 for every odd d>=3. Also F8(d)<64d^8 for d>=81 (divide by d^8, bound every positive inverse power at d=81); since d>64, nine primes >d+2 cannot divide it, hence at most eight exceptional primes above the LOWER threshold d+2. The statement is about possible prime factors, not actual integer roots.

## 3. Enlarged prime-band lift with parity

If d>=81, KD's unique legal real root lies in 4d^2/5<=q<=4d^2/3. For p>d+2 dividing h, h<=8d^2/3+d<3p^2. If p|F8(d), let b=G(0)/p mod p and a=G'(0) mod p. Then G(pt)/p=b+at mod p. As in KM, calculate a,b from G(0),G(p) mod p^2, using full integer carrier. If a is nonzero, t belongs to one residue class mod p and 0<t<3p. Since d odd, t odd. Among at most three representatives separated by odd p there are at most two odd representatives. For p>2d+3, h<p^2, so at most one representative as in KM. If a=0,b!=0 all lifts excluded; a=b=0 remains open at this order. Thus we enlarge the proven p threshold from the earlier n=-2 coordinate's 2d+3 to d+2 in this new coordinate, with at most two candidate evaluations for simple lifts. No probabilistic independence. p not dividing F8 requires no O(d) carrier computation; Horner cost is eight modular multiply-adds given d,p. Exact evaluation of exceptional lifts is O(d) modular operations; bit cost depends on modulus, and finding candidate prime factors is separate.

## 4. Actual finite computation

Exact dyadically scaled full carrier verifies the identity for all odd 5<=d<=301 (149 cases). The scan covers all odd 81<=d<=2001 and all primes d+2<p<=5d, enumerated by Eratosthenes. Every exceptional prime is tested at p^2; all simple candidates in the KD interval are tested at p^3. Number-valued loop bounds and integer q recovery are within exact safe integer range (d<=2001, p<=10005). All carrier operations BigInt; no floating point sign decisions. Results below. No claim of uniform nondegeneracy beyond tested domain. The new coordinate does not require that h have such a prime; full integer exclusion stays at d<=3200 (KL), unbounded problem open.

```json
{
  "exact": 149,
  "pairs": 490143,
  "exception": 191,
  "largePairs": 358006,
  "largeExceptions": 109,
  "simple": 191,
  "singularNoLift": 0,
  "singularAllLift": 0,
  "outside": 163,
  "insideFibers": 28,
  "insideCandidates": 28,
  "p3excluded": 28,
  "unresolved": 0,
  "rows": [
    [
      135,
      199,
      17942,
      "6573766"
    ],
    [
      143,
      271,
      20931,
      "3818932"
    ],
    [
      339,
      443,
      119662,
      "73789624"
    ],
    [
      425,
      1021,
      199393,
      "869395794"
    ],
    [
      815,
      2011,
      690371,
      "1888604507"
    ],
    [
      817,
      1109,
      576826,
      "964226704"
    ],
    [
      833,
      953,
      665254,
      "76289556"
    ],
    [
      1169,
      1493,
      1142307,
      "2342730499"
    ],
    [
      1215,
      1609,
      1902035,
      "3608900114"
    ],
    [
      1279,
      1741,
      1802166,
      "951759434"
    ],
    [
      1303,
      2251,
      2021872,
      "2553768504"
    ],
    [
      1313,
      1453,
      1936919,
      "755812822"
    ],
    [
      1327,
      3779,
      1970085,
      "52367843947"
    ],
    [
      1393,
      3821,
      2461938,
      "53669750716"
    ],
    [
      1419,
      2423,
      1808060,
      "8107752949"
    ],
    [
      1447,
      1889,
      2338803,
      "4260575274"
    ],
    [
      1461,
      1723,
      2081515,
      "11874916"
    ],
    [
      1515,
      2857,
      2854814,
      "5974912668"
    ],
    [
      1547,
      2087,
      2861547,
      "8475937274"
    ],
    [
      1593,
      1667,
      2235484,
      "194522230"
    ],
    [
      1605,
      1879,
      2764146,
      "314227049"
    ],
    [
      1619,
      2383,
      3169772,
      "12135358393"
    ],
    [
      1655,
      1861,
      3292212,
      "1603517623"
    ],
    [
      1697,
      2687,
      2722426,
      "8259644536"
    ],
    [
      1699,
      5381,
      3176631,
      "8223265724"
    ],
    [
      1771,
      4253,
      2999606,
      "55439747585"
    ],
    [
      1825,
      1873,
      3708564,
      "2031206691"
    ],
    [
      1909,
      2423,
      3671102,
      "13280041398"
    ]
  ]
}
```

## Executed JavaScript

```javascript
function experiment(){
 const coeff=[54n,294n,981n,2136n,3406n,4266n,3544n,1536n,256n];
 const f=d=>coeff.reduce((v,c)=>v*d+c,0n);
 function scale(v,d){let tail=Array(d+1).fill(1n),z=1n,out=[];for(let k=d-1;k>=0;k--)tail[k]=tail[k+1]*(v+2n*BigInt(k+3));for(let k=0;k<=d;k++){out.push(z*tail[k]);z*=v-2n*BigInt(k)}return [tail[0],out]}
 function exactFiber(D){let d=BigInt(D),[,U]=scale(d,D),[Dn2,N2]=scale(0n,D),power=1n<<d,N=N2.map(x=>x/power),Dn=Dn2/power,J=d*(d+1n),L=2n,V=0n,Q=0n,A=0n;
 for(let k=0;k<=D;k++){let K=BigInt(k),l=d-K,a=(K+1n)*(l+1n)*U[k]*N[Number(l)],b=l?(K+1n)*l*U[k]*N[Number(l-1n)]:0n;V+=a;Q+=b;A+=(d-2n*K)*(d+2n*K+4n)*(a+b)}
 let W8=2n*(L*A-d*d*U[D]*Dn*(2n*d+3n)*2n),Q8=8n*J*L*Q,Z8=L*(-d*A+8n*J*(V+Q));let P=-3n*d*(d+1n)**2n*W8*Q8+32n*(d-2n)*Z8**2n;
 let fact=2n*Dn, rhs=32n*d*d*fact*fact*U[D]**2n*f(d);if(P*(d-2n)!==rhs)throw Error("identity "+D);return true}
 const mod=(x,m)=>(x%m+m)%m;
 function carrier(D,q,M){let d=BigInt(D),u=q+d,n=2n*q+d,J=mod(2n*u*(2n*u+1n),M),L=mod(4n*n+2n,M);
 function sc(v){let tail=Array(D+1).fill(1n),z=1n,out=[];for(let k=D-1;k>=0;k--)tail[k]=mod(tail[k+1]*(v+BigInt(k+3)),M);for(let k=0;k<=D;k++){out.push(mod(z*tail[k],M));z=mod(z*(v-BigInt(k)),M)}return [tail[0],out]}
 let [Du,U]=sc(u),[Dn,N]=sc(n),V=0n,Q=0n,A=0n;
 for(let k=0;k<=D;k++){let K=BigInt(k),l=d-K,a=mod((K+1n)*(l+1n)*U[k]*N[Number(l)],M),b=l?mod((K+1n)*l*U[k]*N[Number(l-1n)],M):0n;V=mod(V+a,M);Q=mod(Q+b,M);A=mod(A+(u-K)*(u+K+2n)*(a+b),M)}
 let W=mod(L*A+u*U[D]*Dn*q*(2n*d+3n)*(n+2n),M),Qn=mod(J*L*Q,M),Z=mod(L*(q*A+J*(V+Q)),M);
 return mod(3n*q*(4n*q+3n*d+1n)**2n*W*Qn-32n*(3n*q+d+1n)*Z*Z,M)}
 function g(d,h,M){return carrier(d,mod((h-BigInt(d))*((M+1n)/2n),M),M)}
 function pow(a,b,m){let x=1n;for(;b;b>>=1n,a=a*a%m)if(b&1n)x=x*a%m;return x}
 const N=10005,prime=Array(N+1).fill(true);prime[0]=prime[1]=false;for(let i=2;i*i<=N;i++)if(prime[i])for(let j=i*i;j<=N;j+=i)prime[j]=false;const ps=prime.map((v,i)=>v?i:0).filter(Boolean);
 let out={exact:0,pairs:0,exception:0,largePairs:0,largeExceptions:0,simple:0,singularNoLift:0,singularAllLift:0,outside:0,insideFibers:0,insideCandidates:0,p3excluded:0,unresolved:0,rows:[]};
 for(let d=5;d<=301;d+=2){exactFiber(d);out.exact++}
 for(let d=81;d<=2001;d+=2){const F=f(BigInt(d)),lo=Math.floor((4*d*d+4)/5),hi=Math.floor(4*d*d/3);for(const p of ps){if(p<=d+2)continue;if(p>5*d)break;out.pairs++;const P=BigInt(p),large=p>2*d+3;if(large)out.largePairs++;
 if(F%P!==0n)continue;out.exception++;if(large)out.largeExceptions++;
 let M=P*P,r=g(d,0n,M),s=g(d,P,M);if(r%P||s%P)throw Error("fiber");
 let a=mod((s-r)/P,P),b=r/P;
 if(!a){if(b)out.singularNoLift++;else out.singularAllLift++;out.rows.push([d,p,String(a),String(b),b?"singular_no_lift":"singular_all_lift"]);continue}
 out.simple++;let t0=Number(mod(-b*pow(a,P-2n,P),P)),hits=0;
 for(let t=t0;t<3*p;t+=p){let q=(p*t-d)/2;if(!t||!Number.isInteger(q)||q<lo||q>hi)continue;
 if(large&&t>=p)throw Error("large bound");
 hits++;out.insideCandidates++;let v=carrier(d,BigInt(q),M*P);if(v%M)throw Error("lift");if(v)out.p3excluded++;else out.unresolved++;out.rows.push([d,p,q,String(v)])}
 if(hits>2)throw Error("parity bound");if(hits)out.insideFibers++;else out.outside++;
 }}
 return out
}
console.log(JSON.stringify(experiment(),null,2));
```

## Next

Combine n=0 and n=-2 with KG/KJ at actual root-adjacent budgets, retaining smooth h and small-prime exceptions. Seek a uniform criterion for the two possible singular lift coefficients; do not infer derivative nonvanishing from finite results. A separate even-d jet at n=0 may already be in KF and must be compared before any new claim. No formal Result, independent review or native transfer.
