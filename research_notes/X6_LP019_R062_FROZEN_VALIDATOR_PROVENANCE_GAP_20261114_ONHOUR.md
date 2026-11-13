# X6 LP019 — R062 Stage-0 original validator recovered and exact replay-count crosscheck

Observed 2026-11-14. Mother task `RS-X6-LEGACY-PLANE-RECONCILIATION` / publication `TP2-B4A441B23DA3159232C2`.
TASK_RESEARCH author-side provenance and algebraic certificate. **Not** a new native benchmark, Source semantic PROGRESS, formal Result, or independent review.

**Frozen science remains unchanged:** signed P000 V5 / centered X6 baseline `59538f585d037d09ef687b28715c4bc1a3f9fe03`; pre-rebase plane baseline `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

## 1. Exact historical source recovery

At frozen `fd2bcff1`, `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` (Git blob `6ec0d73a19e28ec586c59a97d24f5798c9119771`, lines 213–231) names `scripts/r062_stage0_validate_brc_multipath_bridge.py` and reports its accepted replay. That script is **not at that path on frozen main or current main** (two GitHub Contents 404 observations); main-path commit history returned `[]`. These are correct *main-tree* observations but do not establish that the historical checker is absent.

The original Driver's frozen review, `driver_reviews/R062_STAGE0_BRC_MULTIPATH_ENRICHMENT_BRIDGE_DRIVER_REVIEW_20260821.md`, immutable blob `d46593b6c2c257d5ff43f653ab32eb0385b238dd`, explicitly records the original owner branch:
`research/r062-stage0-brc-multipath-bridge`.

**Recovery succeeded on that named branch:**
- Original deterministic integer-only checker: `scripts/r062_stage0_validate_brc_multipath_bridge.py`; exact connector-returned Git blob **`48ba38a55969b32fab40bc33d066b10216a249d0`**, 30,847 bytes, 730 lines.
- Original replay summary: `research_results/R062_STAGE0/R062_STAGE0_REPLAY_SUMMARY.json`; blob **`b47be0fe8dd110f0b2af4160110d07ece06bd2f0`**.
- Original mismatch certificate: `research_results/R062_STAGE0/R062_STAGE0_MISMATCHES.json`; blob **`1961317cf182795454243ebdb58e26aaf7ff1583`**.
- Original reproducibility proof: `research_results/R062_STAGE0/R062_STAGE0_REPRODUCIBILITY_PROOF.md`; blob **`18b86510877a04ec9ef1e9dffb39bc8bcdf7c685`**.
- Original return: `research_results/R062_STAGE0/R062_STAGE0_FINAL_RETURN.md`; blob **`6ae618335ad0705ef887f2ad3086fdbb1194c6db`**.
- Current centered-signed retyping is separately maintained at `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` main blob `97ab1403ab04b4fa80034625fb1b2e3ed115e59b`; the older owner branch is **historical evidence**, not a new P000 source of authority.

The original replay summary actually contains the Driver-reviewed exact counts and 15 explicitly named `acceptance_gates` all `true`, `mismatch_count=0`, `no_duplicate_witnesses=true`, `translation_covariance=true`, and witness replay SHA256
`175c7f0efa6e62497dde5abbb65d354ddfc17a557f37640ee30260815cd68726`.
The historical R061 Stage1R regeneration component also records `pass=true` with SHA256 `359474ba6b53ffbb3c326cf331d55dd3ed098837451a46b0754926b7c642d702`; the original mismatch file reports an empty `all_mismatches` array.

This unit **read these exact original files**, but did **not** re-execute the 730-line old checker or rederive the reported witness SHA256. Its recorded accepted result is supported by the frozen Driver review and original owner artifacts, not by an invented current execution.

## 2. New direct exact combinatorial certificate for three headline counts

For one historical positive two-generator sector and one translated start, count every pair `(a,b)` with `a,b>=0`, `a+b<=12`. For fixed `n=a+b`, there are `n+1` distinct traces and `sum_{a=0}^n binom(n,a)=2^n` ordered positive generator words. Their total primitive transition count is `n*2^n`.

Because the original archived source explicitly enumerates **7 translated starts and 3 labeled sectors**, the following exact formulas hold for the specified finite historical model:
```text
translated_traces   = 7*3*sum(n+1, n=0..12)  = 21*91     = 1,911
path_occurrences    = 7*3*sum(2^n, n=0..12)  = 21*8,191  = 172,011
center_transitions  = 7*3*sum(n*2^n, n=0..12)
                    = 21*(11*2^13 + 2)      = 1,892,394
```
Independent exact Python integer enumeration with `math.comb(a+b,a)` over all `(a,b)` and a separate closed-form calculation both actually executed and agreed:
`PASS_R062_STAGE0_EXACT_REPLAY_COUNTS`, with per-start words `24,573` and per-sector words `57,337`. These results match the recovered original `native_bridge_enumeration` object field-for-field on the three totals and margins.

This is an **author-verified algebraic count check** on the original finite trace-combinatoric input; it does not replace the accepted original native-history replay, duplicate-witness checks, bridge typing, or hash verification.

## 3. Disposition and preserved frontier

- `LP019_R062_HISTORICAL_REPLAY_VALIDATOR_PATH`: **`RECOVERED_OWNER_BRANCH / ORIGINAL_SOURCE_PINNED`**; the earlier `SOURCE_REF_UNRESOLVED` main-path finding is superseded by this exact original branch recovery.
- R062 original Driver acceptance remains `ACCEPTED/FROZEN` in its own historical positive-sector model. This does not reclassify its positive-sector objects as native signed X6.
- `LP019_NBRC_SIGNED_CANCELLATION_WRONG_CALLER` and `LP011_NATIVE_ARGMAX_WRONG_CALLER` remain **`UNRESOLVED_PROVENANCE`**; the recovered checker distinguishes nonnegative positive-path multiplicity from signed coefficient cancellation and does not establish either alleged bad native caller. Other 28-LP consumer closure and Driver `REQUEST_REVISION` remain.

**Do not repeat:** already certified original current signed-X6 S6 regressions (115,513 assertions), G25/G3, R061 fixed-sector 72, historical accepted R062 Stage0 replay, and previously classified CWM weighted callers.

**Next precise task step:** use the now recovered **exact 730-line original checker and original result artifacts** as a source-linked reference when tracing an actual frozen/current higher-level R061/R062 consumer; identify concrete call sites that import old three-positive native path identity, N-BRC multiplicity or signed cancellation into the current signed-X6 domain. Record immutable file/line/input/operator and patch only a verified live type violation. For historical wrong-caller attribution, report the bounded residue when no concrete source exists, without inventing blame.

**Research lineage, not a fresh claim:** `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, old `RUN-756de85b94c23b46b181f7b8` generation 5/revision 4; historical claim `MCP-bdd4acf9d96a8f1f0dfab4e9`. New exact own continuation read request `onhour-20261114-0211-own-continuation-read-v1` was `QUEUED/WAIT_ORIGINAL` at last observation; next step for that request is original-ID receipt, not replay or unauthorized CLAIM.

**Status:** `HISTORICAL ORIGINAL VALIDATOR RECOVERED / ORIGINAL BRANCH RESULTS MATCHED / DIRECT INTEGER THREE-TOTAL CERTIFICATE PASS / AUTHOR-VERIFIED / NOT_NEW_NATIVE_BENCHMARK / NOT_NEWLY_REVIEWED`.

No scheduler, maintenance conversation, Source CLAIM, P000, Result or Review mutation.
