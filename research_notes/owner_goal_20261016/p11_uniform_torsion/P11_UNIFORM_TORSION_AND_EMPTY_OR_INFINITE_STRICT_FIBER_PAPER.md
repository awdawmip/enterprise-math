# Uniform torsion and an empty-or-infinite strict P11 fiber

Status at author freeze: UNREVIEWED PAPER CANDIDATE. No program, parameter search, point enumeration or certificate consumer was run. This new object refines a precise remaining torsion alternative in the accepted primitive diagonal-fiber return. It is not a new general isogeny or Mazur theorem, a claim of historical novelty, a registered Tool, a Task/RR/DR, or a reopening of any of the five accepted Tasks.

Author EM-DVR-F73673, canonical /root/public129_line_reviewer, own actual Driver session MCP-10b3bf1d95f645ce8c0e419e458a2e49 / DA-7CBB43F6EB54D841994D. Shared CONTROL, prior proof/planning and directed NONBLIND exposure remain disclosed; a genuine different nonauthor must independently review this new proof. No prior PASS automatically covers it. All curve and group objects are external classical arithmetic under the unchanged native Heartbeat affine Z6/six discrete Cell basis, without a native plane. No Working Truth, Foundation, or parent closure is asserted.

## 1. Exact old scope and the unclosed alternative

The accepted primitive P11 diagonal curve is

    E_{P,Q}: y^2=x(x-P^2)(x-Q^2),   P>Q>0,

where A,B are positive coprime Euclidean legs, A^2+B^2=C^2, P=A+B and Q=|A-B|. Thus D=P^2-Q^2=4AB is positive. The accepted RETURN, Section 3, proves no rational point of order four by the two-division criterion and the accepted Fermat fourth-power boundary. Its use here is an exact inherited theorem, not a repeated proof of Fermat or a new computation.

The same accepted return and its final integration retain the alternatives C2 x C2 or C2 x C6, with an exact finite third-division-polynomial test for each core. They explicitly do not uniformly eliminate rational three-torsion. They consequently preserve a possible rank-zero fiber with isolated strict points from three/six-torsion. These are conservative open alternatives, not assertions that such a primitive core exists.

This paper removes that remaining alternative using a classical two-isogeny and the same full-two-torsion Mazur list. It then composes with the accepted exact rational-point/strict-fiber correspondence. It does not classify the still-unknown ranks across all cores.

## 2. A classical auxiliary isogeny rules out odd torsion

The first assertion has the larger elementary input class P,Q in Q, P>Q>0; no Pythagorean relation is needed. Put

    a=-(P^2+Q^2), b=P^2 Q^2, D=P^2-Q^2,
    E:  y^2=x(x^2+a*x+b),
    E': Y^2=X(X^2-2a*X+(a^2-4b))
          =X(X+(P+Q)^2)(X+(P-Q)^2).

Both curves are nonsingular: P,Q,D are nonzero, as are P+Q,P-Q and their squared difference 4PQ. On x nonzero set

    phi(x,y)=(X,Y)=(x+a+b/x, y*(1-b/x^2)).

This is the standard degree-two isogeny with kernel {O,(0,0)}. The following checks fix the exact convention rather than merely citing an unspecified isogenous curve. We have X-a=x+b/x and therefore

    X^2-2a*X+(a^2-4b)=(x-b/x)^2.

Multiplying by X and using y^2=x(x^2+a*x+b) verifies the target cubic identically. As a rational map between smooth projective curves it extends across the missing points; O maps to O, and the orders of the poles of X,Y at (0,0) show that it too maps to O. Generically x satisfies x^2+(a-X)*x+b=0, with y recovered from Y/(1-b/x^2), so the map has degree two. The exceptional zero of that last denominator is only a generic degree argument, not a discarded projective point. A nonconstant morphism of elliptic curves carrying origin to origin is a group isogeny; in characteristic zero this one has the stated two-element kernel. These are the classical isogeny facts used here, in the same rational-two-torsion setting as Fisher's higher-descent Section 5.

The auxiliary curve has full rational two-torsion. More strongly the rational point

    R=(D,2P*D) in E'(Q)

has exact order four. Indeed D+(P+Q)^2=2P(P+Q) and D+(P-Q)^2=2P(P-Q), so the cubic at X=D is (2PD)^2. Its ordinate is nonzero. For the model with a2=-2a=2(P^2+Q^2), a4=D^2, the tangent slope at R is

    (3D^2+2a2*D+D^2)/(4PD)=(2D+a2)/(2P)=2P.

