# R5 K3 — supercritical clock-hull rigidity by two dual switching thresholds

Date: 2026-11-04, Asia/Shanghai. Scientific status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific inputs: GLOBAL_KNOWLEDGE_V1 a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e.
Predecessor: research_notes/brc_r5_k3_equal_mu_clock_no_go_20261104_t0640/RESEARCH.md at immutable commit 9ec0241798f73019347071cc6b12a67d10b05fb4. The model, positive source capacities and masks are inherited. P000 and ACTIVE worldview are unchanged. This theorem is inside the auxiliary K3 observer model and does not assert a native X6 physical embedding.

## Model, observer, theorem

Four distinct BRC provenance sources S=(C,I,BJ,IJ) have positive capacities c=(1/8,1/6,1/16,3/32). FULL upstream variables obey 0<=x,y<=1 and 0<=i<=1-x; seedless LR requires i=(1-x)y. Their source weights are w=(1/8,(1-x)/6,y/16,3i/32). FULL independently selects z_s,t_s,u_s in [0,1]; LR has common z,t,u. Set M_s=w_s z_s, S_s=2 M_s t_s/3, U_s=S_s u_s. The stop-time observer is

TP=3+sum M_s+(3/2)sum S_s+sum r_s U_s,
TQ=3+(1/2)sum M_s+(3/8)sum S_s+(1/4)sum v_s U_s.

Let O_clock=(TP,TQ). All quantified behavioral policies below may have arbitrary real parameters, rather than only deterministic or rational inputs.

**Theorem (supercritical rigidity).** For every 0<r_s,v_s<1 with

mu_s=(9+2v_s)/(8(3+r_s)) >= 3/8, equivalently v_s>=3r_s/2, for ALL four sources,

conv O_clock(FULL) = conv O_clock(seedless LR) if and only if r_C=r_I=r_BJ=r_IJ and v_C=v_I=v_BJ=v_IJ. Every heterogeneous clock satisfying this hypothesis has a strict signed time-support separator. Hence the full four-observer convex hulls also differ for any independent p_s,q_s in (0,1).

## Complete analytic proof

For arbitrary signed clock normal (a,b), the source-stage gains (after subtracting common 3(a+b)) are

g0=0,
g1=a+b/2,
g2=2a+3b/4,
g3_s=(2+2r_s/3)a+(3/4+v_s/6)b.

Every source capacity c_s is simultaneously attained by FULL using x=0,y=1,i=1. The FULL support is therefore exactly 3(a+b)+sum_s c_s max(0,g1,g2,g3_s). An LR local stage is shared. The LR objective is multi-affine in the real decision variables (in particular, after seedless substitution i=(1-x)y); extrema occur at deterministic common stages and upstream corners. Every LR source weight w_s is at most c_s.

**Mixed-stage lemma.** If J=max(0,g1,g2)>0 and some g3_s>J while some g3_t<J, then h_FULL>h_LR. FULL picks stage 3 on s and a common baseline J stage on t, at simultaneous full capacities. Any LR common stage other than 3 misses the positive improvement on s. Any LR common stage 3 has t contribution at most c_t max(0,g3_t)<c_t J. Every other LR source contribution is bounded by its FULL per-source optimum. The finite set of LR deterministic extrema therefore has strictly smaller support. This proves the lemma over all real strategies.

Define alpha_s=v_s/(4r_s) and nu_s=(3+2v_s)/(4(3+2r_s)). The supercritical hypothesis implies alpha_s>=3/8 and 1/4<nu_s<1/2. The latter lower bound follows from nu_s-1/4=(v_s-r_s)/(2(3+2r_s))>0, and the upper bound follows from 0<v_s<1, r_s>0.

**Route A (distinct nu).** If the nu_s are unequal, select min nu_s < tau < max nu_s and normal (a,b)=(-tau,1). Here 1/4<tau<1/2; J=g1=1/2-tau>max(0,g2). The identity
g3_s-g1=(1+2r_s/3)(nu_s-tau)
has both strict signs across source labels. Apply the mixed-stage lemma.

