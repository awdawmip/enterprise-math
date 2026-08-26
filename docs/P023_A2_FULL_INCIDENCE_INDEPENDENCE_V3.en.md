# P023 / A2 — Full-Incidence Independence, v3 Supplement

Status: `PROVED OWNER RESEARCH`  
Owner: A2 future-compatible quotient  
Depends on: A2 Precision Incidence Core v3

## 1. Definition

Let `X` be finite and let `E_1,...,E_m` be finite task partitions, with `n_i=|X/E_i|`. Call the family **full-incidence independent** when the joint block map is surjective:

\[
\boxed{X\longrightarrow\prod_{i=1}^m X/E_i\quad\text{is onto}.}
\]

Equivalently,

\[
\boxed{|X/(\cap_iE_i)|=\prod_i n_i.}
\]

This is a deterministic finite realization property, not probabilistic independence.

## 2. Every subfamily also realizes its full product

For every coordinate subset `S`,

\[
\boxed{|X/E_S|=\prod_{i\in S}n_i,\qquad E_S=\bigcap_{i\in S}E_i.}
\]

This follows by projecting the fully realized tuple set onto the selected coordinates.

## 3. Exact directed repair formula

For any coordinate subsets `S,T`,

\[
\boxed{\rho(E_S,E_T)=\prod_{i\in T\setminus S}n_i.}
\]

After fixing one realized `S`-tuple, every assignment to the genuinely new coordinates `T\S` remains realized by full-product surjectivity.

## 4. Uniform repair spectrum

Every `E_S` block has the same split multiplicity

\[
r_{S,T}=\prod_{i\in T\setminus S}n_i,
\]

and there are `prod_{i in S} n_i` such blocks. Therefore

\[
\boxed{\mathcal R_k(E_S,E_T)=\left(\prod_{i\in S}n_i\right)\binom{r_{S,T}}k.}
\]

The entire local repair-size distribution is uniform.

## 5. Scheduling becomes order-independent

If primitive tasks are acquired one at a time, every not-yet-retained task `i` costs exactly `n_i` repair symbols. Hence every order `sigma` has

\[
\boxed{P_\sigma=\prod_i n_i=|X/(\cap_iE_i)|.}
\]

Incidence-capacity slack is zero. Fixed-base total symbol cost `sum_i L_B(n_i)` is also order-independent. If every `n_i>=2`, zero-cost dependency closure is trivial.

## 6. Binary case: exact Hamming precision geometry

If every `n_i=2`, then

\[
\boxed{\rho(E_S,E_T)=2^{|T\setminus S|}.}
\]

For base two,

\[
\boxed{d_2(E_S,E_T)=|T\setminus S|,\qquad D_2(E_S,E_T)=|S\triangle T|.}
\]

Thus subset-generated precision states form the exact `m`-dimensional Hamming cube. The primitive-distance-one graph is `Q_m`; radius-`r` spheres have size `binom(m,r)`, and two vertices at distance `r` have `r!` shortest coordinate-flip geodesics.

These are standard hypercube facts. A2 supplies the exact reduction from repair geometry to that normal form.

## 7. Pairwise completeness is not enough

For `m>=3`, pairwise complete incidence does not imply full-incidence independence. The even-parity/full-cube eight-state counterexample has identical complete pairwise binary incidence in both systems, while only one realizes the full three-dimensional product.

Therefore full-product independence is genuinely higher-order.

## 8. Program consequence

Whenever a program proves that a finite family of binary tasks realizes every binary pattern, all A2 repair/scheduling geometry on that family immediately takes the Hamming normal form above.

P017's fixed finite least-prime split-bit families are one number-theoretic candidate specialization once their finite-pattern realization theorem is supplied.

## 9. Executable specification

- `src/enterprise_math/a2_full_incidence.py`
- `tests/test_a2_full_incidence_independence.py`

The tests cover heterogeneous finite alphabets, exact product repair factors, uniform repair spectra, and the binary Hamming formulas.
