# EC49DZ — Exact nine-feature transfer, reduced to three future operations

Date: 2026-11-02. Project: Enterprise Math / native signed X6. Status: AUTHOR_ANALYTIC_PROOF / EXECUTED_EXACT_AUDIT / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. Parent: EC49DY at ea3fb17da0735615f9c25f9d33967b47f3fbb561 (Draft PR #1730).

Frozen scientific-input pins inherited from EC49DX–DY: GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current separately verified normative snapshots in this run: global canonical main `aa5e3ee8aa3481ececba9181847bb7b28a9ba41f`; Enterprise Math canonical main `89453173bf0e78d01726362d8f8d79c115235346`. Protected P000/ACTIVE worldview are unchanged.

## Exact question and observer

Use all six genuine native signed X6 axes with ordered primitive words, history displacement D=(-2,0,0,0,0,0), and any finite history population. Define A=(+E1,+E2) and B=(+E2,+E1). Historical terminal classes: N (neither), A-only, B-only, AB (A first), BA (B first). The nine historical features, in this fixed order, are

```
z9=(1[N],1[A],1[B],1[AB],1[BA],
    1[A and L=+E2],1[B and L=+E1],
    1[N and L=+E1],1[N and L=+E2]).
```

Here L is the last historical primitive, with other endpoints treated as port 0. Strictly positive BRC instruments are `X(w)=prod_i x_i^p_i(w)` and `Y(w)=prod_i y_i^p_i(w)`, where `p_i` counts +Ei; negative primitives have weight one. Third instrument counts paths. Thus `H9(w)=(X(w)z9(w),Y(w)z9(w),z9(w))` has 27 columns.

The original fixed open-loop future operations, written by signed axis index, are `a=(-1,-1)`, `b=(-2,-2)`, `c=(1,2,-1,-2)`, `d=(2,1,-2,-1)`, `e=(3,1,1,-3)`. Future words must return full X6 displacement +2E1. Read all five terminal buckets separately, in each of the X,Y,count channels. These are formal native-path observations, not physical experimental claims.

## Theorem — a minimum three-letter returning language suffices at every horizon

For **all** strictly positive real x,y, **every** finite genuine historical population at D=-2E1 and **every** integer future operator horizon h>=2, the subalphabet `Gamma0={c,d,e}` already satisfies

```
rank O(Gamma0,exactly h) = rank H9;
rank O({a,b,c,d,e},exactly h) = rank H9.
```

The same identity holds for cumulative horizons 1..h. No subalphabet with fewer than three of the original operations can recover all nine historical Boolean features on the full native history domain for all h>=2. In particular, b never participates in an original-alphabet return word because its -2E2 net displacement cannot be cancelled; a is not needed for nine-feature observability.

### Analytic proof: upper factorization

Any future fixed word t contains internal A/B events known from t, plus at most one seam event (last primitive of w, first of t). N only needs terminal ports +E1/+E2 to resolve the seam. A-only additionally needs its +E2 port to detect a first B at the seam; B-only needs its +E1 port to detect a first A. AB/BA already retain their first-occurrence order forever. This proves that every terminal bucket indicator of w·t is a **linear** function of exactly z9(w), with integer coefficients. Positive counts add under concatenation, hence X(wt)=X(w)X(t) and Y(wt)=Y(w)Y(t). Consequently every future observation column factors through H9 and `rank O<=rank H9`, independently of the future language.

### Analytic proof: a uniform nine-column right inverse

At exact operator horizon two, the only returning words over c,d,e are `ce,ec,de,ed`. The independent seam-transfer audit constructs their integer 9-by-5 matrices using the nine genuine historical state atoms. For the ordered nine word:bucket columns

```
ce:A, ce:AB, ce:BA, de:B, de:AB,
ec:A, ec:AB, ed:B, ed:AB
```

the **exact 9-by-9 determinant is +1**. The verifier supplies every transfer coefficient; each is calculated directly from the seam and internal signed primitive adjacency.

For any h>=2 put k=h-1 and choose

```
c^k e,  e c^k,  d^k e,  e d^k .
```

Each c begins +E1, ends -E2 and contains exactly internal event A; each d begins +E2, ends -E1 and contains exactly event B; e begins +E3, ends -E3 and contains no A/B. Every operation ends with a negative primitive, so inter-operation boundaries contain no A/B event. Repeating only c or only d adds occurrences of an event already present and cannot change first-occurrence order. The historical seam depends only on the first operation. Hence the four transfer matrices, in the order displayed, are **identical** to ce,ec,de,ed for every k>=1. The same determinant +1 witnesses the full nine-dimensional feature span at every h>=2; no finite-horizon extrapolation is used.

All four words have full native displacement +2E1 and the identical positive count vector `(h+1,h-1,1,0,0,0)`. Their future multiplicative factors are therefore the same within each instrument:
`X_h=x1^(h+1)*x2^(h-1)*x3>0`, `Y_h=y1^(h+1)*y2^(h-1)*y3>0`, and count factor 1. All three 9-by-9 blocks remain invertible. The resulting future-column space equals the 27-column H9 space on any finite historical population, proving equality.

### Analytic proof: three letters are necessary

Any returning future word needs +2E1; e is the only original operation providing positive net E1. Without e, there are no returns. With e and b only, the uncancelled -2E2 contribution of b excludes returns at h>=2. With e and a, neither operation produces A or B internally or at operation boundaries; all port-sensitive historical features are invisible, so at most the five terminal bucket flags remain. With e and c but not d, a history initially in B-only has its last +E1 port never consulted (no future primitive begins +E2), so the independent feature 1[B and L=+E1] remains unobservable; the symmetric argument applies to e and d without c. Thus no two-letter subalphabet has full nine-feature observability on the genuine nine-atom historical domain. The explicit nine genuine length-10 histories in the checker all have identical p=(2,2,0,0,0,0), exact D=-2E1, and z9 determinant -1; this prevents an artefact of an unrealizable symbolic history state.

## Exact execution / evidence boundaries

The self-contained JavaScript checker `VERIFY_EC49DZ.js` was **actually executed** in a V8 runtime in this research turn, returning PASS. It independently regenerates signed six-axis paths, seam transitions, all 9×5 matrices at h=2 and 3, verifies 4 and 15 returning words respectively, and verifies nine genuine length-10 history witnesses with common positive count vector and exact z9 determinant -1. It uses BigInt Bareiss arithmetic for the +1 nine-column transfer determinant, compares the uniform padded witnesses at h=2..8, checks all six displacement components, and for two explicit positive integer instrument vectors checks both BRC multiplicative identities on all nine actual histories and padded future witnesses.

The attached `EC49DZ_EXECUTED.json` contains actual executed matrices, words and checks. A separate Python standard-library implementation was executed locally; it additionally exhaustively checked every subset of the five-operation alphabet for h=2..6 with exact rational elimination. Its observations agree that the unique cardinality-three exact-horizon-full-rank subset is {c,d,e}; this extra local check is corroboration, not required for the infinite-horizon proof. No finite numerical check is promoted into a theorem without the analytic argument above.

This improves EC49DX's previously used `(ae)^k` parity promotion: **neither a nor b is needed**. It does not alter EC49DX/DY historical-rank classifications, which may be invoked with their original author-side evidence strength. No formal Result, independent Driver review or Foundation admission is established by source publication.

## Authorization and next question

Current GitHub login: `awdawmip`; PR branch publication uses normal authorized repository write access. Native gateway status exposed `research_authority_granted=false`; owner listing returned `CONTROL_QUOTA`; registration of this RESEARCHER's own native session returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. There is therefore no authenticated RA/CLAIM/Result/Driver review for this author-side unit, and no verified active owner to take over. Continue as portable source material only.

Next EC49EA: minimize the **number of distinct returning future words and observed output columns** needed at each h, not just the size of the operation alphabet. At h=2 the original four returning words are necessary (each subset of three has rank 7); determine whether 3 returning words can ever suffice at greater h, and prove a sharp horizon-uniform lower bound or exhibit the first exact counterexample. Preserve the genuine X6 seam, event order, both positive BRC factors, all historical fibers and the frozen input pins.
