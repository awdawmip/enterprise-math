# EC49EC — Exact native-X6 shared-prefix cost (2026-11-02)

**Status:** AUTHOR_FINITE_THEOREM / EXECUTED_EXACT_CHECKS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED. Scientific source pins remain GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e` and Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current normative context read separately on 2026-11-02. Parent EC49EB, existing Draft PR #1730. Protected P000 and ACTIVE worldview unchanged.

## Question and primitive model

The signed native-X6 operations are `a=(-E1,-E1)`, `b=(-E2,-E2)`, `c=(+E1,+E2,-E1,-E2)`, `d=(+E2,+E1,-E2,-E1)`, `e=(+E3,+E1,+E1,-E3)`. Historical endpoint is `-2E1`; future words of exactly h operations must displace `+2E1`. The historical seam and future primitives are observed for first occurrences of adjacent positive pairs `A=(+E1,+E2)`, `B=(+E2,+E1)` with terminal buckets `N,A,B,AB,BA` (the latter two distinguish the first-event order).

Nine real ten-step X6 histories realize historical atoms `N0,N1,N2,A0,A2,B0,B1,AB,BA`, all with positive counts `(2,2,0,0,0,0)`; their nine-feature determinant equals -1. For a finite set W of distinct returning future words, define `T(W)` as the number of distinct nonempty **signed primitive-step prefixes** of the fully expanded paths, i.e. the number of edges in their shared native primitive trie. Compute all five terminal-bucket indicator columns per word and require rational rank 9 on the nine atoms. `T_equal` additionally requires identical complete six-axis positive counts for all selected words. Full ordered paths, word identities and terminal labels are preserved, and each strictly positive BRC channel can remove the known nonzero future factor independently.

## Theorem EC49EC-1 — exact optimum at h=2,3,4

| h | exact returning word inventory | distinct transfer signatures | prior independent primitive cost | minimum T | minimum T_equal |
|---|---:|---:|---:|---:|---:|
| 2 | 4 | 4 | 32 | **28** | **28** |
| 3 | 15 | 9 | 34 | **34** | **44** |
| 4 | 56 | 8 | 56 | **46** | **46** |

These optima quantify over **all subsets**, including those with more than four words. The full signed primitive tries, all words and signature classes, each checked class family, selected independent columns, exact determinants and representative enumeration counts are in `EC49EC_EXECUTED.json`.

## Proof — completeness, not just example search

Return displacement gives `n_b=0`, `n_e-n_a=1`, `h=n_c+n_d+2n_a+1`, with future positive vector `(h+1,n_c+n_d,n_e,0,0,0)`. The primitive length of a word is `4h-2n_a`.

For each returning word its *transfer signature* is the entire 9-by-5 zero-one matrix of final bucket observations on the real historical atoms. Identical signatures yield identical observer columns; distinct known positive BRC factors merely rescale the corresponding column in each instrument. Removing duplicate-signature words cannot reduce observer transfer rank, and dropping words cannot increase a prefix trie. Likewise, an inclusion-minimal signature subset suffices whenever a larger signature set has rank 9. Therefore it is mathematically exhaustive to enumerate one representative from each class in every inclusion-minimal full-rank signature collection.

Exhaustive enumeration of all original `5^h` words leaves 4/15/56 returning words, grouped into 4/9/8 exact signatures. Enumerating all 2^4/2^9/2^8 class subsets, the **only** inclusion-minimal full-rank signature index sets, 0-based with classes sorted by their first lexicographic word, are:
- h=2: `{0,1,2,3}` (classes `ce,de,ec,ed`).
- h=3: `{0,1,4}` or `{1,4,5,8}`. Relevant classes are `{aee,eae,eea}`, `{cce,cec}`, `{dde,ded}`, `{ecc}`, `{edd}`.
- h=4: `{0,1,2,4}`. These classes are `{acee,aece,aeec,eace,eaec,ecae,eccc,ecea,eeac,eeca}`, `{adee,aede,aeed,eade,eaed,edae,eddd,edea,eead,eeda}`, `{caee,ccce,ccec,ceae,cecc,ceea}` and `{daee,ddde,dded,deae,dedd,deea}`.

The signatures are zero-one, and every minor has order <=9. Hadamard's bound is `|det_k|<=k^(k/2)<=9^(9/2)<1000003`; hence a modular rank over prime 1000003 equals rational rank for all class subsets, including negative rank claims. Two independently executed exact checkers (Python standard library and standalone JS) reproduce the above class enumeration. All representative choices in the minimal families were checked: **1** at h2; **12+4=16** at h3; **3600** at h4. Under equal positive counts the admissible choices are **1**, **4**, and **729+9=738** respectively. This is a complete finite certificate.

A direct signed-prefix lower-bound argument also explains the minima. At h2 all four words have 8 primitives and only `ec/ed` share their initial four-step `e`: `32-4=28`. At h3, `{0,1,4}` needs one length-10 no-event word plus `c`-first and `d`-first length-12 words, with distinct initial signed primitives, giving 34. The alternative four-class family has four 12-step paths and only `ecc/edd` share a common four-step `e`, giving 44; only this family satisfies equal positive counts. At h4, classes 0 and 1 begin with `a` or `e`, class 2 begins `c`, and class 4 begins `d`. Their four primitive lengths are >=14. Only one pair, classes 0 and 1, may share an initial signed prefix; its maximum possible length is 10, realized by `aeec/aeed` sharing `aee`. Therefore `T>=4(14)-10=46`. Witnesses below attain each bound. Combined with the duplicate-signature lemma this proves global optimality within each stated finite h.

## Exact witness data

- h=2: `ce,de,ec,ed`, trie **28**, individual total 32, shared `e` prefix four steps; common positive vector `(3,1,1,0,0,0)`; nine-column determinant **-1**.
- h=3 unrestricted: `aee,cce,dde`, trie **34**, determinant **+1**; vectors `(4,0,2,0,0,0)` and twice `(4,2,1,0,0,0)`.
- h=3 equal counts: `cce,dde,ecc,edd`, trie **44**, individual total 48; common vector `(4,2,1,0,0,0)`; determinant **-1**.
- h=4 both cases: `aeec,aeed,caee,daee`, trie **46**, individual total 56; common vector `(5,1,2,0,0,0)`; determinant **-1**.

The JS verifier reconstructs all nine actual native signed histories, checks historical endpoints and positive counts, calculates full across-seam terminal buckets on concatenated paths, and checks two BRC multiplicativity equalities using positive integer instruments. The independent executed Python checker performs the same native-path and rank audit. For every strictly positive real parameter choice, `X(hw)=X(h)X(w)` and `Y(hw)=Y(h)Y(w)` follow exactly from positive-count addition; nonzero factor scaling preserves column rank. The finite class theorem is model-internal and makes no physical-outcome claim.

## EC49EC-2 — proven all-h construction bounds, with open optimality

For integer k>=0, append `(ae)^k` to every word in any displayed witness. Each `ae` has zero native displacement and six signed primitive steps, creates no A/B positive adjacent pair, and leaves seam transfer unchanged because preceding operators end in negative steps. Distinct original leaves stay separate when extended, giving exactly six extra trie edges per selected leaf per appended pair. Thus `T(2)=28`, **`T(h)<=12h-2` for even h>=4**, **`T(h)<=9h+7` for odd h>=3**, **`T_equal(h)<=12h-2` for even h>=4**, **`T_equal(h)<=12h+8` for odd h>=3**. These are constructive upper bounds; optimality for h>=5 is an open EC49ED question.

## Reproducibility, tool reuse and custody

`VERIFY_EC49EC.js` is a standalone reproduction of the exact function executed in this publication run; run with `node VERIFY_EC49EC.js`. `EC49EC_EXECUTED.json` is its captured complete report. Python standard-library source, its independently generated full JSON and a SHA256 manifest were also generated locally, and its numeric conclusions and determinants agree. Typed BRC and order-sensitive transfer are **REUSE_APPLIED** from EC49DZ/EC49EA and signed primitive-cost semantics from EC49EB; the shared native prefix optimizer **EXTEND_EXISTING_TOOL** preserves full path provenance.

As of 2026-11-02, native session registration returned `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`), and active-owner listing returned `CONTROL_QUOTA`. No source-native CLAIM/Result/independent Driver review was issued or asserted. This GitHub PR contribution is **author-side portable evidence**, not canonically admitted research.