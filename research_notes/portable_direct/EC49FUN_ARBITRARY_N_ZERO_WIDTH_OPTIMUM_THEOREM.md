# EC49FUN — Arbitrary-sample zero-width optimum, exact BRC overlap defect, and nuisance-common garbling obstruction

Date: 2026-11-20 (Asia/Shanghai). Evidence level: **AUTHOR_PROVED / EXACT_FRACTION_CROSSCHECKED / PARENT_DEPENDENT / NOT_REVIEWED**.

## Question and frozen scientific scope

Extend the EC49FUM 15-trial complete minimax atlas to a rigorous **arbitrary positive integer number of independent binary observations** without assuming the existing n=15 phase partition survives. The scientific model pin is the inherited BRC16943 clipped-price observer pin **fc0f038e7bfd12c886b4d37f900bfb770c0f61ab**. Parent result: EC49FUM, immutable source commit **d1058c1acd90dc9b449ee8d9a5203e18ef5b72d4**, PR #2838. The signed/typed native price origins and Heartbeat/X6 joint state are not identified by the present two-symbol readout; this is an explicitly typed statistical projection, not a claim that joint origins are redundant.

Fix a single nuisance parameter shared by H− and H+ and all n conditionally independent trials. Its compactified coordinate is θ ∈ [0, θ_E], where the actual finite domain is θ ∈ (0, θ_E] and θ=0 denotes the limit e→−∞. The constants and laws inherited from the pinned observer are

\[
\begin{aligned}
\beta&=3/637,&\eta&=141024/1653649,\\
C&=21829245984,&H&=45529434409,&B&=456083905,\\
\theta_E&=31597745/1653649,&
u(\theta)&=\frac{C}{H-B\theta},\\
u_I&=\frac{C}{H},&
u_E&=\frac{4822040484}{8132285009},\\
T(\theta,x)&=(1-x)(1-\beta x+\beta x\theta),&
T_E(x)&=(1-x)(1+\eta x).
\end{aligned}
\]

Here x∈[0,1] is the normalized detector width. Conditional on θ, the n binary hits are independent with probabilities p_−=1−T and p_+=1−uT. The nuisance θ is *common*, not redrawn between trials or hypotheses. We consider all tests (possibly randomized) of the entire n-bit output and equal H± priors. Let V_n(x)=inf_φ sup_{0<θ≤θ_E} R_θ(φ,x), where R_θ is the equal-prior classification error.

The geometric/coordinate background is P000 (native X6, signed paths and typed observer), whereas the following argument is exact rational arithmetic on the declared binary observation. No classical geometry is imported as native structure.

## Theorem 1 — all n: exact optimum at zero width, and strict loss at every nonzero width

For **every integer n≥1**,

\[
\boxed{V_n(0)=\frac{u_E^n}{2}.}
\]

At x=0 the single rule “choose H+ iff at least one hit is observed” is minimax. For **every x∈(0,1]**,

\[
\boxed{V_n(x)>V_n(0).}
\]

More precisely, for 0<x≤1 let T=T_E(x), p=1−T, q=1−u_ET. Then

\[
\boxed{V_n(x)-V_n(0)\ \ge\
\frac12 \min\Big\{(1-u_E^n)p^n,\ q^n-u_E^np^n\Big\}>0.}
\tag{1}
\]

This is an explicit positive certificate rather than an extrapolation from the n=15 atlas. It proves the global optimality of the zero-width observer for every fixed finite n in this binary family; **it does not assert V_n(x) is monotone for every pair of positive widths**.

### Proof and exact branch-residual decomposition

At x=0, under H− every bit is zero and under H+ all bits are zero with probability u(θ)^n. Thus the displayed rule has risk u(θ)^n/2; u(θ) is strictly increasing on the compactified θ interval. Its supremum is u_E^n/2. The simple pair at the admissible endpoint θ_E has the same Bayes lower bound, proving the first equality.

