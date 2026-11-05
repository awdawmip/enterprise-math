# D25 / 2026-11-06 — Lucas decomposition of the original-216 integer shadow at every prime divisor

**Research status:** author-derived exact finite-field algebra; 24 Lucas-factor checks and three squarefree-composite witnesses executed in a local standard-library Python process; **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM**. This is a new, restricted ordinary-arithmetic observer result, not a native Source checkpoint or a proof of the D25 second digit.

**Task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research lane as provided for this continuing conversation: `chatgpt-research-hourly-enterprise-math-20260923`.

## Previous input, not newly credited

The earlier author-side 2026-11-05 shadow was
[
C_n=sum_{k=0}^{2n}(6k+1)(-1)^k2^{2n-k}
 inom{2n}{k}inom{3n}{k}inom{4n}{k}inmathbf Z.
]
For primes (p=6n+1), the existing first-digit lemma relates this shadow to the original signed 216 sum (W_p). A previous computation observed ((6n+1)mid C_n) for (1le nle500), with no proof for all composite moduli. The current unit proves a Lucas decomposition, a prime-divisor criterion and a genuinely infinite squarefree composite family.

## Theorem: exact Lucas reduction at an arbitrary prime divisor

Take **any** integer (nge1), a prime (qge5) with (qmid6n+1), and write (n=qN+r), (0le r<q). For each (a=2,3,4), define
[
c_a=lfloor ar/qfloor,quad s_a=ar-qc_a,quad M_a=aN+c_a.
]
All following finite sums are in (mathbf F_q). Put
[
L_q=sum_{j=0}^{q-1}(6j+1)(-2^{-1})^j
 inom{s_2}{j}inom{s_3}{j}inom{s_4}{j},
quad
T_{q,N}=sum_{ellge0}(-2^{-1})^ell
 inom{M_2}{ell}inom{M_3}{ell}inom{M_4}{ell}.
]
The second sum terminates at (min(M_2,M_3,M_4)). Then
[
oxed{C_nequiv2^{2(r+N)}L_qT_{q,N}pmod q.} 	ag{1}
]
Moreover (6r+1equiv0pmod q), hence
[
-s_2equiv	frac13,qquad -s_3equiv	frac12,qquad
-s_4equiv	frac23pmod q.
]
Using (inom{s_a}{j}equiv(-1)^j(-s_a)_j/j!) for (0le j<q), we obtain
[
L_qequiv
sum_{j=0}^{q-1}(6j+1)
rac{(1/2)_j(1/3)_j(2/3)_j}{2^j(j!)^3}
=:W_qpmod q.
]
Thus the **precise composite-to-prime factorization** is
[
oxed{C_nequiv2^{2(r+N)}W_q T_{q,N}pmod q,qquad qmid6n+1.} 	ag{2}
]
All (q)-local denominator inverses are valid because (qge5), (j<q).

### Proof

By the mod-(q) Lucas/Frobenius binomial identity,
[
inom{an}{qell+j}=inom{qM_a+s_a}{qell+j}
equivinom{M_a}{ell}inom{s_a}{j}pmod q
quad(0le j<q).
]
The original (C_n) sum may safely extend over all (kge0), since the factor (inom{2n}{k}) vanishes for (k>2n). Split (k=qell+j); in (mathbf F_q),
(6k+1equiv6j+1), ( (-2^{-1})^{qell+j}=(-2^{-1})^{ell+j}), and
(2^{2n}=2^{2(qN+r)}=2^{2(N+r)}).
The double sum therefore separates exactly into (L_q T_{q,N}), proving (1). Since (qmid6n+1), the parameter congruences above convert its low digit to the signed original-216 (W_q), proving (2).

## Immediate composite family and exact scope

For **each** prime (qmid6n+1) with (W_qequiv0pmod q), (2) proves (qmid C_n). Let (mathcal Q(n)) consist of those prime factors; their product divides (C_n). In particular, the frozen accepted first-digit result (W_qequiv qpmod{q^2}) for (qequiv13,19pmod{24}) gives
[
oxed{
 m=6n+1	ext{ squarefree and all }qmid m
 	ext{ satisfy }qequiv13	ext{ or }19pmod{24}
  Longrightarrow mmid C_n .
} 	ag{3}
]
This yields an infinite parametric composite family, e.g. (m=q_1q_2) for distinct primes (q_1,q_2equiv13,19pmod{24}) whose product is (1pmod6). The infinitude of primes in these progressions follows by Dirichlet's theorem; the algebraic implication (3) needs only the frozen first-digit premise. Formula (2) is unconditional as a mathematical identity; the divisibility conclusion for a given prime depends on its actual (W_qmod q). Prime-power divisibility (q^emid C_n) for (q^emid6n+1, e>1) remains open.

**Typed observer / BRC:** preserve original ordered index (k=qell+j), signed factor (6k+1), three independent binomial factors, both digit/carry triples ((s_a,c_a,M_a)), modulus (q), and low/high sums ((L_q,T_{q,N})). Reduction to (L_q) loses high-factor information needed for a general (q^2)-valuation; the theorem certifies only the declared future operation: first-digit divisibility modulo each prime (q). It makes no claim about original native Heartbeat-X6, divided-power H0/B0, crystalline Frobenius, (eta,kappa), or temporal dynamics.

## Actual finite checks (supporting, not replacing the proof)

The companion exact Python script independently computes (C_nmod q) using the original integer-binomial sum and the factorization (1); 24 sample pairs (qmid6n+1) pass, including nonzero carries and (qin{5,7,11,13,19,23,37}). Direct (C_nmod m=0) at the three new composite witnesses (m=247=13cdot19) ((n=41)), (481=13cdot37) ((n=80)), (817=19cdot43) ((n=136)). A legacy-window regression of (1le nle200) passes; previously checked (1le nle500) is not recredited. The sampled prime-power cases (25,49,169) also vanish, but no prime-power assertion is proved.

## Existing source frontier and next independent unit

At this run's fresh native Source read, requests `em-h20-20261106-0023-d25-task` and `em-h20-20261106-0023-d25-continuation` both returned SUCCEEDED on Source `f375daccca6dd2e8a6a00375331b1a7ff29a7edd`. It preserved the pre-existing `SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED` checkpoint, two previous native completed units and old contributor history; task is HANDOFF_READY with no live CLAIM, route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION and execution_authorized=false. This artifact is author-side portable material, not a new Source CLAIM, OPEN, checkpoint, frozen Result or review.

**Next precise mathematical actions:** derive the (q^2) digit/carry correction to (2) and test whether it yields (q^{v_q(6n+1)}mid C_n); separately, return to the D25 mother target by seeking a non-tautological finite-sum telescoper for the signed (F,H) ports enforcing (W_pequiv ppmod{p^3}). Do not redo the already accepted WZ/Green or existing Hensel precision results. Native p373 original-class H0/B0, ([X]Umod139129), Frobenius direction/normalization, (eta,kappa) and independent review remain open.
