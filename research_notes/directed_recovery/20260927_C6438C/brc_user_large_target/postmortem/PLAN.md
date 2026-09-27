# Post-hoc diagnosis of the confirmed block test

Status: CODE_ONLY / NOT_EXECUTED / NOT_ADMITTED. This is a new, independently billed diagnostic after the blind block trial. It is not another factoring proposal.

Source: `postmortem_native.py`, SHA-256 `656d26f613f14c61542f0a1d2bc8ef3a50d491c1c006ae1fc1493976cb2d3202`. Only source writing and compile validation are performed by the author. The coordinator will decide the actual single execution after source review, completion of the confirmed blind block test, and the actual current activity guard. Existing research authorization suffices; no original driver or specific conversation is required.

## Execution gate and isolated inputs

The user confirmed the product p*q as the formal target. Only `../runs/block` must have a durable COMPLETE result. The interrupted full-decimal attempt is preserved separately and is not resumed, projected or required to complete. `USER_TARGET_CONFIRMATION.md` binds that change of scope without rewriting the frozen blind PLAN or source.

Before reading disclosed labels, the diagnostic validates the block SUMMARY/STARTED match, frozen runner source, full evidence and index hashes, contiguous index extents/counts, and final complete-result record against SUMMARY. It requires the recorded regular k=3 main-clock result. This is an integrity and applicability gate, not a substitute for the separate complete saved-digit review of the blind run.

Only after that gate does it open the pinned `input_integrity_v2/INPUT_RESULTS.json.gz` and extract the supplied p and q. Its decoded SHA is `a5ec56bfd6423118fa822eeed923d384e38e52e873bb40ac9e34e688702f99a1`; its scientific source is `041032580718b64d2c9645015d04839062d4dca4e7001b1e6387bbe7d7b03e28`. The previously reviewed typed multiplication record binds those labels and their product to the completed block N. No new product multiplication or primality test is performed. The labels are explicitly disclosed inputs of this diagnosis; they were not arguments or proposal-selection inputs of the blind run.

## Fixed diagnostic operations

1. Construct p-1, p+1, q-1 and q+1 through actual typed compare/difference and add operations.
2. Compute the four cross gcds `gcd(p±1,q±1)` by recorded typed Euclidean divisions. There is no host gcd or remainder. Record the powers of two and odd parts of these four gcds and four order-size candidates using explicit parity/shift wiring, with every shift retained and separately counted. These are label decompositions, not newly inferred multiplicative orders.
3. Evaluate the actual Jacobi symbols J(5,p) and J(5,q) with the frozen streamed Jacobi recurrence. The labels exceed five, so its nonnegative principal-numerator contract applies. Calling these Legendre symbols, or treating p±1/q±1 as torus group orders, remains conditional on primality, which this unit does not prove.
4. Take the completed block's recorded V_E, V_(E+1), identity tau/w and antipodal tau/w. Reduce all six recorded quantities separately modulo p and q using twelve actual typed divisions. Classify each signed local return solely from the two corresponding observed zero residues. No local matrix power, adjacent power, exponent search or expected factor is supplied. The original clock E and original global characters are copied as bound historical observations, not recomputed or changed.

The selected cross-gcd label is chosen from the two observed local characters only as a post-hoc theorem interpretation. For distinct odd prime p,q, Delta=5 and E=N-J(5,N), the existing public-clock theorem gives `gcd(E,p-sigma_p)=gcd(E,q-sigma_q)=gcd(p-sigma_p,q-sigma_q)`. The diagnostic measures the right-hand candidates and local returns; it does not use this equality as a free arithmetic answer, certify primality, or claim that a small gcd prohibits every other native algorithm. A small odd part identifies a restriction of this fixed public clock, not an impossibility result for BRC or Shor.

## Native implementation and evidence

The source imports the frozen `streaming_public_clock.py` (`e4cde846c1d5c0238b881e05f3128c184fb599366f7da1f3e55161c8fbf5b86b`) only as a verified stdlib-only module. After exclusive STARTED it loads the actual lazy arithmetic and admits the full native catalog. It reuses the unchanged streaming retention, arithmetic methods and Jacobi recurrence. This does not call the blind runner's `run` or `compute` functions.

The existing member transport retains its original `BRC_STREAMED_PUBLIC_CLOCK_V1` schema. Post-hoc binding and terminal records additionally identify `BRC_POSTHOC_PUBLIC_CLOCK_DIAGNOSTIC_V1`, and the independent outer SUMMARY uses that diagnostic schema. These records are not presented as another blind public-clock execution. Per-stream IDs are unique by name across the diagnostic and the two local-character contexts.

The diagnostic output is exclusively `postmortem/run/`. Existing STARTED, success, failure, evidence or index files reject another attempt. Every returned primitive is serialized and fsynced before its ID returns. Full native admission/final call lists, modular projection links, Euclidean links, label-shift receipts, all costs and the completed historical input pins are saved. Source, plan, helper, guard, target confirmation, input-integrity evidence and blind artifacts are rechecked at completion.

Failure preserves completed members, available pending returned trace, stage/state and costs as FAILED_NOT_RESUMABLE. As in the frozen arithmetic, a failure inside a primitive before it returns can lack the primitive's internal cells. Process death or filesystem failure can also prevent a terminal failure receipt; no stronger guarantee or invented receipt is claimed.

The full diagnostic cost is separate from both blind production and the earlier input-integrity bill. It reports all arithmetic streams, typed operations, digit replays, native calls, arithmetic bit wiring and bit-length calls, plus explicit two-part and Jacobi label wiring. Administrative hashing, JSON/gzip, file I/O and control are outside digit costs and can be reported separately. No timing or factor-discovery advantage is predicted.

## Invocation and continuation

After the sole confirmed block run completes and this new source is reviewed, the coordinator supplies the current guard and real pins:

```powershell
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -X utf8 'D:/em/TEMP/sep27-brc-user-large-target/postmortem/postmortem_native.py' --plan-sha256 ACTUAL_PLAN_SHA --guard-file ACTUAL_GUARD_PATH --guard-record-sha256 ACTUAL_RECORD_SHA --global-knowledge-sha ACTUAL_KNOWLEDGE_SHA
```

Any authorized conversation can read the resulting record and pursue the symbolic clock/odd-part question. Unavailable execution tools do not prevent mathematical analysis. Any new actual arithmetic must preserve its native provenance and receive its own accounting; disclosed labels must never be retroactively attributed to the blind test or used to tune its fixed k/E after the fact.

Global-Knowledge-Sync: main@b304760 / GLOBAL_KNOWLEDGE_V1, author's actual read context. The executed binding will additionally record the coordinator's actual current knowledge read and guard.
