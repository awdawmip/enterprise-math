# PREFIX-922 — Full-row noninjectivity across 91 zero-coincident-source second moduli

Date: 2026-11-19 (Asia/Shanghai). Auxiliary named XOR two-port observer, frozen input `f42f2906d77f24085c123f3ccfe9667d41caa96d`; building on PREFIX-918, PREFIX-920 and PREFIX-921. Status: EXACT_FINITE_COMPUTED / TWO_IMPLEMENTATION_NAMED_WITNESS_AUDITED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Exact finite proposition

For p=32, N=2^32, legal named traces Z_x=(x,x) and F_x^i=(x,x XOR 2^i), and strict-19-bit odd modular observations (start mod a, endpoint mod b), define the finite set

[
D=\{b\in[262145,524287]\cap(2\mathbb Z+1):
 W_{32}(b)=0,\quad b\mid 2^d-1\ \text{or}\ b\mid2^d+1\ \text{for some }32\le d\le52\},
]
where
[
W_{32}(b)=\sum_{d=1}^{31}(32-d)(1_{b\mid2^d-1}+1_{b\mid2^d+1}).
]

**Result:** (|D|=91). For **every** (b\in D) and **every** odd strict-19-bit (a), the named observer is noninjective. Thus
[
\boxed{91\cdot131072=11,927,552}
]
distinct **ordered** modulus pairs ((a,b)) have an explicit, directly checked collision between **different starting states**. The 91 rows have no equal-start collision, because (W_{32}(b)=0). This result is a certified finite family, not a universal claim about all b and not an increment deduplicated against the preexisting global collision-union ledger.

## Complete selection, scan and audit

First independently enumerate all 131072 strict-19-bit odd b, computing successive (2^d\bmod b) exactly for (1\le d\le52). Reject b when (2^d\equiv\pm1\bmod b) for any (1\le d\le31); select it when (2^d\equiv\pm1\bmod b) for some (32\le d\le52). This selects exactly 91 b.

For each selected b, run `PREFIX921_R6_DISTINCT_START_ROW.cpp` (C++17) across all 131072 legal a. The generator uses zero/zero, zero/flip and then full source-labelled two-flip bit-window search; it verifies its actual returned collision endpoints and both moduli before emitting each witness. All 91 rows returned zero gaps. An independent Python auditor additionally parsed every generated witness, recomputed its two real XOR endpoints and verified state bounds, both modular equalities, source-bit labels and complete ordered a coverage for every b. In total **11,927,552 named witness records** were independently checked, with **0 invalid records**.

The disjoint first-witness classes over the full 91-row collection are:

| First witness class | Number of ordered modulus pairs |
| --- | ---: |
| Zero/zero | 437,682 |
| Zero/one-flip | 5,381,582 |
| One-flip/one-flip | 6,108,288 |
| **Total** | **11,927,552** |

`PREFIX922_R6_W0_91ROW_COUNTS.csv` contains the complete 91-item b list and all first-witness type counts. Each row sums to exactly 131072. The independent audit program, `PREFIX922_R6_W0_91ROW_INDEPENDENT_AUDIT.py`, generates the set D, executes the original C++ witness generator, and independently checks its entire stdout. The locally generated extended JSON result has SHA-256 `749aa8178e32e22f48ccc233b49258e62cf4ded8e28ab33eb6fad0e06a67d5b0`; its per-b evidence includes each generated output SHA-256. The CSV plus executable script is a self-contained reproducible Source certificate; each direct witness is regenerated rather than storing 11.9 million repeated full text lines in the repository.

## Mathematical meaning and next unit

PREFIX-921 identified a Mersenne b with compulsory same-start collisions. The 91 b here have **no same-start collision**, so their noninjectivity is entirely from genuinely different starts. This supplies 91 exact additional complete-row test cases of the harder collision mechanism. P000, native coordinate scope and the original scientific freeze are untouched.

Next: determine whether the row property holds for all remaining strict-19-bit odd b with (W_{32}(b)=0), or find a counterexample with no colliding named traces. Continue to distinguish the auxiliary observer from the parent (B_{\mathrm{fix,odd}}(32)\in\{19,20\}) objective, and from native X6 task ownership. No shared CLAIM, formal review or admission is represented by this research note.
