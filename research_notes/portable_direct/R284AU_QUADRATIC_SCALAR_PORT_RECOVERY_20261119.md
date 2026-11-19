# R284AU — O(n²) exact scalar Port observations suffice for bounded positive rational cores

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Lineage: R284AR → R284AS → R284AT. Historical frozen scientific input pin retained from R284AT: R284AR @ 43ec6098b1330ae86d0a7863be336c5d97f6ef34. This is an auxiliary named Port-channel observer inside P000's six-spatial-axis Heartbeat World research, not an independent native lower-dimensional geometry. Current behavioral rules were read separately from frozen science.

## 1. Main theorem: finite scalar readouts, with polynomial bit complexity

Let n≥2, let b and M≥1 be known positive integers, and let the unknown matrix C=A/b have all integer numerators A_ij∈{1,…,M}. At one specified rational diagonal d=(d_i), and a chosen ordered edge (u,v) with edit z, the observer returns one exact rational scalar
    O_C(d,z;u,v)=det(diag(d)-C-z E_uv).
An unedited observation has z=0. Names, edit directions and signed determinant values are retained.

Given ANY oriented spanning tree E on [n], the entire A, hence C, can be reconstructed with at most
    Q(n)=n+binom(n,2)+(n-1)+2(n-1)(n-2)=O(n²)
exact scalar determinant observations. Every chosen diagonal entry lies in {0,L/b}, and z∈{0,1/b}, with the same universal integer
    B=n! (M+1)^n,     L=2B+2.
Each scalar query has O(n log n+n log(M+1)+log b) bits of rational query input, and the exact determinant output has polynomial bit length. Postprocessing and determinant calculation are polynomial-bit under this declared bounded-common-denominator model. This theorem is an upper bound; it is not a claim about arbitrary unbounded-height rationals, noisy scalar observations or universal query optimality.

## 2. Single-scale coefficient extraction lemma (zero-error)

For T⊆[n], S=[n]\T, s=|S|, and e∈{0,1}, define B_e=A+eE_uv (for e=1 choose u,v∈T) and
    P_{T,e}(t)=det(t diag(1_S)-B_e)=∑_{j=0}^s a_j t^j.
By determinant multilinearity, its leading coefficient equals
    a_s=det(-B_e[T,T]).
Each coefficient is a sum of at most binom(s,j) principal minors of order n-j. Since the entries of B_e have absolute value at most M+1, the Leibniz formula yields
    |a_j|≤binom(s,j)(n-j)!(M+1)^(n-j)≤n!(M+1)^n=B.
Therefore
    |P_{T,e}(L)/L^s-a_s|≤∑_{h=1}^s B/L^h<B/(L-1)<1/2
for L=2B+2. Taking the nearest integer RECOVERS a_s EXACTLY. The statement also holds when s=0, when the expression is already a determinant.

The original rational oracle at d_i=L/b for i∈S (otherwise d_i=0) and z=e/b gives
    b^n O_C(d,z;u,v)=P_{T,e}(L),
so a single scalar rational readout supplies the exact targeted principal coefficient. Integer L has O(n log n+n log(M+1)) bits. The absolute integer determinant has the bound n!(L+M+1)^n and hence O(n²(log n+log(M+1))) bits; rational input/output scaling contributes O(n log b) bits. Exact fraction-free elimination is adequate. No multivariate polynomial expansion or limiting operation is used.

## 3. Tree reconstruction with O(n²) scalar reads

Denote the extracted leading coefficient by ℓ_T(e). First read ℓ_{ {i} }(0) for each i:
    α_i=A_ii=−ℓ_{ {i} }(0).                                      [n calls]
Next read ℓ_{ {i,j} }(0) for all unordered pairs:
    p_ij=A_ij A_ji=α_i α_j−ℓ_{ {i,j} }(0).                   [binom(n,2) calls]
For each oriented tree edge (u,v), read ℓ_{ {u,v} }(1). Direct 2×2 cofactor expansion yields
    A_vu=ℓ_{ {u,v} }(0)−ℓ_{ {u,v} }(1),
    A_uv=p_uv/A_vu.                                          [n−1 further calls]
