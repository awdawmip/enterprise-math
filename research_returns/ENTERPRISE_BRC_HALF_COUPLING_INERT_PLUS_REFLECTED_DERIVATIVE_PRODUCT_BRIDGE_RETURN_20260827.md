# Enterprise BRC Half-Coupling Inert Plus Reflected Derivative Product Bridge — Research Return

Status: `FINAL_FROZEN / EXACT_SECOND_ORDER_REDUCTION / PROOF_NOT_CLOSED_WITH_SMALLER_IDENTITY`

Date: `2026-08-27`

Researcher-ID: `EM-EBP4P-6D8A31`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-REFLECTED-DERIVATIVE-PRODUCT-BRIDGE`

Publication: `TP2-17FC09F805797C961013`

Claim: `chatgpt-ebp4p-20260827-1953-6d8a31`

Execution: `ER-1A1992ADA63C4AACE014`

## 1. Frozen verdict

`PRIMARY_VERDICT = PROOF_NOT_CLOSED_WITH_SMALLER_IDENTITY`.

`HARD_TARGET_DISPOSITION = ACHIEVED_BY_EXACT_SECOND_ORDER_PARAMETER_DEFORMATION_REDUCTION`.

No counterexample was found for either `p ≡ 13 (mod 24)` or `p ≡ 19 (mod 24)`. The all-prime product congruence is not claimed proved here.

The exact advance is stronger than another finite check and strictly smaller than the parent unresolved interface: the reduced product congruence

\[
G_pH_p\equiv p+p^2R_p\pmod{p^3}
\tag{L+}
\]

is converted into one finite second-order deformation identity modulo `p^2`, equivalently two explicit scalar identities modulo `p`. The parent `0/1/2` valuation blocks are simultaneously identified as exact Taylor vanishing orders of the same deformation.

Thus the remaining theorem is no longer “control the full p-adic product of two length-p truncations”. It is one finite Jacobi/harmonic identity on the low/middle/high deformation coefficients.

## 2. Frozen parent inputs

For `p=6m+1`, retain the parent definitions

\[
B_k=\frac{(1/6)_k(1/3)_k}{(k!)^2}2^{-k},
\qquad
G_p=\sum_{k=0}^{p-1}B_k,
\qquad
H_p=\sum_{k=0}^{p-1}(12k+1)B_k.
\]

The parent proved, for the plus classes, the exact reflected tail reduction

\[
T_p\equiv p^2R_p\pmod{p^3},
\]

where

\[
R_p=
2\sum_{i=1}^{m}B_i
\sum_{r=1}^{i}(1+6(i-r))C_r\pmod p,
\]

and

\[
C_r=
\frac{2^{r-1}(r-1)!^2}
{18(5/6)_r(2/3)_r}.
\]

Consequently the original plus-sign inert target is exactly `(L+)`. No finite-tail bookkeeping is reopened in this task.

## 3. Exact parameter deformation

For `p=6m+1`, the two hypergeometric parameters satisfy the exact identities

\[
\frac16=-m+\frac p6,
\qquad
\frac13=-2m+\frac p3.
\]

Introduce

\[
b_{m,k}(\varepsilon)
=
\frac{(-m+\varepsilon/6)_k(-2m+\varepsilon/3)_k}
{(k!)^2 2^k}.
\]

Then

\[
\boxed{B_k=b_{m,k}(p)}.
\]

This makes the parent valuation split structural rather than accidental:

- `0<=k<=m`: neither negative-integer Pochhammer has crossed its zero, so the Taylor order is `0`;
- `m<k<=2m`: `(-m+eps/6)_k` contains exactly one vanishing factor, so the Taylor order is `1`;
- `2m<k<=6m=p-1`: both Pochhammers contain a vanishing factor, so the Taylor order is `2`.

Therefore the frozen `v_p(B_k)=0,1,2` blocks are exactly the `eps`-Taylor vanishing-order blocks under `eps=p`.

This is the first main result of the task.

## 4. Exact coefficients through second order

Write `H_n=sum_{j=1}^n 1/j` and `H_n^(2)=sum_{j=1}^n 1/j^2`.

### 4.1 Low block `0<=k<=m`

Put

\[
w_k=\binom mk\binom{2m}{k}2^{-k},
\]

\[
L_k=-\frac16(H_m-H_{m-k})
     -\frac13(H_{2m}-H_{2m-k}),
\]

and

\[
Q_k=\frac12\left(
L_k^2
-\frac1{36}(H_m^{(2)}-H_{m-k}^{(2)})
-\frac19(H_{2m}^{(2)}-H_{2m-k}^{(2)})
\right).
\]

Direct logarithmic differentiation of the two Pochhammer factors gives

\[
\boxed{
b_{m,k}(\varepsilon)
=w_k(1+L_k\varepsilon+Q_k\varepsilon^2)+O(\varepsilon^3).
}
\tag{A0}
\]

### 4.2 Middle block `m<k<=2m`

The simple zero at the `-m` parameter gives

\[
d_k=
\frac{(-1)^{m+k}}6
\frac{m!(k-m-1)!(2m)!}
{(2m-k)!(k!)^2 2^k},
\]

and the relative first correction is

\[
M_k=
\frac16(H_{k-m-1}-H_m)
-\frac13(H_{2m}-H_{2m-k}).
\]

Hence

\[
\boxed{
b_{m,k}(\varepsilon)
=d_k\varepsilon+d_kM_k\varepsilon^2+O(\varepsilon^3).
}
\tag{A1}
\]

### 4.3 High block `2m<k<=6m`

Both negative-integer parameters have crossed their zeros. The exact quadratic leading coefficient is

\[
v_k=
\frac{(-1)^m}{18}
\frac{m!(2m)!(k-m-1)!(k-2m-1)!}
{(k!)^2 2^k},
\]

so

\[
\boxed{
b_{m,k}(\varepsilon)=v_k\varepsilon^2+O(\varepsilon^3).
}
\tag{A2}
\]

All denominators appearing here are `p`-adic units because every index is `<p`.

## 5. Five finite deformation sums

Define

\[
F_0=\sum_{k=0}^{m}w_k,
\]

\[
F_1=\sum_{k=0}^{m}w_kL_k
+\sum_{k=m+1}^{2m}d_k,
\]

\[
F_2=\sum_{k=0}^{m}w_kQ_k
+\sum_{k=m+1}^{2m}d_kM_k
+\sum_{k=2m+1}^{6m}v_k,
\]

and

\[
J_0=\sum_{k=0}^{m}(12k+1)w_k,
\]

\[
J_1=
\sum_{k=0}^{m}(12k+1)w_kL_k
+\sum_{k=m+1}^{2m}(12k+1)d_k.
\]

Substituting `eps=p` into `(A0)-(A2)` gives the exact p-adic reconstructions

\[
\boxed{G_p\equiv F_0+pF_1+p^2F_2\pmod{p^3}}
\tag{G2}
\]

and

\[
\boxed{H_p\equiv J_0+pJ_1\pmod{p^2}}.
\tag{H1}
\]

No `J_2` is required for `(L+)` once `p|G_p` is established.

## 6. Exact leading divisibility `p|G_p`

This step is deliberately separated from the conjectural derivative-weighted target.

Let

\[
U_p=\sum_{n=0}^{p-1}
\frac{(2n)!(3n)!}{(n!)^5\,216^n}.
\]

The proved unweighted congruence of Zhi-Hong Sun, *Congruences involving* `binom(2k,k)^2 binom(3k,k)`, J. Number Theory 133 (2013), 1572–1595, gives

\[
U_p\equiv0\pmod{p^2}
\]

for the inert residue classes, including `p≡13,19 (mod24)`.

Independently, the same finite Clausen coefficient identity used by the parent gives

\[
G_p^2=U_p+T_p^{(0)},
\]

where `T_p^(0)` is the unweighted degree-at-least-`p` finite convolution tail. For `p=6m+1`, the already frozen `0/1/2` support theorem implies every term of `T_p^(0)` has total valuation at least `2`: low+low and middle+middle cannot reach degree `p`, and the first surviving support is low×high/high×low. Hence

\[
T_p^{(0)}\equiv0\pmod{p^2}.
\]

Therefore

\[
G_p^2\equiv0\pmod{p^2},
\]

so in `Z_p`

\[
\boxed{p\mid G_p}.
\tag{D}
\]

This uses an unweighted proved theorem only to establish the leading divisibility. It does not import the derivative-weighted mod-`p^3` target.

## 7. Exact terminal reduction of the plus target

From `(G2)` and `(D)`, define the p-adic integer

\[
A_m:=\frac{F_0}{p}+F_1.
\]

Then

\[
\frac{G_p}{p}\equiv A_m+pF_2\pmod{p^2}.
\]

Combining with `(H1)`, the plus target `(L+)` is equivalent to

\[
\boxed{
(A_m+pF_2)(J_0+pJ_1)
\equiv1+pR_p\pmod{p^2}.
}
\tag{R2}
\]

Splitting `(R2)` into its two p-adic digits gives the exact pair

\[
\boxed{A_mJ_0\equiv1\pmod p,}
\tag{R0}
\]

\[
\boxed{
\frac{A_mJ_0-1}{p}
+A_mJ_1+F_2J_0
\equiv R_p\pmod p.
}
\tag{R1}
\]

Thus, under the proved leading divisibility `(D)`, the following are exactly equivalent for every plus-class prime:

`G_pH_p ≡ p+p^2R_p (mod p^3)`

`<=>`

`(R2)`

`<=>`

`(R0) and (R1)`.

This is the terminal theorem-level reduction of this execution.

The all-prime truth of `(R0)` and `(R1)` is **not proved here**. They are the smallest exact remaining identities.

## 8. Separate residue-class audit

The algebra above treats both requested classes without inserting a Frobenius sign:

- `p≡13 (mod24)` corresponds to `m≡2 (mod4)`;
- `p≡19 (mod24)` corresponds to `m≡3 (mod4)`.

No class-specific extra premise enters the deformation or reduction. The target sign `+` is not assumed in the derivation of `(G2)`, `(H1)` or `(D)`; it appears only in the final equality being reduced.

No exact obstruction distinguishing the two plus classes was found.

## 9. Second proof lane

A structurally distinct p-adic transformation/Gamma route was audited rather than conflated with the parameter deformation.

The parent already established that the Mao–Pan truncated transformation framework reaches mod `p^2` for the relevant unweighted transformation technology, while this problem needs derivative-weighted mod `p^3` information. That precision gap remains.

The Zhi-Hong Sun unweighted theorem closes only `(D)` above. It does not supply `(R0)` or `(R1)`.

No audited imported Gamma/Dwork identity in the source set evaluates the exact finite second-order coefficient combination in `(R1)`. Therefore this lane does not close the target and is retained only as a dependency/precision audit.

This satisfies the task requirement to test a second structurally distinct mechanism without pretending a mod-`p^2` unweighted theorem solves a mod-`p^3` derivative target.

## 10. Deterministic checker and falsification

Task-local checker:

`scripts/check_enterprise_brc_half_coupling_inert_plus_reflected_derivative_product_bridge.py`

It uses exact `Fraction` arithmetic and independently checks:

1. the direct `B_k` recurrence;
2. `(G2)` modulo `p^3`;
3. `(H1)` modulo `p^2`;
4. the unweighted inert congruence on the finite test set;
5. `p|G_p`;
6. the parent reduced product target modulo `p^3`;
7. `(R0)`;
8. `(R1)`.

Current exact regression in this execution:

- all plus-class primes `p<2000`;
- `77` primes total;
- `40` primes in class `13 mod24`;
- `37` primes in class `19 mod24`;
- `sum m = 11487` across the cases;
- failures: `0`.

This is `FINITE_REGRESSION_ONLY_NOT_A_PROOF`.

## 11. Tool/method reuse audit

After the problem structure was fixed, current repository coverage was searched for a reusable parameter-deformation / hypergeometric-Taylor checker. No matching reusable mechanism was located.

The new script is therefore classified

`NOT_APPLICABLE_TASK_LOCAL_CHECKER`.

No new general tool family, toolbox ID or canonical method promotion is claimed.

## 12. What is closed and what remains open

Closed exactly in this task:

1. the parent valuation blocks are Taylor-order blocks of one explicit deformation;
2. the full `G_p mod p^3` and needed `H_p mod p^2` data reduce to `F0,F1,F2,J0,J1`;
3. `p|G_p` follows from a proved unweighted inert congruence plus the finite unweighted Clausen tail valuation;
4. `(L+)` is exactly equivalent to `(R0)+(R1)`;
5. both requested residue classes are covered by one uniform reduction.

Not closed:

1. an all-prime proof of `(R0)`;
2. an all-prime proof of `(R1)`;
3. therefore an all-prime proof of `(L+)` itself.

No exact counterexample was found.

The smallest remaining unit is:

> Prove the finite Jacobi/harmonic identities `(R0)` and `(R1)` uniformly for `m≡2,3 (mod4)` with `p=6m+1` prime, or reduce them further by a terminating creative-microscoping/WZ or finite-field Jacobi-sum certificate.

Broadening the prime scan is not a successor-worthy action.

## 13. Final freeze

`PRIMARY_VERDICT = PROOF_NOT_CLOSED_WITH_SMALLER_IDENTITY`.

`HARD_TARGET = ACHIEVED_AT_EXACT_REDUCTION_STRENGTH`.

`PLUS_TARGET = UNPROVED_UNREFUTED`.

`SMALLEST_EXACT_REMAINING_IDENTITY = (R0)+(R1)`.

`FINITE_TAIL = ALREADY_ELIMINATED_BY_PARENT`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH = NOT_GRANTED`.

`NOVELTY_OR_PRIORITY_CLAIM = NONE`.

Recommended Driver action: accept this as a strict exact reduction if the imported unweighted congruence dependency and coefficient algebra check out; do not mark the plus target proved. If continuing, publish a narrowly scoped successor for the finite Jacobi/harmonic identities `(R0)` and `(R1)` rather than reopening the full finite-Clausen or broad inert tasks.
