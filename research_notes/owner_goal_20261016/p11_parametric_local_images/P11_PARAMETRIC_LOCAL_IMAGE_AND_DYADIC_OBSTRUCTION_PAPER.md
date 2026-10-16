# Parametric local Kummer images and a dyadic obstruction for P11 cores

Status: AUTHOR PAPER / UNREVIEWED NEW PARAMETER INPUT. This is a directed, reversible paper derivation by EM-DVR-F73673, not a Tool, new Task, Native Result, Driver acceptance or extension of the active fixed-(233,119) certificate Task. No arithmetic program, enumeration, point search or scientific invocation was run. The earlier nonauthor checks of the fixed core do not review this paper.

## 1. Exact model, sources and declared result

Let P,Q be distinct positive coprime odd integers, D=P²−Q²≠0, and
E: y²=x(x−P²)(x−Q²).
The root order is (0,P²,Q²). Write local Kummer classes as (a,b), with third class ab. Ordinary points map to (x,x−P²,x−Q²); at a zero coordinate use the product of the two other root differences. Thus
δ(O)=(1,1,1), δ(T0)=(1,−1,−1), δ(TP)=(1,D,D), δ(TQ)=(1,−D,−D).

External elliptic curves and p-adic fields retain their classical types. They are not native spatial models, reductions of Heartbeat X6, or Working Truth/Foundation changes. Static arithmetic needs no added time axis.

Author-derived local-image statement:

* For odd p not dividing PQD, I_p consists exactly of pairs of unramified unit squareclasses.
* For odd p|D, I_p={(1,b): b∈Q_p*/Q_p*²}.
* For odd p|P and p≡1 mod4, I_p={(a,a)}.
* For odd p|Q and p≡1 mod4, I_p={(a,1)}.
* For odd p|PQ and p≡3 mod4, I_p consists exactly of pairs of unramified unit squareclasses.
* At infinity I_∞={(+, +),(+, −)} in the first two coordinates.
* If 32|D, then I_2={(1,b): b∈Q_2*/Q_2*²}.
* For every such odd P,Q, irrespective of 32|D, the particular class U2=(1,2,2) is locally soluble at 2 if and only if v_2(D)≠4.

These are exact image statements, not local sampling. The last equivalence gives a real failure branch for the attempted fixed-core extrapolation. This paper does not classify the whole dyadic image when v_2(D)=4 and makes no constant Selmer-dimension, positive-rank, saturated-generator or whole-family claim.

Primary ingredients already source-checked in the earlier applicability paper: Michael Stoll, “Implementing 2-descent for Jacobians of hyperelliptic curves,” Acta Arith.98(2001),245–277, DOI10.4064/aa98-3-4, Lemmas4.1,4.3,4.4,4.8 and Proposition4.2, specialized to monic squarefree degree3 and split étale algebra Q³. Exact PDF SHA256 b4854a404601da748a687c64a3d72a36033590a4ba911b7021db53340c5aa9d1. The new valuation arguments below are provided here, not attributed to an uninspected textbook.

Immutable prior interface: Source62f22f7432923ac4c04d9a89944957654920a481, research_notes/owner_goal_20261016/p11_fixed_curve_paper/P11_PRIMARY_THEOREM_APPLICABILITY_AND_EXACT_SCOPE.md, SHA256 a322dd552307535d600dcabc0999af3d1df57ef7e4da682a0190a3ee6500412b. Its acceptance status is paper support, not a new Native vote.

## 2. Why a necessary squareclass condition proves a complete local image

The Kummer homomorphism has kernel 2E(K). Since all three nonzero 2-torsion points are K-rational, the image has order4 for odd p, order8 for p=2, and order2 over R. One elementary check of the finite indices is as follows. Choose a sufficiently deep torsion-free open formal subgroup H with formal logarithm H≅Z_p. Multiplication2 on H has index1 for odd p and2 at p2. The map E/H→2E/2H has kernel (E[2]+H)/H of order4: if 2x∈2H, subtract its H-half to obtain an element of E[2]. Consequently [E:2E]=4[H:2H]. This also explains the use of full 2-torsion rather than a two-isogeny index.

