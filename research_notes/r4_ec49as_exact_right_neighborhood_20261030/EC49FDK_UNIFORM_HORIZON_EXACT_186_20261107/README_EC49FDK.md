# EC49FDK — exact signed-native prefix minimum on all 186 horizon-uniform five-key rank-nine schedules

2026-11-07; scientific input frozen at **fc0f038e7bfd12c886b4d37f900bfb770c0f61ab**. Status: **AUTHOR EXACT FINITE RESEARCH / EXECUTED / UNREVIEWED / NOT ADMITTED**. P000 and ACTIVE worldview unchanged.

## Exact question and result

Fix the original signed primitive operation alphabet (with complete ordered X6 provenance), H2/H3 paths **fe, ge, feg, gef**, giving 16 distinct nonempty signed primitive prefixes and three full positive BRC cache keys. Allow exactly **two additional distinct full positive keys** for H4 through H9. Require the original six nine-state observer signatures D=de, E=ed, C=ce, J=ec, F=feg, G=gef and rational rank nine at every horizon. **Within each horizon all operation paths share one of the two keys**, but the chosen key may change without restriction between horizons.

The preceding EC49FDJ complete integer-key and signature census yielded 124 rank-nine key pairs, 174 monotone one-switch schedules. A full rank-nine mask of a single key at an individual horizon can be exactly **15 = D|E|C|J** (four required words) or **48 = F|G** (two required words). Its six-signature mask takes one of 0, 15, 16, 32, 48 in this finite model. Thus the per-horizon required labeled paths are uniquely determined by the selected key. This observation is essential: only 16 of EC49FDJ's 174 schedules realize the older predesignated 20-label pattern.

Enumerating every independent choice of an individually rank-nine key at H4, H5, H6, H7, H8, H9 gives **186 distinct (key pair, six-horizon selection) schedules: 174 monotone and 12 nonmonotone**. Their variable-label counts are **60 cases with 20, 104 cases with 22 and 22 cases with 24**, including nonmonotone schedules.

**Theorem (exact domain above).** For every one of the 186 schedules, selecting one legal ordered native operation word per required horizon-signature label has a union of signed primitive prefixes of at least **112 edges**. At least one schedule attains **112**. Therefore the exact family minimum is **112 edges**. The unique schedule reaching 112 in this census is early **(4,2,1)**, late **(6,4,1)**, selection **EELLLL** at H4..H9.

This proves a finite cost obstruction for the entire **horizon-uniform five-key family**. The original five-key <=93-edge mother problem remains open for **mixed keys within a horizon** or an admissible different H2/H3 seed; the pre-existing author-side 94-edge witness should be examined for precisely which route it uses.

## Exhaustive method, independent bound and evidence

For 164 schedules with 20 or 22 variable labels, enumerate the **complete ordered BRC operation-word language** for each required label. Encode every word as ordered signed native primitive steps, construct the merged Trie, and mark each edge that is already in the 16-edge fixed-seed Trie as zero incremental cost. Exact bottom-up disjoint-subset dynamic programming assigns every required label once; a child edge is charged once iff at least one selected leaf label uses it. The recurrence combines disjoint label subsets with integer addition/minimum and yields an exact global minimum for each of the 164 restricted languages. The minimum of these 164 exact values is 112.

For each of the 22 remaining 24-label schedules, **remove every H8 requirement**, leaving exactly 20 labels and running the same complete exact solver. Removing requirements enlarges feasible choices, so the relaxed optimum is a rigorous lower bound on the original schedule optimum. The **minimum of these 22 lower bounds is 146**, already above 112. Thus all 186 schedules are mathematically covered without doing expensive 24-bit full searches. The 12 nonmonotone schedules have minimum 140 (exact in this run). The combined executed C++ DP inspection counter for 164 exact cases plus 22 relaxed cases is **11,882,228,808 inspected state pairs**; this is an execution counter, not an asymptotic complexity claim.

The explicit 112-edge original 24-path word witness and independent Python full-model verification are preserved in predecessor **EC49FDE@2c4fbecf6a11e44ec944d1d942f74e549aa721e0**. The actual executed primitive Trie solver is the same source as earlier **EC49FDG** (DP_EC49FDG.cpp, fixed-source 16-edge seed) reused here for the larger label sets. The current compressed certificate stores all **186** keyed results as exact values or identified H8-dropped lower bounds, label counts and inspected-pair counts; gunzip and parse the UTF-8 JSON, whose complete newline-terminated SHA-256 is **046182aabca3ecd3db638d66a4fa54cbe991006de95aa964579a396459bc19b6**.

The accompanying VERIFY_EC49FDK_CENSUS.js recomputes 124/174/186 schedules directly from the EC49FDJ source, checks 16 older predesignated schedules, checks all 186 certificate schedule IDs and the exact/lower-bound distribution, min values and plaintext digest. It was run successfully against the source-compatible EC49FDJ compute output. Numeric exact DP results were obtained by actual C++ runs and their individual batch scripts; the JS verifier checks the certificate, and **does not re-execute every large numeric DP**. An all-in-one Python replay was prepared but not run through all 186 cases; retain original executed batch reports for reproduction. Scientific pin, exact scope, signature masks, cost semantics and provenance remain distinct.

## Next discriminating research — EC49FDL

Investigate **two-key mixtures within the same horizon** at fixed H2/H3 and original six signatures. For a key pair and horizon, enumerate all legally typed candidate words from both keys and run an exact prefix Trie cover per required signature. Test the 94-edge witness and seek <=93; if no witness, report bounded exact lower bounds on the actual mixed-key languages. An independent second route is to alter the H2/H3 seed while retaining the full five-key ceiling and P000.

## Source, authority and state

Predecessor source: EC49FDJ, immutable commit **22f918d0c8dd1df0c3ec1808916d9818e4b280e0**, with original 124-pair / 174-schedule certificate and nine-state verifier. Current work reuses frozen scientific source **fc0f038e7bfd12c886b4d37f900bfb770c0f61ab**; latest behavioral policy is read separately.

GitHub actor: awdawmip (author-side research branch). At this run, native Enterprise Math gateway returned **BACKEND_IDENTITY_OR_VERSION_MISMATCH**, **operation_sent=false**; current Source owner/CLAIM/Result and independent mathematical Driver admission are pending.