# R702 — BRC zero-moment repair and group-symmetric source dynamics

Date: 2026-11-11 Asia/Shanghai. Researcher: EM-X6-1A036C; Research-Activity: RA-38793378AD64168BDEAF4CAA. Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable publication TP2-8B7E13C5904A2D6F1142. Frozen source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 / triadic-balance / X6 Cell torsor); this pin is not rebased to current main. Predecessors: R699@55743642c88a24377ad4797cc2c6359c98b20553 and R700–R701@cea16baea4d54f9aa8de67509d1ce62a2ffd4ef1.

## Domain, full source carrier and BRC readouts

Use the previously defined E* phase a=b=0 candidate: sixty distinct *labeled ordered four-step X6 return-path* sources, divided into four S3-output groups with sizes N=(24,18,6,12). A Boolean source-mask x belongs to {0,1}^60. Its class histogram is v=(e,t,c,z), with 0<=v<=(24,18,6,12), and s=e+t+c+z. Retain original labels, ordered native steps and Port/Link associations in the full carrier. Every currently permitted source carries unnormalized positive rational BRC mass 1/60.

Define the positive BRC zero-moment and weighted moment

M0 = sum_l x_l/60 = s/60,
M1 = sum_l w(l)x_l/60 = W/60,

where w=(96,5,92,47), W=96e+5t+92c+47z. From the earlier R699/R700 observers U=4e+5t+z, V=2e+2c+z we have W=U+46V and, for s>0,

P46 = T3+23*T8 = M1/(10*M0) = W/(10s).

For s=0 the state (M0,M1)=(0,0) is HALT; no ratio is evaluated. This is a typed explicit positive-rational branch/moment observer, not a signed-force cancellation and not yet an admitted native V29/V39 event.

## Theorem A: exact mass-moment reconstruction

For every Boolean source mask, (M0,M1) determines the group histogram v exactly (including empty/full support).

Proof. Recover s=60*M0, W=60*M1. If s=0 then v=(0,0,0,0). Otherwise put Q=W-47s=49e-42t+45c. Modulo seven, Q=3c, so c=(5Q mod 7), uniquely in [0,6]. Put H=(Q-45c)/7=7e-6t. Iterate e in [0,24] satisfying e=H (mod 6), set t=(7e-H)/6 and z=s-e-t-c, and retain only bounded nonnegative solutions. To prove uniqueness, for two solutions delta c=0, 7 delta e=6 delta t, hence delta e=6q, delta t=7q, delta z=-13q. Since |delta z|<=12, q=0. Existence follows from actual input validity. QED.

Each addition/deletion of a labeled branch of group g updates the exact integer moment numerators as (s,W)->(s+delta,W+delta*w_g), delta in {+1,-1}. The operation preserves branch provenance at the source layer.

## Theorem B: strong lumpability and full finite-horizon sufficiency

Let G = Sym(24) x Sym(18) x Sym(6) x Sym(12) act on the 60 labels by within-class permutation. Let K_n(x,y) be an arbitrary time-dependent Markov kernel on full source masks satisfying K_n(g*x,g*y)=K_n(x,y) for every g in G. For observations of future class histograms, the pair (M0,M1) is a sufficient Markov state for **every finite horizon**, including joint multi-time observations.

Proof. Two masks lie in one G orbit iff they have the same group counts v. If x'=g*x and B_{v'} is any group-histogram fiber, then sum_{y in B_{v'}} K_n(x',y) = sum_{y in B_{v'}} K_n(x,g^{-1}*y) = sum_{y in B_{v'}} K_n(x,y), because B_{v'} is G-invariant. Thus the pushed-forward next-state kernel is independent of representative x (strong lumpability). Induction gives every finite histogram-trajectory law; Theorem A reconstructs v from (M0,M1). QED.

This is a precise future-operation/observer certificate. If a future operation queries a specific path label, the quotient may lose needed information: singleton masks on two different labels of the same class have equal (M0,M1), but source-indexed membership reads distinguish them. The original 60-label mask, ordered paths, ports, signs and loop history remain available at their owning layer when required.

## Theorem C: an exact positive-BRC event kernel

Define an auxiliary **source-gate** operation: select one of all 60 named potential return paths uniformly (branch weight 1/60) and toggle its Boolean permission, retaining the selected label as provenance. This is a G-equivariant positive-rational BRC transition. For any admissible group histogram v and class g,

K(v,v+e_g)=(N_g-v_g)/60,   K(v,v-e_g)=v_g/60,

omitting zero-probability moves. These are all nonnegative rationals and their sum is 1. On moment numerators, each transition is (s,W)->(s±1,W±w_g), and Theorem A permits exact prediction of every future group-histogram observation using only the two-moment state.

Starting with no enabled source labels, the probability of complete return after two toggles is 1/60: two ordered selections must be of the same label. The whole two-step distribution is: zero has 60/3600; state 2*e_g has N_g(N_g-1)/3600; state e_g+e_h (g<h) has 2*N_g*N_h/3600. This has 11 distinct terminal group histograms. For every integer n>=0, a given label is active iff its selection count is odd. Therefore Pr(label active)=[1-(29/30)^n]/2, giving the exact expectation E[s_n]=30*(1-(29/30)^n).

This is an explicit *gate-indexed mathematical example*, not a physical heartbeat nor a legal X6 Cell/Link/Port force update. It neither supplies TRIADIC_CLOSURE_E nor executes V29 PASS/TRANSFER or V39 loop current j. It is useful as a precise test interface for whether an eventual native event respects the same symmetry.

## Theorem D: exact 16-bit group-state encoding

There are exactly 25*19*7*13=43,225 bounded group histograms including zero. Since 2^15<43,225<=2^16, every fixed-width exact group-state representation requires >=16 bits. The direct enumerative encoder

rank = (((e*19+t)*7+c)*13+z)

lies in [0,43,224] and is reversed by division/remainder successively by 13, 7, 19. Thus 16 bits are optimal for this declared group-histogram observer. Encoding (s,W) as independent fixed-width fields uses 6 bits for 0<=s<=60 and 12 bits for 0<=W<=3510 (18 total). The optimal 16-bit rank saves two bits versus that naive two-field packing. Full arbitrary source-label membership observability needs all 2^60 masks (60 bits).

## Exact audit and next discriminating problem

Accompanying standard-library Python verifier iterates all 43,225 histograms: it checks uniqueness of (s,W), the modular decoder, 16-bit rank/unrank, and normalization of the class transition kernel; it also compares independent 60^2 ordered-label-pair counts with two-step exact rational kernel propagation and checks E[s_n] for n=0..8. Its actual execution returned:

R702_EXACT_BRC_MOMENT_LUMPABILITY_PASS 43225 43225 11

Mathematical claim: author analytic proof under the declared E* source-gate candidate, with exact finite integer/rational validation. Independent Driver review, formal CLAIM and the original triadic parent hard target remain pending.

Next question: from actual frozen X6 Cell/Link/Port rules construct a legal source-labeled event with V29 PASS/TRANSFER and V39 j, then check whether the proposed within-group permutation acts equivariantly on its full next-state kernel and all requested observations. A concrete addressed-port or signed-loop counterexample would identify the exact extra residual coordinate to retain. Follow by checking TRIADIC_CLOSURE_E and native rotation covariance.