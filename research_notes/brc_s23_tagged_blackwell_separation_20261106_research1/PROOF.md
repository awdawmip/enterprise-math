# S23: equal total variation but strictly different Bayes risks for a tagged observer

Date: 2026-11-06. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34, research_notes/brc_n4_s23_asymmetric_hull_gap_sqrt43_20261101_research1/PROOF.md.
Direct predecessor: awdawmip/enterprise-math@5a3b827cda4135517688f9a195da399f70b59982, PR #1773. No frozen input was rebased.

## Exact hypotheses and experiments

The frozen rational box is Q=[1/2,7/8] × [1/8,1/2] × [1/2,7/8] with theta=(a,b,c). Keep all six source labels AU0, AU1, AV, BU0, BU1, BV and their shared A/B second-stage control b. Their four-stop distributions are:

- AU0=AU1=(a,(1-a)b,(1-a)(1-b)/2,(1-a)(1-b)/2)
- AV=(a,0,(1-a)c,(1-a)(1-c))
- BU0=BU1=(1/4,3b/4,3(1-b)/8,3(1-b)/8)
- BV=(1/4,1/4,1/4,1/4).

For legal hypotheses theta_-=(1/2,1/8,1/2) and theta_+=(1/2,1/8,7/8), only AV differs. The full four-stop AV experiment has conditional distributions

A_-=(1/2,0,1/4,1/4),  A_+=(1/2,0,7/16,1/16).

The deterministic source-tagged event W=1_{AV:stop3} induces Bernoulli distributions (yes,no):

B_-=(1/4,3/4),  B_+=(7/16,9/16).

This defines two precisely scoped binary-hypothesis experiments, not an assertion about an unrestricted ten-decoder implementation.

## Theorem A — equal TV and equal-prior decision risk

Under TV(U,V)=sum_i |U_i-V_i|/2,

TV(A_-,A_+)=TV(B_-,B_+)=3/16.

Indeed AV stops 3 and 4 change by +3/16 and -3/16, while stop1 is fixed; grouping the complement of stop3 preserves their total variation for this pair. Consequently, the minimum 0-1 error under equal priors is (1-TV)/2=13/32 for both experiments.

## Theorem B — exact Bayes-risk loss for every prior

Let t=Pr(H_+) range over all real numbers in [0,1]. For conditional laws U_-,U_+, minimum 0-1 Bayes risk is R_U(t)=sum_j min((1-t)U_{-,j},t U_{+,j}). Subtracting the full AV risk from the Bernoulli risk, their stop3 terms cancel, leaving

L(t)=R_B(t)-R_A(t)
    =min(3(1-t)/4,9t/16)
     -min((1-t)/2,t/2)
     -min((1-t)/4,t/16).

The three residual minima switch affine branches at exactly t=4/7, 1/2, 4/5 respectively. Thus for EVERY REAL t in [0,1]:

    L(t)=0                  for 0<=t<=1/2;
        =t-1/2              for 1/2<=t<=4/7;
        =(4-5t)/16          for 4/7<=t<=4/5;
        =0                  for 4/5<=t<=1.

The formulas agree at their shared endpoints. Hence L(t)>0 exactly when 1/2<t<4/5. Its unique maximum equals 1/14 at t=4/7, where R_B=3/7 and R_A=5/14. At t=1/2, both risks equal 13/32. Equal total variation is therefore not a certificate of decision fidelity across all priors, even for the same fixed lawful hypothesis pair.

## Theorem C — no hypothesis-independent reverse stochastic kernel

The forward kernel from AV to W is deterministic (yes iff stop3). Suppose a reverse row-stochastic K from {yes,no} to the four stops satisfied B_- K=A_- AND B_+ K=A_+. Write u=K(yes,stop3) and v=K(no,stop3). Because the stop3 probability in each target equals its input yes probability b_- or b_+, where b_-=1/4 != 7/16=b_+, the two equations

    b_- u+(1-b_-)v=b_-;   b_+ u+(1-b_+)v=b_+

force u-v=1, hence v=0 and u=1.

The stop1 target probability is exactly 1/2 in BOTH hypotheses. Since the yes probabilities differ, the same two linear equations for stop1 instead force K(yes,stop1)=K(no,stop1)=1/2. The yes row then assigns at least 1+1/2>1 total mass to stops 3 and 1, contradicting stochasticity. No such reverse K exists. Therefore full AV strictly Blackwell-dominates the one-bit observer W for the disclosed binary experiment. The explicit 1/14 prior-Bayes-risk gap witnesses strictness without invoking any unproved general theorem.

## BRC / legal transfer boundary and verification

This analysis retains the positive BRC carrier, original four-stop ordering, source labels and common b. It proves a source-tagged information-loss witness for a specific allowed pair and a specified observer operation. An exact lawful implementation of AV:stop3 in the original ten-label encoder/decoder is a separate access/composition problem; the earlier recorded full mother bound 1/2<=R_beh(k,10)<=2/3 (k=4,6) is not tightened by this theorem.

VERIFY.py (actual Python standard-library Fraction execution) reconstructs all six rows, computes both TV values, checks endpoint and midpoint rational certificates for the affine risk branches and the exact kernel contradiction. RUN_EVIDENCE.txt records its stdout. The all-real proof rests on the displayed affine-minima identities, not finite sampling. Independent mathematical review and official task admission remain outstanding.
