# EC49CV — h=8 native signed-X6 BRC full saturation

Date: 2026-11-01 Asia/Shanghai.
Status: AUTHOR_EXACT_MODULAR_CERTIFICATE / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED.

## Frozen inputs and typed model

GLOBAL_KNOWLEDGE_V1 main@40c95779c44d4c55e420d207e1b20e9a6f9c9a80. Enterprise Math main@ace20a3785eb79ba4f7f4fa7299871fffc07a96e. Author predecessor EC49CU@a1e51c0f7e3b7283553c38e163fae1fb387aae8b; EC49CS formal-rank theorem@8ccf4816303707e0514f2cb61c7b398da9d3de25. P000 and ACTIVE worldview not edited.

A primitive prefix is an ordered word over the twelve signed six-axis directions ±E1,...,±E6 relative to one chosen Cell. These signed displacement coordinates are not public six-nonnegative-integer Cell addresses. Positive-letter BRC weights are W0=(2,3,3,2,1,1), W1=(3,2,3,2,1,1); every negative letter has weight 1. The third channel W2 counts paths with weight 1. Ordered adjacent substrings A=(+E1,+E2) and B=(+E2,+E1) produce four joint terminal tags through a nine-state DFA, including pending states. Native prefixes retain literal order, signed endpoint and provenance.

Complete suffix operations are a=(-E1,-E1), b=(-E2,-E2), c=(+E1,+E2,-E1,-E2), d=(+E2,+E1,-E2,-E1), e=(+E3,+E1,+E1,-E3), S'={a,b,c,d,e}. For prefix p and suffix operation word u, the observation R_(u,tag,channel)(p) is its exact positive integer BRC weight on the *literal ordered concatenation* p+u when the resulting six-coordinate displacement is zero and final A/B tag matches, and zero otherwise. Observers are rational-linear and additive over prefix path multiplicities. No signed/complex amplitude cancellation, physical time evolution or nonlinear memory statement is implied.

## New theorem: n_sat(8)=24

For h=8, the genuine prefix language of length n=24 attains the formal observation rank in **all 81 target displacement fibers** (2u,2v,0,0,0,0), v>=0, |u|+v<=8. The exact-h observer has rank **1248**, and the cumulative future observer for 1..8 complete operations has rank **1356**. Therefore the earliest saturated prefix length for both is **24**. Saturation holds for every larger even length.

### Upper bound (exact)

The prior all-h formal DFA rowspace theorem EC49CS yields exact-h dimension 3(11h^2+15h+8)/2 and cumulative dimension 18h^2+24h+12. At h=8 these evaluate to 1248 and 1356. The 81 cumulative target fibers consist of 17 boundary fibers of per-channel DFA row rank 4 and 64 interior fibers of rank 6, hence 3(17*4+64*6)=1356.

This study also independently calculated formal ranks over exact rational Fractions for h=1..8. The cumulative sequence is 45,132,246,396,582,804,1062,1356; the exact-h sequence is 45,123,228,366,537,741,978,1248. Exact suffix transformation deduplication maintains each pair (net displacement, full nine-state DFA transformation), not merely a four-tag projection. Two words with equal pairs have identical tag-indicator row vectors; their positive suffix BRC weights act only as nonzero scalars within each typed channel. There are 350 such signatures among all 390625 length-eight operation words, and 386 distinct signatures across depths 1..8. This explains a rigorous finite-state rowspace reduction, rather than a sampling assumption.

### Lower bound (literal nonzero minors)

EC49CV_COMPACT_CERT.json.xz.b64 contains a *lossless reconstructible* certificate: for each of 81 target fibers, 12 boundary or 18 interior **actual ordered length-24 signed six-axis paths**, represented by deterministic sampler seed plus exact accepted attempt indices; selected complete suffix-word and tag observation rows; and one recorded determinant modulo p=1000003. The included standalone VERIFY_EC49CV_COMPACT.py independently reconstructs each of the **1356 actual primitive paths** and all suffixes, replays six-component endpoint, checks literal adjacent A/B substrings and two positive weight products plus count, computes every full integer matrix, verifies rational independence of the nine-state feature rows, and recomputes each modular determinant without trusting the recorded determinant. All **81 nonzero square minors** pass. A nonzero determinant modulo a prime implies an integer determinant is nonzero over Q, giving genuine cumulative rank at least 1356; the exact formal upper bound forces equality. Restricting a full-rank representation of the entire cumulative formal rowspace to its exactly-eight subspace also attains its formal 1248 rank.

Sampling found candidate paths but plays *no probabilistic role in the proof*. The unusual (8,8,0,0,0,0) boundary target needed explicit rare tag-NONE constructions to complete its 12-dimensional minor. Their negative template indices are encoded in the certificate; the standalone replay rechecks them as literal paths. The exact expanded 1356-path JSON and full generator are retained in the attached expanded-evidence archive.

### Earliest length and propagation

The previous EC49CU extreme-target lemma supplies the strict necessary bound n_sat(h)>=2h+8 for every h>=4. Thus h=8 cannot saturate at an earlier even length, in particular not n=22. Adding a primitive neutral prefix (+E3,-E3) preserves all six endpoint coordinates and A/B completion while multiplying channels W0 and W1 by 3 and count by 1; therefore every n=24 rank witness extends rank-preservingly to all larger even lengths. Every target has even endpoint parity, so odd prefix lengths cannot attain all fibers. Combining necessity and the n=24 witness gives n_sat(8)=24.

## Verification and reproducibility

Run: python3 VERIFY_EC49CV_COMPACT.py EC49CV_COMPACT_CERT.json.xz.b64

Actual output: {"fibers":81,"modulus":1000003,"nonzero_independent_real_X6_minors":81,"rank":1356,"status":"PASS"}.

The compressed payload is standard base64 of xz-compressed JSON; it contains all selected suffix/tag pairs, seeds, accepted indices and nonzero minor residues. The Python checker is standalone, pure standard library. Random-number replay uses the standard Python random.Random implementation and the exact recorded seeds/attempts; an expanded literal-path JSON is also retained for runtimes requiring byte-independent path transport. Other executed local evidence includes a distinct direct-substring checker, an exact-Q formal rank report and signed native BRC kernel checks at primitive length 1 and exhaustive length 4. The source kernel for those primitive checks is pinned in the predecessor EC49CS signed_brc.py evidence.

This proves h=8 saturation *only* in the specified rational-linear additive, finite-future, typed positive BRC path model. The global sufficiency claim for all h>=4, physical propagation, infinite-future memory capacity, signed/complex amplitude inference and an independently admitted theorem remain open.

## Control and next question

Native service version 0.6.11 reports research_authority_granted=false. A bounded active Owner/task query returned CONTROL_QUOTA; current Owner remains unverified. No native task CLAIM, Result, Driver review, formal admission or P000/worldview modification is claimed. These files are author-side portable research evidence, not formal Source acceptance. Read NEXT_EC49CW.md for the h=9 and uniform-induction obligations.
