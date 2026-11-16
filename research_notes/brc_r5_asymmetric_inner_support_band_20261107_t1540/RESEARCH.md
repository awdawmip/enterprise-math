# R5 — Exact asymmetric-time inner signed-support band (all real parameters)

Date: 2026-11-07 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Scientific source, parent and representation scope

R5 original immutable inputs retained: Global `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Direct mathematical predecessor: `8902141f486f496958f6e4e8f084472ef33f08af`, `research_notes/brc_r5_signed_lambda_exact_switch_20261107_t1442/RESEARCH.md`. The four-observer mother question remains whether FULL_HIST and seedless LR have identical images for W=(eP,eQ,TP,TQ). This exact unit extends the predecessor's symmetric TP=TQ=31/10 support theorem to an asymmetric two-dimensional parameter strip. It is a frozen four-stage P/Q-BRC LR observer, not a full native-X6 world dynamics statement. Preserve seven LR node masses and the central-history mixture until the final observation map.

Let (g,a,b,u,v,w,z) be real flows with 0<=a,b<=g<=1, C0=13a/40+b/80, C1=a/10+9b/40, C2=3a/40+21b/80, and 0<=u<=C0, 0<=v<=C1, 0<=w<=C2, 0<=z<=a/10, 0<=v-z<=9b/40. The times and the seven increasing stopped Q-masses at r=(1/10,1/2,3/4,1,5/4,3/2,19/10) are exactly those given in the predecessor, reproduced in VERIFY.py. Every terminal random declaration obeys 0<=Ej<=Mj and gives eQ=sum Ej, 1-eP=sum rj*Ej. Seedless LR requires 9*b*z=4*a*(v-z).

## Theorem (asymmetric common support band)

Define
```
lambda_minus = -351/17291,  lambda_plus = 351/16589
epsilon in [-1/56, 9/344]
lambda in [lambda_minus, lambda_plus]
TP = 31/10 + epsilon, TQ = 31/10 - epsilon
U_lambda = eQ - (1+lambda)*(1-eP)
F(epsilon) = 13269/53000 + (27/6625)*epsilon
```
For **every** real pair (epsilon,lambda) in this entire rectangle, with all admissible real flow and randomized declarations,
```
max_FULL_HIST U_lambda = max_seedless_LR U_lambda =
   F(epsilon) - (45413/159000 + 112987*epsilon/59625)*lambda,
          lambda_minus <= lambda <= 0;
   F(epsilon) - (641/3000 + 2359*epsilon/1125)*lambda,
          0 <= lambda <= lambda_plus.
```
In particular the signed direction lambda=0 has exact optimum `13269/53000+27*epsilon/6625` on the full asymmetric interval. At epsilon=0 this recovers the prior exact inner two pieces.

The following single family of **seedless** flows attains every displayed bound:
```
g=1, a=(44-504*epsilon)/53, b=(44+344*epsilon)/53,
u=w=0, v=a/10+9*b/40, z=a/10.
```
For lambda<0 declare all Q-mass at keys 0,1,2,3; for lambda>0 declare all Q-mass at keys 0,1,2; at lambda=0 key 3 has zero objective coefficient and either declaration is optimal. All remaining declarations are zero. At lambda endpoints with zero coefficients, either choice is permitted.

## Exact proof

1. **Legality and asymmetry.** The displayed a,b are nonnegative throughout the indicated closed epsilon interval. The two only restrictive early-gate upper inequalities are a<=1 and b<=1, equivalent respectively to epsilon>=-1/56 and epsilon<=9/344. The other flow inequalities are saturated: u=w=0, v=C1, z=a/10, v-z=9b/40. Thus 9*b*z=9*a*b/10=4*a*(v-z). Direct substitution in the time equations gives TP=31/10+epsilon and TQ=31/10-epsilon. Endpoint legality plus affinity in epsilon proves legality of the family for every real epsilon in the interval.

2. **Three exact global capacity certificates.** Put dP=TP-31/10, dQ=TQ-31/10, L=(u,C1-v,w,9b/40-v+z), J=1-g. The immutable predecessor proves three exact affine identities, here independently checked by 8-coordinate rational-basis tests at each anchor:
```
 B + alpha*dP + beta*dQ - S_lambda
     = mu0*u + mu1*(C1-v) + mu2*w
       + mu3*(9b/40-v+z) + xi*(1-g).