**Route B (equal nu, distinct alpha).** If the nu_s are equal and alpha_s are unequal, choose min alpha_s < tau < max alpha_s and normal (a,b)=(tau,-1). Here tau>3/8, J=g2=2tau-3/4>max(0,g1), and
g3_s-g2=(2r_s/3)(tau-alpha_s).
Again there are both signs and the mixed-stage lemma applies.

**Completeness.** Suppose alpha_s and nu_s are both constant across sources. Put k=4alpha>=3/2; then v_s=k r_s. Equal nu at sources i,j implies
(3+2k r_i)(3+2r_j)=(3+2k r_j)(3+2r_i),
so 6(k-1)(r_i-r_j)=0. Since k>=3/2, all r_s and therefore all v_s are uniform. Thus all heterogeneous parameters are covered by Route A or B.

Conversely, with uniform r and v, the gains g0,g1,g2,g3 are source-independent for every signed (a,b). FULL achieves total capacity times the largest nonnegative gain. LR attains the same support at x=0,y=1,i=1 and that single shared stage. Equality of support functions for all signed clock normals proves equality of the compact convex time hulls. QED.

This is a continuous real-parameter proof, with the equality boundary included. The Fraction computations below independently check two rational special cases only.

## Exact rational witnesses

Fix r=(1/10,1/5,3/10,2/5), p=(1/3,1/2,3/5,4/5), q=(2/3,1/4,3/7,5/8). There are six distinct FULL upstream vertices times 4^4 continuation configurations, hence 1,536 FULL deterministic observations. LR has four upstream corners times four shared stages, hence 16 deterministic observations.

**A: alpha common, nu distinct.** Set v=(1/5,2/5,3/5,4/5). Then alpha=(1/2,1/2,1/2,1/2), nu=(17/64,19/68,7/24,23/76). Normal n=(0,0,-2/7,1) gives h_FULL=10041/4480, h_LR=1003/448, gap=11/4480. FULL witness W=(799/960,12025/86016,437/120,6301/1920) uses x=0,y=1,i=1 and source stages (1,1,3,3). The L-infinity distance from this W to the LR four-hull is at least 11/5760.

**B: nu common, alpha distinct.** Set v=(21/50,27/50,33/50,39/50). Then nu=(3/10,3/10,3/10,3/10), alpha=(21/20,27/40,11/20,39/80). Normal n=(0,0,3/5,-1) gives h_FULL=-199/200, h_LR=-639/640, gap=11/3200. FULL witness W=(2147/2880,43019/258048,59/15,671/200) uses x=0,y=1,i=1 and stages (2,2,3,3). Its L-infinity distance from the LR four-hull is at least 11/5120.

For A and B the one-norms of normals are 9/7 and 8/5. The distance bounds follow by Holder duality from the support gap. The source VERIFY.py uses only Python standard-library Fraction and enumerates actual FULL and LR four-vectors; EXACT_OUTPUT.txt is its literal output.

## Scope, consequence, next question

Previous K3 research has established on its declared scopes: unequal mu with min mu<3/8 forces four-observer separation by mask/fiber analysis; common mu with heterogeneous r forces signed time separation. With this new supercritical result, those predecessor claims together imply the necessary condition that **any K3 four-hull equality must have source-uniform r and v**. This synthesis depends on the cited earlier author-side proofs. The present note newly proves and tests the supercritical component, without independently re-auditing the entire predecessor chain.

The remaining branch is the uniform-clock four-observer error-fiber question for arbitrary p_s,q_s, including the previously unclassified high ratio v/r>1. Exact full-hull primal/Farkas certificates and real-image membership tests belong after the next source-specific derivation. No change to P000, ACTIVE worldview, frozen pins, task ownership, or mathematical admission follows from this proof.

## Publication / authority

The connected GitHub account is authorized to preserve this material on the existing R5 research PR. The Enterprise Math Site reported read-only static identity and rejected an own session registration with STATIC_READONLY_SCOPE_DENIED; task-owner inventory returned CONTROL_QUOTA. The current report asserts no native RA, CLAIM, Result, Driver review or admission. Only author-side research/source evidence is being published.
