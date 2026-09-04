# Free Research — One/Two-History Parity Block Coupling

Status: `FREE_RESEARCH_FRONTIER / EXACT_PARITY_SECOND_ITERATE / LOG_BLOCK_LAWS_CLOSED / OVERLAP_ONE_MINUS_E_INV / COUPLING_INEQUALITY_CLOSED / S3_COMPATIBLE_BLOCK_ENERGY_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V15_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `COMPOSE_APPLIED` from the existing prime-power return operator, weighted relation field, parity-folded history carrier, and `S_3` provenance mixer.

## 1. Executive advance

The V15 parity fold gives a positive finite scalar readout but leaves a two-channel propagation problem.  A second, complementary representation is obtained by iterating the exact prime-power return equation once.

Let

\[
\omega(q):=\frac{\Lambda(q)}q,
\qquad
A(n):=\sum_{q\le n}\omega(q),
\]

and for `n>=2` define

\[
(Pf)(n):=\frac1{A(n)}
\sum_{q\le n}\omega(q)
 f\!\left(\left\lfloor\frac nq\right\rfloor\right).
\]

For

\[
r(n):=\frac{\psi(n)}n-1,
\]

the already established full residual estimate has the form

\[
\boxed{r+Pr=e,\qquad |e(n)|\ll \frac1{1+\log n}.}
\tag{1.1}
\]

Applying `P` once more gives the exact parity identity

\[
\boxed{
2r=(P^2-P)r+2e-Pe.
}
\tag{1.2}
\]

Thus the scalar value is controlled by the difference between the adaptive two-history endpoint law and the one-history endpoint law.  These laws have a constant macroscopic overlap in logarithmic scale:

\[
\boxed{L_\infty=1-e^{-1}.}
\tag{1.3}
\]

After a finite logarithmic block coupling, (1.2) yields

\[
\boxed{
|r(n)|
\le (1-L_{n,K})\|r\|_{\infty,[1,n]}
+\sqrt{L_{n,K}\,\mathcal V_{n,K}(r)}
+O\!\left(\frac{\log\log n}{\log n}\right),
}
\tag{1.4}
\]

where `V_(n,K)` is a positive within-block relation energy between matched odd and even histories.

This closes the scalar parity coupling algebra.  The remaining issue is sharply typed: realize `V_(n,K)` as an `S_3`-compatible standard-sector energy, rather than merely as an arbitrary maximal-coupling variance.

---

## 2. Exact second-iterate identity

For state `1`, fix any bounded convention for `P`; its contribution at a large parent state has mass `O(1/A(n))` and is absorbed into the displayed forcing.

Starting from (1.1),

\[
Pr=e-r.
\]

Therefore

\[
P^2r=P(e-r)=Pe-Pr,
\]

and

\[
P^2r-Pr=Pe-2Pr=Pe-2e+2r.
\]

Rearrangement gives (1.2) exactly.

Let `mu_n` be the one-history endpoint probability and `nu_n` the adaptive two-history endpoint probability:

\[
\mu_n(m)
=\frac1{A(n)}
\sum_{\substack{q\le n\\\lfloor n/q\rfloor=m}}
\omega(q),
\tag{2.1}
\]

\[
\nu_n(\ell)
=\frac1{A(n)}
\sum_{q\le n}\omega(q)
\frac1{A(m_q)}
\sum_{\substack{s\le m_q\\
\lfloor m_q/s\rfloor=\ell}}
\omega(s),
\qquad m_q=\lfloor n/q\rfloor,
\tag{2.2}
\]

with the bounded `m_q=1` convention just noted.  Then

\[
(P^2-P)f(n)=\int f\,d(\nu_n-\mu_n).
\tag{2.3}
\]

---

## 3. One-history logarithmic law

Put

\[
T:=\log n,
\qquad
u_1:=\frac{\log m_q}{T}\in[0,1].
\]

The available first-mass theorem is

\[
\boxed{A(x)=\log x+O(1).}
\tag{3.1}
\]

For every fixed `z in (0,1]`, the event `nu_1<=z` is, up to a floor displacement of logarithmic size `O(1)`, the event

\[
q\ge n^{1-z}.
\]

Consequently

\[
\boxed{
\mu_n\{\log m/T\le z\}
=z+O_z(1/T).
}
\tag{3.2}
\]

At any fixed finite collection of positive `z` values the error is uniform.  The mass at `m=1` is

\[
\frac{A(n)-A(n/2)}{A(n)}=O(1/T).
\]

The floor deformation itself is harmless at this scale.  For `q<=n/2`,

\[
0\le\log(n/q)-\log\lfloor n/q\rfloor
\le\frac1{\lfloor n/q\rfloor}
\le\frac{2q}{n},
\]

and therefore its weighted mean is

\[
\ll\frac1{nA(n)}\sum_{q\le n/2}\Lambda(q)
\ll\frac1T
\]

by the Chebyshev bound.

Thus the one-history endpoint is asymptotically uniform on normalized logarithmic scale.

---

## 4. Adaptive two-history logarithmic law

Condition on a first endpoint with logarithmic length

\[
u:=\log m_q.
\]

For a fixed threshold `zT`:

- if `u<=zT`, the second endpoint is automatically below the threshold;
- if `u>zT`, (3.1) gives

\[
\Pr\{\log \ell\le zT\mid u\}
=\frac{zT}{u}+O\!\left(\frac1u\right).
\tag{4.1}
\]

Averaging against the asymptotically uniform first-endpoint law yields, for every fixed `z in (0,1]`,

\[
\begin{aligned}
\nu_n\{\log\ell/T\le z\}
&=\int_0^z1\,du+
\int_z^1\frac z u\,du+O_z(1/T)\\
&=\boxed{z(1-\log z)+O_z(1/T).}
\end{aligned}
\tag{4.2}
\]

Equivalently, the limiting two-history density is

\[
\boxed{f_2(z)=-\log z,\qquad0<z<1.}
\tag{4.3}
\]

The interpretation is simple: in the logarithmic continuum, a one-step endpoint ratio is uniform, and the adaptive second step multiplies it by another independent uniform ratio.  The product of two independent `Uniform(0,1)` variables has density `-log z`.

If uniformity down to a moving threshold is required, split at `u=1`; the integrated conditional discrepancy is then

\[
O\!\left(\frac{\log T}{T}\right).
\tag{4.4}
\]

This is the source of the harmless `log log n/log n` term below.

---

## 5. Exact macroscopic overlap

The overlap of the two limiting probability densities is

\[
\begin{aligned}
L_\infty
&:=\int_0^1\min\{1,-\log z\}\,dz\\
&=\int_0^{e^{-1}}1\,dz
+\int_{e^{-1}}^1(-\log z)\,dz\\
&=\boxed{1-e^{-1}.}
\end{aligned}
\tag{5.1}
\]

Thus their unmatched mass is exactly

\[
\boxed{1-L_\infty=e^{-1}.}
\tag{5.2}
\]

This is not a small perturbative overlap.  It is a constant positive parity-mixing resource.

For an integer `K>=2`, partition normalized logarithmic scale into

\[
I_j=[(j-1)/K,j/K],
\qquad1\le j\le K.
\]

Let

\[
p_{n,j}:=\mu_n(I_j),
\qquad
q_{n,j}:=\nu_n(I_j),
\]

and define the block overlap

\[
\boxed{L_{n,K}:=\sum_{j=1}^K\min(p_{n,j},q_{n,j}).}
\tag{5.3}
\]

For fixed `K`, (3.2) and (4.2) give

\[
L_{n,K}=L_K+O_K(1/T),
\tag{5.4}
\]

where

\[
L_K
=\sum_j\min\left\{\frac1K,
\int_{I_j}-\log z\,dz\right\}.
\]

Because `-log z` crosses `1` only once, every block not containing `e^-1` contributes exactly the corresponding integral of `min(1,-log z)`.  Hence only one block can create a Riemann error, and

\[
\boxed{
|L_K-(1-e^{-1})|\le\frac1K.
}
\tag{5.5}
\]

Combining (5.4)--(5.5),

\[
\boxed{
L_{n,K}
\ge1-e^{-1}-K^{-1}-O_K(1/\log n).
}
\tag{5.6}
\]

A moving `K` is possible, but a fixed sufficiently large `K` already preserves a strict constant overlap.

---

## 6. Exact finite block-coupling inequality

Let `mu` and `nu` be probabilities on a finite set `X`, partitioned by blocks `B_j`.  Put

\[
\lambda_j:=\min\{\mu(B_j),\nu(B_j)\},
\qquad
L:=\sum_j\lambda_j.
\]

Inside each block, form matched submeasures

\[
\mu_j'=\frac{\lambda_j}{\mu(B_j)}\mu|_{B_j},
\qquad
\nu_j'=\frac{\lambda_j}{\nu(B_j)}\nu|_{B_j},
\tag{6.1}
\]

with the zero-mass convention omitted.  Their common mass is `lambda_j`.  Let

\[
\pi_j:=\frac{\mu_j'+\nu_j'}{2\lambda_j}
\]

be the pooled probability in block `j`, and define

\[
\boxed{
\mathcal V_{\rm block}(f)
:=\sum_j\lambda_j\operatorname{Var}_{\pi_j}(f).
}
\tag{6.2}
\]

The unmatched parts of both measures have mass `1-L`.  Therefore, for every bounded real `f`,

\[
\boxed{
\frac12|\nu(f)-\mu(f)|
\le
(1-L)\|f\|_\infty
+\sqrt{L\,\mathcal V_{\rm block}(f)}.
}
\tag{6.3}
\]

### Proof

Write `d_j` for the difference of the two matched conditional means in block `j`.  Then

\[
|\nu(f)-\mu(f)|
\le2(1-L)\|f\|_\infty
+\sum_j\lambda_j|d_j|.
\]

Cauchy--Schwarz gives

\[
\sum_j\lambda_j|d_j|
\le\sqrt{L\sum_j\lambda_jd_j^2}.
\]

For the equal mixture `pi_j`, the between-component variance is `d_j^2/4`, so

\[
\frac14d_j^2\le\operatorname{Var}_{\pi_j}(f).
\]

Substitution proves (6.3).

No smoothness, bounded density ratio, or exact endpoint collision is assumed.  All failure to couple exactly inside a block remains as a positive relation energy.

---

## 7. Scalar parity readout

Apply (6.3) to `mu_n`, `nu_n`, and `f=r`.  From (1.2),

\[
|r(n)|
\le\frac12|(P^2-P)r(n)|
+|e(n)|+\frac12|Pe(n)|.
\]

Let

\[
S(n):=\sup_{1\le m\le n}|r(m)|.
\]

Then

\[
\boxed{
|r(n)|
\le(1-L_{n,K})S(n)
+\sqrt{L_{n,K}\mathcal V_{n,K}(r)}
+|e(n)|+\frac12|Pe(n)|.
}
\tag{7.1}
\]

Here `V_(n,K)` is the concrete instance of (6.2) for the one- and two-history endpoint measures.

The first residual term is `O(1/T)`.  The second satisfies

\[
|Pe(n)|
\ll\frac1{A(n)}
\sum_{q\le n}
\frac{\omega(q)}{1+\log\lfloor n/q\rfloor}
\ll\frac{\log T}{T},
\tag{7.2}
\]

because the one-step endpoint log is asymptotically uniform and

\[
\int_0^T\frac{du}{1+u}=\log(1+T).
\]

Hence

\[
\boxed{
|r(n)|
\le(1-L_{n,K})S(n)
+\sqrt{L_{n,K}\mathcal V_{n,K}(r)}
+O\!\left(\frac{\log\log n}{\log n}\right).
}
\tag{7.3}
\]

---

## 8. Conditional constant contraction from the `S_3` standard sector

Suppose the matched block relation energy admits the exact provenance-compatible estimate

\[
\boxed{
\mathcal V_{n,K}(r)
\le\left(\frac19+o(1)\right)S(n)^2
+F_{\rm low}(n),
}
\tag{8.1}
\]

where `F_low` is summable or strictly lower-scale.  The coefficient `1/9` is the existing `S_3` standard-energy survival.

Then (7.3) has limiting homogeneous coefficient

\[
q(L)=(1-L)+\frac{\sqrt L}{3}.
\tag{8.2}
\]

At the ideal overlap `L=1-e^-1`,

\[
\boxed{
q_*
=e^{-1}+\frac13\sqrt{1-e^{-1}}
\approx0.632895<1.
}
\tag{8.3}
\]

Thus an `S_3`-compatible realization of the matched block energy would give a genuine constant macrostep contraction, substantially stronger than the asymptotically critical first-return coefficient.

The conclusion is conditional because maximal block matching is not automatically invariant under the product-weighted three-history transpositions.  One must construct an equivariant matched subkernel or prove a one-density-factor domination by the already formalized product-history Dirichlet form.

---

## 9. Precise remaining intertwiner

The required theorem is now the following.

### Parity-block / `S_3` intertwiner target

Construct, for fixed `K`, a positive three-history measure `Theta_(n,K)` and a pushforward to each pooled block measure `pi_j` such that:

1. its one- and two-history marginals contain matched masses totaling
   \[
   L_{n,K}\ge1-e^{-1}-K^{-1}-o(1);
   \]
2. its transposition action is stationary or dominated by a stationary product-history measure with a scale-independent one-density factor;
3. its block relation observable is the odd/even endpoint difference;
4. the standard component contracts by `1/3` in amplitude and `1/9` in energy;
5. every unmatched or nonstationary defect lands in a strict lower logarithmic band or has normalized mass `O(1/log n)`.

If this theorem holds, (8.1) follows and the scalar channel acquires the constant coefficient (8.3).

This is narrower than the former request to identify all of `mathfrak E_n` with one profile norm.  Only the matched odd/even block relation field must be intertwined.

---

## 10. No-go boundary

A scalar-only argument cannot simply replace `V_(n,K)` by `S(n)^2`.  That gives

\[
(1-L)+\sqrt L,
\]

which exceeds one for every `0<L<1`.

Likewise, the V15 scattering identity

\[
(1-2\alpha)^2+4\alpha(1-\alpha)=1
\]

shows that discarding the standard relation channel and reconstituting it from a scalar envelope returns exactly to the critical coefficient.  The strict gain comes only from retaining the standard channel through the `S_3` mixer.

Therefore:

\[
\boxed{
\text{PARITY OVERLAP ALONE IS NOT ENOUGH;}
\quad
\text{PARITY OVERLAP PLUS RETAINED STANDARD ENERGY IS.}
}
\]

---

## 11. Current classification

Proved at finite/research-note theorem strength:

1. exact second-iterate parity identity (1.2);
2. one-history uniform logarithmic law;
3. adaptive two-history density `-log z`;
4. exact limiting overlap `1-e^-1`;
5. fixed-block approximation and lower bound (5.6);
6. exact finite block-coupling inequality (6.3);
7. scalar readout inequality (7.3);
8. residual forcing `O(log log n/log n)`.

Conditional:

1. the coefficient `q_*<1` in (8.3), conditional on the parity-block / `S_3` intertwiner;
2. any resulting quantitative decay rate.

Open:

1. construction of the equivariant matched subkernel;
2. domination of `V_(n,K)` by the product-weighted three-history standard Dirichlet form;
3. integration with the full V14/V15 multichannel recurrence;
4. a promoted native quantitative remainder;
5. any RH-scale conclusion.
