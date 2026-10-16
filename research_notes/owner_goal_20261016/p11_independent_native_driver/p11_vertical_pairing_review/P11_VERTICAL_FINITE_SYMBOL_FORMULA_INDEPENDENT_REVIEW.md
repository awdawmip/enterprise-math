# Independent paper review: finite vertical Selmer Cassels formula

Reviewer: EM-DVR-BFF6DC, own session MCP-47562f9f432d4978a7bea0dd60ecc4aa / DA-144D0C4639CACEEE75DC. Root delegated this new bounded nonauthor paper assessment. I did not construct or repair this formula, any preceding parameter paper, or the fixed-(233,119) certificate/code/plan. I already knew the fixed-core claims and read the new author's proposed formula before judging, so this is NONBLIND shared control context. My earlier independent P11 preparation and two independent Parity paper reviews are disclosed; none substitutes for this assessment.

Exact target: EM-DVR-F73673's `P11_VERTICAL_SELMER_FINITE_CASSELS_SYMBOL_FORMULA_PAPER.md`, 9927 bytes, SHA-256 `721e23197a05e469040d1b865e43d7a7a6bf2520c61f6466a812a4e1c8a4ea37`, blob `98fecb8cf7168230a905b302e201b6b820391781`. I independently verified it against its separate fourth-object freeze and verified the three preceding author inputs plus their three separate 7CDA51 reports, seven complete files in all. These are frozen local paper inputs awaiting actual Source binding, not newly Source-published or Native-accepted results.

**Assessment: PAPER PASS for the complete finite formula on the specified vertical full-2-Selmer subspace. No mathematical must-fix found.** The proof covers all local squareclass branches and every place, retains actual valuation multiplicities at primes of PQ, and supplies a finite Hilbert/Legendre expression without a local-point search. It proves no general Selmer matrix rank or unexamined curve rank. This is an independent paper report, not a Native scientific vote, Result, Task satisfaction, Tool acceptance or authorization to alter the fixed certificate Task.

## Dependencies and theorem strength

I read in full the frozen 11894-byte parameter-local lemma (SHA 13e6d431...), 10886-byte core-(5,4) paper (SHA 4a27760e...) and 3810-byte prime-support corollary (SHA ba35da92...), followed by their separate 9944/10263/5169-byte nonauthor reports. Each length/SHA/blob matches the exact handoff. The old reports cover those exact objects; their PASS verdicts are not transferred to this fourth paper.

I independently followed the local-table arguments relevant here. Stoll's full split Kummer map, exceptional zero-factor convention and local indices identify the image sizes as four at odd primes, eight at two and two over R. Necessary subgroup containments therefore prove complete images. The parameter lemma retains negative valuations, arbitrary multiplicities in P,Q,D, the distinct root-collision cases, and the dyadic hypothesis v2(D)>=5. Its complete table and Stoll's all-place characterization justify the vertical Selmer description used below. The separate U2 obstruction at v2(D)=4 is retained and not generalized into a whole-image classification.

The exact Stoll 2001 source is the previously independently connector-bound V2 capsule member, PDF SHA b4854a40... and complete text SHA 64b80d38.... I read its relevant full theorem pages. I also consumed the actual preserved FSS 0710.2079v1 and Shukla–Stoll 2302.01640v1 sources, with PDF SHA 70c46caa... and f84fee9a..., in my earlier preparation and applied the same model checks here. FSS permits the long a2 model. The declared characteristic-zero translation x=X+(P²+Q²)/3 reaches the latter's short model and preserves all root differences and covering variables. Full splitting makes the orbit factors the three declared rational root coordinates. This is full multiplication-by-two descent, not a two-isogeny formula.

## 1. Exact vertical space and normalized cover

