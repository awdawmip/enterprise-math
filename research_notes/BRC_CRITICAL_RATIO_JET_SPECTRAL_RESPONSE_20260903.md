# BRC Critical Ratio-Jet Spectral Response

Status: `RESEARCH / EXACT FINITE POSITIVE-RATIONAL / IRREDUCIBLE CRITICAL CORE`
Date: `2026-09-03`
Parents: PR #1177 powered rational critical gauge; PR #1178 critical ratio histogram finite jet; WBRC-T39..T44.

## 1. Scope and prior-art boundary

This note studies the **critical residual matrix** after the tropical/global dominant scaling has already been removed.  It does not yet claim the first correction of the full original moment matrix when noncritical state edges/cycles may decay on a competing scale.

Analytic perturbation of a simple Perron root, left/right Perron response, and determinant implicit differentiation are classical.  The Enterprise/BRC content is the exact connection to the finite rational ratio jet extracted from the explicit positive-rational branch histogram, together with a root-selector certificate that avoids floating eigenvectors or eigenvalues.

## 2. Exact ratio jet

On the tropical critical cells, PR #1178 gives finitely many rational ratios

\[
1=\theta_0>\theta_1>\cdots>\theta_s>0
\]

and nonnegative integer matrices `L_j` such that

\[
\boxed{
R_m
=
\sum_{j=0}^s\theta_j^mL_j
=
K+\sum_{j\ge1}\theta_j^mL_j.
}
\]

Here `K=L_0` is the critical-degeneracy matrix.  Assume for this note that:

1. `K` is irreducible;
2. at least one subdominant layer exists;
3. `L_1 != 0` for the largest subdominant ratio `theta=theta_1`.

Then the Perron root `rho(K)` is a simple positive eigenvalue.

## 3. Characteristic first ratio layer

Define

\[
p_0(z)=\det(I-zK)
\]

and, for a formal additive first-layer parameter `epsilon`,

\[
q(\epsilon,z)
=
\det\!\bigl(I-z(K+\epsilon L_1)\bigr).
\]

Let

\[
\boxed{
p_1(z)=\left.\frac{\partial q}{\partial\epsilon}\right|_{\epsilon=0}\in\mathbf Z[z].
}
\]

The full determinant of the exact ratio jet is a finite exponential sum in the moment order `m`.  Its base `1` coefficient polynomial is exactly `p_0`; its base `theta_1` coefficient polynomial is exactly `p_1`.

Every remaining determinant base either uses one lower ratio `theta_j<=theta_2` or at least two subdominant selections, each at most `theta_1`.  Therefore, with

\[
\boxed{
\delta=
\begin{cases}
\max(\theta_2,\theta_1^2),&s\ge2,\\
\theta_1^2,&s=1,
\end{cases}
<\theta_1,
}
\]

we have coefficientwise

\[
\boxed{
\det(I-zR_m)
=
p_0(z)+\theta_1^m p_1(z)+O_{\rm coeff}(\delta^m).
}
\]

The `O_coeff` constant is finite and exact: for each `z` coefficient it may be chosen as the sum of the absolute integer coefficients of all strict determinant bases.

## 4. Exact root response state

Let `z_c` be the smallest positive root of `p_0`; by WBRC-T41,

\[
z_c=1/\rho(K).
\]

Use the existing exact state

```text
p_0(z) in Z[z]
selector = SMALLEST_POSITIVE_REAL_ROOT
rational exact root OR rational Sturm isolating interval
```

and append the integer response polynomial `p_1(z)`.

Implicit differentiation of

\[
q(\epsilon,z(\epsilon))=0
\]

gives

\[
z'(0)=-\frac{p_1(z_c)}{p_0'(z_c)}.
\]

Hence for

\[
\Gamma(\epsilon)=-\ln z(\epsilon)=\ln\rho(K+\epsilon L_1)
\]

we obtain the exact algebraic response

