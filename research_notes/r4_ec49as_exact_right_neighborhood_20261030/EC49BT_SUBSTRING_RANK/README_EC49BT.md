# EC49BT | Signed-X6 BRC substring-filter rank (author-side evidence)

Date: 2026-10-31 +08:00. Parent: EC49BS, same existing draft PR #1730. Status: `AUTHOR_FINITE_THEOREM / EXACT_NATIVE_BRC_CHECK_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED`.

## Scientific result

On all 19,920 native ordered length-six zero-displacement signed-X6 paths, use positive rational signed weights `wp=(2,3,3,2,1,1)`, `wm=(1,1,1,1,1,1)`, two weight channels `H={id,(E1 E2)}` with **fixed** instrument, signed ordered prefix and suffix of length one, and substring predicates `A=(+E1,+E2)` and `B=(+E2,+E1)`. For every nonnegative rational path ensemble, the least rational-linear additive state dimensions are exactly **288** for only end filters, **444** for separate `A,B` filters, **458** for all conjunctions (including `AB`), and **459** when a global unweighted ensemble count is also observed. Boolean-atom ranks are `(00,10,01,11)=(288,78,78,14)`. Complete finite proof is in `PROOF_EC49BT.md` inside the archive. A four-word exact counterexample shows separate filters and count do not determine composition.

## Source and verification

The checker runs `signed_brc.endpoint_weight` and `endpoint_multiplicity` from the **unchanged** native source at `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`, Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. Two full exact Fraction executions yielded byte-identical 84,888-byte JSON; a second portable exact script independently returned the same dimension totals twice; modular elimination at two primes also matched. Proof is finite under stated observation language; no independent Driver review, formal Result/CLAIM or physical heartbeat dynamics is asserted.

Frozen scientific inputs: `GLOBAL_KNOWLEDGE_V1 main@428c27742773a02959ae49ca87317426630f2c84` and `enterprise-math main@673a838d7baa33e7427e98aa5b06381a2ada81d4`. Verified predecessor author branch `0c109e892f61ce33b113d5de10cc6f6964b2559c`; this artifact does not overwrite protected P000/worldview. Native service 0.6.11 reported `research_authority_granted=false`; owner inventory returned `CONTROL_QUOTA` (5/5). Existing claim ownership is untouched.

## Full reproducibility package

Concatenate the four files `EC49BT_full_exact_sources.tar.xz.b64.part01` through `.part04` **without extra whitespace** (base64 ignores the one terminal newline in each part), decode base64 then extract xz tar:

```sh
cat EC49BT_full_exact_sources.tar.xz.b64.part0{1,2,3,4} | base64 -d | tar -xJf -
python VERIFY_EC49BT.py
python VERIFY_EC49BT_PORTABLE.py
python INDEPENDENT_EC49BT_MODULAR.py
```

Archive SHA256 **`cb91867a914c4f05e6480e991c4c5de28196dfec36f49ac6b95dbf68cc68c760`**, decoded archive bytes **14292**. Contains full PROOF, original actually executed VERIFY, alternate verifier, independent modular rank check, complete per-fibre `EXACT_REPORT_EC49BT.json`, portable output, SOURCES/HANDOFF, MANIFEST and the full next task. The source script imports original native kernel and verifies its Git blob; run in repo or provide the kernel at that exact path. Python 3 standard library; no external SymPy required by the published checkers.

Next EC49BU: product automaton/reachability method for general finite group H and Boolean substring selectors, avoiding raw 12^n enumeration, and independently reproduce n=6 rank before examining n=8 (1,281,420 return paths). The standalone next-task text is also included in the archive. See original documentation and full proofs for exact scope.
