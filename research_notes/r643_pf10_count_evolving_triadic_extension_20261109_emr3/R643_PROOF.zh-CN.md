# R643｜PF10 计数演化的精确观察同余与六步奇 holonomy 保持

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_SIDE_EXACT_THEOREM / EXPLICIT_CANDIDATE_EXTENSION / UNREVIEWED / NOT_ADMITTED.

## 0. Source and scope

Frozen signed BRC science: R462 @ `18783e01e3646c72b7aab3b16d3f565e83e6446f` (unchanged).
Exact typed inputs: enterprise-math @ `b62110008321d9147212cb89f2627ff613c2550d`:
- `research_notes/X6_CHANNEL_NONRECIPROCITY_CIRCULATION_BRIDGE_V26_20260906.md`;
- `research_notes/X6_ATOMIC_TRIADIC_PASSAGE_DRIVES_ODD_HOLONOMY_V27_20260906.md`;
- `experiments/x6_dynamic_law_holonomy_v24_20260906/check_channel_circulation_bridge.py`.
Use R640's 10 signed PF10 contrasts and 14-dimensional integer kernel, R641 PF10 fixed-count V27 congruence, and R642 ordered-triad histogram + mod-3 holonomy residual. V26/V27 fix the count snapshot; **the count-changing law below is a newly proposed auxiliary typed extension**, not an assertion about a deployed or complete native X6 time law.

PF10 source ports are four explicitly injected internal channels, not native X6 axes. The 20 active triads are 3-subsets of six native axis labels, not spatial Cell addresses. One relation step is not asserted to equal a physical heartbeat. Positive Weighted-BRC weights and signed relation scores remain distinct.

## 1. Exact count-changing congruence criterion

Let `X=(I_0..I_3,O_0..O_3,M_00..M_33)∈N₀²⁴`. Define the surjective integer linear map
`T:Z²⁴→Z¹⁰` by `T(X)=(u,Ω)`, `u_i=I_i−O_i` and `Ω_ij=M_ij−M_ji` for `i<j`. R640 proves `ker_Z(T)≅Z¹⁴` with basis `K`: 4 paired `(I_i,O_i)` increments, 6 paired `(M_ij,M_ji)` increments and 4 diagonal `M_ii` increments.

**Theorem A.** For every affine everywhere-nonnegative source update `f(X)=AX+b`, `A∈N₀^{24×24}`, `b∈N₀²⁴`, the following are equivalent:
(i) `T(f(X))` is uniquely determined by `T(X)` for every `X∈N₀²⁴`;
(ii) `TAk=0` for all 14 displayed integer kernel basis vectors `k∈K`;
(iii) a unique `B∈Mat_{10×10}(Z)` satisfies `TA=BT`.
In this case the exact induced update is `z↦Bz+Tb` for `z=T(X)`.

Proof: (iii) implies (i), and (ii) implies (iii) because T is split-surjective over Z: take an integer right inverse R and set B=TAR; then `x−RTx∈ker T` gives `TAx=BTx`. For (i)⇒(ii), given any integer kernel vector k, choose sufficiently large nonnegative x so x and x+k are nonnegative; their T values coincide. Equality of their updated T values gives TAk=0. The 14 integer generators suffice for the full kernel. Uniqueness of B follows from T surjective.

**Exact safe family.** Any nonnegative additive event increment `Δ=Δ(z,S,σ)` chosen from the retained observer state has `z' = z + TΔ` and is therefore observation-safe on its stated future operation language. In particular, `M↦2M` with I,O fixed has induced `B=diag(1,1,1,1,2,2,2,2,2,2)`.

**Exact unsafe affine witness.** Let f add current `M_00` to `I_0`, leaving all other 23 counts fixed. This everywhere-nonnegative source update has `TA(K_{M00})=e_{u0}≠0`. Two V27 source states differing only by `M_00=0` versus `M_00=2` initially have identical `(u,Ω)` and triad history. After f their `u_0` are −2 and 0. For active triad 013 the unique V26/V27 maximizers become 012 and 035 respectively. Thus both the next signed observer and an actual triad successor can split on the same starting observer fiber.

