# Stage493-B — Provenance-aware INSERT / moving-SET theorem and exact witness

Status: AUTHOR-SIDE PROOF / EXACT INTEGER EXECUTION / UNREVIEWED / NOT ADMITTED.
Parent: Stage492-B on research PR #1736 at 5e3246518dd09803c87c423fe278f4ee4f5bdd73.
Frozen scientific inputs (unchanged): global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; global P000 original blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative read: global main@233c36ecbc128906d7dcd9c7db9f2c1e16dc36ba; Enterprise Math main@002b4c8e91d0f78f464ccde9357deeb8d455165b. Current P000 startup original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc verified against projection.

## Exact model and carrier

D={A,...,L} denotes +E1,...,+E6,-E1,...,-E6: twelve signed step directions of native X6, not twelve spatial dimensions. For each history word q, observe length, the six signed integer displacement components v(q), and all 144 directed-edge counts E(q). For two words P and Q, also observe positional agreement K(P,Q)=sum_{i<=min(|P|,|Q|)} 1[P_i=Q_i]. Observations of P and Q are separate. Future labels and public letter parameters are common to compared histories. Preserve each original path as a multiplicity-one labeled BRC branch; Boolean class support is distinct from exact raw-history population.

A provenance token is (kind,origin,value), where kind is original, inserted or appended; origin is an original index or public-event ID. Public INSERT at position j adds a token before the current j-th token (1-based); DELETE and POP remove tokens; APPEND adds a public token. Value determines observable displacement and edges; origin/kind determines the exact transported position before the next operation. This is an address computation, not an assertion that the origin tag itself is observable.

## Theorem 493.1 — exact one-SET future refinement with transported public tokens

Fix a finite, content-independent operation grammar B of publicly specified Q INSERT/DELETE/POP/APPEND actions (including the traces without any edit) and public P POP/APPEND actions. Public action validity, including the absolute or relative insertion address, is determined by the public trace and lengths, never hidden values. Let E be the extension that permits *at most one* additional Q SET(j,z) after an admissible B-prefix, with all twelve z in D allowed, and subsequently permits only P/Q POP/APPEND. Require the SET center to be strictly interior and its absolute index to exceed the maximum reachable P length for the entire continuation. Both compared initial histories have the same P word and Q length, and the same budget/grammar.

For each legal prefix s ending immediately before the optional SET, let t_s(Q) be the current ordered value triple (left, center, right) at that prefix's SET target, obtained using provenance-aware address transport. Let X~B Y mean equality of the *complete declared observation at every stage* for every B-only trace. Then the exact enhanced observational equivalence is

    X~E Y   iff   X~B Y and (for every legal SET prefix s, t_s(Q_X)=t_s(Q_Y)).

The signature is exact as a family of reachable value triples, indexed by the public prefix. It is not claimed coordinate-wise irredundant. An origin tag is an implementation aid; distinct origins with identical values at every reachable edit inspection need not be distinct equivalence classes.

Proof (necessity). The zero-SET sublanguage yields X~B Y. Fix any legal s. After s the base observations coincide. Replacing the center c by z changes displacement by v(z)-v(c), so equality for one common z implies the two centers have identical native signed direction c (the twelve v(c) are distinct). Now choose z outside the union of both length-three neighborhoods (at most six letters, with twelve available). The directed-edge correction is -[l,c]-[c,r]+[l,z]+[z,r]. As z is fresh for both triples, the unique incoming new edge [l,z] and outgoing new edge [z,r] recover l and r. Hence the two triples are equal for every s.

Proof (sufficiency). Before SET the entire trace is in B, so all observations coincide by X~B Y. Identical triples give identical SET corrections to displacement and 144 directed edges. The edit target cannot contribute to K because its index is larger than any subsequent P length. Under later Q POP/APPEND, the difference between the edited word and its never-edited counterpart remains local to the edited center and its immediate right boundary: while the original right suffix survives, the edge correction is fixed; when Q POP reaches the initial right neighbor, the transition only depends on the known original triple; if the edited center becomes terminal, further publicly labeled APPEND/POP steps use its known value and known appended tokens; once the edited center is popped the correction vanishes. Thus each edited-vs-base correction is the same for X and Y at every stage. P operations are unchanged, and the positional observer does not touch the edited index. The B-only observations agree at each corresponding public trace, proving X~E Y.

