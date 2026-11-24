# R775 — Rank-one complete target spectrum and universal-reserve overhead

2026-11-25. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Continuation of R774 (b96e1401092ff2081dd239ba1583253e4b7191b2:research_notes/portable_direct/R774_SYNDROME_T_JOIN_POINT_RESERVE.md) and R773 (8c9c1a69883a9d97653bf131414ab20423a0f57f:research_notes/portable_direct/R773_ALL_RANK_HALL_DEFICIT_RESERVE.md). Scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 unchanged. Read frozen p000_reality_foundation.json (blob dc84bdae6595b5e237a2ad50d8b21916adb2e447), joint relation contract (3923890d77a02d84b772f789e6912dd14f220d14), weighted BRC substrate (f375a059fa4af8c6eefaddb4d4a8689a0c063674), ACTIVE worldview and current portable/continuation and relevant account rules. Frozen Heartbeat companion lookup unavailable; no repin. Existing own session metadata recovery r3-20261125-0020-own-metadata-v1 confirms original registration SUCCEEDED, no runs, execution_authorized=false; owner inventory r3-20261125-0020-owner-read-v1 last observed RUNNING before publication. No shared claim or formal Result. Boolean auxiliary observer only; retain native signed, ordered, provenance, weighted amplitude and common-depth carriers separately.

## 1. Exact formula

Use R774's V_i=F2^2, S(0)={0}, S(1)=V_i minus {0}, S(2)=V_i, P(p)=product S(p_i). Target w is any representative of the quotient class. With nonnegative vertex event prices alpha_i, define k_p^alpha(w)=min sum alpha_i t_i over t such that q(P(p))+q(w) subset q(P(t)). Unit prices give k_p(w).

Consider a rank-one block with K={0,z}, all z_i nonzero (a cycle of length n>=2, including a two-edge parallel cycle). At each vertex define three local costs in event counts:

a_i(b)=p_i+1_{p_i<2 and w_i+b z_i != 0}, b in F2.
c_i=1 if p_i=0 and w_i not in span(z_i); otherwise c_i=2.
f_i=0 if p_i=0 and w_i in span(z_i); otherwise f_i=1.

Let A_b=sum alpha_i a_i(b), C=sum alpha_i c_i, G=max_i alpha_i(c_i-f_i). Then

    k_p^alpha(w)=min(A_0,A_1,C-G).                 (1)

A fixed b candidate uses t_i=a_i(b). The flexible candidate chooses any maximizer j of the gain, uses t_j=f_j, and t_i=c_i for i!=j. For a given prefix state, in that candidate choose b according to the local state at j. These constructions attain the displayed cost. In a general graph with rank-one connected cyclic blocks after deleting bridges, sum (1) over those blocks and the ordinary local formula alpha_i[p_i+1_{p_i<2 and w_i!=0}] at isolated rank-zero vertices. This covers every finite subcubic cactus (including parallel pairs), with arbitrarily many cycles. R774's bridge factorization is reused: a bridge carries no cycle-kernel bit, so both half-port bits must be retained, not just their xor. If a target is supplied in syndrome coordinates instead of a lift, obtain a lift by satisfying local parity using a spanning forest: on non-tree edges pick one half-bit arbitrarily and the other by syndrome, private bits are prescribed, then solve tree half-bits leaf-to-root by parity; component parity ensures root consistency. O(n+m) graph operations. The representative change adds z on a rank-one block, swapping A_0,A_1 and leaving C,G unchanged.

## 2. Proof: two-lift branch obstruction

For fixed reserve t and local prefix state x_i in S(p_i), let L_i(x_i)={b in F2 : x_i+w_i+b z_i in S(t_i)}. Universal feasibility is exactly: for every product choice x, the intersection of all L_i(x_i) is nonempty. Necessarily no L_i(x_i) is empty. If one vertex can force {0} and a DISTINCT vertex can force {1}, independent prefix choices make the intersection empty. Conversely, with nonempty local sets, an empty intersection can only be caused by such a pair. Hence a feasible reserve has either (i) a single b common to every local choice at every vertex, or (ii) all vertices except possibly one always admit both b, and the exceptional vertex admits at least one b for each local choice. Indeed if both singleton labels occur anywhere, their possible forcing sites must be the same unique site. This is an exact Boolean branch test preserving the forall-prefix exists-lift quantifier order, not an independence assumption on joint lift bits.

