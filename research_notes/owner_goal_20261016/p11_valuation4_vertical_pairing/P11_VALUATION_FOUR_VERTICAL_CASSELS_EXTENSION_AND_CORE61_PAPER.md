# Extending the vertical Cassels formula across valuation four, with the core (6,1)

Status: UNREVIEWED NEW AUTHOR PAPER, ninth separate object. EM-DVR-F73673. The eighth local-image theorem is a separately reviewed dependency, not a verdict on this new pairing proof or its new fixed-core application. All preceding author and reviewer bodies remain unchanged. No scientific program, matrix consumer, factorization routine, parameter enumeration or point search ran. No new Task, registered Tool, Native Result or truth promotion is created; the fixed-(233,119) certificate Task and its actual budget are unchanged.

## 1. Exact remaining gap and vertical domain

Let P>Q>0 be coprime odd integers, D=P²−Q² and v2(D)≥4. Use the classical curve E:y²=x(x−P²)(x−Q²), ordered roots (0,P²,Q²), and U_a=(1,a,a) in full split Kummer coordinates. Set R=P−Q and S=P+Q. Exactly one of R,S has valuation one and the other has valuation at least three. Write T for the distinct odd prime support of D.

The earlier fourth/fifth papers proved a finite vertical pairing formula only when v2(D)≥5. Their exact odd-place, real, model and outside-support arguments do not require that stronger dyadic hypothesis. The eighth paper now supplies the complete local image at v2(D)=4. The remaining gap is its dyadic tangent evaluation, followed by an actual check that the global product still computes a full-descent pairing on the right domain.

Define V by signed squareclasses supported on T, adding the generator 2 only when v2(D)≥5, and impose (a/p)=+1 at every p|PQ with p≡1 mod4. Then a↦U_a is exactly the vertical subspace of Sel²(E/Q).

For v2(D)≥5 this is the fourth paper's domain. For valuation four, the eighth complete image permits a vertical class (1,a,a) precisely when a is an odd-unit class at 2. Thus its global 2-exponent is excluded. At primes of PQ the complete odd table excludes their valuation bits from a vertical coordinate and imposes the displayed characters at the 1 modulo 4 primes. Odd primes of D, infinity and all other primes give no further second-coordinate condition. These observations prove necessity and sufficiency, not just a containing support bound.

In a signed basis for this domain, dim V=|T|+1+epsilon−rank(L), where epsilon=1 for v2(D)≥5 and 0 for valuation four, and L is the actual finite matrix of those Legendre characters on that basis. No rank of L is computed here and V need not be the full Selmer group.

## 2. Statement: a uniform finite product on this vertical domain

For a,b∈V choose nonzero signed squarefree rational representatives. At p|PQ let eta_p(a) be its nonsquare-unit character bit and m_p=v_p(PQ), with the actual multiplicity retained. Let Sigma_+ contain the odd primes of S=P+Q, adding the place 2 exactly when 8 divides S.

The candidate extension is

<U_a,U_b> = product_(p in Sigma_+) (a,b)_p
             · product_(p|PQ, p≡3 mod4) (−1)^(m_p eta_p(a) eta_p(b)).

This is a restriction of the full 2-descent Cassels pairing, not a different two-isogeny pairing or an arbitrary extension to all rational squareclasses. For v2(D)≥5, the new threshold 8 selects exactly the same branch as the old threshold 16. The new mathematical content is valuation four, where the high branch has valuation exactly three and both a,b have odd 2-adic valuation parity zero.

At valuation four our constructed tangent value has class −5a in the high-sum branch and −5 in the high-difference branch. The factor 5 is real squareclass information. Its Hilbert pairing with every permitted odd-unit target b is one, so the local pairing sign agrees with the old-looking expression. It would be wrong to assert that the tangent values themselves lost the factor 5, or to allow the obstructed even target U2.

## 3. Model, cover, and nonzero tangent conventions

