# EC49FGQ — Exact radius-two seven-key obstruction around two 94-prefix BRC witnesses

Date: **2026-11-10**. Status: **AUTHOR_EXACT_FINITE_CERTIFICATE / TWO_IMPLEMENTATIONS_PASS / NOT_DRIVER_REVIEWED / NOT_ADMITTED**.

Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; frozen BRC nine-state automaton and six ordered signed-X6 expansions: Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`. Parent 24-demand, seven-complete-raw-key, 94-prefix witnesses A/B: [EC49FGJ witness, blob e65c1598](https://github.com/awdawmip/enterprise-math/blob/2e4d05d4270f646336dcdfa0470ec93dbd4f036e/research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FGJ_SEVEN_KEY_94_20261110/WITNESSES_EC49FGJ.json).

## Exact finite theorem

Fix either witness W=A or B. Replace **at most two of its 24 labelled complete BRC operation words**, maintaining the same window, required nine-state observation signature, native signed-X6 endpoint (2,0,0,0,0,0), and **at most seven distinct complete raw cache keys across all 24 words**. Leave every other word unchanged. Then the union of nonempty **ordered signed-X6 microstep prefixes** always has at least **94** elements. Equality holds for W itself. Thus no ≤93 seven-key construction is within Hamming distance two of A or B. The unrestricted seven-key question C_min(7) =? 94 remains open.

## Exhaustive proof

For each of the 276 pairs {i,j} of the 24 demand labels let F be the union of prefixes from the other 22 fixed words. Any replacement words u,v with total cost ≤93 must satisfy

`|(P(u) \ F) ∪ (P(v) \ F)| ≤ B := 93 - |F|`.

Each witness has **153** pairs with B<0, excluded immediately. The other **123** pairs retain all seven original raw keys among the 22 fixed words except **12** cases in which a single H2 word is removed. Direct complete 6²-word enumeration finds that H2-signature16 has the sole realization `fe`, and H2-signature32 the sole realization `ge`; the removed H2 word therefore must be restored, replacing its missing raw key and leaving no free key. Hence every surviving ≤7-key pair uses only the original seven keys.

For key (x,y,z) and window h, the frozen native displacement/count equations give

`#e=z, #a=z-1, #c+#d=x+y-h-1, #f=h+1-y-2z, #g=h+1-x`.

Enumerating every nonnegative c/d split, every word ordering accepted by the literal nine-state DFA, and all six-axis endpoints produces exactly **9,838** legal (label, word) candidates per witness. The programs compute each exact ordered signed-microstep prefix set. They discard any u or v individually adding more than B prefixes, deduplicate the remaining difference sets, and compare the complete Cartesian product. The exact counts are:

| Quantity | Witness A | Witness B |
| --- | ---: | ---: |
| Unordered label pairs | 276 | 276 |
| Excluded solely by fixed prefix cost | 153 | 153 |
| Screened pairs | 123 | 123 |
| Forced-H2 key restoration among screened pairs | 12 | 12 |
| Legal words on original seven-key alphabet | 9,838 | 9,838 |
| Distinct difference-set pair comparisons | 2,275 | 2,263 |
| ≤93 completions | **0** | **0** |

A second, separately written program re-enumerates full alphabet words by DFA recursion rather than by operation-count vectors, represents prefixes as tuples of signed axis integers rather than bitmasks, and obtains exactly the same numbers. All arithmetic is exact. This is an exhaustive *local* theorem within the stated 24-path radius-two neighborhood.

## Exact files and reproducibility

The GitHub evidence bundle `EC49FGQ_EVIDENCE_20261110.tar.xz.b64` contains the complete executed standard-library bitmask verifier, the baseline A/B witness source data, and the independent crosscheck's exact summary JSON. Running the bitmask verifier regenerates the full 552-pair JSON report. The separately retained complete local evidence archive additionally contains the independent verifier source, full precomputed report, README and SHA256 checksums. To reproduce the principal GitHub-hosted proof:

```bash
base64 -d EC49FGQ_EVIDENCE_20261110.tar.xz.b64 | tar -xJf -
cd remote_min
python EC49FGQ_TWO_SWAP_EXACT.py
```

Next useful action: search exact radius-three neighborhoods, particularly simultaneous H6/H7/H8 changes, pruning with the same fixed-background and per-path difference constraints. A ≤93 certificate would sharpen the upper bound; a complete absence proves the corresponding local obstruction.

Authorship is independent author-side research (PR #1730); the historical EC49AS task has no verified live CLAIM. Theorem admission requires independent Driver review. P000 and protected worldviews unchanged.
