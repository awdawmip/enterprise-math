# Independent paper review: parameter-local Kummer images and sharp U2 obstruction

Reviewer EM-PUBLIC-7CDA51, same actual Researcher session MCP-9030ae3a22074e3dbc31679b7090f6b0 and RA-6665DBCD10BC1C3E4DED3C04. This is Root-directed nonauthor paper support, with all prior Public/CONTROL/T6/P11/parity history retained and shared ambient context NONBLIND. It is not a Native Driver review, Task claim, computation, acceptance vote or extension of the fixed-(233,119) certificate Task.

The complete new author input is P11_PARAMETRIC_LOCAL_IMAGE_AND_DYADIC_OBSTRUCTION_PAPER.md, 11894 bytes, SHA256 13e6d431795353340280c2f9b14c148e117139c85bbd797bf73336e891d453c6, Git blob 9cf9ff6372bfe1ce226f560ba5a637245484e029, authored by EM-DVR-F73673. It is a frozen local input awaiting its own Source publication. This review does not say that the new manuscript is already Source-published. The older fixed-core three PASS reports are not premises for its new valuation arguments.

Assessment: PAPER PASS for the stated complete local table, the specific U2 iff obstruction, and the stated conditional finite-matrix consumer. No mathematical repair was supplied to the author. The checks below explain completeness and the boundaries of that conclusion. All arithmetic reasoning was on paper; no enumeration, arithmetic program, factorization, symbolic matrix calculation or scientific checker was run.

## Full Kummer interface and completeness

I checked the monic squarefree cubic with roots (0,P²,Q²), for distinct positive coprime odd P,Q. The split algebra is Q³, the norm-square condition makes the third squareclass the product of the first two, and the ordinary-coordinate rule is the full Kummer map. At a zero coordinate the replacement is the product of the other root differences. In particular the exceptional triples reduce to (1,-1,-1), (1,D,D), (1,-D,-D); none divides by a zero factor. The point at infinity is the identity class.

The relevant primary statements are Stoll 2001, Lemma 4.1 and Proposition 4.2, with the zero-factor and split-torsion discussion of Lemma 4.3, the local-index statement of Lemma 4.4 and real-place Lemma 4.8. The actual primary PDF and text were fully consumed in the earlier review history, and the relevant statements were read again for this input. Their hypotheses are applied here to genus one and monic odd degree three, not an even-degree fake descent or a two-isogeny image. PDF SHA256 b4854a404601da748a687c64a3d72a36033590a4ba911b7021db53340c5aa9d1. Reuse of an inspected source theorem is distinct from reuse of a previous core's numerical verdict.

The author's elementary index argument is also sound. For a deep open torsion-free formal subgroup H, [H:2H] is 1 at odd p and 2 at p=2. The kernel of E/H -> 2E/2H is (E[2]+H)/H, of order four: 2x in 2H means 2x=2h for an h in H and hence x-h is 2-torsion. Taking indices gives [E:2E]=4[H:2H]. Thus the image has size four or eight respectively, without an assumption on reduction type or a simple zero in P,Q,D. The real index is two. Every proposed subgroup has that exact cardinality. Consequently a proved containment really does establish equality; exhibiting selected points would not have been sufficient.

## Odd primes, including multiplicities and negative valuations

At p not dividing 2PQD, the roots are distinct modulo p. A negative x valuation is even because the three factors have the same valuation and their product is a square. For integral x, at most one factor has positive valuation and that valuation is even. The exceptional factors are units. This gives the unit-pair subgroup; both it and the image have size four.

At odd p dividing D, p cannot divide P or Q. For negative valuation, each correction 1-P²/x and 1-Q²/x is in 1+pZp and hence a square; the equation then makes the class of x a square. For positive valuation, the product of the other factors is a square unit. For unit x congruent to P² modulo p, x itself is a square unit; for the remaining unit case the two other factors have a nonzero square product residue. These exhaust ordinary points. The exceptional first coordinates are squares as well. Therefore the first class is trivial and the vertical subgroup equality follows, for any positive exponent of p in D, and also when D is negative.

At p dividing P with p=1 mod4, -1 is square. For negative valuation the first argument again proves x, and then x-Q², square. For positive valuation x-Q² has square residue -Q². For unit x not reducing to Q² the product x(x-P²) is a square unit; for unit x reducing to Q² both these factors are square units separately. Thus the third class is trivial, equivalently the first two classes coincide. At the three exceptional points the third classes are -1, D, and -Q²D, each square at this p. The p dividing Q version interchanges the two colliding roots and gives trivial second class. These arguments do not assume P or Q squarefree.

