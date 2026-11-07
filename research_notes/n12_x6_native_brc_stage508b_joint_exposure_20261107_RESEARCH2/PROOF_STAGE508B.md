# Stage508-B: exact joint position/public-rank exposure for X6–BRC
Date: 2026-11-07. Status: AUTHOR_PROOF / EXACT_FINITE_EXECUTED / UNREVIEWED; **not** an authenticated CLAIM or Result/Driver review.

## Frozen sources and current controls
Scientific inputs remain unchanged: GLOBAL_KNOWLEDGE frozen pin `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; EM frozen pin `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Exact predecessor: `awdawmip/enterprise-math@7d53c1741c5bec29886b43d7d7d27c0e68ff6370:research_notes/n12_x6_native_brc_stage507b_rank_provenance_20261107_RESEARCH2/PROOF_STAGE507B.md`. Current normative main read separately at GK `0d784f0083dc24d6bfbb09fec89b293d0233a649` and EM `c30aa207b5bb6d445c0291a9a31dbfca20743576`.

## Objects and observer
Histories are finite words `w=((a_i,t_i))`, `a_i` one of native signed X6 directions `{±E1,...,±E6}`, `t_i∈{O,P}`. `F(w)=(length, D∈Z^6, E∈N^{12×12})` where `D=Σ v(a_i)`, `E_ab=#{i:a_i=a,a_(i+1)=b}`. This retains all 144 directed relational counters; O/P tags are observable only through ranked deletion and its subsequent F readouts. The observer includes legality and F after every action prefix of length at most h.

Operation alphabet: POP last, DELETE2 third from right, INSERT2(c) insert a fresh P before final two, SET_END(r,c) replace direction at right offset r∈R *preserving tag*, DELETE_KTH_PUBLIC(k) delete k-th P from right for k∈S. Length/rank legality is part of the observer. Direction c ranges over all 12 signed axes. R finite nonnegative offsets and S finite positive ranks.

## Definition of exact direct-exposure set T_h(w)
Assign each original token a unique identity 0,...,n−1 and track its O/P tag; each INSERT2 gets a new distinguishable non-original P identity. The direction labels need not enter the reachability state, because none of these operations changes rank/length legality or token movement based on direction. Enumerate abstract identity/tag skeletons over **all legal operation strings of length <h**, with SET transitions preserving the skeleton. At every reachable *pre-action* state, mark every original identity which (1) is a legal POP/DELETE2/SET_END/ranked-public-delete target, or (2) borders the legal INSERT2 boundary on either side. The union is T_h(w). New inserted P nodes are always explicit.

An exact finite-state enumeration for each fixed n,h computes T_h(w), including short-length illegality and inserted P rankings. It may use exponentially many skeletons in h; no polynomial-time claim is made. 'Exact' means exact for this declared syntactic exposure definition, **not** the minimum possible state code among all algorithms.

## Theorem 508.1 (finite-horizon full-observer sufficiency)
Encode the original tokens at T_h(w) as explicit direction+tag singletons in order. Replace every maximal intervening original run by its complete F summary; keep piece order and lengths. Call the encoding C_h(w). For **every** permitted action string of length ≤h, all action legality and full F prefix observations can be computed on C_h(w) without opening an opaque run. Consequently equal encoded states entail equality of the declared finite future-response signatures.

**Proof.** The full F summaries have an exact associative concatenation law: add length, displacement, 144 counts, and the single junction edge from last(left) to first(right) if both nonempty. First direction equals `D−Σ_ab E_ab v(b)` and last equals `D−Σ_ab E_ab v(a)`; they are unique because the signed X6 unit vectors are pairwise distinct. Caching first and last directions changes no information.

Induct on an arbitrary action prefix of length t≤h. By the *construction* of T_h, every original token that can be a removal or SET target at any pre-action depth t−1<h, or can neighbor the INSERT2 boundary, was explicitly retained initially. Inserted tokens also remain explicit. Every permitted action thus edits/removes a singleton or inserts between piece boundaries and never splits a hidden F gap. Length/r-offset legality is read from exact lengths. For ranked deletion, if a legal k-th P target were hidden, that original identity would have been included in T_h; contradiction. Further, ranked deletion legality itself is exact without hidden P counts: whenever ≥k total P exist, the selected token is explicit, hence ≥k visible explicit P; otherwise there are <k visible P. Recomposition by the associative F law preserves the full observer even across newly created junctions. This proves the induction. QED.

The input mask can depend on hidden initial tags, but equality of actual compressed states is safe: each input independently satisfies the same all-futures executable-state invariant, so equal states generate identical observations under identical actions.

## Theorem 508.2 (strict refinement of Stage507's sufficient union)
Let B be the initial end-offset set `([0,h+2]∪⋃_{r∈R}[r−h,r+h])∩[0,n−1]`, and let U_h(w) contain every original token with end offset in B plus the rightmost `M=max(S)+h−1` original P tokens. Then `T_h(w)⊆U_h(w)`. Proof: each earlier action shifts any surviving original end offset by at most 1, and direct positional access or insertion boundaries therefore lie in B. A public token outside the rightmost M originally has M original P to its right; before the h-th operation at most h−1 can disappear, leaving ≥max(S) to the right, so that older P cannot be selected. QED.

**Strict witness:** n=19, h=3, R={2,11}, S={1,3}, public initial indices {0,3,6,12,15,18}, signed direction number `a_i=(3i+i²+7) mod 12`. Stage507 U_h retains 15 singleton identities `[3,4,5,6,7,8,9,10,12,13,14,15,16,17,18]`; new T_h retains 12 `[3,5,6,7,8,9,12,14,15,16,17,18]`. Thus three additional original positions (4,10,13) can be compressed into opaque BRC summaries. The exact T_h has rank-dependent contributions; deleting PUBLIC operations removes indices 3 and 12 from the exposure set.

**Nontrivial fiber:** two n=28 words with the same 12-direction path, common late P tags {20,24,26,27}, and one older extra P at index 0 versus 1 share exactly the same new encoding for h=2, R={2,12}, S={1,2} while being different tagged histories.

## Exact execution, proof scope, reuse and open work
`REPRO_STAGE508B_DELTA.py` imports the **immutable** predecessor's actual `REPRO_STAGE507B.py` BRC F monoid and independent raw/piece-step engines. It implements a new identity/tag BFS exposure function and compares complete raw and compressed F (six signed displacements + all 144 edge counters) and legality at every prefix. `STAGE508B_DELTA_EXECUTED.json` is the output of an actual executed Python standard-library run.

Exhaustive inputs: all tagged words over three native signed directions (+E1,−E1,+E2) and both O/P flags, lengths ≤5 at h=1 and ≤4 at h=2, with R=(2,5)/(2,4), S=(1,2), plus full-12-direction strict/collision witnesses. 10,889 roots, 185,991 prefix nodes, 226,470 transitions; assertions PASS. This is finite corroboration, not a substitute for the general proof. The program checks T_h⊆U_h on every root. No run-time performance or universal information-theoretic optimality is asserted.

BRC reuse classification: **COMPOSE_APPLIED** to the complete 144-relation F-piece algebra of Stage507, preserving all future-relevant relations and source ports in the declared horizon.

**Next:** find a symbolic/nonenumerative algorithm computing T_h with better preprocessing complexity, or prove a smaller sufficient boundary-visibility rule for INSERT2 using recoverable F first/last directions. The separate full-144-heterogeneous-edge Euler–BRC rank/unrank bit-cost/peak-RSS comparison remains open.

**Actual authority:** GitHub author-side evidence; native service `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`; current Owner, native CLAIM, Result and Driver review unconfirmed.