For the endpoint θ_E, write μ_−^0=δ_{0^n}, and decompose the H+ law at width zero as

\[
\mu_+^0=u_E^n\delta_{0^n}+(1-u_E^n)\nu_n,
\]

where ν_n is the **full n-bit distribution conditioned on at least one hit**. This retains the complete input-bit population, multiplicity and event distinctions.

Define K_x as the product binary Z-channel that independently turns an original zero into one with probability p=1−T_E(x), and never turns a one into zero. Then exact source-to-observer transport holds at the endpoint:

\[
\mu_-^x=K_x\delta_{0^n}=:A_x,\qquad
\mu_+^x=u_E^n A_x+(1-u_E^n)K_x\nu_n=:u_E^n A_x+(1-u_E^n)B_x.
\]

Thus, for every outcome y∈{0,1}^n,

\[
\min\{A_x(y),\mu_+^x(y)\}
=u_E^nA_x(y)+(1-u_E^n)\min\{A_x(y),B_x(y)\}.
\]

Summing gives the **exact BRC-style overlap/observer defect identity**

\[
\boxed{R_{\theta_E,n}^{\mathrm{Bayes}}(x)
=\frac12\big[u_E^n+(1-u_E^n)\Omega_n(x)\big],}
\qquad
\Omega_n(x):=\sum_{y\in\{0,1\}^n}\min\{A_x(y),B_x(y)\}.
\tag{2}
\]

The nonnegative overlap Ω_n quantifies information lost when the atom-vs-nonatom origin branch is no longer resolvable. Equation (2) is a statement of the specific **binary projection** only. No signed/native joint information is deleted from the parent source.

For y=1^n, A_x(y)=p^n and

\[
B_x(y)=\frac{q^n-u_E^np^n}{1-u_E^n}.
\]

The overlap contains at least the minimum of these two positive masses. Therefore (2), together with V_n(x)≥R_{\theta_E,n}^{Bayes}(x), proves (1). For x>0, p>0 and q>u_Ep, hence both arguments of the minimum are strictly positive. At x=1, the observation is constant and V_n(1)=1/2, also consistent with (1).

## Theorem 2 — an explicit n-dependent endpoint-dominated phase and exact leading loss

Set

\[
m_n=u_I^n\frac{B}{H},\qquad
\boxed{\delta_n=\frac12\min\left\{1,\
\frac{m_n}{\beta(1+m_n)},\
(1-u_E)u_E^{n-1}\right\}>0.}
\]

For **all real x∈[0,δ_n]**, the pure rule φ_n(y)=1{at least one hit} is globally composite-minimax and its worst nuisance is the *finite* endpoint θ_E:

\[
\boxed{V_n(x)=\frac{1-(1-u_E^n)[(1-x)(1+\eta x)]^n}{2}.}
\tag{3}
\]

In particular,

