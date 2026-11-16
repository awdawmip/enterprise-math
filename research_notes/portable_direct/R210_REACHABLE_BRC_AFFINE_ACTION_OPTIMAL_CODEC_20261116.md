# R210 — Optimal fixed-width encoding of the *full reachable* paired-observer affine action

Date: 2026-11-16 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Scientific input frozen: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Exact dependencies: R200 paired provenance/event quotient, R201 faithful affine representation, R203 selector rows, R209 optimal global rank/unrank.
Output scope: finite observer of native X6 paths; not full path, signed phase, hidden provenance, independent spatial dimensions or a Working Truth promotion.
Source API: `src/enterprise_math/brc_transport.py` at frozen pin, blob `be1debe367263931bd5e93fd750be3ed54624fe1`.

## Question and result

R203's 210-bit selector/constant representation stores any D=35 row-descriptor action, whereas R209's 21-bit rank stores the reachable finite observer state. R201 already proved more: the **entire affine action** induced by any history descends to that state, and distinct states induce distinct actions. Thus the reachable affine action monoid has exactly the same cardinality as the observer quotient. The new result supplies a **direct, history-free synthesis map** from the optimal identifier to every row of the complete affine action, so it is an actual compressed *action* interface, not only an initial-orbit code.

Let m>=1, k>=0, L>=0, event alphabet A=[m]×({0}∪[k]), a=m(k+1), with 0 neutral provenance. Let F(w)=(s,t), where s is the ordered list of distinct last occurrences of selected sources, oldest to newest, and t is the last min(L,|w|) full paired events. Put b=ceil(log2(a+1)), d=k+binom(k,2), D=d+bL. For D=0 the affine singleton is understood abstractly (the installed Affine API needs positive dimension).

Let J be the reachable quotient, N=|J| as exactly counted in R209, and ρ:J→Aff(F^D) the R201 representation over any field F.

### Theorem R210-A: direct action reconstruction

Given (s,t)∈J, the D-row selector/constant description of ρ(s,t) is uniquely synthesized without replaying a generating history:

* For source occurrence row U_i, use CONST(1) if i∈s and SELECT(U_i) otherwise.
* For each pair i<j, use SELECT(V_ij) when neither i nor j occurs in s; otherwise use CONST(1) if last_s(i)>last_s(j), and CONST(0) otherwise, with absent index = −1.
* For tail register slots T_0,...,T_(L−1), let h=|t|. For each slot r<L−h set SELECT(T_(r+h)); for each r>=L−h set CONST(c(t_(r−L+h))), coordinatewise, where c(x) is R201's nonzero b-bit event code x+1.

Proof: A source bit changes precisely when the corresponding source appears in the word; a pair register changes precisely when one of its two sources appears, and the later source determines the final constant. The untouched case is exactly the identity selector. For tail registers, a word of length h<L shifts every old register h positions and appends its h event codes. A word of length at least L overwrites every tail register with the final L codes. The displayed rows implement exactly these word effects; each case depends only on (s,t). The map therefore reconstructs the **whole affine transformation for every input state**, not just its effect on the all-zero orbit. It uses O(k²+Lb)=O(D) row constructions after the state is decoded, and O(D) row storage if materialized.

### Theorem R210-B: exact optimal action code and composition

Let rank:J→{0,...,N−1} be R209's bijection, and define Code(ρ(f))=rank(f) for the *reachable image* ρ(J). Since R201 proves ρ is injective, Code is a bijection onto N consecutive integers. Hence the minimum worst-case fixed binary width for an arbitrary reachable **full affine action** is ceil(log2 N). This is information-theoretically optimal for that action family.

For encoded actions i,j, define i★j=rank(unrank(i)·unrank(j)) using the R200 chronological quotient product. Then

    synth(i★j) = synth(i) THEN synth(j)

as full affine transformations, and ★ is associative with identity rank(F(empty)). Proof: R200 gives a quotient monoid, R201 a faithful homomorphism and R209 a bijective rank. The direct synthesis map in R210-A equals ρ, so conjugating the monoid product through rank proves the identity. A joined positive-rational, multiplicity-bearing BRC histogram keyed by (weight, physical Affine, encoded observer action) therefore has exactly the same alternatives/convolution algebra as its dense Lift into `EffectHistogram` for the explicitly declared fixed-weight total-affine, no-hidden-path-observer interface. BRC positive branch mass and signed/phase-cancelling carriers remain distinct.

For X6's 12 signed native directions, k=6 independent selected source tags and L=2, a=84, D=35, N=1,407,685 and the optimal full reachable affine-action code is **21 bits**. R203's complete unrestricted selector/constant row representation has the simple uniform upper bound D ceil(log2(D+2))=**210 bits**. A factor of 10 compares these fixed-width observer-action storage budgets, not physical matrices, runtime, entropy-coded streams, complete original paths or arbitrary row-selector actions. To recover a particular affine matrix, the 21-bit code is decoded and the rows reconstructed. The cost includes the R209 inverse-rank algorithm, followed by O(D) row synthesis.

### Theorem R210-C: finite reachability bound and exact validation scope

Any admissible J state is represented by a word of length at most k+L: prepend the ordered sources absent from its full tail, then append the full tail; a shorter-than-L state is represented by its tail alone. Therefore exhaustively enumerating all words of length up to k+L covers every J state in a finite model. Checking distinct synthesized actions and their full selector rows is consequently a complete finite verification for that model, though not a replacement for the general symbolic proof above.

Independent `R210_reachable_action_descriptor_check.mjs` uses exact integer/BigInt cardinality calculations and selector/constant composition. It exhausts **36** parameter models m=1..3, k=0..2, L=0..3, and enumerates every word through k+L. Each model's reachable-state count matches R209, every canonical state action equals the chronological product of its per-event actions, and distinct states have distinct entire row descriptions. It checks sampled ordered products across all models and X6 random deterministic histories.

Stored reference output: `R210_validation.json`. Validation status: PASS (36 models; 88,914 histories; 2,727 reachable states aggregated over models; 3,082 sampled products; 800 X6 histories). The checker is an exact independent implementation of R201's selector semantics; it does not import the installed `enterprise_math` package. Independent review=NOT_REVIEWED; native `EffectHistogram` adapter, serialized byte accounting, and end-to-end performance tests remain open.

## Next research

Implement a native `EffectHistogram` adapter that delays `Affine` block expansion until an operation explicitly requests it, preserving exact multiplicities, positive rational weights and physical-action keys. Benchmark packed action IDs (21 bits for X6 L=2), the 210-bit uniform descriptor, and native dense rational matrices including input encoding, arithmetic bit growth, composition, output recovery and serialization. Investigate the separate X6 depth-two minimal affine orbit dimension interval 31..35 without conflating it with the 21-bit finite-action identifier.

Control: portable, unshared research. No asserted formal task CLAIM, native Result/Review, Source promotion or P000 modification.
