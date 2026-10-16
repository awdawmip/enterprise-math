# A mixed higher-pairing bit at core (9,8): conditional theorem and certificate boundary

Status at author freeze: UNREVIEWED CONDITIONAL PAPER. The abstract well-definedness theorem below is asserted with proof; its arithmetic bit, explicit four-cover and computable mixed-pairing certificate are UNKNOWN. No arithmetic program, point search, four-descent or certificate consumer has run. This is a composition inside the existing classical descent method family, not a new Tool family or a historical novelty claim.

Author: EM-DVR-F73673, canonical actor /root/public129_line_reviewer, actual Driver SID MCP-10b3bf1d95f645ce8c0e419e458a2e49 / DA-7CBB43F6EB54D841994D. Directed NONBLIND shared-control and all prior P11 proof/planning contributions are retained. A different genuine nonauthor must review this new object; none of the earlier paper verdicts reviews it. The stopped fixed-(233,119) certificate Task and its exhausted budget are not inputs or authority for this paper.

All curves, torsors, completions and Galois cohomology here have their external classical arithmetic types. They do not reinterpret Heartbeat's native affine Z6 torsor and six discrete Cell axes. There is no native plane; time is separately typed only for provenance. No Working Truth, Foundation or parent closure follows.

## 1. Exact reuse and the remaining information gap

Retain the primitive Euclidean core (9,8), with A=17, B=144, P=161, Q=127 and D=P^2-Q^2=9792=2^6*3^2*17. The fixed ordered-root curve is

    E: y^2 = x(x-25921)(x-16129).

For U_b=(1,b,b), the sixth paper proves the full two-Selmer group

    W = Sel_2(E/Q) = <U_-1,U_2,U_3,U_17>, dim_F2 W=4,

and proves its entire genuine Cassels form is zero. This is full coverage, not merely a vertical restriction or the tenth compatibility matrix. The actual rational two-torsion Kummer image is K0=<U_-1,U_17>, of dimension two. These are exact inherited inputs, not new calculations. Thus W/K0 has the explicit basis represented by U_2 and U_3.

The eleventh paper, using the exact CT-kernel/image theorem and an all-place restricted-kernel argument, proves

    pi: Sel_4(E/Q) -> W is onto;
    ker pi = i(W), ker(i|W)=K0;
    Sel_4(E/Q) = (Z/4)^2 direct_sum (Z/2)^2;
    Sha(E/Q)[4] = (Z/4)^(2-r), with r UNKNOWN in {0,1,2}.

The two papers are actual author Source4090e063926e770103afc4628ea40c8a8949cedb and Sourcea427759fc3dffd69c3d90ccf8440b6af8acf9e2a, respectively. Their original freeze histories remain unchanged. The separate eleventh nonauthor paper review has been fully read; its Source40eb6e1e438f20f8fba06b8aa04f6dce06999613 is the reviewer's reported actual full-byte publication, not a claim that this author has newly fetched those four review files. A separate dependency manifest retains the exact original local hashes.

Counting the 64 abstract four-Selmer classes again cannot distinguish r=0,1,2: that group is already the same in all three cases. The new finite information sought here is a genuine mixed CT value. Its existence as an abstractly defined quantity must be separated from the production and verification of a concrete covering and a formula that computes it.

## 2. Mixed pairing on the first radical: a general conditional lemma

Let E/Q be an elliptic curve with full rational two-torsion. Write W=Sel_2(E/Q), S=Sel_4(E/Q), and q_n:Sel_n->Sha[n] for the Kummer quotient. Let B be the classical alternating Cassels--Tate pairing Sha x Sha -> Q/Z. Its pullback to W is b_0. Write R=rad(b_0), and assume the standard kernel/image theorem in the exact form im(pi:S->W)=R. The all-place kernel argument gives ker pi=i(W), where i comes from E[2] included in E[4]. The maps on Sha satisfy

    q_4(i(w)) = q_2(w),       2*q_4(c) = q_2(pi(c)).

