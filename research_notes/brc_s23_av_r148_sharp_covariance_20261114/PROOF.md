# R148 — Sharp CRT covariance bound, equality classes, and first positive Sturmian witness

**Date:** 2026-11-14 (Asia/Shanghai). **Scientific input:** immutable `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. **Status:** author-side proof + independent exact computational crosscheck; `NOT_REVIEWED`.

**Scope:** the external scalar tied-phase S23 mechanical-word observer, with R146/R147's integer phase-index multiplicity. No native Heartbeat-X6 identification or formal shared Result is asserted.

**Predecessors:** R146 `b02b0c242b274bc6a82111dbd3600126a2867319` and R147 `2b81c43614889ccb638bb7d8feb329c3c467ff02`.

## 1. Exact definitions

Let `w` be a finite Sturmian binary word of length `m>=1` whose free-intercept slope-support endpoints are reduced rationals
`alpha=a/b < beta=c/d`, with `0<=alpha<beta<=1`, `b,d>=1`, and `g=gcd(b,d)`. For its prefix sums `s_j`, write

```
U = min_{0<=j<=m} [b(s_j+1)-ja],   V = max_{0<=j<=m} [d*s_j-jc].
x_L = (aL-U) mod b,                y_L = (cL-V) mod d,
eta_d(y)=0 if y=0, else 1-y/d,    L=K-1>=1.
```

R146 gives `C_w(K)=ceil((Lc-V)/d)-floor((La-U)/b)-1`. Thus with `h=U/b-V/d`, `delta=c/d-a/b`, and `e_w(L)=C_w(L+1)-L*delta`,

```
e_w(L) = h-1+x_L/b+eta_d(y_L).
```

The correction is periodic over `P=lcm(b,d)`. Define `Gamma_w=Cov_P(x_L/b, eta_d(y_L))`, taking the uniform average over any complete period.

## 2. R148.1 — A one-permutation covariance formula

**Theorem (all reduced rational endpoints and integer U,V).** Put `q=(g-1)/2`. For `t=0,...,g-1` set

```
r_t = (at-U) mod g,
z_t = (V-ct) mod g.
```

Then

```
Gamma_w = [1/(g*b*d)] * sum_{t=0}^{g-1} (r_t-q)(z_t-q).       (R148.1)
```

Both `(r_t)` and `(z_t)` are permutations of the residue set `0,...,g-1`. This formula replaces R147's conditional-mean expression by a centered permutation dot product and makes alignment explicit.

**Proof.** R147 partitions its full CRT period by `L mod g=t`. Write `B=b/g`, `D=d/g`. Conditional on `t`, all compatible `x` are `r_t+gj`, `0<=j<B`, and all compatible `y` are `((ct-V) mod g)+gk`, `0<=k<D`; the conditional joint distribution is their Cartesian product. The conditional means from R147 reduce, after subtracting the unconditional means, to

```
E[x_L/b | t] - E[x_L/b] = (r_t-q)/b,
E[eta_d(y_L) | t] - E[eta_d(y_L)] = (z_t-q)/d.
```

The second identity holds also at residue zero: the discontinuity of `eta_d(0)=0` converts the conditional centered mean into the residue `z_t=(-ct+V) mod g`. Total covariance and the conditional independence give (R148.1). The reduced endpoint fractions ensure `gcd(a,g)=gcd(c,g)=1` when `g>1`; when `g=1` the single centered residue is zero. QED.

## 3. R148.2 — Sharp bounds and equality characterization

For all admissible integers `b,d,a,c,U,V` as in §1,

```
                    g^2-1
|Gamma_w| <= -----------------------.                         (R148.2)
                 12*b*d
