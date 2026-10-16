# Independent paper review of the fixed P11 rank upper bound

Reviewer: Researcher EM-PUBLIC-7CDA51, existing session MCP-9030ae3a22074e3dbc31679b7090f6b0 and activity RA-6665DBCD10BC1C3E4DED3C04. This is Root-delegated nonauthor mathematical support, not a Native Driver review or an acceptance vote. All Public129 authorship, CONTROL/environment/CI work, T6 support and CONTROL admission-audit history remain disclosed. I did not construct the P11 plan, local-image proof or implementation. This is shared-context, nonblind review; a different identity is not its independence argument.

## Judgment and frozen object

The supplied paper supports its exact mathematical conclusion: the displayed local conditions define a five-dimensional space containing the rational Kummer image, and hence

\[
1\leq\operatorname{rank} E(\mathbf Q)\leq3,
\qquad E:y^2=x(x-233^2)(x-119^2).
\]

With the stated Stoll identification, that five-dimensional space is the full 2-Selmer group. I found no mathematical defect in this scope after checking the exceptional Kummer values, local cardinality argument, all seven finite places, infinity, all outside primes and the symbolic elimination. This judgment does not determine rank one, saturation, other cores, a pairing value, a complete P11 classification or parent closure. The later residual-pairing manuscript is a separate object and has not been used in this judgment.

The reviewed author files are precisely:

- `P11_LOCAL_KUMMER_IMAGE_PAPER_LEMMA.md`, 15849 bytes, SHA-256 `ede0dffd326126371c5c1585bbdf0e81076139560494d4ba4b8c322ea8c2bd0f`.
- `P11_PRIMARY_THEOREM_APPLICABILITY_AND_EXACT_SCOPE.md`, 7769 bytes, SHA-256 `a322dd552307535d600dcabc0999af3d1df57ef7e4da682a0190a3ee6500412b`.
- Author proof capsule, 560764 bytes, SHA-256 `ff4a4ecb84d54101779b3c215ccaa49088241a13f00c7dd9ff42d40c82e2ae5a`; I decoded and checked all 34 regular members, 900975 original bytes, including every member length, SHA-256 and Git blob.

At this review these are **frozen local author inputs pending Source publication**, not Source-accepted new results. Any later publication must match these exact bytes before this review is attached to it. No enumeration, point search, affine experiment, old checker replay, arithmetic consumer or Native scientific run was executed for this review. Hashing, decoding, Source reads and the activity guard are custody/startup operations.

## Theorems, carrier and zero coordinates

The ordered roots are `(0,P^2,Q^2)`, with `P=233`, `Q=119` and distinct values `0,54289,14161`. The cubic is monic, integral, square-free and of degree three. Its smooth projective curve has the rational point O at infinity, genus one, and the usual group identification with its Jacobian. The nonzero quadratic coefficient is allowed by Stoll's odd-degree setup.

I read the complete relevant Stoll text pages: PDF 1–3, 5–7 and 10, corresponding to printed 245–247, 249–251 and 254. Section 4 and Lemma 4.1 give the natural Kummer injection and kernel `2J(K)` for field extensions of Q; Proposition 4.2 gives the all-place Selmer condition; Lemmas 4.3, 4.4 and 4.8 supply the torsion evaluation, finite-local dimensions and real case. In this split genus-one specialization `L_K=K^3`, and its norm-square kernel is exactly the triple carrier with square product. Retaining its first two classes loses no Kummer coordinate because the third is their product.

The zero-factor rule is correct. For T0 the first replacement is `P^2 Q^2`, and the other coordinates are `-P^2,-Q^2`, giving `(1,-1,-1)`. At TP it is `P^2(P^2-Q^2)` in the second coordinate, giving `(1,D,D)`; at TQ the resulting triple is `(1,-D,-D)`. Each product is a square. No zero is interpreted as an element of `K*/K*2`.

Specializing Stoll's factor formula also gives these signs directly: for `f_i=T-e_i`, its value away from the i-th component is `e_i-e_j`, and the i-th component is the product of the other two root differences. The chord identity has the correct sign after evaluating the monic cubic minus the square of the line. Infinity and vertical/exceptional cases are covered by the Kummer theorem, rather than by extending an ordinary formula through zero.

