# Independent P11 arithmetic proof and interface audit

Verifier: EM-P000-37E795; Task RS-P000-P11-ARITHMETIC-LINE-INDEPENDENT-AUDIT, publication TP2-4E0EE03CCD6B6126A1D7. Exact inputs and line locations are in SOURCE_INPUTS.json and CLAIM_MATRIX.json. This is an independent, source-exposed mathematical audit, not blind discovery, a line Driver review, or a formal-kernel certificate.

**Verdict: VERIFIED_COMPATIBLE at the derived-arithmetic interface stated below.** Neither a complete global classification nor native-X6 geometry follows. The existing Results remain immutable. This proof and the independent computation replace reliance on the authors' historical PASS statements for the audited obligations.

## A. Derivation of the common P11 reconstruction interface

Let the row sums be H=(h-d,h,h+d), d>0, and the column products T=(t-e,t,t+e), e>0. An outer cell (i,j) is an unordered pair of roots of z^2-H_i z+T_j. Its discriminant is H_i^2-4T_j, and its two roots are (H_i+delta_ij)/2 and (H_i-delta_ij)/2. We retain all eight cell positions and both roots, including negative, zero and composite roots. The middle cell is outside this eight-cell interface.

Write the top discriminants as a,b,c and the bottom ones as f,g,k, with a> b> c>0 and f> g> k>0 in the frozen ordered-core domain. Then a^2-b^2=b^2-c^2=4e and similarly for f,g,k. Put x=(a+c)/2, y=(a-c)/2, X=(f+k)/2, Y=(f-k)/2. It follows directly that x^2+y^2=b^2, X^2+Y^2=g^2 and xy=XY=2e, with x>y>0 and X>Y>0. Conversely these labeled equal-area triangles recover a=x+y, c=x-y, f=X+Y, k=X-Y and the six outer-row discriminants. Integer pairability requires the exact half-sum parity; rational triangle data alone do not assert integral P11 roots.

Let K=g^2-b^2. Subtracting the bottom/top middle-column discriminants gives K=4hd. If K is nonzero, h=K/(4d), and the top middle cell gives t=((h-d)^2-b^2)/4. Define A_cut=(a^2+f^2)/2 and C_cut=(c^2+k^2)/2. Direct expansion gives the two middle-row cut equations

    d^2+mu^2=A_cut,     d^2+nu^2=C_cut,

where mu^2=h^2-4(t-e), nu^2=h^2-4(t+e). Thus the off-diagonal reconstruction is both necessary and sufficient in this domain after actual roots are required to be integral (or rational roots are cleared and normalized). For an integral fixed core, the wording 4d|K requires integral d>0 as explicitly corrected in the off-diagonal RETURN; it is not a rational-divisibility assertion.

If K=0, d>0 forces h=0. Equal hypotenuse and equal product determine x+y and x-y, so the two ordered positive factors coincide. Remove the common integer scale from (x,y,b) to obtain the primitive Euclid legs A0=r^2-s^2, B0=2rs, C0=r^2+s^2, where r>s>0, gcd(r,s)=1, and r,s have opposite parity. Restore leg order by max/min. Put P=A0+B0 and Q=|A0-B0|. After dividing by the common scale, the exact cuts are D^2+U^2=P^2 and D^2+V^2=Q^2. This reproduces the fixed-locus-to-Euclidean-core passage without borrowing the authors' reconstruction code.

## B. Independent diagonal verification

For every permitted core P>Q>0, put a0=P+Q, b0=P-Q and R=PQ. From T0=U+V, U-V=(P^2-Q^2)/T0. T0 cannot vanish. With Y0=2T0D, substitution gives

    Y0^2=(a0^2-T0^2)(T0^2-b0^2).

The forward map xi=R(a0+T0)/(a0-T0), eta=a0 R Y0/(a0-T0)^2 has cubic factors R(a0+T0)/(a0-T0), a0 P(T0-b0)/(a0-T0), a0 Q(T0+b0)/(a0-T0). Their product equals eta^2. Solving, rather than taking square roots, yields

    T0=a0(xi-R)/(xi+R), Y0=4a0 R eta/(xi+R)^2,
    D=Y0/(2T0), U=(T0+(P^2-Q^2)/T0)/2,
    V=(T0-(P^2-Q^2)/T0)/2.

