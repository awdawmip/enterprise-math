# BRC N=4 / S23: exact local total-variation geometry of policy boxes

2026-11-01. **Author-side analytical proof and executed exact-rational validation; UNREVIEWED / NOT_ADMITTED.** A finite six-source S23 statistical experiment, not a statement about P000 native X6 spatial/time dynamics. This note extends the sharp global anisotropic modulus at Enterprise Math PR #1765, commit `4d85c43512f544689cab044be7951c4c26fc0faf`.

## Frozen model and BRC typing

The eleven legal controls in `[0,1]^11` are
`(a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)`. Six distinct statistical sources have maps
`A=(0,0,0,1,1,1)`,
`B=(2,2,3,2,2,4)`,
`C=(5,6,7,8,9,10)`.
The common `b_U` is one shared control. For each source x, the four-stop law is
`F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c))`.
Prepared input i has
`p_i(theta)=sum_{x=0}^5 M_ix F(theta[A_x],theta[B_x],theta[C_x])`,
where `M=M20/20` and
`M20=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))`.

BRC interface: positive weighted provenance-retaining source mixture, exact rational row-stochastic observer. Reuse status **REUSE_APPLIED** (same typed law and predecessor as PR #1765). The population remains six labelled statistical sources. The prepared-law distance is an observer-specific quotient, not a license to delete source identities or to identify these with P000 native spatial axes. All policy controls, including the shared U information set, remain as defined.

## Theorem 1. Exact box diameter from seven probability cuts

Let `Q=prod_{j=0}^{10}[l_j,u_j]` be a closed policy box, including degenerate coordinates, and `V(Q)` its set of distinct corners. For each prepared row i and nontrivial subset S of {1,2,3,4}, set
`f_{i,S}(theta)=sum_{t in S} p_i(theta)_t`.
Choose just seven complementary-pair representatives: the bit masks
`C={1,3,5,7,9,11,13}`, where bit 0 represents stop 1. Define
`L_{i,S}=min_{v in V(Q)} f_{i,S}(v)`,
`U_{i,S}=max_{v in V(Q)} f_{i,S}(v)`.
Then **for every real policy box**,
```
Delta_i(Q) := max_{theta,phi in Q} TV(p_i(theta),p_i(phi))
            = max_{S in C} (U_{i,S}-L_{i,S}),
Delta(Q)   := max_{theta,phi in Q} max_i TV(p_i(theta),p_i(phi))
            = max_i Delta_i(Q).
```
All displayed extrema are attained at pairs of vertices. For d genuinely varying controls, an exact computation needs 2^d evaluations of six prepared 4-stop distributions and 6*7 cut ranges, rather than enumerating all pairs of vertices. This is an exact finite *symbolic reduction* for arbitrary real box endpoints; actual exact rational evaluation applies when endpoints are rational. Complexity is exponential in d.

**Proof.** Each single latent-source stopping probability is multi-affine in its three distinct control coordinates A_x,B_x,C_x. Source summation preserves multi-affinity even though a control such as b_U is shared **across different source summands**. Thus each scalar cut mass f_{i,S} is multi-affine in all eleven coordinates. A scalar multi-affine function on a box attains its maximum and minimum at vertices: iteratively replace one coordinate with the better of its two endpoints, since the function is affine in that coordinate with all others held fixed. For finite probability measures `TV(p,q)=max_{S subseteq {1,2,3,4}} |p(S)-q(S)|`. The empty/full cuts give zero, and complementary cuts have identical absolute differences; the seven masks above represent the remaining equivalence classes. Interchanging two finite maxima over independent policies theta,phi yields the range U-L for each cut. Then maximize over i. Compactness gives attainment. QED.

## Theorem 2. Exact anchor radius and continuum risk certificate

For any fixed anchor z in Q, define `rho_Q(z)=max_{theta in Q} max_i TV(p_i(theta),p_i(z))`. Then
```
rho_Q(z)=max_{i,S in C} max(
       U_{i,S}-f_{i,S}(z), f_{i,S}(z)-L_{i,S}).
```
Let an arbitrary **fixed**, policy-independent encoder and any finite nonempty bank of fixed policy-visible decoder kernels induce row laws q_{li}, label losses
`L_l(theta)=max_i TV(p_i(theta),q_{li})`,
and bank risk `G(theta)=min_l L_l(theta)`.
The following **exactly certified upper bounds** apply:
```
G(z) <= sup_{theta in Q} G(theta) <= G(z)+rho_Q(z),
osc_Q(G) <= Delta(Q).
```
One may combine this bound with the existing fixed-label vertex bound
`sup_Q G <= min_l max_{v in V(Q)} L_l(v)`
and retain the smaller upper bound. The new geometric radius depends only on the prepared policy laws and can be reused across arbitrary candidate banks.

**Proof.** The same probability-cut identity as in Theorem 1, with the second policy fixed to z, gives the exact radius formula by multi-affine extrema. The TV reverse triangle inequality bounds
`|TV(p_i(theta),q_{li})-TV(p_i(z),q_{li})| <= TV(p_i(theta),p_i(z))`.
Taking the maximum over i and minimum over l preserves any common additive Lipschitz bound. This proves the anchor certificate and the oscillation certificate via Delta(Q). The lower anchor inequality follows from z belonging to Q. For a fixed label l, `L_l(theta)` is a maximum of absolute affine cut differences of multi-affine functions; each such cut difference is bounded over Q by the extrema of its endpoints, so `max_Q L_l=max_{v in V(Q)}L_l(v)`. Taking one fixed label throughout the box proves the final fixed-label upper bound. QED.

## Theorem 3. Closed form on a six-third-stage-control face

Fix the first five controls `a_A,a_B,b_U,b_AV,b_BV`, and vary the six distinct third-stage controls `c_x in [c_x^-,c_x^+]` independently. Write the stage-survival weight
`s_x=(1-a_{A_x})(1-b_{B_x})>=0` and width `h_x=c_x^+-c_x^- >=0`. Then simultaneously for all six prepared rows,
```
Delta_i(Q_C)=sum_x M_ix s_x h_x.
Delta(Q_C)=max_i sum_x M_ix s_x h_x.
rho_{Q_C}(midpoint)=Delta(Q_C)/2.
```
**Proof.** With early stages fixed, changing c_x only transfers mass s_x dc_x between stop times 3 and 4; prepared changes have form `(0,0,v_i,-v_i)` where `v_i=sum_x M_ix s_x (c_x-c'_x)`. Since each coefficient M_ix s_x is nonnegative, the largest |v_i| over independent c_x,c'_x equals the sum of the coefficient-weighted widths; both opposite corners achieve equality. At the midpoint the largest difference is one half of this sum, simultaneously for all prepared rows. QED.

## Two exact adversarial examples

**Mixed-corner obstruction.** Set all controls to zero except `a_A in [0,1/4]` and shared `b_U in [1/4,1]`. On row AU, parameters `(a_A,b_U)=(0,1)` give distribution `e2`, while `(1/4,1/4)` give `(1/4,3/16,0,9/16)`. TV is `13/16`; the complete seven-cut calculation across all six rows proves `Delta(Q)=13/16`. The single all-low versus all-high corner pair has only `3/4`: **mixed corners are indispensable** even on a two-control face.

**Survival-weight obstruction to global-radius efficiency.** Fix `a_A=9/10`, `b_U=0`, all other controls zero, and vary only `c_AU0 in [0,1]`. Theorem 3 gives `Delta=1/20` and the exact midpoint radius `1/40`. The previous bank-independent global anisotropic bound would give diameter `1/2`, half-width radius `1/4`. At `a_A=1`, the declared prepared law is entirely insensitive to c_AU0 and its exact box diameter is zero; this does not delete the latent source's identity.

For a rational six-C face with early controls `(9/10,2/5,3/7,1/3,5/8)` and low/high third controls `(0,1/7,1/3,1/5,0,1/8)` / `(1,6/7,3/4,4/5,1/2,1)`, the six exact row diameters are `(12/245,59/1225,1/36,33/175,153/875,63/320)`, so the overall diameter equals `63/320`.

## Executed evidence, exact scope and continuation

`VERIFY.py` runs Python stdlib `fractions.Fraction`: 2048 exact full-box corner evaluations with the seven cuts; a 64-corner six-C face; explicit rational mixed-corner and survival examples; 32 seeded rational 3-control boxes checked against every explicit vertex pair and exact anchor radius, plus 192 rational interior strategy pairs. Actual stdout in `RUN_EVIDENCE.txt` ends `PASS_BRC_N4_S23_LOCAL_BOX_EXACT_TV_GEOMETRY_20261101`. The **universal real-box statements are analytical**, not extrapolations from tests.

This result is exact geometry for a frozen finite S23 prepared-law model. It does not independently prove the original full ten-label minimax interval is sharp, lower the existing `[1/2,2/3]` bracket for `k=4,6`, or transfer S2 causal information sets or finite sources to P000 six-dimensional native Cells/time. Formal Result, independent review and admission require separate authorization and evaluation. Next use the exact local radius as a bank-independent branch-and-bound ingredient, combined with the fixed-label upper envelope, while jointly redesigning at least one of the first nine decoder kernels and the tenth.