For odd p, the squareclasses of units form a group of order2. Therefore the unit-pair subgroup, or any one of the displayed one-coordinate subgroups with the other coordinate arbitrary, has order4. It suffices to prove containment in that subgroup. At2 the vertical subgroup has order8, so the same method proves equality. This avoids constructing four/eight arbitrary sample points and pretending they exhaust an image.

Throughout, for odd p, an element of 1+pZ_p is a square; an odd 2-adic unit is a square exactly when it is1 mod8. Negative valuations and zero factors are dealt with explicitly.

## 3. All odd primes

### Good primes

If p∤2PQD the three roots are distinct modulo p. For a point with v_p(x)<0, all three factors have that valuation, so 3v_p(x)=2v_p(y) forces v_p(x) even. If x is integral, at most one of x,x−P²,x−Q² can have positive valuation, and its valuation is even from the curve equation. The exceptional 2-torsion definitions are units at p. Hence both first coordinates are unramified, and the index proves the claimed equality.

### p|D

Here p∤PQ and P²≡Q²≠0 mod p. We prove that x is square whenever it is a nonzero ordinary coordinate.

If v_p(x)<0, the two correction factors 1−P²/x and1−Q²/x are squares, so y²=x³ times a square implies x square. If v_p(x)>0, the other two factors have product a square unit, with residue P²Q²; again x is square. If x is a unit congruent to P² mod p it is itself square. Otherwise the product (x−P²)(x−Q²) is a square unit, because its residue is the nonzero square (x−P²)², and the equation forces x square. The exceptional first coordinates P²Q²,P²,Q² are squares. Thus I_p lies in {(1,b)}, and the local index proves equality for every exponent v_p(D)>0.

### p|P and p≡1 mod4

Now p∤Q and −1 is square. We prove x−Q² square, which is exactly a=b because the three Kummer classes multiply to1.

For v_p(x)<0, the preceding correction-factor argument shows x square, hence x−Q² square. If v_p(x)>0, x−Q² is a unit with square residue −Q². For unit x not congruent to Q², the factors x and x−P² have product a square unit with residue x²; the curve equation forces x−Q² square. If unit x is congruent to Q², both x and x−P² are square units, with residue Q², giving the same conclusion. At the exceptional points the third classes are respectively −1,D, and Q²(Q²−P²), all squares at p. The index completes the diagonal-image assertion.

For p|Q and p≡1 mod4 interchange the colliding roots 0,Q² and the remaining square root P². The identical argument proves that the second class x−P² is square, hence I_p={(a,1)}.

### p|P and p≡3 mod4

Write h=v_p(P)>0. We prove that x and x−P² both have even valuation. Negative v_p(x)=k gives all three factor valuations k, so k is even. At v_p(x)=0 both first factors are units. For k=v_p(x)>0:

* If k<2h, then x(x−P²) is a square class, since x−P²=x(1−P²/x), while x−Q² has nonsquare unit class −1. The equation is impossible.
* If k>2h, both x−P² and x−Q² have class −1, so x must be square; k and v_p(x−P²)=2h are even.
* If k=2h, the equation forces v_p(x−P²) even as well.

At T0 the first two exceptional valuations are 2h and2h; at TP they are2h and2h; at TQ both are0. All are even. Thus both coordinates are unramified, and the index supplies all unit pairs. For p|Q and p≡3 mod4 the same reasoning makes the first and third coordinates unramified, and their product makes the second unramified too. Multiplicities in P or Q do not change these conclusions.

## 4. The dyadic vertical image when 32 divides D

We first show that the first Kummer class is square. For an ordinary point with k=v_2(x)<0, all factors have valuation k, so k is even. If k≤−4, both correction factors1−P²/x and1−Q²/x are squares. If k=−2, each is5 mod8, and their product is1 mod8 and square. In either case the equation makes x square.

If k>0, x−P² and x−Q² are odd and congruent mod8, so their product is square; x is square.

If x is an odd unit, its only nonsquare residues mod8 are3,5,7. In residues3 or7, put m=v_2(x−P²)=1; in residue5 put m=2. Because 32|D, the odd units
(x−P²)/2^m and (x−Q²)/2^m
are congruent mod8 in both cases, and their product is square. The curve equation would then force x square, a contradiction to the selected residue. Residue1 already is a square unit. At the exceptional points the first coordinates are squares as above.