The independent symbolic checker reduces both quadrics, both inverse-forward compositions, and the quartic identity to zero modulo eta^2-xi(xi-P^2)(xi-Q^2). The manuscript's forward-inverse composition follows already by solving the first fractional-linear equation and the linear sum/difference equations; no unchosen root sign is suppressed.

The exceptional values xi=R and xi=-R have cubic values -R^2(P-Q)^2 and -R^2(P+Q)^2, respectively, so neither is rational/real on the curve. The four D=0 points map to O,(P^2,0),(Q^2,0),(0,0) in the T0 order a0,b0,-b0,-a0. There is no rational point with projective coordinate Z=0, because a sum of two rational squares zero forces both zero. Every other rational point has D nonzero and |D|<=Q<P. If |D|=Q, then U^2=P^2-Q^2=4A0B0. Coprimality would make both positive legs squares, contradicting the standard strong Fermat descent theorem a^4+b^4=c^2 has no positive integer solution. Hence |D|<Q and U,V are nonzero. The all-n strict domain is proved; it is not a finite acceptance filter.

There are also no zero roots on a strict diagonal fiber: the three column products before positive scaling are (D^2-P^2)/4, (D^2-C0^2)/4 and (D^2-Q^2)/4. Since Q<C0<P and |D|<Q, all three are strictly negative. Every recovered cell therefore has one positive and one negative nonzero root.

The two-division criterion on a split cubic excludes halves of (0,0) and (Q^2,0) by negative root differences, and excludes halves of (P^2,0) by the same nonsquare 4A0B0. Thus no rational point has order four. Applying the standard full-two-torsion part of Mazur's theorem leaves (2,2) or (2,6). The exact third-division polynomial is

    psi3(z)=3z^4-4(P^2+Q^2)z^3+6P^2Q^2 z^2-P^4Q^4.

Independent polynomial expansion verifies f'(z)^2-4f(z)(3z-P^2-Q^2)=-psi3(z). With nonzero ordinate, psi3=0 is exactly x(2H)=x(H); then 2H=-H, because 2H=H would imply H=O. Generalized Nagell-Lutz integrality and the integer-root divisor rule make the published z|P^4Q^4 plus nonzero-square test necessary and sufficient. This is a finite decision criterion per input core, not a proof that the (2,6) case never occurs.

For completeness, the descent support argument is also checked independently. At a prime outside 2PQ(P^2-Q^2), the three integral roots are distinct modulo that prime. If xi is integral there, at most one factor has positive valuation, so the square product forces that valuation even. If xi has negative valuation, all three factors share it, and three times it is even, so it too is even. The signed squarefree classes therefore have the stated finite support. Their covering equations reconstruct xi and eta when a rational point is actually supplied. The standard two-division theorem identifies the trivial class with divisibility by two. No Selmer/rank/local-global conclusion is supplied by this argument.

At P=233,Q=119 the seed (194089,69872040) satisfies the cubic exactly. Its nonzero ordinate is divisible by 5 whereas the cubic discriminant is 4 modulo 5. Generalized Nagell-Lutz therefore proves infinite order. As an independent safeguard, the exact short-model substitution X=9xi-3(P^2+Q^2), Y=27eta satisfies the stated integral short cubic; the discriminant changes by 3^12. Thus the ordinary short-model criterion has the same odd-prime obstruction. Counting the five residue classes gives 8 points over F5, excluding rational three-torsion by good-reduction injection. These are exact certificates with checked theorem hypotheses, not empirical rank computations.

Every positive seed multiple is distinct and avoids the torsion boundary, so it yields a signed strict cut triple. Absolute values have at most eight preimages. Take twice the lcm of its rational denominators, construct the sixteen integer roots using Section A with h=0, and divide those actual roots by their positive gcd m. Differences of root pairs give m|k0P and m|k0Q; since gcd(P,Q)=1, m|k0. Integer divided root sums and differences preserve all required parity, and products divide by m^2. The primitive sextuple recovers the positive normalized triple by its fixed-core scale. Therefore normalization cannot merge distinct normalized triples; at least ceil(N/8) distinct outputs occur among the first N multiples. Mordell finite generation then gives the stated per-core equivalence between infinitude and positive rank, without deciding all core ranks.

## C. Independent off-diagonal verification

