# R284AN — Intrinsic-rank compression and integer-primitive exterior-span certification

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Lineage: R284AM (exterior-tensor span), R284AL (random diagonal witness), R284AK (nonsymmetric principal-rank gap), R284AE (Schur graded response).
Frozen scientific source: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Current P000/worldview and observer/provenance constraints unchanged.
Scope: finite rational, auxiliary independently named diagonal Port-edit system; no native heartbeat dynamics, P000 modification, or future-operation-safe quotient is claimed.

## AN1. Intrinsic-rank factorization without materializing the m-by-m product

Let `U,V ∈ Q^(m×r)`, `m,r>=1`, `C=UV^T` and `k=rank_Q(C)`. There is an exact factorization `C=XY^T` with `X,Y ∈ Q^(m×k)`, computable from the supplied factors using two thin rank decompositions and a small coupling matrix. Hence the R284AM total paired exterior ambient dimension can be reduced from

`D_r = Σ_(j=0)^r binom(r,j)^2 = binom(2r,r)`

to

`D_k = Σ_(j=0)^k binom(k,j)^2 = binom(2k,k)`.

**Construction and proof.** Compute full-column-rank factors `U=P A`, `V=Q B`, where `P∈Q^(m×a)`, `Q∈Q^(m×b)`, `A∈Q^(a×r)`, `B∈Q^(b×r)`, with `a=rank(U), b=rank(V)`. Form only the `a×b` coupling `H=A B^T`, and its exact rank decomposition `H=L F` with `L∈Q^(a×k), F∈Q^(k×b)`. Since P is injective and Q^T is surjective, `rank(P H Q^T)=rank(H)=k`. Now set `X=P L`, `Y=Q F^T`, and check

`X Y^T = P L F Q^T = P A B^T Q^T = U V^T = C`.

If `k=0`, then `C=0`, every nonempty principal minor vanishes, and `d(C)=0` immediately. This factorization does not assume `rank(V^T U)=rank(UV^T)` (an assertion false even in rank-one nilpotent examples).

All named principal minors `det C[S,S]` remain exactly unchanged because the product C itself is preserved. This is a change of computational representation, not a deletion of user-declared future Port operations or provenance.

## AN2. Fraction-free rational-span updates with named-subset witnesses

Apply the R284AM basis-span recurrence to the reduced factors `X,Y` of width k. For each row i, multiply `X[i,:]` by a positive common denominator `α_i`, and `Y[i,:]` by `β_i`, yielding integer rows `x_i,y_i`. For an ordered named subset S of size j, define

`a_S = wedge_(i∈S) x_i`, `b_S = wedge_(i∈S) y_i`,
`z_S = a_S ⊗ b_S ∈ Z^(binom(k,j)^2)`.

The standard trace contraction `ℓ_j(z_S)=Σ_(|J|=j) (a_S)_J (b_S)_J` satisfies exactly

`ℓ_j(z_S) = (∏_(i∈S) α_i β_i) det C[S,S]`.      (AN2a)

Thus nonvanishing and the largest nonzero principal-minor order are unchanged. Nonzero witnesses recover the **original** rational determinant by exact division by the positive scaling product.

Maintain for each grade j a rational row span using only **integer** echelon vectors. Reducing a candidate integer vector v against a pivot row w with pivot p applies

`v ← w[p] v − v[p] w`,

then divides all coordinates by their positive integer gcd and optionally normalizes sign. This operation has integer entries, preserves membership in the rational span of already accepted rows, and clears the pivot without using rational fractions. If the result is nonzero, retain its primitive integer echelon row **and separately** the original true subset label S with its unmodified wedge factors a_S,b_S. The latter is essential: a linear combination of subset states is not a genuine named subset witness.

The echelon rows have zero coordinates before their first nonzero pivot. Processing distinct pivots in increasing order gives exact zero/nonzero rational-span membership; the primitive normalization is multiplication by a nonzero rational, so the span is unchanged.

**Completeness.** Let L_j(i) be the rational span of all true named states z_S with `|S|=j` and S within rows 1..i. Appending named row i gives the exact recurrence

`L_j(i) = L_j(i−1) + E_i L_(j−1)(i−1)`.       (AN2b)

