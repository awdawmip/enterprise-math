# R749SMU — Exact optimal *affine* Walsh-source reconstruction and the nonlinear frontier

Date: 2026-11-13 (Asia/Shanghai). Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Scientific predecessors: R749SMQ (positive convolution bounds), R749SMR/SMS/SMT (nonlinear minimax on selected fibers). Independent abstract source-observer result, no V29/V39 native event or independent review asserted.

## 1. Statement and decoder class

Let `G=F_2^d` be a finite source group; `U⊆G\{0}` are retained Walsh characters and `m_U(mu)=(E_mu chi_a)_{a∈U}`. The identity observer's target is the entire source distribution `mu∈Delta(G)`. Define **affine** decoders as maps `D` on the *feasible moment polytope* satisfying `D(m_U(mu))∈Delta(G)` for every law and affine behavior on that moment polytope. Set

`R_U^aff = inf_{D affine} sup_{mu∈Delta(G)} TV(D(m_U(mu)),mu)`.

Define the positive Fourier-support feasible set

`K_U={rho∈Delta(G): sum_x rho(x)chi_a(x)=0 for all nonzero a∉U}`.

**Theorem (exact affine minimax reduction).**

`R_U^aff = 1 - max_{rho∈K_U} rho(0)`.

The maximization is an ordinary finite linear program with `2^d` nonnegative variables and the displayed linear equalities. The theorem holds for any finite `d`, any retained set `U`, and includes arbitrary stochastic affine reconstruction, not merely translation-equivariant or convolutional reconstruction.

**Corollary (all 168 exceptional four-dimensional classes).** For the canonical five-element circuit `C={1,2,4,8,15}` and its ten-character complement `B=G\({0}∪C)`,

`R_C^aff=5/6,qquad R_B^aff=5/8.`

These values hold for every GL(4,2)-equivalent circuit and its complement.

## 2. Proof: group twirling reduces every affine decoder to convolution

Write `T(mu)=D(m_U(mu))`. Because `m_U` and `D` are affine on the source simplex, `T` is an affine map of source probabilities into output probabilities, hence a stochastic `|G|×|G|` matrix: `T(mu)=sum_x mu_x T(delta_x)`. Its columns obey `T(delta_x)≥0` and each sums to one.

For each `g∈G`, let `tau_g` denote translation of distributions, `(tau_g mu)(x)=mu(x⊕g)`. Since `m_a(tau_g mu)=chi_a(g)m_a(mu)`, translation of the source induces a **known** signed transformation of retained moments. Therefore `T_g=tau_{-g}T tau_g` is still a valid stochastic affine moment decoder. Consider the average

`Tbar = (1/|G|) sum_g tau_{-g} T tau_g`.

By convexity and translation invariance of total variation, for every `mu`,

`TV(Tbar mu,mu) ≤ (1/|G|)sum_g TV(T tau_g mu,tau_g mu) ≤ sup_nu TV(T nu,nu)`.

Thus twirling never increases worst-case risk. The averaged map commutes with every source translation. Consequently its columns are translates of one probability law `rho=Tbar(delta_0)`, so `Tbar(mu)=rho*mu` is **convolution** (commutativity means that left/right and inverse translations coincide in `F_2^d`).

By Walsh diagonalization, `widehat{rho*mu}(a)=hat rho(a) hat mu(a)`. If `a∉U∪{0}` and `hat rho(a)≠0`, the result would depend on an unretained moment `hat mu(a)`; that dependence cannot factor through `m_U`. To see this directly, the two strictly positive source laws `mu_±(x)=[1±epsilon chi_a(x)]/|G|` with `0<epsilon≤1` have identical retained moments and different outputs. Therefore `hat rho(a)=0`; hence `rho∈K_U`. Conversely every `rho∈K_U` yields an affine decoder that depends only on retained moments by Fourier inversion, so the characterization is exact.

For any such convolution, the convex function `mu→TV(rho*mu,mu)` attains its maximum over the simplex at a vertex `delta_x`. For any vertex,

`TV(rho*delta_x,delta_x)=1-rho(0)`.

Therefore `sup_mu TV(rho*mu,mu)=1-rho(0)`. Minimizing over convolution kernels completes the theorem.

## 3. Exact values using already certified positive kernels

R749SMQ proved that among positive convolution kernels with Fourier support in `{0}∪C`, the maximum diagonal mass is `rho_C(0)=1/6`; the explicit maximizing kernel is

`rho_C(x)=[1+(chi_1(x)+chi_2(x)+chi_4(x)+chi_8(x)+chi_15(x))/3]/16`.

It has masses `1/6` at 0, `1/12` at ten points and 0 at five points. That work also provided a summation-of-positivity-inequalities certificate of **optimality** of the diagonal mass, not merely its feasibility.

For B, R749SMQ proved `rho_B(0)≤3/8` for any such convolution kernel, and constructed equality with `rho_B(0)=3/8`, `rho_B(x)=1/8` at the five states whose five circuit characters have exactly four negative signs, and 0 elsewhere. These exact rational Fourier-support certificates were executed and published in R749SMQ's standalone checker and results. Substituting yields `5/6` and `5/8`, with no new numerical assumptions.

## 4. Why the quantifier matters

Theorem 1 is a **complete result only for affine decoders on the entire feasible moment polytope**. It does not claim that arbitrary nonlinear decoders have the same global optimum: for them R749SMQ gives `3/4≤R_C(I)≤5/6` and `1/2≤R_B(I)≤5/8`, while R749SMR/SMS/SMT determine several full individual moment-fiber radii exactly.

In particular, R749SMT's circuit-line optimal decoder uses `z(t)=max(0,2|t|-1)`, a nonlinear function of the retained moment t; its worst-case loss on those fibers can be strictly below `5/6`. Comparing a **restricted moment fiber** with the **global affine minimax** does not by itself establish a strict global nonlinear-vs-affine gap.

The exact next question is whether an explicitly moment-adaptive decoder can achieve uniform global loss <5/6 for C or <5/8 for B; or, alternatively, a nonzero higher-dimensional moment fiber can establish matching nonlinear lower bounds. The two-coordinate equal-moment line does not supply such a bad fiber. The present theorem isolates the obstruction for every affine method and removes the need to optimize that entire decoder class again.

## 5. Verification and references

Logical proof: finite group twirl, character orthogonality and simplex-convexity above. Numeric input: none. Exact kernel optimality reused without re-running from `research_notes/portable_direct/2026-11-13_R749SMQ_ARBITRARY_WALSH_FAMILY_SANDWICH_AND_CIRCUITS.md`, checker `R749SMQ_ARBITRARY_WALSH_FAMILY_EXACT_CHECK.py`, results `R749SMQ_ARBITRARY_WALSH_FAMILY_RESULTS.json` at commit `db31f593d0c81e10686ccc18d92b229b3f19fa07`, previously read from GitHub. No formal verification/independent scientific review performed.
