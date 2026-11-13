# BRC N=4 / S23: exact full-policy storage phase diagram

2026-11-01 · Portable author-side analytic proof + executed exact Fraction checker · UNREVIEWED / NOT_ADMITTED.

## Model and quantifiers

Six latent sources, in order: AU0, AU1, AV, BU0, BU1, BV. The positive-preparation mixing matrix and exact inverse are

M =
[[1/2,1/2,0,0,0,0],
 [9/20,11/20,0,0,0,0],
 [0,0,1,0,0,0],
 [0,0,0,1/2,1/2,0],
 [0,0,0,1/10,9/10,0],
 [0,0,0,0,0,1]].

N = M^-1 =
[[11,-10,0,0,0,0],
 [-9,10,0,0,0,0],
 [0,0,1,0,0,0],
 [0,0,0,9/4,-5/4,0],
 [0,0,0,-1/4,5/4,0],
 [0,0,0,0,0,1]].

For a lawful causal S23 stopping policy H let F(H) be its 6×4 stochastic latent-stop-time kernel; readout is MF(H) on the four times T=1,2,3,4. The common encoder E is an arbitrary REAL nonnegative row-stochastic 6×k matrix fixed before the future policy is chosen. The decoder D_H is a policy-informed row-stochastic k×4 matrix that may depend on the complete future policy. The minimax loss R(k,full) is inf_E sup_H inf_D max_i TV((MF)_i,(MED)_i). The 11 S23 information-set controls have 2 first-stage A/B bits, 3 second-stage bits and 6 terminal source bits; there are 2048 deterministic policies, together with all lawful behavioral randomized policies.

## Theorem (complete exact full-policy storage curve)

R(k,full) = 2/3 (k=1); 1/2 (k=2 or 3); 1/5 (k=4); 1/40 (k=5); 0 (k>=6).

**The newly closed cases here are k=2, k=3, k=4, for every real stochastic encoder and all behavioral S23 policies.** The k=1 heavy-time and k=5 dual/construction endpoints were established in predecessor notes; proofs are reproduced succinctly for the complete curve. This does NOT solve finite-m strategy-label minima, because allowing D_H to depend on the full H is strictly more informative.

## Shared signed readout dual lemma

For E row-stochastic with k<6, choose any nonzero z in ker(E^T). Because E·1_k=1_6, sum(z)=0. Let P=sum(z_x over z_x>0)=sum(-z_x over z_x<0)>0. A lawful deterministic S23 policy may continue at both previous stages and stop at time 3 exactly on source set S={x:z_x>0}, and at time 4 on the rest: the time-3 true latent column is u=1_S. For the time-3 decoder column d, let r=M(u-E d). If all six prepared TV errors are <=epsilon, ||r||_infinity<=epsilon. Since N=M^-1,

P=z^T u = z^T (u-E d)=z^T N r <= ||N^T z||_1 epsilon.               (1)

Thus epsilon >= P/||N^T z||_1 for ANY common real E and ANY policy-informed stochastic decoder. This is a readout-difference dual, not physical negative BRC mass. For any zero-sum scalar weights v_j with positive mass P and fixed comparison rows r_j,

||sum_j v_j r_j||_1 <= P·max_{i,j}||r_i-r_j||_1.                 (2)

Proof: normalize the positive and negative v parts to probability distributions p,q; expand sum v_j r_j/P as sum_i,j p_i q_j (r_i-r_j) and use the triangle inequality.

## New lower bound k=4: one forced nullspace equality

dim ker(E^T)>=2 for every 6×4 E. Intersect with the hyperplane z0=z1; a nonzero z necessarily survives. Write z=(a,a,z2,z3,z4,z5), and v=(2a,z2,z3,z4,z5), which has zero sum and exactly the same positive mass P. Define five comparison rows

rA=(N0+N1)/2=(1,0,0,0,0,0), r2=N2, r3=N3, r4=N4, r5=N5.

Their maximal pairwise L1 distance is exactly 5: ||r3-r4||_1=5, while every other pair has distance <=9/2. Since N^T z = 2a rA+z2 r2+z3 r3+z4 r4+z5 r5, equation (2) gives ||N^T z||_1<=5P. Equation (1) gives R(4,full)>=1/5. This argument includes rank-deficient, non-rational and randomized encoders.

## New lower bound k=2,3: two forced nullspace equalities

For k<=3, dim ker(E^T)>=3. Simultaneously impose z0=z1=a and z3=z4=b: two homogeneous constraints leave a nonzero z. Direct multiplication with the exact N yields

N^T z = (2a,0,z2,2b,0,z5), and ||N^T z||_1=2|a|+|z2|+2|b|+|z5| = 2P.

Equation (1) implies R(k,full)>=1/2 for k=1,2,3. This improves the previous support-subset floors 2/5 (k=2) and 1/5 (k=3), since the whole kernel dimension is used.

## Matching upper bounds, valid for ALL six-source stochastic F

