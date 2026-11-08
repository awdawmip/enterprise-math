# PREFIX-603-R2 — Sharp recurrence on the actually reachable native 96-port BRC one-step image

2026-11-08 · Author-side exact proof and independent exact SymPy certificate · Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Continues PREFIX-599/601/602. P000 and ACTIVE worldview unchanged.

## Exact object

The native typed X6-BRC operator `A(z)` acts on 96 original bit-ports, defined from 48 original STAR triple phases, three successor phases per row, and four labeled original source/destination bit-port actions. It contains 576 typed original actions before setting the six axis weights to `(1,1,1,1,0,0)`. Its unique native gate target phase is `g=4`: the typed transition targeting phase `g` from bit 1 to bit 1 carries gate weight `z`; all other typed actions carry weight 1 before axis weighting. We work with **all real nonnegative z**.

Retain the previously established **first-step** 48-phase encoder `C` (sum of the two native ports for each phase except at g, where only bit 0 is retained) and its native port embedding `E` (phase j -> native bit 0 for j!=g, phase g -> both native bits). Set

\[
F(z)=C A(z):\mathbb R^{96}\to\mathbb R^{48},\qquad Q(z)=F(z)E=C A(z)E.
\]

The full 48-phase observer after an arbitrary native first step is `v_1=F(z)r_0`; further stationary evolution is `v_{n+1}=Q(z)v_n`. The original 96-port observation recovery follows PREFIX-595/596's explicitly scoped factorization. These are 48-component internal state coordinates, **not** a change in the P000 six-dimensional native spatial ontology or a declaration of physical time length.

## Theorem 1: exact source image rank

For every real `z>=0`,

\[
\boxed{\operatorname{rank} F(z)=\operatorname{rank}Q(z)=32,\quad\operatorname{im}F(z)=\operatorname{im}Q(z).}
\]

**Proof.** The frozen STAR combinatorics sets 16 complete rows of `F` to zero because their final native axis is 5 or 6 under the specified zero-axis weights. Hence `rank F<=32`. The exact typed native formula gives `Q=FE`, so `rank Q<=rank F` and `im Q\subseteq im F`. Select the 32 independent rows/columns from the exact z=2 integer pivot computation; the determinant of the corresponding 32×32 polynomial minor of `Q(z)` is

\[
\boxed{7044820107264(z+3)}.
\]

This is strictly nonzero for all z>=0, so `rank Q>=32`, proving equality and the image statement. The checker verifies all 48×48 entries of `Q=FE`, the 16 vanishing native rows, and the symbolic minor identity.

## Theorem 2: sharp accessible minimum polynomial

Define the least monic polynomial annihilating **every actually reachable post-first-step state** `F(z)r_0` under subsequent `Q(z)` evolution. For all real z>=0 it is

\[
\boxed{
\mu_{Q\mid\operatorname{im}F}(t)=
\begin{cases}
t(t^4-16), & z=1\quad(\deg=5),\\
t(t^4-16)(t^4-(4z+12)), & z\ne1\quad(\deg=9).
\end{cases}}
\]

This strengthens the earlier sharp full 48-phase matrix minimal-polynomial degrees 6 and 10 by one degree **for every original 96-port source**, regardless of the signs of its linear coordinates. The statement applies to arbitrary integer numbers of further stationary native typed BRC steps.

**Proof.** The original 48-phase exact matrix identities from PREFIX-599 were recomputed:

\[
Q^2(Q^4-16I)(Q^4-(4z+12)I)=0,\qquad Q(1)^2(Q(1)^4-16I)=0.
\]

As `im F=im Q`, divide each annihilator by one factor `t` after acting on a vector in `im Q`. This gives upper polynomials of degrees 9 and 5. Sharpness is witnessed by the **nonnegative original bit-port** input `r_0=e_{16}\in\mathbb R^{96}_{>=0}`. Its native first-step encoded state is

\[
F(z)e_{16}=2e_2+2e_{14}+2e_{15}\quad \text{for all }z\ge0.
\]

For the 48×9 Krylov matrix `K=[v,Qv,...,Q^8v]` with `v=F(z)e16`, the determinant on exact rows `(2,3,4,5,14,16,17,26,27)` is

\[
\boxed{-34359738368(z-1)^4(z+3)}.
\]

This is nonzero for all `z>=0,z!=1`, proving degree at least 9. At z=1, the exact rank of the corresponding five-column Krylov matrix is 5, achieving the other sharp bound. Thus both polynomials are **exact minimum polynomials on the reachable image**.

## Theorem 3: a strict original-source nonnegative reachability obstruction

For each native raw port basis input, its 48-phase first-step image column in `F(z)` is either identically zero or has **exactly three strictly positive phase coordinates**, for every real z>=0. The exhaustive native typed-graph column count is `32` zero columns and `64` three-supported columns; the symbolic entries in nonzero columns are strictly positive throughout the nonnegative domain.

Consequently, for every native nonnegative original input `r_0>=0`, if `F(z)r_0\ne0` then it has **at least three nonzero phase coordinates**. In particular the exactly two-phase nonnegative vectors from PREFIX-602 (e.g. `e0+e36`, `e0+e18`, `e0+e4`, `e8+e11`) are **not first-step reachable from a nonnegative original 96-port input** under this frozen zero-axis native model. Their exact formal right-phase recurrence theorems remain valid in that observer class; the present theorem selects original-source realizations without conflating the classes.

The script checks each entry of `F=C A`, the original 576 typed source actions, support at z=0,1,2 with the exact symbolic positivity classification, and verifies sharp original raw-port Krylov rank distributions:

| exact degree of post-step reachable state | z=1: original bit ports | z=2: original bit ports |
|---:|---:|---:|
| 0 (zero state) | 32 | 32 |
| 4 | 32 | 32 |
| 5 | 32 | 16 |
| 9 | 0 | 16 |
| **total** | **96** | **96** |

The single-port table is a finite exact census at two specified gates; Theorems 1–3 are for **all** z>=0.

## Why this matters and next research unit

For the original 96-port source family, sharp recurrence order is 5 at gate unity, and 9 at other nonnegative gates after first-step encoding. The 3-supported native source `e16` realizes the 9-order bound. This gives a stronger, source-respecting fast-jump interface than an arbitrary 48-phase 10-order algorithm and identifies exactly why some dramatic two-phase formal compression examples cannot be directly invoked as positive original-source accelerations.

Next: (i) classify **nonnegative native 96-port mixtures** by minimal recurrence and common primary support; (ii) implement shared preprocessing and endpoint recovery to measure full input/output and integer-bit complexity for stationary long-depth batch queries; (iii) analyze time-varying gates separately, since a stationary matrix polynomial does not apply to arbitrary noncommuting parameter sequences. Preserve all native source branches and joint observations where requested. No native Result, independent Driver review, or physically measured heartbeat claims are made.

**Exact evidence:** `PREFIX603_R2_native_reachable_tail_checker.py` (independent reconstruction of original typed 96-port actions, source encoding and symbolic certificates), `PREFIX603_R2_native_reachable_tail_results.json`. Author-side assertions passed with exact SymPy polynomial and integer arithmetic.
