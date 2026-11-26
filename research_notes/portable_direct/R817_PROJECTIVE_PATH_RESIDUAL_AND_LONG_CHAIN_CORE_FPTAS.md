# R817 - Projective residual transport, sharp multiplicative path cuts, and degree-paid long-chain core FPTAS

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation, no shared CLAIM/RUN/Result. Researcher EM-DIRECT-82A007 / TASK_RESEARCH, own metadata recovery r3-20261126-r817-own-read returned original successful registration, no run and execution_authorized=false. RUNNING inventory request r3-20261126-r817-running-read remained RUNNING during derivation; do not infer an empty inventory. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint-observer blob 3923890d77a02d84b772f789e6912dd14f220d14 read; generated foundation startup at that pin returned 404, canonical inputs read directly. Global entries at 9a682ac66416b2806d0c9d4ae8298457e31124a6, relevant ACTIVE worldview and policies. Predecessor R816 c895dd303ae751370b0b84bc00e7fd3043a9e780:research_notes/portable_direct/R816_SOFT_SEPARATOR_TRANSPORT_AND_PAID_RESPLITTING.md; R815 b981236f0fa70e0cfdc4e86c9592db68f9f674e5; R813 c6a2b95f767b8cf8316c207ec103cb86130e78d1. This is a fixed-charge nonnegative auxiliary Port occupancy/parity observer, not a native BRC phase computation. All signed/native matrices, branch provenance, time order, common depth and original interface data are retained. The finite computation below concerns the auxiliary rational tensor contraction only.

## 1. From real additive transport to projective transport

Use R813 h_B implicit joint interface observers and shared factors g_v=1-delta_v prod z_{Bv}. Consider a two-terminal path in the factor-incidence graph, with no external incidence at its internal nodes after summing independent attached tree branches. Terminal variables are the two original binary incidence bits; external tensors and cycles are arbitrary nonnegative. Local internal group matrices N_i may contain zeros and have arbitrary correlation. At every traversed shared factor absorb off-path messages; by R816 its nonnegative matrix has form A_i [[1,1],[1,a_i]], 1-delta_i<=a_i<=1. If the path has a zero local tensor the entire contraction is zero; otherwise each A_i>0 and N_i is nonzero. After scalar extraction the exact two-terminal matrix is M=N_0 S_1 N_1 ... S_l N_l, l>=1, S_i=[[1,1],[1,a_i]], N_i>=0. Endpoint unary weights may be included. The support of M is rectangular: after S_1 every surviving input row is positive, and through each nonzero N and positive S subsequent surviving rows have identical support. This proves positivity on the Cartesian product of active rows and active columns. If either endpoint has only one active state, M is rank one and no approximation is needed.

For a nonnegative 2x2 matrix L=[[a,b],[c,d]] with both columns nonzero, the action on positive row ratios r is f(r)=(ar+c)/(br+d). Its logarithmic derivative is
 |d log f(r)/d log r|=|ad-bc|r/[(ar+c)(br+d)].
It is <=1 by expansion of the denominator. For all-positive entries its maximum is
 kappa(L)=|sqrt(ad)-sqrt(bc)|/(sqrt(ad)+sqrt(bc)),
by minimizing ab r+cd/r at r=sqrt(cd/ab). For a missing column the map is constant at a boundary ratio and the path subsequently has proportional surviving rows; one can handle that case exactly. For rank-one L with positive rows and columns the derivative is zero. Thus for full positive M the logarithmic ratio map of the product has derivative bounded by the product of the individual bounds (chain rule on positive ratios; boundary inputs by continuity, and a rank collapse is exact). In particular
 kappa(M) <= product_i kappa(S_i) <= rho:=product_i delta_i/(4-3delta_i).
Here the last inequality is R816's rational bound; the factor A_i cancels. Write R_M=max(M00 M11/(M01 M10), its reciprocal), and K=(1+rho)/(1-rho). The derivative identity implies
 R_M <= K^2.                                             (1)
