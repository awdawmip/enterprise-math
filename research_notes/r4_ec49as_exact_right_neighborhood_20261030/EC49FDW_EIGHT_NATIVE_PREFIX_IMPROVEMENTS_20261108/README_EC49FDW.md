# EC49FDW — Exact native-prefix improvement within the 64 quota-three-phase schedules

Date: 2026-11-08 (Asia/Shanghai). Parent: EC49FDV at immutable commit `7e3b0450c17c4fe1b6e604b5749fb762d3eca63e`. Frozen science: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Research status: author-side, constructed and exact-checked, independent Driver admission pending.

## Concrete result

Within eight *fixed* EC49FDV late-key schedules, replacing the selected complete paths by prefix-aware coordinate descent yields eight valid H2–H9 24-word systems. Four original greedy witnesses of 126 native prefix edges are improved to **118**, and four of 128 to **120**, each an exact saving of 8 primitive edges. At every horizon the nine-history/five-state rational observation matrix has rank 9; each path is a signed-native X6 sequence of the six original operations, returns +2E1, belongs to the declared positive full BRC cache key, and all systems have exactly five keys and six original signature classes. All quota windows have counts `(4,2,2,4,2,4,4,2)` for H2–H9. This supplies eight **constructive upper bounds for their fixed subfamilies**; it is not a minimum-cost or a new global mother-problem upper bound. The best previously known mother construction remains 94 edges, target <=93.

For every case the exact words, late keys, 6-step late-key schedule, prior greedy cost, and improved native-prefix count appear in `WITNESSES_EC49FDW.json`. `VERIFY_EC49FDW.py` recomputes ranks by independent exact Fraction row reduction and counts ordered primitive signed prefixes directly. The validated outcomes are **8/8 examples, 64/64 horizon rank checks, 192/192 complete operator words**, costs `118,118,118,118,120,120,120,120`. Local source optimization used deterministic-seeded perturbation plus exact marginal-cost single-signature substitutions, followed by this independent full certificate audit; optimization is a *search* not a proof of optimality.

## Conserved native-length lemma

Let `k=(x,y,z)` count the positive `(+E1,+E2,+E3)` native primitives of any valid complete operator word, and suppose its total native signed displacement is `+2E1`. The negative primitive counts must be `(x-2,y,z)`. Therefore **every such complete word has exactly `L(k)=2(x+y+z)-2` signed primitive steps**, irrespective of its operator horizon `h`. In particular all H7, H8 and H9 words using the same C key occupy the *same primitive trie depth* despite differing in operator length. This lemma is an exact identity of the declared six-operation model, and applies to the literal signed primitive strings; it does not identify complete words that differ in order. The operation codewords are prefix-free because their first two signed primitives distinguish a,c,d,e,f,g, so comparing the trie by actual primitive tuples is faithful to the original ordered path accounting.

The local search exploited the equality of these primitive-depth costs and kept the full signed sequence: no aggregation to positive masses or sign-free length was used. It modifies the previously supplied EC49FDV witness inside the same frozen scientific model and retains the full nine-history observer.

## Reproduce and next question

Place the accompanying two UTF-8 files together and run `python VERIFY_EC49FDW.py` (Python standard library). The independent witness checker contains all scientific operation tuples and observer update semantics and does not depend on a live solver, old model cache, or SciPy. For provenance and wider regeneration, EC49FDV's original parent package contains the full exact literal word-pool generator; this turn's stochastic source and eight-record local JSON are also preserved in the downloadable local handoff archive.

**Next EC49FDX:** jointly optimize horizon pairs H7/H8 over the same primitive trie rather than replacing one signature class at a time; include the four exceptional H4-mixed triples and non-three-phase schedules as separate branches. Search for a <=93 full valid witness, or derive certified lower bounds under precisely specified fixed-key/early-seed subfamilies. The reported 118/120 values do not exclude stronger improvements.

GitHub author-side files are research evidence; no Source-native CLAIМ/Result/independent Driver acceptance is inferred from this commit.