For every w∉{u,v}, read ℓ_{ {u,v,w} }(0) and ℓ_{ {u,v,w} }(1). A direct 3×3 cofactor gives
    ℓ_{ {u,v,w} }(1)−ℓ_{ {u,v,w} }(0)
      = A_vu α_w−A_vw A_wu,
so the labeled two-step path product is
    q_{(u,v)|w}=A_vw A_wu=A_vu α_w−(ℓ_{ {u,v,w} }(1)−ℓ_{ {u,v,w} }(0)).
This takes at most 2(n−1)(n−2) more calls (caching identical unedited triple values saves calls).

Fix a root x and its unique tree path x=v₀,v₁,…,v_k. The tree edges themselves are known in both orientations. Suppose A_{x,v_i} and A_{v_i,x} are known. For next edge (u,v)=(v_i,v_{i+1}), q_{(u,v)|x}=A_{v_{i+1},x} A_{x,v_i}, so divide by the known A_{x,v_i}, then use p_{x,v_{i+1}} to recover the reverse orientation. For the reversed probe (u,v)=(v_{i+1},v_i), use q_{(u,v)|x}=A_{v_i,x} A_{x,v_{i+1}} instead. Every divisor is strictly positive; induction recovers both directions between x and every other vertex. Repeating over roots recovers all n² entries. This proves the theorem for every n and every orientation of every spanning tree. Positivity, the exact named coefficients and directed path provenance are load-bearing.

## 4. Sharp sparse boundary counterexample (n=2)

Strict positivity cannot be dropped from the AT tree criterion. Consider
    C₁=[[1,1],[0,1]],    C₂=[[1,2],[0,1]].
The single directed edit E_12 has a connected undirected observation graph, but for ALL formal d_1,d_2,z,
    det(diag(d)-C₁-zE_12)=det(diag(d)-C₂-zE_12)=(d_1−1)(d_2−1).
The reverse E_21 intervention gives (d_1−1)(d_2−1)−z C_12 and separates them. In general at n=2 an E_uv readout identifies C_vu, while the unedited pair minor identifies only C_uv C_vu; the case C_vu=0 is the precise failure of the tree reconstruction's division step. This is a *full-polynomial* indistinguishability counterexample, stronger than a finite-sampling failure.

## 5. Exact execution and reproducibility

Companions:
- research_notes/portable_direct/R284AU_scalar_port_checker.py — standard-library Python with exact Bareiss determinants, single-scale integer rounding, arbitrary oriented-tree path recovery, known-denominator oracle scaling, and the zero-support counterexample.
- research_notes/portable_direct/R284AU_exact_verification.json — deterministic seed, tested dimensions, query counts, integer-bit bounds and boundary cases.

The executed local checker reported PASS for 208 deterministic-seed positive integer examples of n=2…7 (40,45,45,40,24,14) and 3 deliberate additional positive boundary examples. In total 5,978 integer determinant scalar-equivalent calls and 637 directed tree edges were checked; the recovered matrices matched entrywise. The maximum tested per-instance call count was 88, maximum probe-base length 32 bits, and maximum determinant-bound length 233 bits. Six independent evaluations with b=37 matched the rational oracle after multiplying by b^n; the n=2 sparse indistinguishability example was also checked. All tests use exact integer/fraction arithmetic. These finite checks are corroboration; the general assertion rests on the algebraic argument above. Formal checker and independent mathematical review: not performed.

## 6. Research continuation

Investigate whether overlapping 3-channel witnesses can reduce the readout bound to n²+O(n) while preserving polynomial precision; extend from known common denominator b/entry bound M to precise finite-height classes; characterize orientation-sensitive sufficient conditions on sparse/signed support; measure finite-precision stability, since the exact high-base method trades large input and output bits for fewer evaluations.

Source-status boundaries: this is independently reproducible portable research and does not itself establish a formal CLAIM, native PROGRESS, Result, Review, Working Truth, Foundation promotion or a native X6 transfer theorem. The existing R284AT scientific freeze and prior author contributions are unchanged.