For actual Port shared vertices d_i>=2, delta_i<=1/32, so rho<=125^(-l). This is stronger than an additive conditional-probability bound for rare events: it controls the cross ratio even with arbitrarily nonuniform external likelihoods. It applies to the path matrix, not merely to an unconditional forest measure.

## 2. Sharp multiplicative rank-one observer cut

For positive M, the optimal one-sided rank-one certificate A<=M<=K_* A entrywise is K_*=sqrt(R_M). Proof: if A is rank one and positive, its cross ratio is 1; the cross ratio of M/A is between K_*^(-2) and K_*^2, so K_*>=sqrt(R_M). Relabel one column if necessary to arrange r=M00 M11/(M01 M10)>=1. Keeping off-diagonal entries and reducing both diagonal entries by sqrt(r) gives a rank-one matrix attaining equality. The same lower bound is necessary for a uniform sandwich over all nonnegative external environments, since each entry is individually selectable by unary pinnings.

For a rational construction with the certified rational K in (1), put q=min(K,r), keep both off-diagonal entries, set A00=M00/q, A11=M11*q/r. Then A00 A11=M01 M10; both ratios M00/A00=q and M11/A11=r/q lie in [1,K]. Undo any relabeling. This achieves A<=M<=K A with rational factors, including a zero residual (K=1). On rectangular support with a missing row/column simply take A=M and K=1. Nonnegative rank-one A can be factored by choosing one nonzero pivot and taking its column and scaled row.

For any collection of disjoint path interiors, replace each contracted M_e by A_e, retaining the exact original matrix and repair ratio as separate data. For every nonnegative external weight, including arbitrary cycles and external pins, pointwise multiplication and summation prove
 Zhat <= Z <= K_tot Zhat, K_tot=product_e K_e.              (2)
The same inequalities hold for any external event E numerator, hence for positive probabilities K_tot^(-1) P_hat(E)<=P(E)<=K_tot P_hat(E); zeros are preserved. Internal path queries use the original tensor, not this endpoint approximation. If the selected paths break the remaining incidence graph into forests, their rank-one unary factors permit exact R813 contraction. For l_e>=l and p>=1 cuts, K_e-1<=2/(125^l-1). For 0<epsilon<=1, 125^l>=1+4p/epsilon implies K_tot<=exp(epsilon/2)<=1+epsilon, yielding a relative epsilon result for any such supplied decomposition. This one-shot approximation has a precision-dependent length requirement and is not asserted to be an FPTAS for every epsilon on a fixed graph class merely from that requirement.

## 3. Exact one-entry residual and a new FPTAS for cyclic cores

Avoid dropping any path residual: for positive M choose a column ordering making r=M00 M11/(M01 M10)<=1. Set B00=M00, B01=M01, B10=M10, B11=M01 M10/M00. Then B is rational positive rank one and
 M(x,y)=B(x,y)(1-D I_{x=1,y=1}), D=1-r,
with the indicator's original bit values restored after undoing the column permutation. By (1),
 0<=D<=1-K^(-2)=4rho/(1+rho)^2<=4*125^(-l).               (3)
If support is deficient or rank one, absorb its exact unary factors, with D=0. All matrices and residuals may be recovered exactly; no signed-phase claim. Observe the distinction between the sharp approximate cut in section 2 and the exact one-entry residual representation here.

Suppose the supplied (or polynomially constructed) factor graph decomposition consists of disjoint core groups and internally disjoint two-terminal paths joining distinct core groups, after independent pendant trees are absorbed. No remaining coupling other than these paths; core-group internal interface tables may have arbitrary correlations and zeros, with exact polynomial unary-weighted/pinned oracle as in R813 (e.g. each group has logarithmic cycle rank or supplied logarithmic treewidth). Degree-2 path nodes can be contracted using four oracle calls per group and ordinary finite sum/product of exact occupancy weights. All edge groups and fixed charge assignments are the original R813 ones; no global parity change. Original fixed-charge infeasibility gives zero. A zero path gives zero. Once the B factors are absorbed into unary weights at the core groups, the base measure is a product of independent core groups, each retaining its full joint interface distribution. Its partition Z0 is the product of exact local oracle values. If Z0=0 the exact Z is zero; otherwise
 Z/Z0=E0 product_{e}(1-D_e I_e).
