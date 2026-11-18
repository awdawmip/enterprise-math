# EC49FAC — Strict-76 search after four explicit native-X6/BRC witnesses

**2026-11-04 / Task continuation from EC49FAB.**

## Mother question and frozen input

Find the global minimum distinct nonempty **ordered signed primitive** prefix edges E for horizons h=2..8, five full six-axis positive-step BRC cache keys, <=6 distinct nine-history transfer signatures, and rank-nine observation matrices at each h. Preserve seven native operation symbols, six signed displacement axes, path/sign/order/provenance and exact observer semantics. Frozen science input pins: EM `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; account science `773d538180bfb49e24cffeb35c3ee75eb0628e2e`. Current behavior rules are separate from those pins. P000 and ACTIVE worldview remain unchanged.

## Highest verified author-side frontier

- Previous EC49EXZ: two fully verified exact 78-edge witnesses, so E*<=78.
- EC49FAB: **four fully verified E=76 constructions** among 1,506 newly tested distinct EXY candidate arrangements at source ranks 1512, 1513, 2200, 2203. Each independent signed-X6 expansion and full nine-history rank audit PASS. Exact OR-mask DP fixed-arrangement optimum 76. Global author-side interval **63<=E*<=76**. No formal Driver review or Source-native Result.
- New tested census: 1,492 exact negative cutoff-78 receipts, 4 exact 76 witnesses, 10 timeouts, all disjoint from earlier first 200 and EC49FAA ten. Remaining **6,402** double-collision arrangements not yet excluded for E<76: starting with 12,356 EXY rows, deduct 4,282 prior strict-78 lower bound, 166 EXZ precise first-200 decisions including two 78 optima, 10 EC49FAA negative certificates, 1,492 FAB negative certificates and 4 proven fixed-E=76 schedules. Earlier 7,900 count omitted the two EXZ 78 optima; true pre-FAB strict-78 unresolved count was 7,898.
- Complete reproducible evidence: sibling `README_EC49FAB.md`, `VERIFY_EC49FAB_STANDALONE.py`, `EC49FAB_EXPLICIT_76_WITNESSES.json`, `EC49FAB_CENSUS_REPORT.json`; full **109KB gzip tar** split in five `EC49FAB_COMPLETE_EVIDENCE.tar.gz.b64.part01..05.txt` segments, reconstructed by concatenating five text files in order, base64-decoding and then `tar xzf`. Expected full tar SHA256 `92805107e7e9de6bf91816bf915a55b6d73ed3481fabc598290e511863615c40`.

## Independent executable next question

At **strict cutoff E<76**, recompute the existing proved per-arrangement B_EXY and other signed-prefix lower bounds against the *new threshold*. Explicitly count every exclusion in the original immutable 12,356-row EXY candidate list. Remove known completed schedules by original zero-based source rank and no false double-counting. For schedules whose necessary lower bound is below 76, execute actual unchanged signed native path trie / integer OR-mask DP, prioritizing smaller candidate word counts and same exact-input hash deduplication. Start by resolving the ten FAB TIMEOUT source ranks [272,273,387,517,914,915,950,951,1002,1003] if a stronger lower bound or resource-bounded exact alternative is available.

An **E<=75 witness** must include explicit operation words for all seven horizons, each full six-coordinate BRC key, all nine-history signatures, exact rational rank-nine check per horizon, signed primitive prefix-edge union cost, and independent replay. A negative must carry original schedule ID, exact input SHA256, solver cutoff, actual outcome and finite-enumeration coverage; TIMEOUT is pending. A single new verified E<=75 witness improves the mother upper bound. Otherwise, a strictly new count of sound exclusions shrinks the unresolved domain.

## Delivery / authority

Continue existing Draft PR #1730 on branch `research/r4-ec49as-20261030-exact-right-neighborhood` with non-force guarded writes and remote readback. Native CLAIM/Result/review require actual Source authenticated authority and confirmed live owner; GitHub storage is author-side draft only. Do not alter P000 or task frozen scientific inputs. Preserve complete proof, code, evidence and next unresolved question.
