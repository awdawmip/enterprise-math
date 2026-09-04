# Free Research — `S_3` Provenance Mixer and the Standard-Sector Gap

Status: `FREE_RESEARCH_FRONTIER / EXACT_FINITE_MIXER_GAP / DEGREE_THREE_SPECIAL / NATIVE_IMPLEMENTATION_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION / EXTERNAL_NOVELTY_UNVERIFIED`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PRIME_WINDING_ORDERED_CUBIC_CURVATURE_20260904.md`

## 1. Executive advance

The ordered cubic curvature note identifies quotient-cloud variance with the antisymmetric sector of three-history closing-edge readouts.  This note identifies an exact finite mixer on the same `3!` provenance fiber.

Uniform averaging over the three position transpositions of `S_3`

\[
(12),\qquad(13),\qquad(23)
\]

annihilates the entire standard representation in one step while preserving the trivial component.  For endpoint-symmetric closing-edge readouts, the sign component is absent.  Therefore the mixer is the exact orthogonal projection onto the common recoalesced amplitude.

Consequently, the weighted quotient-cloud variance is exactly the Dirichlet dissipation of this six-history mixer.

---

## 2. Six ordered histories over one product endpoint

Fix three action labels `a,b,c`.  All six permutations have the same total quotient endpoint

\[
q_{abc}(n).
\]

Write

\[
x_a=f(q_a(n)),\qquad
x_b=f(q_b(n)),\qquad
x_c=f(q_c(n)),
\]

and

\[
z=f(q_{abc}(n)).
\]

For an ordered history `sigma in S_3`, define the direct closing-edge readout

\[
H(\sigma)=x_{\sigma(1)}+z.
\tag{2.1}
\]

Thus the six values are

\[
x_a+z,\ x_a+z,\ x_b+z,\ x_b+z,\ x_c+z,\ x_c+z.
\]

The readout depends only on the first action and the common endpoint.

---

## S3M-T01 — Representation decomposition

Let

\[
\bar x=\frac{x_a+x_b+x_c}{3},
\qquad
\bar H=z+\bar x.
\]

The `S_3` history space contains the trivial, sign, and standard representations.  For the readout (2.1):

1. the trivial component is the mean `bar H`;
2. the sign component vanishes, because exchanging the final two positions leaves `H` unchanged;
3. all nontrivial content lies in the two-dimensional standard representation.

The exact standard-sector norm is

\[
\boxed{
\sum_{\sigma\in S_3}|H(\sigma)-\bar H|^2
=2\sum_{j\in\{a,b,c\}}|x_j-\bar x|^2
}
\tag{3.1}
\]

or equivalently

\[
\boxed{
\sum_{\sigma\in S_3}|H(\sigma)-\bar H|^2
=\frac23\left(
|x_a-x_b|^2+|x_b-x_c|^2+|x_c-x_a|^2
\right).
}
\tag{3.2}
\]

---

## S3M-T02 — Uniform transposition mixer

Let `P_ij` permute history positions `i,j`, and define

\[
\boxed{
\mathsf M_3
:=\frac13(P_{12}+P_{13}+P_{23}).
}
\tag{4.1}
\]

For a history whose first action is `a`, the three transpositions send the first slot respectively to `b`, `c`, and `a`.  Hence

\[
(\mathsf M_3H)(\sigma)
=z+\frac{x_a+x_b+x_c}{3}
=\bar H
\]

for every `sigma`.

Therefore

\[
\boxed{
\mathsf M_3H=\Pi_{\rm triv}H,
\qquad
\mathsf M_3|_{\rm std}=0.
}
\tag{4.2}
\]

The standard-sector spectral gap is exactly `1`.

The associated Dirichlet form is

\[
\boxed{
\langle H,(I-\mathsf M_3)H\rangle
=\sum_{\sigma}|H(\sigma)-\bar H|^2.
}
\tag{4.3}
\]

Since each transposition is an involutive isometry,

\[
\boxed{
\langle H,(I-\mathsf M_3)H\rangle
=\frac16\sum_{t\in\{(12),(13),(23)\}}
\|H-P_tH\|^2.
}
\tag{4.4}
\]

Thus the entire nontrivial history content is dissipated by one symmetric transposition-averaging step.

---

## S3M-T03 — Global weighted variance identity

Let `S` be a finite action set with positive weights `u_a`, and let

\[
U=\sum_a u_a.
\]

For each ordered triple `(a,b,c)`, construct its six-history readout as above.  Summing the local standard energy with weight `u_au_bu_c` yields

\[
\boxed{
\sum_{a,b,c}u_au_bu_c
\langle H_{a,b,c},(I-\mathsf M_3)H_{a,b,c}\rangle
=4U^2\Gamma_S(f;n).
}
\tag{5.1}
\]

Therefore

\[
\boxed{
\Gamma_S(f;n)
=\frac1{4U^2}
\sum_{a,b,c}u_au_bu_c
\langle H_{a,b,c},(I-\mathsf M_3)H_{a,b,c}\rangle.
}
\tag{5.2}
\]

Equivalently, by (4.4),

\[
\boxed{
\Gamma_S(f;n)
=\frac1{24U^2}
\sum_{a,b,c}u_au_bu_c
\sum_t\|H_{a,b,c}-P_tH_{a,b,c}\|^2.
}
\tag{5.3}
\]

For the prime-power weights `u_a=Lambda(a)/a`, permutation of the three action labels preserves the product measure exactly.  Hence `M_3` is measure-preserving on the arithmetic cubic history packet.

---

## S3M-T04 — Why degree three is special

The construction extends to `r!` ordered histories.  Let

\[
H_r(\sigma)=x_{\sigma(1)}+z,
\qquad \sigma\in S_r,
\]

and average uniformly over all position transpositions:

\[
\mathsf M_r
=\binom r2^{-1}\sum_{1\le i<j\le r}P_{ij}.
\]

On the standard representation,

\[
\boxed{
\mathsf M_r|_{\rm std}
=\lambda_r I,
\qquad
\lambda_r=\frac{r-3}{r-1}.
}
\tag{6.1}
\]

This follows directly from the first-slot action.  For a zero-mean vector `(x_1,...,x_r)`, a transposition not involving slot `1` leaves `x_1` unchanged, while the `r-1` transpositions involving slot `1` replace it by one of the other coordinates.  The average is

\[
\frac{\binom{r-1}{2}x_1+\sum_{j\ne1}x_j}{\binom r2}
=\frac{r-3}{r-1}x_1.
\]

Hence the standard-sector gap is

\[
\boxed{
1-\lambda_r=\frac2{r-1}.
}
\tag{6.2}
\]

The cases are revealing:

- `r=2`: `lambda_2=-1`; the two-history fiber only reverses the fluctuation and has no mixing contraction under iteration;
- `r=3`: `lambda_3=0`; one step annihilates the standard component exactly;
- `r>3`: `0<lambda_r<1`; the standard component contracts, but less strongly.

Thus degree three is the unique smallest factorial provenance degree at which symmetric transposition averaging is both aperiodic and an exact one-step projection on the first-history fluctuation sector.

---

## S3M-T05 — General factorial-standard energy law

For one `r`-tuple of action labels, the `r!` readout norm is

\[
\boxed{
\sum_{\sigma\in S_r}|H_r(\sigma)-\bar H_r|^2
=(r-1)!\sum_{j=1}^r|x_j-\bar x|^2.
}
\tag{7.1}
\]

Averaging over independently weighted action labels gives

\[
\boxed{
\sum_{a_1,\ldots,a_r}
\left(\prod_j u_{a_j}\right)
\|H_r-\bar H_r\|^2
=(r-1)(r-1)!U^{r-1}\Gamma_S(f;n).
}
\tag{7.2}
\]

The transposition Dirichlet dissipation is therefore

\[
\boxed{
\sum_{a_1,\ldots,a_r}
\left(\prod_j u_{a_j}\right)
\langle H_r,(I-\mathsf M_r)H_r\rangle
=2(r-1)!U^{r-1}\Gamma_S(f;n).
}
\tag{7.3}
\]

At `r=3`, this reduces to (5.1).

---

## 8. Consequence and boundary

The existence of a gap-one mixer means the finite six-history fiber already contains a perfect fluctuation-removal operator.  However, this does not yet prove a new quantitative bound for `psi(x)-x`.

The remaining implementation question is substantive:

> Is uniform transposition averaging on the six ordered quotient histories generated by, or admissibly equivalent to, a primitive Enterprise rotation/branch-recoalescence operation that occurs with controlled positive mass in the arithmetic dynamics?

If yes, the standard-sector variance would be dissipated exactly before product-label recoalescence.  If not, `M_3` remains an externally imposed symmetrizer and cannot by itself improve the PNT remainder.

The important correction is that the spectral-gap problem is no longer abstract: the candidate operator, its invariant measure, its spectrum, and its exact Dirichlet form are all explicit and finite.

---

## 9. Exact checker

The script

- `scripts/check_free_research_s3_provenance_mixer.py`

verifies with exact rational arithmetic:

1. the local `S_r` first-slot action;
2. the eigenvalue `(r-3)/(r-1)` through degree eight;
3. vanishing of the sign projection;
4. the local standard norm formula;
5. the transposition Dirichlet identity;
6. the global weighted cubic variance law;
7. the general factorial-standard energy law through degree five.

No numerical prime-distribution input is used.

---

## 10. Updated next target

The next finite theorem should choose between two outcomes:

1. **native realization:** construct `M_3` as an exact allowed branch mixer on the six-history provenance fiber and prove that its denotation preserves the fine reachable support while dissipating only the standard fluctuation sector; or
2. **no-go:** prove that the current deterministic primitive operations cannot realize convex transposition averaging without an explicit weighted-branch state extension.

Either result would sharply determine whether the `3!` provenance fiber can support a genuinely native quantitative prime-remainder mechanism.
