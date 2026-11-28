# R284KO — Fixed-support family and even second-branch decic

2026-11-28. Author derivation and exact BigInt computations; NOT_REVIEWED. Auxiliary arithmetic of R284, not native spatial transfer. Existing own activity RA-B82240E8488EF5A1DA5186C4, EM-DIRECT-0C386E / TASK_RESEARCH. Own metadata recovery r1-20261128-1900-own-recovery returned original open registration, no own runs; no shared Task acquisition or mutation. LEASED query r1-20261128-1900-owner-inventory was RUNNING at last prepublication observation; no inference of empty ownership. Global entry files read and rechecked at immutable main e79bfcdfbba44967b44d8560f1c4995812f21218; EM normative entry and portable protocol at 0198337ee4c5643645f4407ad0f2001cf6698ee8. P000 V4, Source foundation startup projection, ACTIVE worldview, current method and role entry consulted. Frozen science preserved.

Frozen inputs: JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md (full V,Q,A,E,W,Z,C,P); KD 544d7a97fa075fe62848ae1cf27acdb9bdc7df19:research_notes/portable_direct/R284KD_FINITE_BRIDGE_AND_MODULAR_FALLBACK_20261128.md (unique legal real root, root bracket as carried by KN); KN 69a79410f72419172b4ca7d102ebd7354e319b77:research_notes/portable_direct/R284KN_ODD_ZERO_SECOND_BRANCH_OCTIC_AND_LIFTS_20261128.md. Compare KF dffdb8e6221f1f4820189dfeac8ab40ca704f850:research_notes/portable_direct/R284KF_NEGATIVE_DOUBLE_FIBERS_AND_COMPOSITE_SIEVE_20261128.md (integer negative support-zero fibers). This continuation changes n=0 odd d to a fixed nonnegative n with opposite parity, not the integer negative zero family. No exhaustive novelty claim.

## 1. Fixed-support rational compression theorem

Keep the full JR definitions. Fix an integer s>=0, let d>=max(3,s+2) be an integer with d+s odd, and take q0=(s-d)/2, u=(d+s)/2, n=s. Put r=R_u(d), which is nonzero since u is half-integral. For i=0..s+1 define rho_i=R_u(d-i)/r. Exact backward recurrence gives

rho_i = product_{j=0}^{i-1} (3d+s+4-2j)/(s-d+2+2j).

There are no zero denominators by parity. Since R_s(i)=0 for i>s, the full V/r,Q/r are the sums of
v_i=(d-i+1)(i+1)rho_i R_s(i),
b_i=(d-i+1)i rho_i R_s(i-1) (zero at i=0),
over i=0..s+1. A/r is the sum of (u-d+i)(u+d-i+2)(v_i+b_i)/J, J=(d+s)(d+s+1). E/r=(u-d)(2d+3)(s+2)/(2(2u+1)(4s+2)). Then W/r=A/r+E/r and Z/r=q0 A/r+Q/r+V/r. All terms including endpoint retained.

Let B_s(d)=product_{j=0}^{s}(s-d+2+2j), H_s=J B_s. In a polynomial indeterminate d, V/r and Q/r have denominator B_s, numerator degree <=s+2; A/r and W/r have denominator H_s, numerator degree <=s+4; Z/r denominator H_s, numerator degree <=s+5. All constants lie in the localization of Z at primes <=2s+2: R_s(i) denominators <=2s+2 for nonzero terms; 4s+2 has prime factors <=2s+1 (s=0 gives 2); halves and quarters are included. Consequently a positive integer K_s with only those prime factors clears the constant denominators of H_s^2 C(q0,d)/r^2. Define N_s(d)=K_s H_s(d)^2 C(q0,d)/r^2 as the resulting integer polynomial. Degree <=2s+11: the first term multiplies two numerator degrees <=s+4 by degree 3, second degree <=2s+10 by degree 1. This is fixed degree for each s, without d-dependent summation.

For every prime p>d+s+2, J, B_s, L=4s+2, D_s=product_{i=0}^{d-1}(s+i+3), K_s, and D_u*r=2^-d product_{i=0}^{d-1}(d+s-2i) are p-units. Indeed the absolute B_s factors are <=d+s+2 since d>=s+2, and all nonzero numerator factors have absolute value <=d+s. Hence v_p(P_d(q0))=v_p(N_s(d)) (infinite if zero). G(h)=P_d((h+s-d)/2) in Z[1/2][h]; G(h)-G(0) divisible by h there. Any legal integer zero must satisfy, for h=2q+d-s,

p>d+s+2, p|h => v_p(h)<=v_p(N_s(d)).

