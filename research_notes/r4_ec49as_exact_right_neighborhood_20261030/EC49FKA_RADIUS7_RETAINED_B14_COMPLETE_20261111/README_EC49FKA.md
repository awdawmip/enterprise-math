# EC49FKA — exact B=14 retained-key radius-seven native BRC minimum (2026-11-11)

**Status:** AUTHOR_EXACT_FINITE / TWO_EXECUTED_ALGORITHMS_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.  
**Frozen scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.  
**Source dependencies:** original frozen `EC49FGW_RADIUS5_SCREEN.py` generator, `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` A/B witnesses, and `FJR_CATALOG.tsv` from EC49FJR, all inside PR #1730 provenance.

## Exact finite theorem: 11,780 new sharp local optima

For either existing witness A or B, take the 24 labeled nine-state signed-native-X6 BRC observation-demand paths using exactly seven *complete raw cache key identities* and 94 distinct literal ordered/signed native microstep prefixes. Choose seven positions Q for replacement, fixing the other seventeen *original operation words* exactly. Write F(Q) for their literal nonempty prefix union.

Among all 346,104 choices Q per profile, precisely 153,408 keep all seven raw key identities on the fixed seventeen words; 192,696 release at least one key. Among the retained-key Q, precisely **5,890 per profile** have |F(Q)|=79, equivalently hypothetical 93-prefix incremental budget **B=14**. They form **26 fixed-prefix background classes per profile**, 20 classes of 275 Q plus 6 classes of 65 Q.

For each of these 5,890 Q in A and 5,890 Q in B, **every legal seven-word completion has at least 15 distinct new literal prefixes, and the original witness achieves 15**. Thus the exact total cost is **79+15=94** for all **11,780** corresponding local subproblems. This is **not** an all-constructions proof of C_min(7)=94.

| Disjoint obstruction arity | Profile A | Profile B |
|---|---:|---:|
| Two omitted observation labels | 1,100 | 1,100 |
| Three labels | 4,595 | 4,790 |
| Four labels | 195 | 0 |
| **Total sharp local 94 optima** | **5,890** | **5,890** |
| Unresolved in B14 retained-key class | 0 | 0 |

## Proof and exhaustive scope

For every legal original operation word w, retain full key k(w), typed observation label ell(w), and literal signed ordered X6 prefix set P(w). Since the seventeen fixed paths already occupy seven distinct complete keys, an at-most-seven-key completion can only use those same keys, rather than selecting an eighth key.

For each fixed F and omitted label ell, define the *complete* eligible incremental family:

`A_F(ell,14) = { P(w)\\F : w in frozen legal word catalogue; ell(w)=ell; k(w) in original seven raw keys; |P(w)\\F|<=14 }`.

A hypothetical total cost <=93 would select one member of A_F for **every** omitted observation label such that their seven-set union had cardinality <=14. Thus every subset of the seven omitted labels would also admit union <=14.

The first executed verifier enumerates **all 178,850 legal words, 94 complete keys, 9,838 words using the retained seven keys per profile** and every seven-position Q. For each of the 26 background classes in A and B, it finds a set S of 2, 3 or 4 observation labels that is omitted for *every* Q in that class and for which **no** selection from the corresponding complete A_F families can yield a literal union of size <=14. The algorithm's prefix-union antichain domination is exact: if U1 is contained in U2, then |U1 union V|<=|U2 union V| for any later V. No endpoint, sign, order, or cache-key identity quotient is taken.

The **second independently coded verifier** separately parses all **178,850 rows** of the frozen TSV catalogue, constructs literal signed X6 microstep prefix tuples, and exhaustively checks the **52** class-specific obstructing label subsets, retaining all distinct intermediate literal unions and eliminating **only exact duplicates** (no antichain domination). It also checks membership of S in every Q of the associated class. Thus no completion can have <=14 new prefixes; the original frozen 94-prefix witness provides the matching upper bound 15.

Observed execution success sentinels:
`EC49FKA_ALL_11780_EXACT_PASS` and `EC49FKA_DIRECT_ALL_11780_PASS`.

This establishes an exact **finite local** mathematical result under the frozen generator and signed native BRC model, not a formal proof-assistant check, independently admitted Driver Result, or global all-key optimization.

## Reproducible source and evidence

The adjacent **`EC49FKA_EXECUTED_SOURCES_CERTIFICATES.tar.xz`** contains the **two original actually executed verifiers** and all **52 compact per-background certificate records**. Neither script is a pseudocode-only replacement. To reproduce, extract archive and make a sibling `EC49FJR/` folder holding the exact frozen `EC49FGW_RADIUS5_SCREEN.py`, `EC49FGJ_SEVEN_KEY_94_WITNESSES.json`, `FJR_CATALOG.tsv` already published/derivable from prior PR #1730 files. Execute in this order: `python EC49FKA_R7_B14_VERIFY.py`; `python EC49FKA_R7_B14_DIRECT_CHECK.py`. The first writes `EXACT_REPORT_EC49FKA.json` (59,290 bytes original report), then the second writes `EXACT_DIRECT_CHECK_EC49FKA.json` (9,275 bytes original report). Do not substitute a different scientific input or normalize a native prefix to an endpoint.

Published compact archive original SHA256: `0a9af7093c2b4dc73998c68bab6b45f10e55294a50e9672552c1a6391ae11b34`; Git Blob SHA1: `af4435cd772b3b6e39951fe62880f920cd7529ca`.

The separate *conversation delivery archive*, `EC49FKA_R7_B14_COMPLETE_EVIDENCE_20261111.tar.xz`, additionally stores both complete per-class JSON reports and both actually captured execution logs (6,540-byte archive, SHA256 `072f46ac67b1ceffdece86955e7a94398c78bbca255991e19a7cf53558fcffb9`). The full archive is a conversation attachment, **not** part of this GitHub commit; the scripts in this GitHub directory regenerate those reports.

## Continuing mother problem and authority

The last verified retained-key radius-seven report EC49FJZ had 121,880 certified Q per profile, 31,528 retained-key contexts still open, and 192,696 released-key contexts. This new B14 class is disjoint and reduces retained-key unexplained cases to **25,638 per profile**; cumulative retained-key sharp Q become **127,770 per profile / 255,540 A+B**. Independent global 93-prefix construction search and the retained-key B15 class are next; released-key radius-seven contexts additionally require key-aware exact optimization.

No new formal CLAIM, Result, Driver review or P000/ACTIVE worldview change is asserted. Repository publication preserves the existing Draft PR provenance; mathematical admission is independent.
