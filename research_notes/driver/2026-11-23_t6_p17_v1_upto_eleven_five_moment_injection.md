# T6: exact 17-adic valuation-one cancellation with at most eleven atoms per side

Date: 2026-11-23 Asia/Taipei. Mathematical author: continuing Driver `EM-DVR-DEBB5E`; prior T6 mathematical contributors and original task owners retain their own provenance. This is a scoped, reproducible exact finite proof, not an admitted Native Result or independent review.

## Proposition

Let `A,B` be finite multisets of positive integer exponents `e`, with **independent per-side budgets** `sum_{e∈A}e<=2331` and `sum_{e∈B}e<=2331`. For `X=A,B`, write `d=e+1`, `H_k(X)=sum_{e∈X}(e/(e+1))^k` and `m_X(d)` for denominator multiplicity. Suppose `H_k(A)=H_k(B)` for all `0<=k<=5`. If each side has at most **eleven** denominators with exact `v_17(d)=1` (multiplicity counted), then

```
m_A(17u)=m_B(17u)   for all positive u with 17∤u.
```

This includes the original T6 hypothesis `H_0,...,H_6` equal, without using the sixth degree moment.

## Exact reduction from the original complete moments

Set `S_k(X)=sum_{e∈X}(e+1)^(-k)`. Binomial inversion supplies `S_k=sum_{i=0}^k(-1)^i*binom(k,i)*H_i`, hence `S_k(A)=S_k(B)` for `k=1,...,5`.

Reuse the previously saved [universal cancellation of denominators divisible by 17²](https://github.com/awdawmip/enterprise-math/blob/e4efdec710abca45bfd1cf93255049fab53bd72e/research_notes/driver/2026-11-23_t6_universal_p17_squared_cancellation_67_profile_injection.md) at its actual hypotheses, available already under `H_0,...,H_3`. Subtract the equal contributions of all such denominators. Multiply the remaining k-th full rational identity by `17^k` and reduce modulo `17^k` in the 17-localization. Every term with denominator prime to 17 vanishes. The remaining exact-valuation-one profiles `U_A,U_B` therefore satisfy

```
F(U_A)=F(U_B),
F(U)=(sum_{u∈U} u^{-k} mod 17^k)_{k=1,...,5}.
```

No independent per-prime moment equality is assumed.

## Exhaustive exact injectivity

All legal exact-`v_17(d)=1` atoms are `d=17u`, `1<=u<=137`, `17∤u`, with mass cost `17u-1`. Legal one-side profiles are nondecreasing sequences `u_1<=...<=u_n`, `0<=n<=11`, `sum_i(17u_i-1)<=2331`.

The exact C++17 checker enumerated all profiles and independently counted them using an unbounded-coin generating-function integer DP. The signature consists of five exact modular inverse-power sums mod `17,289,4913,83521,1419857`, encoded losslessly using radices `17^1,...,17^5`. Its key space is `17^15=2862423051509815793<2^64`. All keys were assigned to exactly one of 256 buckets based on low eight key bits, then every bucket was fully sorted and every adjacent key equality compared.

| Profile cardinality | Exact lawful profiles |
|---:|---:|
| 0 | 1 |
| 1 | 129 |
| 2 | 4,220 |
| 3 | 62,225 |
| 4 | 531,399 |
| 5 | 3,017,496 |
| 6 | 12,469,599 |
| 7 | 39,974,384 |
| 8 | 104,260,287 |
| 9 | 229,524,497 |
| 10 | 439,058,783 |
| **11** | **747,018,123** |
| **Total** | **1,575,921,143** |

The enumeration and separate DP match in every cardinality. To avoid an unnecessary long monolithic output, one successful emission wrote all legal 0–10-atom keys (`828903020`), a second successful emission independently traversed all 0–11-atom profiles but wrote only the 11-atom keys (`747018123`), and each bucket's bytes were concatenated preserving the exact disjoint cardinality union. The combined buckets were sorted and checked in four disjoint completed range processes:

| Bucket range | Exact keys compared | Duplicate signature pairs |
|---|---:|---:|
| 0–63 | 393,982,351 | 0 |
| 64–127 | 393,979,633 | 0 |
| 128–191 | 393,980,999 | 0 |
| 192–255 | 393,978,160 | 0 |
| **All buckets** | **1,575,921,143** | **0** |

All four comparators completed with exit code 0, and their exact counts add to the independent complete population. Therefore `F` is injective on every legal profile with at most 11 atoms, including profiles of different cardinality; the necessary 17-adic congruences force `U_A=U_B`, proving the proposition.

## Reproduction and boundary

- First compile/run [the previously saved 0–10-atom checker](https://github.com/awdawmip/enterprise-math/blob/8a9a97db330df5e96c9fac3fc9615657f1b8fe93/research_checks/T6_P17_V1_UPTO_TEN_FIVE_MOMENT_BUCKET_EXACT_20261123.cpp) with `emit` in a sufficiently large working directory; its 256 files are `t6p17ten_<b>.bin`. Check the printed independent DP counts.
- Compile/run [the additive 11-atom emitter](https://github.com/awdawmip/enterprise-math/blob/148c3b9f6971a06bc5e4832e9878ebbf994f92f4/research_checks/T6_P17_V1_ELEVEN_ADDITIVE_BUCKET_EXACT_20261123.cpp) with `emit11`, producing exactly the 11-atom additions as `t6p17eleven_<b>.bin`; check its printed DP counts and completion marker.
- For each integer `b=0,...,255`, append `t6p17eleven_<b>.bin` to `t6p17ten_<b>.bin` with an ordinary binary concatenation, once only. Then run the 0–10 checker with `check 0 64`, `check 64 128`, `check 128 192`, `check 192 256`, using mutually disjoint bucket ranges. Each verifies all keys in its range and deletes its checked bucket files. A failed or interrupted emission must be restarted from fresh files to avoid duplicate appends.

The computation is entirely integral, including modular inverse computations; this is a finite exhaustive calculation supported by source code and documented complete coverage, not a Lean formalization. The independent DP validates domain cardinalities rather than substituting for the signature collision search.

The proposition is restricted to at most 11 exact-`v_17(d)=1` atoms on each side. A higher-cardinality 17-adic injection theorem and the global `T_6=2332` lower-bound objective remain open. Mathematical publication, Activity association, Native Review, canonical Result and official Task completion are distinct. No owner, identity or scheduling changes were made.

Next experimental branch: test 12 atoms by modular partitioning or derive a structural reason that the five signature coordinates separate higher-cardinality profiles; if an exact signature collision arises, test the sixth moment and do not call that alone a counterexample to full rational-moment equality.