Reuse the fourth paper's exact covering and tangents:

z0²−a zP²=P²t²,   z0²−a zQ²=Q²t²,
F=(Qt−z0)(z0−Pt).

The full-descent theorem computes <U_a,U_b> as product_v(F(q_v),b)_v. The third conic a(zQ²−zP²)=Dt² has its rational point ((D/a−1)/2,(D/a+1)/2,1); its tangent contributes against the first target coordinate 1. That construction works at valuation four as a rational conic identity. The FSS long-model and Shukla–Stoll translated short-model bridges, root order, all zero-factor conventions and Cassels–Tate compatibility are exactly those already checked in the fourth paper.

Any unused tangent zero can be avoided in a sufficiently small smooth local neighborhood while retaining the nonzero F squareclass calculated below. The curve and its two-cover are smooth over Q2 because the three roots are distinct. A nonzero tangent divisor is a proper finite divisor, so it cannot contain that local neighborhood. This is the same justified local perturbation principle as in the fourth paper, not a claim that a zero may be inserted into a Hilbert symbol.

## 4. New dyadic construction at v2(D)=4

Write D=16d with d odd. The vertical-domain theorem makes a and b odd 2-adic units. Put n=d/a. Choose an odd unit c such that the following u and v are both nonzero:

u=(n/c−c)/2,   v=(n/c+c)/2.

Only the equations c²=n or c²=−n are excluded; infinitely many odd units remain. Both u,v are integral, of opposite parity, and v²−u²=n. If desired avoid the proper unused tangent divisor by a further arbitrarily small choice or perturbation; the following residue relations hold on the entire permitted unit branch.

Set t=1,zP=4u,zQ=4v and choose w=z0 satisfying
w²=P²+16a u²,   w≡P mod4.

The odd unit on the right is 1 modulo 8 and has a square root; one of the two signs satisfies the displayed modulo-four choice. Both cover equations hold because a·16(v²−u²)=16d=D. Nonzero u,v ensure w−P and w−Q are nonzero. The precise unit-square criterion, rather than an incorrect simple-root derivative condition at 2, supplies w.

### High sum: v2(S)=3 and v2(R)=1

Write R=2r0,S=8s0 with r0,s0 odd; hence P=r0+4s0 and d=r0s0. Define

h=(w+P)/2,   delta=w−P.

The sign choice makes h odd, and the cover equation gives exactly

delta=8a u²/h,   h=P+4a u²/h.

Let epsilon be the parity of u. Modulo 8 these identities give

h≡P+4epsilon≡r0+4(1+epsilon).

Consequently r0/h has unit squareclass 5^(1−epsilon). Also

Q−w=−2r0(1+delta/(2r0)),
1+delta/(2r0)=1+4a u²/(r0h)≡1+4epsilon mod8,

whose squareclass is 5^epsilon. Since u≠0, delta has squareclass 2a/h. Therefore the chosen nonzero tangent value has class

F=(Q−w)(w−P) ~ (−2r0)·5^epsilon·(2a/h)
                  ~ −a·5^(1−epsilon)·5^epsilon = −5a.

This includes both parities of u and both square/nonsquare possibilities for the odd unit a. No local root has been chosen by a numerical search.

### High difference: v2(R)=3 and v2(S)=1

For this algebraic calculation only, replace the constant Q by −Q. The squared root Q², the cover equations and D are unchanged, while the new sum has valuation three and the new difference valuation one. The previous calculation is valid for this negative auxiliary constant because it used only those identities and odd-unit congruences, not real positivity.

For the same nonzero cover coordinates write F_Q=(Q−w)(w−P) and F_(−Q)=(−Q−w)(w−P). Their ratio has squareclass

F_(−Q)/F_Q=(w+Q)/(w−Q)
          =(w+Q)²/(w²−Q²) ~ a.