Here q_2(w) on the right of the first identity is included in Sha[4]. These are Kummer naturality identities, not the false identity i(delta_2(P))=delta_4(P): the actual identity is i(delta_2(P))=delta_4(2P).

For x,y in R, choose any c_y in S with pi(c_y)=y and define

    beta(x,y) = j( B(q_2(x),q_4(c_y)) ) in F2,

where j is the group isomorphism {0,1/2} subset Q/Z -> F2 taking 1/2 to 1. The value is in this subgroup since q_2(x) is killed by two. This notation does not multiply a half by two inside Q/Z, which would lose the bit.

**Lemma.** beta is well-defined, bilinear and alternating on R. The full rational Kummer image K=delta_2(E(Q)/2E(Q)) is in its radical. If lambda=rank_F2 beta, then

    r <= dim R - lambda - 2.

Proof. Two lifts of y differ by i(w), w in W. Their pairing difference with x is B(q_2(x),q_2(w))=b_0(x,w)=0 because x lies in R. Hence the value is independent of the lift. The discrepancy between a lift of y+z and the sum of separately chosen lifts again lies in i(W); this proves additivity in the second argument. Additivity in the first is immediate. For the diagonal, choose c_x and put a=q_4(c_x). Then q_2(x)=2a and B(2a,a)=2B(a,a)=0, by actual alternation of the elliptic CT pairing. Thus beta is alternating. Its F2 bilinearity also makes it symmetric.

A rational Kummer class has zero Sha image, so it is in the left radical, and therefore also in the right radical. Equivalently, for y=delta_2(P) one can choose c_y=delta_4(P), whose Sha image is zero. K is already contained in R for the same reason. Since full rational two-torsion gives dim K=r+2, we have r+2 <= dim rad(beta)=dim R-lambda. This proves the bound. No finiteness of all Sha, explicit lifting algorithm or splitting of a Selmer extension is used. QED.

This is a higher-descent consequence of the standard CT pairing and exact sequences. It is presented as a derived reuse lemma, not as a claim of an original general duality theorem. A compatibility matrix, a restricted vertical matrix without coverage, or a two-isogeny pairing cannot replace b_0.

## 3. One bit at the exact core and the sharp nonzero consequence

At core (9,8), R=W because b_0=0. K0 is in K and hence in rad(beta), so beta descends to the two-dimensional space W/K0. It is completely determined by

    e = beta(U_2,U_3) in F2.

In particular, every actual choice of a four-Selmer lift c_3 of U_3 gives the same e. No sweep of lifts can change it.

**Conditional theorem.** If a genuine certificate establishes

    B(q_2(U_2),q_4(c_3)) = 1/2 in Q/Z, pi(c_3)=U_3,

then r=0 and Sha(E/Q)[2^infinity] is exactly (Z/4)^2.

Proof of the rank assertion. The nonzero alternating form on the two-dimensional quotient W/K0 has rank two. The lemma gives r <= 4-2-2=0. Nonnegativity gives r=0, and the eleventh theorem then gives A=Sha[4] isomorphic to (Z/4)^2.

Proof of the full two-primary assertion. Surjectivity in the eleventh theorem gives a in A with 2a=q_2(U_2); set b=q_4(c_3). The certified equality gives 2B(a,b)=1/2, so B(a,b) is an odd quarter. On A=(Z/4)^2, an alternating form is represented in any Z/4 basis by a matrix tJ/4. The existence of an odd-quarter value makes t a unit modulo four. Consequently the restricted form on A is nondegenerate.

