# EC49B — Four-stage future signal: exact strict separation and likelihood-ratio-spectrum quotient

Date: 2026-10-28 (Asia/Shanghai). Role: TASK_RESEARCH; portable author-side derivation with shared author context from EC49A (not independent Driver review). Local contribution tag: R4-EC49B-20261028-1134-LOCAL, not a service-issued Researcher/session/Activity identity. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED.

## Frozen authority, sources and interpretation

Single GLOBAL_KNOWLEDGE_V1 canonical read snapshot: awdawmip/chatgpt-global-knowledge main@3bb22d0180e44ab7efaea8c18630ba39aab0b77e; entry files, P000 projection and original with matching original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview and mathematics/code/handoff/BRC rules read. Separate Enterprise Math main scientific read: fc58c221e06739e3428e299952ad01d23c996cb0; read AGENTS, p000_reality_foundation.json, native X6+time, joint-relation preservation, autonomous and portable protocols. Frozen direct predecessor EC49A: Draft PR #1615, immutable head 189326aca4a8eab0dd574183d81076ecec05e778 (PROOF.md, NEXT_TASK.md). Native service reported research_authority_granted=false; active owner control query returned CONTROL_QUOTA. No CLAIM, Source Activity, Result or independent review is asserted. Earlier explicitly rejected activity write was not retried or bypassed.

The present paper is about a finite strictly-positive rational dual-source P/Q probabilistic BRC *auxiliary* stopping observer, with a fixed one-state memory. It is not a signed-amplitude BRC computation, native six-axis X6 Cell embedding, three-dimensional X6 slice or physical heartbeat law. Decision counter T=1..4 is not a physical heartbeat time. Project P000 and ACTIVE worldview are not modified. The eventual typed native-state/observer/future-operation bridge remains an independent proof obligation.

## A. Sixteen-leaf exact four-stage counterexample

Let H,Z,W,V be binary. Under both sources P(H=h)=Q(H=h)=1/2. Define Z independent of H:

| z | PZ(z) | QZ(z) |
|---|---:|---:|
| 0 | 1/4 | 3/4 |
| 1 | 3/4 | 1/4 |

The source-neutral W kernel is K(W=1|H=0)=1/4, K(W=1|H=1)=3/4. The future source-conditional V=1 kernel, independent of Z given H,W, is:

| H | W | P(V=1|H,W) | Q(V=1|H,W) |
|---|---|---:|---:|
| 0 | 0 | 17/24 | 7/24 |
| 0 | 1 | 7/8 | 1/8 |
| 1 | 0 | 3/8 | 5/8 |
| 1 | 1 | 7/8 | 1/8 |

For s=P,Q, the entire strictly positive 16-leaf distribution is

P(h,z,w,v)=(1/2) PZ(z) K(w|h) PV(v|h,w),
Q(h,z,w,v)=(1/2) QZ(z) K(w|h) QV(v|h,w),

with V=0 masses the complements. All 16 reduced rational P,Q masses and P/Q are in the executed EXACT_REPORT.json. Both sources sum to 1 exactly and every leaf has positive weight.

The t1 readout is H, action acc/rej/cont. After t1 the fixed sole memory register is reset and H erased. The t2 readout is a constant y plus complete fine-history LR 1, action acc/rej/cont. After continuation, at t3 the refined observer sees (Z,W,lambda_z), while the coarse observer sees (Z,lambda_z) only, both with acc/rej/cont. Here lambda_z=PZ(z)/QZ(z), either 1/3 or 3. After t3 continuation, t4 readout for both is (Z,V,L_full), with acc/rej, where L_full=lambda_z PV(v|h,w)/QV(v|h,w). Reading the exact LR at time 4 is allowed to reveal earlier information through a **current** observation, not through a retained hidden register. Policies are source-neutral behavioral distributions depending on the specified current readout only, with no persistent common random seed. Stopping T is the selected decision time, and O=(alpha,beta,E_P T,E_Q T), alpha=P(acc), beta=Q(acc).

### A1. Source ancillarity and an H-independent one-step V marginal

At every reachable t3 prefix, the conditional mixture of H is equal under P,Q, because t1/t2 decisions depend only on H or the shared y with source-neutral probabilities. Hence the conditional law of W given Z and survival is identical under P,Q; W is source-ancillary at t3. Nonetheless two policies selecting respectively only H=0 or H=1 at t1 give the same positive live t2 mass 1/2, same readout y and LR 1, yet Q(Z=1,W=1|survival,t2 cont)=1/16 and 3/16. This preserves EC49A's strict 1/8 failure of policy-independent fine prediction.

Furthermore, independently for each h,

sum_w K(w|h) PV(V=1|h,w) = 3/4,
sum_w K(w|h) QV(V=1|h,w) = 1/4.

The full binary V law before any t3 selection is therefore independent of H under each source (conditioned on Z). V is genuinely informative about P vs Q. The joint (H,W,V) relationship remains relevant when the observer may decide whether to continue after seeing W.

### A2. Exact strict separation of the entire raw four-vector regions

