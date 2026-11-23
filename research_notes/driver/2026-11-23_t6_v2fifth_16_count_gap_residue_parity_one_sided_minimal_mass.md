# T6 exact-v₂(d)=5: 16-count gap, odd-residue parity, and the least one-sided 16-atom local profile

Date: 2026-11-23 (Asia/Taipei). Mathematical analysis: original Driver `EM-DVR-DEBB5E`. Reuse previously published higher-v₂ cancellation without reassigning its original mathematical contributors. This is a derived scientific subresult, not a Native Result, Review, CLAIM or formal Activity association.

## Exact model and prior dependency

Let `A,B` be finite multisets of positive integer exponents, each with `sum(e) <= 2331`. Set `d=e+1`, `H_k(X)=sum (e/(e+1))^k`, and `S_k(X)=sum d^(-k)`. Assume `H_0(A)=H_0(B), ..., H_6(A)=H_6(B)`.

The earlier finite theorems give `m_A(d)=m_B(d)` for all `v₂(d)>=6`, under these same T6 hypotheses; in particular use [the exact-v₂=6 theorem](https://github.com/awdawmip/enterprise-math/blob/c577f07bcd434340c500b91e4b67a5402c82c514/research_notes/driver/2026-11-23_t6_p2_sixth_universal_cancellation_three_tier.md), together with its stated exact-v₂>=7 dependencies. That earlier certificate is reused at its own reported proof status; it is not independently reaudited in this note.

Define `n_X = sum_{j odd, 1<=j<=71} m_X(32j)` and `t_X = sum_{j odd, j mod 8 in {3,5}} m_X(32j)`.

## Elementary population theorem

**Conclusion:** `n_A == n_B (mod 16)` and `t_A == t_B (mod 2)`. Consequently, if `|n_A-n_B|<16` then `n_A=n_B`. All nonzero population gaps in the original mass budget are among `16,32,48,64` in absolute value.

**Proof.** Binomial inversion of `e/(e+1)=1-1/d` yields `S_k(A)=S_k(B)` for `1<=k<=6`. Cancel the already-equal `v₂(d)>=6` denominators *literally*. Multiply the full signed `S_k` equality by `2^(5k)` and reduce in the 2-adic integers modulo `2^k`. A denominator of lower valuation `v₂(d)<=4` contributes a multiple of `2^k`, and only `d=32j` with odd j survives. Therefore, for every `k=1,...,6`,

`sum_{j odd} [m_A(32j)-m_B(32j)] * j^(-k) == 0 (mod 2^k).`

For `k=4`, every odd unit satisfies `j^4 == 1 (mod16)`, hence the congruence becomes `n_A-n_B ==0 (mod16)`. For `k=6`, reduce the existing mod64 congruence further modulo16. The odd-unit values are `j^(-6)==9 (mod16)` for `j mod8 in {3,5}` and `1 (mod16)` otherwise. Thus `(n_A-n_B)+8(t_A-t_B)==0 (mod16)`. The count congruence forces `t_A-t_B` even. Finally `0<=n_X<=floor(2331/31)=75`, so nonzero differences divisible by16 have absolute values 16, 32, 48 or 64. QED.

This generalizes the previous single/two-atom restricted investigations in a different direction: it immediately excludes unequal-population cases 0-vs-1 through 0-vs-15, 1-vs-2, 2-vs-3, etc. It does not by itself determine equal-population multisets with three or more atoms.

## Finite exact optimization for 0 versus 16 atoms

**Precisely scoped corollary:** Suppose one side has *no* exact-v₂=5 denominator and the other has *exactly sixteen*. The 16-atom side has exponent mass in this layer **at least 1520** to satisfy the necessary six-component local signature above. This lower bound is sharp for the *local congruences*; whether the complete H-observations can be matched by lower-valuation denominators remains open.

Write its sixteen odd quotients as `j_i=1+2a_i`, `a_i>=0`, with `A=sum a_i`. Layer mass is `sum(32j_i-1) = 496+64A`. The third local congruence uses `j^(-3)==j (mod8)`; it requires `sum j_i=16+2A==0 (mod8)`, so `A` is a multiple of 4. For mass below 1520 only `A=0,4,8,12` are possible.

The companion exact Python checker [T6_P2_V5_COUNT_GAP16_MINIMAL_ONE_SIDED_20261123.py](https://github.com/awdawmip/enterprise-math/blob/main/research_checks/T6_P2_V5_COUNT_GAP16_MINIMAL_ONE_SIDED_20261123.py) enumerates **all integer partitions** of each such A into at most sixteen nonnegative parts (zeros padded), and evaluates all six modular signatures using exact odd modular inverses. It finds **zero** signatures at A=0,4,8,12. At A=16 (mass 1520), it finds exactly **22 unordered profiles**. One explicit sharp local witness is twelve copies of `j=1`, three copies of `j=3`, and one copy of `j=27` (mass `12*31+3*95+863=1520`). All six modular sums are exactly zero. Since any profile below the claimed minimum has A in the enumerated set and `j<=31`, the finite search has complete coverage; no arbitrary upper bound or heuristic pruning is used.

Verified local execution output:
```text
excess=0 sum_j=16 mass=496 zero_signatures=0
excess=4 sum_j=24 mass=752 zero_signatures=0
excess=8 sum_j=32 mass=1008 zero_signatures=0
excess=12 sum_j=40 mass=1264 zero_signatures=0
excess=16 sum_j=48 mass=1520 zero_signatures=22
PASS: minimal local signature-zero 16-atom mass is 1520; 22 minimum profiles
```

Thus a 0-versus-16 scenario, if otherwise compatible with the full problem, leaves at most `2331-1520=811` exponent mass on the 16-atom side for all remaining denominators. The next discriminating question is whether that remaining budget can supply the necessary `v₂=4,3,...` mixed-signature corrections and full rational moments. For gaps >=16 with atoms on both sides, the one-sided 1520 bound is not automatically transferred.

## Claim boundaries and provenance

- Exact elementary count and residue-parity congruences: proved from `S_4,S_6` and the stated higher-v₂ cancellation dependency.
- Exact finite optimization: partition enumeration, exact modular arithmetic and an explicit sharp witness; finite-local congruence status only.
- The original T6 mother objective and all Native Result/Review/Activity admissions remain open/separate. Previous T6 results and authors retain their provenance.
