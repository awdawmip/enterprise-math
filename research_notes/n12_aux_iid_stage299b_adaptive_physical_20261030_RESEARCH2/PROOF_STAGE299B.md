# Stage299-B — Adaptive observers and the exact two-label shared-IID-port gap

**Author proof, 2026-10-30; portable research / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.** This result concerns a finite, source-labelled, positive-rational BRC-style probability model. It is not a P000-native X6 theorem, Source Result, independent review or claim about empirical physics.

## Frozen research and control inputs

GLOBAL_KNOWLEDGE_V1 main@9e420b135a44bff76ce2118dca75bee161178b28; Enterprise Math main@483b519b6ff93042bf15db751ceb921dba2c47d0; original P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488 (the global startup projection points to an older original). The P000, ACTIVE Heartbeat X6/time, residual-fidelity worldview, Weighted BRC and portable research protocol were loaded. The immutable predecessor is Stage298-B at b2938ac32206e3e39a122426d23e3b73bbc06af2 in Draft PR #1736. Stage295-B.2 is earlier evidence, not relabelled as this theorem. Native status v0.6.11 returned research_authority_granted=false, registered_session_count=0, active_jobs=5/5. Control task listing returned CONTROL_QUOTA. Native owner and claim are unverified.

## Explicit probability model and observers

S is a provenance source with equal prior weights 1/3 for S=0,1,2. G is an independent fair visible context bit. The ordered bits X then Y have source-conditional law in word order (00,01,10,11):

~~~text
P0=(3,5,5,3)/16
P1=(2,6,6,2)/16
P2=(225,15,15,1)/256 = IID Bernoulli(1/16) twice.
~~~

The 24 source/context/word raw BRC branch weights are each (1/6) P_s(x,y)>0. They keep source, time order, distinct path and exact positive rational mass; no signed cancellation is used.

After observing (G,X), the examiner chooses B or C, perhaps randomly depending on that visible history, but not on S or a hidden simulator seed. B reveals Y precisely when G=0; C reveals Y precisely when G=1; otherwise the typed output is MASK. The scoring observation is the entire ordered path (S,G,X,action,Y-or-MASK). The examiner and simulator never directly read S. The deterministic adaptive policy pi_full=(B for G=0, C for G=1) reveals the complete raw (G,X,Y). A source-independent randomized examiner is a mixture of source-independent deterministic visible-history policies.

A deterministic compression ell maps the three sources into at most two persistent labels. The free class allows any normalized causal response kernels and private persistent seed, including dependence on past visible output and the chosen action. The physical class, for each retained label, first samples any real-valued joint law of (G,Theta), Theta in [0,1], allowing arbitrary pre-randomization and dependence between public G and Theta. Conditional on (G,Theta), X and Y are **independent with the same Bernoulli(Theta) rate**. The subsequent action only reveals/masks Y: no retuning, hidden-seed observation or intervention changing Y is permitted. The two labels can have different laws; permitting different hypothetical source-correlated Theta laws only strengthens the lower-bound adversary.

For policy pi, define the source-retaining average TV risk

~~~text
R_pi(ell,Q) = (1/3) sum_{s=0,1,2} TV(P_s^pi, Q_{ell(s)}^pi).
R_free^*(2) = inf_{ell,Q_free} sup_pi R_pi(ell,Q_free).
R_IID^*(2) = inf_{ell,Q_IID} sup_pi R_pi(ell,Q_IID).
~~~

The two classes refer to exactly these interfaces, not any enlarged joint-coupling or physical model.

## Theorem A — sharp adaptive minimax and nonzero continuum gap

~~~text
R_free^*(2) = 1/24;
R_IID^*(2) = 1/8;
R_IID^*(2) - R_free^*(2) = 1/12.
~~~

**Proof, part 1: force the relevant partition.** Both P0 and P1 give Pr(X=1)=1/2; P2 gives Pr(X=1)=1/16. The public X marginal is preserved under every examiner policy. If source 2 is merged with either source i=0 or 1, the same label forces the same simulator law Q for the two. By triangle inequality, their source-weighted TV risk is at least TV(P_i^pi,P2^pi)/3 >= |1/2-1/16|/3 = 7/48. A one-label compression also merges such a pair. Since 7/48 > 1/8, a global optimum in either class must merge precisely sources 0 and 1, with source 2 assigned the second label.

**Part 2: free lower and upper certificate.** The two source-word laws have TV(P0,P1)=1/8. For pi_full, any common simulated law Q for the merged pair has [TV(P0,Q)+TV(P1,Q)]/3 >= 1/24. The midpoint

~~~text
Q*=(P0+P1)/2=(5,11,11,5)/32
~~~

is realized by a source-blind causal kernel: first draw G fair, draw X fair, then draw Y with Pr(Y=1 | X=0)=11/16 and Pr(Y=1 | X=1)=5/16. On the unmerged source label reproduce P2 exactly. For every admissible examiner policy, applying the common observation kernel to Q* gives (P0^pi+P1^pi)/2; hence each pair TV equals half TV(P0^pi,P1^pi), and its weighted risk is TV(P0^pi,P1^pi)/3 <= 1/24 by total-variation contraction. The full-reveal policy attains equality. Therefore R_free^*(2)=1/24.

**Part 3: physical bound over all REAL pre-mixtures.** For every theta in [0,1], the shared-IID pair has Pr(X!=Y | G,theta)=2 theta(1-theta) <= 1/2. Integrating against an arbitrary measure on (G,Theta) retains Pr(X!=Y) <= 1/2; this inequality also holds after arbitrary source-correlated choices, if those are hypothetically allowed. But source 0 has Pr(X!=Y)=5/8, and source 1 has Pr(X!=Y)=3/4. Under pi_full, TV(P0,Q0) >= 1/8 and TV(P1,Q1) >= 1/4 for every shared-IID simulator, even when Q0 and Q1 are chosen separately. Weighted risk >= (1/8+1/4)/3 = 1/8. This argument covers ALL real-valued pre-randomized mixing laws, not merely finite rational support.