This is an unbounded fixed-support family, not merely the two explicit cases. Nonzero N_s(d) is needed for a useful restriction; no uniform nonvanishing for all s is proved. The construction does not assert that every h has a qualifying prime.

## 2. Explicit even-d fiber, s=1

For even d>=6 set q0=(1-d)/2, u=(d+1)/2, n=1, r=R_u(d). R_1(1)=1/4, higher terms zero; rho_1=(3d+5)/(3-d), rho_2=rho_1*(3d+3)/(5-d). Substitute the three support positions from section 1. Direct simplification gives

V/r=-(d^2+9d+6)/(2(d-3)),
Q/r=(3d+5)(d^2+10d-3)/(2(d-5)(d-3)),
A/r=-(3d+5)(2d^2+13d+3)/(8(d-3)(d+2)),
E/r=-(d-1)(2d+3)/(8(d+2)),
W/r=-(d+3)(2d+1)/(2(d-3)),
Z/r=(6d^5+29d^4+90d^3+952d^2+1680d+315)/(16(d-5)(d-3)(d+2)).

The W cancellation requires the full E. Substitution into JR's C gives

C(q0,d)/r^2=F10(d)/(16(d-5)(d-3)^2(d+2)^2),

F10=72d^10+1218d^9+9823d^8+52530d^7+169258d^6+363894d^5+1209376d^4+3125910d^3+3335166d^2+1060992d+108945.

F10>0. Put A_d=product_{i=0}^{d-1}(d+1-2i). Here J=(d+1)(d+2), L=6, D_n=(d+3)!/6. Thus

P_d(q0)=(d+1)^2 ((d+3)!)^2 A_d^2 F10(d) / [2^(2d+4)(d-5)(d-3)^2].

In particular v_p(P_d(q0))=v_p(F10(d)) for p>d+3. A legal integer zero must satisfy v_p(2q+d-1)<=v_p(F10(d)) for every such prime dividing that coordinate. For d>=81, F10(d)<100d^10: divide by d^10 and bound each positive inverse power at 81 (exact bound checked by F10(81)<100*81^10). Also (d+3)^11/d^10 >= (d+3)(1+30/d)>100. So at most ten distinct exceptional primes above d+3, and at most nine above 2d+3 since (2d+3)^10>100d^10. No restriction for d=4 is claimed.

## 3. Simple lift, parity and computation

For d>=81 KD gives 4d^2/5<=q_d<=4d^2/3. For h=2q+d-1 positive, p>d+3 implies h<3p^2 and p>2d+3 implies h<p^2. If p|F10, compute r0=G(0) mod p^2 and r1=G(p) mod p^2. The lift constraint is b+a*t=0 mod p for h=p*t, where b=r0/p, a=(r1-r0)/p mod p. If a!=0 then t has one residue class modulo p; because d is even, h and t are odd. At most two candidates in the smaller-prime band and at most one above 2d+3; evaluate full carrier at p^3. Singular a=0,b!=0 excludes all; a=b=0 unresolved.

The exact dyadically scaled full carrier checks every even 6<=d<=300. The finite sieve checks every even d in 82..2000 and 3202..4000, every prime d+3<p<=5d by Eratosthenes. All polynomial arithmetic and modular evaluations BigInt, safe integer loop bounds. The exact identity verifier scales each branch by 2^d, W,Q,Z by 2^(2d+3), and P by 2^(4d+7). The following actual output was obtained twice by executing the same code. No independent implementation claim. No uniform derivative nondegeneracy claim, no coverage for smooth coordinates or primes outside the scanned bands. No extension of the full all-budget d<=3200 result from KL. In particular the newer d interval is a partial conditional fiber exclusion.

