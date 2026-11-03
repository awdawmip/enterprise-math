# Stage394-B — Sharp finite-POP memory for signed-X6 BRC paths

Date: 2026-11-03 (Asia/Shanghai). Research2; follows Stage393-B. Classification: author-side exact combinatorial theorem, executable corroboration, UNREVIEWED / NOT_ADMITTED. This is a typed Path-formal result; POP is a history-stack operation, not an established physical reversal or heartbeat law.

## Frozen basis, model and observer

Science pins: `awdawmip/enterprise-math@2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, global scientific context `awdawmip/chatgpt-global-knowledge@bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, exact P000 V5 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral rules independently sourced from canonical main. Frozen native sources: `research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md` and `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`. Stage393-B author-side input: Research2 PR #1736 commit `3ca4582cea6fedeeee1501f01b49901229ab5862`.

Fix a chart-relative Cell anchor in the native signed X6 torsor. Alphabet `A={+E_i,-E_i : 1<=i<=6}` has twelve letters. A Path-formal ordered word `w=d_1...d_m` has endpoint `z(w)=sum(delta(d_j))` in `Z^6`, and `tau(w)=sum_{j=2}^m [d_j != d_{j-1}]`. Source `sigma` is retained independently. For each of the twenty 3-element axis subsets S, retain the ordered three-component relative readout `R_S(z)=(z_i-b,z_j-b,z_k-b)`, with `b=min(z_i,z_j,z_k)`, including its third component. Also retain `h(z)=min_{1<=i<=6}z_i`; together these reconstruct the signed six coordinates. The endpoint BRC readout is the *frozen all-length signed-path count* `N_m(z)` using the exact multinomial/opposite-pair formula of the cited source; it is not a phase-amplitude or physical time model.

The current observer is `O(w,sigma)=(sigma,(R_S(z))_{|S|=3},h(z),m,N_m(z),tau(w))`. Future operations are the path-typed `APPEND(d):w -> wd` and `POP(wd):wd -> w` (only on nonempty words). A future operation sequence is admissible at budget H if it contains at most H total POP operations, interspersed with arbitrarily many APPEND operations. Read O after every operation or at any selected future endpoint. `m` is the Path-formal step index, not independently identified with a heartbeat interval.

For any H>=0, set `s_H(w)=the last min(m,H+1) signed letters of w` (empty word gives empty suffix). Define exact future equivalence `w ~_H v` on one current O-fiber when *every* admissible future sequence produces identical O readouts.

## Theorem 394.1 — Exact necessary and sufficient history quotient

For all H>=0, all source tags, and any ordered signed-X6 words w,v with `O(w,sigma)=O(v,sigma)`, the following are equivalent:

1. `w ~_H v` under all future APPEND/POP sequences with at most H total POPs;
2. `s_H(w)=s_H(v)`.

Consequently for a *fixed current observer fiber* `F_o=O^{-1}(o)`, its **exact** minimum number of distinguishable additional memory states is

`q_H(o) = | { s_H(w) : w in F_o } |`,

and the exact fixed-width bit minimum is `ceil(log2(q_H(o)))` (zero for q=1). This is an observer- and fiber-relative equality, not the claim that every fiber attains `12^(H+1)`.

