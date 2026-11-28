# R284KH — Composite-power jets and integral Hermite block sieve

2026-11-28. Author proof and executed exact BigInt computation, NOT_REVIEWED. Auxiliary arithmetic of R284, not a native spatial transfer. Own recovered open RESEARCHER registration r1-20261124-0256-r284gd-session-v1 (recovery r1-20261128-1200-own-recovery), no formal runs; historical own RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E / TASK_RESEARCH. Current LEASED inventory r1-20261128-1200-owner-inventory still RUNNING at last observation; no shared claim or ownership mutation. Global entry immutable main 2d45984ae46346eddafb1c2a8adea3b1e7b34abd verified (both blob IDs matched fresh main reads). P000 V4/V5, ACTIVE worldview, joint observer and residual contracts, current method and portable protocol read.

Frozen science: KG 0c5c18b5e6725fcdebad3c12b9ebec33659ba12f:research_notes/portable_direct/R284KG_SEXTIC_POLE_FIBER_AND_PRIMITIVE_COMPOSITE_SIEVE_20261128.md; KF dffdb8e6221f1f4820189dfeac8ab40ca704f850:research_notes/portable_direct/R284KF_NEGATIVE_DOUBLE_FIBERS_AND_COMPOSITE_SIEVE_20261128.md; JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md; KD bracket as carried by KG and KF. All hypotheses retained. No new claim about native geometry.

## 1. Whole-composite power sieve

Use exactly JR's cleared carrier P_d = D^2 C and KG's H_d = P_d / (2^kappa G_d (q+d)^2 (4q+2d+1) F_odd F_KE) in Z[q], with J_d = {j integer : (d+1)/3 < j <= d/2}, G_d = product (q+j)^2, kappa=2 floor(d/2)+3+2(d mod 2). All removed factors and D are nonzero on the legal positive budget domain. H=0 is equivalent to C=0 there. Keep the original carrier and removed factors for reconstruction.

For any j in J_d and any positive integer t, set h=q+j and a_i=[X^i] H_d(-j+X), 0<=i<t. Define R_{j,t}(h)=sum_{i<t} a_i h^i. If a legal integer q is a root, then necessarily

    h^t divides R_{j,t}(h).

Proof: ordinary integer polynomial division H_d(-j+X)=R_{j,t}(X)+X^t T(X), T in Z[X]. Evaluate at h. This is a congruence of the entire integer h, without factoring, including primes below 2d+2 and repeated factors. At t=1 it is KG's constraint. Passing order t+1 implies passing t (reduce modulo h^t). When h does not divide R_1 it is already excluded; for larger t, an exact nonzero residue excludes the root. For a prime p dividing h, the test retains simultaneous residues to precision t*v_p(h); no independence assumption. It does not infer an integer zero merely from passing a finite order.

## 2. Exact division of truncated cleared-carrier jets

At q=-j+X, remove the local X^2 factor and write P_d(-j+X)=X^2 B_j(X) H_d(-j+X), where B_j is the remaining KG factor, including 2^kappa. B_j(0) is nonzero by disjoint factors. Compute P mod X^(t+2) using all cleared observations Wn,Qn,Zn (including endpoint) in Z[X]/(X^(t+2)); compute B mod X^t. Recurrence

    a_i = ([X^(i+2)]P - sum_{k=1}^i [X^k]B_j * a_(i-k)) / B_j(0).

Every division is exact in Z by the KG integrality theorem. This avoids inversion of nonunits in Z/h^t and is valid for smooth h. Using prefix/suffix products of linear factors gives O(d*t^2) elementary integer operations with naive truncated multiplication, plus O(t^2) quotient operations; not a bit-complexity claim. Coefficient lengths grow with d, integer exact division and modulus cost must be included for performance comparisons. The computation keeps the full joint polynomial observer up to the declared jet order; no independent branch approximation.

## 3. Integral Hermite block theorem (written proof; higher-order block not executed)

