# R284AP — Primewise modular exterior spans and final-basis closure certificates

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Lineage: R284AO modular bounded-bit exterior spans; R284AN intrinsic-rank integer spans; R284AM paired exterior spaces.
Frozen scientific source pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Scope: finite rational auxiliary Port observer with independently named diagonal edits; no native X6 dynamics or lossless quotient of undeclared future operations. P000 and the ACTIVE Heartbeat worldview are unchanged.

## AP1. A sharper coverage bound

Let `X,Y ∈ Z^{m×k}`, `C=XY^T`, `M=max(1,|X_ia|,|Y_ia|)`, and `d(C)=max({0}∪{|S|:det C[S,S]≠0})`. This construction also applies after exact rowwise denominator clearing of rational thin factors: each principal minor is multiplied by a nonzero product of row scalars.

By Cauchy–Binet, for every `S⊆[m]` with `|S|=j≤k`,

```
det C[S,S] = Σ_{I⊆[k], |I|=j} det X[S,I] det Y[S,I].
```

The Leibniz bound gives `|det X[S,I]|, |det Y[S,I]| ≤ j! M^j`; therefore

```
|det C[S,S]| ≤ H_j := binom(k,j)(j!)²M^{2j},
H := max(1,H_1,...,H_k) ≤ 2^k(k!)²M^{2k}.                (AP1)
```

Select any **distinct primes** `P={p_1,...,p_l}` with product `Q=∏p>H`. Define `d_p(C)` as the greatest order of a nonzero principal minor of `C mod p`. Then

```
                   d(C) = max_{p∈P} d_p(C).              (AP2)
```

Indeed, every nonzero minor mod `p` is a nonzero integer minor, so `d_p≤d`. Conversely choose a true nonzero principal minor `Δ` of maximal order. If all primes divided `Δ`, their product `Q` would divide the nonzero integer `Δ`, contradicting `|Δ|≤H<Q`. Thus some `p` sees its exact order.

**Key simplification against R284AO:** no rational independence decision is performed during a modular run; the complete DP can be evaluated separately over each field. The bound `H` is on *principal-minor values*, not on the much larger determinants of exterior-state matrices. Hence one can use the first primes until `Q>H`, requiring at most `floor(log_2 H)+1` primes, with `log H=O(k log k+k log M)`. R284AO's per-grade full-rational-span recovery remains valid, but this new route avoids its `D_j!,(j!)^{2D_j}M^{2jD_j}` prime-product bound, where `D_j=binom(k,j)^2`.

## AP2. Exact per-prime exterior DP

For a named subset `S={s_1<...<s_j}`, define
`a_S=∧_{i∈S}x_i`, `b_S=∧_{i∈S}y_i`, `z_S=a_S⊗b_S` in `W_j=(∧^j F_p^k)⊗(∧^j F_p^k)`, of dimension `D_j=binom(k,j)^2`. Let `ell_j(a⊗b)=Σ_{|I|=j}a_I b_I`, extended linearly; this has the exact interpretation

```
ell_j(z_S) = det C[S,S] (mod p).                        (AP3)
```

For each `p`, initialize `B_0={z_empty}` and empty higher-grade bases. Process named indices `i=1,...,m`, updating grades in **descending order**: from every retained true subset `S` in the previous grade-`j−1` basis, form `z_{S∪{i}}` and insert it into grade `j` iff linearly independent over `F_p`. Because the extension `E_i:W_{j-1}→W_j` satisfies `E_i(z_S)=z_{S∪{i}}` for `i∉S` and `0` otherwise, and is linear, the retained states span all grade-`j` named subset states over `F_p`. There is **no** need to align modular bases across primes. Determine `d_p` from nonzero `ell_j` values on the final true-state bases and combine them using (AP2).

The algorithm handles arbitrary signs and exact cancellations. Its arithmetic/bit costs are polynomial in `m`, `log M`, `k`, and the intrinsic exterior-state total dimension `D=Σ_j D_j=binom(2k,k)`; this is an FPT algorithm in `k` with a polynomial rather than `D_j`-scaled prime-budget exponent. Exact thin factorization and denominator clearing are counted separately. A detected named subset `S` can be verified by direct exact evaluation of `det C[S,S]`.

## AP3. A compact **post-hoc** closure certificate

A second result replaces the full streaming decision transcript with independently checkable **final** basis labels.

