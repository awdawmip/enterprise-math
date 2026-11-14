# EC49FEI — BRC five-key budget saturation and complete radius-one exclusion

Date 2026-11-08. Author-side **exact finite proof**, unreviewed and not canonically admitted. Scientific input remains frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Parent: EC49FEH, whose 94-edge witness and exact lower-bound proof use the original six signed-X6 operator words and the nine-state observer.

## Proposition 1: five-key budget saturation for the 22-path quota

Fix the H2...H9 word quotas `(4,2,2,4,2,2,4,2)` and require the four exact rank-nine observation clauses `(18,20,33,40)` at each horizon. Every word has endpoint `+2E1` and records a complete **positive native BRC cache key** `(x,y,z)` on axes E1,E2,E3. Preserve ordered signed native paths and all word identities.

For a horizon with two required words, the only possible signature combination is `(16,32)` because those two signature bits each cover two of the four clauses and each low signature `1,2,4,8` covers just one. In the operator grammar, any high signature key for horizon h has `x+y=h+1`. The high requirements at H3,H4,H6,H7,H9 hence need keys with respective `x+y` values `4,5,7,8,10`. These are disjoint **five required key groups**. There are at least five different keys, so a global budget of at most five forces exactly one key in each group; all shared horizon keys belong to that set.

In the full finite grammar H3's only single complete positive BRC key that supports **both** signatures 16 and 32 is `(3,1,1)`. Therefore this key is mandatory. H2 can achieve the four low signatures with this key, and no other one of the four late keys is legal at H2. The H2 words are exactly `ce,ec,de,ed`. H3's 16/32 choices are `(feg or fge, gef or gfe)`.

Exact high-signature key counts by horizon: H4: 2, H6: 6, H7: 9, H9: 16. The complete 22-path five-key inventory family therefore has **2×6×9×16 = 1728** possible inventories BEFORE testing four-path feasibility. This is a finite parameterization of all five-key inventories within the declared horizon/signature/quota class; it is not a claim of 1728 valid full systems.

The exact high-key options are:

- H4: `(3,2,1),(4,1,1)`.
- H6: `(3,4,1),(4,3,1),(5,2,1),(5,2,2),(6,1,1),(6,1,2)`.
- H7: `(3,5,1),(4,4,1),(5,3,1),(5,3,2),(6,2,1),(6,2,2),(7,1,1),(7,1,2),(7,1,3)`.
- H9: `(3,7,1),(4,6,1),(5,5,1),(5,5,2),(6,4,1),(6,4,2),(7,3,1),(7,3,2),(7,3,3),(8,2,1),(8,2,2),(8,2,3),(9,1,1),(9,1,2),(9,1,3),(9,1,4)`.

## Proposition 2: complete one-key replacement exclusion

For the original 94-edge witness's five-key inventory

`K0 = ((3,1,1),(3,2,1),(4,3,1),(4,4,1),(5,5,1))`,

consider replacing **exactly one** of these five keys by any other complete BRC key while preserving the five-key global budget, 22-path quota, rank-nine clauses, native endpoint and allowing arbitrary word ordering, any legal key placement and within-window mixing. A change to the first key `(3,1,1)` destroys H3 feasibility as Proposition 1 shows. Changing one of the four late keys to another high-signature eligible key gives exactly `1+5+8+15 = 29` possible inventories; any other replacement leaves a mandatory high horizon uncovered and is infeasible.

For all **29** altered inventories and **all four** allowed early H3 variants, the exact per-depth prefix-cover lower bound is at least **98 edges**. Hence no one-key replacement of K0 admits a system of cost ≤97, and in particular none meets the ≤93 mother target. K0 itself has exact optimum **94 edges** from EC49FEH.

Per-replacement certified lower bounds (all four early variants give the same bound):

| Changed slot | Replacement key → lower bound |
|---|---|
| H4 | (4,1,1)→98 |
| H6 | (3,4,1)→101; (5,2,1)→102; (5,2,2)→117; (6,1,1)→110; (6,1,2)→118 |
| H7 | (3,5,1)→102; (5,3,1)→98; (5,3,2)→106; (6,2,1)→102; (6,2,2)→106; (7,1,1)→110; (7,1,2)→114; (7,1,3)→118 |
| H9 | (3,7,1)→118; (4,6,1)→98; (5,5,2)→126; (6,4,1)→98; (6,4,2)→102; (7,3,1)→98; (7,3,2)→102; (7,3,3)→135; (8,2,1)→108; (8,2,2)→112; (8,2,3)→116; (9,1,1)→127; (9,1,2)→135; (9,1,3)→143; (9,1,4)→166 |

## Exhaustive proof certificate

`EC49FEI_EXACT_ONE_KEY.py` applies the original unmodified exact native operator/nine-state observation core in `EC49FEH_EXACT_CERT.py`: it enumerates the four mandatory high-horizon key families from integer operator counts; constructs all legal path pools at every horizon/signature; checks H5/H8 contain the low signature set; forms all mandatory late-group depth-prefix incidence masks, and solves the exact minimum additional-prefix set cover via exhaustive memoized integer bitmask DP. It repeats the calculation for all four early H3 variants (29×4 full configurations). Per-depth bounds relax across depths, making them unconditional **lower** bounds for all coherent full-path choices.

`EC49FEI_REPORT.json` stores every candidate high key, all 29 inventory changes, all 4 early-prefix variants, every depth cover vector, and every exact lower bound. Independently, `EC49FEI_INDEPENDENT_MILP.py` uses a distinct SciPy/HiGHS integer-set-cover solver to check all **2,432** individual depth cover instances (variable horizon up to 26 depth levels). All 2,432 agree with exact DP, MIP gaps zero for nontrivial cases; no external solver is relied on for the exact combinatorial proof. The original 22-word 94-edge witness is also checked by EC49FEH.

Run in one directory:

```bash
python EC49FEH_EXACT_CERT.py > EC49FEH_CERT.json
python EC49FEI_EXACT_ONE_KEY.py > EC49FEI_REPORT.json
python EC49FEI_INDEPENDENT_MILP.py > EC49FEI_MILP_REPORT.json
```

The GitHub `EC49FEI_complete_evidence.tar.xz.b64` is a lossless base64-encoded XZ archive containing all programs, original native semantics, complete exact results and independent verification. It is submitted alongside this text, with immutable Git blob readback. No credentials or private infrastructure files are included.

## Next EC49FEJ

The full 22-path high-signature family comprises at most 1,728 inventories. Use a cheaper certified cover lower bound and compatible key families to target inventories at Hamming distance ≥2 from K0; the 29 radius-one inventories are now excluded. A change in H7 path quota or observation signature family is another distinct route, but should not be silently conflated with this fixed-22-path theorem. The original mother target remains five full BRC keys, native-prefix cost ≤93. Native ownership, CLAIM and independent Driver review are separately pending due to unavailable control gateway.