```
Here S_lambda is the fixed-flow optimum over all random terminal declarations; its keys are {0,1,2,3} on [lambda_minus,0] and {0,1,2} on [0,lambda_plus]. The three anchors (lambda,B,alpha,beta,mu0,mu1,mu2,mu3,xi) are:
```
lambda_minus, 22146/86455,6694/86455,3016/86455,
 22473/345820,7789/69164,46129/345820,81757/622476,0
0, 13269/53000,391/6625,364/6625,
 3999/53000,1283/10600,7127/53000,247/1800,117/10600
lambda_plus, 20391/82945,3184/82945,6526/82945,
 26373/331780,7789/66356,42229/331780,81757/597204,0
```
All five coefficients in each anchor are nonnegative. Therefore for all FULL_HIST flows at the specified times S_lambda<= B+(alpha-beta)*epsilon. The constructed seedless flow has L=0 and J=0, hence equality at **all three** anchors.

3. **Interpolation over all real lambda.** On either side of 0 the set of positive coefficients 1-(1+lambda)*rj is constant, so S_lambda is affine in lambda for each flow. Convex interpolation of two adjacent global nonnegative affine certificates proves the claimed bound at every intermediate real lambda, while the same seedless flow attains equality. Substitution into the stop-mass formulas gives the two bilinear expressions stated above. This also proves the theorem for irrational epsilon and lambda and all endpoints.

The constructed mass vector is explicitly:
```
M0=M6=(16966*epsilon+4719)/47700
M1=11*(27-290*epsilon)/1060
M2=9*(56*epsilon+1)/106
M3=2*(429-1204*epsilon)/11925
M4=(9-344*epsilon)/106
M5=3*(350*epsilon+99)/1060.
```
It has sum Mj=1 and sum rj Mj=1 exactly. The observer at lambda=0 with key 3 undeclared is
```
eQ=(50108*epsilon+11067)/23850
1-eP=(18872*epsilon+1923)/9000.
```
Thus two explicit asymmetric exact four-observer witnesses on the common exposed support are:
```
epsilon= +1/100: W=(172207/225000,144601/298125,311/100,309/100)
epsilon= -1/100: W=(181643/225000,132074/298125,309/100,311/100).
```

## Verification and applicability

Run `python3 VERIFY.py` (standard-library Fraction). The checker tests 24 anchor affine certificate evaluations (origin plus each coordinate unit vector), exact mass normalization and LR moment identities, endpoint legality and seedless identity, bilinear formula coefficients, and the two explicit W witnesses. `EXACT_OUTPUT.txt` is the stdout of the actual execution. Because the identities are affine in the seven real flow variables, the rational basis check establishes them algebraically on all real flows. Because the central policy and its support on each side are bilinear in epsilon and lambda, coefficient checks together with the proof's interpolation establish the full real rectangle. No floating approximation underlies the theorem.

Research category: exact analytic result with executable algebra verification; independent mathematical review pending. Native research gateway read returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false on 2026-11-07; no native CLAIM/Result/Review or active ownership asserted. Published PR-branch provenance is author-side evidence, not formal mathematical admission.

## Next scientific unit

Use the exact common central strip as a benchmark, and characterize how the two outer support switches vary with asymmetric epsilon, starting at epsilon=+/-1/100. Search for a rational lambda/timing direction outside this strip where FULL_HIST strictly outperforms every seedless LR timing configuration; alternatively prove a larger common-support band. See NEXT_UNIT.md.
