# Independent bounded BRC runtime migration review

Verdict: **PASS_FINITE_BOUNDARIES_NO_MATERIAL_DEFECT_FOUND**.

This is an internal independent source/API migration check for the owner. It is not a formal V2 mathematical review, an all-N proof, or a promotion of the underlying shell theorem.

Packaging run workspace: `D:/em/owner-20260907`; the script does not hard-code this path.
Published historical baseline used by this replay: `5eddb6ea23761d928197b3d8227a5b42a7975a34`.
Baseline tree: `8c0a6c8d0383b3063ae97d00be069db1613c726e`.
Before packaging, independent local `git rev-parse <commit>^{tree}` calls for that published commit and the original review commit `9c8ba08cb82f0d071dfd91c0bdcf17f8220f08c6` both returned this exact tree. The public-baseline replay checks the tree pin again and reads historical source from the published commit; it does not require the local-only commit to exist.

This publication package replays exactly the existing two endpoint cases and boundary/fault injections. It adds no mathematical cases and is not a new mathematical review.
Policy read: `exact_arithmetic_runtime_policy.json` (V2) and `docs/EXACT_ARITHMETIC_BRC_RUNTIME_PROTOCOL.md`.

## Exact frozen inputs

| Relative to experiments/owner_shell_length_20260907 | SHA256 |
| --- | --- |
| shell_length.py | 31c09afd186ecc86d608fdfeb3b014091f22a3b40bcbdc32d568fe0c0db8aa18 |
| validate_brc_runtime.py | 956126dae579767e65dd9f4f80ab04947a8cc1bdbaa9e34c6e41125dea2a21ec |
| validate_brc_runtime.json | c4b454f6b84ed774d8471d685106c143ebea98d689c28cf7aba1ae9817d4fae9 |

All three hashes were checked before and after independent execution. The frozen JSON's helper, validator, original validation, original source, and dependency hash bindings agree with actual bytes. Its reported 61-case/1641-trace author run was inspected as prior evidence, not rerun or relabeled as this review's test run.

The current bytes of these dependencies equal their baseline Git blobs exactly:

- signed_brc.py: `6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4`.
- x6_signed.py: `e48b6f2133edc588fde98b1b0f02ce27fecda915b152b7901300898920d52b8e`.
- src/enterprise_math/exact_arithmetic.py: `f4f8feead82dc53a35e5fec495b31e46e64820f7b115c9efd6034063e68f8ad6`.

## Semantic review

1. `upper_length` preserves the old parity adjustment: for parity bits kp,np in {0,1}, abs(kp-np) is exactly the residue previously computed from k-N modulo 2. The new expression never sends a possibly negative k-N into the natural-number facade. The scalar API remains available; `upper_length_evaluation` and the optional ledger expose its three BRC evaluations.
2. `reduction_parameters` checks N >= base before evaluating the even excess. Existing positivity/parity/strict-inequality contracts remain present. Search bounds preserve their original floor/root meaning; x <= sqrt(floor(D/3)) and y <= sqrt(floor((D-x*x)/2)) keep all subsequent radicands nonnegative.
3. For positive odd B and v, their residues modulo 4 are 1 or 3. Equal residues select +v; unequal residues select -v, which then has B's residue. This is equivalent to the old signed difference test without performing division on negative integers. Hadamard nonnegativity is checked before any coordinate division, and divisibility/output-sum/output-square checks remain afterward.
4. At shortest length k=sum(abs(z)), the original signed endpoint formula has zero gap and only the zero extra-pair composition. Its denominator is precisely product(factorial(abs(z_i))); factorial(0)=1 handles the absent sign. The migrated path carries that same factorial numerator and denominator, evaluates the quotient through BRC once, and requires zero remainder. It does not call either legacy multiplicity routine. Norm, shortest length, signed coordinates, residual/depth, and all 20 slice reconstruction checks remain on the unchanged original signed tool paths.
5. Every governed quotient/remainder/root occurrence in the changed helper routes through its BRC wrappers. Hex is a lossless representation of large trace integers, not a precision truncation; trace field sets and exact integer/root-basin reconstruction are verified. The independent instrumentation below checks a one-to-one ordered match between facade calls and stored records for two actual complete certificates.
6. Resource semantics are unchanged in scope: search budget counts tested candidate pairs; event budget limits multiplicity materialization; decimal conversion failure preserves the verified endpoint and exact factorial ratio. These are not claims of uniform CPU/memory bounds or endpoint nonexistence. The certificate schema intentionally advances to v2, while original v1 evidence remains unchanged.

