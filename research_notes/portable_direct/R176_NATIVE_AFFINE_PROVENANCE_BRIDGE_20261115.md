# R176 — Exact positive Affine/EffectHistogram carrier for labeled X6 four-moment paths

Date: 2026-11-15 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED.
Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: R175, immutable commit 10ca66f6f1a40dc7a2ee0ff6052d4adf98c56b85, research_notes/portable_direct/R175_PROVENANCE_MONOID_FOUR_MOMENT_LIFT_20261115.md.

Native interface read directly from canonical enterprise-math main: src/enterprise_math/brc_transport.py (Affine.then, EffectHistogram.from_terms, alternatives, then). This document is a mathematical adapter theorem, not a modification of the existing API.

## Population and observer

Work in a chosen chart of the P000 X6 affine torsor. Primitive path steps are ±E_1,...,±E_6 and carry chart-relative integer displacements. Given P=(v_1,...,v_n), write D(P)=Σ v_t and J(P)=Σ_{t=1}^n Σ_{r=1}^t v_r. Length counts ordered steps, not another spatial axis. Let M be any finite monoid, possibly noncommutative, with identity 1 and chronological label product m*n. The positive source family comprises branches (input port i, output port j, positive rational weight w, positive integer multiplicity c, label m, ordered path P). Alternatives add branches. Serial pairs match intermediate ports, multiply weights and multiplicities, concatenate paths and multiply labels chronologically.

The observer reads for each ordered port pair and individually selectable provenance label m the signed-linear weighted prefix integral C_m after arbitrary compatible left and right serial contexts. The R175 minimal summary for this scope is A_m=Σwc, L_m=Σwc|P|, B_m=ΣwcD(P), C_m=ΣwcJ(P). The native effect histogram is a finer carrier because it retains the joint tuple (positive weight, affine effect, multiplicity).

## R176A — Faithful affine action of four-moment path classes

Fix d=6 and V=Q^d_x ⊕ Q^d_j ⊕ Q[M]_z. Define the right regular linear representation R_m(e_u)=e_{u*m}, including for noninvertible monoid elements. Set

    T(m,P)(x,j,z) = (x+D(P), j+|P|x+J(P), R_m z).

**Theorem A.** For every m,n∈M and signed native paths P,Q,

    T(m,P).then(T(n,Q)) = T(m*n,PQ).

Further, T(m,P)=T(n,Q) if and only if m=n, |P|=|Q|, D(P)=D(Q), and J(P)=J(Q).

**Proof.** R_n R_m(e_u)=e_{(u*m)*n}=R_{m*n}(e_u). The composite j-coordinate is j+(|P|+|Q|)x+J(P)+J(Q)+|Q|D(P), exactly j+(|PQ|)x+J(PQ) by the R171 concatenation cocycle. x-displacements add. To recover the class from an affine map, apply its label block to e_1 and read e_m; read |P| in any j-from-x block coefficient, and D(P),J(P) in its affine offset. The converse is immediate. QED.

The auxiliary rational action dimension is 2d+|M|=12+|M|, containing bookkeeping registers, not additional physical/native spatial axes. The map retains precisely (m,|P|,D,J), not raw ordered-word identity. A nonunit label may give a singular affine linear part; the native then method supports this, whereas inverse would not be available.

## R176B — Positive native effect-histogram homomorphism

Map every raw branch (i,j,w,m,P,c) to the joint native atom (w,T(m,P),c) in the (i,j) port entry, represented using EffectHistogram.from_terms(12+|M|, terms). Then alternatives correspond to native .alternatives, and serial composition corresponds to native .then followed by summation over intermediate ports. This map is an exact semiring homomorphism, injective on the finite histogram of equivalence classes (w,m,|P|,D,J), with multiplicity.

**Proof.** By Theorem A, actions compose as paths and labels do; the inspected native .then multiplies positive rational weights and integer multiplicities, and from_terms coalesces exactly equal joint (weight,action) atoms by adding counts. Port routing is ordinary matrix composition in the alternatives semiring. Distinct class tuples give distinct actions or weights. QED.

## R176C — The minimal four-moment observation quotient

Decode m, n=|P|, D,J from each retained affine atom, and for each labeled port compute A=Σwc, L=Σwcn, B=ΣwcD, C=ΣwcJ. For compatible families F,G the projection obeys ordered Q[M]-matrix products

    A(FG)=A(F)A(G),
    L(FG)=L(F)A(G)+A(F)L(G),
    B(FG)=B(F)A(G)+A(F)B(G),
    C(FG)=C(F)A(G)+A(F)C(G)+B(F)L(G).

The identities hold at every pair of outer ports and every output label, summing over intermediate ports and ordered label decompositions. They follow by multiplying the raw branch equations and collecting coefficients. Induction proves exact preservation through any compatible two-sided context. R175B provides necessity and minimality of the four labeled moments under these exact C-observations and contexts. Thus the native positive affine-effect histogram supplies a faithful fine carrier of the observable quotient, while the four-moment projection is the minimal sufficient signed-linear summary for this declared scope.

For negative rational branch coefficients, use the formal additive group completion of the positive histogram semiring and extend serial multiplication bilinearly. Its projection obeys the same formulas. The **existing native EffectHistogram prohibits negative weights**; this formal completion is outside the native positive API, and does not confer signed amplitude semantics on positive mass.

## R176D — Exact counterexample to one-point output compression

Let e=+E_1 and f=-E_1. The empty path ε has (|ε|,D,J)=(0,0,0), while Q=effe has (|Q|,D,J)=(4,0,0). At the initial affine state (x,j,z)=(0,0,e_1), their transformed states coincide. Their full affine effects differ because the j-from-x coefficient is 0 versus 4. Prepending the path e distinguishes them: J(eε)=e, J(eQ)=5e. Consequently a single initial-state evaluation is not a safe quotient under arbitrary left contexts, while the full affine action and four moments distinguish the two.

## Exact evidence

The accompanying R176_native_affine_bridge_check.py is a standalone Python integer/Fraction reference checker for the inspected native interface laws. R176_verification.json records its output. The check uses the first two axes as a restricted X6 embedded slice and the four-element noncommutative full transformation monoid of a two-element set. It executes 64 monoid-associativity checks, 441 path-action compositions, 48 label/word compositions, 144 two-port raw-to-histogram serial comparisons, 144 independently computed moment products, 144 raw moment checks and two explicit boundary witnesses. Theorem statements are proved for the full six native axes and every finite monoid, not inferred from these tests. An optional imported-native probe is included in the source, but the author environment had no importable enterprise_math package; native cases actually executed: 0.

Review: NOT_REVIEWED. Formal Task CLAIM/Result/Review: none. No Foundation or actual deployment claim.

## Next discriminating work

Run the optional imported-native probe in the repository checkout, build a typed 6-axis port adapter, and measure the representation overhead. Determine the actual source/provenance selectors before choosing a finite monoid quotient; an unbounded ordered-source-word observer may require retaining the full word. Analyze recurrence/closure separately for the lifted positive affine packet and for the formal signed completion. Complexity improvement, if claimed, must include construction, rational bit lengths, and decoding costs.