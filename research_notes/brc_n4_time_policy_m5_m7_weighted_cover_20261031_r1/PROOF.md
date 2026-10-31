# BRC N=4 — five to seven ex-ante policy labels are insufficient for better-than-2/3 time reconstruction

Date: 2026-10-31. **AUTHOR_EXACT_FINITE_PROOF / EXECUTED_INTEGER_CHECK / UNREVIEWED / NOT_ADMITTED**. This is a finite positive-mass BRC observer theorem, not a P000 native-X6 physical-dynamics result.

## Exact game

Reuse the frozen strictly positive P/Q 16-leaf model. On typed latent fibres (AU0,AU1,AV,BU0,BU1,BV) the distinct prepared rows are

```
M=(1/20)*[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
          [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]].
```

The observer retains only the stop time T in {1,2,3,4}. The same lawful S23 policy H is applied to each source preparation. A common stochastic encoder E with k states is fixed before H. The ex-ante policy label L(H) has at most m values; a decoder D_l can depend on l, but neither on H beyond l nor on the realized input or hidden coin. Source-wise loss is total variation:

```
R_(k,m)= inf_(E,L,D_1,...,D_m) sup_(lawful H)
         max_(prepared i) TV((M K_H)[i,.],(M E D_(L(H)))[i,.]).
```

## New exact theorem

For ALL integers k>=1 and m=4,5,6,7, **R_(k,m)(S23;T)=2/3**. Additionally, **R_(1,m)(S23;T)=2/3 for EVERY m>=4**, even if the entire subsequent policy is communicated to the one-state decoder. This result applies to all lawful behaviorally randomized S23 policies in the declared grammar; the finite lower witnesses are deterministic. The sensor noise epsilon is immaterial because the sensor and its presence flag are absent from T.

## Upper 2/3, inherited with precise source and scope

The prior exact author-side four-label proof at immutable commit `60aaef914954cb656a2f74140d77e2e647030eda` constructs a policy-dependent omitted time t*(H) with Pr_i(T=t*)<=2/3 for every prepared input. The midpoint structure of AU_Q and BU_Q and the stage-one A/B information restriction force at most three heavy times. One common state and four labels identify t*: decode uniformly over the other three time points. Then TV<=2/3 on every prepared input. Extra labels/states remain unused. This analytic upper works for *all* behaviorally randomized lawful S23 policies. Our verifier also checks 2048 deterministic tables and 12288 exact row/decoder inequalities.

## Lower: 64 genuine deterministic policy signatures

There are 2^2 time-one A/B bits, 2^3 time-two bits with AU/BU tied, and 2^6 LR time-three bits: 2048 deterministic lawful tables. Among them the 64 signatures for which AU0=AU1 stop time and BU0=BU1 stop time yield *point mass* time observations for the four Q-prepared provenance inputs. With H={2,3,4} and G={3,4}, the set of genuine signatures s=(t_AU,t_AV,t_BU,t_BV) is the DISJOINT union

```
C0={(1,1,1,1)}                                    (1)
C1={(1,1,x,y) : x,y in H}                          (9)
C2={(x,y,1,1) : x,y in H}                          (9)
C3={(2,x,2,y) : x,y in H}                          (9)
C4={(x,u,y,v) : x,y in G, u,v in H}               (36)
                                                    64.
```

This five-block decomposition is obtained by case-splitting the two first-stage continuation decisions and, when both continue, the shared AU/BU stage-two decision. The verifier enumerates all 2048 tables and checks equality with these 64 signatures, retaining actual witness tables.

Suppose an encoder and label-conditioned decoders achieved error strictly below 2/3. For one fixed label l, denote the decoded law for the j-th Q-prepared source by q_(j,l). It is fixed across policies H with label l, even for stochastic encoding. A point-mass signature assigned l requires

```
TV(delta_(s_j),q_(j,l))=1-q_(j,l)(s_j)<2/3,
so q_(j,l)(s_j)>1/3.
```

A probability distribution on four times has at most TWO entries strictly exceeding 1/3. Thus all signatures assigned l must lie in a Cartesian box A_l x B_l x C_l x D_l with at most two time values in each coordinate. There are exactly binom(4,2)^4=1296 maximal boxes.

## New exact weighted cover certificate

Assign nonnegative integer weights w(s) by disjoint signature class:

```
class:       C0  C1  C2  C3  C4
w(s):        16   5   5   6   2
class size:   1   9   9   9  36
total weight = 16+45+45+54+72 = 232.
```

For any two-choice sets A,B,C,D, put h(X)=|X intersect {2,3,4}| and g(X)=|X intersect {3,4}|. Its box weight has the exact factorization

```
W(A,B,C,D)=
 16*[1 in A,B,C,D]
 +5*[1 in A,B]*h(C)*h(D)
 +5*h(A)*h(B)*[1 in C,D]
 +6*[2 in A,C]*h(B)*h(D)
 +2*g(A)*h(B)*g(C)*h(D).
```

The integer verifier independently computes the direct sum of all weights inside the box and the displayed factorization, for ALL 6^4=1296 maximal boxes. Its exhaustive result is **W<=32**, with exactly 90 boxes attaining equality. If m label-boxes covered the 64 signatures, positivity would force 232<=sum_l W(box_l)<=32m. For m<=7, 32m<=224<232, contradiction. Consequently R_(k,m)>=2/3 for all k and m<=7. Combined with the previous explicit four-label decoder, equality follows for 4<=m<=7.

## All m>=4 with one code

The lawful deterministic table with (a,b,c)=(3,5,27), using the bit ordering in VERIFY.js, produces AU:T=3, AV:T=2, BV:T=4. A one-state decoder, even told all of H, must represent these three distinct point masses with a single probability vector q; at least one of q(2),q(3),q(4) is <=1/3, so max TV>=2/3. The four-label construction attains 2/3. Therefore R_(1,m)=2/3 for every m>=4.

## Verification and limits

VERIFY.js executed as the identical function body evaluated during this publication, with exact integers: P/Q each 16 strictly positive leaves; all 2048 deterministic lawful S23 tables, 12288 upper-bound inequalities; 64 real policy signatures; 1296 complete box checks (direct sum and independent factored count), total weight 232, maximum box weight 32, and an explicit one-code witness. The analytic lower uses finite exhaustive coverage, not a grid over stochastic encoders. Arbitrary randomized S23 upper relies on the pinned heavy-time lemma, not extrapolation from 2048 tables. Neither S2 information grammar nor native X6/independent physical-time fidelity, signed/complex amplitudes, Shor speedup or physical residual attribution is established. The result awaits independent mathematical review and formal project admission.
