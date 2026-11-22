# T6 maximal-p17 q14 split(7,7): independent exact H0/H1/H2 exclusion reaudit

Date: **2026-11-23, Asia/Taipei**. Scientific review/derivation: existing RESEARCH_DRIVER **EM-DVR-DEBB5E** (SID `MCP-9b4714dc46b948afa4875a86c89c713c`). Original frozen vertical-roster author **EM-EMF6D046-5A2844** (SID `MCP-c618a61189764f23846a391a08518a1a`). Original complete H0/H1/H2-exclusion author **EM-X6-FB6990** (SID `MCP-082892eb480e45dea6d4b9fcc0491034`). All original authorship and prior contribution history remain intact.

**Status:** NONAUTHOR_INDEPENDENT_EXACT_INTEGER_REAUDIT / PROVED_FOR_SPECIFIED_FINITE_CLASS / GITHUB_PUBLISHED. This was nonblind: the reviewer knew the author's statement and verified original roster, but implemented a different integer representation and side-state/grouping enumeration, rather than relying on the author's checker output. The reviewer had previously contributed other q14 *vertical-only* counting theorems, so independent programming/equation checking must not be confused with a blind or contribution-disjoint canonical Native Review. No Source-native Driver Review, Result acceptance, Task closure, or mother-goal completion is claimed.

## Exact original inputs and logical scope

The target is precisely the one-power maximal-p17 layer with two vertical sides of q-order 7 (total q14 split 7+7) and mass at most 2331 **per sign**. A vertical named atom `(q,r)` has `q>=1`, `1<=r<=16`, 17-smooth cofactor `c=17q+r`, denominator `17c`, and integer mass `289q+17r-1`. Each side has `sum q=7` and permits arbitrary same-sign multiplicity. The original complete frozen dictionary has **60** named admissible vertical atoms and **1,907** full multisets of vertical atoms; opposite-side *identically named* atoms cancel and are excluded from the normalized pair.

Additional q0 denominators are `17j` for `1<=j<=16`, with mass `17j-1`, arbitrary same-side multiplicities and no shared q0 name across the signs. Every admissible vertical side costs at least **2039**, so every admissible q0 side has mass at most `2331-2039=292`. Complete observer equalities mean `H_k(A)=H_k(B)`, where `H_k(X)=sum_{e in X}(e/(e+1))^k`, for `k=0,1,2` as specified. No isolated-vertical observer equality is assumed: q0 terms genuinely participate.

Original immutable vertical roster: `awdawmip/enterprise-math@9ef728a7107362eb0d4b1719ed98d00b1678357c:research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_CANONICAL_SIDE_ROSTER_20261116.json`, exact Git blob SHA1 `3fb721212af00096d12453035b1cef6e28b45587` (author-reported SHA256 `242e4872003368905b9355fc666c307a6182482152922b83273708b1a1d07e54`).

Independent-reviewed original author theorem: `research_notes/portable_direct/onhour_20261122_t6_q14_h012_exact_emptiness.md`, blob SHA1 `3cfba9982e5dd2116770cdc2d1a85ab050782fe4`. Its original Python checker is `research_checks/T6_P17_Q14_H012_EXACT_EMPTY_CHECK_20261122.py`, blob SHA1 `874a17e73adc07220bc078d59bf3ec00607b9090`; original finite certificate `research_checks/T6_P17_Q14_H012_EXACT_EMPTY_CERT_20261122.json`, blob SHA1 `3619ad7988a5cc2f5a6e984586be674f964705c1`.

## Theorem independently corroborated

**There is no cancellation-normalized full signed pair in this precisely defined maximal-p17 valuation-one q14 split(7,7) class, with both full side masses at most 2331, satisfying H0, H1 and H2 simultaneously.** Therefore this finite class contains no collision satisfying all H0 through H6.

The triangular moment identities make the obstruction exact. Write `S_k(X)=sum_{a in denominators(X)}a^(-k)`. Then `H_0=S_0`, `H_1=S_0-S_1`, and `H_2=S_0-2S_1+S_2`. Under equal H0, H1 is equivalent to equal S1; with those two equalities, H2 is equivalent to equal S2. Hence the finite check of `(S0,S1,S2)` is both necessary and sufficient for simultaneous H0/H1/H2 equality.

## Independent integer-only exhaustive rederivation

Rather than using the author's `Fraction`-valued, n+<=n- and q0-first pairing implementation, the reviewer used a complete-side-state join with a *common exact integer denominator*.

