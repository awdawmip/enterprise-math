# EC49FGZ — Exact five-path exclusion for budgets 16–18 (2026-11-10)

**Claim (finite, original frozen BRC model).** Let A or B denote either immutable 24-demand, 7-complete-key, 94-signed-prefix witness from EC49FGJ. Select exactly five demand labels Q to replace, and keep the other 19 words unchanged. Suppose that the 19 retained words still use all seven original complete keys and that the target is at most seven keys and at most 93 distinct ordered signed native X6 microstep prefixes. If the allowed extra-prefix budget is 16, 17 or 18, there is no legal five-word completion.

Scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Input witnesses: `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` at the EC49FGJ evidence frontier, consumed by the existing EC49FGW/EC49FGX sibling verifier. Original operation alphabet, DFA and signed X6 step map are reused unchanged.

## Exact reduction and proof

For a baseline prefix e, define S(e) as the subset of the 24 baseline words containing e. For any five-label set Q, the fixed 19-word background is F(Q), with

```text
|F(Q)| = 94 - #{e : S(e) subseteq Q}.
B(Q) = 93 - |F(Q)| = #{e : S(e) subseteq Q} - 1.
```

The original complete-key support masks similarly show that no baseline key is released precisely when none of its support sets is contained in Q. Then the retained 19 words already occupy seven distinct complete keys: any admissible replacement under the seven-key cap must use one of those same seven keys. This reduces all admissible replacement paths to the **complete** frozen legal-word catalog filtered by these keys (9,838 words out of 178,850).

For each replaced demand label i and each legal candidate word w, retain the exact native microstep prefix difference D_i(w) = P(w) \\ F(Q), provided |D_i(w)| <= B. The five-way decision condition is

```text
exists w_1,...,w_5: | D_1(w_1) union ... union D_5(w_5) | <= B.
```

The verifier represents distinct signed ordered prefixes by unique bit positions; it computes exact unions by integer bitwise OR and exact size by popcount. The dynamic program starts with {empty set} and adds one candidate group at a time, dropping any union larger than B. Within one layer, if X subseteq Y, Y is discarded: for every future prefix set Z, X union Z subseteq Y union Z. This dominance is lossless. All legal five-word completions are represented by the maintained inclusion-minimal sets.

## Completed exhaustive scope

| Allowed new prefixes B | A five-label positions | B five-label positions | Completions of cost <=93 |
|---:|---:|---:|---:|
| 16 | 32 | 32 | 0 in each |
| 17 | 404 | 404 | 0 in each |
| 18 | 180 | 180 | 0 in each |
| **Total** | **616** | **616** | **0** |

The `VERIFY_EC49FGZ.py` executable was run locally on all positions in this domain using the historical EC49FGX exact antichain checker; it returned `EC49FGZ_EXACT_PASS`. A separate local implementation with candidate antichain pre-reduction independently tested the same 616 cases for each witness, returning identical outcomes. Source logs and both implementation variants are included in the local evidence bundle.

**Frontier update.** EC49FGY and EC49FGX had already eliminated the remaining no-key-release five-substitution cases with B <=15, as well as their singleton/pairwise exclusions. Of the **744** no-key-release five-position cases per witness surviving EC49FGY's earlier screens, **436** are now newly excluded (B=16 or 17). The 180 cases with B=18 had already failed the exact pairwise screen; they are independently verified here by the full five-way checker. Hence **308 no-key-release cases per witness remain** under B=19,20,21,22,23,25, with respective counts 144,116,20,20,4,4.

The **4,898 five-position cases with released original keys per witness** remain a separate task. This is a local theorem around A/B, not a global lower bound for arbitrary 7-key solutions. The pre-existing 94-prefix construction still supplies the upper bound `C_min(7) <= 94`.

## Reproduction and evidence

- `VERIFY_EC49FGZ.py`: exact all-position verifier; imports the previously published `EC49FGX_RADIUS5_PAIR_FIVE_DP_20261110/VERIFY_EC49FGX.py` and its `EC49FGW` frozen generator and EC49FGJ witness JSON.
- `EXACT_REPORT_EC49FGZ.json`: observed exact totals for both witnesses.
- Local author evidence: legacy five-way full test and independent variant (`EC49FGZ_B16.py`, `EC49FGZ_B17.py`, `EC49FGZ_B18.py`, `EC49FGZ_CROSSCHECK.py`, logs and JSON). All data are nonsensitive research materials.

## Next smallest units

Finish B=19 and B=20 by minimizing native prefix unions and adding exact conditional bounds before costly full five-way DP; then check B>=21. The separate released-key cases require joint key-selection and prefix-union enumeration. Preserve exact frozen pin, P000 semantics, author activity history and original witness scope. No formal EC49AS CLAIM or independent Driver review has been acquired for this author-only increment.

Researcher-ID: `EM-DIRECT-C37E32` (TASK_RESEARCH). Activity: `RA-5F283DFC9E477B2EBA32F0A7` (Source registered). Status: author-side exact finite audit; not mathematically admitted.
