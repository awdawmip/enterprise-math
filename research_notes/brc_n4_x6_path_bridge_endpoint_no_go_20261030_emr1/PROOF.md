# A typed X6 path realization of BRC N=4 and a sharp endpoint-only no-go

**Date:** 2026-10-30 23:00 Asia/Shanghai. **Status:** AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is a finite path-representation result, not a native physical evolution theorem.

## 1. Frozen source and research target

The external 16-leaf experiment has S in {AU,AV,BU,BV}, J,K in {0,1}. Both source laws have positive weight at every leaf:

\[
Q(s,j,k)=q_s/4,\qquad P(s,j,k)=q_s r_{s,j}/4,
\]
where \(q=(1/6,1/3,1/4,1/4)\) and the four ordered ratio pairs are \(r_{AU}=(9/10,11/10),r_{AV}=(1/4,1/4),r_{BU}=(1/5,9/5),r_{BV}=(2,2)\). Integer numerators over 240 are Q=[10,20,15,15] for each j,k and P=[(9,11),(5,5),(3,27),(30,30)] for each k. Both sums are 240.

Native input is P000 V5's SIX-dimensional affine Cell torsor \(X\) for \(G=\mathbf Z^6\), with native primitive signed unit-axis steps \(\pm e_i\). There is no distinguished global Cell origin. Time is a separately typed ordered parameter, not a seventh spatial axis. Our target is an exact representation of the external weighted observation experiment *inside native X6 path syntax*, preserving lawful stagewise prefixes, and an explicit statement of what P000 itself does not provide.

## 2. Two cell-only obstructions (unconditional statements about the declared X6 torsor)

**Theorem 1a (trivial-label translation invariance).** Let A be any label set with trivial G-action. If a deterministic Cell-only observation \(f:X\to A\) satisfies \(f(x+g)=f(x)\) for every \(x\in X,g\in G\), it is constant. Proof: transitivity of the torsor provides \(g=y-x\) between any two Cells. Therefore \(f(y)=f(x)\).

**Theorem 1b (no normalized spatially uniform probability).** There is no countably additive probability law \(\mu\) on the *absolute* countably infinite Cell set X invariant under all G translations. Indeed every singleton has the same mass a. If a>0 its infinite sum diverges; if a=0 countable additivity gives total zero. Thus P000 Cell identity plus unrestricted translation invariance alone neither selects 16 nonconstant absolute labels nor determines the two source probability laws.

These are **scoped** obstructions: a chosen anchor, a relative path word, an internal relation, or a nontrivial label action evades the first hypothesis; a probability law on a finite family of relative paths evades the second. No impossibility of a native probabilistic extension is claimed.

## 3. Constructive, translation-covariant path bridge

Choose a temporary native Cell anchor \(o\), four distinct native axes \(e_1,e_2,e_3,e_4\), and five ordered instants \(\tau_0<\tau_1<\tau_2<\tau_3<\tau_4\). These are explicit *interface choices*, not new ontology. Encode

\[
s=AU,AV,BU,BV\ \longleftrightarrow\ (\sigma_1,\sigma_2)=(+,+),(+,-),(-,+),(-,-),
\]
\[
\sigma_3=(-1)^j,\qquad \sigma_4=(-1)^k,\qquad
x_m=o+\sum_{i=1}^{m}\sigma_i e_i\quad(0\le m\le4).
\]

Every \(x_{i-1}\to x_i\) is exactly one allowed signed native-axis step; the *four-step compound trace* is not called a primitive diagonal segment. All 16 sign words are different and, on this **restricted fixed-axis-order family**, even the relative endpoint \(x_4-o=(\sigma_1,\sigma_2,\sigma_3,\sigma_4,0,0)\) is injective. The last two zeros are relative chart components in this witness and neither suppress the ambient six axes nor identify a three-dimensional 晶包 layer.

Let \(\iota\) carry a leaf \((s,j,k)\) to its ordered potential native trace, and let \(\rho\) read the first two step signs as s, the third as j, and fourth as k. Then \(\rho\circ\iota=id\). Translating o and every \(x_m\) by the same g leaves the relative word and \(\rho\) invariant. Assign *external, expressly specified* path probabilities \(\nu_L=\iota_*\mu_L\) for L=P,Q. Hence

\[
\rho_*\nu_L=\mu_L \quad (L=P,Q)
\]

**exactly**, not approximately. The finite law is thus realizable as a positive-weight BRC distribution on a selected family of P000-admissible primitive path words, with no global spatial origin.

The full four-step word is a **potential full leaf**. Under an actual stopping policy the *realized* path is truncated at the stop time: latent later steps in the sample space do not assert physical motion after stopping.

## 4. Causal operations and joint-law preservation

The time-one prefix reveals the A/B sign, the time-two prefix reveals s, the time-three prefix reveals J, and on paths reaching time four the fourth sign reveals K. The original S2/S23 grammar observes/stops/continues and chooses terminal P/Q labels; it has no declared operation rewriting K. At the t2 s-nodes the two-law likelihood ratios are \(1,1/4,1,2\) respectively; at t3 and t4 the ratios are \(r_{s,j}\), constant over k. Thus the original equal-contemporaneous-ratio restrictions are carried without change by the bijective prefix coding.

For any finite randomized, source-law-independent *causal* behavioral policy H on the declared S2 or S23 prefix-information language (including the same independent decision coins under both laws), its induced native-path policy is \(H\circ\rho\), evaluated only when its required prefix is exposed. Consequently