For P>Q>0 coprime odd, D=P²-Q² and 32|D, the odd supports of PQ and D are disjoint. A vertical class is (1,b,b). At primes of D and at two the full vertical local image imposes no restriction on b. Infinity allows either second sign. At p|PQ with p=3 mod4, only the valuation bits must be even, which excludes these primes from b's squarefree support. At p|PQ with p=1 mod4, the diagonal or trivial-second-coordinate image forces b to be locally square; because b is a unit there, this is precisely the stated Legendre condition. Every outside prime automatically sees unit classes.

These conditions are sufficient as well as necessary. Thus V is exactly the signed support on {2} union the odd prime support T of D, cut out by the stated finite character matrix L, and dim V=|T|+2-rank(L). This is the vertical subspace only; nontrivial first-coordinate Selmer classes may remain in the general case. The all-PQ-primes=3mod4 corollary is its correctly identified special branch.

For U_a=(1,a,a), the covering equations and their third conic have the correct root order. The third conic's rational point satisfies zQ²-zP²=D/a exactly. The points on the other two conics give tangents Qt-z0 and z0-Pt with the correct indices. Paired against (1,b,b), their combined factor is F=(Qt-z0)(z0-Pt) against b. Fixed rational tangent rescalings disappear by global Hilbert reciprocity, and homogeneous point scaling multiplies F by a square. All a,b are nonzero signed squarefree representatives, so the local unit and valuation cases below are well defined.

## 2. Odd primes of R=P-Q and S=P+Q

No odd prime divides both R and S, since their gcd is two. At each such prime P,Q are units and the local a class is one of: square, nonsquare unit, or ramified valuation one. The proof treats all three, not merely U2.

If a is square, the homogeneous t=0 point has F=-a. This has class -1 in the R case and gives the required -a class in the S case.

For a nonsquare unit, the finite-field norm conic z²-a y²=P² has p+1 points, with exactly two at y=0. A remaining point has y nonzero and z not equal to either P or -P. Fixing a lift of z, Hensel lifts both square-root coordinates independently because their derivatives 2ay are units. Both tangents remain units. If p|R, their product is -(z-P)² modulo p and has class -1. If p|S, it is P²-z²=-a y² modulo p and has class -a. This argument proves existence and does not rely on an unperformed search.

For v_p(a)=1, t=0 is impossible for a nonzero covering point. Normalize t=1. The valuations of z0² and a zP² have opposite parity, so a negative minimum cannot cancel to the unit P². Both coordinates are integral and z0 is a unit; the Q equation likewise makes zQ integral. The residue is z0=+/-P. At p|R, choose the minus branch: F=-4P² modulo p, so its class is -1. At p|S, choose the plus branch: (z0-Q)/(z0+P) is a unit congruent to one and hence square, giving F equivalent to -(z0+P)(z0-P)=-a zP², and therefore class -a away from zero. No exponent of D is silently restricted.

Consequently the odd R product is exactly product(-1,b)_p and the odd S product exactly product(-a,b)_p.

## 3. The dyadic split, zero tangents and infinity

Since v2(RS)>=5 and gcd(R,S)=2, the smaller valuation is one and the larger at least four. Exactly one of R,S is divisible by sixteen. This exhausts the two dyadic cases.

If a is a local square, the t=0 point gives F=-a. For nonsquare a, the Selmer condition supplies a local point and t cannot be zero. After t=1, no integrality assumption on z0 is needed. Of z0-P and -z0-P at least one has valuation at most one, since their sum is -2P; the analogous statement holds for z0+P and -z0+P.

When 16|R, choose the first bound. The quotient (z0-Q)/(z0-P)=1+R/(z0-P) belongs to 1+8Z2, so is square and F has class -1. When 16|S, choose the second bound. Then (z0-Q)/(z0+P)=1-S/(z0+P) is square, and the covering equation makes F have class -a. These are exactly the two proposed C2 factors.

