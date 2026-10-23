# Exact complete parameter interval for the length-six two-episode BRC word

**New author-side algebraic theorem; UNREVIEWED, NOT ADMITTED, NOT NATIVE X6.** This strengthens the rational point z=3/4 in MINIMAL_LENGTH6_AUTHOR_PROOF.en.md. Keep the original four hidden labels, the original good **exact** occupied pairs {0,1},{1,2},{1,3},{2,3}, original laws q_0=(0,1+z,1-z,1)/3 and q_2=(1,1,0,1)/3, and residual R_t=sum_{j=2}^t [delta_j-delta_{j-1}]_+ - max_{s<=t}delta_s. Add just one action N with q_N=(0,1/4,0,3/4). Fix public word p=0N20NN.

## Theorem (iff parameter classification)

Let alpha=(sqrt(109)-3)/10, which lies strictly between 11/15 and 3/4. For z in [0,1], the strict residual-growth times of this fixed word contain two separated episodes **if and only if**

**alpha < z <= 5/6.**

Throughout that interval, G(p,z)={4,6}. This is a continuum of counterexamples to enlarging the {0,2}-specific theorem to the extra action N.

## Exact proof

For any time-varying action distributions, the exact occupancy probability of a given pair {i,j} equals

P(D_t={i,j}) = product_{s<=t}(q_i^(s)+q_j^(s)) - product_{s<=t}q_i^(s) - product_{s<=t}q_j^(s).

Sum this identity over the four disjoint good pairs and expand for successive prefixes of 0N20NN. The exact rational *polynomials*, with no approximation, are:

delta_1 = 0

delta_2 = (8-z)/12

delta_3 = (4z+17)/36

delta_4 = (10z^2+18z+41)/108

delta_5 = (40z^2+90z+149)/432

delta_6 = (154z^2+402z+569)/1728.

In particular,

Delta_3 = 7(z-1)/36 <= 0,

Delta_4 = (5z^2+3z-5)/54,

Delta_5 = (6z-5)/144,

Delta_6 = (-2z^2+14z-9)/576.

The polynomial 5z^2+3z-5 is strictly increasing on [0,1] and has unique positive root alpha. Thus Delta_4>0 iff z>alpha. Also Delta_5<=0 iff z<=5/6.

For all z in [0,5/6], the exact differences from delta_2 are

delta_2-delta_3 = 7(1-z)/36,

delta_2-delta_4 = (31-27z-10z^2)/108,

delta_2-delta_5 = (139-126z-40z^2)/432,

delta_2-delta_6 = (583-546z-154z^2)/1728.

Each is decreasing on [0,5/6]. At z=5/6 they are respectively 7/216, 7/486, 7/486 and 379/31104, all **strictly positive**. Hence the historical maximum is frozen at delta_2 for t=2,...,6 throughout that interval.

Moreover alpha>11/15, because (5z^2+3z-5)|_{z=11/15}=-1/9<0. The polynomial -2z^2+14z-9 is strictly increasing throughout [0,1] and equals 43/225>0 at 11/15. Hence Delta_6>0 whenever z>alpha. For alpha<z<=5/6, Delta_4>0, Delta_5<=0, Delta_6>0, while the running max remains delta_2: residual strict gains therefore occur **exactly** at rounds 4 and 6.

To prove the **only-if** direction: delta_0=delta_1=0 forces R_2=R_3=0 identically. In a six-round word two separated positive-growth episodes must start at rounds 4 and 6, with round 5 non-growing. If z<=alpha then Delta_4<=0 so no residual gain at round 4. If z>5/6 then Delta_5>0. The general identity

R_t-R_{t-1} = min( [Delta_t]_+, M_{t-1}-delta_{t-1} )

implies that a zero residual gain during a **strictly positive** Delta_5 can only occur if the historical headroom M_4-delta_4 was already zero. Then a following positive Delta_6 cannot restart gain. On the other hand, if round 5 has positive residual growth, rounds 4 and 6 cannot be separated. Thus outside (alpha,5/6] two separated episodes are impossible. QED.

## Checks and boundary

Exact symbolic polynomial expansion, subtraction, endpoint rationals and radical interval were checked by the accompanying local SymPy script (not a formal theorem prover); the independent standard-library Fraction/mask checker for rational witness points is saved separately in the same folder. The proof above uses only explicit polynomial identities and rational monotonic inequalities, not a floating-point scan or finite-word extrapolation.

This is strictly an auxiliary four-label positive-rational BRC theorem under the **expanded action alphabet**. The original theorem limited to {0,2} is not contradicted. Native P000 X6 Cell/slice/readout/future-operation preservation, current owner, formal Research Driver review and canonical admission remain open. Original source pins: GLOBAL_KNOWLEDGE_V1 main@674c44f8c3c194a82c63f0bba6da995d1d307ad3 and Enterprise Math read main@4fe67f915d52a563825757c8d6e9e199f2eb4b64.