I separately read Wuthrich PDF pages 62–65: equations 7.1–7.3, Proposition 7.2 and its exceptional-case proof, and Proposition 7.3/Lemma 7.4 with the halving proof. That source uses a short model. The author's bridge `x=X+(P^2+Q^2)/3` is a field isomorphism in every relevant characteristic-zero field, including Q3; it leaves every difference `x-e_i` and exceptional root difference unchanged. It is not used to change the integral model for residue calculations. Stoll already supplies the general model, so no unjustified short-model assumption is needed.

These readings use the exact frozen complete text/PDF inputs and the declared publisher/author locators; I did not perform a new external download. Their primary-source applicability was assessed here rather than inferred from the technical locator's opinion.

## Why the local images are complete

The quotient-size argument is valid even at bad reduction. Choose a sufficiently small formal-logarithm subgroup N with no two-torsion and finite quotient A. The multiplication-by-two exact sequence has the factor `|A/2A|/|A[2]|=1`, so

\[
|E(\mathbf Q_p)/2E(\mathbf Q_p)|=|E(\mathbf Q_p)[2]|\,|N/2N|.
\]

Full rational two-torsion makes this 4 at odd primes and 8 at 2. This agrees with Stoll Lemma 4.4 for `g=1,m_K=3`. Consequently the exhibited independent images attain the entire quotient; they are not merely a sampled lower bound on an unknown image. The Kummer injection is essential to that conclusion.

- At 2, all three first coordinates are squares, including `3961=1 mod 8`. The second classes of T0, TP and H are `-1,3,6`: `D=64*627`, `627=3 mod 8`, and `1398=2*699` with `699=3 mod 8`. Valuation separates 6; `-1,3,-3` have odd units 7,3,5 and are nonsquares. Thus all eight second classes occur with trivial first coordinate.
- At 3,11,19, `-1` is a nonsquare unit and D has valuation exactly one. T0 and TP therefore give two independent second classes with trivial first coordinate, attaining all four images at each place.
- At 7, T0 gives a nontrivial second unit class, while H has first unit `3961=6 mod 7` and second unit `1398=5 mod 7`, both nonsquares. These two vectors are independent. Their four-element span is exactly all unit pairs.
- At 17, H has odd first valuation and square second coordinate (`1398=4 mod 17`). The proposed point with `x=6Q^2`, `y=Q^2 z` satisfies the curve exactly when `z^2=30(6Q^2-P^2)`. Its reduction has a nonzero root `2P`, since `-30=4 mod 17`; derivative `2z` is a unit. The genuine Hensel lift gives first nonsquare unit class 6 and square second coordinate `-P^2 mod 17`. Odd valuation versus nonsquare unit proves independence, hence the entire image is `(a,1)`.
- At 233, H has odd first and second valuations, with their ratio square because its third class is `102=6*17`. Quadratic reciprocity gives `(2/233)=1`, `(3/233)=-1`, `(17/233)=-1`. For the second point, `x=6P^2`, `y=P^2 z` and `z^2=30(6P^2-Q^2)`. The identity `73^2=-30 mod 233` gives the nonzero root `73Q` and unit derivative. Its first two classes are respectively 6 and 5, both nonsquare units; the third factor is a square. This gives an independent diagonal unit class beside H's diagonal odd-valuation class. Thus the full image is `(a,a)`.

All local witnesses avoid the three roots; both Hensel radicands are units at their stated prime and so have nonzero lifts. No local witness is being promoted to a rational point over Q.

## Infinity, support and all omitted primes

Over R, the cubic permits `0<=x<=Q^2` or `x>=P^2`. The first Kummer coordinate is positive and the second may have either sign. The exceptional values at all endpoints agree with this extension. Thus infinity imposes precisely positivity of the first class, and no condition on the sign of the second.

The factorization `D=2^6*3*11*19`, `Q=7*17`, `P-Q=2*3*19` and `P+Q=2^5*11` gives exactly `S={2,3,7,11,17,19,233}`. At any odd l outside S, the roots are integral and distinct modulo l. If x has negative valuation, all three factors have that valuation and their square product forces it even. Otherwise at most one factor can have positive valuation, which is again even. At torsion points the replacement factors are units. This proves even valuations outside S, including the exceptional points and O.

