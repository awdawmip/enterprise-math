# A new P11 core (5,4): a rank-zero and two-primary Sha paper candidate

Status: AUTHOR PAPER / UNREVIEWED NEW CORE. Author EM-DVR-F73673, directed paper research under the existing true Driver session. No scientific program, enumeration, point search, factorization program, Lean execution, Task/claim or Native acceptance is asserted. This is not part of the official fixed-(233,119) certificate Task and is not covered by that core’s three earlier nonauthor paper reports.

## 1. Exact new input and conclusion under review

Take the primitive Euclidean core (r,s)=(5,4). Its legs and hypotenuse are
A=25−16=9, B=2·5·4=40, C=41.
Thus P=A+B=49, Q=|A−B|=31, and
E: y²=x(x−49²)(x−31²),  D=49²−31²=1440=2^5·3²·5.
The root order is (0,2401,961), and gcd(P,Q)=1. The support is S={2,3,5,7,31}, since49=7². These are written exact integer identities; no program was used to obtain them.

The author-derived conclusion is
dim_F2 Sel²(E/Q)=4,  rank E(Q)=0,
Sha(E/Q)[2∞]≅(Z/2Z)².
No assertion is made about odd-primary Sha, full Sha finiteness, finite odd torsion, or other cores. The existing accepted diagonal correspondence would then imply finitely many strict primitive diagonal outputs for this core; it does not identify those outputs or rule out isolated strict points from odd torsion.

This is a new paper input, not an extrapolation of rank1 for (11,8). The exact proof follows, including all places and the distinction between local solubility and global points.

## 2. Complete local-image input and exact Selmer space

Apply the separately frozen author paper P11_PARAMETRIC_LOCAL_IMAGE_AND_DYADIC_OBSTRUCTION_PAPER.md. Its full proof uses Kummer with kernel2E(K), local image order4 at odd p/order8 at2, and Stoll’s split full2-descent identification. It is itself pending independent review; a gap in that lemma kills this paper’s downstream conclusion.

Because32|D:
I2={(1,b)}.
At p3 and p5 dividing D:
I3=I5={(1,b)}.
At p7 dividing P and p31 dividing Q, both primes are3 mod4:
I7=I31={(a,b): both classes unramified units}.
At every other odd prime the good-prime image is the same unit-pair subgroup. At infinity the first coordinate is positive and the second arbitrary in sign.

Represent global squareclasses by signed S-units. The first coordinate a must have zero coefficients at −1 (infinity),2 (I2),3,5 (I3,I5),7,31 (unramified pairs). Hence a=1 exactly. The second coordinate b has zero7 and31 coefficients and no other restriction. Conversely every b in the span of −1,2,3,5 satisfies all the complete local images, including unit-character conditions, since a=1. Thus the full Selmer group is exactly
W={(1,b,b): b∈〈−1,2,3,5〉}, dim W=4.
The four displayed generators are independent rational squareclasses, so this is an equality, not an upper bound from sampled classes.

The rational 2-torsion Kummer classes are
δ(T0)=(1,−1,−1), δ(TP)=(1,10,10),
since D=12²·10; δ(TQ) is their product. The classes −1 and10 are independent. They span a two-dimensional known rational subspace K. Select the two remaining classes
U=(1,2,2), V=(1,3,3).
They lie in W and are independent modulo K. Their covers are locally soluble at every place by the complete table. This does not give either a rational point or a nonzero rank.

## 3. Actual Cassels pairing model and tangent normalization

Use the full split 2-cover for U:
z0²−2zP²=P²t²,  z0²−2zQ²=Q²t².
The third conic is2(zQ²−zP²)=Dt². It has the rational point
(zP,zQ,t)=(719/2,721/2,1),
since (721²−719²)/4=720=D/2.
The other two conics have rational points (z0,zQ,t)=(Q,0,1) and (z0,zP,t)=(P,0,1). Choose tangents
L2=Qt−z0, L3=z0−Pt, F=L2L3.
The first tangent contributes against V’s first coordinate1 and does not affect the numerical product. If a chosen local point lies on that unused tangent, move it off its finite divisor within the smooth local curve while retaining the two nonzero evaluated squareclasses.

The full2-descent Cassels formula gives
〈U,V〉=∏_v(F(q_v),3)_v.
This is the same root-ordered full Kummer representation, not a two-isogeny or a projection of P11.

Primary sources are the same versioned sources actually read for the fixed-core paper:
Fisher–Schaefer–Stoll, “The yoga of the Cassels–Tate pairing,” arXiv0710.2079v1 (all8pages; PDF SHA25670c46caaf9b6a34efc65e341a610afc62b5ca3e7591ee3ec133287c4b78f32b4), especially the tangent pairing and Theorem5.2; Shukla–Stoll, arXiv2302.01640v1, equations3.9–3.10 and Theorem5.6 (PDF SHA256f84fee9a3cd3e2e37aee1c0b41f08296e88988a5f1142c5911b4d16762e408ce).

For the short Weierstrass convention in the latter source, translate x=X+(P²+Q²)/3. Root differences and the displayed split covering equations are unchanged over every Q_v, including Q3. The long model x³−(P²+Q²)x²+P²Q²x is also within the former source’s stated a2 model. The derived pairing is alternating/bilinear and contains the rational Kummer image in its radical; its induced pairing on Sha[2] agrees with Cassels–Tate. These are source theorems, not an inference from the local product.

## 4. Place3: the negative factor

The unit −1/2 is1 modulo3, so there is r∈Q3 with r²=−1/2. Hensel applies to the residue r=1 because the derivative2r is a unit. Set
q3=(z0,zP,zQ,t)=(0,49r,31r,1).
Both equations hold exactly. F=−49·31=−1519 is a3-adic unit with residue2. Since3 is a uniformizer,
(F,3)_3=(−1519/3)=−1.
There is no guessed local-index or point-count substitution here.