Denote latent time laws f0,...,f5. Write A_P=(9 f0+11 f1)/20, A_Q=(f0+f1)/2, B_P=(f3+9 f4)/10, B_Q=(f3+f4)/2. Let a=(19f0+21f1)/40 and b=(3f3+7f4)/10. For any stochastic F,

TV(A_P,a), TV(A_Q,a) <=1/40;
TV(B_P,b), TV(B_Q,b) <=1/5.

k=4: deterministic common encoder groups (0,1), (2), (3,4), (5), and the complete-policy decoder outputs respectively a, f2, b, f5. Prepared errors are at most 1/40,0,1/5,0; hence R(4,full)<=1/5.

k=3: common encoder groups (0,1), (2,5), (3,4), and decoder outputs a, (f2+f5)/2, b. Mixed AU error <=1/40, mixed BU <=1/5, and AV/BV error <=1/2; hence R(3,full)<=1/2.

k=2: common encoder groups (0,1,2) and (3,4,5), and decoder outputs dA=(A_P+f2)/2 and dB=(B_P+f5)/2 respectively. Pointwise A_Q >= (1/2) A_P, because coefficients (1/2,1/2)>=(9/40,11/40). Both dA>=(1/2)A_P and dA>=(1/2)f2. Thus each of A_P,A_Q,f2 has overlap with dA of at least 1/2 (sum of pointwise minima), and hence TV<=1/2. Analogously, B_Q>=(1/2)B_P because coefficients (1/2,1/2)>=(1/20,9/20), while dB dominates B_P/2 and f5/2. Hence all three B prepared laws have TV<=1/2. Consequently R(2,full)<=1/2.

These decoders are stochastic and affine/linear in F; they work for every six-by-four stochastic F, not just the 2048 deterministic policies, so the full behavioral S23 upper bounds are analytic.

## Existing endpoints and phase-diagram closure

k=5: any nonzero left kernel z yields (1), and all six inverse N rows have pairwise L1 diameter 40, giving >=1/40. Merge only (0,1), keep sources 2,3,4,5 separate and decode the merged symbol by a; this gives <=1/40 for every F. Hence k5=1/40.

k>=6: retain all six sources separately; D_H=F(H) gives zero error.

k=1: for every lawful behavioral S23 policy at most three of the four output times can be heavy (>2/3) for at least one prepared input. Within each AU or BU mixture pair, the equal-source-mixture Q and the other convex mixture P cannot be heavy at distinct times: Q(t)>2/3 implies F0(t)+F1(t)>4/3, forcing the sum at any different t' to be <2/3 and therefore P(t')<2/3. AV and BV add at most one heavy time each. If time 1 is heavy for either A or B, the first-stage A/B information restriction means every input of that group has >2/3 mass at time 1, precluding later heavy times there; the other group contributes at most two. If time 1 is not heavy, only 2,3,4 can be heavy. Hence choose an omitted non-heavy time t* and decode from one common symbol the uniform law on the other three times. Every prepared law has >=1/3 mass outside t*, yielding overlap >=1/3 with that uniform decoder (sum min(p_i(t),1/3)>=min(sum_{t!=t*}p_i(t),1/3)); TV<=2/3. Conversely, lawful S23 decisions A stops at time 1, B continues, BU stops at time 2, BV continues and stops at time 3 yield three distinct prepared delta laws. A one-state decoder q must have max error >=2/3. So k1=2/3.

## Verification, boundary, provenance

VERIFY.py was actually executed with Python Fraction and tested all 36 entries of MN=I, ten effective inverse-row distances, six pair distances, 344 small integer dual vectors, all 2048 deterministic S23 tables and 36864 six-prepared-law TV comparisons across k2,k3,k4. RUN_EVIDENCE.txt is verbatim stdout. Universal real-encoder results are analytic rank-nullity statements, not finite search claims; the upper bounds apply to every stochastic F, including all lawful behavioral causal strategies. No independent mathematical review, Lean formalization, native Result admission, or physical validation is asserted.

BRC semantics: six strictly positive source laws with retained provenance; M is an external prepared-mixture observer; future operation is causal S23 stopping; residual is worst-case time-readout TV after common state compression. Signed z is dual bookkeeping only. The six latent source names are not P000's six native spatial axes; the four stopping times do not define P000's independent time evolution or any three-dimensional slice.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@c93fe73d7cc7391e8c27c5c51e0552ecfd611b2a, Enterprise Math main@f8cc8141ca4c92b793ec694de7bfff9ad5e3bba6. P000 projection blob c6d4d2d79b09537bdae55253baef9c28583e44dc matched canonical original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. See SOURCES.md for immutable predecessor science refs; NEXT_TASK.md for genuine open problems. Native research_authority_granted=false and owner read CONTROL_QUOTA were observed on this run; authorship is explicitly portable author-side, UNREVIEWED / NOT_ADMITTED.