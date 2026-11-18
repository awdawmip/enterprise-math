# EC49FDO — one-key exchange, signature/slot constraint and exact prefix probes

Date: 2026-11-07. Frozen science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Scope: the four original EC49FAJ five-key sets with fixed early H2/H3 paths `de, ed, ce, ec; feg, gef`. Source: EC49FDN exact four-family optimum and EC49FDL six-signature native signed-X6 primitives; unchanged P000.

## New exact finite screening theorem

In the six-signature model, for horizon h and full positive cache key k=(x,y,z), the operation multiplicities are
`a=z-1; e=z; c+d=x+y-h-1; f=h+1-y-2z; g=h+1-x`.
All multiplicities must be nonnegative. For each integer c/d split, the complete nine-state DFA dynamic program enumerates *reachable signature bits*, preserving the operation order internally. Rank nine is equivalent, for this frozen observer, to hitting each signature mask in `(18,20,33,40)`. The finite domain over h=4..9 has exactly **158** keys; **155** have some accepted word.

Starting from each of the four EC49FAJ five-key sets, keep (3,1,1) (the H2/H3 key), replace exactly one of the remaining four keys, and allow arbitrary mixed-key words inside each later window. There are **502 distinct rank-nine-viable exchange events per family, 2008 across four named families** (counts have family identity; duplicates across families are not deduplicated). In particular, replacing the H9-essential *last* key leaves **49** rank-nine-viable replacements in each family.

Adding the actually prescribed number of word slots at H4..H9, and requiring all **five different complete keys to occur**, narrows those 49 to **15 per family** (**60 named family/exchange events**). The slot vectors are `(4,2,2,2,4,2)` for cases 1512/1513 and `(2,4,2,2,4,2)` for cases 2200/2203. This screening is exact for DFA/rank/slot/key-occurrence *feasibility*. It does not prove prefix-cost feasibility or a <=93 optimum; those cost problems are still independent search units.

The checker is `SCREEN_EC49FDO.py`, using integer bitmask dynamic programming over signature, number of occupied slots and nonseed-key usage. It produces all 15 replacement keys per family. Since any selected (key,signature) pair is realized by at least one legal word, this is a complete finite abstract feasibility screen. All accepted original four seed keysets passed as a regression test.

## Prefix-cost exact finite probes

For case 1512, replacing only the H9-essential key (5,5,1), allow full signed-X6 ordered word languages at H4..H9 and enforce five-key usage and original window slot quotas. Exact 0-1 prefix-Trie MILP (HiGHS status OPTIMAL, integer dual matching primal) plus independent exact Fraction observer rank and native endpoint audit gives:

| Replacement new key | Candidate words | Trie edges | Exact signed prefix minimum |
|---|---:|---:|---:|
| baseline (5,5,1) | 3744 | 19962 | **94** |
| (6,4,1) | 4966 | 26742 | **98** |
| (4,6,1) | 1762 | 8116 | **106** |

All three explicit optimized witnesses meet `[4,2,4,2,2,2,4,2]` word counts over H2..H9 (22 words), exactly five complete keys, net `(2,0,0,0,0,0)` each, rational rank 9 every window, and six frozen signatures. Every Trie vertex variable denotes one ordered signed primitive-prefix edge; selecting a terminal forces every ancestor; each horizon has all four rank clauses, and nonseed-key occurrence and word-slot upper bounds are explicit. Direct native prefix-union recomputation matches all three objectives. Finite MILP optimality depends on HiGHS and model equivalence, rather than an independently formalized UNSAT certificate.

In contrast, candidate keys (6,5,1) and (5,7,1) pass the *signature-only* 49-case screen but fail the *slot-plus-all-five-keys* feasibility test. This explains why signature-only pruning is insufficient when the mother problem fixes window slot counts.

## Reproduce / evidence

`python SCREEN_EC49FDO.py` (stdlib), then `OPENBLAS_NUM_THREADS=1 python REPLAY_EC49FDO_MILP.py` (NumPy/SciPy). The latter imports the existing sibling `../EC49FDL_TEN_MIXED_PAIR_EXACT_20261107/REPLAY_EC49FDL_PORTABLE.py`; it is a narrow extension of the verified EC49FDN model, not a replacement for the frozen primitives. `EXACT_REPORT_EC49FDO.json` records the actual executed finite results and the scope.

Status: author-computed / GitHub evidence publication; independent Driver review and native Source Result not yet obtained. Original <=93 five-key mother target remains open.

## Next EC49FDP

Inspect the other **12** slot-feasible H9-key replacements per case, prioritizing 1512/1513 where the original seed prefix cost is 42; run exact signed-prefix MILP with hard <=93 feasibility test and derive witness or instance-specific bound. Separately alter H2/H3 seed and jointly optimize five-key choice, rather than inferring a global obstruction from four local seed families. Preserve positive BRC multiplicity, signed order, and the original observer semantics.