This bound is attained by setting Theta=1/2 and G fair on the merged label, giving Q=(1,1,1,1)/4. Direct exact comparison gives TV(P0,Q)=1/8, TV(P1,Q)=1/4. On the singleton label set Theta=1/16 and G fair, reproducing P2. Each other examiner policy acts as a common Markov postprocessing of the complete raw path, and thus its risk is no larger than under pi_full. This proves R_IID^*(2)=1/8 and the gap 1/12. QED.

The source covariance is -1/16 for P0 and -1/8 for P1. Any common-setting conditionally IID pre-mixture has Cov(X,Y)=Var(Theta)>=0. The obstruction is a typed joint relationship residual, not a mismatch of the equal one-visit marginals.

## Theorem B — genuine adaptive examiner effect

For an examiner compelled to choose one fixed action B or C independent of the current context and observation, the exact unrestricted free minimax is

~~~text
R_free,fixed^*(2)=1/48.
~~~

For the forced pair (0,1), a fixed action reveals Y on exactly half the fair-G mass and otherwise reports only X, whose marginal is identical for those sources. Their public TV is (1/2) TV(P0,P1)=1/16. Pair triangle inequality yields >=1/48. The same midpoint simulator above attains this for either fixed action, and every alternative source merge has public X risk >=7/48. The adaptive full-reveal examiner increases free minimax risk by 1/24-1/48=1/48. This theorem does not claim the fixed-action physical optimum.

## Theorem C — exact no-gap sufficient family

Let three sources have equal weights; the examiner has any common, source-independent visible-history-adaptive observation language. Suppose the **full original counterfactual law** for EACH source can already be produced by the same physical interface: a source-specific joint pre-mixture mu_s(G,Theta) followed by two conditionally IID same-Theta draws and the identical downstream action/readout rule. Source-correlated *original* parameters are allowed because the original sources are known before compression. The compressed simulator may pre-randomly mix the physical parameter laws for a retained label.

For this declared class,

~~~text
R_free^*(2) = R_IID^*(2)
            = (1/3) min_{i<j} sup_pi TV(P_i^pi,P_j^pi).
~~~

**Proof.** Every <=2-label assignment merges at least one pair i,j; for every policy pi the source-tagged triangle inequality gives risk >= TV(P_i^pi,P_j^pi)/3. Therefore, after the supremum and infimum, every compressor is bounded below by (1/3) min_pairs sup_pi TV(P_i^pi,P_j^pi). Choose a pair realizing that finite minimum. Use the physical pre-mixture mu=(mu_i+mu_j)/2 on its shared label and exactly reproduce the third source using its own mu. Because the SAME source-independent future observation/operation kernel is applied after the pre-mixture, the merged path law for every policy is Q^pi=(P_i^pi+P_j^pi)/2. The weighted risk therefore equals TV(P_i^pi,P_j^pi)/3 simultaneously for every adaptive policy. It attains the lower bound in BOTH free and physical classes. QED.

Example: with fair G and original source Theta values (1/4,1/2,3/4), the three full-word TVs are respectively 5/16, 1/2, 5/16. Two labels suffice with exact free/physical minimax 5/48 by mixing Theta=1/4 and 1/2 equally on one label. All observed source words remain strictly positive. This is an exact no-gap class, not a statement about the arbitrary nonphysical originals of Theorem A.

## Reproducible evidence, literature context and limits

REPRO_STAGE299B.py (Python standard library Fraction), actually executed, checks positivity and exact normalization of all 24 source/context/word paths, exhaustive 16 deterministic visible-history-action policies, source pairing exclusion, both minimax primal/lower certificates, the fixed-action free result, 17 rational parameter probes, 17 rational two-atom pre-mixture probes, and the strictly positive all-physical no-gap witness. Actual captured stdout: REPRO_STAGE299B_EXECUTED_STDOUT.txt, ending in STAGE299B_ADAPTIVE_SHARED_PORT_EXACT_PASS. The enumerations are exact for their stated finite sets; arbitrary real pre-mixtures and randomized examiner policies are covered by the mathematical inequalities and contraction arguments above. No Lean formal proof, external independent reviewer, empirical data, or native X6 bridge was performed.

BRC resolution REUSE_APPLIED: source-labelled positive branch masses, serial composition and ordered-future observer from definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json. G,X,Y are external auxiliary bits, not native three-dimensional slice coordinates or three X6 axes. Time/order remains typed and distinct from the six native spatial axes. A native lift needs one-axis signed path semantics, branch identity/multiplicity, triadic force closure, time and six-field lossless address, and a commuting observer/future map.

Methodological background only, not support for novelty of this exact witness: Bernhard von Stengel (1996), Efficient Computation of Behavior Strategies, Games and Economic Behavior 14, 220–246, DOI 10.1006/game.1996.0050 (finite behavior/sequence-form); Persi Diaconis and David Freedman (1980), Finite Exchangeable Sequences, Annals of Probability 8, 745–764, DOI 10.1214/aop/1176994663 (finite exchangeability).

**Stage300-B:** test commuting-mixture stability under source-sensitive interventions, or construct an exact positive-rational counterexample with full causal/adaptive future operators; keep the P000 native X6 bridge separate and Stage278-A Bellman N=12 distinct.
