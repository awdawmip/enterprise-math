# PREFIX-679-R6 — Quantitative transversality and inverse conditioning of the frozen BRC diagonal–edge crossover

Date: 2026-11-11 (Asia/Shanghai). Status: AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessors: PREFIX-676 (cd2c6681a6ed4857bb7d416e82a8642f6cc0739f), PREFIX-677 (b1cda0db8097c4addac67899ecfe32dc7aa1446e), PREFIX-678 (029ecd8afe03187ea5b166708546a9d7e0554567). The observer probabilities are scalar readouts of the frozen BRC Heartbeat World X6 model, not native spatial dimensions. No P000 or task publication change.

## Problem and exact definitions

For the two independent frozen Poissonized first-stop clocks, define Y(p,z)=max(Y_p,Y_z), μ(p,z)=E[Y(p,z)], W(p,z)=Var(Y(p,z)) and V_q(p,z)=q²W(p,z)−qμ(p,z).
On the diagonal and parameter edge let
A(z)=W(z,z)−W(0,z), B(z)=μ(z,z)−μ(0,z),
q₀(z)=B(z)/A(z), and
D_q(z)=V_q(z,z)−V_q(0,z)=q A(z)[q−q₀(z)].
For this theorem all quantities are the finite-kernel exact polynomials or rational functions of the frozen observer.

## New theorem (uniform inverse condition number and residual bound)

Set b=53/1000, ρ=1/330000000, I=[b−ρ,b+ρ] and
J=[1794869/100000,1794888/100000]=[17.94869,17.94888].

For every real z∈I:

  33000 < q₀′(z) < 104000.                                         (1)

Consequently, for each real q∈J there is a unique crossing z_q∈I; the crossing curve is continuously differentiable with

  1/104000 < dz_q/dq < 1/33000.                                    (2)

For every q₁<q₂ in J,

  (q₂−q₁)/104000 < z_(q₂)−z_(q₁) < (q₂−q₁)/33000.                  (3)

In particular the two endpoint crossing locations differ by more than
19/10400000000 and less than 19/3300000000.

For q∈J, z∈I, z≠z_q, the variance comparison has an explicit two-sided transverse residual bound:

  173844 |z−z_q| < |D_q(z)| < 1103232 |z−z_q|.                     (4)

At z=z_q both sides vanish. Thus exact evaluation of the variance gap at any z∈I guarantees the root-distance estimate
|z−z_q|<|D_q(z)|/173844 (for z≠z_q).
The diagonal configuration has larger V_q for z<z_q; the edge has larger V_q for z>z_q. All stated inequalities hold for the entire real-parameter intervals, without numerical sampling interpolation.

## Proof

The PREFIX-677/678 exact 189-layer predecessor center jet and Bernstein budgets at b give

  11/25 < A(b) < 441/1000,   789/100 < B(b) < 79/10,
  −1681 < A′(b) < −1680,      128 < B′(b) < 129,
  R(b) > 332788/25,           R=B′A−BA′,
  17948788665/10⁹ < q₀(b) < 17948788666/10⁹,
  |A″(z)| ≤ A₂=281945567232, |B″(z)| ≤ B₂=133031808 for 0≤z≤1/2.

Define exact rational quantities
  δ_A=1681ρ + A₂ρ²/2, δ_B=129ρ+B₂ρ²/2;
  A_−=11/25−δ_A, A_+=441/1000+δ_A;
  B_−=789/100−δ_B, B_+=79/10+δ_B;
  a_+=1681+A₂ρ, b_+=129+B₂ρ.

Taylor's theorem implies throughout I:
A_−<A(z)<A_+, 0<B_−<B(z)<B_+, |A′(z)|<a_+, |B′(z)|<b_+.
The exact companion checker establishes A_−>439/1000 and A_+<442/1000.

The derivative cancellation from PREFIX-678,
R′=B″A−BA″, gives the certified lower bound
R(z)>R_−:=332788/25−ρ(B₂A_++A₂B_+)>6500.
For the **new upper bound**, keep R's two-term structure:
R(z)=B′A−BA′<b_+A_++B_+a_+=:R_+.
Since A_−>0,
R_−/A_+² < q₀′(z)=R(z)/A(z)² < R_+/A_−².
The checker performs exact Fraction comparisons
R_−/A_+²>33000 and R_+/A_−²<104000,
establishing (1).

The certified q₀(b) bracket, integrated q₀′>33000, and exact comparisons
q₀(b)_upper−33000ρ < 1794869/100000,
1794888/100000 < q₀(b)_lower+33000ρ
show J lies strictly within q₀(I); thus inverse z_q exists uniquely. The inverse-function theorem gives dz_q/dq=1/q₀′(z_q) and (2), while integration gives (3). The width of J is 19/100000.

For q∈J use q=q₀(z_q) and the mean value theorem:
33000|z−z_q| < |q₀(z)−q₀(z_q)| < 104000|z−z_q|.
Multiply by qA(z), with 12≤q≤24 and 439/1000<A(z)<442/1000. The exact products 12(439/1000)(33000)=173844 and 24(442/1000)(104000)=1103232 establish (4). The orientation follows qA(z)>0 and q₀ increasing. QED.

## Exact verification, reuse and next research unit

The companion PREFIX679_R6_TRANSVERSE_CROSSING_CERTIFICATE.py executes 17 integer/Fraction implication checks and produces PREFIX679_R6_RESULTS.json. Its actual local execution returned ALL_CHECKS_PASS 17. It reuses the precise PREFIX-677/678 original-survivor center jets and global curvature budgets; the 189-level path recurrence was NOT rerun this iteration. This is an author-derived implication certificate, not independent review or theorem admission.

This result gives a rigorous certified condition number for crossover root isolation. If a numerical evaluation has certified absolute error ≤e, the safe root-distance bound is (|computed D_q(z)|+e)/173844 on the stated domain.

Next: replace coarse second-derivative budgets with signed local Bernstein intervals for A′, B′ and R, to expand q₀'s uniqueness interval across more of 13/250<z<27/500. Then use PREFIX-675's complete p=0 edge optimum to prune genuinely two-parameter boxes. Preserve original P000, frozen science and active owner constraints.
