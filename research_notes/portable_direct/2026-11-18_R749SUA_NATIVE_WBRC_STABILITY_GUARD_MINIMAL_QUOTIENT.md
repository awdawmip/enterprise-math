# R749SUA — Exact finite-feedback stability-guard quotient for a recurrent BRC port

Date: 2026-11-18 (Asia/Shanghai). Evidence: **AUTHOR_EXACT_NOT_REVIEWED**. Independently authored portable TASK_RESEARCH; no shared TASK CLAIM, physical triadic-event authorization, Result/Review or theorem promotion asserted.

Scientific source pin unchanged: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Foundation reused exactly at this scientific pin: `definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md` (WBRC-T30..T32). Predecessor R749STZ@d01c5b73d57fa87d0ddd17d30c6f1cf07d5b8660 proved a rollback residual under a *candidate* observer; the present work instead uses an **actually allowed finite positive-rational WBRC-T31 port-to-external feedback context** and a carefully restricted Boolean observation alphabet.

## 1. Declared model, native context and elementary guard

Let W be a finite nonnegative rational recurrent module with a single labeled visible port P, stable internal block A, and baseline stable effective mass `w=(W_eff)_{PP} in Q∩[0,1)`, with `W_eff=B+Y(I-A)^{-1}X`. Keep the WBRC-T30–T32 source-defined hypotheses.

For a chosen nonnegative rational feedback c, introduce one new external state X and edges P→X of mass c, X→P of mass 1, no other new edges. These are WBRC-T31-permitted connections to **visible** ports only. After collapsing the original hidden block, the two visible vertices have recurrent matrix

```
          P  X
       P [w, c]
       X [1, 0]
```

The observer outputs one bit: 1 iff the enlarged nonnegative matrix is **strictly** stable (spectral radius <1). A critical spectral radius exactly 1 outputs 0. A probe is reset before the next read. We do not allow any additional port-star amplitude, hidden-state mutation, path-POP, absolute zeta, or unlisted feedback context in the *finite-grid* observer.

**Lemma 1.** Its Boolean output is `g_c(w)=1 iff w+c<1`.

*Proof.* The two eigenvalues solve `lambda^2-w*lambda-c=0`. The Perron root is `(w+sqrt(w^2+4c))/2` and dominates the absolute value of the other eigenvalue. Because `0<=w<1`, this root is <1 exactly when `1-w-c>0`. WBRC-T30/T31 transfers the status to the original module plus its permitted external context. QED.

## 2. Sharp finite-resource quotient, with exact boundary convention

Fix `K>=2` and `1<=M<=K-1`, integers. Allow exactly the feedback alphabet `C_{K,M}={j/K : j=1,...,M}`. Thus the maximum **declared** feedback mass is `M/K`, and each query reports only g.

Set `k=floor(Kw)` and `h_{K,M}(w)=max(0,k-(K-M-1)) in {0,...,M}`.

**Theorem 2.** Two baseline-stable one-port modules have identical outputs to **every finite adaptive sequence** of the above resettable queries iff their h values agree. There are exactly `M+1` observational classes. The minimum extra uniform fixed-width state required by this observer is

```
b(K,M) = ceil(log2(M+1)) bits.
```

*Proof.* For each allowed j, Lemma 1 gives
```
g_{j/K}(w)=1 iff w < (K-j)/K
           iff floor(Kw) < K-j
           iff j <= M-h_{K,M}(w).
```
Consequently h determines all answers, and different h values give different answer vectors. The h=0 class is `[0,(K-M)/K)`; class `a=1,...,M` is `[(K-M+a-1)/K,(K-M+a)/K)`. All are nonempty and rationally realizable. The convention at equality is essential: `w+c=1` is **unstable**, so each interval is left-closed, right-open. Adaptive querying cannot distinguish equal complete response vectors: induction on the common answer history proves identical subsequent choices and outputs. Conversely one differing allowed query separates unequal classes. Encoding h gives the upper bit bound; pigeonhole on M+1 classes gives the matching lower bound. QED.

For the full declared grid `M=K-1`, `h=floor(Kw)`; therefore the K classes have exactly `ceil(log2 K)`-bit optimal signatures. For a limited feedback budget M/K, only M+1 classes remain. This is an exact observer-relative residual, *not* unrestricted compression of `W_eff`.

## 3. Sharp adaptive versus fixed-set query complexity

