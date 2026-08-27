# P017 — c=103/20 j=1 Top×Top Canonical-Suffix Coupling Refinement

Status: `PROVED_WIP EXACT TOP×TOP DIRECT CARRY < 0.00058 L23 / REFINES 0.001 BLOCK BOUND / NOT FULL j=1 / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Companion checker:

`experiments/p017_p2_c515_t12_j1_top_top_suffix_coupling_20260827.py`

Refines:

`docs/P017_P2_C515_T12_J1_TOP_TOP_DIRECT_CARRY_20260827.md`.

Depends on:

- `docs/P017_P2_C515_T12_RESIDUAL_TRIPLE_CANONICAL_BN_FACTORIZATION_20260827.md`;
- `docs/P017_P2_C515_T12_J1_TOP_LONG_SUPPORT_BT_BINS_20260827.md`.

Purpose: retain the canonical dependence between the long hard factor and the 185 top short suffixes. The preceding direct block theorem treated the long and short supports independently. On the corrected depth-four `j=1` Rosser family that loses a substantial finite factor.

---

## 1. Top short states are exactly two-prime suffixes

At the Tier-A splice the `j=1` hard primes lie in

\[
29\le q\le1439.
\]

The top short block is

\[
\frac56N_0<n\le N_0,
\qquad N_0=W^{1/4}.
\]

Exact enumeration gives 185 short states. Since the top block lies above `15000` whereas every single hard prime is at most `1439`, each one is necessarily

\[
\boxed{n=ab,\qquad 29\le a<b\le1439,}
\tag{SC1}
\]

a product of two distinct hard primes.

By the deterministic greedy suffix rule, these are the two smallest hard primes of the full Rosser modulus. Consequently every prime entering the long hard factor `b_1` is strictly larger than `b`.

The corrected `j=1` hard Rosser depth is at most four, so after two primes have been placed in the short suffix, `b_1` contains at most two hard primes.

---

## 2. Suffix-dependent long reciprocal mass

For a top short suffix `ab` with `a<b`, put

\[
S_{>b}=\sum_{\substack{b<q\le1439\\q\text{ prime}}}\frac1q.
\]

The reciprocal mass of all admissible long hard factors is bounded by

\[
\boxed{
C_h(b)
\le
1+S_{>b}+\frac12S_{>b}^2.
}
\tag{SC2}

The final term is the repeated-prime majorant for products of two distinct primes; it is intentionally one-sided.

The companion checker upper-encloses every reciprocal with denominator `10^12` and, over the exact 185 top short states, proves

\[
\boxed{
\sum_{ab\text{ top short}}C_h(b)<236.
}
\tag{SC3}

For comparison, multiplying the former uniform bound `269/128` by 185 would cost more than 388. Thus keeping the canonical suffix relation removes roughly forty percent of that finite support envelope.

---

## 3. Couple the Brun–Titchmarsh long count to the short suffix

The q-binned long-support theorem proved

\[
R_{\log}
:=
\sum_{1447\le r<q,\ rq^2<B}
\frac1{rq\log(q/6)}
<
\boxed{\frac{1997873}{115500000}}.
\tag{SC4}

For fixed top short suffix `ab`, the same Brun–Titchmarsh proof, now summing only the allowed long hard factors above `b`, gives

\[
\frac{A_M(ab)}{(5/6)B}
<
\frac25R_{\log}C_h(b).
\tag{SC5}

Summing (SC5) over all 185 short suffixes and applying (SC3),

\[
\sum_{ab}A_M(ab)
<
\frac56B\cdot\frac25R_{\log}\cdot236.
\tag{SC6}

As in the preceding top×top theorem, the full level condition forces the P(23) anchor divisor to be `e=1` throughout this block.

---

## 4. Refined direct sharp-carry bound

The corrected pair kernel and source prefactor satisfy

\[
\kappa\le\frac{73}{80},
\qquad
\Delta=\frac{93}{20}.
\]

For the sharp anchored interval every modulus carry has magnitude `<1`. Therefore

\[
|R_{11}^{\rm top\times top}|
<
\frac1\Delta\frac{73}{80}
\frac56B\frac25R_{\log}\cdot236.
\]

Using

\[
B<494793856728460,
\]

and

\[
L_{23}=232018561402828200,
\]

the exact rational checker proves

\[
\boxed{
\frac{|R_{11}^{\rm top\times top}|}{L_{23}}
<
\frac{29}{50000}
=0.00058.
}
\tag{SC7}

The internal rational upper bound is about `0.00056946`; the decimal is not used in the proof.

---

## 5. Consequence and boundary

The top×top part of the only large valuation shell is now below `0.00058 L23` with no Fourier expansion and no generic factorization multiplicity.

The gain comes from preserving four exact structures simultaneously:

1. top-long Brun–Titchmarsh support compression;
2. the exact 185-state short set;
3. the canonical rule that the short pair consists of the two smallest hard primes;
4. the full-level fact that top×top forces anchor `e=1`.

This still does **not** control lower geometric blocks, the `j=2` 254-state correction, or finite source-main normalization. No finite P2 theorem is claimed.

The next step is to generalize the anchor exclusion to a depth filtration

\[
e<\left(\frac65\right)^{i+j+2}
\]

on disjoint long/short blocks and use that filtration to decide which remaining high blocks can still be closed by direct carry before Cauchy is invoked.