The denominator equals a zQ² and is nonzero. The high-sum calculation gives F_(−Q)~−5a, hence F_Q~−5. This sign substitution is an identity for the fixed tangent evaluation; it does not change the curve's ordered roots or silently replace its published pairing model.

### The target domain makes the extra 5 invisible to the sign

For every odd 2-adic unit b, the ordinary dyadic Hilbert formula gives (5,b)_2=1: its exponent is ((5−1)/2)((b−1)/2), an even integer. Thus the constructed points give

(F,b)_2=(−a,b)_2 when 8|S,
(F,b)_2=(−1,b)_2 when 8|R.

The actual F classes remain −5a and −5 at these constructed points. For example a square a also has a t=0 cover point with F class −1; these different representatives agree on all allowed odd targets, not on every potential squareclass. This distinction is why the complete eighth-paper domain is essential.

## 5. All other places and reciprocity

The fourth paper's odd-place proofs apply unchanged. At odd p|R the local pairing is (−1,b)_p, at odd p|S it is (−a,b)_p, and at p|PQ, p≡3 mod4 it is the stated actual-multiplicity correction. At the 1 modulo 4 primes of PQ, membership in V makes a,b squares and the factor is one. The real factor is (−1,b)_infinity. The primitive-coordinate valuation proof covers every odd prime outside 2PQD, without a prime cutoff. Inspection of those arguments shows no use of 32|D: the old stronger assumption was used only for the replaced dyadic paragraph.

For valuation at least five, use the old dyadic proof. At valuation four use Section 4 above. Thus the raw all-place formula has the same factors with high-branch threshold 8. Factor (−1,b) from infinity, 2 and every odd prime of D. Since b is supported on 2D, all missing finite factors of this baseline are unit-unit and one. Rational Hilbert reciprocity cancels the full baseline. The remaining product is exactly the claimed Sigma_+ expression and the unchanged PQ correction.

This reuses the fifth paper's already explicit elementary reciprocity proof, not its old valuation hypothesis as if automatically enlarged. Bilinearity and symmetry hold for the finite expression; alternation on V comes from equality with the genuine full Selmer pairing. A rank bound still requires the dimension of the full Selmer group, not merely dim V.

## 6. One complete new application: primitive core (6,1)

Take r=6,s=1. Then A=35,B=12,C=37,
P=47,Q=23,R=24,S=70,
D=1680=2^4·3·5·7.

This is a new fixed symbolic input, not the fixed-(233,119) Task or an inferred consequence of its accepted H. These identities are direct hand arithmetic. The primes 23 and 47 are certified by divisibility checks by primes up to their square roots: 2,3 for 23 and 2,3,5 for 47. The smaller factors 3,5,7 have the immediate checks. Both primes of PQ are 7 modulo 8 and 3 modulo 4.

Use the first/eighth complete local table directly. In signed S-unit first coordinates, the odd-D valuation bits are killed by the square condition at 3,5,7; the PQ bits are killed by the unit-pair condition at 23,47; the 2 bit is killed by the new complete dyadic image; and infinity kills the sign. Thus the first global coordinate is 1. For the second coordinate, the PQ bits and the 2 bit are killed, and every remaining class is allowed. Consequently the full Selmer group is exactly

W={U_b: b∈<−1,3,5,7>},   dim W=4.

This is a fresh full-image deduction for valuation four, not a verbatim use of the old corollary which required 32|D. Every outside prime is covered by the same complete good-prime argument and Stoll's all-place criterion.

The rational two-torsion classes U_(−1) and U_D=U_105 are independent. Modulo them the remaining two directions can be represented by U3,U5: together these four classes span W because U7=U105 U3 U5, and the signed support basis proves independence.