**Theorem 3.** With these resettable Boolean experiments, the minimum worst-case number of adaptive queries to identify h is `ceil(log2(M+1))`. The minimum number of distinct queries in a nonadaptive, preselected fixed set is `M`.

*Proof.* A binary decision tree of depth d has at most 2^d leaves, so d must be at least `ceil(log2(M+1))`. For achievability, maintain a consecutive interval of possible integer h. At a midpoint `mid`, probe `j=M-mid+1`: it returns true exactly if `h<mid`. Binary search identifies h in the claimed worst-case depth. For m preselected probes, ordered along j, their threshold crossings generate at most m+1 distinct Boolean patterns as h runs through 0,...,M. Hence m>=M. The entire M-probe grid attains M+1 patterns. QED.

These are finite-grid classification costs, **not** claims about finite-time exact recovery of an arbitrary rational W_eff with unbounded denominator.

## 4. Unrestricted rational stability bits still separate every exact port mass

**Theorem 4 (pairwise).** If *all* nonnegative rational single-feedback probes c are available, two baseline-stable positive-rational one-port modules yield the same Boolean responses in every probe **iff** their effective port masses are equal.

*Proof.* The forward direction from equal masses follows from Lemma 1. Conversely, for rational `0<=w1<w2<1`, select the rational `c=1-(w1+w2)/2>0`. Then `w1+c<1<w2+c`; the outputs differ. QED.

This gives a new one-port observer refinement of WBRC-T32: exact W_eff can be separated using *qualitative stability feedback alone* if arbitrarily precise rational probes are admitted, whereas the finite-feedback alphabet admits the strict quotient in Theorem 2. Pairwise separation does **not** mean every completely unknown rational can be identified in a uniformly bounded number of queries.

## 5. Concrete WBRC-permitted counterexample to finite-grid full-mass faithfulness

Use two finite positive-rational one-hidden-state, one-port modules
`A=[0], X=[1/4], Y=[1/4]`, and `B_1=[1/16]`, `B_2=[1/8]`.
The effective masses are `w1=1/8` and `w2=3/16`; both original modules are stable by WBRC-T30. With K=4, M=3, the three guard probes c=1/4,1/2,3/4 all return stable for both, so **their finite feedback signatures coincide** even though W_eff differs. With the out-of-grid but WBRC-allowed rational `c=27/32`, however, `w1+c=31/32<1` and `w2+c=33/32>1`; this single additional guard separates them.

This is a truly permitted **positive rational recurrent BRC Port** experiment, but not yet an authenticated physical **X6 Cell/Link/Port triadic event**. P000's six native spatial axes plus distinct time, composite-path provenance and triadic-balance ontology remain intact. Unlike R749STZ's hypothetical rollback predecessor read, there is no hidden-state access here. Enlarging the observer alphabet is precisely what creates the information distinction.

## 6. Exact program, validation range and status

The accompanying `R749SUA_PORT_GUARD_GRID_CERT.py` uses only Python `fractions.Fraction` and integer operations. It was **executed locally** in this turn and returned PASS. Coverage: all integers `K=2,...,32`; every grid boundary and two strict interior rationals per bin; every integer `M=1,...,K-1`; adaptive decision trees, exact guard vectors and class counts; all nonadaptive probe subsets of size at most two; and the concrete two-module witness.

Observed counts: 1,581 full-grid rational samples, 6,897 full-grid adaptive probe operations, 5,487 fixed-probe subsets, 32,736 bounded-budget sample cases, all passed. The third file `R749SUA_PORT_GUARD_GRID_RESULTS.json` records these exact counts and per-K outputs. The universal theorems are established by the arguments above, not by finite enumeration. No independent review or formal theorem acceptance has occurred; no original X6 dynamics implementation was executed.

## 7. Remaining research

(i) Find a P000-compliant actual triadic/causal X6 Cell–Link–Port event that supports the same typed positive-rational guard readout, **or prove its non-transferability** under the current native license. Preserve exact native coordinates, third slice coordinate, source labels, causal time and resource guards in that comparison. (ii) Extend the finite-test quotient to multiport BRC matrices, identifying exact semialgebraic stability cells under chosen rational feedback alphabets. (iii) Compare guard-only, stable-star and absolute-zeta observer levels; preserve structural/provenance residuals where total mass is insufficient.

**Scientific classification:** AUTHOR_EXACT_NOT_REVIEWED; independent scoped mathematical result inside the preexisting WBRC Foundation observer. Existing WBRC-T30/T31/T32 are reused as stated, not re-proved or silently promoted.