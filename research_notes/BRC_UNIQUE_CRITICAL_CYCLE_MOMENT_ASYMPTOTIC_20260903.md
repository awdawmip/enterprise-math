# BRC Unique-Critical-Cycle Large-Moment Recurrent Asymptotic

Status: `RESEARCH CANDIDATE / EXACT FINITE EXPLICIT POSITIVE-RATIONAL / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCFB-93C7D1`
Parents: `WBRC-T33`, `WBRC-T36..T38`, existing max-plus/idempotent path closure principles

## 1. Purpose and prior-art boundary

For explicit positive-rational branches, the moment matrices

\[
W_m:=W^{(m)},\qquad (W_m)_{ij}=\sum_{e:i\to j}q_e^m
\]

interpolate between count, total mass and the tropical/dominant regime.

The leading large-`m` statement

\[
\rho(W_m)^{1/m}\to \mu,
\]

where `mu` is the maximum cycle geometric mean of the entrywise dominant-weight graph, belongs to classical max-algebra / Perron-Frobenius dequantization theory. Max-plus critical graphs and critical classes are classical as well.

The BRC-specific question here is the **first exact multiplicity correction** supplied by the histogram quotient `Lead=(M,d)` when there is one isolated critical simple cycle.

No generic max-plus/Perron novelty claim is made.

## 2. Dominant edge graph

For each supported ordered state pair `i->j`, let

\[
a_{ij}=\max\{q_e:e:i\to j\}>0
\]

and

\[
d_{ij}=\#\{e:i\to j:q_e=a_{ij}\}.
\]

Thus

\[
(W_m)_{ij}
=d_{ij}a_{ij}^m+
\sum_{q<a_{ij}}c_{ij,q}q^m.
\]

For every directed simple state cycle `C`, define

\[
Q_C=\prod_{(i,j)\in C}a_{ij},
\qquad
\mu_C=Q_C^{1/|C|}.
\]

Let

\[
\mu=\max_C\mu_C.
\]

## 3. Exact unique-critical hypothesis

Assume there is exactly one directed simple cycle `C_*` attaining `mu`.
Let

\[
r=|C_*|,
\qquad
Q=Q_{C_*},
\qquad
D=\prod_{(i,j)\in C_*}d_{ij}.
\]

Because the finite graph has finitely many simple cycles, uniqueness is equivalent to a strict exact rational gap certificate:

\[
\boxed{
Q_C^{\,r}<Q^{\,|C|}
\quad\text{for every simple cycle }C\ne C_*.
}
\]

No root evaluation is required to certify this condition.

## 4. Characteristic coefficients as exponential rational sums

Write

\[
p_m(\lambda)=\det(\lambda I-W_m).
\]

The standard directed cycle-system determinant expansion gives

\[
p_m(\lambda)
=
\sum_F(-1)^{c(F)}
\lambda^{n-|V(F)|}
\prod_{(i,j)\in F}(W_m)_{ij},
\]

where `F` ranges over vertex-disjoint directed cycle systems and `c(F)` is the number of cycles.

Expanding each matrix entry into its explicit parallel branches gives every characteristic coefficient the form

\[
\boxed{
a_{k,m}=\sum_{b\in B_k}c_{k,b}b^m,}
\]

with a finite set `B_k subset Q_{>0}` and integer coefficients `c_{k,b}`.

This is an exact finite exponential-sum representation; no floating eigenvalue is used.

## 5. Unique dominant characteristic monomial

For a cycle system `F` occupying `k` vertices, each constituent simple cycle has mean at most `mu`. Therefore every explicit branch-selection base `b` occurring in its product obeys

\[
b\le\mu^k.
\]

In exact root-free form,

\[
\boxed{b^r\le Q^k.}
\]

If equality holds, every selected branch must be dominant on its state edge and every constituent simple cycle must itself be critical.

Under the unique-critical hypothesis this forces

\[
F=C_*,\qquad k=r.
\]

The dominant branches along `C_*` can be chosen independently in

\[
D=\prod_{e\in C_*}d_e
\]

ways, all with the same rational product `Q`. Hence the characteristic coefficient at `lambda^(n-r)` contains the unique maximal exponential base `Q` with exact coefficient

\[
\boxed{-D.}
\]

Every other nonconstant cycle-system base satisfies a strict exact inequality

\[
b^r<Q^k.
\]

