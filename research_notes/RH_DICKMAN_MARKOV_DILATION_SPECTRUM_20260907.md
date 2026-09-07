# RH Dickman Green Markov dilation and inverse-log spectral no-go

Status: `RESEARCH FRONTIER / EXACT GREEN-OPERATOR RETYPING + EIGENMODE LAW + LOG-ORDER NO-GO / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Scope: `RH / harmonic prime discrepancy / Dickman Green identity / Markov dilation / rooted Volterra source`
Parent frontier:

- `RH_ROOTED_VOLTERRA_GREEN_IDENTITY_20260907.md`
- `RH_ROOTED_VOLTERRA_SOURCE_RESOLVENT_20260907.md`
- `RH_ADJOINT_ROOTED_RESOLVENT_EDGE_ENERGY_20260907.md`
- `RH_PARITY_ENDPOINT_ONE_ARM_INSTABILITY_20260907.md`

Tool-reuse resolution: `EXTEND_EXISTING_TOOL`.

The existing rooted Green identity is rewritten as a finite-depth Markov dilation on the logarithmic prime-error coordinate. No new top-level BRC family is introduced.

P000 is unchanged. The dilation variable is an arithmetic scale/provenance coordinate, not a native X6 spatial axis.

BRC discipline:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

---

## 0. Scope

This note studies only the **floor-free prime-harmonic quadrature block** of the exact rooted source at the Möbius/Dickman endpoint `t=1`. Integer-floor and state-rounding repairs remain separately typed exactly as in the parent Green/source notes.

The result is a structural no-go:

> Dickman Green centering removes the constant harmonic-prime mode exactly, but it does not improve the decay order of any inverse-log mode.

Thus a smooth asymptotic expansion in powers of `1/log N` cannot generate a new logarithmic order, let alone a power saving, merely by passing through the Dickman Green kernel.

---

## 1. Harmonic prime discrepancy

Let

\[
\mathcal E(x)
=
\sum_{p\le x}\frac1p
-\log\log x-B_1,
\]

where `B_1` is the prime Mertens constant. Only differences of `mathcal E` enter below, so the normalization constant has no mathematical effect.

As a Stieltjes measure,

\[
d\mathcal E(q)
=
\frac1q\,d\pi(q)
-\frac{dq}{q\log q}.
\]

For a rooted state `(N,y)`, define

\[
U=\frac{\log N}{\log y}-1\ge0
\]

and the Dickman continuation field

\[
\Phi_{N}(q)
=
\rho\left(
\frac{\log(N/q)}{\log q}
\right),
\qquad y\le q\le N.
\]

Because `rho(v)=1` for `0<=v<=1`, the field is constant on `sqrt(N)<=q<=N`.

The floor-free prime quadrature source is

\[
\boxed{
Q_\pi(N,y)
=
\int_{(y,N]}\Phi_N(q)\,d\mathcal E(q).
}
\]

This is the ideal prime-intensity component of the exact discrete-minus-continuum source.

---

## 2. Exact finite-depth Green identity

Stieltjes integration by parts gives

\[
Q_\pi(N,y)
=
[\mathcal E(N)-\mathcal E(y)]\rho(U)
+
\int_y^{\sqrt N}
[\mathcal E(N)-\mathcal E(q)]\,d\Phi_N(q).
\]

Set

\[
v=\frac{\log(N/q)}{\log q},
\qquad
q=N^{1/(v+1)}.
\]

For `v>1`, the Dickman equation gives

\[
-\rho'(v)=\frac{\rho(v-1)}v.
\]

Therefore

\[
\boxed{
Q_\pi(N,y)
=
[\mathcal E(N)-\mathcal E(y)]\rho(U)
+
\int_1^U
\left[
\mathcal E(N)
-
\mathcal E\left(N^{1/(v+1)}\right)
\right]
\frac{\rho(v-1)}v\,dv.
}
\]

For `0<=U<=1`, the integral is empty and `rho(U)=1`, so the same formula remains valid.

This is the exact one-dimensional Green representation of the prime-harmonic source. It retains the lower cutoff through the boundary atom `rho(U)`.

---

## 3. Markov-dilation form

Put

\[
x=\log N,
\qquad
F(x)=\mathcal E(e^x).
\]

Define

\[
\boxed{
(\mathcal T_UF)(x)
=
\rho(U)F\left(\frac{x}{U+1}\right)
+
\int_1^U
F\left(\frac{x}{v+1}\right)
\frac{\rho(v-1)}v\,dv.
}
\]

Since

\[
\int_1^U\frac{\rho(v-1)}v\,dv
=1-\rho(U),
\]

the coefficients in `T_U` are nonnegative and have total mass one. Thus `T_U` is a genuine Markov averaging operator on multiplicative log-scale contractions.

The Green identity becomes

\[
\boxed{
Q_\pi(N,y)
=(I-\mathcal T_U)F(\log N).
}
\]

The boundary atom at scale `x/(U+1)=log y` is essential. Dropping it changes the operator and violates observer preservation.

Freeze:

`DICKMAN_GREEN_SOURCE = IDENTITY_MINUS_FINITE_MARKOV_DILATION`.

---

## 4. Constant mode is removed exactly

For `F_0(x)=1`,

\[
\mathcal T_UF_0=F_0.
\]

Hence

\[
\boxed{
(I-\mathcal T_U)1=0.
}
\]

This is the exact cancellation of the prime Mertens constant. It explains why the arbitrary additive normalization of `mathcal E` disappears from the rooted source.

In BRC language, the Green source takes a centered difference of one arithmetic scale field against a probability carrier. The longitudinal constant mode is a true gauge mode.

---

## 5. Exact inverse-log eigenmodes

For every real `m>=0`, let

\[
F_m(x)=x^{-m}.
\]

Then

\[
F_m\left(\frac{x}{v+1}\right)
=(v+1)^mF_m(x).
\]

Therefore

\[
\boxed{
\mathcal T_UF_m
=M_m(U)F_m,
}
\]

where

\[
\boxed{
M_m(U)
=
\rho(U)(U+1)^m
+
\int_1^U
(v+1)^m\frac{\rho(v-1)}v\,dv.
}
\]

For `m=0`, `M_0(U)=1`.

For integer `m>=1`, integration by parts gives the equivalent exact formula

\[
\boxed{
M_m(U)
=2^m
+m\int_1^U(v+1)^{m-1}\rho(v)\,dv.
}
\]

Hence, for every `U>=1`,

\[
M_m(U)>1,
\]

and

\[
\boxed{
(I-\mathcal T_U)x^{-m}
=[1-M_m(U)]x^{-m}.
}
\]

Thus every inverse-log mode is preserved at the **same decay order**. The operator changes only its coefficient.

Freeze:

`DICKMAN_GREEN_CENTERING_KILLS_ONLY_m=0_LOG_MODE`.

`m>=1_INVERSE_LOG_MODE -> SAME_ORDER_NONZERO_MULTIPLIER`.

---

## 6. The first logarithmic mode

For `m=1`,

\[
M_1(U)
=2+\int_1^U\rho(v)\,dv.
\]

The Dickman mass is

\[
\int_0^\infty\rho(v)\,dv=e^\gamma,
\]

and `rho=1` on `[0,1]`. Therefore

\[
\boxed{
M_1(U)\longrightarrow1+e^\gamma.
}
\]

Consequently

\[
\boxed{
(I-\mathcal T_U)\frac1x
=
-\left(1+\int_1^U\rho(v)\,dv\right)
\frac1x
\longrightarrow
-\frac{e^\gamma}{x}.
}
\]

So the first nonconstant smooth prime-error mode is not attenuated. Its sign is reversed and its coefficient tends to `e^gamma`.

This answers one of the parent frontier tests:

> the Dickman Green transform is not merely the raw weighted intensity `J_(1/2)`, but it also does not provide a new inverse-log decay order. The constant mode cancels; the `1/log N` mode survives with a nonzero exact multiplier.

---

## 7. General smooth asymptotic consequence

Assume a log-scale field has an asymptotic expansion

\[
F(x)
=c_mx^{-m}+o(x^{-m})
\]

for some fixed `m>=1`, with enough boundedness to pass the Dickman probability kernel through the remainder. Let `U=U(x)->infinity`.

Because all positive moments of the Dickman Green kernel are finite,

\[
M_m(U)\longrightarrow
M_m(\infty)
=2^m+m\int_1^\infty(v+1)^{m-1}\rho(v)\,dv.
\]

Hence

\[
\boxed{
(I-\mathcal T_U)F(x)
=
[1-M_m(\infty)]c_mx^{-m}
+o(x^{-m}).
}
\]

Therefore a regular expansion

\[
\mathcal E(e^x)
\sim\frac{c_1}{x}
+\frac{c_2}{x^2}+\cdots
\]

would pass through the Green source term-by-term without gaining a new power of `1/x`.

This is a no-go for the proof pattern

`SMOOTH_INVERSE_LOG_PRIME_ERROR + DICKMAN_GREEN_CENTERING -> EXTRA_LOG_ORDER`.

Any genuine gain must use information not contained in the smooth inverse-log jet, such as oscillatory sign, root-label correlations, quotient-cell cancellation, or cancellation across several rooted depths.

---

## 8. Relation to known unconditional bounds

The classical prime-harmonic discrepancy satisfies a decaying bound after removal of the constant mode. Substituting such a bound into the Markov identity controls `Q_pi`, but the eigenmode law shows why this control does not automatically improve its logarithmic order.

For example, an input bounded like `1/log N` remains of order `1/log N` under the ideal Dickman Green source in the model case. Stronger zero-free-region bounds remain stronger after averaging, but no new fixed power of `N` is created by `I-T_U` alone.

This note does not estimate the integer-floor repair, and it does not claim that the actual prime discrepancy has a full inverse-log asymptotic series. The result is an operator theorem and a proof-strategy boundary.

---

## 9. Geometric interpretation

The Markov kernel chooses a random contraction

\[
x\longmapsto\frac{x}{V+1}
\]

with probability measure

\[
\rho(U)\delta_U(dV)
+
\mathbf1_{1\le V\le U}
\frac{\rho(V-1)}V\,dV.
\]

The atom is the unresolved lower-cutoff face; the continuous part is the Dickman transition from one rough-prime root into the smooth continuation.

- Constant scale fields are gauge directions and vanish under centering.
- Inverse-log fields are exact eigen-directions.
- Their eigenvalues are moments of the contraction denominator `V+1`.

This is a relation-space geometry, not a new spatial metric. X6 may encode a local root/continuation transition, while the Markov measure records the continuum quotient of all labeled prime paths.

---

## 10. Exact checker

Task-local checker:

`experiments/rh_dickman_markov_dilation_check.py`.

It numerically integrates the Dickman delay equation and verifies:

- the Markov kernel mass `rho(U)+int_1^U rho(v-1)/v dv=1`;
- the inverse-log eigenmode moments;
- the exact finite-`U` identity
  `M_1(U)=2+int_1^U rho(v)dv`;
- convergence `M_1(U)->1+e^gamma`.

The checker is diagnostic only. The Markov and eigenmode formulas are exact analytic identities.

---

## 11. Prior-art boundary

Dickman delay equations, harmonic prime asymptotics, and Markov/dilation operators are classical ingredients. The project-specific content claimed here is the exact composition of the current rooted Green identity with the log-scale eigenmode analysis and the resulting no-go for smooth inverse-log order improvement.

No generic novelty claim is made before a dedicated literature audit.

---

## 12. New smallest research unit

The ideal one-step Green source is now spectrally understood on every smooth inverse-log mode:

- `m=0` is removed;
- every `m>=1` survives at the same order.

Therefore the next admissible object is not another smooth asymptotic expansion of the prime Mertens error. It is the signed oscillatory component paired with the full finite adjoint front block.

The concrete target is

\[
\sum_{r=0}^{K-2}(-1)^r
\left\langle
(I-\mathcal T_{U_r})F,
\mathcal G_r^{\rm adj}
\right\rangle,
\]

with root labels, quotient populations, floor repair, and terminal modes retained. A new result must show cancellation **across scales or rooted depths**, because one Dickman Green step alone has no smoothing gap on inverse-log modes.

A useful next theorem would be an orthogonality or almost-orthogonality law between different rooted depths in the path-mass Hilbert measure. Without such a law, Cauchy reduces the front block to positive capacity and returns the sharp half-depth barrier.

No RH proof is claimed.