The theorem allows public inserted letters to be the left neighbor, center or right neighbor of SET. For grammars permitting a second internal edit after SET, an additional transported state argument is needed; this theorem states no such extension.

## Strict two-action witness: a previously invisible INSERT changes the inspected history

Take P=T=ABGABA, W=GH, H1=AAAABAA and H2=AAABAAA, Q=TWAHA, and |Q|=17. Both Q have identical length, six-vector displacement and every directed-edge count; the full initial observation including K is identical. The initial moving edit SET_FROM_END(6,z), for every z in D, targets position 11 with triple AAA in both histories and hence gives identical observation.

Perform a public interior INSERT immediately before Q's final A, at absolute position 17, inserting C. Both histories remain observationally equal; the edited local pair is AA in both. The Q length becomes 18, and SET_FROM_END(6,I) now targets absolute position 12. The transported triples there are AAA (first history) and AAB (second history). The two final six-vector displacements are equal, but the exact directed-edge difference (history 1 minus history 2) is

    -[AA] + [AB] + [IA] - [IB] != 0.

Consequently the old original-site-11 triple alone is not sufficient for this INSERT+moving-SET grammar. This is a two-action strict distinguishing trace whose first action is individually unobservable. Here I=-E3. The public C is inserted next to the terminal A, not disguised as an original step.

## Local INSERT/SET interaction lemma

For original substring a b c, inserting public z immediately before b and then setting that same surviving original b to x yields a z x c. The exact directed-edge correction is

    Delta E = -[ab]-[bc]+[az]+[zx]+[xc].

Writing Delta_insert=-[ab]+[az]+[zb] and Delta_set_on_original=-[ab]-[bc]+[ax]+[xc], the missing interaction is

    I = [zx]-[zb]-[ax]+[ab].

This equality follows by cancellation and holds for all twelve directions, including coinciding letters. In the checked 4-letter family a,b,c,z,x in {A,B,G,H}, 1024 exact cases passed and 576 have nonzero I.

## Executed evidence and scope

The independent standard-library checker REPRO_STAGE493B_PORTABLE.py was executed. It checks the strict witness and all twelve replacement directions, verifies 1024 exact insertion+SET identities and exhausts H in {A,B,G,H}^7 (16,384 raw histories). Under the fixed grammar consisting of initial Q, one INSERT(C) before the final original A, and one subsequent SET_FROM_END(6,z) for arbitrary z in D, it finds 5,219 base observation fibers and 14,752 enhanced classes. The exact 12-response signature is injective in the current transported triple within each base fiber. Class-size histogram: 13,252 singleton, 1,380 size-two, 108 size-three, 12 size-four classes. Every assertion passed.

A larger local source REPRO_STAGE493B.py additionally executed a deterministic provenance-token transducer and all 72 schedules of one POP, one before-final INSERT(C), and one APPEND(z) (all 12 signed z and six orders); the two witness histories have identical base observations in all 72 schedules and distinct reachable edit triples. It recorded fully signed 144-dimensional edge comparisons. The full local execution output is STAGE493B_EXECUTED.json; portable source and stdout are also independently saved in this PR.

BRC scope: typed multiplicity-one original-history branches, exact integer observer and positive raw-population counting. No phase cancellation or native physical dynamics is asserted. Mathematical theorem depends on the stated finite-language observer/grammar assumptions; finite checks establish their declared domains only. Native source identity/CLAIM and independent Driver review are pending.

## Next research unit

Stage494-B: (i) allow a second internal DELETE or SET after the first moving SET, and inspect whether the single-pre-SET transported triple can be replaced by a finite composed provenance-boundary signature; seek the shortest counterexample if not; (ii) compare a genuinely high-support (near 144-edge) Euler–BRC branch counting/ranking implementation, including representation construction and total rank/unrank output costs. Preserve current immutable scientific pins.