For (i), the least local t that covers S(p_i)+w_i+bz_i is a_i(b): p=0 yields a singleton, p=1 a translated complement of one point, p=2 the full four points. For (ii), a nonexceptional vertex must contain S(p_i)+w_i+span(z_i); the least t is c_i (only p=0 with an outside-span target gives a two-point set of nonzero states). At the exception, every local state needs at least one permitted lift. For p=0 and w in span, t=0 works; otherwise t=1 works because each z-orbit has two distinct points, at least one nonzero; t=0 fails whenever an outside orbit occurs. This gives f_i. Minimize over the two classes, with nonnegative prices (including zero). This proves (1). The theorem does not depend on R770's graphic full-cover lower bound or R773's Hall proof. More generally it is valid for any linear two-element kernel with nonzero projection at every considered site; zero projections factor independently. Fixed cost, both-admit cost, largest local gain are sufficient for the specified scalar reserve observer. The actual prefix and local data must remain available for witness reconstruction or other observers.

## 3. Exact pointwise worst-case and sharp overhead

Let d_alpha(w)=min over lifts of sum alpha_i 1_{lift_i!=0}, as in R774, and L_p^alpha(w)=max over x in P(p) of d_alpha(x+w). Define H_b=sum alpha_i over vertices with p_i=0 and w_i=b z_i. Then

    L_p^alpha(w)=sum alpha_i-max(H_0,H_1).          (2)

Proof: each site contributes to the two lift costs either (0,alpha_i), (alpha_i,0) or (alpha_i,alpha_i). At a site with p_i>0 an outside-span translated state is available (the set has at least three elements); this simultaneously maximizes both costs. For p_i=0 outside span it is already forced. The only forced missing costs are H_0,H_1. Thus both coordinatewise upper bounds can be attained by one product choice; taking their minimum yields (2).

For unit prices, P=number of sites with p_i>0. The fixed universal overhead is bounded sharply in size:

    0 <= k_p(w)-L_p(w) <= min(P,n-1).               (3)

The lower bound is the pointwise relaxation. Choose the b maximizing H_b. In that fixed b candidate, the zero-stock contribution equals its pointwise maximal contribution, while at each positive-stock site a_i(b) exceeds the maximal point cost (one) by at most one. This proves gap<=P. If P=n, (2) gives L=n and c_i=2,f_i=1 for every site, so (1) yields k<=2n-1. If P<n the P bound already gives n-1. For every n>=2 choose a cycle, p_i=1 and w_i outside span(z_i) at every site. Then A_0=A_1=2n, C=2n, G=1, so k_p(w)=2n-1, while L=n. At target zero, A_0=n, hence k_p(0)=n. Both the universal-overhead gap and the nonzero-terminal surcharge are n-1 in this family. Thus even a single joint relation can produce unbounded fixed-reserve overhead as the cycle grows. Merely retaining the worst pointwise transport cost is insufficient. Formula (1) resolves this gap on every rank-one block. The proof uses the full Boolean branch compatibility and does not infer native signed cancellation.

## 4. Exact reproducible check

Independent direct lifted-set masks: all 3^n inventories and all 2^(2n-1) quotient targets for n=2,3,4,5, with uniform and deterministic nonuniform positive prices; also zero-price family for n<=4. Local coordinates choose z_i=1 by independent local invertible maps; the entire four-state S(p) is invariant under these maps. The direct checker unions the two lifts of each prefix in a mask, translates by each representative and finds the cheapest covering reserve; pointwise worst computed separately by direct prefix enumeration. Every comparison passed, and the unit gap bound was checked. Rows (checks count prefix-target pairs per weight family):

```json
[
  {
    "n": 2,
    "weights": [
      1,
      1
    ],
    "checks": 72,
    "maxGap": 1
  },
  {
    "n": 2,
    "weights": [
      1,
      2
    ],
    "checks": 72,
    "maxGap": 2
  },
  {
    "n": 2,
    "weights": [
      0,
      1
    ],
    "checks": 72,
    "maxGap": 0
  },
  {
    "n": 3,
    "weights": [
      1,
      1,
      1
    ],
    "checks": 864,
    "maxGap": 2
  },
  {
    "n": 3,
    "weights": [
      1,
      2,
      3
    ],
    "checks": 864,
    "maxGap": 4
  },
  {
    "n": 3,
    "weights": [
      0,
      1,
      2
    ],
    "checks": 864,
    "maxGap": 2
  },
  {
    "n": 4,
    "weights": [
      1,
      1,
      1,
      1
    ],
    "checks": 10368,
    "maxGap": 3
  },
  {
    "n": 4,
    "weights": [
      1,
      2,
      3,
      1
    ],
    "checks": 10368,
    "maxGap": 5
  },
  {
    "n": 4,
    "weights": [
      0,
      1,
      2,
      0
    ],
    "checks": 10368,
    "maxGap": 2
  },
  {
    "n": 5,
    "weights": [
      1,
      1,
      1,
      1,
      1
    ],
    "checks": 124416,
    "maxGap": 4
  },
  {
    "n": 5,
    "weights": [
      1,
      2,
      3,
      1,
      2
    ],
    "checks": 124416,
    "maxGap": 7
  }
]
```

