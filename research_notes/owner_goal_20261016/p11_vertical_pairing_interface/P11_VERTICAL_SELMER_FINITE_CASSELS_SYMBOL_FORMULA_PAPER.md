# An explicit local-symbol formula on the vertical full-2-Selmer subspace

Status: FOURTH NEW AUTHOR PAPER / UNREVIEWED. EM-DVR-F73673. The three preceding frozen parameter/core papers are unchanged. This is not an accepted Tool, new Task or a modification of the fixed(233,119) certificate Task. No arithmetic program or enumeration was run.

## 1. Hypotheses, exact subspace and statement

Let P>Q>0 be coprime odd integers, D=P²−Q², with32|D. Use
E:y²=x(x−P²)(x−Q²)
and ordered roots (0,P²,Q²). Assume the complete local-image lemma in the separately frozen P11_PARAMETRIC_LOCAL_IMAGE_AND_DYADIC_OBSTRUCTION_PAPER.md, itself independently paper-checked but not yet a Native accepted Result.

Let T be the odd prime support of D. Define V as the signed rational squareclasses supported on {2}∪T, subject to
(b/p)=+1 for every odd p|PQ with p≡1 mod4.
Then b↦U_b=(1,b,b) identifies V exactly with the vertical subspace of the full2-Selmer group.

Indeed the complete local table forces absence of prime factors of PQ from a vertical second coordinate; at their1mod4 primes it additionally forces that coordinate to be square. At2, infinity and all primes of D there is no further restriction on that coordinate. The good-prime unit conditions are automatic. Thus this description is necessary and sufficient. If L is the matrix of those finite Legendre characters, dim V=|T|+2−rank(L). In particular L is empty in the previously frozen all-primes-of-PQ≡3mod4 corollary. This does not identify the entire Selmer group in the general case, where first-coordinate classes can also be nontrivial.

For a,b∈V choose any nonzero signed squarefree representatives. At p|PQ put
eta_p(a)=0 if a is square modulo p and1 otherwise,
and m_p=v_p(PQ), retaining its actual exponent. Let R=P−Q and S=P+Q. Exactly one of R,S is divisible by16: their gcd is2, their smaller2-adic valuation is1, and v2(RS)≥5.

The author-derived formula for the Cassels full2-descent pairing is
< U_a,U_b > =
(-1,b)_infinity
· C2(a,b)
· product_{odd p|R} (-1,b)_p
· product_{odd p|S} (-a,b)_p
· product_{p|PQ, p≡3mod4} (-1)^{m_p eta_p(a) eta_p(b)},
where
C2(a,b)=(-1,b)_2 if16|R,
C2(a,b)=(-a,b)_2 if16|S.

Every factor is an ordinary rational Hilbert symbol or a specified finite Legendre/valuation bit. No search for local covering points is part of this formula. Its proof below establishes the needed local point classes, covers all places and retains the prime multiplicities m_p. It makes no constant-rank or all-core assertion.

## 2. Covering and tangent normalization

For U_a use
z0²−a zP²=P²t²,   z0²−a zQ²=Q²t².
The third conic a(zQ²−zP²)=Dt² has the rational point
zP=(D/a−1)/2, zQ=(D/a+1)/2, t=1.
The other two conics have rational points (Q,0,1) and(P,0,1), yielding tangents
L2=Qt−z0, L3=z0−Pt, F=L2L3.
The full2-descent formula is
< U_a,U_b >=product_v(F(q_v),b)_v.
The unused tangent contributes against the first coordinate1. Smooth local perturbation may avoid its finite zero divisor and any zero of L2L3; the evaluated nonzero squareclasses are locally constant.

Source/model requirements are exactly those spelled out in the preceding rank-zero paper: FSS0710.2079v1 permits the long a2 model; the Shukla–Stoll2302.01640v1 short-model convention is reached by x=X+(P²+Q²)/3. Root differences and these covering equations are unchanged. The pairing is on full root-ordered Kummer classes and is compatible with Cassels–Tate; no two-isogeny representation is substituted.

## 3. Odd primes dividing R or S

At such a prime p, P,Q,a's unit part are nonzero units and P²≡Q² mod p. Replace a by its squareclass representative with v_p(a)=0 or1.

If a is square in Qp, choose t=0,z0=sqrt(a),zP=zQ=1. Then F=−a. This has class−1 in the R case and class−a in the S case, as required.

Suppose a is a nonsquare unit. The finite-field conic z²−a y²=P² has p+1 points, by the norm map from F_(p²)* onto F_p*. Exactly two have y=0. Choose one with y≠0, hence z≠±P. Modulo p the same pair (z,y) solves the Q equation. Fix t=1 and a lift of z; Hensel lifts zP and zQ independently from y because their derivatives2ay are units. Both tangents are units. If p|R their product has residue
(P−z)(z−P)=−(z−P)²,
so F has class−1. If p|S it has residue
(−P−z)(z−P)=P²−z²=−a y²,
so F has class−a. The finite-field norm count proves existence, not an unexecuted search claim.

Finally suppose v_p(a)=1. Since a is nonsquare, a local cover point cannot have t=0. It exists because U_a is Selmer. Normalize t=1. In z0²−a zP²=P², the valuations of the two terms on the left have different parity, so a negative minimum cannot cancel; z0 is an integral unit and zP integral. Likewise zQ integral, and z0≡±P mod p.