## Independent finite execution

Interpreter: Python 3.12.14, `-B`, normal assertions enabled; decimal digit limit remains 4300.

- N=60, signs (+,-,+,-,+,-): endpoint `(4,-1,3,-3,3,-4)`, signed odd triple `(-1,3,3)`, exact shortest count `51459408000`, 31 facade calls and 31 matching stored traces.
- N=61, signs (-,+,-,+,-,+): endpoint `(-4,3,-3,3,-3,3)`, signed odd triple `(1,1,1)`, exact shortest count `651819168000`, 29 facade calls and 29 matching stored traces.
- Both N values are absent from the old 61 selected cases. Only these two historical endpoint constructors were executed as an explicitly typed old-code comparison. The full old runner and legacy multiplicity functions were not executed. Counts were independently obtained by an integer-addition recurrence over the last occupied axis, without quotient/root operations.
- N=60 rejects search_budget=1 after one candidate and succeeds at search_budget=2 with exactly two candidates.
- Injected malformed positive triple `(101,1,1)` at N=61 produces `Hadamard nonnegativity failed` before any `Hadamard coordinate` division is called; no negative numerator enters the natural facade.
- Exact integer encoding at bit lengths 2048 and 2049 uses integer and hex-object representation respectively; JSON round trips exactly without changing the decimal limit.
- Five additional malformed trace signatures are rejected: wrong quotient, zero denominator, boolean integer, wrong next root basin, and missing root collapse field.
- Previously observed independent static policy gate: `EXACT_ARITHMETIC_POLICY: PASS (2 files)` for shell_length.py and validate_brc_runtime.py at the same frozen hashes. This packaging step did not rerun or broaden that gate.

Execution evidence for this public-baseline replay: `review.json`, SHA256 `9d485a64cc490ce8ee60b502279bdcc82f6dc522e92d1b2b40d30e6175eb788d`.
Final script SHA256: `013ca7d3cb7f7164a166ddad3cbd80c5b3fc18a00fe88944c37159100a98ab4c`.
Actual replay timestamp: `2026-09-07T19:00:24.589865+00:00`.
The JSON records actual interpreter, source hashes, baseline tree, case outputs, and the script hash. The final script was run once with its default root from outside the repository working directory; its existing six check groups all passed again.

Reproduction, with Python 3.12 and normal assertions enabled:

```text
python -B experiments/owner_shell_length_20260907/brc_runtime_independent_20260908/review.py
```

The optional positional argument selects another repository checkout:

```text
python -B path/to/brc_runtime_independent_20260908/review.py path/to/enterprise-math
```

Without that argument, the script derives the repository root from its source package layout. The published baseline Git object must be locally available. The script reads that exact object and writes only the adjacent `review.json`; it does not fetch or mutate Git refs. Replaying refreshes the JSON run timestamp, so its new content hash will differ from this frozen report's recorded execution hash.

Publication byte normalization: the earlier portable script and report lacked their terminal LF. The script changed by exactly one appended LF byte; its Python AST is identical. The original portable three files are preserved under `%TEMP%/owner-shell-brc-portable-before-eof-20260908-bfwed0bg`, with a normalization proof. The final normalized script was actually executed again using only the existing two cases and original boundary/fault injections; the JSON and hashes above refer to that execution. All mathematical inputs, reviewed source pins, case outputs and runtime semantics remain identical. Every final package file is UTF-8 without BOM, uses LF, ends with LF and has no trailing spaces or tabs.

Arithmetic trace checks establish exact local evaluations; they are not a certificate authenticity signature. This finite review does not establish the all-N theorem. The owner can publish the frozen migration unit with accurately updated catalog/provenance binding; this review grants no formal task/review authority.

Only review.py, review.json, and REVIEW.md were added in this dedicated publication directory. The three frozen reviewed files, catalog, source dependencies, original evidence, untracked proof, and remote refs were not modified by this reviewer. The original TEMP package remains byte-for-byte unchanged; its earlier report and run retain their original hashes and local-baseline provenance.

Global-Knowledge-Sync: main@990d7c1 / GLOBAL_KNOWLEDGE_V1