## 5. Place5: a separate explicit non-chart point

Here2 and−2 are both nonsquares modulo5, so neither of the fixed-core shortcuts using sqrt2 or sqrt(−1/2) applies. This is a substantive difference from (233,119).

Take z0=2,t=1 and choose
zP²=(4−2401)/2=−2397/2,
zQ²=(4−961)/2=−957/2.
Each radicand is4 mod5. Each therefore has a root2 mod5, by Hensel with unit derivative4. These roots provide a point on both cover equations. Its two tangent values are the exact nonzero integers
L2=31−2=29, L3=2−49=−47, F=−1363.
Both F and3 are units at5. The odd-prime Hilbert symbol of two units is+1, hence (F,3)_5=+1. No running search for this point is used.

## 6. Places7,31 and infinity

At7, sqrt2 has residue3; at31 it has residue8. In each case the derivative2sqrt2 is a unit, so Hensel supplies a local square root. Over R use the positive real square root. At all three places set
q_v=(sqrt2,1,1,0).
Then F=−2. At7 and31 both −2 and3 are units, giving+1. At infinity the second Hilbert argument3 is positive, giving+1 regardless of F’s sign. Smooth local perturbations handle the unused tangent if necessary; F stays nonzero and its squareclass stays unchanged.

## 7. Place2: an explicit exact norm certificate

Set t=1, zP=88, zQ=92, and choose
w²=P²+2·88²=2401+15488=17889.
This is an odd unit1 mod8, so it has a2-adic square root. The second equation holds because
17889−2·92²=17889−16928=961=Q².
Choose the sign of w so that w≡49 mod4. Then v2(w+49)=1, and
(w−49)(w+49)=15488=2^7·121
gives w−49=64k with k odd. Substitution gives exactly
49k+32k²=121.
Consequently k≡1 mod8. The tangent values have squareclasses
L3=w−49=64k ∼1,
L2=31−w=−18−64k=−2(9+32k) ∼−2.
Thus F∼−2. The exact rational norm identity
N_{Q2(sqrt3)/Q2}(1+sqrt3)=−2
proves (F,3)_2=(−2,3)_2=+1. This records the dyadic branch, radicands, valuations and norm witness, rather than reusing the old fixed-core dyadic number5017 or a guessed Hilbert sign.

## 8. Every other prime, without a prime cutoff

For p∉{2,3,5,7,31}, the complete local table supplies a point q_p on U’s cover. Move off the zero tangents and scale to primitive integral coordinates. All of2,P,Q,D,3 are p-adic units.

If p divides z0−Pt, then t must be a unit: otherwise z0,zP,zQ,t would all be divisible by p from the two equations, contradicting primitivity. Hence z0+Pt is a unit, and
(z0−Pt)(z0+Pt)=2zP²
makes v_p(z0−Pt) even. The same argument with Q gives even valuation for Qt−z0 whenever that factor is nonunit. Therefore v_p(F) is even. Since3 is a unit and p is odd, the Hilbert symbol (F,3)_p is+1.

This is a proof for all remaining primes, not evidence from testing a finite list. It also states why primitive scaling, the unit hypotheses, smoothness and nonzero tangents are necessary.

## 9. Radical, exact rank and the two-primary group

All local factors are+1 except the factor at3. Hence the paper calculation gives 〈U,V〉=−1.

An alternating form on the four-dimensional W with this nonzero2×2 block has rank at least2, so its radical has dimension at most2. The rational Kummer image E(Q)/2E(Q) lies in that radical and already contains the two independent torsion classes K. Thus the radical and rational image both equal K and have dimension2.

Mordell–Weil gives dim E(Q)/2E(Q)=rank E(Q)+dim E(Q)[2]=rank+2. Consequently rank E(Q)=0. No positive-rank point, height saturation, good-reduction count or descent enumeration is used.

The exact Kummer sequence then gives dim Sha(E/Q)[2]=4−2=2. The induced Cassels–Tate pairing on this quotient is nondegenerate because the radical on W is exactly K. If a class c∈Sha had order4, its nonzero double2c∈Sha[2] would pair trivially with every t∈Sha[2], since
〈2c,t〉=〈c,2t〉=0.
That contradicts nondegeneracy. Higher2-power order would yield an order4 class by taking a multiple. Hence
Sha(E/Q)[2∞]=Sha(E/Q)[2]≅(Z/2Z)².
No finiteness assumption on the full Sha group is used; the odd-primary part is untouched.

## 10. Audit obligations and failure branches

This proof must receive a new genuinely nonauthor paper review. Its earlier fixed-(233,119) reviewer’s three PASS reports do not imply acceptance here. The review must cover the new complete local-image lemma, repeated factor P=7², the dimension4 global intersection, the distinct5-adic point, the dyadic branch k≡1, the model translation, all outside-support primes, and radical/2-primary deductions.

Kill at the first failed local-image necessity/index claim, wrong source hypothesis, incorrect cover/tangent normalization, zero-factor mistake, bad Hensel condition or false norm/product. A failure retains only the exact proved weaker boundary; it never silently promotes dim4 or rank0. No new Task or computation is authorized by this paper.

Contributions: accepted old diagonal arithmetic and general core/Kummer interface remain the original authors’ work; EM-DVR-3B8E7F proposed the earlier fixed-core rank direction; EM-PARITYREV-12B648 supplied its bounded planning audit; EM-DVR-F73673 alone authors this new parameter lemma and new (5,4) derivation. The old fixed-core independent reviewer has not yet reviewed either new object. The parent objective remains OPEN; no old Task is reopened or current certificate scope expanded. No claim of historical novelty is made.

