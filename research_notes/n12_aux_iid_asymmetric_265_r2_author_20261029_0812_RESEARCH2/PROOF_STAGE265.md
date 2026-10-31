# Stage265 — exact H5–H6 adjacent support and complete real contact region

**Research status:** `AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED`. This is an independently computed author-side result in the external ternary IID auxiliary model, not a native P000/X6 dynamical theorem or Source-native CLAIM/Result/Driver acceptance. Research actor: `EM-R2-STAGE265-20261029-0812-AUTO11` (local descriptive identity; no service session/authority is claimed).

**Frozen sources (2026-10-29):** `GLOBAL_KNOWLEDGE_V1 main@419795d154e3436e96b996f5f5a75a56dfe9bc34`; `enterprise-math main@919f879a4b29e686117930e148bbd19b722317f5`; immutable Stage264 result `a62d4ac5109ab9824b203b648771646ab093e109` at `research_notes/n12_aux_iid_asymmetric_264_r2_author_20261029_0713_RESEARCH2/`. The GLOBAL source includes P000 original git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` and validated matching P000 startup projection. ACTIVE world-model and portable-research instructions were read. The exact prior `H5,H6` vertices are reused without redetermining Stage264. Source provenance, P/Q path multiplicity and all four observer values remain explicit. Scientific research did not apply or assume P000's native six-axis dynamics.

## 1. Definitions and exact result

Alphabet `{0,1,2}`, horizon `N=12`, strictly positive IID source distributions

`P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6)`.

A policy may use randomized actions `P` (stop and declare P), `Q` (stop and declare Q), or `C` (continue) depending on its **entire ordered history**, with stopping mandatory at time 12. Define four observers `eP=Pr_P(declare Q)`, `eQ=Pr_Q(declare P)`, `tP=E_P[tau]`, `tQ=E_Q[tau]`; `V12(a,b)` is the minimum possible `max(tP,tQ)` over policies with `eP<=a,eQ<=b`; it is `+infinity` when infeasible.

**Theorem 265A (new exact optimum).** At

`a265=2501401941677/29023764480000`, `b265=13264221055/17414258688`,

`V12(a265,b265)=348042679485689167/62233299993600000 = 5.592547390568739...`.

A global Bellman dual supporting this exact value has positive multipliers

`lambdaP=6216128/68615`, `lambdaQ=3900924/68615`, time weights `(thetaP,thetaQ)=(0,1)`, root value

`H=90763458197/1600650720`.

**Theorem 265B (all-real if-and-only-if face).** Write the exact full observer vectors, in order `(eP,eQ,tP,tQ)`, as

- `H5=(3750849409/46438023168, 13498546055/17414258688, 8819755201/1934917632, 7717391977/1451188224)`;
- `I5=(1763120017/23219011584, 6802983965/8707129344, 4453822913/967458816, 3922172551/725594112)`;
- `I6=(443710351/5159780352, 1462089145/1934917632, 3279966317/644972544, 960037303/161243136)`;
- `H6=(1420974803/15479341056, 4343298685/5804752896, 3244810067/644972544, 2829330659/483729408)`.

Let `pi` discard the two time coordinates and let `R265=conv{pi(H5),pi(I5),pi(I6),pi(H6)}`. For **every real** error cap `(a,b) in [0,1]^2`, including infeasible caps under the extended-value convention,

`V12(a,b) = H - lambdaP*a - lambdaQ*b  <=>  (a,b) in R265`.

This region is a strictly convex four-vertex rational polygon with exact area

`area(R265) = 4606719970703125/67390312367240773632`.

`R265` and the Stage264 region `R264=conv{pi(G5),pi(H5),pi(H6),pi(G6)}` share exactly their full `H5–H6` edge, while their interiors are disjoint.

## 2. Finite Bellman certificate for *all ordered-history policies*

For a history with count state `s=(i,j,k)`, its positive mass ratio is `r(s)=Q(h)/P(h)=(2/3)^i 2^j`. Normalize conditional future dual cost by `P(h)`. At horizon 12, set `D(s)=min(lambdaQ*r(s),lambdaP)`. At earlier states use the exact recurrence

`D(s)=min{ lambdaQ*r(s) [declare P], lambdaP [declare Q], r(s)+sum_{z=0}^{2} P[z] D(s+unit_z) [continue] }`.

This recurrence is a global lower bound for the cost `tQ + lambdaP*eP + lambdaQ*eQ` of *every* randomized complete ordered-history policy by induction on remaining observations, including history-dependent conditional decisions. The exact Fraction certificate checks all `455` count states and all `1274` legal action costs; root equals `H`; `817` nonminimizing action gaps are strictly positive and the minimum positive gap is `2048/177147`. The two and only two action ties occur at `(0,0,5)` with choices `P/C`, and `(0,1,9)` with choices `Q/C`.

Consequently every feasible policy satisfies

`max(tP,tQ) >= tQ >= H-lambdaP*eP-lambdaQ*eQ >= H-lambdaP*a-lambdaQ*b`.

All inequality directions use positivity of the two multipliers. This is a global inequality, not an approximation or a floating linear-programming output.

## 3. Exact sufficiency, provenance, and equality hull

The reduction to counts is **observer-relative**, not a collapse of unobserved path information. Aggregate positive P masses of complete *ordered* histories at a given count state separately for each action. Their Q/P ratio is exactly `r(s)`, independent of arrival order; thus averaging action probabilities under these P masses preserves P and Q action mass, their child-state propagation, and all four observer sums. This constructs a count-state randomized policy having exactly the same four observers as any full-history policy. Path multiplicity is retained in the sums. The reduction need not preserve any external fifth observable or P000/X6 relational state.

Bellman equality requires every action reached with positive P probability to be a minimizing action. All non-tie choices are fixed. A randomized choice at either of the two tie states may be presampled as an independent Bernoulli value, making the resulting observer vector a convex combination of the four deterministic tie policies. Conversely every mixture of these four policies is permitted. The Fraction program enumerates those four policies under both (i) merged count-state mass recursion and (ii) an **independently written ordered-history DFS** with separately multiplied P and Q positive rational masses. The two implementations give identical exact observer vectors in every case. DFS visits `661+691+718+754=2824` nodes and `441+461+479+503=1884` termination branches; both source terminal mass sums are exactly one for each policy. The four vectors are precisely `H5,I5,H6,I6` above, and all have `tQ>tP` and `tQ+lambdaP*eP+lambdaQ*eQ=H`.

Therefore, given an error cap pair in the projected four-corner hull, a mixture realizes its exact error pair and its max time equals the global dual lower bound. Conversely, if a feasible policy attains that affine bound, then compactness of the finite-horizon randomized policy space gives a minimizer, and strict positive dual multipliers force `eP=a,eQ=b`; its positive reached actions must all achieve Bellman equality. The sufficient-state argument and tied-action enumeration put `(a,b)` in the four-corner hull. This proves the universal `iff`, including its necessity part.

## 4. Exact primal matching and adjacent geometry

For the ordered simplex `(H5,I5,H6)` use positive weights

`w=(374206659479903/837585449218750, 18135982964736/418792724609375, 136674183619/268027343750)`.

They sum **exactly** to one. Their four-observer mixture is

`(a265,b265,398394906718840411/82977733324800000,348042679485689167/62233299993600000)`.

Its time gap is `tQ-tP=2870888257469/3627970560000>0` and exact substitution gives `H-lambdaP*a265-lambdaQ*b265=tQ`; hence primal and global dual match and prove Theorem 265A.

The four consecutive strict left turns of ordered `(H5,I5,I6,H6)` are

`2093963623046875/33695156183620386816`,
`418792724609375/5615859363936731136`,
`418792724609375/5615859363936731136`,
`2093963623046875/33695156183620386816`.

Shoelace on these four rational vertices gives the stated exact area. Stage264's `G5,G6` are strictly on the positive side of oriented `H5->H6`, while `I5,I6` are strictly on its negative side; both regions are strictly convex and have the exact common `H5,H6` endpoints. Hence their intersection is **the complete common edge**. The Stage265 target is strictly outside R264 because

`orient(H5,H6,(a265,b265))=-46865/17414258688<0`,

and is strictly inside R265 because each of its four counterclockwise edge orientations is positive (asserted in the executable). This closes the previously open Stage264 adjacency question exactly.

## 5. Execution, scope and following question

Source code: `STAGE265_EXACT_FACE.py`. Actual executed output: `STAGE265_EXECUTED_STDOUT.txt` terminates with `STAGE265_EXACT_ALL_REAL_FACE_PASS`; `python3` stdlib `fractions.Fraction`, with exact inequality and equality assertions, no SciPy in the proof run. Mathematical extent: finite IID model, arbitrary complete ordered histories and their randomized policies, exactly four listed observers and all real caps in `[0,1]^2`. Scientific novelty claimed within this exact auxiliary succession only. Prior Stage264 `H` vertices are reused as immutable antecedents rather than reattributed to Stage265.

**Current control observation at 2026-10-29:** the native gateway `em_status` reports `research_authority_granted=false`; read-only Owner/task query returned `CONTROL_QUOTA`, so native active Owner is unconfirmed. No Source-native CLAIM, session, formal Result, review, or mathematical admission is asserted. Separate next obligations: independent authorized Driver review and any bridge theorem into P000 native X6 dynamics. This exact auxiliary result respects BRC-inspired positive source mass/path multiplicity constraints but asserts no physical/native transfer.

**Stage266 question:** Cross `R265`'s outer `I5–I6` edge. A concrete strictly exterior rational *candidate*, whose feasibility remains to be proved, is

`a266=4693965992729/58047528960000`, `b266=26764770235/34828517376`,

with `orient(I5,I6,(a266,b266))=-715465/278628139008<0`. Establish feasibility or an exact separation certificate first; if feasible, construct new primal/dual Bellman support and exact full-real adjacent contact region, retaining P/Q ordered-history provenance. See `NEXT_TASK_PACKET_266.md`.