The projective two-quadric cut carrier is nonsingular for A_cut>C_cut>0. In a dependent pair of gradients, either one coefficient vanishes and all coordinates vanish, or both are nonzero and mu=nu=0; then (A_cut-C_cut)w^2=0 forces d=w=0. Both contradict projectivity. The standard smooth (2,2) complete-intersection formula gives genus one. Rational solvability remains a separate condition.

The map (u,v)=(d^2,d mu nu) satisfies v^2=u(u-A_cut)(u-C_cut). Away from v=0, its rational image is exactly the class triple (1,-1,-1), which supplies the three rational square roots. The accepted RETURN's correction is essential: the full signed algebraic cover generically has four preimages; fixing d>0 leaves two choices for (mu,nu) at a fixed signed (u,v); the all-positive P11 display uses |v| and is unique. The uncorrected sentence in the first report is not independently accepted on the positive-d slice. Boundary points with v=0 are outside this affine inverse statement; the displayed family avoids them by infinite order.

On the core (21,20,29),(35,12,37), direct arithmetic gives equal area 210, K=528, A_cut=1945, C_cut=265. The seed (9,2112) lies on the curve. Its ordinate is divisible by 11, whereas the polynomial discriminant is 3 modulo 11, so the same integral Nagell-Lutz criterion gives infinite order. The independently computed double has u=1037419681/69696, agreeing with the frozen record.

For each root e_i of f, a nonvertical chord/tangent L with intersections R,S,T satisfies f(z)-L(z)^2=(z-u_R)(z-u_S)(z-u_T). Evaluating at e_i yields (u_R-e_i)(u_S-e_i)(u_T-e_i)=L(e_i)^2. Negation preserves u, hence the square class of u(R+S)-e_i is the product of the two input classes. A tangent gives trivial classes at 2R. Every nonzero multiple of the nontorsion seed avoids O and the two-torsion points, so the factors never vanish. Adding 2P0 successively to positive odd multiples never gives a vertical line: that would equate an odd multiple with -2P0, impossible for infinite order. Thus all positive odd multiples keep (1,-1,-1). In particular 0<u<265 and d,mu,nu are nonzero rational roots. This proves the all-n cuts independently of the sample computations.

Let D be the lcm of the sixteen rational root denominators and G their gcd after multiplication by D. All scaled row sums and column products are integers because they are recovered from actual integer root pairs; division of those roots by G gives a primitive datum. Here the upper-right discriminant is 1, so two scaled roots differ by D and G divides D. If G>1, the smaller integer D/G would clear every rational root, contrary to minimality. Therefore G=1. Equal primitive outputs give the same top hypotenuse 29D and hence the same D and d; equal d gives equal elliptic u and thus nP0=+/-mP0. Positive n,m and infinite order force n=m. The sign of h distinguishes the factor-swap partner. This proves injective primitive infinitude, not merely infinite common scaling.

The denominator refinement is exact. For d=p/q in lowest positive terms, r=q mu and s=q nu are integers. Modulo 4 excludes even q; modulo 8 excludes v2(p)=1. If p is odd, r,s are divisible by 4; if p is even, r,s are odd. The sixteen displayed numerators have common denominator 2pq and their gcd g divides 2pq because the top c=1 pair differs by 2pq. Odd primes dividing q divide no top numerator. At an odd prime dividing p, comparison with 132q^2 gives valuation min(v(p),v(132)); hence the odd part is gcd(p,33). For odd p, v2(g)=1. For v2(p)=2, all numerators are divisible by 8 and their difference bounds v2(g) by 3. For v2(p)>=3, a top numerator has valuation exactly 2. This proves the three cases g=2o,8o,4o and the published D formula, including the exceptional factor of two. It uses only the stated integer/coprimality/parity restrictions, so its artificial integer test domain must not be labeled a curve-point population.

For a zero product column, setting t=e,0,-e forces h-d=epsilon(a,b,c) and h+d=eta(f,g,k) respectively; subtraction/summation gives the displayed finite sign candidates, while the remaining cuts and parity must still be tested. On this fixed core, candidates are {3,44},{4,33},{11,12}. Bounds discard 44 and 33; exact nonsquares 249,1824,1801 discard 4,11,12. Only d=3 survives. Positive odd n>=3 cannot have d=3, since that would give nP0=+/-P0. This is a complete fixed-core statement, not a global zero-column classification. Euclid's separate labeled parameterizations give the stated equal-area equation; neither factor equality nor independence is substituted for it.

