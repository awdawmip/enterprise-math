# Free Research — Parity-Folded Square Scalar Readout

Status: `FREE_RESEARCH_FRONTIER / EXACT_PARITY_FOLD_RESOLVENT / SCALAR_READOUT_CLOSED / ODD_SQUARE_VARIANCE_BRIDGE / PAIR_S3_DIRICHLET_BRIDGE / NATIVE ENERGY DECAY COMPOSITION OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V14_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `COMPOSE_APPLIED` from the exact full residual, quotient composition, weighted relation-field variance, and weighted `S_3` lift--transpose--project machinery. No new general-purpose tool family is claimed.

## 1. Executive result

The remaining scalar-readout problem admits an exact finite solution.

Let

\[
u_a:=\frac{\Lambda(a)}a,
\qquad
A_N:=\sum_{a\le N}u_a,
\qquad
q_a(n):=\left\lfloor\frac na\right\rfloor.
\]

For a field `f` define its adaptive full signless residual

\[
G_f(n)
:=A_n f(n)+\sum_{a\le n}u_af(q_a(n)).
\]

On the full ordered action square `(a,b)<=N`, fold every valid two-step history `ab<=N` to its two-step endpoint and every invalid second step `ab>N` back to its one-step endpoint:

\[
\Phi_N(a,b)
=
\begin{cases}
q_{ab}(N),&ab\le N,\\
q_a(N),&ab>N,
\end{cases}
\]

and attach the parity sign

\[
\varepsilon_N(a,b)
=
\begin{cases}
-1,&ab\le N,\\
+1,&ab>N.
\end{cases}
\]

Then the following exact resolvent holds:

\[
\boxed{
A_N^2f(N)
=A_NG_f(N)-\sum_{a\le N}u_aG_f(q_a(N))
-\sum_{a,b\le N}u_au_b\varepsilon_N(a,b)
 f(\Phi_N(a,b)).
}
\tag{1.1}
\]

The last term is not estimated by absolute mass. Its sign measure is asymptotically balanced, and its centered part is controlled by one positive folded-square variance.

For the actual normalized prime error

\[
r(N):=\frac{\psi(N)}N-1,
\]

the V14 full-residual theorem gives `G_r(n)=O(1)`, while Chebyshev gives `r=O(1)`. Consequently

\[
\boxed{
|r(N)|
\le
\sqrt{\mathcal F_N(r)}
+O\left(\frac1{\log N}\right),
}
\tag{1.2}
\]

where

\[
\mathcal F_N(f)
:=\operatorname{Var}_{\pi_N}
\bigl(f\circ\Phi_N\bigr),
\qquad
\pi_N(a,b):=\frac{u_au_b}{A_N^2}.
\]

Thus the scalar readout is no longer an open informal step:

\[
\boxed{
\text{quantitative decay of the parity-folded history variance}
\Longrightarrow
\text{quantitative decay of }\psi(N)/N-1.
}
\]

Moreover `F_N=f o Phi_N` lives on an ordered pair carrier. The canonical three-transposition lift--project mixer on this pair carrier has centered `L^2` norm `2/3`, energy survival `4/9`, and a completely explicit degree-three Dirichlet form. Hence

\[
\boxed{
|r(N)|
\le
\sqrt{3\mathcal D_N(r)}
+O\left(\frac1{\log N}\right),
}
\tag{1.3}
\]

where `D_N` is a positive ordered three-history transposition energy.

This closes the map from retained provenance energy to the scalar prime-counting error. It does not yet prove decay of `D_N` from the full multichannel cascade.

---

## 2. Abstract finite setup

The exact algebra does not require primality.

Fix an integer `N>=2`, a finite action family

\[
S_N\subseteq\{1,2,\ldots,N\},
\]

and nonnegative weights `u_a`. Put

\[
A_n:=\sum_{\substack{a\in S_N\\a\le n}}u_a,
\qquad
A:=A_N>0.
\]

For a real field `f` on the integer scales, define

\[
G_f(n)
:=A_nf(n)+
\sum_{\substack{a\in S_N\\a\le n}}
 u_af(q_a(n)).
\tag{2.1}
\]

Natural-number division supplies the exact composition law

\[
q_b(q_a(n))=q_{ab}(n).
\tag{2.2}
\]

Define the valid collision mass

\[
C_2(N)
:=\sum_{\substack{a,b\in S_N\\ab\le N}}u_au_b.
\tag{2.3}
\]

The complementary stopped-tail mass is

\[
A^2-C_2(N)
=
\sum_{\substack{a,b\in S_N\\ab>N}}u_au_b.
\tag{2.4}
\]

---

## PFS-T01 — Exact adaptive parity-fold resolvent

Expand the two residual terms:

\[
\begin{aligned}
A G_f(N)
&=A^2f(N)+A\sum_{a\in S_N}u_af(q_a(N)),\\
\sum_a u_aG_f(q_a(N))
&=\sum_au_aA_{q_a(N)}f(q_a(N))
 +\sum_{ab\le N}u_au_bf(q_{ab}(N)).
\end{aligned}
\]

Since

\[
A-A_{q_a(N)}
=\sum_{b>q_a(N)}u_b
=\sum_{ab>N}u_b,
\tag{3.1}
\]

we obtain

\[
\begin{aligned}
&A G_f(N)-\sum_a u_aG_f(q_a(N))\\
&\quad=A^2f(N)
+\sum_{ab>N}u_au_bf(q_a(N))
-\sum_{ab\le N}u_au_bf(q_{ab}(N)).
\end{aligned}
\tag{3.2}
\]

The last two terms are exactly

\[
K_f(N)
:=\sum_{a,b\in S_N}u_au_b\varepsilon_N(a,b)
 f(\Phi_N(a,b)).
\tag{3.3}
\]

This proves (1.1).

The identity is finite, floor-exact and cutoff-adaptive. No limit, approximation, PNT input or complex analysis occurs.

---

## 4. Why this is the correct completion of the action square

The raw valid-history region `ab<=N` has only the collision mass `C_2(N)`. Its complement cannot simply be discarded: it has asymptotically the same mass.

The fold completes the full ordered square by interpreting an invalid second action as a stopped one-step history. Hence every pair carries a retained endpoint:

\[
\boxed{
\text{valid pair}\mapsto q_{ab}(N),
\qquad
\text{overcut pair}\mapsto q_a(N).
}
\]

The positive carrier has exact total mass

\[
\boxed{A^2.}
\tag{4.1}
\]

Its signed parity imbalance is

\[
\boxed{
\sum_{a,b}u_au_b\varepsilon_N(a,b)
=A^2-2C_2(N).
}
\tag{4.2}
\]

For ideal Lebesgue measure in logarithmic action coordinate, the valid-collision and stopped-tail endpoint densities cancel pointwise: both have density proportional to the remaining logarithmic length. The arithmetic expression (4.2) is the finite discrepancy from that ideal cancellation.

---

## PFS-T02 — Prime-winding parity balance

Specialize to

\[
u_a=\frac{\Lambda(a)}a.
\]

The established first-mass law is

\[
A_N=\log N+O(1).
\tag{5.1}
\]

The positive two-history continuation law gives

\[
C_2(N)=\frac12\log^2N+O(\log N).
\tag{5.2}
\]

Therefore

\[
\boxed{
A_N^2-2C_2(N)=O(\log N)
}
\tag{5.3}
\]

and

\[
\boxed{
\eta_N
:=\left|1-\frac{2C_2(N)}{A_N^2}\right|
=O\left(\frac1{\log N}\right).
}
\tag{5.4}
\]

For an explicit bounded-discrepancy form, suppose

\[
|A_N-\log N|\le C
\]

and

\[
\left|C_2(N)-\frac12\log^2N\right|
\le2C\log N+C^2.
\]

Then, whenever `log N>C`,

\[
\boxed{
\eta_N
\le
\frac{6C\log N+3C^2}{(\log N-C)^2}.
}
\tag{5.5}
\]

---

## PFS-T03 — Scalar covariance bound

Normalize the full square to the probability measure

\[
\pi_N(a,b):=\frac{u_au_b}{A^2}.
\]

Set

\[
F_N(a,b):=f(\Phi_N(a,b)),
\qquad
\epsilon_N(a,b):=\varepsilon_N(a,b).
\]

Then

\[
\frac{K_f(N)}{A^2}
=\mathbb E_{\pi_N}[\epsilon_NF_N].
\]

Writing bars for expectations,

\[
\mathbb E[\epsilon F]
=\operatorname{Cov}(\epsilon,F)+\bar\epsilon\,\bar F.
\]

Since `epsilon` takes only the values `+1,-1`,

\[
\operatorname{Var}(\epsilon)\le1.
\]

Therefore Cauchy--Schwarz gives

\[
\boxed{
\left|\frac{K_f(N)}{A^2}\right|
\le
\sqrt{\mathcal F_N(f)}
+\|f\|_{\infty,[1,N]}\eta_N.
}
\tag{6.1}
\]

Suppose

\[
|G_f(n)|\le C_G
\qquad(1\le n\le N).
\]

The two residual terms in (1.1) satisfy

\[
\left|
\frac{AG_f(N)-\sum_au_aG_f(q_a(N))}{A^2}
\right|
\le\frac{2C_G}{A}.
\]

Hence

\[
\boxed{
|f(N)|
\le
\frac{2C_G}{A}
+\sqrt{\mathcal F_N(f)}
+\|f\|_{\infty,[1,N]}\eta_N.
}
\tag{6.2}
\]

This is the exact scalar-readout theorem.

---

## PFS-C01 — Prime-error readout

For

\[
f=r,
\qquad
r(n)=\psi(n)/n-1,
\]

the V14 Selberg residual closure supplies

\[
G_r(n)=O(1)
\]

uniformly, without using PNT as an input. Chebyshev supplies

\[
\|r\|_\infty=O(1).
\]

Combining these facts with (5.1) and (5.4) yields

\[
\boxed{
|r(N)|
\le
\sqrt{\mathcal F_N(r)}
+O\left(\frac1{\log N}\right).
}
\tag{7.1}
\]

Thus, for every `alpha>0`,

\[
\mathcal F_N(r)=O((\log N)^{-2\alpha})
\quad\Longrightarrow\quad
r(N)=O((\log N)^{-\min\{\alpha,1\}}).
\tag{7.2}
\]

In particular, any proof that `F_N(r)->0` implies PNT directly.

---

## PFS-T04 — Positive odd-square domination

The folded variance is itself controlled by signless history defects.

By the minimizing-center characterization of variance, choose the center

\[
c=-f(N).
\]

Then

\[
A^2\mathcal F_N(f)
\le
\sum_{a,b}u_au_b
|F_N(a,b)+f(N)|^2.
\]

On the stopped-tail region `ab>N`,

\[
F_N(a,b)+f(N)=\delta_af(N).
\]

On the valid-collision region `ab<=N`,

\[
F_N(a,b)+f(N)=\delta_{ab}f(N).
\]

Therefore

\[
\boxed{
A^2\mathcal F_N(f)
\le
\sum_{ab>N}u_au_b|\delta_af(N)|^2
+
\sum_{ab\le N}u_au_b|\delta_{ab}f(N)|^2.
}
\tag{8.1}
\]

If

\[
E_1^{\rm full}(f;N)
:=\sum_{a\le N}u_a|\delta_af(N)|^2
\]

and

\[
E_{\rm dir}^{\le}(f;N)
:=\sum_{ab\le N}u_au_b|\delta_{ab}f(N)|^2,
\]

then positivity gives

\[
\boxed{
\mathcal F_N(f)
\le
\frac{A E_1^{\rm full}(f;N)+E_{\rm dir}^{\le}(f;N)}{A^2}.
}
\tag{8.2}
\]

This is a stopped-history version of the odd-simplex energy. It uses exactly the one-step and valid direct two-step channels; no transported term is required for the scalar readout itself. The transported channel remains necessary for proving decay of the right side from finite return dynamics.

Combining (6.2) and (8.2),

\[
\boxed{
|f(N)|
\le
\frac{2C_G}{A}
+
\frac{\sqrt{A E_1^{\rm full}+E_{\rm dir}^{\le}}}{A}
+\|f\|_\infty\eta_N.
}
\tag{8.3}
\]

This is an explicit end-to-end scalar extraction from a positive finite signless history packet.

---

## 9. The pair-valued `S_3` lift--project mixer

The scalar readout has reduced the problem to the variance of a function on an ordered pair carrier. There is a canonical degree-three mixer on precisely this space.

Let `S` carry a probability measure `p`, and let

\[
F:S^2\to\mathbb R.
\]

Define row and column means

\[
R_F(a):=\mathbb E_cF(a,c),
\qquad
C_F(b):=\mathbb E_cF(c,b).
\]

Lift `F(a,b)` to triples `(a,b,c)`, average the three position transpositions, and project out `c`. The resulting operator is

\[
\boxed{
(\mathcal K_3^{(2)}F)(a,b)
=\frac{F(b,a)+R_F(a)+C_F(b)}3.
}
\tag{9.1}
\]

It is self-adjoint and Markov on `L^2(p tensor p)`.

---

## PFS-T05 — Exact Hoeffding spectrum

Decompose a centered pair field orthogonally as

\[
F(a,b)
=s(a)+s(b)
+d(a)-d(b)
+h_+(a,b)+h_-(a,b),
\tag{10.1}
\]

where

- `s,d` have `p`-mean zero;
- `h_+` is symmetric with zero row and column means;
- `h_-` is antisymmetric with zero row and column means.

Then

\[
\boxed{
\begin{array}{c|c}
\text{sector}&\mathcal K_3^{(2)}\text{ eigenvalue}\\ \hline
s(a)+s(b)&2/3\\
d(a)-d(b)&0\\
h_+(a,b)&1/3\\
h_-(a,b)&-1/3
\end{array}}
\tag{10.2}
\]

Consequently

\[
\boxed{
\operatorname{Var}(\mathcal K_3^{(2)}F)
\le\frac49\operatorname{Var}(F).
}
\tag{10.3}
\]

The slow sector is the symmetric additive channel; all genuine pair interaction energy survives by at most `1/9`.

---

## PFS-T06 — Exact degree-three Dirichlet form

Let the three transpositions act on the lifted triple by

\[
(a,b,c)\mapsto(b,a,c),
\quad
(a,b,c)\mapsto(c,b,a),
\quad
(a,b,c)\mapsto(a,c,b).
\]

A direct self-adjoint expansion gives

\[
\boxed{
\begin{aligned}
\mathcal D_p(F)
&:=\langle F,(I-\mathcal K_3^{(2)})F\rangle_{p\otimes p}\\
&=\frac16\mathbb E_{a,b,c}
\Big[
|F(a,b)-F(b,a)|^2\\
&\qquad\qquad+|F(a,b)-F(c,b)|^2
+|F(a,b)-F(a,c)|^2
\Big].
\end{aligned}}
\tag{11.1}
\]

Since the centered spectral radius is `2/3`, the spectral gap is `1/3`, and therefore

\[
\boxed{
\operatorname{Var}_{p\otimes p}(F)
\le3\mathcal D_p(F).
}
\tag{11.2}
\]

Equivalently,

\[
\boxed{
\operatorname{Var}(F)
\le\frac12\mathbb E_{a,b,c}
\left[
|F_{ab}-F_{ba}|^2
+|F_{ab}-F_{cb}|^2
+|F_{ab}-F_{ac}|^2
\right].
}
\tag{11.3}
\]

This is a positive ordered degree-three provenance energy. It is built only from differences between histories related by one slot transposition.

---

## PFS-C02 — Degree-three scalar prime readout

Apply PFS-T06 to the folded endpoint field `F_N=f o Phi_N`, with

\[
p_N(a)=u_a/A_N.
\]

Equations (6.2) and (11.2) give

\[
\boxed{
|f(N)|
\le
\frac{2C_G}{A_N}
+\sqrt{3\mathcal D_N(f)}
+\|f\|_\infty\eta_N,
}
\tag{12.1}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal D_N(f)
=\frac16\mathbb E_{a,b,c\sim p_N}
\Big[&|f(\Phi_N(a,b))-f(\Phi_N(b,a))|^2\\
&+|f(\Phi_N(a,b))-f(\Phi_N(c,b))|^2\\
&+|f(\Phi_N(a,b))-f(\Phi_N(a,c))|^2
\Big].
\end{aligned}}
\tag{12.2}
\]

For `f=r`,

\[
\boxed{
|r(N)|
\le
\sqrt{3\mathcal D_N(r)}
+O\left(\frac1{\log N}\right).
}
\tag{12.3}
\]

Thus the final scalar output is controlled by exactly the degree in which the existing `3!` provenance and `S_3` mixing geometry live.

---

## 13. Chamber interpretation of the three transposition edges

The three terms in (12.2) have distinct meanings.

1. `F_ab-F_ba` vanishes on valid collisions `ab<=N`; on the stopped-tail region it is
   \[
   f(q_a(N))-f(q_b(N)),
   \]
   the ordered one-step relation field.

2. `F_ab-F_cb` keeps the second slot and exchanges the first. In the valid/valid sector it is a common-suffix curvature
   \[
   f(q_{ab}(N))-f(q_{cb}(N)).
   \]
   Mixed valid/stopped sectors are moving-cutoff boundary relations.

3. `F_ab-F_ac` keeps the first slot and exchanges the second. In the valid/valid sector it is the quotient-cloud relation at the intermediate state `q_a(N)`; in the stopped/stopped sector it vanishes. Mixed sectors are again exact tail-boundary relations.

Hence `D_N` is not an unrelated auxiliary norm. It is the union of the already identified channels:

\[
\boxed{
\text{ordered quotient curvature}
+\text{common-suffix transport}
+\text{moving-cutoff boundary relations}.
}
\tag{13.1}
\]

This is the precise interface to the V14 rectangular tail-return and two-channel ANOVA packets.

---

## 14. What is now closed and what remains open

Closed at exact finite/research-note theorem strength:

1. an adaptive two-step resolvent for the scalar field;
2. a full positive stopped-history square of mass `A_N^2`;
3. asymptotic parity balance `O(1/log N)`;
4. scalar error bounded by one positive folded variance;
5. direct domination by a positive stopped odd-square packet;
6. an exact pair-valued `S_3` mixer with centered energy survival `4/9`;
7. an exact degree-three Dirichlet/Poincare bridge;
8. scalar prime error bounded by the square root of a retained three-history relation energy plus `O(1/log N)`.

Still open:

1. prove `D_N(r)` decays from the full V14 multichannel return system rather than from PNT;
2. audit the mixed valid/stopped transposition chambers against the rectangular tail-potential recurrence without coefficient loss;
3. combine the mean coefficient, standard coefficient and the new pair-additive `2/3` amplitude sector into one finite block recurrence;
4. obtain an unconditional native exponent for `r(N)`;
5. any RH-scale statement, Working Truth or Foundation promotion.

The previous endpoint problem has therefore changed type. It is no longer

> how can a relation-energy estimate be read back into a scalar prime error?

That map is now exact. The remaining question is

> can the concrete degree-three folded Dirichlet energy in (12.2) be shown to decay under the already constructed multichannel cube-root dynamics?

This is a narrower and directly testable theorem.