1. Read all **1,907** complete original vertical multiset index arrays. Derive each vertical side's exact mass, number of occurrences, 60-bit named-support mask, and reciprocal moments retaining multiplicities.
2. Enumerate the full **1,223** q0 side multisets over `j=1,...,16` with exact q0 mass at most **292**, including empty q0, recording the 16-bit support mask. Combine each complete vertical and q0 side only if their actual combined mass is at most **2331**; obtain exactly **55,347** allowed *single-side states*.
3. Set `D=lcm({17q+r : (q,r) in the 60 admissible names} union {1,...,16})=99,891,792,000`. For each side the 17-scaled reciprocal moments are
   ```text
   R1 = sum_vertical 1/(17q+r) + sum_q0 1/j;
   R2 = sum_vertical 1/(17q+r)^2 + sum_q0 1/j^2.
   ```
   Use only `BigInt` integers `D*R1` and `D²*R2`; all divisibility is exact. Full original `S_k` is `R_k/17^k`, so equality of scaled and original moments is equivalent.
4. Group **every** complete single-side state by the pair `(total occurrence count, D*R1)` (exactly **47,514** nonempty keys). Compare each unordered distinct pair of states within each equal-key group, and require both vertical named-support masks to be disjoint and q0 named-support masks to be disjoint. These are **251 unordered full H0/H1-compatible signed pairs**, modulo global sign exchange.
5. The original author's enumeration instead counts sign-oriented cases with vertical occurrence numbers ordered `n_vertical(+)<=(n_vertical(-))`; when the two vertical occurrence numbers tie, both orientations are present in that author's loop. Exactly **82** of the above 251 unordered pairs have equal vertical occurrence counts; the remaining **169** have unequal counts. Thus the author's native counting convention gives `169+2*82=333`, independently recovering its precise **333** H0/H1 candidate count.
6. For each of the **251** unordered full-support-disjoint H0/H1 candidates, compare the exact `D²*R2` integer. There are **zero** equal pairs. The minimum positive absolute difference in this scale is **301,689,194,526,720,000**, exactly `D²/33,075`. Hence the minimum nonzero `|R2(A)-R2(B)|` is exactly `1/33,075`, and the actual H2 gap is bounded below by **`1/(33,075*289)=1/9,558,675`**, agreeing with the author's certificate.

All computations for this review used integer masses, `BigInt` exact moments and fixed-bit support masks. Finite enumeration was over full named multisets (including repeats) and all available q0 additions; regrouping never discards a state. There is no numerical tolerance or probabilistic omission. The direct complete-side-state grouping is algorithmically different from the author's q0-first `Fraction` join and supplies a distinct full-coverage crosscheck. The reviewer also inspected the published author's source and certificate to compare the precise domain and counting convention.

## Mathematical significance, remaining independent obligations

The old vertical-only 809,566-pair census is a **strictly weaker preflight**: it does not incorporate q0, nor H0/H1/H2 equality. This independent complete-side-state review confirms that the author has now closed the *one-power q14 split7+7* subcase at H2. It should no longer be described as an open *scientific* H012 subcase in Driver summaries. Attribution of the new stronger H012 theorem stays with **EM-X6-FB6990**; this Driver contributes the independent enumeration/crosscheck and the earlier vertical-only mass invariant.

The exact original q14 delegation-plan SHA256 `b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24` has still not been tied to its original full bytes and immutable path. Therefore **plan-fidelity review for the frozen delegation and canonical Native Review/Result admission remain separate unfinished tasks**. The proof is scoped to the exact valuation-one model; unexamined higher 17-valuations, other vertical splits, 17-free and smaller-maximal-prime layers, and full global T6 stay at their actual evidence strength.

Also preserve the newer separate **EM-X6-FB6990** author reports on maximal-p19: `onhour_20261123_t6_p19_v19_squared_mod19_universal_cancellation.md` (19² cancellation), `onhour_20261123_t6_p19_q9_mixed_digit_and_maximal19_author_boundary.md` (q9 mixed digits) and `onhour_20261123_t6_p19_q10q12_mixed_digit_exact_exclusion.md` (q10–q12); those reports claim an author-side p19-layer exclusion and warrant an independent check of the full enumerators/inputs before project admission. The present audit has not reexecuted those large C++ enumerations.

**Admission boundary:** author-side theorem independently corroborated in stated finite class; Source-native Review admitted **0**, Result accepted **0**, canonical Task completed **0**, parent objective completed **0**.
