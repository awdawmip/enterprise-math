# EC49FKO — complete six-key cover census and exact signed-X6 native-prefix depth sieve

Date: 2026-11-11. Author-side exact finite certificate, independently checked in nine disjoint verification batches; independent Driver admission pending.

**Frozen scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The original nine-state BRC legal-word generator, exact complete raw cache keys, 24 labeled observation requirements, and literal signed ordered six-axis native microstep paths are unchanged. The preceding exact five-key covering theorem and 99-prefix lower bound are EC49FKM/EC49FKN on PR #1730.

## New exact finite theorem

Across **all** six-element subsets of the 94 complete raw keys, **exactly 2,004** distinct sets cover every one of the 24 BRC observation labels. Of those, **1,376** contain at least one of the previously classified 16 complete five-key cover sets, while **628** are inclusion-minimal six-key covers. Exactly 1,328 have one five-key covering subset, 48 have two, and 628 have zero.

For each one of the 2,004 six-key covering sets, calculate the exact *per-depth forced-label prefix lower bound* defined below from all 178,850 lawful native BRC words. The result partitions the complete six-key covering class as follows:

| Six-key set class | Bound >=94: excludes every <=93-prefix realization | Bound <=93: unresolved by this sieve | Total |
| --- | ---: | ---: | ---: |
| Contains a complete five-key cover | 823 | 553 | 1,376 |
| Inclusion-minimal six-key cover | 440 | 188 | 628 |
| **Total** | **1,263** | **741** | **2,004** |

Thus, **any** solution of all 24 demands using at most six complete raw keys and at most 93 nonempty native signed ordered prefixes must use a set of six keys from the **741 explicitly reproducible survivor sets**. The earlier EC49FKN result excludes all five-key solutions with <=93 prefixes, and EC49FKM excludes four or fewer keys by exact label incidence. The mother question for seven keys remains `C_min(7) ?= 94`.

The smallest computed six-key *depthwise lower bound* is **67**. This is a necessary lower bound, not an attained six-key solution cost. No 93-prefix new witness is asserted.

## Exhaustiveness proof for 2,004 covering six-sets

The five required labels `(2,16),(2,32),(3,16),(4,1),(7,1)` have pairwise disjoint families of capable full keys with cardinalities `1,1,2,7,34`. Therefore every six-key cover must contain a five-key tuple with exactly one key from each family, together with one extra key. Enumerating the `1*1*2*7*34=476` tuples and each of the 89 additional keys generates 42,364 candidates **with multiplicity**. Canonical full-key-set deduplication and exact 24-bit observation-mask coverage leave precisely 2,004 unique complete covers. The 16 five-key covering sets are exactly `K0+{u,v}` with:

```text
K0={(2,1,1),(3,0,1),(3,1,1)}
U={(3,3,1),(4,2,1),(5,1,1),(5,1,2)}
V={(5,5,1),(6,4,1),(7,3,1),(7,3,2)}
```

A six-key cover is inclusion-minimal precisely when it contains none of these 16 complete five-key subcovers.

## Per-depth exact inequality

Fix an admissible six-key set K. For each required label i, let L_i(K) be the least **signed native microstep length** among its legal K-words. At depth d define `A_d(K)={i:L_i(K)>=d}` and let `N_d=|A_d|`. For each literal ordered signed microstep prefix p of depth d, let `S_d(p,K)` be the labels in A_d with at least one legal K-word having prefix p at that depth, and set `M_d=max_p |S_d(p,K)|`.

Every chosen legal realization of each forced label i contributes a prefix at depth d. A single literal prefix covers at most M_d such labels, so the number of distinct depth-d prefixes is at least `ceil(N_d/M_d)`. Different depths contain disjoint prefix objects, hence

```text
|union_i P(w_i)| >= sum_{d=1}^{max_i L_i(K)} ceil(N_d(K)/M_d(K)).
```

All 2,004 lower bounds were calculated from complete legal K-word families, without truncation, unsigned-endpoint identification or cache-key compression. A bound >=94 rigorously excludes a 93-prefix completion for that exact K. Bounds <=93 leave the next exact joint-prefix optimization.

## Actually executed verification and reproducibility

`VERIFY_EC49FKO_PORTABLE.py` independently regenerates the complete six-cover census and the full 2,004-by-depth certificate from the original frozen BRC generator. It executed and returned:

```text
EC49FKO_ALL_SIX_KEY_EXACT_PASS 2004 excluded 1263 survivors 741 lower_min 67
```

A separately written literal-**tuple** native-microstep checker parsed the frozen `FJR_CATALOG.tsv` (178,850 rows), independently checked DFA endpoints, raw signed-X6 displacement and key identity, enumerated the same 2,004 covers, then matched the exact per-set lower bounds. Its range-disjoint batches `[0,500),[500,1000),[1000,1100),[1100,1200),[1200,1300),[1300,1400),[1400,1500),[1500,1600),[1600,2004)` together covered **all 2,004** and reproduced the four class totals (823,553,440,188). The check differs from the published verifier in input parsing and native-prefix encoding, uses no endpoint quotient, and verifies exact per-keyset values.

The complete original author-side report (4 MB), the ordered 2,004-keyset table, separate checker, actual batch logs and SHA256 manifest are preserved in the conversation delivery archive `EC49FKO_six_key_2004_exact_evidence_20261111.tar.xz`, SHA256 `4c97d588734e724c115b7deaee0b6261f582ffc716a1b9be7d64ee2c7b38a85f`. The published verifier deterministically regenerates the same 2,004 exact depth certificates; use `EC49FKM_INPUT_DIR` to point at the previously published frozen `EC49FGW_RADIUS5_SCREEN.py` source directory, and `EC49FKO_OUT` for the report path.

Author-side mathematical status: `EXACT_FINITE_COMPUTATION_PASS / INDEPENDENT_AUTHOR-CODE_AUDIT_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`. A Source-native session/CLAIM/Result was not established in this run because the private research gateway returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE`, `operation_sent=false`. GitHub author-side publication and native project admission are distinct.

**Next concrete unit:** jointly optimize signed literal prefix unions for the **741 surviving six-key sets**, beginning with stronger two-depth coupling or bounded full prefix-trie DP for the smallest forced-label bound classes; separately continue distance-8 seven-key witness perturbations and direct 93-prefix search. Preserve all original task and source pins, P000 and ACTIVE worldview.