Let F(O)=alpha-beta-(E_P T+E_Q T)/16. At t4 the source-neutral terminal decision accepts iff L_full>1, which maximizes alpha-beta because Q mass times (L_full-1) is the local contribution.

For fixed finite behavioral decision simplexes the objective is multiaffine: holding all but one action-distribution fixed yields a linear function of that simplex. An extremum over the compact product is thus attained at deterministic behavioral strategies by optimizing one simplex at a time. This argument is sufficient for a support maximum; no convexification of the raw region is assumed.

All t1 and t2 accept/reject actions have zero alpha-beta contrast because LR=1, and continuation adds nonnegative time cost. Any support-maximizing strategy can either stop at t1 (value -2c, c=1/16), or select a subset S of H histories at t1 and continue those through t2 to t3. A t2 stop is never better than the immediate stop choice.

For w=0,1 define k_S(w)=sum_{h in S}(1/2)K(w|h). Define

d_S(z,w)=k_S(w)(PZ(z)-QZ(z)),

g_S(z,w)=sum_{h in S,v} [ (1/2)K(w|h)(PZ(z)PV(v|h,w)-QZ(z)QV(v|h,w)) ]_+ - c k_S(w)(PZ(z)+QZ(z)),

where [x]_+=max(0,x). For a fixed z,w, d is immediate accept/reject contrast and g is the maximal terminal LR-based contrast after continuation minus the additional time-4 survival cost. Full-LR collisions do not alter the positive-part optimization: equal LR gives the same sign of the likelihood contrast, so aggregates of equal-ratio atoms may be optimized together.

The exact support max conditioned on a t1 survivor subset S is

F_coarse(S) = -2c - 2c|S| + sum_z max(0, sum_w d_S(z,w), sum_w g_S(z,w)),

F_refined(S) = -2c - 2c|S| + sum_{z,w} max(0,d_S(z,w),g_S(z,w)).

The -2c term is the unavoidable t1 stopping-time cost, and -2c|S| accounts for the two additional time-step survival costs of exactly the selected H histories. Substitution of the rational kernels yields the following complete four-case table:

| S | Coarse max F | Refined max F |
|---|---:|---:|
| empty | -1/8 | -1/8 |
| {0} | 0 | 1/64 |
| {1} | 1/32 | 3/64 |
| {0,1} | **1/8** | **3/16** |

Therefore over **all real source-neutral randomized behavioral policies in the specified model**,

max F(S_coarse)=1/8,
max F(S_refined)=3/16,
max F(S_refined)-max F(S_coarse)=**1/16 > 0**.

An attaining refined controller continues for both h at t1 and at t2. At t3 it rejects on (z,w)=(0,0), continues on (0,1), accepts on (1,0), and continues on (1,1); at t4 it accepts iff L_full>1. Its exact four-vector is

**O_refined = (13/16,3/16,7/2,7/2)**, F=3/16.

An optimal coarse controller continues t1/t2, accepts at t3 iff z=1, and gets O_coarse=(3/4,1/4,3,3), F=1/8. By linearity, the refined witness lies outside even the convex hull of the coarse **raw** region, and hence outside the raw region itself.

Exact Fraction code exhaustively checked all 3^2 * 3 * 3^2 = 243 coarse and 3^2 * 3 * 3^4 = 2,187 refined deterministic **preterminal** strategies, with each terminal strategy optimized by the exact full LR sign, and obtained the same support maxima. A separate exact evaluation checks all four S-formula rows and the explicit four-vector. The universal support claim follows the multiaffine extremum argument and analytic case table, not the finite test alone.

This refutes the sufficiency of (i) W being source-ancillary and (ii) the unselected marginal V distribution conditional on H,Z being H-independent. It does not refute exact causal future-kernel equivalence.

## B. Sufficient theorem: invariant conditional likelihood-ratio spectrum

**Theorem B — one final remaining decision, full raw four-vector preservation.**

Fix a finite coarse t3 observation z. Assume (1) all reaching fine histories in z have the same LR lambda_z>0 and W conditional on z has a common source-neutral distribution kappa_z(w) under P and Q, possibly depending on the earlier survival policy; (2) when the observer continues at t3, the final readout Y has strictly positive source kernels K_P^w(y),K_Q^w(y), and its exact observable complete LR is L_full=lambda_z R_w(y), where R_w(y)=K_P^w(y)/K_Q^w(y); the one-state terminal controller can use z,L_full without retaining W; (3) for each attainable r the **conditional Q-distribution of R**,

nu_z(r)=sum_{y:R_w(y)=r} K_Q^w(y),

is the same for every reached w. Then observing or hiding W at t3 gives **exactly equal raw regions of all four original outputs**, for all real source-neutral randomized behavioral policies, without requiring the raw label distribution of Y to be W-independent.

**Proof, refined to coarse.** Given any refined controller, write pi_w(a), a=acc/rej/cont, for its t3 action distribution, and mu(a)=sum_w kappa(w)pi_w(a). Because kappa is source-neutral and z has a fixed LR, replacing pi by mu reproduces both P,Q immediate acceptance, rejection and continuation masses at t3. Thus t3/t4 survival probabilities and the two stopping-time expectations are unchanged.

