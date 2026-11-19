# EC49FUJ — Exact endpoint minimax throughout the second-count phase for 15 clipped-price observations

Date: 2026-11-20 (Asia/Shanghai). Evidence: AUTHOR_PROVED / EXACT_FRACTION_BERNSTEIN_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.

Frozen scientific parent: BRC16943 source fc0f038e7bfd12c886b4d37f900bfb770c0f61ab, as inherited through EC49FUI / Draft PR #2830 at cb4df4d3b3aa20f1af3f4edd454992e048f84a12. This is a theorem about the inherited clipped-price count observer, not a new native X6 physical dynamics or Bellman-optimality proof. All previous source parameters remain frozen.

## Observer and exact parameter interval

Fix 15 conditionally independent binary observations, a single common nuisance e ≤ E=1048576/18958647 under both hypotheses and all trials, and equal hypothesis priors. Introduce θ=(1-ae)^{-1}∈(0,θ_E], with a=2807259/163840 and θ_E=31597745/1653649. θ=0 denotes only the limit e→−∞.

For normalized width x∈(0,1), retain the inherited probability coordinates

\[
T(\theta,x)=(1-x)(1-\beta x+\beta x\theta),\quad
\beta=\frac3{637},\qquad
u(\theta)=\frac{C}{H+B\theta},
\]
\[
(C,H,B)=(21829245984,45529434409,-456083905),\qquad
p=1-T,\quad r=1-Tu.
\]

Under H_−, K∼Bin(15,p); under H_+, K∼Bin(15,r). Endpoint data are

\[
u_E=\frac{4822040484}{8132285009},\quad
u_I=\frac{21829245984}{45529434409},\quad
\eta=\frac{141024}{1653649},
\]
\[
T_E=(1-x)(1+\eta x),\qquad T_I=(1-x)(1-\beta x).
\]

Let x_B be the unique endpoint Bayes K=1 likelihood-ratio crossing from EC49FUH/FUI, with the inherited exact rational isolation

\[
\frac{2956}{10^7}<x_B<\frac{2957}{10^7}.
\]

**New exact second-count transition.** Let x₂ be the unique root in (0,1) of

\[
\boxed{[1-T_E(x)]^2=u_E^{13}[1-u_E T_E(x)]^2.}
\]

The accompanying pure-Fraction program verifies the strict rational bracket

\[
\boxed{\frac{15172}{10^6}<x_2<\frac{15174}{10^6}<\frac{61}{4000}.}
\]

Uniqueness: p_E=1−T_E strictly increases on (0,1); r_E/p_E=u_E+(1−u_E)/p_E is strictly decreasing. Hence the count-2 likelihood ratio (r_E/p_E)^2 u_E^13 crosses one exactly once, with the program's rational endpoint signs.

## Theorem — entire adjacent K≥2 phase

**For every real x∈[x_B,x₂] and every finite shared e≤E,** the deterministic test

\[
\boxed{\phi_2(K)=\mathbf1_{\{K\ge2\}}}
\]

is minimax among all randomized tests measurable with respect to the full 15-bit observation sequence, under equal hypothesis priors. The sharp error risk is

\[
\boxed{
R_{15}^{mm}(x)=\frac{1-D_{2,E}(x)}2,\quad
D_{2,E}=15T_E^{14}(1-u_E^{14})-14T_E^{15}(1-u_E^{15}).
}
\]

For this rule, the worst finite common nuisance is exactly e=E, with strictly lower risk for every finite e<E. The interior endpoint Bayes count rule is uniquely K≥2; at x_B and x₂ extra endpoint-Bayes ties are possible. This fills the complete second-count endpoint-Bayes phase immediately adjacent to the previously solved randomized first-count phase (x₁₅,x_B).

## Proof 1 — endpoint Bayes lower bound

For k∈{0,…,15} the endpoint count likelihood ratio is

\[
L_k=\left(\frac{r_E}{p_E}\right)^k u_E^{15-k},
\qquad
L_{k+1}/L_k=\frac{r_E}{p_Eu_E}>1.
\]

Thus L₀=u_E^{15}<1; by the definitions of x_B and x₂, L₁≤1≤L₂ throughout [x_B,x₂]. Therefore φ₂ is Bayes-optimal at admissible nuisance e=E. Every test has composite maximum risk at least the e=E Bayes risk, namely [1−D₂,E]/2.

## Proof 2 — strict nuisance-coordinate concavity