## 2. Single atomic triadic event as a nonnegative count-changing extension

Take V27 initial `I=(0,0,0,10)`, `O=(2,4,3,0)`, and `M=C` with precisely `C_01=C_12=C_20=1` (others 0). Its signed values are
`u=(-2,-4,-3,10)`,
`Ω₀=((0,1,-1,0),(-1,0,1,0),(1,-1,0,0),(0,0,0,0))`.

Define a *candidate* joint relation step:
```
S_(n+1) = argmax_{T: |S_n∩T|=2} [uᵀ c(T) + c(S_n)ᵀ Ω_n c(T)]
I_(n+1)=I_n, O_(n+1)=O_n, M_(n+1)=M_n+C.
```
The finite V23 matching code `c(S)∈Z⁴` and score are exactly those of pinned V26/V27. Then `M_n=(n+1)C`, `Ω_n=(n+1)Ω₀`. The update changes three nonnegative PF10 passage counts on *every relation step*. It preserves the signed quotient and can be coupled to R642's ordered slot transport / (h,q).

For each source-defined directed edge let `a(S,T)=c(S)ᵀΩ₀c(T)` and `v(T)=uᵀc(T)`. Its score at integer n≥0 is
`Φ_n(S,T)=v(T)+(n+1)a(S,T)`.

**Theorem B (unbounded exact curved orbit).** Starting at S₀=012, the complete candidate history follows
`012→123→234→034→035→025→012→...`
for *every* integer n≥0. The inherited slot holonomy after six edges is `(2,1,0)` (odd transposition); after twelve edges it is the identity, while `M_n` strictly grows.

Proof: on each of those six source edges W(S), finite exact evaluation shows `a(S,W)=1=max_{T∈N(S)}a(S,T)` and the strict margin at n=0 is respectively `(4,1,1,4,1,1)`. Hence for any competitor T and n≥0,
`Φ_n(S,W)−Φ_n(S,T)=[Φ_0(S,W)−Φ_0(S,T)] + n[a(S,W)−a(S,T)] ≥1`.
Thus all six successors remain unique and identical for every n; induction yields the claimed path. Slot transport is the pinned V17 operation, giving transposition after six steps and identity after twelve. No numerical extrapolation is used for the all-n conclusion.

**Theorem C (exact global selector stabilization).** At n=0 all twenty active triads have unique maximizers. For n=1..13, ties occur *exactly* at
`n=1:015; n=2:124,134; n=3:045,345; n=4:125; n=11:245; n=12:135; n=13:014`.
At n=14 all twenty have unique maximizers W(S) satisfying `a(S,W)=max_T a(S,T)`. Therefore all twenty successors remain uniquely identical for every n≥14 by the same increasing-margin argument. The n=13 tie proves 14 is the least threshold after which the whole 20-state selector is everywhere unique and permanently constant. The proof reduces the global infinite assertion to explicit 20×9 integer score comparisons at n=14 plus 14 finite earlier slices, enumerated in the attached exact checker; the complete stabilized successor table is in the evidence JSON.

## 3. What this adds and the next discriminating question

R641 supplied exact operation-safety only for fixed PF10 counts. R643 provides a count-changing PF10 extension that preserves V27's odd holonomy indefinitely **on the specified 012 orbit**, with a fully computed finite tie transition elsewhere; it also gives a 14-generator test to determine whether a general affine count update descends to the ten signed contrasts.

The extension is deliberately an auxiliary admissible nonnegative event law using the already typed atomic 3-cycle. Physical network conservation, neighboring Cell coordination, source-to-port injection, event authorization and native time assignment are still open. Next: extract an actual V28–V43 coupled event ledger and test its update against the 14-generator congruence criterion, then verify locality and conservation on a finite multi-Cell complex. Preserve source-count provenance and R642 path trit until those tests pass.

No P000/ACTIVE changes. No formal task CLAIM, RR/DR or independent mathematical admission is claimed.
