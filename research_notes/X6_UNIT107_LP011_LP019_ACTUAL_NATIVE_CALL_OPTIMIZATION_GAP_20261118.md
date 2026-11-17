# X6 Unit107 — LP011 / LP019 real native call-site validation gap under Python optimization

**2026-11-18 · TASK_RESEARCH · RS-X6-LEGACY-PLANE-RECONCILIATION · TP2-B4A441B23DA3159232C2**

**Status:** AUTHOR-SOURCE-AUDITED / EXACT-PYTHON-CONTROL-FLOW-EXECUTED / UNREVIEWED / NOT_ADMITTED. This is an independently reproduced executable *test-validity defect* in two **current** callers, not a demonstrated historical wrong-native-argmax or natural-N-BRC-sign-cancellation bug. No formal Result/review/admission, no original R063/Helly replay.

## 1. Frozen premise and bounded source audit

Research scientific pins remain unchanged: P000 V5 `59538f585d037d09ef687b28715c4bc1a3f9fe03`; pre-rebase `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Mother question remains restoring correct native signed Cell, carrier/observer, and natural BRC path provenance.

I read the full current GitHub source bytes of all **27** distinct Python entries in `research_checks/` whose leaf filename begins `X6_LP011` or `X6_LP019` (as of canonical main `fe4c92fbd0b5bcb498363e4b3270df8d58a3eda1` before this publication). The inspected group covers **11 LP011-prefixed / LP011+LP019 cross entries** and **16 LP019-prefixed entries**. The historical complete pre-rebase corpus and all current downstream consumers are not exhausted by this group; the allegation of a historical wrong caller remains `UNRESOLVED_PROVENANCE`.

Actual relevant current Source files and Git blob SHA1s:

* `research_checks/X6_LP011_TYPED_DOMINANT_CONSUMER_20261112.py`, **cf2c11d47a4abf5a462c4c96540a125f0f942a8d**. Lines **83–86** conditionally import real `signed_brc.py`; lines **103–105** perform the imported native assertion and count reported calls.
* `research_checks/X6_LP019_SIGNED_THICKNESS_AND_BRC_FIBERS_20261112_ONHOUR.py`, **24664a814c83b471febaabb4a1c0b0ae0c59d571**. Lines **98–105** import original real signed BRC module and assert its Git blob pin; lines **110–117** perform the native endpoint assertions and increment the reported comparison count, and lines **128–131** assert original module return counts.
* In `X6_LP011_LP019_CHART_EVENT_CONTEXT_NONFACTOR_20261114.py` (**f04316c612a0595def4aaed8aac29543a7ae90ea**), distinct current consumer uses an original-source hash guard and dynamically imports two chart/event programs. It was **not** made the target of this specific counterexample.
* The other selected 24 scripts contain separately scoped signed/observer/BRC formulas, explicit source pointers or finite checks; their presence is not evidence of an offending historical LP011/LP019 native caller.

## 2. Exact executable failure of evaluation, rather than a failure of X6 arithmetic

Python removes every `assert` statement when compiling with `optimize=1` (`-O`) or `optimize=2` (`-OO`). In both current callers above, the *native function call itself* is inside the assertion expression, while the associated counter increment is outside the assertion. Thus the optimized program can report that original module calls were checked even though none were invoked. This is a concrete test-instrumentation problem; it has no bearing on the valid formal multinomial BRC identity under signed native coordinates.

LP011 has a selected raw signed `[-7,7]^3` cube with `15^3=3375` iterations. LP019 builds native length-0..6 endpoint supports of sizes `(1,12,73,304,985,2668,6321)`; their exact sum is **10,364**.

A fresh, standalone Python checker reproduced the **same exact assert/counter Python control-flow pattern**, compiled at optimization levels 0, 1, 2; it counted actual stub native function invocations independently of each displayed report. This executable uses no replacement native BRC theorem and does not run the project production modules.

| Reported source comparison count | Python normal `actual_calls` | Python `-O` actual | Python `-OO` actual |
| --- | ---: | ---: | ---: |
| LP011: reported **3375** in every mode | 3375 | **0** | **0** |
| LP019: reported **10364** in every mode | 10364 | **0** | **0** |

The independent checker itself was run using Python normal, `-O`, and `-OO`, yielding byte-identical JSON, SHA256 **7156af21d8e9327c2636ddf989de5e5b2ac8b832783e485cdddb2b1b1aad68**. Its exact generated payload digest is `0d924cbe639be386ca9cf2def9f86159cb631e2f1b4e018ec00f005fb7c9ed05`.

**Executed witness program:** `research_checks/X6_UNIT107_LP011_LP019_OPTIMIZED_ASSERT_CALL_ELISION_CHECK_20261118.py`, commit `3cb9d245e3916f91154f732eb859afda1d0c3de7` blob `b6e1771285d0bf609f2caba69f52c383a3d80dae`. **Machine JSON:** `research_checks/X6_UNIT107_LP011_LP019_OPTIMIZED_ASSERT_CALL_ELISION_RESULTS_20261118.json`, commit `fd693fb46fe4aaa793b55cac9d4a4ce994cba500` blob `5a08405366e23f111821dafa57060c93803acbee`. Both original source bytes and new evidence were remotely read back.

## 3. Minimal correction boundary and acceptance criterion

A narrow versioned adjustment to the two current checker consumers must:

1. Evaluate the actual imported native call **outside** `assert`, compare the resulting value with an always-on `if ...: raise AssertionError`, then increment the comparison counter only after the actual value is checked.
2. Make the LP019 **original Git blob pin comparison** an explicit always-on check rather than an `assert`; no pin replacement and no changes to original frozen source/benchmark.
3. LP011's optional Source import branch must retain `existing_native_brc_imported` and `existing_native_brc_calls` as separate facts; a portable no-import pass must not masquerade as a native comparison pass.
4. With original Source available, run both corrected programs under Python normal, `-O`, `-OO`; require **actual** native-call counts equal 3375 and 10364 respectively (under the specified current inputs) in all modes, equal data values, and restored blob guard enforcement. Missing source/pin failure is a failure for that affected original-source regression, not a pass.

Current status: a verified reproduction of the **pre-fix counterexample**; versioned source correction and full original-module integration/regression **NOT YET EXECUTED**. This is not the original native benchmark identified by R063 support Issue #2416; the issue remains open, original object and acceptance unchanged.

## 4. Original Source native request and task continuation

The original same-lane `onhour-20261118-0402-x6-own-unit104-native-progress-v1` has now been remotely reconciled as **SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED**, with Source `b935d61e55dcaca2db42688c8c40099e17221e73`; previous `QUEUED` / resource-wait report is obsolete. This fact does **not** assert that Unit105–107 have native semantic PROGRESS; those units remain GitHub author evidence pending a new same-run authenticated operation.

Own historical research identity is `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-3e221a50dc8818f914e228f6`, RUN `RUN-95866d78d35721116c362956`; current saved generation 2/revision 2 is a historical projection, not an unconditional live writer license. Do not borrow maintenance or owner-custody roles.

**Next exact action:** implement and test the *two specific versioned consumer checks* on original Source with always-on comparisons, then resume actual 28-LP downstream type/source:line ledger. Separately reconcile live X6 claim/generation under current Source before any Native progress and link Units105–107 only with winning current authorization. Preserve Unit106's proved one-step Johnson/BRC nonfactor, R063/Helly frozen original, and Driver `REQUEST_REVISION` without redoing them.