```json
{
  "exact": 148,
  "ranges": [
    {
      "start": 82,
      "end": 2000,
      "pairs": 489510,
      "exceptions": 197,
      "lowerPairs": 131869,
      "lowerExceptions": 92,
      "simple": 197,
      "singularNoLift": 0,
      "singularAllLift": 0,
      "outside": 162,
      "insideFibers": 35,
      "candidates": 35,
      "p3Excluded": 35,
      "unresolved": 0
    },
    {
      "start": 3202,
      "end": 4000,
      "pairs": 623572,
      "exceptions": 63,
      "lowerPairs": 166828,
      "lowerExceptions": 25,
      "simple": 63,
      "singularNoLift": 0,
      "singularAllLift": 0,
      "outside": 53,
      "insideFibers": 10,
      "candidates": 10,
      "p3Excluded": 10,
      "unresolved": 0
    }
  ],
  "rows": [
    [
      108,
      223,
      13884,
      "5122087"
    ],
    [
      136,
      239,
      15826,
      "5540737"
    ],
    [
      148,
      461,
      20441,
      "3400336"
    ],
    [
      266,
      307,
      92735,
      "10838635"
    ],
    [
      306,
      577,
      112074,
      "50272279"
    ],
    [
      334,
      389,
      131121,
      "7868692"
    ],
    [
      370,
      1123,
      131768,
      "703709982"
    ],
    [
      374,
      541,
      181319,
      "2341448"
    ],
    [
      410,
      433,
      138139,
      "5624670"
    ],
    [
      510,
      601,
      328793,
      "189630525"
    ],
    [
      592,
      971,
      337127,
      "619446537"
    ],
    [
      604,
      2311,
      347504,
      "373850470"
    ],
    [
      632,
      701,
      525084,
      "59459521"
    ],
    [
      848,
      997,
      792690,
      "33796306"
    ],
    [
      850,
      1123,
      708750,
      "1119882552"
    ],
    [
      914,
      1279,
      946643,
      "395873522"
    ],
    [
      922,
      1091,
      917616,
      "1092677958"
    ],
    [
      1018,
      1063,
      965227,
      "1198897109"
    ],
    [
      1018,
      1873,
      1008102,
      "3897531319"
    ],
    [
      1048,
      2143,
      1138481,
      "1437436537"
    ],
    [
      1268,
      1279,
      2121867,
      "983140441"
    ],
    [
      1388,
      1433,
      2236936,
      "809074666"
    ],
    [
      1436,
      1931,
      2670821,
      "6118896801"
    ],
    [
      1458,
      2579,
      2620825,
      "4462982711"
    ],
    [
      1580,
      1607,
      2686918,
      "2461073897"
    ],
    [
      1592,
      2129,
      3204414,
      "6993865063"
    ],
    [
      1600,
      1951,
      2567692,
      "5564958262"
    ],
    [
      1636,
      3119,
      2751700,
      "25419684693"
    ],
    [
      1696,
      2543,
      3509764,
      "15947249634"
    ],
    [
      1708,
      2293,
      3808966,
      "352275883"
    ],
    [
      1790,
      2371,
      3084962,
      "8083919758"
    ],
    [
      1856,
      3491,
      3914229,
      "10822127928"
    ],
    [
      1866,
      3863,
      4207806,
      "55796233291"
    ],
    [
      1882,
      1931,
      3037488,
      "514569018"
    ],
    [
      1926,
      3643,
      4314171,
      "15275437799"
    ],
    [
      3218,
      6679,
      11569759,
      "266940501344"
    ],
    [
      3296,
      7789,
      9621662,
      "321057813132"
    ],
    [
      3332,
      3853,
      14730280,
      "8773754919"
    ],
    [
      3346,
      3583,
      11075172,
      "43738687823"
    ],
    [
      3362,
      5471,
      13853627,
      "129155893915"
    ],
    [
      3470,
      9749,
      15640536,
      "876296469220"
    ],
    [
      3580,
      3967,
      10869774,
      "4500807454"
    ],
    [
      3714,
      8231,
      11188188,
      "422146268391"
    ],
    [
      3766,
      6263,
      17600279,
      "153291960452"
    ],
    [
      3822,
      4339,
      15299573,
      "74178068740"
    ]
  ]
}
```

## Executed JavaScript