The exact duplication formula gives X(2R)=(2P)^2-a2-2D=0 and Y(2R)=-2PD+(2P)D=0. Thus 2R=(0,0), a nonzero two-torsion point. Either other rational two-torsion point lies outside <R>, whose only nonzero two-torsion point is (0,0). Hence E'(Q) contains C2 x C4.

By Mazur's full-two-torsion list, E'(Q)_tors must be C2 x C4 or C2 x C8: the possibilities C2 x C2 and C2 x C6 have no point of order four. In particular E'(Q) has no nonzero odd-order torsion. The restriction of phi to any odd-order torsion subgroup is injective, since its kernel has order two. Therefore E(Q) likewise has no nonzero odd-order torsion.

The argument does not state that the target E has a rational order-four point. R lives on E', and the two models are not identified. It also does not claim the auxiliary torsion alternative C2 x C8 is realized, or rule it out here. The existence of R is a classical symbolic torsion construction, not a new target-curve point search or an assertion of positive rank.

**Lemma.** For every rational P>Q>0, E_{P,Q}(Q) has no nonzero odd-order torsion.

The larger rational input class is explicit. Removing positivity would require restating the root-order and degeneracy conditions, not automatically importing P11 strictness. Over number fields other than Q, the rational Mazur list cannot be substituted; in particular the same exclusion is not asserted over quadratic fields.

There is also an input-typing warning for the twelfth abstract Selmer-four interface. On E', exactly (0,0) among the three nonzero rational two-torsion points can be halved: its two other root differences are the squares (P+Q)^2 and (P-Q)^2, whereas either negative-root point has a negative difference from zero. The two-division criterion therefore gives dim delta_2(E'[2](Q))=1. One must not transfer the primitive E's value k=2 to this auxiliary E'. The generic nu/rho/k formula may use k=1 there only after its other full Selmer/pairing inputs are actually supplied; they are not calculated by this remark.

## 3. Exact torsion on every primitive P11 core

Return now to the primitive Euclidean input in Section 1. The accepted no-order-four theorem excludes every rational torsion point of order divisible by four, by taking an appropriate multiple. The new lemma excludes every nonzero odd torsion point. Together these facts show that all rational torsion is killed by two. Since the three distinct rational roots already provide exactly four two-torsion points,

    E_{P,Q}(Q)_tors = E_{P,Q}[2](Q) = C2 x C2.

This is a uniform elimination of the old C2 x C6 alternative, obtained by composition with an auxiliary classical isogeny. No third-division-polynomial enumeration or finite-field count across cores is needed. The previously accepted finite per-core test remains mathematically valid as a test; the new theorem shows that it never returns the three-torsion branch on this primitive family. Its old immutable text and acceptance history are preserved, rather than silently rewritten.

The larger input lemma alone does not eliminate rational order four on every curve with arbitrary P,Q: its proof only removes odd torsion. The primitive no-four theorem and its exact hypotheses remain essential for the conclusion C2 x C2. Likewise no conclusion about saturation or generators of the free part is supplied.

## 4. Empty or infinite: the strict-fiber consequence

Let F_strict(r,s) denote the accepted strict primitive diagonal P11 outputs at a fixed primitive Euclidean core, retaining the signed elliptic state, exact denominator scale, parity and the true outer-root gcd before any displayed sign readout. The accepted diagonal return proves the exact correspondence between rational E-points outside E[2] and nonboundary signed rational fiber points, and its strictness/normalization proof gives the following properties:

* No point of E[2] produces a strict fiber point.
* Every rational point outside E[2] produces a strict point after the declared sign readout and the exact primitive reconstruction.
* The readout has finite fibers; after primitive normalization the retained core/scale data prevent an infinite signed elliptic family from collapsing to finitely many outputs.

These are inherited results with their original reconstruction obligations. A bare squareclass, six-coordinate gcd, unsigned point or scale orbit cannot replace the retained exact data. No group law is asserted on the displayed primitive outputs.

By Mordell--Weil and Section 3, rank zero gives E(Q)=E[2](Q), and thus F_strict is empty. Conversely a single strict point gives a rational point outside E[2], which is now necessarily of infinite order. Its nonzero multiples are distinct and avoid E[2]; the accepted finite-fiber/primitive-normalization argument supplies infinitely many strict primitive outputs at that core. Therefore

    F_strict is nonempty  iff  F_strict is infinite
                          iff rank E_{P,Q}(Q)>0,
    F_strict is empty     iff rank E_{P,Q}(Q)=0.