## D. Compatibility, quotients, and native typing

The shared output is the labeled P11 sum/product datum together with its sixteen recovered roots and reconstruction ledger. The branches are disjoint by h=0 versus h!=0. The K=0 specialization of the off-diagonal *equations* has A_cut=P^2, C_cut=Q^2 and reproduces the diagonal cuts. This observation does not extend the off-diagonal theorem across its explicit K!=0 hypothesis.

Even in that specialization, the elliptic coordinates must not be identified. The diagonal map is birational in (xi,eta), while the cut map uses u=D^2 and v=D U V. Explicitly

    D=2R eta/(xi^2-R^2),
    U=[P(xi^2+R^2)-2QR xi]/(xi^2-R^2),
    V=[Q(xi^2+R^2)-2PR xi]/(xi^2-R^2).

Thus u=4R^2 xi(xi-P^2)(xi-Q^2)/(xi^2-R^2)^2, and v=D U V. These formulas give the commuting bridge, checked symbolically against the same cubic. For the diagonal seed xi=194089 but u=11025: treating them as one coordinate would already be false. No author Result requires that identification. Likewise the diagonal bound is finite-to-one (not asserted injective in n), while the off-diagonal positive-odd sequence is injective. Integration must retain that distinction.

Changing the sign of a square discriminant only swaps the two roots within a declared unordered pair. It preserves the eight cell labels and all sum/product observers. It does not justify forgetting the signed elliptic ordinate before a future group operation. Primitive scaling preserves the projective scaling class, while exact unscaled roots require the retained scale. The full ledger keeps core/factor labels, coupling sign, signed point, multiplier, sign choices, denominators, root gcd and scale. The maps are inverse on their stated domains after these repair data are retained. Arbitrary group addition does not descend to bare unsigned primitive outputs: P and -P have the same u, but combining them with P gives O versus 2P. Therefore no stronger quotient is admitted.

This applies the existing T6 fiber-constancy/operation-descent criterion at the explicit reconstruction observer. T0 BRC provenance discipline is used only at this static typed boundary; no absent path-composition law, positive mass, or affine transport execution is claimed. The independent checker is a task-specific verification required by the audit contract, not a new general-purpose tool family or a capability-gap claim.

All Euclidean triangles, projective curves and elliptic groups remain external arithmetic carriers. They do not assert native 90-degree geometry, a native plane, a fractional native Cell move, a two-force primitive balance, or a reduction from six native spatial axes. P000's signed axes, native 120-degree relation, triadic balance and discrete-X6 basis are retained. Time is unnecessary for these static arithmetic identities and is not silently identified with a multiplier or curve parameter.

## E. Evidence boundary

The independent program uses Python Fraction arithmetic and SymPy 1.14.0 exact polynomials. It imports/executes no author checker. It verified ten symbolic identities, diagonal multiples 1..8, off-diagonal odd multiples 1..13, the nontorsion residue certificates, actual sixteen-root reconstruction/gcd, factor swap, all fixed-core zero-column candidates and the denominator formula on the actual curve points. A separate independent data comparator matches every published family row (three diagonal and six off-diagonal) and both required old witnesses. The extra sample points are regression only; Sections B-C supply the infinite arguments.

All 23 accepted manifest artifacts match SHA256 and Git blob hashes. The diagonal inner manifest's eleven non-self entries also match. Static checker coverage is recorded separately from independent execution. The authors' old temporary reproduction environment and external PDF byte-download history were not independently recreated. The missing ARITHMETIC.md/optional REFERENCE_APPLICABILITY.md and removed REPRODUCED.json are historical/availability limits, not used proof inputs: the actual audited derivations are fully in RETURN.md/FAMILY.md and reproduced in Sections A-D here. Their historical PASS assertions are not evidence for this verdict. Classical Euclid, strong Fermat descent, Nagell-Lutz, Mazur, Mordell, two-division and smooth-(2,2)-genus theorems remain explicit imported mathematics; their hypotheses and used conclusion strengths were checked, not formally re-proved in a kernel.

No counterexample or unresolved task-specific proof obligation was found at this scope. Global classifications, ranks/generators across cores, global zero-column arithmetic, stronger operation quotients, native bridges, Working Truth, Foundation and the parent Objective remain OPEN or ungranted.