For p|R, change the sign of z0 so z0≡−P; then F has nonzero residue−4P² and squareclass−1. For p|S, choose z0≡P. The ratio
(z0−Q)/(z0+P)
is a unit1 mod p and therefore square. Away from zP=0 this gives
F=−(z0−Q)(z0−P) ~ −(z0+P)(z0−P)=−a zP² ~−a.
If necessary perturb off zP=0 and tangent zeros within the same residue branch. Smoothness over Qp follows from the distinct roots P²,Q²,0, so such a local neighborhood exists.

Thus all possible local squareclasses a are covered, and the R/S factors in the formula are proved.

## 4. The dyadic factor without guessing a Hilbert sign

The complete lemma gives the vertical local image at2, so a local cover point exists. If a is square in Q2, the t=0 point gives F=−a; this also has class−1 when16|R.

If a is nonsquare, t≠0 and normalize t=1. No integrality assumption on z0 is needed. Among z0−P and−z0−P, at least one has valuation≤1 because their sum is−2P. Likewise among z0+P and−z0+P at least one has valuation≤1.

If16|R, change the sign of z0 so v2(z0−P)≤1. Then
(z0−Q)/(z0−P)=1+R/(z0−P) ∈ 1+8Z2,
which is square. Consequently F=−(z0−Q)(z0−P) has class−1.

If16|S, change the sign of z0 so v2(z0+P)≤1. Then
(z0−Q)/(z0+P)=1−S/(z0+P) ∈1+8Z2,
which is square. Using the cover equation,
F ~−(z0+P)(z0−P)=−a zP² ~−a.
A smooth perturbation handles a vanishing zP or tangent while retaining the strict valuation bound and the square ratio. This proves the stated dyadic factor, including both possible orderings of the odd/even Euclidean legs. It does not transplant the old fixed-core chosen root or norm identity to every core.

## 5. Primes dividing PQ

All such p are odd and a,b are units there because they are supported on2D.

If p≡1 mod4, the definition of V makes a and b local squares. The local symbol is1.

If p≡3 mod4 and a is square, the t=0 point has F=−a, a unit; the unit-unit Hilbert symbol is1. If a is nonsquare, −a is square, so choose r²=−1/a and
(z0,zP,zQ,t)=(0,Pr,Qr,1).
Both cover equations hold and F=−PQ. With b a unit, the odd-prime Hilbert formula gives
(F,b)_p=(b/p)^{v_p(PQ)}
=(-1)^{m_p eta_p(a) eta_p(b)}.
This is why the exponent of P=7² in core(5,4), for example, must not be discarded merely because the prime support records only7.

## 6. Infinity and every remaining prime

At infinity, if a>0 choose the t=0 point and F=−a<0. If a<0 choose r²=−1/a>0 and the z0=0 point, giving F=−PQ<0. Hence the real factor is always(-1,b)_infinity.

For odd p outside2PQD, a and b are units and the local Selmer cover has a point. Scale it to primitive integral coordinates and avoid zero tangents. If p divides z0−Pt, then t is a unit (otherwise the cover equations would force every coordinate divisible by p), and z0+Pt is a unit. From
(z0−Pt)(z0+Pt)=a zP²
the valuation of z0−Pt is even. The same argument holds for Qt−z0. Thus v_p(F) is even and b is a unit, so (F,b)_p=1. This covers all remaining primes uniformly, with no numerical cutoff.

Every place has now been included. Multiplying the local results proves the formula.

## 7. Use, internal checks and explicit failure boundaries

The formula provides a finite bit matrix on V after exact factorizations and Legendre/Hilbert signs are certified. It is not a matrix of unproved positive-rank assertions. The known rational classes U_(-1) and U_D lie in the radical; alternation and those radical rows provide necessary sanity checks for a future implementation, not substitutes for the proof.

As a paper consistency check, the previously frozen core(5,4) has R=18,S=80. For a=2,b=3: only p3 contributes−1 from(-1,3)_3; p5 contributes(-2,3)_5=1; the dyadic factor is(-2,3)_2=1; p7 has even exponent2 and p31 sees2 square; the real factor is1. This reproduces the independently paper-checked product−1 without altering that earlier proof. No program was run.

The old fixed(233,119) vertical subspace is also within the general statement even though not all primes of PQ are3mod4: one must retain its Legendre constraints at17 and233. This observation does not replace the existing official certificate inputs or amend its scope.

Kill/unknown boundaries: gcd(P,Q)>1, even/repeated roots, v2(D)=4, a or b not in the exact vertical Selmer subspace, a missing theorem/model bridge, invalid perturbation/zero-factor handling, wrong factorization or dropped valuation multiplicity invalidates use of the formula. First-coordinate-nontrivial Selmer classes require a different pairing calculation. Saturated generators, odd-primary Sha, full Sha finiteness, infinite parameter families and all-core classification remain outside the claim.

Primary citations and exact hashes are inherited by explicit reference from the two earlier frozen papers: Stoll DOI10.4064/aa98-3-4 split full2-Selmer/local-index framework; FSS0710.2079v1 and Shukla–Stoll2302.01640v1 full2-descent pairing/model compatibility. The local R/S, dyadic-ratio and PQ-exponent arguments here are new author derivations requiring a new nonauthor review. No historical novelty or Native acceptance is claimed.