Here I_e is an event specifying two incidence bit values, not necessarily both 1; the R815 proof only uses 0<=I_e<=1 and exact moment factorization. Its dependency graph is the line graph of the core multigraph: two residuals can be dependent only if they touch a common core group. Parallel paths are permitted and may only reduce degree from the sum upper bound h_e<=deg(u)+deg(v)-2. Each joint moment of any chosen residual subset is exactly a product of local pinned oracle ratios, with conflicting pins giving zero. In particular no explicit 2^b interface table is required.

Reuse R815's weighted zero-free and enumeration theorem: choose c_e=max(1,ceil(h_e/4)), R=5/4, q=1/9. An exact, polynomially verifiable sufficient test is
 D_e (5/4)^c_e <= (1/9)(8/9)^(2h_e).                     (4)
Then h_e<=4c_e, so connected supports of cost <=k are enumerable in O(n 2^(4k) poly(N)), and their log coefficients computed by R815's exact moment/Mobius formula. The R815 log tail <=(n/2)(4/5)^k gives a deterministic FPTAS for all 0<epsilon<=1 with k=O(log((n+1)/epsilon)); n is the number of nonzero residual paths. This covers zero or nonzero feasible charge. Polynomial bit complexity: oracle messages are finite sums of products over disjoint original local factors, with rational denominator bit sizes bounded by original explicit input size; each path has four such entries, and its pivot divisions and D use only a constant number of these entries. Each core unary-weight product contains each path factor once; across the graph these rational lengths remain polynomial. R815's polynomially many order-k rational coefficient operations, tail and certified exponential evaluation complete the full cost, with no epsilon-dependent topology search. If no residual path remains, contraction is exact.

A simple degree-paid length condition (independent of epsilon) implying (4) uniformly is
 l_e >= 1+ceil(max(0,h_e-4)/16).                           (5)
Let t=ceil(max(0,h_e-4)/16); h_e<=4+16t, c_e<=1+4t. By (3) the left side of (4) is at most (1/25)*(5/256)^t. The right side is at least (1/9)(8/9)^8*((8/9)^32)^t. Both rational inequalities 1/25 <= (1/9)(8/9)^8 and 5/256 <= (8/9)^32 follow by integer cross multiplication. This proves (5) for every h, without a maximum degree assumption. The constants are sufficient, not claimed optimal. The direct actual D test (4) is often stronger.

Explicit physical topology family: take any finite loopless core graph, one retained cycle B_u of length at least max(3,deg(u)) per core vertex, using distinct cycle vertices for the incidences of the core edges. Connect each pair of incidence vertices with a private outside-J road chain of sufficient length to give l_e traversed shared factors (at least two, since both endpoints are shared); internal road groups are singletons, internal chain vertices have original road degree two, endpoints three. These original graphs are simple when distinct incidence vertices are used. Every retained block has cycle rank one, unbounded interface count is permitted, and all core graph degrees and cycle counts may grow. The construction and the path oracle are polynomial in the explicitly supplied road graph (or in the core graph with chain lengths given by (5)). For every feasible fixed charge, (3)-(5) prove FPTAS on this family. When all shared factors are expanded directly, a core block can generate a large dependency clique despite each original degree being only three; after exact chain contraction the residual degree is paid by path length. This gives a separate route around that obstruction, not a claim that no previous algorithm could handle this family.

## 4. Exact verification and next problem

