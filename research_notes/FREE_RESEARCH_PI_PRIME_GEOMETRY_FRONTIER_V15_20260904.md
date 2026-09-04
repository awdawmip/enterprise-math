# Free Research — Pi-to-Prime Geometry Frontier V15

Status: `FREE_RESEARCH_CURRENT_FRONTIER / PNT_CLOSED_BY_REAL_SMOOTHING / PRIME_BIRTH_AND_WINDING_GEOMETRY / COMPLETE_PROVENANCE / V14 DENSITY_AND_RESIDUAL BRIDGES / V15 PARITY_FOLD SCALAR READOUT CLOSED / NATIVE ENERGY DECAY COMPOSITION OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Supersedes as current frontier: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V14_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Stable geometric chain

The stable interpretation remains

\[
\boxed{
\begin{aligned}
\text{prime }p
&=\text{irreducible multiplicative-holonomy birth direction},\\
p^a
&=\text{the }a\text{th winding layer on that direction},\\
\det\mathcal W_N
&=\operatorname{lcm}(1,\ldots,N),\\
\psi(N)&=\log\det\mathcal W_N.
\end{aligned}}
\]

The degree-three provenance carrier retains the complete intermediate history, splits into the trivial/history-mean and `S_3` standard sectors, and has the exact standard energy coefficient `1/9`.

V14 closed the induced-density and full adaptive-residual gates at research-note strength:

- actual deepest marginals have Beta-type logarithmic profiles rather than flat profiles;
- endpoint conditioning is removed by positive ANOVA;
- suffix-pair density is absorbed into one-body coefficient potentials;
- rectangular adaptive return identities route all remaining tails to lower scale;
- the full prime-winding residual of `r(N)=psi(N)/N-1` is uniformly bounded without using PNT backward.

The open issue after V14 was the final scalar readout from the retained relation/provenance energy.

---

## 2. V15 scalar carrier: the parity-folded action square

Let

\[
u_a=\Lambda(a)/a,
\qquad
A_N=\sum_{a\le N}u_a,
\qquad
q_a(n)=\lfloor n/a\rfloor.
\]

Complete the full ordered square of actions by the stopped endpoint

\[
\Phi_N(a,b)=
\begin{cases}
q_{ab}(N),&ab\le N,\\
q_a(N),&ab>N,
\end{cases}
\]

with sign

\[
\varepsilon_N(a,b)=
\begin{cases}
-1,&ab\le N,\\
+1,&ab>N.
\end{cases}
\]

For the adaptive residual

\[
G_f(n)=A_nf(n)+\sum_{a\le n}u_af(q_a(n)),
\]

the exact finite resolvent is

\[
\boxed{
A_N^2f(N)
=A_NG_f(N)-\sum_{a\le N}u_aG_f(q_a(N))
-\sum_{a,b\le N}u_au_b\varepsilon_N(a,b)
 f(\Phi_N(a,b)).
}
\]

The action square has total positive mass `A_N^2`. Its signed imbalance is

\[
A_N^2-2C_2(N),
\qquad
C_2(N)=\sum_{ab\le N}u_au_b.
\]

The first-mass and two-history laws imply

\[
\frac{|A_N^2-2C_2(N)|}{A_N^2}
=O(1/\log N).
\]

---

## 3. Exact scalar readout

Normalize the action square by

\[
\pi_N(a,b)=u_au_b/A_N^2
\]

and define

\[
F_N(a,b)=f(\Phi_N(a,b)),
\qquad
\mathcal F_N(f)=\operatorname{Var}_{\pi_N}(F_N).
\]

If

\[
\sup_{n\le N}|G_f(n)|\le C_G,
\qquad
\sup_{n\le N}|f(n)|\le B,
\]

then

\[
\boxed{
|f(N)|
\le
\frac{2C_G}{A_N}
+\sqrt{\mathcal F_N(f)}
+B\left|1-rac{2C_2(N)}{A_N^2}\right|.
}
\]

For the prime error, V14 supplies `C_G=O(1)` and Chebyshev supplies `B=O(1)`. Hence

\[
\boxed{
\left|\frac{\psi(N)}N-1\right|
\le
\sqrt{\mathcal F_N(r)}
+O(1/\log N).
}
\]

This closes the formerly open energy-to-scalar map.

---

## 4. Positive stopped odd-square energy

Choosing the variance center `-f(N)` gives

\[
\boxed{
A_N^2\mathcal F_N(f)
\le
\sum_{ab>N}u_au_b|\delta_af(N)|^2
+
\sum_{ab\le N}u_au_b|\delta_{ab}f(N)|^2.
}
\]

Consequently

\[
\boxed{
\mathcal F_N(f)
\le
\frac{A_NE_1^{\rm full}(f;N)+E_{\rm dir}^{\le}(f;N)}{A_N^2}.
}
\]

The scalar field is therefore read from a positive one-history plus valid two-history packet. The transported channel remains necessary only for proving decay of that packet.

---

## 5. Degree-three `S_3` Dirichlet realization

For a pair field `F(a,b)` on a probability action space, lift it to triples, average the three position transpositions and project the third coordinate. The induced operator is

\[
(\mathcal K_3^{(2)}F)(a,b)
=
\frac{F(b,a)+\mathbb E_cF(a,c)+\mathbb E_cF(c,b)}3.
\]

Its centered Hoeffding spectrum is

\[
\boxed{2/3,\ 0,\ 1/3,\ -1/3,}
\]

on the symmetric-additive, antisymmetric-additive, symmetric-interaction and antisymmetric-interaction sectors respectively. Thus

\[
\operatorname{Var}(\mathcal K_3^{(2)}F)
\le\frac49\operatorname{Var}(F).
\]

Its exact Dirichlet form is

\[
\boxed{
\mathcal D_p(F)
=\frac16\mathbb E_{a,b,c}
\left[
|F_{ab}-F_{ba}|^2
+|F_{ab}-F_{cb}|^2
+|F_{ab}-F_{ac}|^2
\right],
}
\]

and the spectral gap gives

\[
\operatorname{Var}(F)\le3\mathcal D_p(F).
\]

Applying this to `F_N=f o Phi_N` yields

\[
\boxed{
|r(N)|
\le
\sqrt{3\mathcal D_N(r)}
+O(1/\log N).
}
\]

Every term in `D_N` is one of the already retained geometric channels: ordered quotient relation, common-suffix curvature, or a mixed valid/stopped moving-cutoff boundary relation.

---

## 6. Quantitative consequence, conditional only on energy decay

For any `alpha>0`,

\[
\mathcal D_N(r)=O((\log N)^{-2\alpha})
\]

implies

\[
\boxed{
\psi(N)-N
=O\left(
\frac{N}{(\log N)^{\min\{\alpha,1\}}}
\right).
}
\]

Thus a future block recurrence no longer needs a separate scalar extraction theorem. Its energy exponent transfers with the expected square-root loss.

---

## 7. Updated boundary

Closed at exact finite/research-note theorem strength:

1. the full adaptive parity-fold resolvent;
2. valid/tail mass completion and `O(1/log N)` parity imbalance;
3. scalar error controlled by one positive folded variance;
4. folded variance controlled by a positive stopped odd-square packet;
5. pair-valued `S_3` mixer and exact Hoeffding spectrum;
6. degree-three Dirichlet/Poincare realization;
7. a direct quantitative energy-to-prime-error transfer theorem.

Open:

1. prove decay of the concrete folded Dirichlet energy from the V14 multichannel return equations;
2. perform a coefficient-safe audit of the mixed valid/stopped transposition chambers;
3. close one finite block recurrence containing the pair-additive `2/3` amplitude sector, the interaction `1/3` sectors, and the lower-scale tails;
4. derive an unconditional native logarithmic remainder;
5. any RH-scale, Working Truth or Foundation claim.

The decisive correction is that the final readout is not a point evaluation of a flat shell state. It is the parity expectation of a stopped two-history square, whose nonconstant part is exactly a positive degree-three `S_3` Dirichlet energy.

---

## 8. Artifacts

- `research_notes/FREE_RESEARCH_PARITY_FOLDED_SQUARE_SCALAR_READOUT_V15_20260904.md`;
- `research_notes/FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V15_20260904.md`;
- `scripts/check_free_research_parity_folded_scalar_readout.py`.

The checker uses `Fraction` only and verifies the finite resolvent, parity mass balance, covariance decomposition, odd-square domination, scalar inequality, pair mixer, `4/9` variance contraction, exact Dirichlet identity and Poincare inequality.