Thus the image is contained in the vertical subgroup. Both have order8, proving I2={(1,b)}. No condition on the odd part of D was assumed.

## 5. The sharp dyadic obstruction for U2

Use its actual 2-cover
z0²−2zP²=P²t²,   z0²−2zQ²=Q²t².
There is no nonzero Q2 point with t=0, since2 is nonsquare. Normalize t=1. In the first equation the two valuations 2v2(z0) and1+2v2(zP) have different parity, so a negative minimum cannot cancel. Thus z0,zP are integral, z0 odd; likewise zQ integral. Reduction modulo8 forces zP,zQ even. Writing zP=2u,zQ=2v gives
D/8=v²−u²,  u,v∈Z2.
A difference of two integral squares is never2 mod4. Hence v2(D)=4 is impossible.

Conversely write n=D/8. It is an integer since P,Q are odd. If n is odd, take u=(n−1)/2,v=(n+1)/2. If4|n, take u=n/4−1,v=n/4+1. Then v²−u²=n exactly. The unit P²+8u² is1 mod8, so it has a root w∈Q2. Set z0=w,zP=2u,zQ=2v,t=1. Both equations hold. These are exactly the two cases n≠2 mod4, i.e. v2(D)≠4.

This is an obstruction to the specific U2 class, not a nonexistence theorem for rational points on E and not a classification of I2 at the excluded valuation.

## 6. Euclidean cores and a finite exact Selmer matrix

For a primitive opposite-parity core r>s>0, let
A=r²−s², B=2rs, P=A+B, Q=|A−B|, D=4AB.
Then P,Q are odd and coprime. If e is the even member of {r,s}, v2(D)=3+v2(e). In particular:

* 4|e implies32|D and the entire preceding local table applies, including the complete dyadic image.
* e≡2 mod4 implies v2(D)=4 and U2 is locally obstructed at2.

For the first branch, let S be the prime support of2PQD. Represent the first two global squareclasses by signed S-units, with 2(|S|+1) F2 coordinates. The complete 2-Selmer group is the kernel of these explicit linear conditions:

1. first-coordinate sign positive at infinity;
2. first coordinate square in Q2 (valuation parity and odd unit mod8);
3. at each odd p|D, first coordinate square in Qp;
4. at each p|P, p≡1 mod4, the two coordinates equal in Qp;
5. at each p|Q, p≡1 mod4, the second coordinate square in Qp;
6. at each p|PQ, p≡3 mod4, both coordinate valuations even.

Every remaining prime sees an unramified unit pair automatically. Conditions at each odd prime are valuation parity plus the relevant Legendre-unit character, so this is a finite exact matrix, not an exhaustive squareclass search. Stoll Proposition4.2 identifies its kernel with the full 2-Selmer group, not merely a sampled bound. The dimension is the number of input bits minus the actual matrix rank; it is not uniformly5.

Failure/kill boundary: noncoprime or even P,Q, repeated roots, an uncertified factorization, a wrong zero-factor convention, or v2(D)=4 prevents invoking this matrix unchanged. One must retain the missing local analysis rather than apply the fixed-core table. This paper establishes no rank without a separate known-point/radical or pairing argument.

## 7. Custody, overlap and limits

The complete current Task directory was observed at Source81910f7f40769d36f7ff98d5898beb1729ee80d8 (491 entries). The exact existing fixed-core certificate Task is RS-P11-FIXED-233-119-CERTIFIED-2-DESCENT-RANK / TP2-FCBBFD9867F24A66940E, Source5bbdeca4f91cd8a20be9645da8db6cc0e543b149. This paper does not modify it. Two bounded GitHub queries (“Cassels pairing”, “local Kummer image”, top12) returned no indexed results; they are not proofs of global absence or historical novelty.

The general support/Kummer/Euclidean-core interfaces are accepted inherited work. The new deliverable here is an explicit complete parameter-local table, its valuation proofs, the sharp U2 dyadic failure branch and their finite linear consumer interface. It remains unreviewed paper. Original author/Driver/RA histories and the fixed-core independent reviewer’s scope remain unchanged.

