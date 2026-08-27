# P017 — c=103/20 j=1 Top×Top Direct Sharp-Carry Certificate

Status: `PROVED_WIP EXACT TOP×TOP ABSOLUTE CARRY < 0.001 L23 / NO FOURIER / NOT FULL j=1 / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Companion checker:

`experiments/p017_p2_c515_t12_j1_top_top_direct_carry_20260827.py`

Depends on:

- `docs/P017_P2_C515_T12_RESIDUAL_TRIPLE_VALUATION_LADDER_20260827.md`;
- `docs/P017_P2_C515_T12_RESIDUAL_TRIPLE_CANONICAL_BN_FACTORIZATION_20260827.md`;
- `docs/P017_P2_C515_T12_P23_ANCHOR_AFTER_SUFFIX_FACTORIZATION_20260827.md`;
- `docs/P017_P2_C515_T12_J1_TOP_LONG_SUPPORT_BT_BINS_20260827.md`.

Purpose: bound one complete geometric block of the corrected residual `j=1` triple carrier directly in the sharp full-basin carry model. The point is that the newest support compression is already strong enough that this block does not need Cauchy, Fourier truncation, or the explicit reciprocal-sum constant 15.

---

## 1. Frozen top scales

At the Tier-A splice put

\[
K_0=116009280740973308,
\qquad W=K_0+1,
\]

and keep

\[
D=W^{10/9},
\qquad B=W^{31/36},
\qquad N_0=W^{1/4},
\]

so

\[
D=BN_0.
\]

Use the ratio-`6/5` top blocks

\[
\boxed{
\frac56B<m\le B,
\qquad
\frac56N_0<n\le N_0.
}
\tag{TT1}

The exact scale certificates give

\[
\lfloor B\rfloor=494793856728459,
\qquad
\lfloor N_0\rfloor=18455.
\]

---

## 2. The P(23) anchor label disappears on top×top

The preferred anchored target interval has

\[
Q_{23}=P(23)=223092870,
\]

\[
L_{23}=Q_{23}
\left\lfloor\frac{2K_0}{Q_{23}}\right\rfloor
=232018561402828200.
\]

After exact prestripping, a full Rosser modulus carries an odd anchor divisor

\[
e\mid P(23)
\]

and canonical long/short hard factors `m,n`. Its full level condition is

\[
\boxed{emn<D.}
\tag{TT2}

But (TT1) gives

\[
mn>rac{25}{36}BN_0
=rac{25}{36}D.
\]

Every nontrivial odd divisor of `P(23)` is at least `3`. Hence if `e>1`,

\[
emn>3\frac{25}{36}D
=rac{25}{12}D>D,
\]

contradicting (TT2). Therefore

\[
\boxed{
\text{on the complete top×top block, }e=1\text{ is forced.}
}
\tag{TT3}

So the generic `2^8=256` possible anchor labels do **not** occur here at all. This is a level-geometry fact, not a cancellation estimate.

---

## 3. Long and short supports

The latest q-binned Brun–Titchmarsh support theorem proves

\[
\frac{A_M}{(5/6)B}
<
\frac{537427837}{36960000000}
<rac3{200}.
\]

Since

\[
\frac3{200}\frac56=rac1{80},
\]

we have

\[
\boxed{A_M<\frac{B}{80}.}
\tag{TT4}

For `j=1`, the hard inner primes lie in the range `29..1439`, and the canonical short suffix contains at most two such primes. Exact enumeration in the symbolic top block

\[
\frac56W^{1/4}<n\le W^{1/4}
\]

gives

\[
\boxed{B_N=185.}
\tag{TT5}

The companion checker recomputes this count from the 219 hard primes rather than importing a decimal approximation to `N_0`.

---

## 4. Direct sharp-carry bound

For the sharp anchored interval every one-dimensional floor/carry discrepancy satisfies

\[
|e(q)|<1.
\]

The corrected residual ordered-pair kernel satisfies

\[
\kappa(u,t)\le\frac{73}{80},
\]

and the source outside denominator is

\[
\Delta=2c-b-1=\frac{93}{20}.
\]

By (TT3), every top×top supported modulus has one anchor label only. Therefore absolute summation gives

\[
|R_{11}^{\rm top\times top}|
<
\frac1\Delta
\frac{73}{80}
A_M B_N.
\]

Using (TT4), (TT5) and the certified integer upper bound

\[
B<494793856728460,
\]

we obtain

\[
\frac{|R_{11}^{\rm top\times top}|}{L_{23}}
<
\frac{20}{93}
\frac{73}{80}
\frac{494793856728460}{80}
\frac{185}{232018561402828200}.
\]

The companion exact rational checker proves

\[
\boxed{
\frac{|R_{11}^{\rm top\times top}|}{L_{23}}
<
\frac1{1000}.
}
\tag{TT6}

For orientation only, the rational upper bound is approximately

\[
9.6775011329\times10^{-4}.
\]

The decimal is not used in the proof.

---

## 5. Consequence

This closes one full block of the only large residual valuation shell without any analytic cancellation machinery:

\[
\boxed{
\text{j=1 top long}\times\text{top short}
\Longrightarrow
R/L_{23}<10^{-3}.
}
\]

The reason is the combination of three independent exact reductions:

1. q-binned Brun–Titchmarsh reduces the long support below `1.5%`;
2. the canonical suffix factorization leaves exactly 185 top short states;
3. the full Rosser level forces the P(23) anchor divisor to be `e=1` on top×top.

This certificate does **not** bound lower long/short geometric blocks, the `j=2` 254-state correction, or the finite source-main normalization. It therefore does not close the full `T1–T2` remainder and does not prove a finite P2 theorem.

---

## 6. Next

The level argument behind (TT3) generalizes. If disjoint geometric blocks are indexed by

\[
\frac{B}{\rho^{i+1}}<m\le\frac{B}{\rho^i},
\qquad
\frac{N_0}{\rho^{j+1}}<n\le\frac{N_0}{\rho^j},
\qquad \rho=\frac65,
\]

then

\[
mn>\frac{D}{\rho^{i+j+2}},
\]

so every anchor label satisfies

\[
\boxed{e<\rho^{i+j+2}.}
\]

Thus the 256-anchor family turns on gradually with block depth. The next correct task is to freeze this anchor-depth filtration and combine it with exact short-state counts and long-support bounds before deciding where Cauchy/Fourier is genuinely still required.