The integer-echelon membership procedure keeps precisely a subset-state basis for each L_j(i). Induction proves that dependent candidates may be omitted without losing later reachable vectors, because E_i is linear. Therefore `ℓ_j` vanishes on all j-principal minors iff it vanishes on each retained true subset-state basis. A nonzero trace gives a genuine named S and exact nonzero determinant. Zero trace in all basis states of every grade above d, together with the replayable recurrence, is a deterministic negative certificate for those grades.

## AN3. Scoped Port degree and resource bounds

For the earlier independent diagonal-edit pencil

`M_C(u,v) = [[diag(u), I_m], [C, diag(v)]]`,

the previously proved block identity `det M_C = det(diag(u_i v_i)−C)` implies

`ν(M_C) = 2(m−d(C))`, where `d(C)=max{|S|:det C[S,S]≠0}` and d=0 if all nonempty principal minors vanish.

AN1–AN2 compute d deterministically for **all rational U,V**, including signed weights, cancellation, and the zero-principal-rank case. The intrinsic-rank parameter k can be strictly less than each of `rank U`, `rank V`, and the supplied factor width r.

Counting exact field/arithmetic operations, the thin factorization is `O(m poly(r))`; the conservative DP bound is `O(m poly(k) D_k^3)`. The working span dimension is at most D_k, with genuine subset labels at most k indices apiece. The script uses arbitrary-precision integer products and gcd in the span stage; **the field-operation bound is not a proved sharp bit-operation bound for this particular primitive-echelon implementation**. Its observed intermediate bit lengths and Python timings are finite-instance measurements, not a uniform speedup or worst-case bit-growth theorem. Factor reduction itself still uses exact SymPy rational elimination.

The certificate interface comprises input U,V, reproduced thin rank decomposition X,Y, a deterministic replay of the named-subset recurrence, grade bases, and trace tests. Saving a few final zero traces alone, without the spanning argument or replay, is insufficient for negative certification.

## Exact validation and reproducibility

Artifacts:
- `research_notes/portable_direct/R284AN_intrinsic_rank_fraction_free_checker.py`
- `research_notes/portable_direct/R284AN_exact_verification.json`

Run `python R284AN_intrinsic_rank_fraction_free_checker.py` with SymPy 1.14.0 and standard Python, using the embedded seed `284014`.

Completed local tests:
- 63 signed integer-factor instances with `2<=m<=7` and `1<=r<=min(m,4)`, each compared against independent exact enumeration of the corresponding principal minors;
- 1,377 true named-subset membership checks against the resulting DP spans;
- nonminimal-width examples `(m,r,k)=(12,8,2),(24,8,2),(32,10,2)` with original `D_r=12870,12870,184756` and reduced `D_k=6` in all three. The exact witnesses are S={1,2}, with determinants -126000, 350784, and 89100;
- a five-row example where **both** original factors have rank two but `rank C=1`, witness S={1}, determinant 6;
- the nonzero nilpotent rank-one matrix `C=[[0,1],[0,0]]` (expressed as U=[1,0]^T and V=[0,1]^T), where d(C)=0 as required.

All declared exact checks passed. The routine separately checks each reported nonzero witness by the determinant of the corresponding principal submatrix of the original U V^T. The m=24/32 examples were not compared with full exponentially large subset enumeration; their negative-grade result uses the proved span recurrence. The timing field excludes factor reduction and must not be compared with end-to-end runtimes.

No independent theorem review was performed: `NOT_REVIEWED`. The result is a new improvement within the R284 research line; no general literature novelty claim.

## Interpretation and unresolved work

This provides a smaller exact carrier for the **current fixed rational principal-minor observer**. A smaller factor representation retains C and its declared diagonal-edit determinant polynomial. It is not an automatic minimal state for arbitrary future hidden-state interventions, signed Port provenance, other observables, or native X6 transitions.

Next: (i) derive and implement a truly bounded-bit Bareiss/Hermite or modular incremental span variant with a compact independently checkable closure transcript; (ii) benchmark complete preprocessing + span + witness/negative verification on equal hardware versus R284AM and R284AL weighted probes; (iii) test whether richer declared future Port operations admit the same k-rank quotient, and exhibit exact information-loss witnesses if not.

Publication is an unreviewed portable scientific artifact, not a formal CLAIM, Result, Review or Foundation promotion. Source P000 and the locked scientific input pin remain unchanged.
