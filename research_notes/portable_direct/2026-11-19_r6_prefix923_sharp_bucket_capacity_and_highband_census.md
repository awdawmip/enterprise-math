# PREFIX-923 — Exact start/end bucket-capacity strengthening and 1,024 high-band row certificates

Date: 2026-11-19 (Asia/Shanghai); 进取数论研究6, independent auxiliary BRC observer research. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Direct earlier sources: PREFIX-896 (global capacity), PREFIX-917 (equal-start mass), PREFIX-918 (two-flip bit-window kernel), PREFIX-920 (row scan), PREFIX-921 (Mersenne minima), PREFIX-922 (91 special complete rows). Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / SOURCE_LABELS_DIRECTLY_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Statement and preservation of typed population

Let `p>=1`, `N=2^p`, and let the **named** trace population consist of `Z_x=(x,x)` and `F_x^i=(x,x XOR 2^i)`, `0<=x<N`, `0<=i<p`. The two-port observer is `Phi_(a,b)(u,v)=(u mod a,v mod b)`, where `a,b` are positive integers. The labels `Z/F`, `i` and `x` remain part of distinct underlying traces, even if observations agree.

### Theorem A — two-sided bucket-capacity obstruction

For all `p>=1`, injectivity of the full named trace observer requires **both**

```
b >= (p+1)*ceil(N/a)  and  a >= (p+1)*ceil(N/b).
```

Proof: among the `N` starts, some first-port residue class has `ceil(N/a)` members. For each start there are exactly `p+1` different named traces, all with that same first-port observation. They must occupy distinct second-port residues if the full observer is injective, establishing the first inequality. Likewise, for each endpoint `y` there are exactly `p+1` named traces ending at `y`: one zero trace and one flip preimage at each bit `i`, with starting point `y XOR 2^i`. Some second-port residue class contains `ceil(N/b)` endpoints; their `(p+1)ceil(N/b)` named incoming traces require distinct first-port residues. This proves the second inequality. In particular, violation of either inequality certifies a collision without computing trajectories.

For `p=32`, define the exact strict-19-bit odd modulus set
`Q={262145,262147,...,524287}` with `|Q|=131072` and `|Q^2|=17,179,869,184`. Set
`h(a)=#{b in Q: b<33*ceil(2^32/a)}`. Exact integer counting yields

```
sum_{a in Q} h(a)                          = 7,365,158,936
#{(a,b) in Q^2: [b<33 ceil(N/a)] OR
                  [a<33 ceil(N/b)]}       = 7,365,546,244.
```

PREFIX-896 previously proved the global-cardinality collision set `ab<33N` has size `7,364,142,398`. Since `b<33ceil(N/a)` implies `ab<33N` **or** a strict ceiling excess (and the symmetric analogue), the new two-sided exact condition contains that global set and adds **1,403,846** certified ordered pairs beyond *that capacity-only set*. This increment is **not** deduplicated against later PREFIX-912/914/920/922 global or row certificates.

A reproducible integer implementation computes `h` with lower-bound searches of the sorted odd-modulus array, and unions the two monotone conditions through a second reverse sweep. No floating-point calculation or theorem-admission claim is used.

## Theorem B — explicit further complete rows outside PREFIX-922's 91 special rows

Apply the already published PREFIX-921 C++17 exact source-labeled `scan(a,b)` and `verify(a,b,w)` to all `131072` odd `a in Q`, for each of the following eleven second ports:

`b in {262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285}.`

All eleven rows have a directly checked **different-start** legal named XOR witness for every `a`, i.e. **1,441,792** individual verified ordered modulus-pair certificates. A separate Python auditor checked every emitted witness against the underlying exact XOR transitions, bounds, labels and both modular equalities: invalid witnesses **0**. These eleven ports are outside the `D` selection in PREFIX-922 (which requires `W32(b)=0` and a signed power-of-two congruence at an exponent in 32..52); `b=262145` has `W32(b)>0`, while the other ten have no signed such congruence in that late range.

For regression, the twelfth tested row `b=524287` reproduces PREFIX-921's seven cases with no **different-start** witness. Their identical-start source-label witnesses `F_0^0=(0,1)`, `F_0^19=(0,524288)` collide since `524288-1=524287=b`. Thus the test confirms complete noninjectivity of this row and exposes why the older scanner's seven raw misses are not seven injective observers. Twelve audited full rows cover `1,572,864` distinct ordered pairs including that already-known Mersenne row.

## Theorem C — deterministic 1,024-row high-band collision census

Select 1,024 distinct second ports without random library state:
`b_t=262145+2*((77081*t+12345) mod 131072)` for `0<=t<1024`.
The multiplier 77081 is odd, hence is invertible modulo `2^17`, so these ports are distinct. Let `A_hi={500001,500003,...,524287}` (`|A_hi|=12144`). For each `t` and each `a in A_hi`, the exact parent `scan(a,b_t)` emits a distinct-start witness; its original `verify` directly checks the state bounds and both residue equalities. Thus the finite domain of `1,024*12,144=12,435,456` **ordered pairs** has no witness deficit. The CSV contains exactly one record per selected `b`; every record has `rows=12144,raw_zero=0,first_zero=0`. Its deterministic ASCII SHA-256 is

`831e4092915dfa3f2d7c06aaea90fbc40240fdd2f1bd7abce7878e7e5068e385`.

The reproducibility driver `PREFIX923_R6_BUCKET_AND_HIGHBAND_VERIFY.py` preserves the source-level PREFIX-921 scan and verify methods, alters only the C++ reporting main to permit a bounded `a` window, compiles with `g++ -O3 -std=c++17`, runs all selected 1,024 rows, asserts zero deficits and hashes the output CSV. It also independently recomputes the exact two-sided bucket counts. The full-row supplemental audit uses `PREFIX921_R6_DISTINCT_START_ROW.cpp` and a separate Python integer recheck of each printed direct witness.

The 1,024-row high-band sample is a **finite certified family**. It supplies further falsifiable search evidence for the mother question `B_fix,odd(32) in {19,20}`; it is not an exhaustive classification of all `Q^2`. All of the present observer results remain separate from native X6 dynamics and from formal Result/Review/CLAIM authority.

## Evidence and next unit

- Frozen input and prior C++ generator: `research_notes/portable_direct/PREFIX921_R6_DISTINCT_START_ROW.cpp`, Git blob `0546a05a84f007ce21ed12fdded576108cd4c676`.
- New checker: `research_notes/portable_direct/PREFIX923_R6_BUCKET_AND_HIGHBAND_VERIFY.py`.
- Full deterministic data: `research_notes/portable_direct/PREFIX923_R6_1024_HIGHBAND_COUNTS.csv`.
- Directly audited full-row results, reproduced locally in 2026-11-19, had witness counts by b: 440667=(2467,50032,78573), 440669=(1,79717,51354), 524285=(4095,49010,77967), 524283=(1,46259,84812), 524281=(555,70565,59952), 524279=(2,61609,69461), 524277=(1640,44356,85076), 524275=(2369,57265,71438), 524273=(643,72027,58402), 262145=(6657,57485,66930), 321651=(8339,55226,67507); tuples denote first witness classes (zero/zero, zero/flip, flip/flip). Each triple sums to 131072.

**Next discriminating experiment:** restrict the unresolved `Q^2` candidate search to moduli satisfying *both* new bucket-capacity necessary inequalities and excluding established signed-power aliases; seek either a certified injective witness or a general new sufficient collision mechanism. Compare the new capacity-only set against the entire current collision-certificate ledger before asserting a globally deduplicated increment. Preserve each residue/provenance branch until its actual observer-safety condition is proved.
