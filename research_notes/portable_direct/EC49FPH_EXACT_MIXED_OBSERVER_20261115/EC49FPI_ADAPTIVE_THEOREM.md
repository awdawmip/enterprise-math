# EC49FPI — Optimal adaptive depth three for native BRC mixed sensing

Date: 2026-11-15. **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. This extends EC49FPH on the same unmodified original frozen input; no new formal claim is asserted.

## Domain and exact observation semantics

Keep original BRC scientific commit `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, master SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, and original integer rooted-cost CSV SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. The complete legal-root-domain of original configuration 16943 contains 310 configurations and exactly 141 distinct rooted profiles. The 228 allowed scalar queries are precisely the 144 legal full-allocation terminal cost integers `T(q)` and 84 original named-root/subset cost integers `P(r,S)`, retaining demand, branch and named-root semantics.

A deterministic **adaptive** decision tree chooses each next query based only on the integer values actually returned by earlier queries; its depth is the worst number of scalar observations needed to identify the rooted profile.

## Exact theorem

The minimum adaptive worst-case depth among **all** decision trees over this entire 228-query menu equals

`d_adaptive(16943; terminal + named-root exact scalar queries) = 3`.

In the same domain, EC49FPH proves the minimum *fixed nonadaptive* scalar query count is 4. Thus the exact adaptivity saving is **one primitive scalar query in the worst case**.

### Exhaustive lower bound (depth two is impossible)

For each of the 228 possible first queries Q, partition all 141 rooted profiles into exact integer response fibers `Q^{-1}(v)`. For **each** first Q, the verifier identifies at least one fiber containing two or more rooted states such that **none** of the 228 allowed possible second queries is injective on that fiber. Therefore no choice of first query and response-dependent second query identifies all 141 profiles. Exhaustive count: **228** first queries ruled out, with genuine offending response fiber for each. This is stronger than the EC49FPH fixed-query triple lower bound in a different direction: here the adaptive two-query decision trees themselves are excluded.

### Constructive three-level upper bound

Choose `T(0)` as the first exact complete-allocation observation. Its 141 rooted profiles yield exactly **26 distinct integer response fibers**. For each fiber, the deterministic verifier searches the allowed 228 scalar queries for a second query whose result branches each have either one remaining state or some third allowed query that is injective on that branch. It constructs the explicit response-indexed decision tree and verifies its leaf path for each of all **141** rooted profiles. All 141 decision paths are distinct; no path needs more than three scalar observations. The full decision tree is emitted as JSON, including every first/second/third exact integer response and selected query, by `VERIFY_EC49FPI.py`. The initial query has index zero under the same frozen allocation order as EC49FPH.

The search uses exact Python integer masks for state sets, exact integer response equality, and complete finite branching. Its cached depth-one and depth-two checks prune repeated fibers but do not skip any possible primitive query. Local rerun passed `EC49FPI_ADAPTIVE_EXACT_FINITE_PROOF_PASS` after executing the EC49FPH frozen-input, source-hash, 228-query fixed-minimum verifier; the EC49FPG original byte-Trie verifier was also rerun successfully this turn.

## Reproduction and related evidence

`VERIFY_EC49FPI.py` executes in the same directory as `VERIFY_EC49FPH.py`:

```bash
python VERIFY_EC49FPI.py /path/to/EC49FPG_EVIDENCE > EC49FPI_FULL_VERIFICATION.log
```

The original `EC49FPG_EVIDENCE` directory supplies `frozen_original_master.txt`, `EC49FPG_PROFILE.csv` and the original Trie implementation/verifier (companion archive of [EC49FPG PR #2472](https://github.com/awdawmip/enterprise-math/pull/2472)). Both source hashes are checked before building the 141 states. `VERIFY_EC49FPH.py` is included in this same PR and supplies the predecessor source-bound exact cost and fixed observer theorem.

**Proof strength and next question:** finite exact optimum for this original class and allowed scalar queries. Investigate optimal *expected* adaptive cost under explicitly specified priors or query costs, plus whether root probe choice changes the expected profile-separation efficiency. Extend native residual-gauge restoration to subset-dependent cross-root contrast classes, preserving the full named-root observer.