For distinct integers x_i=-j_i and positive multiplicities t_i, put B(X)=product (X-x_i)^t_i. Monic division in Z[X] gives unique remainder R of degree <sum t_i with H=R+B*T. It follows that any integer root q satisfies B(q)|R(q). All individual power tests follow, but the product can retain repeated prime factors lost by taking only the separate conditions. Recover R without expanding H: start R=0, B=1. At each node x_i, solve modulo Y^t_i for coefficients of U(Y) from B(x_i+Y) U(Y)=H(x_i+Y)-R(x_i+Y). B(x_i) !=0 and coefficient recursion over Q is unique. In fact each division is exact in Z: inductively R is the monic remainder for previous B, so H-R=B*T over Z[X]; U is the truncation of T(x_i+Y). Update R <- R+B U(X-x_i), B <- B (X-x_i)^t_i. This preserves all preceding jets and matches the new ones, and degree bound gives the new monic remainder. When moduli are pairwise coprime at q, separate tests and block are equivalent; otherwise the block may be stronger. Abstract strict example H(X)=X(X-2)+4 with nodes 0,2 (t=1) and q=4: H(0)=H(2)=4, individually 4|4 and 2|4, but product 8 does not divide the remainder 4. This demonstrates the mechanism, not a strict-gain R284 example.

Actual preliminary R284 test of t_i=1, first six consecutive nodes, d=81..120: separate and block counts both [67897,17191,3787,797,183,43]; no strict gain in that finite domain. Consecutive-node Newton coefficients were computed by (-1)^k Delta^k H(-j)/k! with exact integrality assertions. Hence the power sieve (rather than first-order block alone) is the discriminating route here. No assertion that block gain occurs on R284.

## 4. Exact executed power-sieve experiment

All 218330 distinct (d,q) in d=81..120 and ceil(4d^2/5)<=q<=floor(4d^2/3). Evaluate first six consecutive j in J_d and t=1..4 using exact BigInt. Rows index number of included nodes, columns index order t; counts are survivors, closed counts count d with zero survivors. Smooth subgroup defined ONLY by q+j_first having no prime factor >2d+2 (trial division by every integer up to bound). No prime-factor assumption in the test itself. Actual output:
```json
{
  "initial": 218330,
  "counts": [
    [
      67897,
      67259,
      43103,
      42550
    ],
    [
      17191,
      16785,
      5833,
      5617
    ],
    [
      3787,
      3660,
      499,
      477
    ],
    [
      797,
      770,
      36,
      34
    ],
    [
      183,
      179,
      0,
      0
    ],
    [
      43,
      43,
      0,
      0
    ]
  ],
  "closed": [
    [
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      8,
      9
    ],
    [
      0,
      0,
      40,
      40
    ],
    [
      10,
      10,
      40,
      40
    ]
  ],
  "smoothInitial": 85799,
  "smoothCounts": [
    [
      67618,
      67258,
      43103,
      42550
    ],
    [
      17108,
      16785,
      5833,
      5617
    ],
    [
      3762,
      3660,
      499,
      477
    ],
    [
      789,
      770,
      36,
      34
    ],
    [
      183,
      179,
      0,
      0
    ],
    [
      43,
      43,
      0,
      0
    ]
  ],
  "firstWitness": {
    "d": 81,
    "q": 5301,
    "j": 28,
    "x": "5329",
    "residue": "25579200"
  }
}
```
Strict witness d=81,q=5301,j=28, h=5329=73^2 (73<164). First-order divisibility passes, order-two residue 25579200=4800*5329 mod 5329^2 is nonzero. Thus v_73(H_d(q))=2, not >=4, with exact exclusion of a smooth-coordinate budget which KG first-order test alone leaves. Counts are only necessary sieve survivors, not roots. All d tested already lie in KD's proven finite interval; no new all-budget d coverage or independent review claimed. The 2nd and 4th power layers need not be equally effective. The computation uses exact low-order polynomial coefficients and no floating point decisions (small range/index arithmetic is exactly representable).

## 5. Replay

