# R5 — A single K2-success answer coin has an exact all-real signed support gap

Date: 2026-11-03 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / SYMBOLIC_CROSSCHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Frozen input, precursor and target

The preceding verified research is enterprise-math@b25947a3c94313c3ccf993e70de1f87af8a833f0:research_notes/brc_r5_serial_two_law_collision_embedding_20261102_t2342/RESEARCH.md and its VERIFY.py and NEXT_TASK.md. It constructs a genuine finite two-law stopped path model with serial seedless LR collisions and four independent physical observations. The mother target remains: equal convex hulls of FULL/LR four-observer sets but unequal *actual* real behavioral images.

Frozen scientific pins remain global a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current normative main reads: global 59e89513aa300fe9fc5173d484c6095dfb3afb5d; Enterprise Math 2c3dff5dfd6389d9999118b8bef8703ebae7e409. P000 and ACTIVE worldview were read and left unchanged. This is a classical auxiliary finite two-measure stopped-tree theorem, not a native X6 transfer.

**Theorem.** Keep that tree's transition probabilities and decisions unchanged. Introduce one terminal nature coin after K2 success for source BJ, producing Q label with P-law probability eta/8 and Q-law probability eta, where **every real 0<eta<1** is allowed. Then FULL and seedless LR obey, for the physical four-observer O=(eP,eQ,TP,TQ),

    n_eta=(134/9,85/9,-2-eta/2,8+eta)
    h_FULL(n_eta)-h_LR(n_eta)=eta/96>0.

The restricted LR image retains full four-dimensional local rank for every such eta, and a FULL witness has distance at least eta/[16(206+9 eta)] from conv O(LR). This classifies the specified continuous *one-coin family* as hull-separated.

## Probability tree, strict positivity and collisions

Nature selects C,I,BJ,IJ,D under both P/Q with probabilities 1/4,1/4,1/8,1/8,1/4 after the upstream flag X (probability x). Group D stops at time 3 with P/Q Bernoulli Q-label probabilities (1/2,1/2). For flag 1, groups I and IJ exit at time 3 with P/Q Q-label probabilities (1/2,1/4). At time 2, BJ and eligible IJ have a J stop decision; J stop Q-label probabilities are under P beta_s/4 and under Q beta_s/2, beta_B=1/2 and beta_I=3/4. Every other path reaches K1 at time 3, padding shorter routes without changing terminal times.

At K1, behavioral continue is followed by a natural P-success probability alpha_s, with alpha=(1/2,2/3,1/2,3/4) for C,I,BJ,IJ, and Q-success probability alpha_s/2. Success advances to K2 at time 4; failure or stop terminates at time 3 with label P. At K2, behavioral continue is followed by a natural P-success probability c=2/3 and Q-success c/2=1/3 for every group. Success terminates at time 5, stop/failure at time 4. All original K terminal labels are P.

**Only change:** K2-success in BJ now uses a terminal Q-label nature coin with probabilities (eta/8,eta) under P and Q. For all 0<eta<1 every nontrivial nature Bernoulli probability, including the newly inserted coin and its complement, is strictly between 0 and 1. The added coin is sampled *after* the final behavioral decision; J, K1, K2 retain time and prior P/Q likelihood-ratio keys (2,1), (3,1), (4,2), respectively. FULL may observe source and flag; seedless LR must use a common J continuation y, common K1 continuation z and common K2 continuation t. Both laws share each policy's behavioral probabilities.

## Lemma — exact real path-flow formula

Let b in [0,1] and i in [0,1-x] be eight times the BJ and IJ mass reaching K1; full-history root-flag-dependent controls are aggregated by their actual mass. Define

    w=(1/4,(1-x)/4,b/8,i/8);
    d=(beta_B*b+beta_I*i)/8 = b/16+3*i/32;
    H(x)=1/8+(1-x)/6;
    r1=sum_j w_j alpha_j z_j;
    r2=c sum_j w_j alpha_j z_j t_j;
    s=c w_BJ beta_B z_BJ t_BJ.

Here z_j, t_j are effective source-specific conditional controls in [0,1] arising from precise P-law path flow, including adaptive FULL histories; zero-mass sources are harmless. Q advance flows are exactly r1/2 and r2/4 because K1 and K2 natural success likelihood ratios are each 2. The BJ-specific P K2-success flow is s; under Q it is s/4.

Direct summation of all terminal paths under both laws gives, for **every real adaptive FULL policy**,

    eP=107/128 - 21*x/128 + d/4 - eta*s/8;
    eQ=13/64 + 3*x/64 - d/2 + eta*s/4;
    TP=3+r1+r2;
    TQ=3+r1/2+r2/4.

Apply the inverse of the original physical affine observer map:

    vp=eP-107/128, vq=eQ-13/64;
    x'=(-vp/2-vq/4)/(9/128);
    d'=(-3*vp/64-21*vq/128)/(9/128);
    r1'=4*(TQ-3)-(TP-3);
    r2'=2*(TP-3)-4*(TQ-3).