Reproduce with Node.js or equivalent JavaScript BigInt runtime:

```javascript
function verify(){
 const S=[[0],[1,2,3],[0,1,2,3]], rows=[];
 for(let n=2;n<=5;n++){
  const N=4**n,Z=Array.from({length:n},(_,i)=>1<<(2*i)).reduce((a,b)=>a|b,0),pivot=1<<(2*n-2);
  const reps=Array.from({length:N},(_,i)=>i).filter(x=>!(x&pivot));
  const bit=Array.from({length:N},(_,i)=>1n<<BigInt(i));
  const masks=Array.from({length:2*n},(_,b)=>{let m=0n;for(let x=0;x<N;x++)if(!(x&(1<<b)))m|=bit[x];return m});
  function shift(m,w){for(let b=0;b<2*n;b++)if(w&(1<<b)){let a=masks[b],d=BigInt(1<<b);m=((m&a)<<d)|((m&~a)>>d)}return m}
  const types=Array.from({length:3**n},(_,j)=>{let p=[],xs=[0];for(let i=0;i<n;i++){let a=j%3;j=(j-a)/3;p.push(a);xs=xs.flatMap(x=>S[a].map(v=>x|(v<<(2*i))))}let m=0n;for(const x of xs)m|=bit[x]|bit[x^Z];return {p,xs,m}});
  function predicted(p,w,alpha){
   let fixed=[0,0],both=0,gain=0,forced=[0,0],P=0,A=0;
   for(let i=0;i<n;i++){
    const a=p[i],u=(w>>(2*i))&3,h=alpha[i];A+=h;P+=a>0?1:0;
    for(let b=0;b<2;b++)fixed[b]+=h*(a===2?2:a+Number((u^b)!==0));
    const inside=u<2;
    const c=(a===0&&!inside)?1:2, f=(a===0&&inside)?0:1;
    both+=h*c;gain=Math.max(gain,h*(c-f));
    if(a===0&&inside)forced[u]+=h;
   }
   return [Math.min(...fixed,both-gain),A-Math.max(...forced),P];
  }
  const weights=[Array(n).fill(1),Array.from({length:n},(_,i)=>1+i%3)];if(n<=4)weights.push(Array.from({length:n},(_,i)=>i%3));
  for(const alpha of weights){
   const ordered=types.map(t=>({...t,c:t.p.reduce((a,b,i)=>a+b*alpha[i],0)})).sort((a,b)=>a.c-b.c);
   const point=Array.from({length:N},(_,x)=>{let c=0;for(let i=0;i<n;i++)if((x>>(2*i))&3)c+=alpha[i];return c});
   let checks=0,maxGap=0;
   for(const t of types)for(const w of reps){
    const m=shift(t.m,w);
    const actual=ordered.find(u=>(m&u.m)===m).c;
    let worst=0;for(const x of t.xs)worst=Math.max(worst,Math.min(point[x^w],point[x^w^Z]));
    const [want,wantWorst,P]=predicted(t.p,w,alpha);
    if(actual!==want||worst!==wantWorst)throw Error(JSON.stringify({n,p:t.p,w,alpha,actual,want,worst,wantWorst}));
    if(alpha.every(x=>x===1)&&actual-worst>Math.min(P,n-1))throw Error("gap bound");
    maxGap=Math.max(maxGap,actual-worst);checks++;
   }
   rows.push({n,weights:alpha,checks,maxGap});
  }
 }
 return rows;
}
console.log(JSON.stringify(verify(),null,2));
```

## 5. Next

Generalize the two-label obstruction to rank two and overlapping-cycle blocks; investigate finite witnesses for the failure of simultaneous lift availability and whether graph separators permit exact fixed-reserve spectra without enumerating every prefix. Preserve the distinction between pointwise transport and fixed robust reserve. No formal Result or theorem admission asserted.