Executed source, JavaScript BigInt, no external dependencies.
```javascript
function replay(){
const tmax=4,N=tmax+2;
const z=()=>Array(N).fill(0n), lin=(a,b=0n)=>{let v=z();v[0]=a;v[1]=b;return v};
function add(a,b){return a.map((x,i)=>x+b[i])}
function sc(a,b){return a.map(x=>x*b)}
function mul(a,b){let c=z();for(let i=0;i<N;i++)if(a[i])for(let j=0;j<N-i;j++)if(b[j])c[i+j]+=a[i]*b[j];return c}
function Hjet(d,j){
const D=BigInt(d),q=-BigInt(j),u=q+D,n=2n*q+D,kappa=2*Math.floor(d/2)+3+2*(d%2);
function S(v,s){let tail=Array(d+1);tail[d]=lin(1n);for(let k=d-1;k>=0;k--)tail[k]=mul(tail[k+1],lin(v+BigInt(k+3),s));let f=lin(1n),o=[];for(let k=0;k<=d;k++){o.push(mul(f,tail[k]));f=mul(f,lin(v-BigInt(k),s))}return [tail[0],o]}
const [Du,U]=S(u,1n),[Dn,M]=S(n,2n);let v=z(),b=z(),a=z();
for(let k=0;k<=d;k++){let K=BigInt(k),l=d-k,A=sc(mul(U[k],M[l]),BigInt((k+1)*(l+1))),B=l?sc(mul(U[k],M[l-1]),BigInt((k+1)*l)):z();v=add(v,A);b=add(b,B);a=add(a,mul(mul(lin(u-K,1n),lin(u+K+2n,1n)),add(A,B)))}
let J=mul(lin(2n*u,2n),lin(2n*u+1n,2n)),L=lin(4n*n+2n,8n),Q=mul(mul(J,L),b),W=add(mul(L,a),sc(mul(mul(mul(mul(lin(u,1n),U[d]),Dn),lin(q,1n)),lin(n+2n,2n)),2n*D+3n)),Z=mul(L,add(mul(lin(q,1n),a),mul(J,add(v,b))));
const F=lin(4n*q+3n*D+1n,4n),P=add(sc(mul(mul(mul(lin(q,1n),mul(F,F)),W),Q),3n),sc(mul(lin(3n*q+D+1n,3n),mul(Z,Z)),-32n));
if(P[0]||P[1])throw Error("fiber");
let B=sc(mul(mul(lin(q+D,1n),lin(q+D,1n)),lin(4n*q+2n*D+1n,4n)),1n<<BigInt(kappa));
if(d%2)B=mul(B,lin(q+(D+1n)/2n,1n));if(d%3===2)B=mul(B,lin(q+(D+1n)/3n,1n));
for(let k=Math.floor((d+1)/3)+1;k<=Math.floor(d/2);k++)if(k!==j){let f=lin(BigInt(k-j),1n);B=mul(B,mul(f,f))}
let H=[];for(let i=0;i<tmax;i++){let r=P[i+2];for(let k=1;k<=i;k++)r-=B[k]*H[i-k];if(r%B[0])throw Error("quotient");H.push(r/B[0])}return H;
}
const grid=()=>Array.from({length:6},()=>[0,0,0,0]);
let R={initial:0,counts:grid(),closed:grid(),smoothInitial:0,smoothCounts:grid(),firstWitness:null};
function test(H,x){let M=1n,r=0n,pass=0;for(let k=0;k<tmax;k++){r+=H[k]*M;M*=x;if(r%M)break;pass++}return pass}
function smooth(n,B){for(let p=2;p<=B && n>1;p++)while(n%p===0)n/=p;return n===1}
for(let d=81;d<=120;d++){
let j=Math.floor((d+1)/3)+1,hs=Array.from({length:6},(_,k)=>Hjet(d,j+k)),cnt=grid();
for(let q=Math.floor((4*d*d+4)/5);q<=Math.floor(4*d*d/3);q++){
R.initial++;let x=BigInt(q+j),s=smooth(q+j,2*d+2),p=tmax;if(s)R.smoothInitial++;
for(let k=0;k<6;k++){p=Math.min(p,test(hs[k],x+BigInt(k)));if(k===0&&p===1&&!R.firstWitness){let M=x*x;R.firstWitness={d,q,j,x:String(x),residue:String(((hs[0][0]+x*hs[0][1])%M+M)%M)}}
for(let i=0;i<p;i++){cnt[k][i]++;if(s)R.smoothCounts[k][i]++}if(!p)break}
}
for(let k=0;k<6;k++)for(let i=0;i<4;i++){R.counts[k][i]+=cnt[k][i];if(!cnt[k][i])R.closed[k][i]++}
}
return R
}
console.log(JSON.stringify(replay(), null, 2));
```

## Next

Test adaptive high-order composite jets and joint Hermite blocks on genuinely unresolved d>3000, paying bit-cost and checking actual survivors, and seek deterministic unbounded obstruction across distinct whole-composite coordinates. In particular investigate p-adic fixed divisors (distinct from polynomial content) and normalized jets that remove forced divisibility before taking the composite modulus. Preserve full H and original carrier. KD all-budget coverage 3..3000 and JY/JZ sparsity remain at their prior scopes. All-parameter integer exclusion remains open.