Let a_w(y) be the refined terminal acceptance probability, conditional on current terminal information; its actual use depends on terminal readout, not on remembered W. For any r with mu(cont)nu_z(r)>0 set

a_bar(r) = [sum_w kappa(w)pi_w(cont) sum_{y:R_w(y)=r}K_Q^w(y)a_w(y)]/[mu(cont)nu_z(r)].

It is a valid probability in [0,1]. If the denominator is zero, choose an arbitrary legal action. The coarse terminal policy may use this function of z and current L_full=lambda_z r. The Q acceptance mass in each r fiber is then identical to the refined policy by construction. P/Q= lambda_z r is constant on that fiber, so P acceptance mass is simultaneously preserved, not calibrated by an independent P controller. Sum over fibers and previous observations to preserve alpha,beta. Survival mass equality preserves E_P T,E_Q T. The resulting **one source-neutral coarse policy** realizes precisely the refined raw four-vector. Conversely, a refined policy can ignore W, proving equality. QED.

This is a **one-stage terminal result**. It does not assert preservation of hidden-W joint laws, more general future W-conditioned operations, or native signed BRC/X6 dynamics.

### B1. Strictness: unequal full V kernels but equal conditional LR spectra

Retain the H,Z,W kernels and all legal t1..t4 actions, but replace the V experiment by the following strictly positive W-dependent law, now independent of H:

- W=0: P(V=1)=3/4, Q(V=1)=1/4.
- W=1: P(V=1)=1/4, Q(V=1)=3/4.

Both raw P and raw Q laws of the terminal V label differ across W, so **W-independent full future output law fails**. Yet for both W values the distribution under Q of r=PV(v|w)/QV(v|w) is identical:

nu(1/3)=3/4, nu(3)=1/4.

Theorem B therefore applies even if t1 selects different hidden-H mixtures and the fine (Z,W) kernel remains policy-dependent and violates the stronger EC48Z reachable-kernel invariance. The verifier checked 800 seeded arbitrary rational source-neutral randomized policies and their **single-policy** W-hiding simulations by exact Fraction arithmetic. The theorem applies to all real policies by its proof.

For this witness the same raw four-region has an explicit exact rational occupancy LP. Let u[h,a]>=0 with sum_a u[h,a]=1/2 and x2=sum_h u[h,cont]. Let v[a]>=0 with sum_a v[a]=x2; put x3=v[cont]. Let y[z,a]>=0 with sum_a y[z,a]=x3 QZ(z), and L_z=PZ(z)/QZ(z). For each z,r let b[z,r] be Q accepted mass at terminal, constrained by 0<=b[z,r]<=y[z,cont]nu(r). The outputs are exactly

alpha=sum_h u[h,acc]+v[acc]+sum_z L_z y[z,acc]+sum_{z,r} L_z r b[z,r];

beta=sum_h u[h,acc]+v[acc]+sum_z y[z,acc]+sum_{z,r} b[z,r];

E_P T=1+x2+x3+sum_z L_z y[z,cont];

E_Q T=1+x2+x3+sum_z y[z,cont].

All LP coefficients are rational. Every fine policy maps to this LP by the above LR-fiber averaging. Conversely any feasible LP point yields a legal **single** coarse controller via pi1(a|h)=2u[h,a], pi2(a)=v[a]/x2, pi3(a|z)=y[z,a]/(x3 QZ(z)), pi4(acc|z,r)=b[z,r]/(y[z,cont]nu(r)), with arbitrary legal distributions on zero-mass fibers. This proves exact raw-region equality to a rational LP projection; a rational feasible target for **this particular model** admits a rational behavioral lift. It leaves open the general "irrational-only rational four-vector lift" question outside such LP subclasses.

## Evidence, limits and next question

Actual VERIFY.py uses Python standard-library fractions.Fraction, no floating-point tolerance. Its executed EXACT_REPORT.json contains all sixteen exact positive leaf weights, likelihood ratios, source totals and t1 marginal identities, the four-case analytic certificate, exactly 243+2187 deterministic preterminal controller checks with optimal LR terminal behavior, the 1/16 support gap and explicit witness, and 800 seeded forward/reverse exact simulations of the B1 sufficient theorem witness. A universal all-real mathematical result rests on the complete arguments above; the finite checks validate the exact constructions and implementations only.

This is a prior-art-aware application of the Blackwell experiment-comparison / conditional sufficiency and occupancy-measure ideas, not a priority claim over those classical results. External sources are recorded in SOURCES.md. Independently validating the proof, native Source Result/admission, and a typed relation/observer/operation embedding into signed BRC and X6 require their own authority and evidence.

Next proposed author-side unit **EC49C**: determine whether invariant conditional LR spectrum is necessary for universal deletion of W at the penultimate decision under the specified observation/action language, or find a strictly weaker exact causal/Blackwell sufficient condition; extend to a genuinely two-step future controlled experiment. Separately carry the unresolved question of rational four-vectors with only irrational legal behavioral lifts in general non-R models.