\[
\boxed{V'_n(0+)=\frac n2(1-\eta)(1-u_E^n)>0.}
\tag{4}
\]

### Proof

Define D_1(θ,x)=T(θ,x)^n[1-u(θ)^n], so the rule's error is (1−D_1)/2. Write T_θ=∂T/∂θ=β x(1−x)>0 for x>0 and u_θ=u B/(H−Bθ)>0. The exact derivative is

\[
\frac{\partial_\theta D_1}{nT^n}
=\frac{T_\theta}{T}(1-u^n)-u^{n-1}u_\theta.
\]

On 0≤θ≤θ_E and 0<x≤δ_n, we have

\[
\frac{T_\theta}{T}(1-u^n)
\le\frac{\beta x}{1-\beta x}
< m_n
\le u^n\frac{B}{H-B\theta}=u^{n-1}u_\theta.
\]

The strict middle inequality follows from x≤δ_n≤m_n/[2β(1+m_n)]. Thus D_1 strictly decreases as θ increases, so its minimum is at θ_E, with no interior worse nuisance.

At θ_E, the likelihood ratio for an output with k hits is
L_k=[(1-u_ET_E)/(1-T_E)]^k u_E^{n-k}.
It increases strictly with k, L_0=u_E^n<1, and for k=1,

\[
L_1\ge1\quad\Longleftarrow\quad
u_E^{n-1}(1-u_E)\ge x,
\]

because 1−T_E≤x and 1−u_ET_E≥1−u_E. The strict condition holds on [0,δ_n], except k=1 is impossible at x=0 under H− and the same decision is plainly Bayes. Therefore the rule is Bayes-optimal for the simple θ_E pair, giving a lower bound on all compound tests. The previous monotonicity in θ gives a matching uniform upper bound. Equality proves (3); differentiation of T_E(x)=1−(1−η)x−ηx² proves (4).

The conservative δ_n is an **explicit sufficient phase radius**, not a claimed sharp transition threshold. It shrinks with n and does not supersede the sharp n=15 switching values in EC49FUM.

## Theorem 3 — a structural limit on nuisance-uniform Blackwell transport

For each **fixed** θ and 0≤x<y≤1, the experiment at y is a garbling of the experiment at x: independently flip each zero output at x to one with probability 1−T(θ,y)/T(θ,x), retaining existing ones. It transports both H− and H+ exactly.

However, for every 0≤x<y<1, there is **no single θ-independent binary Markov kernel acting identically on each trial** that performs this transport for *all* admissible θ and both hypotheses.

### Proof

Fix θ and let a be the proposed probability to output zero after input zero, and b the probability to output zero after input one. For an input with zero probability z the output zero probability is b+(a−b)z. Applying this to the two input zero probabilities T_x and uT_x and requiring output T_y and uT_y gives, after subtraction,

\[
a-b=\frac{T_y}{T_x},\qquad b=0,\qquad a=\frac{T_y}{T_x}.
\]

Consequently a θ-independent kernel would require r(θ)=T(θ,y)/T(θ,x) to be constant. But for 0≤x<y<1,

\[
\boxed{\frac{dr}{d\theta}
=\frac{1-y}{1-x}
\frac{\beta(y-x)}{[1-\beta x+\beta x\theta]^2}>0.}
\]

This contradicts θ independence. At y=1 the constant all-hit channel is the expected degenerate exception. This obstruction concerns **common one-bit product kernels**. It neither rules out all joint n-bit kernels nor establishes failure of global minimax monotonicity.

## Verification and context

The companion program \`EC49FUN_GENERAL_N_VERIFY.py\` (standard-library Fraction) executed locally with **PASS**. It checks the exact endpoint constants; the sufficient δ_n and endpoint threshold inequalities for n∈{1,2,3,5,15,17,50}; the exact endpoint Bayes formula for rational x; the strict explicit loss bound at four rational widths for each tested n; exact overlap decomposition for n≤5; and rational positivity witnesses for the nuisance-uniform kernel obstruction. These finite checks support but do not replace the universal symbolic proofs above.

For n=15, the deliberately conservative δ_15≈0.0000172956860839. The sharp n=15 crossover in EC49FUM is ≈0.0002797473, which is much wider. The all-width n=15 classification was not rerun or revised in this work.

Scientific dependence: the inherited clipped-price law at pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Exact observer laws are assumed as frozen; native physical interpretation and parent Bellman proof are not independently checked.

Researcher provenance: **EM-DIRECT-8454C6**, original session **MCP-44cfc4e6f2094f96861854ebefc77e84**. This is independent portable source research. No formal Task publication, active CLAIM, Result, Review or change to another owner is asserted.

## Useful next unit

Classify the least-favorable nuisance support and threshold/randomization structure for arbitrary n and positive x, without presupposing a one-parameter-independent Blackwell degradation. A concrete discriminating calculation is to search exact rational n,x witnesses where endpoint θ_E Bayes decisions fail compound minimax, and determine whether the least-favorable prior requires more than two nuisance support points. Preserve the full typed origins if extending beyond the binary observer.