Substitution gives exactly **(x',d',r1',r2')=(x,d-(eta/2)*s,r1,r2)**. This is an observer-coordinate transformation, not a claim that the hidden source state is fully represented by four coordinates.

## Proof of the all-real signed support theorem

Define Phi=-2*x'-d'+2*r1'-(eta/4)*r2'. Up to an additive constant common to FULL and LR, Phi equals n_eta dot O, with n_eta stated above. By the path-flow lemma,

    Phi=-2*x-d+2*r1-(eta/4)*r2+(eta/2)*s.

For FULL, the coefficient of each K1 continuation z_j is strictly positive; the coefficient of t_j is strictly negative for sources other than BJ, and strictly positive for BJ. This remains true for all real eta in (0,1). Hence for fixed x,b,i the optimum chooses all z_j=1, BJ t_BJ=1, and other t_j=0. Exact substitution gives

    max_FULL Phi(x,b,i)=-2*x+2*H(x)+d+eta*b/96.

Using 0<=x,b<=1 and 0<=i<=1-x, this is maximized at x=0,b=1,i=1 (positive coefficients of b,i, negative coefficient of x), so

    max_FULL Phi=71/96+eta/96.

For LR, b=y, i=(1-x)y and A=H(x)+d, so r1=z*A, r2=c*z*t*A and s=c*beta_B*y*z*t/8. The z*t coefficient in Phi is exactly

    (eta*c/4)*(2*beta_B*y/8-H(x)-d).

It is strictly negative: H(x)>=1/8, 2*beta_B*y/8=y/8<=1/8, d>=0, and the would-be equality of the first two bounds forces y=1 while d>0. Thus optimal LR chooses t=0,z=1 and then maximizes -2*x+2*H(x)+d at x=0,y=1. Consequently

    max_LR Phi=71/96,
    h_FULL(n_eta)-h_LR(n_eta)=eta/96.

This establishes the support functions over **all real behavioral policies**; finite vertex enumeration is an independent exact check, not the source of the universal quantifier.

A maximizing FULL strategy has x=0; both J sources continue; all K1 sources continue; at K2 only BJ continues. Its physical observation is

    W_eta=(7/8-eta/192, 1/8+eta/96, 335/96, 207/64).

The maximizing LR policy is x=0,y=1,z=1,t=0. The normal's L1 norm equals (206+9 eta)/6, so dual norm separation yields

    dist_infinity(W_eta,conv O(LR))>=eta/[16*(206+9 eta)].

At eta=1/2, the strictly positive example is W=(335/384,25/192,335/96,207/64), signed gap=1/192, L-infinity distance lower bound=1/6736.

## Independent four-dimensional rank

For LR controls x,y,z,t let A=H(x)+(5-3x)*y/32. Its inverse-observer coordinates are

    (x',d',r1',r2')=(x,(5-3x)*y/32-eta*y*z*t/48,z*A,(2/3)*z*t*A).

At x=y=z=t=1/2, the auxiliary Jacobian determinant is

    71407/28311552 - (505*eta)/5308416 > 0

for every eta in (0,1). The physical affine map has determinant -9/512, giving a nonzero physical LR Jacobian. An independent SymPy differentiation produced the equivalent exact expression -101*(80*eta-2121)/84934656.

## Executed evidence and precise boundary

The accompanying **actual executed** Python standard-library fractions.Fraction checker returned PASS_EXACT_R5_K2_SUCCESS_SINGLE_SOURCE_ANSWER_FIBER and 31,784 exact assertions. Five rational eta points check all 2,048 reduced FULL deterministic vertices and 16 seedless LR deterministic vertices; reduced FULL covers all deterministic observer points because deterministic root flags make all unreachable flag-conditioned J/K policies irrelevant, and the finite-tree observer is multi-affine in each local decision probability. It also checks the exact support gap, witness, distance, probability bounds and three exact LR Jacobians. Independently, 150 nonbinary root-flag-adaptive FULL policies are computed by summing *all terminal paths* under both laws and comparing with the algebraic flow formulas. The continuous eta theorem rests on the proof above.

BRC interface: source-labeled positive rational probability weights, preserved provenance and exact observer-fiber projection; no signed/phase cancellation and no native X6 transfer. The known mother target remains open. GitHub identity awdawmip has repo push/admin rights. Native Owner listing returned CONTROL_QUOTA and a new service session attempt returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false), so no formal CLAIM, native Result or independent Driver acceptance is asserted.

## Next concrete unit

Permit independent K2-success terminal-answer kernels for *two or more* hidden sources, derive the exposed-face source coefficient conditions needed to cancel this specific gap, and test a rational compensated candidate using all-signed convex-hull certificates. A truly hull-equal candidate then needs an exact semialgebraic real-image nonmembership witness. See NEXT_TASK.md.