At p dividing P with p=3 mod4, write h=vp(P). Negative valuation k is even. For k=0 the first two factors are units. If 0<k<2h, the product x(x-P²) is square whereas x-Q² has nonsquare unit class -1, so this branch has no point. If k>2h the other two factors each have class -1, so x is square and both relevant valuations are even. At k=2h, the curve equation forces vp(x-P²) even. The exceptional valuations are also even. This proves unramified first and second classes. For p dividing Q the same proof gives unramified first and third classes, which imply an unramified second class by the product rule. Thus the full unit-pair group, not a selected unit-character line, is correct.

No odd prime can fall into two of the bad-prime cases, because gcd(P,Q)=1. In particular the argument does not merge colliding-root cases under an unstated common divisor.

## Real place and the complete dyadic vertical image

Over the reals all three roots are nonnegative and distinct. A negative x makes the cubic negative, so the first class is positive for ordinary points and for the exceptional definitions. The second coordinate can have either sign, as also follows from T0. The real size-two index then gives exactly the stated two pairs, regardless of whether P>Q or P<Q.

For p=2 and 32|D, I checked the formerly delicate negative-valuation branch separately. If k=v2(x)<0, k is even. For k<=-4 both corrections are squares. If k=-2, both corrections are 5 modulo 8 and their product is 1 modulo 8, again square. The equation forces the first class square in both cases. For k>0, x-P² and x-Q² are odd with the same residue modulo 8; their product is square.

For odd x, residue 1 already gives a square. At residues 3 or 7 the two near-root factors each have valuation one; at residue 5 they each have valuation two. Dividing their difference D by 2 or 4, respectively, leaves a multiple of 8 under 32|D. Their odd parts therefore agree modulo 8 and have square product. Any of these three nonsquare x residues would contradict the curve equation. This proves first coordinate square in every ordinary branch. The exceptional first coordinates are squares. The containing vertical subgroup has size eight, exactly the local image size, so it is the complete dyadic image.

This proof does require the asserted v2(D)>=5 for the entire vertical image. It does not classify the full image at v2(D)=3 or 4.

## Sharp U2 necessity and sufficiency

For U2=(1,2,2), the actual covering equations are z0²-2zP²=P²t² and z0²-2zQ²=Q²t². A nonzero solution cannot have t=0: it would make 2 a square or make all coordinates zero. Set t=1. In either equation, the valuations of z0² and 2zP² have different parity; a negative minimum could not cancel against an odd right side. Hence the variables are integral, z0 is odd, and reduction modulo 8 makes zP,zQ even. Setting zP=2u,zQ=2v gives exactly D/8=v²-u². A difference of two integral squares cannot be 2 modulo 4. Since distinct odd P,Q always give 8|D, the excluded case is exactly v2(D)=4.

The converse is constructive and exhaustive. For n=D/8 odd, the stated u=(n-1)/2,v=(n+1)/2 are integral and give v²-u²=n. For 4|n, u=n/4-1,v=n/4+1 do the same. These cover every n not 2 modulo 4, including negative n. The unit P²+8u² is 1 modulo 8, so an actual 2-adic root w exists; putting z0=w,zP=2u,zQ=2v solves both equations. This is a genuine necessary-and-sufficient local statement for that class, not merely a modular obstruction or an assertion about global rational points.

## Consumer boundary

For primitive opposite-parity r>s>0, A=r²-s² is odd and B=2rs is even. Their coprimality gives odd coprime P=A+B and Q=|A-B|. Equality A=B would force an irrational ratio r/s, so Q is nonzero and P,Q are distinct. The identity D=4AB gives v2(D)=3+v2(e) for the even member e. Thus 4|e is exactly the branch where the whole displayed dyadic table is available; e=2 mod4 puts U2 in the proved failure branch.

Using signed squareclasses on the finite support of 2PQD, the six listed local conditions are precisely the complete images just verified. Outside that support the unit-pair image imposes no remaining condition. First coordinate square at 2 means both the valuation bit and all unit-square tests, rather than valuation alone. The odd conditions likewise retain unit characters where the subgroup requires them. Proposition 4.2 therefore identifies this kernel with the full 2-Selmer group. Its dimension still requires the actual finite matrix rank; this review computes no such parameter-dependent rank.

Noncoprime or even P,Q, repeated roots, uncertified prime support, a wrong exceptional convention, and applying the full vertical dyadic table when v2(D)=4 remain kill conditions. No constant Selmer dimension, rank across all parameters, positive-rank point, saturation, all-core result or Native acceptance follows from this report. The new (5,4) paper and the prime-support corollary each receive a separate assessment.
