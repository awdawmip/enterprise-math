# R166 — Exact one-bit alias survival and finite faithful continuation horizon

Date: 2026-11-15 (Asia/Shanghai). Research status: AUTHOR_PROVED / NOT_REVIEWED. Scope: external finite-Sturmian tied-phase scalar observer. Frozen science pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Mathematical dependencies: R162@f451da2665923179eed166c488a1e8063222ca29, R164@991d99ab20b7669ecf1465eba01e87851855381e, R165@a9ab301eb978d399cc559a9e1bf9fb9b7c8f6a3e. P000 and provenance-sensitive BRC/native transfer remain separate.

## Definitions

Let u,v be distinct admitted binary words of the same length m≥2 with identical exact signature S=(α,β,U,V), where 0≤α<β≤1. By R162/R165, their prefix sums differ by exactly one at a unique internal position 1≤j<m and are equal elsewhere. Orient the pair so p_j(u)=q−1 and p_j(v)=q. Their last prefix sum is the same integer N.

The shared endpoint chord is g(θ)=q−jθ. At every θ∈[α,β] the chord satisfies the closed prefix strips p_i≤x+iθ≤p_i+1 for both words. For every common prefix i≠j and α<θ<β, the chord satisfies the two inequalities strictly: p_i−iθ<g(θ)<p_i+1−iθ. If equality held at an interior slope, the boundary from that common prefix and the opposite j-th strip boundary would intersect transversely (i≠j), making one adjacent open slope infeasible for one word, contradicting the common open support.

## R166A. Exact one-bit append criterion

**Theorem.** Append the same bit e∈{0,1} to u and v. Write k=m+1, t=k−j, r=N+e. The extended words are both admitted with equal exact signatures **if and only if**

\[
\boxed{\frac{r-q}{t}\le\alpha,\qquad \beta\le\frac{r+1-q}{t}.}
\]

When this holds, both extended signatures equal the **original** S, including U,V. The test requires O(1) exact rational comparisons given S,j,q,N.

**Proof, sufficiency.** The inequalities are equivalent, for all θ∈[α,β], to r≤q+tθ≤r+1, or r≤g(θ)+kθ≤r+1. Thus the old common chord satisfies the new last-prefix strip at every old slope, for both extensions. Extending a word can only shrink its slope support; conversely this chord shows that neither support shrinks, so both remain (α,β). At α, the chord was the maximal allowed intercept 1+A, and at β it was the minimal allowed intercept B. As those extremal intercepts remain feasible, adding the last strip changes neither A nor B. Both signatures stay S.

**Proof, necessity.** For the two extensions, all new pair constraints between the last prefix k and an older prefix i≠j are identical; their old support (α,β) is also identical. Let G_- be the maximum of α and all these common new lower slope bounds, and G_+ the minimum of β and the common new upper slope bounds. The two different constraints involving j give

\[
\begin{aligned}
\alpha(ue)&=\max(G_-,(r-q)/t),&
\alpha(ve)&=\max(G_-,(r-q-1)/t),\\
\beta(ue)&=\min(G_+,(r-q+2)/t),&
\beta(ve)&=\min(G_+,(r-q+1)/t).
\end{aligned}
\]

Put l=(r−q)/t and h=(r+1−q)/t. If l≥β, ue is inadmissible: its new lower support limit is at least the old upper limit. If α<l<β, then r−kl=g(l). At the interior slope l every common older prefix has p_i−il>g(l)−1; consequently every new common lower constraint (r−p_i−1)/(k−i) is strictly below l. Hence G_-<l and α(ue)=l>α(ve). Therefore same admitted signature requires l≤α.

Dually, if h≤α then ve is inadmissible. If α<h<β, r−kh=g(h)−1 and p_i−ih<g(h) for all common i≠j. Consequently every new common upper constraint (r−p_i+1)/(k−i) is strictly above h. Hence G_+>h and β(ve)=h<β(ue). Equality requires h≥β. Combining yields the two stated inequalities. QED.

**R166B — unique preserving next bit.** At most one of e=0 and e=1 preserves a valid alias. If both did, the conditions for e=0 and e=1 would force β≤(N+1−q)/t≤α, contradicting α<β.

## R166C. Exact repeated-append certificate and finite horizon

For a common suffix z=z₁...zₛ let N_h=N+Σ_{a=1}^h z_a, N_0=N, and t_h=m+h−j. The two words retain the **same admitted signature after each suffix prefix** h=1,...,s if and only if

\[
\boxed{q+t_h\beta-1\le N_h\le q+t_h\alpha\quad(1\le h\le s).}
\]

In that case the signature remains the original S throughout. This follows by induction from R166A, retaining the same j,q and endpoint data. At each h the allowed real interval for integer N_h has width 1−t_h(β−α)<1. Thus it contains at most one integer. When feasible, N_h is necessarily floor(q+t_hα), and z_h=N_h−N_{h-1} must belong to {0,1}. A given horizon is checked in O(s) exact arithmetic; all stepwise surviving suffixes at that horizon form a set of cardinality at most one.

With Δ=β−α>0, the integer interval can be nonempty only if t_hΔ≤1. Therefore every stepwise-preserving common suffix has the **finite universal upper bound for this pair**

\[
\boxed{s\le \left\lfloor\frac1{\Delta}\right\rfloor-(m-j).}
\]

No infinite common suffix can maintain identical *valid* signatures at every prefix. This finite statement concerns a specified scalar observer and prefixwise survival; it is not an assertion about equality at a later final horizon after an intermediate split, nor about an observer that maps both invalid inputs to one token.

## R166 exact validation

The attached independently implemented Fraction-based oracle exhausts all 131,068 binary candidate words of lengths 2–16, finding 191 two-preimage signature classes. It compares 382 one-bit extensions against R166A, finding 140 preserving cases, zero pairs preserving both bits, and zero disagreement. A separate 1,302-case short-suffix check verifies unique prefixwise survival through horizons 1–5 on tested initial pairs. The deterministic integer-interval algorithm checks all 191 pairs, with 336 oracle-verified persistent intermediate steps. Maximum actual tested survival was six steps; the largest loose geometric upper bound was 48. Script: R166_append_preservation_check.py. Data: R166_verification.json. Expected pass marker: R166_EXACT_APPEND_PRESERVATION_PASS. The universal propositions rest on the symbolic proofs; independent review remains NOT_REVIEWED.

## Research consequence and next question

The one-bit provenance residual identified in R162 has a sharply restricted **stepwise scalar-signature** survival channel: one prescribed next bit at most, an explicit O(1) transition criterion, a unique feasible future prefix stream, and a finite width-based lifetime. Its transport under BRC branch operations or native X6 updates requires its own typed observer mapping.

Next: determine whether equality can **re-merge after a temporary split**, under an arbitrary common suffix and a declared final-horizon observer. Finite samples motivate the question but supply no all-length proof. Preserve the R164/R165 original sources and this independent exact proof; no protected Task/CLAIM/Result/Review is asserted by GitHub publication.