The deterministic JavaScript BigInt program below was executed. It covers all 225 nonzero binary 2x2 endpoint matrix pairs for a single soft factor, 720 nonuniform seeded chains (including zeros, multiple soft factors), 6 long chains up to 512 soft factors, and 300 cyclic-core chain matrices. It compares exact cross ratio bounds, rational rank-one sandwich, exact one-entry factorization, and exact global contraction with each of six single-port pins or none in 100 cyclic-core configurations. The degree certificate is checked for all h=0,...,1024; general h follows the proof. Chain and core tests are abstract nonnegative interface instances, not asserted to be complete native Port or BRC phase experiments. The physical topology family and complexity proof are analytical; no end-to-end production FPTAS benchmark or independent review. A first low-bit pseudo-random draft also passed but final evidence uses high bits as below.

```json
{
  "stats": {
    "chains": 1251,
    "zeroSupport": 1251,
    "crossRatio": 1035,
    "rankOne": 2502,
    "exactFactor": 1035,
    "globalSandwich": 700,
    "globalFactor": 700,
    "degreeCertificate": 1025
  },
  "checks": 8248,
  "long": [
    {
      "l": 1,
      "maxEntryBits": 6,
      "certifiedExcess": "2/(125^1-1)"
    },
    {
      "l": 4,
      "maxEntryBits": 23,
      "certifiedExcess": "2/(125^4-1)"
    },
    {
      "l": 16,
      "maxEntryBits": 95,
      "certifiedExcess": "2/(125^16-1)"
    },
    {
      "l": 64,
      "maxEntryBits": 383,
      "certifiedExcess": "2/(125^64-1)"
    },
    {
      "l": 256,
      "maxEntryBits": 1533,
      "certifiedExcess": "2/(125^256-1)"
    },
    {
      "l": 512,
      "maxEntryBits": 3066,
      "certifiedExcess": "2/(125^512-1)"
    }
  ]
}
```