Write G(z)=15z¹⁴−14z¹⁵ and S(θ,x)=T(θ,x)u(θ). The discrimination gap for K≥2 is

\[
D_2(\theta,x)=G(T)-G(S)
=15T^{14}(1-u^{14})-14T^{15}(1-u^{15}).
\]

For fixed x∈[x_B,x₂], primes denote derivatives with respect to θ. Because B<0 and T is increasing affine in θ, T'>0, u'>0, u''>0, S'>0 and S''=2T'u'+Tu''>0. The exact constants ensure

\[
\frac{13}{14}<T_I(61/4000)\le T<1,\qquad
0<S\le u_E<\frac35<\frac{13}{14}.
\]

Use G'(z)=210z¹³(1−z)>0 on (0,1), G''(z)=210z¹²(13−14z). Then

\[
\boxed{
D_2''=G''(T)(T')^2-G''(S)(S')^2-G'(S)S''<0.
}
\]

The first term is negative (T>13/14) and the remaining two are negative (0<S<13/14, S',S''>0). Thus D₂(·,x) is strictly concave on the entire compactified θ-interval [0,θ_E], so its minimum is at an endpoint.

## Proof 3 — exact endpoint comparison over the full real-width interval

Define J(x)=D₂(0,x)−D₂(θ_E,x). We certify the stronger uniform statement

\[
\boxed{J(x)>\frac1{20000}\quad\text{for every real }0\le x\le L=\frac{61}{4000}.}
\]

Substitute the rational quadratic polynomials T_I=1−(1+β)x+βx² and T_E=1−(1−η)x−ηx² into D₂. This gives an explicit rational-coefficient polynomial J of degree 30. Let y=x/L and expand its degree-30 Bernstein representation:

\[
J(Ly)=\sum_{i=0}^{30} a_i y^i
=\sum_{k=0}^{30}b_k {30\choose k} y^k(1-y)^{30-k},
\quad
b_k=\sum_{i=0}^k a_i\frac{{k\choose i}}{{30\choose i}}.
\]

The companion program EC49FUJ_SECOND_COUNT_STABLE_PHASE_VERIFY.py reconstructs all a_i exactly from the displayed T_I,T_E,u_I,u_E, then checks **31/31** strict Fraction inequalities

\[
\boxed{b_k>1/20000\quad(k=0,\ldots,30).}
\]

The smallest coefficient is b₃₀=J(L)≈0.00005704616095956522; this decimal is descriptive only. Because Bernstein basis functions are nonnegative and sum to one, the 31 rational inequalities prove the displayed bound for every real x∈[0,L]. In particular, D₂(0,x)>D₂(θ_E,x) on [x_B,x₂]. Strict concavity from Proof 2 therefore yields

\[
D_2(\theta,x)\ge D_2(\theta_E,x)
\quad\text{for all }0\le\theta\le\theta_E,
\]

with strict inequality for θ<θ_E.

## Proof 4 — matching upper bound and conclusion

At any finite nuisance e≤E, φ₂ has equal-prior risk [1−D₂(θ,x)]/2, bounded above by its risk at e=E. Its maximum risk thus equals the lower bound from Proof 1. This proves global composite minimaxity against every randomized test, not only count-threshold tests. QED.

## Reproduction, residual scope, and next problem

The companion standalone standard-library Fraction checker was run by the author and reports:

- PASS; exact degree 30; 31/31 Bernstein coefficients > 1/20000.
- x_B∈(2956/10^7,2957/10^7), x₂∈(15172/10^6,15174/10^6).
- At x=1/1000, the exact formula gives minimax risk ≈0.00224217412828716, and J(x)≈0.00410186568285375; the inequalities and identity are checked with Fraction.
- Scope: author-side exact coefficient certification and analytic proof; independent mathematical review NOT_REVIEWED. The parent clipped-price law and its Bellman basis remain inherited, not independently re-executed.

The binomial hit-count map is the declared finite observer. The source's uncensored price and clip-origin provenance remain typed as parent information; this result does not identify count observations with a complete native X6 state or discard residuals for unspecified future operations. P000, Heartbeat World and frozen science have not changed.

The next scientific unit is the endpoint K≥3 phase x>x₂: locate its risk-crossover boundary, identify any randomized boundary count and least-favorable nuisance mixture, and test whether the endpoint-Bayes rule remains composite minimax. Preserve all completed source proofs without recomputing them. No formal Task publication/CLAIM, Result or independent Review is established by this portable theorem.