For each prime and grade choose a set `B_j` of **true named-subset states** (not arbitrary echelon combinations), with `B_0={z_empty}`. The following conditions are sufficient and necessary for `B_j` to be a basis of the span of *all* grade-`j` true states:

1. The states in `B_j` are linearly independent over `F_p`.
2. For every `j=1,...,k`, every `b∈B_{j−1}`, and **every** named index `i∈[m]`, `E_i b∈span(B_j)`.

**Proof:** Every labelled `B_j` state belongs to the true grade-`j` span. By induction, all true states of grade `j−1` lie in `span(B_{j−1})`. Every true grade-`j` state is `E_i` of a true grade-`j−1` state, and linearity plus condition 2 puts it in `span(B_j)`. Independence gives equality. The base `j=0` is immediate. As both wedge factors acquire the same sorting sign, `E_i z_S=z_{S∪{i}}` exactly; if `i∈S` the wedge is zero.

Thus the verifier only needs the original integer factors, the primes/product bound, final named-subset basis labels, independent modular rank checks and all `E_i` closure checks. Zero traces on `B_j` prove **every** grade-`j` principal minor vanishes modulo `p`; combining all primes with (AP1) proves the corresponding integral zero claim. Positive certificates contain an exact nonzero named principal minor. This is an actual independent verifier of the *stored final bases*, not a rerun of the incremental construction.

A verifier may perform `O(mΣ_j |B_{j−1}|)` field-span inclusion tests per prime, each in at most `D_j` coordinates. It does not enumerate `binom(m,j)` subsets. The labels themselves require `O(kΣ_j D_j)` indices per prime. An arbitrary list of final traces **without** rank/closure proof would not be a negative certificate.

## AP4. Exact calculations and reproducibility

Companion standard-library script: `R284AP_primewise_modular_principal_rank_checker.py`.
Evidence file: `R284AP_exact_verification.json`.

The script uses fixed seed 284016 and an independent integer Leibniz-determinant oracle. Its local executed results:

- 87 integer-factor instances, including an explicitly nilpotent matrix with `d=0`, a positive diagonal example, the mixed-prime case `C=[2]`, and 84 signed random instances with `2≤m≤6`, `1≤k≤min(m,3)`: **87/87** agreement with exhaustive exact principal-minor enumeration.
- 4,327 candidate modular states and **7,144 independent final-basis closure tests**; all PASS.
- At most **6** primes in these 87 instances; at most 15 bits for `H` and `Q`. Modular maximum degrees differ between primes in 52 cases, showing the need to combine fields.
- In `C=[2]`, `H=4`, `P={2,3}`: `d_2=0`, `d_3=1` and `d(C)=1`. One single small prime would miss the witness.
- A separate `m=64,k=3` signed fixed-seed probe produced `d=3`, witness `S={1,4,5}` (1-based), `H=9,437,184` and 8 primes. This larger probe is a constructive witness check, not an exhaustive 64-row enumeration.

These finite tests are regression evidence; the general theorem follows from (AP1)–(AP3), the exterior-span recurrence, and the final-closure induction. Independent review remains NOT_REVIEWED.

## Port/BRC observer scope and next questions

For the auxiliary named-diagonal pencil `M_C(u,v)=[[diag(u),I_m],[C,diag(v)]]`, the existing block identity `det M_C=det(diag(u_iv_i)−C)` yields `ν(M_C)=2(m−d(C))`. R284AP computes this degree exactly for integer/rational thin-factor inputs.

Its compression preserves exactly the stated `C`, its signed principal-minor responses, and all independently named diagonal edits. It does not erase path identity, provenance, joint BRC branches, or future operations outside that observer; those remain available for separately typed observer-safe descent analysis. P000, the six-axis ACTIVE Heartbeat basis and the frozen scientific pin remain in force.

Next useful units: (i) independently audit the final-basis certificate on R284AK's positive non-symmetric gap family, (ii) compare full preprocessing+execution+certificate-check costs of R284AN, R284AO and this primewise method on identical inputs, (iii) exploit block/SCC sparsity before exterior-span expansion, (iv) determine whether a declared non-diagonal Port intervention is safe under the same factor reduction, constructing an exact distinguishing witness when it is not.

Publication of this portable research note creates no formal CLAIM, Result, Review, or Foundation admission.
