# R137C — Monotone coefficient progression through Farey denominator periods

Date: 2026-11-14 Asia/Shanghai. Frozen science 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Status: author-side, NOT_REVIEWED. Scope: the tied one-parameter auxiliary S23 floor-word model, not native X6 dynamics. Uses exact R137B integer-gap characterization in FAREY_INTEGER_CRITERION.md.

## Theorem R137C.1 — single Farey cell, exact one-step expansion

Fix integers m>=1 and K>=2; let L=K-1. Let a/b < c/d be neighboring fractions in the order-m Farey sequence (so bc-ad=1), and fix a consecutive open intercept gap with lower cut p-j alpha and upper cut q-k alpha, as in R137B. Let \(\mathcal G(K)\) mean that this exact gap is visited by the tied observer for at least one alpha in (a/b,c/d).

Then

1. \(\mathcal G(K)\implies\mathcal G(K+bd)\);
2. \(\mathcal G(K+bd)\) is true **for every** K>=2, independently of whether \(\mathcal G(K)\) was true;
3. therefore the same gap produces a valid word for every K'>=K+bd, with a rational certificate computable by the R137B midpoint formula. In particular \(\mathcal G(K+tbd)\) for each integer t>=1.

**Proof.** R137B says \(\mathcal G(K)\) iff the open interval (A_K,B_K) contains an integer, where
\[
 A_K=(L+k)a/b-q,\qquad B_K=(L+j)c/d-p.
\]
This interval has strictly positive width: choose any alpha inside the Farey interval; the gap is strictly open, so f(alpha)<g(alpha), and f,g are strictly increasing, giving \(A_K=f(a/b)<g(c/d)=B_K\).

When K is replaced by K+bd, the endpoints become
\[
 A_{K+bd}=A_K+ad,\qquad B_{K+bd}=B_K+bc
                         =B_K+ad+1.
\]
Translation by the integer ad reduces the new feasibility interval to (A_K,B_K+1). Because B_K>A_K, its length exceeds one and it must contain an integer. This proves (2). If an old integer N is already in (A_K,B_K), then N+ad lies strictly inside (A_{K+bd},B_{K+bd}), proving (1) and producing a constructive transformed certificate. Part (3) follows from one-step feasibility and the fact that the width increases strictly as L increases; if an open interval of width>1 contains an integer for every position of its endpoints, all later K also work. In fact the increased width for all K'>=K+bd remains >1. QED.

## Theorem R137C.2 — global coefficient-period inclusion

Set \(P_m=\operatorname{lcm}(1,\dots,m)\). For all K>=2,m>=1,

\[
\boxed{V(K,m)\subseteq V(K+P_m,m).}
\]

More strongly \(V(K+P_m,m)\) is the complete finite Sturmian language of length m for every K>=2 (and thus every K+tP_m with t>=1).

**Proof.** Every word in V(K,m) has a witness in some open Farey slope interval and some open intercept gap. This remains true when its original witness was at a rational boundary, by right-continuity of the consecutive floor differences and finite local cut partitions (R137B). Adjacent Farey denominator pairs b,d are coprime, with 1<=b,d<=m, so bd=lcm(b,d) divides P_m. Theorem R137C.1 applied at K and repeated P_m/(bd) times preserves that particular gap's word at K+P_m, proving inclusion.

For every gap at the initial K, Theorem R137C.1(2) already guarantees its realization at K+bd. Since the gap width grows strictly with K, it remains realized at K+P_m>=K+bd. The collection of all such gap words is exactly the full finite Sturmian language, using R134/R135's classical mechanical-word correspondence. QED.

This theorem provides a precise direction-dependent **monotonicity along a coefficient arithmetic progression**, coexisting with the previously verified nonmonotonicity for K->K+1 (m=7,K=11 to 15). It is a structural statement about represented words, unlike R137's separate temporal jump-count affine periodicity.

## Complexity and witness construction

The binary length of P_m is at most log2(m!), hence O(m log(m+1)) bits. Computing it with gcd/lcm takes polynomial bit complexity. For a given actual represented word, retain its witnessing Farey gap and use N->N+ad for each shift bd, or use the R137B exact integer criterion directly at K+P_m. Thus the inclusion is constructive with arithmetic polynomial in m and log(K+P_m). The potentially exponential *magnitude* of P_m does not require enumeration of that many coefficient values.

## Verification

Companion check_r137c.py uses the independent R137B exact Farey gap/witness algorithm. For every m=1,...,8 and K=2,...,24 (184 exact pairs), it checks word-set inclusion V(K,m) subset V(K+P_m,m) and exact equality of V(K+P_m,m) with the known classical finite Sturmian count F_m. R137B separately checks each constructed witness against the original strict S23 fractional-parts observation. Verification marker: R137C_COEFFICIENT_PERIOD_INCLUSION_PASS.

The infinite theorem follows from the Farey interval proof, while the finite test checks code and examples. Independent review remains NOT_REVIEWED.

## Next research direction

Find the smallest useful common coefficient shift preserving inclusion, instead of the universal but often oversized P_m; characterize the per-word minimal Farey-gap period across its multiple representations. Use this structure and the exact integer-gap criterion to classify return/disappearance of words and sharpen K_first(m), K_eventual(m).