\[
(\rho,\text{transcript})_*\bigl(\nu_L\ltimes (H\circ\rho)\bigr)
 = \mu_L\ltimes H,\qquad L=P,Q.
\]

This is a commuting *representation* identity for the complete joint observed transcript, including a common J-based auxiliary sensor Z if its explicitly provided source-independent noise kernel is composed. It does not construct a native physical noise mechanism or heartbeat-time dynamics.

A nontrivial exact witness uses lawful S2 BU continuation \(u_0=1/4,u_1=3/4\) and, after T4 observation, terminal decision P iff J=K (not S23). Keeping E for stopped AV/BV, A for AU, B3 for stopped BU and B4Pk/B4Qk for continued BU gives the numerator distributions (common denominator 960)

\[
P_Y=(560,160,72,3,81,81,3),\quad
Q_Y=(560,160,120,15,45,45,15)
\]

in order E,A,B3,B4P0,B4P1,B4Q0,B4Q1. Therefore \(TV(P_Y,Q_Y)=3/40\). These exact numbers are independently checked from the 16 path words by VERIFY.js. The source noise example \(\varepsilon=1/4\) gives BU,Z=0 masses 72/960 under P and 120/960 under Q.

## 5. General exact endpoint-fiber safety certificate

**Theorem 2 (finite fully supported two-law path experiment).** Let Ω be any finite family of native paths, μ_P, μ_Q strictly positive on Ω, and let π:Ω→U be a deterministic endpoint or other observer. There exists one *law-independent* stochastic decoder \(R(d\omega\mid u)\) reconstructing the complete joint law \((\pi(\omega),\omega)\) from observed π under both laws **iff** for every fiber \(F_u=\pi^{-1}(u)\),

\[
\boxed{\frac{\mu_P(\omega)}{\mu_Q(\omega)}
       =\frac{\mu_P(F_u)}{\mu_Q(F_u)}
       \quad\text{for every }\omega\in F_u.}
\]

Necessity follows from \(\mu_L(\omega)=\mu_L(F_u)R(\omega\mid u)\) for L=P,Q. Sufficiency chooses \(R(\omega\mid u)=\mu_Q(\omega)/\mu_Q(F_u)\). A reverse kernel on the complete *joint* path then composes with every law-independent future readout H of that same path (when physically causal), so the criterion is observer- and operation-horizon safe for those kernels. It is not a criterion for merely reproducing path marginals while discarding the retained endpoint coupling.

Our 16 fixed-order paths satisfy the certificate trivially because π is injective. General native path families need not.

## 6. Exact minimal endpoint-loss witness

Take two two-step native paths from the *same chosen anchor*:

\[
\omega_{12}: (+e_1,+e_2), \qquad
\omega_{21}: (+e_2,+e_1).
\]

Both end at \(o+e_1+e_2\), hence their complete signed six-coordinate endpoint is identical; their \(\tau_1\) Cell and ordered history differ. Assign strictly positive path weights

\[
P(\omega_{12},\omega_{21})=(3/4,1/4),\qquad
Q(\omega_{12},\omega_{21})=(1/4,3/4).
\]

Let Y read which primitive axis was used first. Then \(TV(P_Y,Q_Y)=1/2\), whereas the endpoint-only laws coincide and have TV zero. Every P/Q-common simulator from endpoint alone yields one output law R; the triangle inequality forces \(\max_L TV(L_Y,R)\ge1/4\), attained by the midpoint uniform law. One retained path-order bit exactly repairs the entire two-path experiment, and a constant label cannot. This witness uses *full six-dimensional Cell coordinates*, not a defective lower-dimensional projection.

Therefore an endpoint-only quotient may be exact for the restricted sixteen fixed-order words while failing immediately after permitting legitimate primitive-step reordering or time-one history observation. The obstruction is a concrete BRC path-provenance residual; it is not an assertion about physical energy or signed-amplitude cancellation.

## 7. Verified scope and next bridge obligations

All displayed universal theorems have direct proofs. VERIFY.js actually executes exact integer checks for all 16 leaves, primitive-step and translation covariance, normalization, path/leaf inverse, an S2 joint transcript, a noisy-sensor pushforward and the two-path collision, including its conditional-likelihood fiber failure. Checks validate the implementation and finite examples, not external physics.

**Reused interfaces:** P000 V5 X6 affine torsor and signed native path calculus (REUSE_APPLIED); positive rational Weighted-BRC leaf/source provenance (REUSE_APPLIED); joint-relation observer fiber/descent rule (COMPOSE_APPLIED). The finite common inverse-kernel criterion is a specialization of classical statistical sufficiency/Blackwell comparison, not claimed as a new general theory.

**Precisely outstanding:** P000 does not specify the two measures \(\nu_P,\nu_Q\), a stochastic native selection law for s/J/K, a physical realization of the auxiliary sensor, or a heartbeat transition program with calibrated \(\tau_i\). Our representation supplied these as *external typed choices*; deriving them from an independently justified native law is a separate scientific/empirical obligation. Nor has this construction established an allowed native operation rewriting K. P000 and ACTIVE worldview files are unchanged.

**Governance:** frozen inputs below; author-side proof and checker only. Native Site reported research_authority_granted=false at 2026-10-30T15:00:29Z and Owner enumeration returned CONTROL_QUOTA. No canonical CLAIM, native Result, independent Driver review, Lean checker or Foundation promotion is claimed.