```javascript
function experiment(){
const cf=[72n,1218n,9823n,52530n,169258n,363894n,1209376n,3125910n,3335166n,1060992n,108945n], f=d=>cf.reduce((a,c)=>a*d+c,0n);
const mod=(x,m)=>(x%m+m)%m;
function sc(v,D,m=null,step=1n){const r=x=>m?mod(x,m):x;let tail=Array(D+1).fill(1n),z=1n,out=[];for(let k=D-1;k>=0;k--)tail[k]=r(tail[k+1]*(v+step*BigInt(k+3)));for(let k=0;k<=D;k++){out.push(r(z*tail[k]));z=r(z*(v-step*BigInt(k)))}return [tail[0],out]}
function exactFiber(D){let d=BigInt(D),q2=1n-d,u2=d+1n,n2=2n,[,U]=sc(u2,D,null,2n),[Dn,N]=sc(n2,D,null,2n),J=u2*(u2+1n),L=6n,V=0n,Q=0n,A=0n;
for(let k=0;k<=D;k++){let K=BigInt(k),l=d-K,a=(K+1n)*(l+1n)*U[k]*N[Number(l)],b=l?(K+1n)*l*U[k]*N[Number(l-1n)]:0n;V+=a;Q+=b;A+=(u2-2n*K)*(u2+2n*K+4n)*(a+b)}
let W=2n*L*A+u2*U[D]*Dn*(u2-2n*d)*(2n*d+3n)*(n2+4n),Qn=8n*J*L*Q,Z=L*(q2*A+8n*J*(V+Q));
let P=3n*q2*(2n*q2+3n*d+1n)**2n*W*Qn-32n*(3n*q2+2n*d+2n)*Z*Z;
let fac=1n;for(let i=2n;i<=d+3n;i++)fac*=i;
let rhs=(1n<<(2n*d+3n))*(d+1n)**2n*fac**2n*U[D]**2n*f(d);
if(P*(d-5n)*(d-3n)**2n!==rhs)throw Error("exact "+D);
}
function carrier(D,q,M){let d=BigInt(D),u=q+d,n=2n*q+d,J=mod(2n*u*(2n*u+1n),M),L=mod(4n*n+2n,M),[Du,U]=sc(u,D,M),[Dn,N]=sc(n,D,M),V=0n,Q=0n,A=0n;
for(let k=0;k<=D;k++){let K=BigInt(k),l=d-K,a=mod((K+1n)*(l+1n)*U[k]*N[Number(l)],M),b=l?mod((K+1n)*l*U[k]*N[Number(l-1n)],M):0n;V=mod(V+a,M);Q=mod(Q+b,M);A=mod(A+(u-K)*(u+K+2n)*(a+b),M)}
let W=mod(L*A+u*U[D]*Dn*q*(2n*d+3n)*(n+2n),M),Qn=mod(J*L*Q,M),Z=mod(L*(q*A+J*(V+Q)),M);
return mod(3n*q*(4n*q+3n*d+1n)**2n*W*Qn-32n*(3n*q+d+1n)*Z*Z,M)}
function g(d,h,M){return carrier(d,mod((h+1n-BigInt(d))*((M+1n)/2n),M),M)}
function pow(a,b,m){let x=1n;for(;b;b>>=1n,a=a*a%m)if(b&1n)x=x*a%m;return x}
const N=20000,prime=Array(N+1).fill(true);prime[0]=prime[1]=false;for(let i=2;i*i<=N;i++)if(prime[i])for(let j=i*i;j<=N;j+=i)prime[j]=false;const ps=prime.map((v,i)=>v?i:0).filter(Boolean);
let out={exact:0,ranges:[],rows:[]};for(let d=6;d<=300;d+=2){exactFiber(d);out.exact++}
for(const [start,end] of [[82,2000],[3202,4000]]){let r={start,end,pairs:0,exceptions:0,lowerPairs:0,lowerExceptions:0,simple:0,singularNoLift:0,singularAllLift:0,outside:0,insideFibers:0,candidates:0,p3Excluded:0,unresolved:0};
for(let d=start;d<=end;d+=2){let F=f(BigInt(d)),lo=Math.ceil(4*d*d/5),hi=Math.floor(4*d*d/3);for(let p of ps){if(p<=d+3)continue;if(p>5*d)break;r.pairs++;if(p<=2*d+3)r.lowerPairs++;const P=BigInt(p);if(F%P)continue;r.exceptions++;if(p<=2*d+3)r.lowerExceptions++;
let M=P*P,x=g(d,0n,M),y=g(d,P,M);if(x%P||y%P)throw Error("fiber");let a=mod((y-x)/P,P),b=x/P;
if(!a){if(b)r.singularNoLift++;else r.singularAllLift++;out.rows.push([d,p,String(a),String(b),"singular"]);continue}
r.simple++;let t0=Number(mod(-b*pow(a,P-2n,P),P)),hits=0;for(let t=t0;t<3*p;t+=p){let q=(p*t+1-d)/2;if(!t||!Number.isInteger(q)||q<lo||q>hi)continue;hits++;r.candidates++;let v=carrier(d,BigInt(q),M*P);if(v%M)throw Error("lift");if(v)r.p3Excluded++;else r.unresolved++;out.rows.push([d,p,q,String(v)])}if(hits>2)throw Error("parity");if(hits)r.insideFibers++;else r.outside++}}
out.ranges.push(r)}return out}
console.log(JSON.stringify(experiment(),null,2));
```

## Next

Use the fixed-support family to compare small s beyond 1 and derive joint constraints on a short consecutive block of coordinates of common parity. Test actual root-adjacent budgets for d>3200 with exact interval sign or modular certificates, without interpreting smooth-coordinate survival as an equality. Determine whether a fixed finite family of these observers suffices for a uniform theorem; the existence of eligible prime factors is not established. No formal Result, independent review or native transfer.