Evaluate <U3,U5> by the now proved raw formula. At infinity the sign is positive. At 2, the high-difference branch gives (−1,5)_2=1. At 3|R the two entries −1,5 are units, giving one. At 5|S the symbol is (−3,5)_5=(−3/5)=−1, since −3≡2 is a nonsquare modulo 5. At 7|S both −3,5 are units, giving one. At 23 and 47, the unit 3 is a square because these primes are −1 modulo 12; thus eta_p(3)=0 and both PQ corrections are one, with their actual multiplicities retained. Every other place contributes one uniformly. Hence

<U3,U5>=−1.

The full alternating form has rank at least two. Its radical contains the two-dimensional rational torsion image, so its rank is exactly two and its radical is precisely that subspace. The entire rational Kummer image has dimension rank(E(Q))+2 and lies in this radical. Therefore rank(E(Q))=0, and the exact Kummer sequence gives dim Sha(E/Q)[2]=2.

The induced pairing on Sha[2] is nondegenerate. If an order-four Sha class xi existed, the nonzero class 2xi would pair trivially with every order-two class by Cassels–Tate bilinearity, contradicting that nondegeneracy. Any higher 2-power order would yield an order-four element. Thus, at this paper's dependency strength,

rank E_(47,23)(Q)=0,   Sha(E_(47,23)/Q)[2^infinity]≅(Z/2)^2.

No finiteness assertion about the odd-primary part or all of Sha is made. Odd rational torsion is not classified, no generator is claimed saturated, and no conclusion about the rank of core (9,8) is imported. This application is included in the single new bounded paper assessment; it is not an additional independent review vote or a new Task authorization.

## 7. Exact dependencies, reuse, and stopping conditions

The complete odd local theorem is Source270c9c6470db2cb14885f82d1021754f2bf19b23 under research_notes/owner_goal_20261016/p11_parametric_local_images/, first paper 11894B SHA25613e6d431795353340280c2f9b14c148e117139c85bbd797bf73336e891d453c6. The fourth9927B SHA256721e23197a05e469040d1b865e43d7a7a6bf2520c61f6466a812a4e1c8a4ea37 and fifth3669B SHA256086bbbae300ee2af867d037debdab991639dd2f224139a0d67eed0febdde7c75 are exact Sourcec4ae668c583a5abe797886e257c210c9e94cae09 under research_notes/owner_goal_20261016/p11_vertical_pairing_interface/.

The eighth9596B full-image paper has SHA2567bef7c3940ba9b2aeb63d1663bf0976c67bca1d4032e150e5ae042d949ba9934. Its separate nonauthor PAPER_PASS11435B SHA2568fa25c92cb66f744beff5b532c052e6246c664a9bdcbc5061d167d4c158f7647 is real but its author Source is pending at this freeze; no Source is invented for it. That PASS reviews no new dyadic tangent, reciprocity extension or core-(6,1) calculation here. Classical primaries are the exact already inspected Stoll2001 DOI10.4064/aa98-3-4, FSS0710.2079v1 and Shukla–Stoll2302.01640v1 editions/model bridges in those dependency papers, plus the explicitly declared standard quadratic/Hilbert supplementary formulas.

This extends an existing derived arithmetic interface at an exact recorded domain gap. It creates no new general-purpose helper, shared Tool registration or novelty claim and does not repeat old seeds, F5, multiples or any of the five closed P11 Tasks. The old fixed certificate's per-place witnesses, input digests, lawful author identity, resource clock and invocation gates are untouched. External classical arithmetic retains its type under Heartbeat X6, without native-plane, WT or Foundation promotion.

Failure boundaries: v2(D)<4, noncoprime/even/repeated roots outside the hypotheses, the wrong root or tangent order, an uncertified support/multiplicity, a or b outside the exact vertical space, a false smooth-perturbation or primary bridge, or using an even target at valuation four prevents the corresponding conclusion. First-coordinate-nontrivial Selmer pairings still need a different calculation; a zero first form still does not supply rank. No infinite family, all-core classification, odd Sha, whole-Sha finiteness or current Task completion is claimed. This ninth paper and its new fixed application require their own genuine nonauthor review.
