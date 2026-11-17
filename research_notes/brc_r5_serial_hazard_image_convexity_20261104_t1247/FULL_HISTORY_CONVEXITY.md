# R5 structural lemma: full-history behavioral four-observer image is convex

Date: 2026-11-04 Asia/Shanghai. Research status: AUTHOR_PROVED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Related exact serial-hazard theorem: research_notes/brc_r5_serial_hazard_image_convexity_20261104_t1247/RESEARCH.md at immutable commit 45e9434afa34f375bcb4ba6fc3edf40dae8876ee.

## Model and statement

Let a finite rooted chance/control tree represent a two-law (P,Q) positive-mass BRC experiment. All control decisions under FULL can be selected independently at each *complete observed history* (including prior actions, origin and ordered source/route labels); the FULL behavioral policy uses arbitrary real local randomized actions. Chance kernels under both P and Q are fixed, have strictly positive probabilities where present, and do not depend on the policy. At each history the same conditional controller action probabilities are used under P and Q; P/Q differences are entirely in fixed chance/prior likelihood ratios. Terminal histories have fixed observer readouts, and each of the four coordinates (error_P,error_Q,time_P,time_Q) is an expectation of a fixed path payoff under the respective law. Randomized declarations can be represented as explicit control edges.

**Lemma (finite perfect-recall realization convexity).** The set of FULL *actual* four-observer vectors over all real behavioral policies is compact and convex. More strongly, the attainable joint terminal path occupancy vectors (under P and Q simultaneously) form a polytope whose Q coordinates satisfy linear nonnegative flow constraints and whose P coordinates are determined by fixed path likelihood ratios.

Consequently, in any such experiment with seedless LR a behavioral subclass of FULL,

    conv O4(FULL) = conv O4(LR)

is equivalent to

    O4(FULL) = conv O4(LR).

Thus if the R5 mother phenomenon (equal four-hulls but unequal actual images) occurs here, LR's *own actual observer image* must be nonconvex. This is a necessary structural condition, NOT an assertion that a candidate exists or that all LR images are nonconvex.

## Proof: full-history occupancy mixing, simultaneously for P and Q

For a FULL policy sigma, let m^Q_sigma(h) be Q mass arriving at a complete history h, and m^Q_sigma(h,a) its mass after choosing a. At a control node, m^Q_sigma(h,a)=m^Q_sigma(h) sigma(a|h), where the a probabilities sum to one. At chance nodes the outgoing masses equal the incoming mass times fixed Q transition probabilities; the analogous P transitions are fixed. Include P and Q initial masses at the roots.

Fix any two FULL policies sigma_0,sigma_1 and t in [0,1]. Define target Q occupancy masses for every complete history/action edge:

    m^Q(h)=t*m^Q_0(h)+(1-t)*m^Q_1(h),
    m^Q(h,a)=t*m^Q_0(h,a)+(1-t)*m^Q_1(h,a).

At each reachable control history define the NEW behavioral action probability

    sigma_t(a|h)=m^Q(h,a)/m^Q(h), if m^Q(h)>0;

otherwise choose any legal action law (that history is unreachable). This gives probabilities in [0,1] summing to one. An induction from the root over chance and control edges shows its Q occupancies agree with m^Q on every history. Crucially it conditions on the complete history, so no shared-node LR constraint is imposed.

For any fixed full history h, the policy-independent Radon–Nikodym path factor rho(h)=m^P_sigma(h)/m^Q_sigma(h) is the product of the initial P/Q prior ratio and exogenous chance transition likelihood ratios; the controller action probabilities cancel because the same behavioral coin is used under both laws. This factor is independent of sigma wherever Q mass is positive. Therefore m^P_sigma_t(h)=rho(h)m^Q(h)=t*m^P_0(h)+(1-t)*m^P_1(h). The same holds for action edges and terminal leaves. Every coordinate of the four-observer vector is a linear sum of fixed terminal payoffs weighted by these P/Q terminal masses. Hence

    O4(sigma_t)=t*O4(sigma_0)+(1-t)*O4(sigma_1).

The Q flow constraints, nonnegativity and normalization describe a bounded polytope; at histories with zero reach arbitrary local behavior does not change terminal flow. The P flow is its fixed linear likelihood-ratio transform, so the combined terminal occupancy set is a compact polytope. A linear image is compact and convex. QED.

The same statement is the familiar perfect-recall realization-plan/sequence-form convexity mechanism expressed in this particular positive BRC two-law observer notation. It is a mathematical tool/reduction, NOT claimed to be an unprecedented external theorem.

## Exact rational micro-check and an important failed shortcut

Suppose at one full history Q reaches under sigma_0 with mass 1/4 and continues with probability 1; under sigma_1 it reaches with mass 3/4 and continues with probability 0. Mix the two terminal distributions with t=1/2. The target reach is 1/2, the target continuing flow is 1/8, so the required continuation coin is (1/8)/(1/2)=1/4. **The pointwise average of the two coins is 1/2, which is wrong** at this history. This exact Fraction arithmetic was executed locally, yielding PASS_EXACT_MIXTURE_AT_A_HIDDEN_HISTORY: posterior_behavior=1/4.

## Limits and next discrimination

The claim uses unrestricted independent FULL action laws at complete histories, fixed finite transition kernels, and expectations of pathwise observables. It does not prove LR image convexity, full hull equality for any genuine diamond, or any source-blind occupation-flow characterization. LR's shared-action/seedless constraints may be nonlinear after reconvergence; whether those constraints leave a missing real-image point while retaining equal four-hulls is precisely open.

For the next genuinely two-reconvergence topology, compute LR's semialgebraic behavioral image after checking all FULL extreme four-vectors lie in the LR four-hull. Search for a nonconvex LR witness as the decisive second stage. Retain explicit source and route labels and signed four-observer components; no native X6 embedding or theorem admission is claimed. Frozen task scientific pins, P000 and ACTIVE worldview unchanged.