## 6. Normalized characteristic-polynomial limit

Set formally

\[
\lambda=\mu^m t,
\qquad \mu=Q^{1/r}.
\]

Then

\[
\mu^{-mn}p_m(\mu^m t)
\longrightarrow
\boxed{t^{n-r}(t^r-D)}
\]

coefficientwise, hence uniformly on compact subsets of the finite-dimensional polynomial space.

The nonzero limiting roots have modulus `D^(1/r)`; the positive one is `D^(1/r)`.

The ordinary Perron root `rho_m=rho(W_m)` is nonnegative. The critical-cycle principal submatrix gives

\[
\rho_m^r\ge\prod_{e\in C_*}(W_m)_e,
\]

and therefore

\[
\liminf_{m\to\infty}\frac{\rho_m^r}{Q^m}\ge D.
\]

Together with characteristic-root continuity and the normalized polynomial limit, this identifies the positive Perron branch uniquely.

### Candidate BRC-UC1

\[
\boxed{
\lim_{m\to\infty}
\frac{\rho(W^{(m)})^r}{Q^m}
=D.
}
\]

Equivalently,

\[
\boxed{
\frac{\rho(W^{(m)})}{\mu^m}
\to D^{1/r}.
}
\]

## 7. Derived logarithmic asymptotic

Taking logarithms only as a derived readout,

\[
r\ln\rho(W^{(m)})
=m\ln Q+\ln D+o(1).
\]

Thus

\[
\boxed{
\ln\rho(W^{(m)})
=m\ln\mu+\frac1r\ln D+o(1).
}
\]

The first term is the classical tropical/max-cycle exponent. The second is the BRC dominant-degeneracy correction inherited from `Lead=(M,d)`.

For a one-state family with largest loop weight `q` occurring `d` times,

\[
r=1,\quad Q=q,\quad D=d,
\]

and this reduces exactly to the earlier histogram asymptotic

\[
\ln P_m=m\ln q+\ln d+o(1).
\]

For `k` equal loops it gives the existing `m ln q + ln k` law.

## 8. Why the correction is a cycle product

Along the unique critical cycle, each edge-level leading pair is

\[
(a_e,d_e).
\]

Serial multiplication in the leading-pair semiring yields

\[
\prod_{e\in C_*}(a_e,d_e)
=
(Q,D).
\]

Hence the recurrent subleading constant is exactly the multiplicity coordinate of the critical circuit in the `Lead` quotient.

This is the recurrent analogue of finite-path dominant degeneracy.

## 9. Important negative boundaries

### 9.1 Multiple critical cycles

If more than one simple state cycle attains `mu`, the limiting normalized characteristic polynomial can contain several nonvanishing cycle-system terms. A single product `D` attached to one cycle is then not a complete correction.

The correct multi-critical object is expected to depend on the full critical leading-pair graph / a critical multiplicity matrix, not on one scalar degeneracy product. This note does not promote that extension.

### 9.2 Edge-level CWM is insufficient

CWM records each edge-cell maximum mass but not its dominant tie multiplicity. Two explicit branch systems can therefore have the same total/dominant edge matrix yet different `D` and different recurrent subleading asymptotic.

### 9.3 No floating spectral primitive

The theorem statement may use the classical Perron root as an observable, but the Enterprise certificate surface is:

- exact rational dominant edge weights;
- exact integer dominant multiplicities;
- exact simple-cycle products;
- root-free critical-gap inequalities;
- exact characteristic coefficient exponential-base decomposition.

Floating eigensolvers are not proof certificates.

## 10. Validation plan

1. Enumerate small explicit positive-rational multigraphs and identify all simple state cycles from exact dominant edge weights.
2. For every unique-critical sample, verify the root-free gap inequalities `Q_C^r<Q^|C|` exactly.
3. Build characteristic coefficients as exact dictionaries `base rational -> integer coefficient` by explicit cycle-system/branch expansion.
4. Verify the unique equality pattern: only degree `n-r` has a base satisfying `b^r=Q^r`, namely `b=Q`, with coefficient `-D`; every other nonconstant base is strict.
5. Test concrete two-/three-state examples with rational `mu` and rational predicted `D^(1/r)` using exact characteristic-polynomial sign brackets around the normalized Perron root for increasing `m`.
6. Include a multi-critical counterexample showing that selecting one cycle's `D` is insufficient.
