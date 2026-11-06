# S23 conditional AV: exact two-trial reconstruction deficiency

Date: 2026-11-06. Status: author analytic proof + executed exact rational verification; independent mathematical review pending. Scientific input frozen at enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Continues the near-exact certificate at 25ca1b5352880bafeef819f25b0db52205ee8c00 in Draft PR #1777.

## Theorem

For every real a,c in [1/2,7/8], set z=(1-a)c and u=(1-a)(1-c). The full AV stop observation is A=(a,z,u) on {1,3,4}; the binary third-stop indicator observation is B=(z,1-z) on {Y,N}. The two trials are conditionally independent given ONE shared unknown (a,c). The underlying separate parameter b in [1/8,1/2] does not affect this conditional AV observer.

For one single parameter-independent row-stochastic kernel L from {Y,N}^2 to {1,3,4}^2, let

    δ₂ = inf_L sup_{a,c∈[1/2,7/8]} TV(A_{a,c}^{⊗2}, B_{a,c}^{⊗2} L),

where TV(P,Q)=sum_x |P_x-Q_x|/2. Then **δ₂=9/49 exactly**. The infimum is attained by the following explicit rational 4×9 stochastic kernel.

## Constructive upper bound: an exact common kernel

Group the nine ordered full-output pairs into six exchange orbits:

    11 | {13,31} | {14,41} | 33 | {34,43} | 44.

For full observations the six orbit masses are T=(a²,2az,2au,z²,2zu,u²). Let K have three rows indexed YY, MIXED, NN (both ordered YN and NY use the same MIXED row), and six columns indexed by those output orbits:

    K = [0,       0,      0,      1,  0,    0]
        [0,      11/21,   1/4,    0,  5/28, 1/21]
        [340/441, 2/21,  59/441, 0,  0,    0].

All rows are nonnegative and sum to one. Turn this into the actual 4×9 kernel L by splitting the mass of each two-element output orbit equally among its two ordered pairs; preserve each singleton mass. Both input sequences YN and NY use the MIXED orbit row, so L is a legal parameter-independent kernel.

The reconstructed orbit law is Q=(z²,2z(1-z),(1-z)²)K. Target and reconstruction are exchange-symmetric, so full ordered-pair TV equals the six-orbit TV: TV(T,Q)=sum_{j=1}^6 |E_j|/2 for E=T-Q.

Split the entire real parameter box into only TWO closed rectangles:

    R1=[1/2,5/7]×[1/2,7/8],  R2=[5/7,7/8]×[1/2,7/8].

On either R, normalize a=a0+(a1-a0)s and c=c0+(c1-c0)t with s,t in [0,1]. Each E_j is separately quadratic in s and t: both A and B are separately affine in a,c, and taking two IID products squares those degrees. Consequently E has the exact tensor-product degree-(2,2) Bernstein representation

    E(s,t) = Σ_{i,j=0}² β_i(s) β_j(t) C_ij,
    (β0(x),β1(x),β2(x))=((1-x)²,2x(1-x),x²).

Write V_pq=E at the grid nodes (s,t)=(p/2,q/2), p,q=0,1,2. The exact six-coordinate Bernstein coefficient vectors are

    C_ij = Σ_{p,q=0}² M_ip V_pq M_jq,
    M = [[1,0,0],[-1/2,2,-1/2],[0,0,1]].

Every C_ij has coordinate sum zero. Its total-variation seminorm h(C)=sum max(0,C_j)=max_{S⊆{1,...,6}} sum_{j∈S} C_j is therefore exactly half of its L1 norm. The following two 3×3 tables give ALL EIGHTEEN coefficient seminorms h(C_ij), calculated in exact rationals (rows i=0,1,2; columns j=0,1,2):

    R1:
      9/49       89/896       61/392
      95/686     15/196       9/49
      142/2401   45/686       9/49

    R2:
      142/2401   45/686       9/49
      65/3136    1005/10976   9/49
      69/784     1529/12544  1053/6272

Every exact entry is at most 9/49. All Bernstein weights are nonnegative and sum to one. Convexity of TV gives, on each rectangle and hence on the entire continuous box,

    TV(T,Q) = h(E(s,t))
            ≤ Σ_{i,j} β_i(s)β_j(t)h(C_ij) ≤ 9/49.

Direct substitution at (a,c)=(1/2,1/2) gives equality, so this very kernel has worst-case error exactly 9/49. The coefficient tables, their rational interpolation formula and positivity of Bernstein weights form a closed global certificate, not a grid extrapolation.

## Matching universal lower bound

The legal parameter points θ0=(a,c)=(1/2,1/2) and θ1=(5/7,7/8) have the identical binary parameter z=1/4, hence identical two-trial compressed observations B^⊗2. Their six full-output orbit laws are

    T0=(1/4,1/4,1/4,1/16,1/8,1/16),
    T1=(25/49,5/14,5/98,1/16,1/56,1/784).

Exact subtraction yields TV(T0,T1)=18/49. Every admissible parameter-independent L produces the same Q at θ0 and θ1. Thus by the TV triangle inequality

    max{TV(T0,Q), TV(T1,Q)} ≥ TV(T0,T1)/2 = 9/49.

This proves δ₂≥9/49; the constructive Bernstein certificate proves δ₂≤9/49. Therefore **δ₂=9/49**.

## Verification and research scope

The companion VERIFY.py implements Fraction-only exact rational interpolation, checks the two 3×3 control tables, independently tests all 64 signed-event sums at each control point, kernel normalization, the fiber witness, and 289 supplementary rational grid inputs. RUN_EVIDENCE.txt is the stdout from an actual execution of the equivalent source-checked local verifier (the remote verifier has the same polynomial, kernel and exact-check semantics). Finite grid tests supplement but are not the universal proof; the 18 Bernstein control values are the universal certificate.

This theorem solves the exact two-conditional-trial *auxiliary statistical observer* reverse deficiency. Its BRC reuse is a typed positive-measure fiber/observer-compression calculation. The original ten-label S23 encoder/decoder mother minimax R_beh(k,10), k=4,6, still requires an independently verified admissible mapping and quantifier bridge. The result does not amend P000 or the ACTIVE six-dimensional ontology. Author evidence is not an independent review or project admission.

Next: test the original frozen ten-label source choice/encoder/decoder legality bridge, or pursue a genuinely new n≥3 shared-parameter reverse-deficiency question. The δ₂ bound-optimization subproblem is now closed at its exact value.