\[
\boxed{
\beta
=
\Gamma'(0)
=
\frac{p_1(z_c)}{z_c\,p_0'(z_c)}.
}
\]

Equivalently, for positive Perron left/right vectors `u,v`,

\[
\beta
=
\frac{u^TL_1v}{\rho(K)u^Tv}.
\]

The Perron-vector formula is interpretation only; the Enterprise certificate is `(p_0, root selector, p_1)`.

Since `K` is irreducible, `u,v>0`; since `L_1>=0` and `L_1!=0`,

\[
\boxed{\beta>0.}
\]

Thus the first positive subdominant branch-ratio layer cannot cancel at first order.

## 5. Residual Perron/log asymptotic

The remaining ratio-jet tail is `O(delta^m)` entrywise and hence is `o(theta_1^m)`.  Standard simple-root perturbation then yields

\[
\boxed{
\rho(R_m)
=
\rho(K)
+c\,\theta_1^m
+O(\delta^m),
}
\]

where

\[
c=-\frac{\psi_1(\rho(K))}{\chi'(\rho(K))}>0
\]

for the equivalent `t`-characteristic polynomials, and

\[
\boxed{
\ln\rho(R_m)
=
\ln\rho(K)
+\beta\,\theta_1^m
+O(\delta^m).
}
\]

The last big-O uses ordinary finite-dimensional analytic perturbation; the determinant coefficient error itself has an exact finite rational-base certificate.

## 6. Closed-form regressions

### 6.1 Branching critical core

Take

\[
K=\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
L_1=E_{00}.
\]

Then `rho(K)=2`, `z_c=1/2`, and

\[
p_0(z)=1-2z,
\qquad
p_1(z)=-z+z^2.
\]

Therefore

\[
\boxed{\beta=1/4.}
\]

For `epsilon=theta^m`,

\[
\rho(K+\epsilon E_{00})
=2+\frac12\epsilon+O(\epsilon^2),
\]

so the logarithmic first coefficient is indeed `(1/2)/2=1/4`.

### 6.2 Irrational Perron root but rational response

Take

\[
K=\begin{pmatrix}0&2\\3&0\end{pmatrix},
\qquad
L_1=E_{01}.
\]

Then `rho(K)=sqrt(6)` while

\[
\rho(K+\epsilon L_1)=\sqrt{6+3\epsilon}.
\]

Thus

\[
\ln\rho(K+\epsilon L_1)
=
\ln\sqrt6+\frac14\epsilon+O(\epsilon^2),
\]

again giving exact rational `beta=1/4` despite an irrational base Perron root.

### 6.3 Algebraic response genuinely remains algebraic

For

\[
K=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\qquad L_1=E_{01},
\]

`z_c` is the smallest positive root of `1-z-z^2`.  The response is

\[
\boxed{
\beta=\frac{z_c}{1+2z_c},
}
\]

which is naturally retained as a rational function of the already-certified algebraic root selector rather than forced into a rational number.

## 7. Hard boundaries

Freeze:

```text
RATIO_JET_FIRST_RESPONSE_SCOPE = IRREDUCIBLE_CRITICAL_RESIDUAL_CORE
CRITICAL_RESIDUAL_R_m != FULL_ORIGINAL_W_m
NONCRITICAL_GLOBAL_GAP_MAY_COMPETE_WITH_THETA_1
FIRST_POSITIVE_RATIO_LAYER -> POSITIVE_FIRST_PERRON_RESPONSE
EXACT_RESPONSE_STATE = p_0 + SMALLEST_POSITIVE_ROOT_SELECTOR + p_1
FLOATING_LEFT_RIGHT_EIGENVECTORS != REQUIRED_CERTIFICATE
ALGEBRAIC_BETA != FORCED_RATIONAL_NUMBER
SIGNED_CANCELLATION != POSITIVE_RATIO_JET_RESPONSE
```

A later theorem must combine this critical-cell ratio scale with the global noncritical characteristic gap from WBRC-T40 before claiming the true next correction of the full moment matrix.
