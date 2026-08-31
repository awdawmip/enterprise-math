# Driver Review — P000 local-to-global background equivariance V18

Status: `ACCEPTED / FULL-LIFT-FIBER GENERATOR CRITERION CLOSED / NONTRIVIAL MODULI NEXT`

Result: `RR-7FED4A83F3922D37319D`  
Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication: `TP2-D6A41E9C3B705F821847`  
Researcher: `EM-P000FCC18-ED9B7E`  
Driver: `EM-DVR-7C31A8`

## Verdict

`ACCEPTED` at verification-interface/local-to-global strength.

Accepted terminal class:

`LOCAL_GENERATOR_EQUIVARIANCE_EXACTLY_EQUIVALENT_TO_GLOBAL_BACKGROUND_TRANSPARENCY`.

This sharpens how the accepted Gen17 semantic gates are verified; it does not reduce their semantic cost count, mutate G15/P000, or grant a complete native `S4` rotation group.

## Decisive audit

Let `q0:G0->S4` be surjective, `K=ker(q0)`, and let `G_B` be the stabilizer of a retained background family `B`.

1. The full-lift-fiber criterion is exact: if every lift in `q0^-1(a)` and `q0^-1(b)` preserves `B`, then the full `a` fiber forces `K<=G_B`; preserved lifts of `a,b` generate the quotient; hence every `g in G0` differs from a preserved word by a kernel element and lies in `G_B`. The converse is immediate.
2. One chosen coherent lift pair is not enough when hidden kernel remains. The exact `C2 x S4` witness has chosen lifts generating `{0}xS4` while the nontrivial kernel element still breaks the background.
3. PF-10 and independent connection share this local-to-global proof schema but remain independently falsifiable semantic gate instances; Gen17's two charged costs do not collapse into one macro.
4. Single-generator and local-orbit regularity conditions are strictly weaker; the return supplies visible exact countermodels for `a`-only, `b`-only, and same-orbit-type claims.
5. Holonomy conjugacy on a cycle basis is not equivalent to structural connection transparency: a flat pure-gauge asymmetric connection is a counterexample.
6. Conversely, nonflatness is not a symmetry obstruction. The K4 connection assigning each Cell edge the channel transposition between that edge and its opposite is fully `S4`-equivariant and has nontrivial triangle holonomy.
7. The finite orbit-index information statements are accepted only for the exhibited witness families, not as universal Shannon/Kolmogorov minima.

## Boundary

Freeze:

`FULL_LIFT_FIBER_AB_EQUIVARIANCE_IFF_GLOBAL_TRANSPARENCY = TRUE` under surjective `q0` and frozen generating pair `a,b`.

`CHOSEN_AB_LIFTS_ALONE_SUFFICIENT_WITH_HIDDEN_KERNEL = FALSE`.

`PF10_AND_CONNECTION_REMAIN_TWO_SEMANTIC_GATES = TRUE`.

`FLATNESS_IS_NOT_EQUIVARIANCE = TRUE`.

`NONFLAT_EQUIVARIANT_CONNECTION_EXISTS = TRUE` at the exact finite K4 witness strength.

`UNIQUE_SECTION_NOT_GRANTED = TRUE`.

No kernel quotient, P000 mutation, carrier/native identity collapse, time rotation, or Gen17 cost reduction is authorized.

## Method harvest

Reusable theorem: for a subgroup-preservation property `G_B<=G0`, global transparency can be checked on full lift fibers of a generating set of the quotient only when the hidden kernel is thereby forced transparent. This is a general verification-interface pattern distinct from choosing representative lifts. For connection-like data, separate edge/path coherence, holonomy, and symmetry naturality.

## Routing consequence

The next P0 stage should no longer ask whether a nonflat equivariant connection exists; Gen18 already answers yes. It should classify the **moduli** of nonconstant `S4`-equivariant PF-10 families and independent connections on the K4/tetra structural models, quotient them by the accepted gauge equivalence, classify holonomy conjugacy classes, and build a single common Full-Cell model carrying nonconstant PF-10 plus a nonidentity/nonflat equivariant connection while preserving the accepted `R_a,R_b` relations.

Final disposition: `ACCEPTED / FOLLOWUP_TASK`.