The possible vanishing zP or tangent does not invalidate these computations: the split 2-cover is smooth over the local characteristic-zero field, and its nonzero tangent sections have finite zero divisors. A local analytic neighborhood contains points away from those divisors. The selected finite valuation bound is open and the nonzero squareclasses are locally constant, so the needed perturbation preserves the proof. The same argument removes the unused first-tangent zero. No Hilbert symbol is evaluated at zero.

Over R, positive a gives the t=0 point with F=-a<0. Negative a gives the stated z0=0 point, using a real square root of -1/a, with F=-PQ<0. Thus the real factor is always (-1,b)_infinity, with no dropped sign coordinate.

## 4. Primes of PQ and actual valuation multiplicities

At each odd p|PQ, a and b are units. For p=1 mod4 their defining V conditions make both local squares, and the symbol is one.

For p=3 mod4 and square a, the t=0 point has unit F=-a, so the odd unit-unit symbol is one. For nonsquare a, -a is square; Hensel's unit-square criterion supplies r²=-1/a. The point (0,Pr,Qr,1) satisfies both equations and gives F=-PQ. Since b is a unit,
(F,b)_p=(b/p)^(v_p(PQ))
       =(-1)^(m_p eta_p(a) eta_p(b)).
This confirms both the sign and the actual exponent m_p, including prime powers in P or Q. Replacing m_p by one merely because support records p would be incorrect. The formula does not make that replacement.

## 5. All other places and finite nature

At every odd p outside 2PQD, a,b,P,Q are units and the local Selmer cover has a point. Choose a nonzero-tangent point and primitive integral projective coordinates. If z0-Pt is divisible by p, t must be a unit, since otherwise the two equations force every coordinate divisible by p. Its conjugate factor z0+Pt is then a unit. The product identity with a zP² forces even tangent valuation. The Q identity does the same for the other tangent. Thus v_p(F) is even, while b is a unit, and the Hilbert symbol is one. This covers every remaining prime uniformly, including arbitrary prime divisors of an evaluated tangent.

Multiplying the real factor, the appropriate C2 factor, both odd R/S products and the PQ exponent bits gives precisely the paper's stated formula. The only prime sets required are finite supports of D and PQ; rational Hilbert symbols, residue characters and integer exponent parities are exact finite data. Local cover-point existence used in the proof is supplied by the verified full Selmer table and is not a search step in the formula's consumer.

The core-(5,4) check agrees with its earlier independent pairing calculation, while retaining the square factor P=7². The fixed-(233,119) branch must retain its conditions at the 1mod4 primes 17 and 233. I found no defect here affecting that fixed paper proof, and this general formula neither replaces its frozen inputs nor supplies its still-missing executed certificate.

## Boundaries and resource record

U_(-1) and U_D are rational Kummer classes and therefore radical rows; they need not be two independent classes for every parameter. Alternation and radical checks are necessary future implementation checks, not proof substitutes. The formula covers only the specified vertical subspace. It proves no dimension of the full general Selmer group, actual matrix rank for an unexamined input, constant curve rank, saturation, odd-primary Sha, full Sha finiteness, parameter-family infinitude or all-core classification.

Noncoprime/even P,Q, repeated roots, an uncertified factorization, v2(D)=4, classes outside V, wrong root/tangent order or missing model theorem invalidate its use. Full signed/core/P11 reconstruction provenance remains necessary outside this descent observer. All elliptic and local-field objects are external static arithmetic within Heartbeat X6, not native spatial models or new axes.

Zero scientific numerical/symbolic program runs, coefficient generation, factorization/point searches, enumeration, certificate/code construction, fixture replays, Native scientific votes or Source mutations occurred. Only read-only custody parsing and cryptographic hashes executed. No author repair was supplied. The fixed certificate Task has no Result available to this reviewer and remains outside this report; its eventual decisive review still requires actual authorized code/input/admission/run/output evidence. Parent Objective remains OPEN.

Driver-ID: EM-DVR-BFF6DC / CONTROL_PLANE
Global-Knowledge-Sync: main@5e844264 / GLOBAL_KNOWLEDGE_V1

