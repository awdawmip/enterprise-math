# R40 — Endpoint-coboundary batched owner counts (2026-11-10)

**Status:** Author-side mathematical derivation, exact verification; independent project review pending.
**Scientific freeze:** S23/AV `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
**Parent:** R39 `299f6986939404fbb10e9085a111a5bd462180ab`, shared historical-cutpoint Floor Sum.
**Scope:** Auxiliary irrational circle-rotation observer with historical arc/source labels; P000/native X6 semantics unchanged.

## Exact theorem R40.1

Fix irrational `0<θ<1`, integer `m≥2`, and the distinct historical cutpoints `x_z={zθ}` for `0≤z<m`. For any successive *phase-sorted* historical indices `a,b` (`a≠b`), let `I_(a,b)` be the corresponding half-open counterclockwise circle arc; `w=1` when the arc wraps through zero, otherwise `w=0`. Its length is `λ=x_b-x_a+w>0`. For integer `L≤J`, define `n=J-L` and the label-preserving source count

`C_(a,b)(L,J)=#{t∈Z:L≤t<J, {tθ}∈I_(a,b)}`.

Let `S_z(L,J)=Σ_(t=L)^(J−1) floor((t−z)θ)`.
R39's direct interval-indicator identity is

`C_(a,b)=S_a−S_b+n(floor(aθ)−floor(bθ)+w)`.  (A)

Define `P_0=0` and for `r=0,…,m−2` set

`P_(r+1)=P_r+floor((J−1−r)θ)−floor((L−1−r)θ)`.

**Then for every owner arc, simultaneously:**

`C_(a,b)(L,J)=P_b−P_a+n(floor(aθ)−floor(bθ)+w).`  **(1)**

**Proof.** The difference between successive historical translations telescopes over the integer source:
`S_(z+1)−S_z=Σ_(t=L)^(J−1) [floor((t−z−1)θ)−floor((t−z)θ)]`
`=floor((L−1−z)θ)−floor((J−1−z)θ)`.
Thus `S_z=S_0−P_z`, and (1) follows from (A). Formula (A) follows by writing the half-open circle-arc indicator as the difference of the two boundary-crossing floor increments plus the winding integer; summing the identity from L to J−1 gives the stated count. All terms are exact integer identities. QED.

**Computational conclusion.** Precompute the `m` historical floors `floor(zθ)` and `m−1` right-end floors `floor((J−1−r)θ)`. Every subsequent *common* left threshold L requires only `m−1` scalar floors, the prefix vector P, and O(m) integer additions, and yields **all m labelled owner counts** at once; no Euclidean Floor Sum call is required by (1). This is a new application of the classical orbit-endpoint coboundary principle to the R39 batch source selector, not a novelty claim about bounded-remainder theory.

## Exact theorem R40.2 — explicit discrepancy / suffix coverage

Let `d=|b−a|` (so `1≤d≤m−1`). Every summand `floor((J−1−r)θ)−floor((L−1−r)θ)` differs from `nθ` strictly by less than 1, since it is the difference of two real values whose separation is `nθ`, minus the corresponding fractional-part difference. The P difference in (1) contains exactly d such terms, with a common sign, hence, for `n>0`,

`|C_(a,b)(L,J)−nλ|<d`. **(2)**

For `n=0` both sides vanish exactly. Any integer suffix length h with `hλ≥d` therefore satisfies `C_(a,b)(J−h,J)>0`. With a certified `0<λ_lower≤λ`, the computable length

`H_(a,b)=floor(d/λ_lower)+1` **(3)**

is a valid guaranteed-hit cutoff. Taking the maximum over historical arcs gives a last-source saturation guarantee independent of the magnitude of J. An especially small λ makes (3) less efficient; that is useful information for algorithm selection.

**Proof details of (2):** Let `f_r=floor((J−1−r)θ)−floor((L−1−r)θ)`. Then `f_r−nθ={ (L−1−r)θ }−{ (J−1−r)θ }`, strictly between −1 and 1 (irrational θ and n>0). The signed sum over d distinct r’s bounds the deviation by d, while the coefficient of n in (1) equals λ. QED.

## Certified rational parameters and last-source selection

Use strictly certified rational bounds `θ_lo≤θ≤θ_hi`. For every input integer s, certify each scalar floor by testing `floor(s θ_lo)=floor(s θ_hi)`, including negative s. For historical phase order, certify floors for each nonzero historical index difference, which fixes pairwise circular positions across the enclosure. A failed enclosure check means refine the exact rational bounds before making that query.

For all owner arcs jointly, maintain exponential-search brackets of the last surviving source, then binary-search their final locations. Group identical threshold requests L and cache one complete vector (1) per distinct L. Last source t for owner k is identified by `C_k(t,J)>0` and `C_k(t+1,J)=0`; when `C_k(J−N,J)=0`, report no source. Owner label identity, multiplicity, and negative source indices are preserved. Compact verifier checks both rational-bound endpoints and the R39 Euclidean Floor Sum oracle.

If Q distinct common thresholds are queried, exact scalar floors are at most `2[(2m−1)+Q(m−1)]` when certification evaluates both enclosure endpoints; integer prefix work is O(Qm) and memory O(Qm) if retaining all count vectors. This is a scalar operation-count statement; bit-operation complexity must include bignum length of J, source window size, parameter rational precision, phase sorting, and serialization. R39 may remain faster for some m/threshold profiles.

## Reproducible evidence

Author-side full program `VERIFY_R40.py`: 14 exact parameter families, historical m in {16,21,31,32,50,72,128,129,257}, near-rational irrational θ and sqrt(2)−1/sqrt(3)−1. Tested owner-labelled last-source equality against an independently programmed Euclidean Floor Sum selector, both rational enclosure endpoints, disappearance at t+1, two short brute-force source windows and a negative-index window [-41,9). Completed:
`PASS_R40_ENDPOINT_COBBOUNDARY_14_CASES`.
Full certificate SHA-256: `c5338336afd23f3bba4b76732f0d19d57b9a36003d09a8d7ec65480fb0c8b76a`.

The published `VERIFY_R40_COMPACT.py` independently checks all historical arc counts at four thresholds and owner last-source endpoints for four families. Completed:
`PASS_R40_COMPACT_FOUR_EXACT_FAMILIES`.

Local Python microbenchmarks (three runs; medians, not complete bit-complexity) comparing R39 and R40 respectively: near-third m=21 5.424/0.849ms, mixed m=128 13.013/8.789ms, mixed m=257 (45 selected narrow owners) 8.335/8.615ms, near-third m=21 at J=10^15 6.309/0.946ms. The full 14-family source, certificate and microbenchmark are retained together in the locally generated `R40_RESEARCH_BUNDLE.zip`. R40's exact local experiment is not a rerun of the full 298-affine-segment S23 prediction.

## BRC observer typing and successor

The carrier is the exact owner-labelled count vector, not just its total count n; source identity remains observable. Existing typed BRC provenance/observer-retention principle is **REUSE_APPLIED**, with no new accepted BRC tool, native triadic dynamical theorem, or P000 promotion. Next, R41 should integrate this batch selector into frozen S23/AV's four initial and 298 total risk blocks, compare full exact runs and bit-cost profiles, and adaptively select between R37 suffix scanning, R38 modular channels, R39 Euclidean Floor Sum, and R40 endpoint coboundary.

Background context: H. Kesten, *On a conjecture of Erdős and Szüsz related to uniform distribution mod 1*, Acta Arithmetica 12 (1966), 193–212.