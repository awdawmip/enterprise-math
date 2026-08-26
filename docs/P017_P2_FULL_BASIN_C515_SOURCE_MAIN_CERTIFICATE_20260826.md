# P017 — Full-Basin c=103/20 Source-Main Certificate

Status: `PROVED_WIP SOURCE-DECIMAL MAIN ENCLOSURE + FORMAL FINITE BUDGET / NOT YET FINITE MAIN NORMALIZATION / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Companion checker:

`experiments/p017_p2_full_basin_c515_source_main_certificate_20260826.py`

Depends on:

- the Iwaniec–Laborde 1981 simplified `a=6`, `b>=3` main formula on p.53;
- `docs/P017_P2_A6_FIVE_NINTH_ROOT_EDGE_PACKAGE_20260826.md` for the source-decimal provenance convention;
- `docs/P017_P2_FULL_BASIN_LOWER_ROSSER_SUPPORT_20260826.md`;
- `docs/P017_P2_FULL_BASIN_C515_TERMINAL_T4_CERTIFICATE_20260826.md`.

Purpose: certify the source main coefficient for the finite-oriented rational terminal packet

\[
\boxed{
a=6,\qquad b=\frac{93}{20},\qquad c=\frac{103}{20},\qquad d=\frac59.
}
\]

This note freezes the source-asymptotic coefficient and a bookkeeping budget. It does **not** yet replace the source `epsilon` / Mertens normalization by a fully finite main-term inequality.

---

## 1. Terminal-complete split

The parameter relation is

\[
b+c=\frac{49}{5},
\qquad
b+c+1=\frac{54}{5}=\frac a d.
\]

Set the analysis split exactly at the selected terminal horizon. In the p.53 notation this means

\[
\frac1{1+\alpha}=\frac c6.
\]

Hence

\[
\alpha=\frac{6-c}{c},
\]

and exactly

\[
\boxed{
\frac6{1+\alpha}=c,
\qquad
\frac{6\alpha}{1+\alpha}=6-c.
}
\]

Therefore the near-terminal quadratic mismatch appearing in the generic short-interval specialization vanishes. The nonconstant source bracket becomes

\[
N_c
=-\frac c6\log c
-\frac{6-c}{6}\log(6-c).
\]

---

## 2. Eliminate B2 by the published reference point

Use the same source-decimal convention as the frozen a6 root-edge packet:

\[
5.1828\le c_0\le5.1829,
\]

\[
4.8698\le b_0\le4.8699,
\]

\[
0.00177\le G_0\le0.00178,
\]

where the ellipses printed in Iwaniec–Laborde are interpreted as prefix intervals.

The first-order condition reconstructs `B_1` with the already-frozen enclosure

\[
0.2433070897\ldots<B_1<0.2433605490\ldots.
\]

Subtracting the published reference identity eliminates `B_2`. Thus

\[
\boxed{
G_c
=G_0
+B_1\bigl[(c-b)-(c_0-b_0)\bigr]
+N_c-N_0.
}
\]

Every logarithm is enclosed by exact rational atanh series arithmetic.

---

## 3. Certified source coefficient

For

\[
c=\frac{103}{20},
\qquad
b=\frac{93}{20},
\]

the exact interval checker gives

\[
0.0760510693\ldots
<G_c
<0.0761692657\ldots.
\]

In particular,

\[
\boxed{
G_c>\frac{19}{250}=0.076.
}
\tag{C515-M1}
\]

This is the finite-oriented counterpart of the root-edge source-decimal bracket `G_*>0.1148`: lowering the terminal horizon sacrifices some asymptotic main coefficient in exchange for a much cheaper terminal Rosser remainder.

---

## 4. Source main scale at the Tier-A full basin

Let

\[
W=K_0+1,
\qquad
D=W^{10/9}.
\]

The p.53 simplified lower bound carries the outside factor

\[
\frac{12}{(2c-b-1)\log D}.
\]

Here

\[
2c-b-1=\frac{93}{20}.
\]

Using the lower bound (C515-M1) together with an exact rational upper enclosure for `log D`, the checker proves

\[
\boxed{
\frac{12G_c}{(2c-b-1)\log D}
>\frac{449}{100000}=0.00449.
}
\tag{C515-M2}
\]

This is a **source-asymptotic main scale**. The source's finite `epsilon` term and finite Mertens normalization have not yet been charged, so (C515-M2) must not be read as a completed finite lower bound for `W(A)`.

---

## 5. Formal budget after the two rigorous carry errors

Two finite carry terms are already rigorous at the Tier-A splice:

\[
\frac{|R_0^-|}{L}<0.00145,
\]

and

\[
\frac{|R_{T_4}|}{L}<0.00125.
\]

Therefore, before charging the still-unresolved source-main finite normalization and `T1–T3`, the certified source-scale budget is

\[
\boxed{
0.00449-0.00145-0.00125
=0.00179.
}
\tag{C515-M3}
\]

Thus the next hard target is quantitative and small:

> the sum of `T1–T3` remainder costs plus all finite source-main normalization losses must be driven below `0.00179 L`.

The previous vague goal “make the bilinear constant explicit” has now been replaced by this concrete budget.

---

## 6. Route consequence

The rational packet

\[
\boxed{b=93/20,\qquad c=103/20}
\]

remains the preferred finite candidate after rigorous terminal certification:

- base lower Rosser carry: `<0.00145 L`;
- terminal `T4` carry: `<0.00125 L`;
- source main scale: `>0.00449 L` before finite source normalization;
- formal unspent budget: `>0.00179 L`.

The next work should not return to the root-edge `c=5.4` package merely because its asymptotic `G` is larger. It should attack `T1–T3` using their actual prime-dependent Rosser supports and simultaneously make the remaining p.53 main normalization finite.

No finite analytic P2 threshold, P2-in-every-square theorem, Legendre theorem, or canonical promotion is claimed here.
