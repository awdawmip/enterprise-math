# R42 — Exact integer-recurrence certificate for historical source ownership

Date: 2026-11-10. Status: AUTHOR-SIDE PROOF AND EXACT TESTS, INDEPENDENT REVIEW PENDING.

Scientific freeze: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: [R41, PR #1978](https://github.com/awdawmip/enterprise-math/pull/1978).
This concerns the auxiliary irrational-circle historical observer and its provenance-preserving labels. The native P000/X6 Heartbeat World is unchanged; no native-X6 physics, Shor, or physical-residual conclusion is inferred. The computation uses rational enclosures and integer circle arithmetic without trigonometric or π computations.

## 1. Exact model

Fix irrational 0<θ<1 with certified rational enclosure ℓ≤θ≤h. Write ℓ=A/D and h=B/D with common D>0 and integers A≤B. Let Q=2D, U=A+B, δ=B−A and θ₀=U/Q. Hence |θ−θ₀|≤δ/Q. Let the m historical cutpoints be {zθ}, for z=0,...,m−1, with cyclic half-open arcs I_k carrying their original index labels. We seek each exact last source

τ_k = max {t in [J−N,J): {tθ} in I_k},

using None if empty, for integers J, N≥1. Define r_s=(sU) mod Q. Sorting (r_z,z) produces the labelled historical cyclic order at θ₀.

## 2. Historical-order certificate

For any consecutive historical labels a,b in sorted cyclic order, set g=(r_b−r_a) mod Q. Require

0 < g < Q,  g>δ|b−a|,  Q−g>δ|b−a|.       (H)

The unreduced angular difference (b−a)θ differs from (b−a)θ₀ by at most δ|b−a|/Q. Both oriented circular gaps g/Q and 1−g/Q therefore stay positive. Any change in the cyclic order of historical labelled points would require an adjacent pair to collide. (H) excludes this at every θ in the enclosure. Thus all historical arc labels and adjacency relations are stable throughout the enclosure.

## 3. Per-source certificate and exactness theorem

For a candidate source t whose θ₀-phase r_t is in the cyclic arc from historical a to b, set

L=(r_t−r_a) mod Q, R=(r_b−r_t) mod Q.

Check L+R=g and

L>δ|t−a|,       R>δ|t−b|.              (S)

There is also the exact half-open left-endpoint case t=a,L=0; retain it if R>δ|t−b| and the historical ordering is certified.

**Theorem.** If (H) holds for all historical adjacent pairs and (S) holds for t in its selected arc (or the exact half-open equality case), the selected historical owner of t is correct for every irrational θ in the enclosure.

**Proof.** Under θ−θ₀, the oriented difference from a to t changes by at most δ|t−a|/Q and the difference from t to b changes by at most δ|t−b|/Q. Condition (S) keeps both differences positive. They cannot wrap through 1 either: Q−L=(Q−g)+R>δ(|b−a|+|t−b|)≥δ|t−a| by (H) and the triangle inequality. Likewise Q−R=(Q−g)+L>δ|t−b|. Thus both angular distances stay in (0,1), with their orientations fixed. Because their sum equals the historical arc length at θ₀ and (H) preserves that arc, t remains inside the same historical arc. If t=a, its phase equals the included left boundary identically for every θ, proving that case. ∎

When a strict certificate fails, the algorithm returns Uncertified. A wider interval is not silently rounded to a chosen label; use a narrower proven enclosure or an exact alternate method.

## 4. Integer recurrence / source-select theorem

Compute r_(J−1)=((J−1)U) mod Q exactly once. Older source phases obey

r_(t−1) = (r_t−U) mod Q.

Since 0<U<Q, this needs only one integer subtraction and possibly one addition of Q per source. Binary search in sorted r_z finds the candidate owner in O(log m) integer comparisons, followed by two exact boundary-margin tests (S). Scan backwards for at most H≤N certified sources.

By R41's suffix theorem, the FIRST backward encounter of each historical owner is its exact last source in the entire source window; if all m owners have appeared, stop immediately. If H is exhausted with some unseen owners, solve ONLY those coordinates by the R40 endpoint-coboundary rank/select. Both procedures return the same labelled vector, because the suffix positions are the most recent positions in the complete window and R40 selects exact maxima. Therefore the hybrid result is exact whenever the stated enclosure certificates and R40 fallback preconditions hold. ∎

## 5. Bit-cost accounting

Let b=ceil(log₂(Q+1)), j=ceil(log₂(max(2,|J|+N))) and M(x) be a multiplication upper bound for x-bit integers. On the all-covered certified suffix branch, including the cost of a common-denominator representation (whose LCM construction is charged explicitly), m historical phase residues require at most O(m M(b+log m)) bit operations. Sorting and certifying history costs O(m b log m). There is one initialization product/remainder with O(M(b+j)). Each of H scanned sources incurs one O(b) modular subtraction/addition, O(b log m) comparison cost, and two exact integer margin products, conservatively O(M(b+j)). Explicit m-item absolute source serialization costs O(mj) bits. Hence this branch has the conservative bound

O( input_conversion + m M(b+log m) + m b log m
   + M(b+j) + H [M(b+j)+b log m] + m j ).

If θ has bounded continued-fraction partial quotients ≤A, the R37 coverage bound provides H=O_A(m) for sufficiently long source windows, giving a specified-bounded-type, bit-cost bound independent of the numeric magnitude of N except its index length. The R40 fallback adds its own batch-threshold counts and exact floor operations; the Farey-stage generator and K emitted affine-risk intervals are separate full-compiler costs.

A serialization lower bound of Ω(mj) is claimed only for the explicit m absolute-source-integer representation, not for compressed ages or deltas.

## 6. Exact evidence and scope

The executable VERIFY_R42.py and pinned predecessor oracle REFERENCE_R41.py use the Python standard library with Fraction, isqrt and integer operations. Eight families are checked against the existing R41 full Fraction implementation AND its independent Euclidean Floor Sum last-source reference. Short finite, historical-boundary and negative-index cases also compare with literal finite brute-force reconstruction. An intentionally broad enclosure is rejected as Uncertified. Certificates: CERTIFICATE_R42.json; local performance: BENCHMARK_R42.json.

The frozen S23/AV case is θ in [262204504569236716045286,262204504569236716045287]/10^24, m=128, J=10^12+128, N=10^9. Exactly 164 certified probes cover all 128 labels; 328 integer boundary-margin tests, one stream-initialization product, 163 modular subtractions, zero per-source Fraction phase products and zero R40 fallback floors. All 128 last-source values match both reference paths.

R41 previously generated all 298 affine intervals. Equality of the complete labelled source vector together with R41's substitution lemma preserves its predicted risk intervals at the affected source-selection step. An independent direct R42-integrated 298-interval compiler replay is the next research unit; the present test does not assert that replay was executed.

Python benchmark medians in BENCHMARK_R42.json cover three local timings of R42 versus the included R41 Fraction-based implementation. They are implementation-specific observations, not a general speedup theorem.

## 7. Next research unit

R43: insert R42 into the complete R41 R33/R36/R32 compiler and actually regenerate both R42-suffix and R40-fallback 298-interval outputs; batch multiple adjacent J values via a maintained modulo-phase state; investigate certificate refinement when width δ/Q is insufficient, including input-conversion/bit-cost tradeoffs. Independent review and formal shared task authority remain separate Source decisions.


## 8. Verified end-to-end addendum (2026-11-10)

R42 recurrence-first and R40 endpoint-only preparation were actually executed in the frozen R41/R33/R36/R32 compiler. Both recreated all 298 affine intervals byte-for-byte (SHA256 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6), with final risk -4017401528447 + 15321634290944 θ. See VERIFY_R42_INTEGRATION.py and INTEGRATION_EVIDENCE.md. This supersedes the earlier §6 pre-integration state. Independent review remains pending.