**Sufficiency and executable descent.** Keep `(z,m,tau,tail,r)` where `r` is the remaining POP budget and `tail=s_r(w)`. Every APPEND(d) adds `delta(d)` to z, increments m, adds one turn exactly if `m>0` and old `last!=d`, and sets `tail=s_r(wd)` by appending d and discarding the now-unneeded oldest letter. Every POP is permitted only if `r>0,m>0`: read the terminal letter d from tail, set `z'=z-delta(d)`, `m'=m-1`, `tau'=tau-[m>1 and penultimate!=d]`, `r'=r-1`, and `tail'=tail without its last letter`. This is precisely `s_{r'}(POP(w))`; the older undisclosed letters cannot become reachable with r' remaining pops. The current native BRC `N_{m'}(z')` is determined by `(z',m')` using the frozen source kernel, and the twenty R_S and h by z'. By induction, any finite mixed operation sequence with total POP count <=H has exactly matching observations from equal initial `(O,s_H)`.

**Necessity.** Suppose `O(w)=O(v)` and the last H+1 letters differ. Let j be the smallest positive distance from the end where they differ. If `j<=H`, perform j POPs. The last j-1 removed signed labels are identical and the j-th removed signed letters have different native displacements, hence the resulting six-coordinate endpoints differ; O separates them. If `j=H+1`, perform H POPs. Their resulting O either already differ, or both still agree but their remaining last labels differ. In the latter case APPEND the first word's last label. Its turn count changes by zero, while the second word's changes by one, so O separates them. This sequence uses at most H POPs. If m<H+1 the same argument uses j<=m<=H. Hence unequal relevant suffixes are future distinguishable. QED.

## Theorem 394.2 — Exponential lower bound, finite budget

For each n>=1 and every choice of axis indices `i_1,...,i_n in {1,...,6}`, let

`w_(i_1,...,i_n)=(-E_1)(+E_(i_1),-E_(i_1)) ... (+E_(i_n),-E_(i_n))(+E_1)`.

These `6^n` distinct ordered words all have `z=0`, `m=2n+2`, `tau=2n+1`, last label `+E_1`, and all source/BRC/triple/depth observations identical. Each adjacent pair of signed labels is different because every positive/negative transition changes sign. Their `s_(2n)` suffixes are pairwise distinct (exactly the n choices of positive/negative cancelling blocks followed by +E_1); Theorem 394.1 makes them pairwise future distinguishable with at most `2n` POPs. Therefore, for every H>=2,

`max_o q_H(o) >= 6^floor(H/2)`;

and the corresponding worst-fiber memory needs at least `ceil(floor(H/2)*log2(6))` bits. A direct general bound is `q_H(o)<=12^min(m,H+1)`; the exact minimal value remains the fiber formula in Theorem 394.1. In particular, finite H always has a finite suffix repair, while required information grows at least exponentially in H when the length is allowed to grow.

## Theorem 394.3 — Unlimited POP requires complete path history

Let all finite admissible APPEND/POP words be available, without a fixed cumulative POP budget. For any two distinct ordered paths in one current O-fiber, choose their first differing signed letter from the **right** at distance j. If j<m, POP j times and compare endpoints, as in Theorem 394.1. The case j=m with all other letters equal is impossible since their original endpoints agree and a signed native letter has a unique six-coordinate displacement. Hence every two distinct histories in one O-fiber are future distinguishable by POP alone. Exact future equivalence is **equality of the ordered Path-formal words**. The full word/stack is sufficient; no uniform finite-memory repair exists for variable m, by the `6^n` family above. This is an exact unbounded-horizon result for this declared observer/operation language, not a claim that all native physical dynamics require unbounded memory.

## BRC branch fidelity and finite exact checks

The underlying signed-X6 endpoint kernel is unchanged. For m,z, `N_m(z)` counts all twelve-letter ordered paths, with the source's factorial/opposite-pair formula. The executable checker independently compares that source formula to the native twelve-label dynamic recurrence `N_(m+1)(z)=sum_(d in A) N_m(z-delta(d))` for all endpoints and lengths 0..5. The POP implementation does not attempt to invert aggregated BRC multiplicities; it uses the typed terminal branch label, and recomputes N from updated endpoint and length.

Executed `REPRO_STAGE394B_SUFFIX_POP.py` twice with byte-identical stdout. Exact finite coverage: 4,043 native BRC endpoint comparisons, 16,500 DP edges, 65,960 within-observer-fiber pair checks for H=0..4 on a four-letter test subalphabet and lengths 0..5, 32,395 mixed-operation compressed-state assertions, and complete distinct-suffix witness families of `6^n` paths for n=1..5. All computations use integer arithmetic and exact Fraction coefficients. The finite checks corroborate the universal arguments, which do not rely on sampled paths.

## Status and next independent question

**Completed mathematical scope:** exact minimal *per-fiber* future-memory equivalence for total-POP budget H and full A, exponential witnesses, and identity equivalence under unbounded POP. POP is a syntactic Path-formal undo and does not reverse a physical Cell or heartbeat event. Full source-provenance, joint/field state, signed amplitude and actual time evolution are not collapsed by this suffix theorem; source labels and branch multiplicities remain typed. This is independent author-side research, with no asserted native CLAIM, Result, review acceptance or Foundation promotion.

**Next Stage395-B:** classify a richer native BRC observer containing signed/weighted branch histories or joint relation labels and specify whether a *restricted physical* inverse move can be represented by the typed POP model. Investigate finite reversible-window memory when only selected labels can be undone, and test whether the exact suffix partition coarsens in that typed restricted operation class; retain full-X6 triples and future-observation quantifiers.