If Sha had an element of order at least eight, multiplying it by a suitable power of two would give an element z of exact order eight. The nonzero element 4z lies in A and pairs to zero with every a' in A, since B(4z,a')=B(z,4a')=0. This contradicts nondegeneracy on A. Hence every two-primary torsion element is already killed by four, and Sha[2^infinity]=A=(Z/4)^2. No finiteness hypothesis for all Sha was needed. This argument says nothing about odd-primary Sha or saturation of a Mordell--Weil generator. QED.

The antecedent is currently UNKNOWN. There is no actual c_3, mixed pairing value, new rational point or rank-zero verdict in the present paper.

## 4. The zero branch is a strict stop for this particular bit

If a correct certificate gives e=0, beta is zero on all W/K0 and hence on W. Testing another lift of U_3, changing the quotient basis, or filling the already-known abstract 64-element Sel_4 group supplies no further value of this same form.

Zero does not prove a rational point or rank two. A purely algebraic countermodel to that inference is A_infinity=(Z/8)^2 with its standard perfect alternating pairing B(e_1,e_2)=1/8. Then A_infinity[2] is generated by 4e_1,4e_2 and A_infinity[4] by 2e_1,2e_2. Both the first pairing on A[2] and the mixed pairing A[2] x A[4] are zero, while A[4]=(Z/4)^2 is nonzero. This is a pairing/group countermodel, not a claim that the present curve has this Sha or that a curve realizing it has been constructed. It proves that the available algebra does not justify the proposed rank inference from a zero bit.

A later question about the entire Sel_4 x Sel_4 pairing would be different: that restriction can have half-valued terms even when the mixed bit vanishes, as the same countermodel illustrates. Such a route needs actual new covering data and a separately justified calculation; it is not silently authorized by this conditional paper. No repeated lift search or automatic higher-stage Task follows.

## 5. Exact low-level covering data and the missing higher lift

The existing two-cover for U_b may be retained with coordinates [z_1:z_2:z_3:t]:

    C_b: z_1^2-b*z_2^2 = 25921*t^2,
         z_1^2-b*z_3^2 = 16129*t^2.

For t nonzero its fixed map to E is x=z_1^2/t^2, y=b*z_1*z_2*z_3/t^3. Direct substitution verifies the cubic. In the projective Weierstrass model its homogeneous expression is

    [X:Y:Z]=[z_1^2*t : b*z_1*z_2*z_3 : t^3].

All entries have degree three. At t=0 the two quadrics force z_1*z_2*z_3 nonzero at any projective point, so the displayed map still reaches O and has no base point there. The inherited two-descent dictionary fixes its covering class as U_b; the displayed equations alone are not a newly supplied four-cover. In the proposed one-bit input take b=3; U_2 is the retained first argument.

An actual higher-lift certificate must give c_3 in H1(Q,E[4]) with pi(c_3)=U_3 and all local four-Kummer conditions. It may use either a fully verified cohomological representation or geometric four-cover data with the actual torsor/Jacobian identification. In the geometric option, a smooth genus-one D, a geometrically [4] covering map D->E of degree 16, and a compatible geometrically [2] map D->C_3 of degree four must be proved to represent that exact cohomological lift. A map of the right degree or the reuse of C_3's rational equations is not by itself that proof. All rational map domains, exceptional charts, cocycle/covering identifications and coefficients must be retained; no particular model or embedding degree for D is invented here.

Everywhere local solubility of C_3 is an old input. It does not establish local solubility of a newly supplied D. The latter needs its own exact local points or suitable Hensel certificates and an outside-support proof. At a finite place, a legitimate certificate can specify an actual chart and a verified simple-root/Hensel condition, or a correctly justified higher-precision singular-root argument. A residue solution alone, especially at 2, is insufficient. Real solubility also requires an actual point or an exact sign/continuity argument on D.

The old curve support is {2,3,7,17,23,127,infinity}. A proposed four-cover and its pairing functions may add bad primes from coefficients, denominators, discriminants or divisors. Therefore the complete support is not frozen to this old list before those objects exist. Good-prime/unramified or unit arguments must cover every omitted prime, with their actual hypotheses, rather than treating finite local success as global coverage.

## 6. What constitutes a computable mixed-pairing certificate

The following are prospective typed obligations, not an assertion that an implementation or a ready execution task exists.

1. Exact input: the fixed E, ordered roots, full W/K0 basis, a verified c_3 with pi(c_3)=U_3, and exact all-place local lift evidence as above. Digests of a nonexistent c_3, code or codec remain null.
2. A mathematically established formula for the actual S(2) x S(4) pullback of CT, with all hypotheses and model changes checked against its primary source. A formula only proved for S(2) x S(2), an unexamined source title, or the tenth compatibility pairing is insufficient. Its actual implementation, if any, would need a pinned source/toolchain/config and a fresh authorized actor; none is selected here.
3. A finite complete support for that actual formula and a proof of zero invariant outside it. At each listed place retain the actual local data, formula inputs, exact invariant in Q/Z and the proof that any zero/pole avoidance or chart transition is legitimate. The global sum must be exactly 1/2 for the nonzero branch. No particular local diagnostic strings or unproved Hilbert-symbol format is imposed: if a chosen proven formula gives local half-invariants, it may specialize accordingly; otherwise exact rational invariants are retained.
4. Genuine nonauthor preaudit of the actual immutable code/input/codec/evidence-cost plan before any future scientific invocation, plus whatever current Native authorization and explicit resource budget that future task requires. This paper supplies none of those grants and changes none of the stopped fixed-233 resources.

The minimal discriminating target is one valid c_3 and one complete mixed-pairing evaluation. It is not all four-cover representatives, a rank census, saturation or a whole-family classification. Failure to obtain the actual primary formula, a valid local lift, complete support, a sound codec or an authorized bounded execution plan is an explicit NO_ARITHMETIC_START boundary. A zero certified bit ends this one-bit unit with ZERO_NOT_A_RANK_DECISION, without an automatic parameter sweep or lift retry. Any detected invalid certificate is rejected at its exact failing obligation; it is not recorded as arithmetic evidence.

## 7. Literature and availability: what was actually read

Shukla--Stoll arXiv:2302.01640v1, actual retained PDF SHA256 f84fee9a3cd3e2e37aee1c0b41f08296e88988a5f1142c5911b4d16762e408ce, PDF pages 1--2 supplies the n-Kummer sequence, alternating CT pairing and exact image/kernel statement. These actual pages were fully read for the eleventh object and reread here. Page 3 explicitly identifies Swinnerton-Dyer [SD13] as a generalized route to S(2) x S(2^m). This establishes a relevant literature route, not the correctness of any imagined computational formula.

Fisher--Schaefer--Stoll arXiv:0710.2079v1, retained PDF SHA256 70c46caaf9b6a34efc65e341a610afc62b5ca3e7591ee3ec133287c4b78f32b4, Theorem 5.2 supplies the comparison used by the inherited first Cassels form. It is not silently promoted into a fully implemented higher-pairing evaluator.

The actual 2026-10-16 metadata lookup resolves SD13 as Peter Swinnerton-Dyer, 2^n-descent on elliptic curves for all n, Journal of the London Mathematical Society87(2013),707--723, DOI10.1112/jlms/jds063. Crossref returned the exact record; OpenAlex and Semantic Scholar reported CLOSED/no open PDF. The actual DOI/publisher request returned HTTP403. The complete SD13 primary was not obtained or read in this bounded lookup, its algorithm hypotheses/representation/code interface remain UNKNOWN, and no inaccessible source is quoted as though read. No claim of a permanent impossibility of access is made. Actual responses and timestamps are retained separately. There was no existing tool execution or fresh capability-gap claim from these metadata observations.

The arithmetic result now proved is the conditional one-bit implication and its precise limit. Actual concrete evaluation remains missing, and no rank assertion for core (9,8) is made until its nonzero antecedent has a separately reviewed genuine certificate. All existing parents remain OPEN.

Driver-ID: EM-DVR-F73673 / CONTROL_PLANE