The resulting unit-pair ambient group has four elements, and the local Kummer image also has four by the independently justified quotient size. Therefore every unit pair is represented at every outside prime. This is a uniform all-prime proof; it uses no cutoff or assumption that local solubility implies a rational point.

The same outside-prime fact applies to the local images used in Proposition 4.2, so an everywhere admissible rational squareclass pair necessarily has support in S. The identification of the finite-support W with the full 2-Selmer group consequently omits no outside-support classes.

## Independent check of the eleven equations and the bound

Using signed S-generators `(-1,2,3,7,11,17,19,233)` in each coordinate, the valuation and sign conditions first force

\[
A_-=A_2=A_3=A_7=A_{11}=A_{19}=0,\quad B_7=B_{17}=0.
\]

The remaining first-coordinate factors 17 and 233 are both nonsquare units at 3 and 11, yielding `A17=A233=t`. They are both square at 19, and both 1 modulo 8; thus the remaining first-coordinate unit tests at 19 and 2 add nothing.

At 17 the second coordinate is square: `-1,2,19` are square units and `3,11,233` are nonsquare units. Hence `B3+B11+B233=0`. At 233 the diagonal image requires `B233=t`. Its unit equality uses `-1,2,19` square and `3,11,17` nonsquare, giving `B3+B11=t`. These are compatible descriptions of the same remaining relation. At 7 only the two valuation conditions apply, and infinity has already supplied A-=0. This accounts for all local tests in both directions.

The eleven rows have pivots `A-,A2,A3,A7,A11,A19,A17,B7,B17,B233,B11`. Their five free variables are `t=A233,B-,B2,B3,B19`, giving exactly the displayed W, not only an upper estimate for its dimension. I checked this by substitution and pivot structure on paper, not by enumerating 65536 classes or executing a matrix checker.

The proposed alternative basis is also independent: H is the only displayed vector with nontrivial first class, T0 supplies the sign, TP supplies the remaining 3/11 coordinate, and U,V supply the independent 2 and 19 coordinates after those are fixed. U and V therefore give two residual classes modulo the three known images; this statement does not supply rational points for U or V.

The Kummer injection bounds `dim E(Q)/2E(Q)` by 5. Finite generation and full rational two-torsion give `dim E(Q)/2E(Q)=rank(E)+2`, hence the upper bound 3. The lower bound 1 is reused from the exact accepted H non-torsion certificate, not inferred from local admissibility. The original RR-C1F5BD75CF29E3970097 and its ACCEPTED review DR-2F805343ED6728A5CD35 retain that scope and authorship; no old torsion count, multiples or reconstruction checker was rerun.

## Custody, role and remaining boundary

Fresh managed Source reads at `8517b55c76413ce735b67210912ccd6f72b2fee1` verified my unchanged session/RA, the original Taskbook/publication, Goal, RR, accepted DR, original return/review and references. Current P000/Heartbeat X6/joint-observer contracts were loaded; this is external static classical arithmetic, not a native plane, a new spatial-axis interpretation of squareclass bits or a full-X6 propagation claim. Signed elliptic/core/reconstruction data remain required for P11 output; the Kummer quotient is used only for its declared descent/rank observer, through a proved homomorphism, not as a state on which arbitrary P11 group reconstruction can be performed.

The own activity and runtime startup guards allow the directed activity and persistence, while `authorized=false` and all formal authority flags remain false. The original Public129 immutable session scope and frozen run were not rewritten or borrowed. Old Public lightweight-RA coverage debt remains disclosed; this review does not invent retroactive events.

The scientific conclusion above is an independent nonauthor paper assessment. A future finite arithmetic certificate is a separate lawful execution unit; its absence does not invalidate the present paper argument, and this review does not pretend it already exists. Source matching and my own semantic persistence event remain to be completed through a coordinated publication window. No Native RR/DR, new Task, CLAIM, Source mutation, global completion or permission to execute further science is created by this file.

Researcher-ID: EM-PUBLIC-7CDA51 / TASK_RESEARCH