```javascript
function verify(){
 const st={chains:0,zeroSupport:0,crossRatio:0,rankOne:0,exactFactor:0,globalSandwich:0,globalFactor:0,degreeCertificate:0};
 function ck(ok,k){if(!ok)throw Error(k);st[k]++}
 const mul=(m,n)=>[m[0]*n[0]+m[1]*n[2],m[0]*n[1]+m[1]*n[3],m[2]*n[0]+m[3]*n[2],m[2]*n[1]+m[3]*n[3]];
 const gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a<0n?-a:a};
 const F=(a,b=1n)=>{if(b===0n)throw Error("zero denominator");if(b<0n){a=-a;b=-b}let g=gcd(a,b);return[a/g,b/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const times=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
 const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
 const le=(a,b)=>a[0]*b[1]<=b[0]*a[1],eq=(a,b)=>le(a,b)&&le(b,a);
 const one=F(1n),zero=F(0n);
 let seed=817;const rnd=()=>((seed=(Math.imul(seed,1664525)+1013904223)>>>0)>>>16);
 const mat=()=>{let a=Array.from({length:4},()=>BigInt(rnd()%8));if(a.every(x=>!x))a[0]=1n;return a};
 function make(l){let M=mat(),p=1n;for(let j=0;j<l;j++){const d=BigInt([32,128,512][rnd()%3]),q=BigInt(rnd()%2);M=mul(mul(M,[d,d,d,d-q]),mat());p*=4n*d-3n;}return{M,p}}
 function checkMatrix(M,p){
  const row=[M[0]+M[1]>0n,M[2]+M[3]>0n],col=[M[0]+M[2]>0n,M[1]+M[3]>0n];
  ck(M.every((x,i)=>(x>0n)===(row[i>>1]&&col[i&1]))&&row.some(Boolean)&&col.some(Boolean),"zeroSupport");
  const K=F(p+1n,p-1n),kk=times(K,K);let A=M.map(x=>F(x)),B=A.slice(),fac=[one,one,one,one];
  if(M.every(x=>x>0n)){
   let r=F(M[0]*M[3],M[1]*M[2]),flip=!le(one,r);
   if(flip)r=div(one,r);
   ck(le(r,kk),"crossRatio");
   const diag=flip?[1,2]:[0,3],q=le(K,r)?K:r;
   A[diag[0]]=div(A[diag[0]],q);A[diag[1]]=times(A[diag[1]],div(q,r));
   const perm=flip?[0,1,2,3]:[1,0,3,2];
   const [a,b,c,d]=perm;B[d]=F(M[b]*M[c],M[a]);fac[d]=div(F(M[d]),B[d]);
   ck(le(fac[d],one)&&le(div(one,kk),fac[d]),"exactFactor");
  }
  ck(eq(times(A[0],A[3]),times(A[1],A[2]))&&eq(times(B[0],B[3]),times(B[1],B[2])),"rankOne");
  ck(M.every((v,i)=>le(A[i],F(v))&&le(F(v),times(K,A[i]))&&eq(F(v),times(B[i],fac[i]))),"rankOne");
  st.chains++;return{M,A,B,fac,K};
 }
 for(let a=1;a<16;a++)for(let b=1;b<16;b++){const m=x=>Array.from({length:4},(_,i)=>BigInt((x>>i)&1));checkMatrix(mul(mul(m(a),[32n,32n,32n,31n]),m(b)),125n)}
 for(const l of [1,2,3,5,8,16])for(let i=0;i<120;i++){let {M,p}=make(l);checkMatrix(M,p)}
 const long=[];
 for(const l of [1,4,16,64,256,512]){
  let M=[1n,0n,0n,1n];for(let i=0;i<l;i++)M=mul(M,[32n,32n,32n,31n]);
  const p=125n**BigInt(l);checkMatrix(M,p);long.push({l,maxEntryBits:M.reduce((a,b)=>a>b?a:b).toString(2).length,certifiedExcess:"2/(125^"+l+"-1)"});
 }
 for(let rep=0;rep<100;rep++){
  const path=Array.from({length:3},(_,i)=>{let {M,p}=make(1+(rep+i)%5);return checkMatrix(M,p)});
  const tabs=[mat(),mat(),mat()],ends=[[0,2],[3,4],[5,1]];
  let K=one;for(const x of path)K=times(K,x.K);
  for(const pin of [-1,0,1,2,3,4,5]){
   let Z=zero,Y=zero,E=zero;
   for(let x=0;x<64;x++){
    if(pin>=0&&!((x>>pin)&1))continue;
    let w=one;for(let i=0;i<3;i++)w=times(w,F(tabs[i][(x>>(2*i))&3]));
    let z=w,y=w,e=w;
    for(let j=0;j<3;j++){let [a,b]=ends[j],i=2*((x>>a)&1)+((x>>b)&1);z=times(z,F(path[j].M[i]));y=times(y,path[j].A[i]);e=times(e,times(path[j].B[i],path[j].fac[i]))}
    Z=add(Z,z);Y=add(Y,y);E=add(E,e);
   }
   ck(le(Y,Z)&&le(Z,times(K,Y)),"globalSandwich");ck(eq(Z,E),"globalFactor");
  }
 }
 for(let h=0;h<=1024;h++){const c=Math.max(1,Math.ceil(h/4)),l=1+Math.ceil(Math.max(0,h-4)/16);
  ck(4n*5n**BigInt(c)*9n**BigInt(2*h+1)<=125n**BigInt(l)*4n**BigInt(c)*8n**BigInt(2*h),"degreeCertificate");
 }
 return {stats:st,checks:Object.values(st).reduce((a,b)=>a+b,0)-st.chains,long};
}
console.log(JSON.stringify(verify(),null,2));
```

Next: extend the exact residual extraction to branching separators (multi-terminal tensors) with a controlled factorization error or zero-free expansion that charges Steiner-tree soft distances; compare with direct R815 condition and seek a polynomial certificate for selecting useful core/path decompositions in general Port networks. General complete Port FPTAS remains open.
