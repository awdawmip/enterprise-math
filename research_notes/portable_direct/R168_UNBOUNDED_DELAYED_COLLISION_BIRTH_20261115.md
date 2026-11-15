# R168 — An exact unbounded-delay, one-instant collision-birth family

Date: 2026-11-15 (Asia/Shanghai). Status: AUTHOR_PROVED / NOT_REVIEWED. Independent portable research; no formal Task/CLAIM/Result/Review assertion.

Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34` (unchanged). Scientific lineage: R164 precise scalar phase signatures at `991d99ab20b7669ecf1465eba01e87851855381e`, R166 append certificate at `40de7600f89e9cf868db2593e4b4907d46086b6a`, and R167 final-horizon non-remergence at `d700f5c6ad0141a1fb6e8636119182b677e36f31`. Source world and P000 remain unchanged. Scope is an external finite binary Sturmian/tied-phase scalar observer; not a native X6/BRC theorem.

## Definition

For a binary word `w=w_1...w_n`, let `p_0=0` and `p_i=sum_{h=1}^i w_h`. At slope `theta in [0,1]`, its feasible intercept interval is

`I_w(theta) = intersection_{0<=i<=n} [p_i-i theta, p_i+1-i theta]`.

For a word having positive-length slope support `(alpha,beta)` define the exact signature `S(w)=(alpha,beta,A,B)` with `A=min_i(p_i+1-i alpha)` and `B=max_i(p_i-i beta)`. These endpoint rational quantities are equivalent to the denominator-scaled `(U,V)` notation of R164: here the unscaled endpoint intercepts are used to avoid notation collisions. The entire argument uses exact rational numbers.

Let `Z_{n,k}=0^(k-1) 1 0^(n-k)` denote a word of length `n` with a single one at position `k` (one-based), `n>=2` and `1<=k<=n`.

## R168A — Closed exact signature of every singleton word

**Theorem.** Every `Z_{n,k}` is admitted and has signature

`S(Z_{n,k})=(0,b_{n,k},1,max(0,1-k b_{n,k}))`, where

`b_{n,k}=min({1, 2/n} union {1/(k-1):k>1} union {1/(n-k):k<n})`.

**Proof.** The slope-support pair constraints from indices `0<=i<l<=n` are `(p_l-p_i-1)/(l-i)<=theta<=(p_l-p_i+1)/(l-i)`. Since the prefix sums take only the values 0 and 1 and never decrease, all lower bounds are `<=0`; the physical slope bound 0 is attained. For the upper bounds, a pair of prefix sums both 0 contributes `1/(l-i)` and its largest possible index gap is `k-1`. A pair both 1 likewise has largest gap `n-k`. A pair crossing from prefix 0 to 1 contributes `2/(l-i)` and has largest gap `n`, realized by indices `(0,n)`. This yields `b_{n,k}>0` exactly as stated. At `alpha=0` the least upper intercept is `1`, and at `beta=b_{n,k}` the greatest lower intercept is `max(0,1-k beta)`, since the prefix sum becomes 1 at index `k` and every later line has smaller intercept. QED.

## R168B — Exact collision birth at length `2j` and nowhere else

For each integer `j>=1` and every `n>=j+1`, compare the two adjacent-swapped words

`u_{j,n}=Z_{n,j+1}=0^j 1 0^(n-j-1)` and
`v_{j,n}=Z_{n,j}=0^(j-1) 1 0^(n-j)`.

Both remain admitted for every such `n`. Their difference is exactly the adjacent `01 <-> 10` exchange at positions `j,j+1`; all subsequent symbols are the same zeros.

**Theorem.**

`S(u_{j,n})=S(v_{j,n})  if and only if  n=2j`.

At the unique collision,

`S(u_{j,2j})=S(v_{j,2j})=(0,1/j,1,0)`.

**Proof.** Put `b_u=b_{n,j+1}` and `b_v=b_{n,j}`. If `j>=2` and `j+1<=n<2j`, the closed formula gives `b_u=1/j`, whereas every candidate in `b_v=min(1,2/n,1/(j-1),1/(n-j))` is strictly greater than `1/j`. Hence the signatures are unequal. (For `j=1` this case is empty.) At `n=2j` both width parameters equal `1/j`, and their remaining endpoint coordinate is respectively `max(0,1-(j+1)/j)=0` and `max(0,1-j/j)=0`, establishing exact signature equality. If `n>2j`, then `b_v=1/(n-j)`, and each possible term defining `b_u` is strictly greater than `1/(n-j)`: namely `1`, `2/n` because `n>2j`, `1/j` because `n-j>j`, and `1/(n-j-1)` because its denominator is smaller. Therefore `b_u>b_v` and equality is impossible. QED.

## R168C — Unbounded first-collision delay and singleton lifespan

At the earliest complete swapped word, `n=j+1`, the pair is distinguishable for every `j>=2`. It remains distinguishable for all lengths `j+1,...,2j-1`, first collides at `2j` (after exactly `j-1` common appended zeros), then ceases to collide at `2j+1` and never collides again under the specified all-zero continuation.

Consequently, **there is no absolute, prefix-position-independent bound on how many common-symbol appends may precede the first scalar-signature collision**, even in the single-one family. The collided signature survives at precisely one length in this family. This does **not** claim that every possible common suffix has only a one-step collision lifespan; R166/R167 give different general bounds.

The loss of the adjacent-swap identity bit is transient and observer-relative: preserving position `k`, the branch ID, or the ordered source path distinguishes the two states throughout. No quotient of a native X6/BRC branch is justified by this scalar coincidence.

## Verification and limitations

`R168_singleton_birth_check.py` implements an independent O(n^2) exact strip-pair oracle, the closed singleton formula, and exact family tests. Expected marker: `R168_SINGLETON_BIRTH_EXACT_PASS`. `R168_verification.json` records **230 independent singleton formula comparisons**, **345 family cases by the strip oracle**, and **49,997 large-j transition cases** for `j<=10000` using the closed formula, all passed. The universal claims are supported by the symbolic proofs above, not inferred from finite numerical tests. Independent mathematical review and formal proof checking: `NOT_REVIEWED` / not performed.

## Scientific handoff

The R167 distinction between *collision birth* and *re-mergence after a split* is now sharp: collision birth can be arbitrarily delayed in this explicit family, but its lifetime here is exactly one length. Next, classify all possible birth lengths and lifespan distributions for fixed adjacent-swap position `j` with nonzero/common nonconstant suffixes. A separate typed BRC/X6 observer map would be required before transferring any scalar result into a native path/provenance claim.

Source-control observation: exact `RS-S23-AV` task lookup returned `SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY` at 2026-11-15T02:15:55Z, scoped to immutable Source `a153e35e4a4d363c7b9f21de6b66e4e820d622e6`; native owner projection was not evaluated. No formal CLAIM is asserted. Research Activity link may be pending independent verified session capability.
