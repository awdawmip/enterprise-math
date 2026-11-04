# Stage422-B — Exact 24-state future quotient for two-source native-X6 BRC histories

Date: 2026-11-04. Parent: Stage421-B, commit 70874f7b3d48624c743fb43e5f457558a719c255, Draft PR #1736. Status: AUTHOR_SIDE_PROOF / EXACT_FINITE_COMPUTATION / UNREVIEWED / NOT_ADMITTED.

Frozen scientific inputs, unchanged: GLOBAL_KNOWLEDGE_V1 bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral rules are separately resolved from canonical main. This is an explicitly scoped ordered-path observer within the six native axes, not an assertion for arbitrary P000 processes.

## Definitions and main theorem

Let D consist of all twelve signed native directions ±E1,...,±E6 and let A=+E1, B=-E1. For each integer n>=11, the initial fiber F_n consists of
P_i=A^(i-1) B A^(n-i), Q_(r,s)=A^(r-1) B A^(s-r-1) B A^(n-s),
with 2<=r, r+2<=s<=n-1, and i in {r,s}. It contains (n-3)(n-4) original path pairs.

The complete observer retains both lengths; both six-component, chart-relative endpoints; each source's full directed adjacency histogram J; and the joint absolute-position match count K=sum_{j<=min(lengths)} 1[P_j=Q_j]. A failed attempt is visible, and so is each successful intermediate full observation.

The L(3,2) operation language allows arbitrarily many paired APP(a,b) with a,b in all of D, at most three Q-only POP operations, and at most two paired CANCEL operations. A CANCEL is enabled only if each source ends with an inverse adjacent direction pair; it then removes these two labels from each source. Future equivalence means identical enabledness and complete observer traces for every finite common attempted action word.

**Theorem 422.1. For every integer n>=11, q_(3,2)(F_n)=24.**

This resolves the Stage421 interval 24..44 (at n=11 its previous upper bound was 43). The lower bound is a complete finite exact certificate plus an algebraic prefix-extension argument; the upper bound is an all-horizon symbolic proof.

## Lemma 422.2 — Coupled appended-stack inequality

Write any reachable source word as its surviving original prefix followed by its surviving APP-generated suffix. Denote deleted-original counts by dP,dQ; surviving appended suffix lengths by u,v; and successful APP, POP, CANCEL counts so far by a,t,c. Then

u >= v, and dQ <= t+dP.

Initially u=v=0. A paired APP increments both by 1; Q-only POP reduces v by 1 if it is positive, otherwise removes an original Q label and leaves v=0. A paired CANCEL changes (u,v) to (max(u-2,0),max(v-2,0)). Each operation preserves u>=v, including all APP directions; denied operations do not change state. Length conservation gives u=a-2c+dP and v=a-t-2c+dQ, so v-u=dQ-dP-t. Thus u>=v implies dQ<=t+dP. This is a general two-source stack invariant: it does not rely on A/B or the F_n path population.

## Corollary 422.3 — Original deletion bounds

P in F_n contains one B and otherwise only A. Two original P letters can be removed by one CANCEL only when that original inverse pair contains B; it can happen for at most one CANCEL. Each remaining CANCEL removes at most one original P letter. Consequently, with c<=2, dP<=3; with t<=3, the coupled inequality gives dQ<=6. Equality dQ=6 forces t=3 and c=2, exhausting both destructive budgets.

If P's B lies at i<=n-3, P initially ends in at least three A. In at most two CANCELs no original B can be reached; every CANCEL removes at most one original P A. Thus dP<=2, dQ<=5. Equality dQ=5 likewise exhausts all POP and CANCEL budgets. All these bounds hold after arbitrary APP insertions and at every reachable intermediate step.

## Lemma 422.4 — Protected-original-tail bisimulation

Consider two initial histories with identical full O. If an original suffix is common between them for a source, its boundary original letter is never removed, and no remaining destructive budget can inspect the unknown earlier original letter once that boundary is exposed, then the reachable edits to that source are functions of its known original suffix, the common appended word and the remaining budgets. The unedited original prefix contributes a fixed endpoint vector and fixed directed-adjacency multiset (including the edge crossing into the retained boundary); initial equality of full endpoint/J totals and equality of the known suffix determine equal prefix aggregate contributions.

For K, split aligned comparisons into an unaffected original-original prefix and the comparisons touching edited or appended positions. If the unaffected-prefix match total is initially the same, and every later mixed original/appended comparison uses an identical known original letter in both histories, then K is preserved under a common operation. This permits different deletion depths in P and Q but requires checking the absolute-position mixed comparisons rather than discarding them.

Induction on every attempted operation proves equal legality, identical deleted-original counts, identical appended words, and full O at every successful step; a denied step is denied for both. This observation-preserving induction works for arbitrary finite APP sequences over all 12 directions.

## Lemma 422.5 — Construct a 24-state all-future representation

Partition F_n into three explicit types:

**Type B: s=n-5, ONE state.** Every such P ends A^5 and every Q ends the same BA^5. From Corollary 422.3, dP<=2, dQ<=5. Thus P cannot remove its original B, Q cannot remove the boundary original B at s, and exposure of Q's B consumes all destructive budgets. All removed P/Q original labels are A, with common directed-edge changes and known appended junctions. For K, the initial P/Q mismatch lies at exactly one of r or s; the prefix through s has exactly s-1 matches for both choices i=r or i=s, while all original positions after s are A in both sources. Subsequent mixed comparisons involve these common As and common appended labels. This proves full-future equivalence within Type B (including both i choices), with population 2(n-8).

**Type R: s != n-5 and i<=n-3, FOURTEEN states.** Corollary 422.3 gives dP<=2,dQ<=5, so original position n-5 is retained in both sources; if Q first exposes that boundary, all destructive budgets are spent. Retaining each source's six original labels at positions n-5,...,n is sufficient. Two histories with equal full initial O and identical P-last-6 and Q-last-6 have equal original prefix aggregate endpoint/J/K contributions, identical reachable edits to those known tails, and identical original/appended overlap comparisons. Thus each equal (P-last-6,Q-last-6) key forms a full-future class.

Counting these keys in Type R: s<=n-6 gives 1 key; s=n-4 gives 2; s=n-3 gives 4; s=n-2 with i=r gives 3; s=n-1 with i=r gives 4. Total: 1+2+4+3+4=14. These counts remain valid for every n>=11.

**Type F: i=s=n-2 or i=s=n-1, NINE states.** P's complete original word is identical across histories at each of these fixed i, and Q's second B is fixed at s. The global dQ<=6 bound preserves Q original position n-6; if it is exposed all destructive budgets are spent. For a fixed P, equality of the complete initial O plus Q's seven original labels at n-6,...,n proves full-future equivalence: initial Q-prefix endpoint/J totals agree, and its K contribution against the literally identical P word agrees. Every subsequent mixed comparison involving an APP into Q also uses the same complete P word at the same absolute position, preserving K despite unequal source lengths. For s=n-2, Q's first B may be earlier than the seven-symbol window or at n-6,...,n-4, giving 4 keys. For s=n-1, it may be earlier or at n-6,...,n-3, giving 5 keys. Total 9. This fixed-P statement is not asserted as a general (4,7) suffix theorem.

The three types are disjoint and exhaust F_n. All histories within each key are future equivalent by the full directed-J, absolute-K and enabledness arguments above. Hence q_(3,2)(F_n)<=1+14+9=24, for all n>=11.

## Lemma 422.6 — Exact lower certificate and infinite-n extension

REPRO_STAGE422B.py enumerates the entire finite F_11 (56 histories) using exact integer words and constructs the 24 upper-key representatives. It computes the full two-source endpoints, directed adjacency histograms and absolute K, and evaluates the complete successful/denied observer responses to twelve explicit short probes. The probes use only POP, CANCEL, APP(B,B), APP(B,A); their complete literal definitions are included in source and the executed JSON.

**Exact finite certificate:** all 24 representatives have pairwise distinct vectors of the twelve complete trace responses. Each probe is a legal attempted action word in the full L(3,2) language. This supplies 24 pairwise future-distinguishable histories in F_11.

For any n>11, prepend A^(n-11) to both original source words of each of these 24 representatives. These pairs belong to F_n and every probe remains within its original F11 terminal portion: Corollary 422.3 bounds Q original deletion by 6, so the common new prefix and at least five original F11 directions remain untouched. This shifts both original endpoints by the same added vector, adds the same directed AA prefix edges and increases aligned K by exactly n-11 in every trace. Terminal enabledness and every original trace-response difference are therefore preserved. It follows that q_(3,2)(F_n)>=24 for every n>=11.

The finite certificate has an explicitly bounded, exhaustively checked input domain; the front-padding proof supplies the universal parametric lower bound. It is not necessary to restrict arbitrary native APP words for the upper bound, which is already a full-horizon bisimulation proof.

## Exact verification and conclusions

The standard-library Python source was actually executed, with marker STAGE422B_EXACT_TWENTY_FOUR_COUPLED_STACK_PASS. It checks 24 grouped states for each n=11..40, covering 16,760 original histories; 24 pairwise different twelve-probe signatures at n=11,12,16,30,40; and 30,382 bounded attempted words against all same-class pairs at n=11, totaling 972,224 same-class trace comparisons. Its finite trace tests include up to one APP over all 144 native direction pairs (with up to three POP/two CANCEL and at most six steps), plus up to two APP over {A,B}² (with full destructive budgets and at most seven steps). This computational cross-check is separate from the full-horizon symbolic upper proof. The exact actual evidence is stored in REPRO_STAGE422B_EXECUTED.json.

Main conclusion: q_(3,2)(F_n)=24 for all n>=11, for this exact path fiber, complete directed-J / absolute-K observer and all 12 signed-native APP choices. The coupled-stack inequality is reusable for deriving original-history deletion budgets in other source configurations. No external physical-dynamics or formal native Source Result/admission claim is made.

## Next Stage423-B

Generalize the coupled-stack flow invariant to k-source asymmetric POP and multi-source cancellation, with precise budget-frontier bounds and smallest counterexamples for changed operator arity. Compose the new 24 future classes with Stage412's remaining-Euler-edge/J/K dynamic programming to compute class populations from observer counts without constructing every original path. Include input-encoding/preprocessing/output costs for any complexity claim; preserve original P000, scientific freeze and independent review obligations.