```

For `g>=2` both signs' equality conditions are exact:

```
Gamma_w= +(g^2-1)/(12bd)   iff  a+c=0 (mod g) and U+V=0 (mod g).
Gamma_w= -(g^2-1)/(12bd)   iff  c-a=0 (mod g) and V-U+1=0 (mod g). (R148.3)
```

For `g=1`, `Gamma_w=0`.

**Proof.** Centered permutations `r-q` and `z-q` have equal squared norm
`sum_{j=0}^{g-1}(j-q)^2=g(g^2-1)/12`. Apply Cauchy–Schwarz to (R148.1). Its positive equality occurs exactly when the two centered vectors are identical, so `z_t=r_t` at each `t`. Negative equality occurs exactly when `z_t=g-1-r_t` at each `t`. Since `r_t,z_t` are affine residues, checking `t=0,1` proves precisely the respective congruence pairs in (R148.3), and these pairs imply the identities for every `t`. QED.

Consequently, R147's exact discrepancy variance obeys

```
A - (g^2-1)/(6bd) <= Var_P(e_w) <= A + (g^2-1)/(6bd),
A = (b^2-1)/(12b^2) + (d^2-1)/(12d^2).              (R148.4)
```

The normalized correlation of the two residue contributions satisfies
`|rho| <= (g^2-1)/sqrt((b^2-1)(d^2-1))` when both denominators exceed one.

These are sharp arithmetic-carrier bounds. The negative bound is also attained by an actual Sturmian word: `w=0110` has `(a,b,c,d,U,V)=(1,2,3,4,1,0)`, `g=2`, and `Gamma=-1/32`.

## 4. R148.3 — Exact first positive covariance witness

**Finite exhaustive result:** Among **all binary words** of lengths `1<=m<=13` that satisfy the exact free-intercept Sturmian support test, `Gamma_w` is nonpositive. At `m=14` there is positive covariance, for example

```
w = 00001000010000
(alpha,beta)=(1/6,3/14), (U,V)=(2,0), g=2,
Gamma_w=+1/336.
```

Indeed `r_t=(t-2) mod 2=t` and `z_t=(-3t) mod 2=t`, so the centered permutations are identical. Thus the positive upper bound in (R148.2) is attained by an actual Sturmian word. Its period variance is `899/5292`, versus the independence baseline `1735/10584`.

The exhaustive rational script additionally checks all Sturmian words up to length 15, finding **1,906** valid words, **298** with `g>1`, **292** negative-covariance words, and **six** positive-covariance words. The first positive witnesses are four complement-related words at length 14, with two more at length 15. Exact source words, fractions and parameters are printed by the checker.

**Completeness argument for the finite search.** The checker visits every `2^m` binary string at each `m<=15`. It builds every prefix sum and evaluates the necessary and sufficient strict free-intercept slope bounds
`alpha=max(0,max_{i<j}(s_j-s_i-1)/(j-i))` and
`beta=min(1,min_{i<j}(s_j-s_i+1)/(j-i))`.
The support is nonempty precisely for `alpha<beta`. Each retained word receives exact reduced endpoint fractions and `U,V`, followed by two independently computed covariance expressions: (R148.1) and direct `P`-period floor/ceiling enumeration. Arithmetic uses Python integer division and `fractions.Fraction`; no floating point or random sampling is used.

The checker also verifies the algebraic inequality and equality criteria on **1,765** reduced rational endpoint/offset residue configurations with `b,d<=8`.

## 5. Research significance and next question

R147's joint dependence can be measured without the full `P=bd/g` population; its entire covariance is a rank alignment of two permutations of only `g` residue classes. The finite sign pattern offers a discriminating research direction: classify which Sturmian slope-support intervals can meet the positive alignment congruences, and determine whether the first positive length 14 extends to infinite families. This joint-residue analysis can be used alongside R146B's one-fiber-loss criterion near `E(m)`, while preserving multiplicity rather than collapsing to word presence.

**Verification status:** human derivation above; exact script execution returned `R148_SHARP_CRT_COVARIANCE_PASS`. No independent theorem review or official Task Result/CLAIM performed.