In particular no primitive core has a finite nonempty strict fiber. This removes the old isolated three/six-torsion caveat; it does not provide an algorithm deciding which side any unknown core occupies. The old witness/multiples computation and census are not rerun or recounted as new research.

For example, composition with the independently established rank-zero core (5,4) or (6,1) papers gives empty strict fibers there, without an enumeration. Composition with the already accepted positive-rank core (11,8) still gives the previously known infinitude, not another discovery. At core (9,8), rank and the higher mixed bit are still UNKNOWN, so this paper only states the exact empty-or-infinite alternative. It does not choose its branch. None of these statements restores a budget or a scientific invocation on the stopped fixed-(233,119) certificate Task.

## 5. Exact sources, deduplication and method reuse

The accepted original return is immutable Source3fca728daf92abc5a4cad36102f5ec58c82aba0f, path research_artifacts/mcp/RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC/MCP-b4bf84ccfffc4affacc0f551cb1fa0ad/e486dcbc06d80c035317/RETURN.md, 13858 bytes, SHA256 c4bc0846af97b5f15eca90af7122ec44c2227a9a3152360cf3aa864cb2a3ed24. Sections 2--3 supply the strict correspondence and no-four boundary; Sections 5--6 supply finite-fiber normalization and the rank criterion with the retained torsion caveat. The old true Driver review at the same Source, driver_reviews/mcp/MCP-1e926295d6f7404d94ea3a90dda4fbfa/80b8a97d25d6342c8a3e/P11_DRIVER_REVIEW.md, 9924 bytes, SHA256 3c82b3ca977eb3abf3870c5f9114aa5350e6c7d2b7c6e080be94c32a1f58586a, and its terminal ACCEPTED DR-2F805343ED6728A5CD35 are exact prior inputs. The accepted final integration RETURN at the same Source, 27518 bytes, SHA256 fa88d26d766d4c10d09dc56b30b3653202a63faedcb0bf5d4e6b34144765dcd0, Section 4 explicitly retains the unresolved uniform three-torsion alternative.

Bekker--Zarhin, arXiv:1702.02255v2, actual versioned PDF downloaded 2026-10-16, 368067 bytes, SHA256 7e9674695454557d58233417151459398bc061b474df57e369eed8f444dff01a, matches the old accepted reference bytes exactly. I personally read its actual PDF pages 1--2 and 7. Theorem 2.1 states the split-cubic two-division criterion; Theorem 4.2 gives the precise rational noncyclic torsion list; Section 5 on the same page explicitly constructs C2 x C4 on the split negative-square-root family. The argument above uses these exact rational hypotheses. Mazur's original general classification is a declared classical input, not newly proved in this paper or claimed independently read in full.

Fisher, Higher descents on an elliptic curve with a rational 2-torsion point, author manuscript dated 10 September 2015, actual author PDF https://www.dpmms.cam.ac.uk/~taf1000/papers/higherdesc.pdf, 411230 bytes, SHA256 784c3ccf22bfe312f25237603ea8deb35565aac1018c9bb96ed1f9f4e4f2a129. Its actual PDF pages 1--13 were fully read in the input/reuse intake that led to this lemma. Section 5 treats E:y^2=x(x^2+a*x+b), its rational-kernel two-isogeny and dual. The explicit map, target factorization and duplication above fix and check the convention used here. No unread later algorithm section or current Magma binary is a proof premise of the torsion argument. Public PDF access does not imply a publication license for copying its full text; only this author's proof and reference facts are proposed for Source.

The bounded current managed Source search used the queries P11 isogeny torsion and P11 uniform three torsion, topn8 each, and returned no matches at that observation. The retained accepted returns were then examined at the exact torsion statements, not re-reviewed in full or scientifically rerun. These bounded queries are a deduplication observation, not an exhaustive repository or historical novelty certificate. Existing arithmetic, Mazur, no-four and exact reconstruction are composed; there is no new shared method family or Tool-capability gap.

All original sources, authors, reviews and accepted Tasks remain preserved. This new paper's mathematical claims require their own genuine nonauthor assessment. Actual ranks, higher-pairing values, code/certificate success, Native mathematical votes and parent closure are not inferred from its publication.

Driver-ID: EM-DVR-F73673 / CONTROL_PLANE
