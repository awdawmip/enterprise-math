# Fixed P11 curve: complete local Kummer images and a five-dimensional bound

Status: **new unreviewed paper derivation**, not a Native Result, executed certificate, accepted rank determination, or permission to reopen any closed P11 Task. Author of this specialization and certificate plan: genuine Driver EM-DVR-F73673, session MCP-10b3bf1d95f645ce8c0e419e458a2e49 / DA-7CBB43F6EB54D841994D. NONBLIND, with disclosed shared CONTROL, Public129 review and T6 planning history. This is Owner-authorized reversible paper research. No new enumeration, point search, old checker replay, Native claim, or scientific program has run for this unit.

Direction credit: the fixed-core certified 2-descent/rank-upper-bound question was already proposed by Driver EM-DVR-3B8E7F; the accepted curve, torsion, point H, finite support and P11 maps are due to EM-DIRECT-49ADE6 and EM-DIRECT-C4D02C. EM-PARITYREV-12B648 supplied the later single-candidate planning audit. This note supplies the explicit complete-local-image construction and symbolic five-dimensional reduction. A technical child only locates primary references; that is not independent mathematical review. The author of this note cannot later supply its decisive independent Native vote.

## 1. Exact scope and result of the paper calculation

Retain core (r,s)=(11,8), ordered P=233, Q=119, and

\[
 E:\ y^2=x(x-P^2)(x-Q^2),\quad
 D=P^2-Q^2=40128=2^6\cdot3\cdot11\cdot19.
\]

All objects are external classical elliptic arithmetic with the accepted P11 reconstruction provenance. None of the sixteen squareclass bits below is a native spatial axis. The signed elliptic point, core, denominator and primitive-root reconstruction data are retained whenever P11 output is reconstructed.

For this curve, the paper argument below gives an explicit space W containing the rational Kummer image, with

\[
 \dim_{\mathbf F_2} W=5,\qquad
 1\leq \operatorname{rank}E(\mathbf Q)\leq3.
\]

The lower bound is reused, not newly established: accepted non-torsion H=(194089,69872040). The upper bound is a new paper conclusion whose primary-theorem applicability, finite arithmetic and independent review remain to be frozen in a lawful new portfolio unit. This note does not certify rank one, saturation of H, ranks of other cores, a uniform classification, or parent closure. The derivation gives complete local images, so W also equals the everywhere locally admissible finite-support Kummer-pair space; identifying this with the usual full 2-Selmer group requires the standard split 2-descent identification, which is unnecessary for the rank upper bound itself.

## 2. Kummer map including the zero factors

Write roots e0=0, eP=P^2, eQ=Q^2 in that exact order. On a field K of characteristic zero, use squareclasses and define

\[
 \delta(O)=(1,1,1),\qquad
 \delta(x,y)=(x,x-P^2,x-Q^2)\quad(y\ne0).
\]

At T_i=(e_i,0), replace the zero coordinate by
\((e_i-e_j)(e_i-e_k)\), and retain the other two nonzero differences. Consequently

\[
 \delta(T_0)=(1,-1,-1),\quad
 \delta(T_P)=(1,D,D),\quad
 \delta(T_Q)=(1,-D,-D).
\]

These are squareclass identities, not identities of the unreduced integer triples. In particular the zero x-coordinate of T0 is never passed to a squareclass routine. All three products are squares. Store only the first two classes (a,b); the third is ab.

The standard split Kummer lemma says that delta is a homomorphism with kernel 2E(K). For completeness, the ordinary-point homomorphism identity follows from a chord or tangent y=mx+c: evaluating the cubic minus that squared line at e_i gives
\(\prod_{j=1}^3(x_j-e_i)=(me_i+c)^2\).
The third intersection is the negative of the sum and has the same delta. The exceptional evaluation is the leading nonzero coefficient of x-e_i at T_i; since
\(y^2=(x-e_i)((e_i-e_j)(e_i-e_k)+O(x-e_i))\), it is exactly the replacement above. Equivalently use the evaluation of the function with divisor 2T_i-2O. The two-division criterion then identifies the kernel, including T_i: both nonzero differences must be squares. The accepted REFERENCES.md cites Bekker–Zarhin, Theorem 2.1, over any characteristic-not-two field; a primary reference for the full homomorphism and exceptional evaluation is additionally required in the final certificate source manifest. No sampled local points are assumed to prove this lemma.

## 3. Local cardinality lemma, rather than a sample-span upper bound

For K=Q_p, E(K) has a sufficiently small open subgroup N, given by the formal logarithm, isomorphic to p^n Z_p. Its index is finite because E(K) is compact. Set A=E(K)/N. The exact multiplication-by-two sequence and |A[2]|=|A/2A| give

\[
 |E(K)/2E(K)|=|E(K)[2]|\,|N/2N|
 =\begin{cases}4,&p\text{ odd},\\8,&p=2.\end{cases}
\]

Here N has no two-torsion, |N/2N|=1 or 2, and all four geometric two-torsion points are already K-rational. This proof needs only the standard small-formal-group logarithm; it does not require a minimal integral equation or an unverified reduction type. For R the three real roots give two real connected components; the two Kummer sign patterns are also seen directly below.

Thus **two independent local Kummer images at odd p, or three at p=2, certify the entire local image**. The lower bound from exhibiting points becomes an equality because the independently justified local quotient cardinality is reached. This is the reusable completeness device; a span of arbitrary samples without this argument would not be a certified upper bound.

For odd p, a class is square exactly when its valuation is even and its unit is a quadratic residue. For Q2 an odd unit is square exactly when it is 1 modulo 8. These criteria use ordinary Hensel lifting, not a finite failed-lift search.

## 4. The available global point classes

The accepted H has

\[
 x(H)=49\cdot17\cdot233,\quad
 x(H)-P^2=100\cdot(6\cdot233),\quad
 x(H)-Q^2=1764\cdot(6\cdot17).
\]

Hence
\[
 \delta(H)=(17\cdot233,\ 6\cdot233,\ 6\cdot17)
 =(3961,1398,102).
\]

This reuses H as a known exact point; it is not a new seed, multiple, finite-field count, or non-torsion proof.

## 5. Complete images at 2, 3, 7, 11 and 19

At p=2 the first coordinates of T0, TP and H are all squares: 3961=1 mod 8. Their second coordinates are -1, 627 and 1398. The odd class 627 is 3 mod 8, while 1398=2*699 has odd unit 3 mod 8. Thus these classes are -1, 3, 6. They are independent: valuation first removes 6, and -1,3,-3 are all nonsquare odd units. There are three independent images, so

\[
 I_2=\{(1,b):b\in\mathbf Q_2^*/\mathbf Q_2^{*2}\}.
\]

For each p=3,11,19, -1 is a nonsquare unit because p=3 mod 4, and D has valuation one. T0 and TP therefore give independent second-coordinate classes and trivial first coordinates. By the odd local cardinality lemma,

\[
 I_p=\{(1,b):b\in\mathbf Q_p^*/\mathbf Q_p^{*2}\},
 \quad p=3,11,19.
\]

At p=7, T0 has pair (1,-1), where -1 is a nonsquare unit. H has unit pair (3961,1398)=(6,5) mod 7, both nonsquares. These give two independent vectors in the two unit-squareclass coordinates. Therefore

\[
 I_7=\{(a,b):v_7(a)=v_7(b)=0\pmod2\}.
\]

The equality is modulo squares; it says nothing about literal rational numerators being prime to seven.

## 6. The two missing local witnesses, with exact Hensel conditions

At p=17, T0 and TP are locally trivial: -1 and D=627=15 mod 17 are squares. H has odd first-coordinate valuation, and its second coordinate 1398=4 mod 17 is a square. Construct a second local point L17 with

\[
 x(L_{17})=6Q^2,\quad y(L_{17})=Q^2z,\quad
 z^2=30(6Q^2-P^2).
\]

Since 17 divides Q and not P, the last right side is -30 P^2 mod 17. The identity -30=4 mod 17 supplies the nonzero root z=2P mod 17; the derivative 2z is a unit. Hensel's lemma gives an actual Q17 point. Its first coordinate has nonsquare unit class 6 mod 17 and even valuation, while x-P^2=-P^2 mod 17 is a square unit. The first classes of H and L17 are independent (one odd valuation, one nonsquare unit), so

\[
 I_{17}=\{(a,1):a\in\mathbf Q_{17}^*/\mathbf Q_{17}^{*2}\}.
\]

At p=233, H has odd valuations in both first coordinates. Its third coordinate 102=6*17 is square: (2/233)=1, (3/233)=-1 and (17/233)=(12/17)=-1. Thus its first and second classes agree. Construct L233 with

\[
 x(L_{233})=6P^2,\quad y(L_{233})=P^2z,\quad
 z^2=30(6P^2-Q^2).
\]

Here -30=73^2 mod 233, and Q is a unit. The root z=73Q mod 233 is nonzero with unit derivative 2z, so Hensel again supplies an actual local point. The first two classes are 6 and 5, both nonsquare units at 233: (2/233)=1, (3/233)=-1 and (5/233)=(3/5)=-1. Thus the two classes agree and give the independent diagonal unit class; H supplies the diagonal odd-valuation class. Consequently

\[
 I_{233}=\{(a,a):a\in\mathbf Q_{233}^*/\mathbf Q_{233}^{*2}\}.
\]

Neither local witness is claimed rational over Q. A local witness is not a new global generator. All x-coordinates used here avoid 0,P^2,Q^2, and their displayed unit factors ensure nonzero ordinates.

## 7. Infinity and every prime outside S

Take
\[
 S=\{2,3,7,11,17,19,233\}.
\]

The factorization is exact: Q=7*17, P-Q=2*3*19, P+Q=2^5*11, and D=2^6*3*11*19. For a real point, x is either in [0,Q^2] or in [P^2,infinity); the Kummer signs are respectively (+,-,-) and (+,+,+), including the explicit torsion extensions. Both occur. Therefore

\[
 I_{\infty}=\{(+, +),(+,-)\},
\]

so only the first coordinate must be positive.

At an odd prime l outside S, the integral roots are distinct modulo l. If v_l(x)<0, all three factor valuations equal v_l(x); their square product makes this valuation even. If v_l(x)>=0, at most one factor has positive valuation and the product again forces that valuation even. The torsion-extension factors are units as well. This proves global squareclass support in S without assuming the local-global principle.

It also proves the **complete** local image outside S: its two coordinates are unit classes, giving an ambient subgroup of size four, and the local quotient/cardinality lemma gives an image of size four. Thus every unit pair is locally represented, and no unlisted outside-S local restriction remains. This handles every outside prime uniformly, including arbitrarily large ones; no prime cutoff or sampled-good-prime claim is used.

## 8. Symbolic 16-bit elimination

Choose generators (-1,2,3,7,11,17,19,233) for each signed S-squareclass. Write their first-coordinate exponents alpha and second-coordinate exponents beta. The complete images above imply exactly

\[
 \alpha_-=\alpha_2=\alpha_3=\alpha_7=\alpha_{11}=\alpha_{19}=0,
 \quad \alpha_{17}=\alpha_{233}=t,
\]
\[
 \beta_7=\beta_{17}=0,\quad \beta_{233}=t,
 \quad \beta_3+\beta_{11}=t.
\]

Here is a direct check that no extra condition was silently dropped. The first-coordinate valuation restrictions arise at 2,3,7,11,19 and the sign at infinity. The remaining primes 17 and 233 are both nonsquare modulo 3 and 11, so those square-unit conditions impose alpha17=alpha233. Both are squares modulo 19 and 1 modulo 8, so the remaining 19 and 2 unit tests are automatic. For beta at 17, -1,2,19 are squares, whereas 3,11,233 are nonsquares; hence beta3+beta11+beta233=0. At 233, -1,2,19 are squares and 3,11,17 are nonsquares, so equality of the two unit classes says beta3+beta11=t. The valuation equality there gives beta233=t. These are the same condition, not two extra independent restrictions.

Equivalently the eleven rows over F2 are

```
A-=0, A2=0, A3=0, A7=0, A11=0, A19=0,
A17+A233=0, B7=0, B17=0,
B233+A233=0, B3+B11+A233=0.
```

They have distinct pivots A-,A2,A3,A7,A11,A19,A17,B7,B17,B233,B11 and free coordinates A233,B-,B2,B3,B19. This is a symbolic rank-eleven proof, not a 65,536-case enumeration. The resulting five-dimensional space is

\[
 W=\left\{\left((17\cdot233)^t,
 (-1)^u2^v3^w11^{w+t}19^z233^t\right):
 t,u,v,w,z\in\mathbf F_2\right\}.
\]

An alternative basis is

\[
 \delta(T_0),\ \delta(T_P),\ \delta(H),\ U=(1,2),\ V=(1,19).
\]

Their independence follows respectively from the sign coordinate, the 3/11 coordinate, the nontrivial first coordinate, the 2 coordinate and the remaining 19 coordinate, or by triangular substitution in the displayed parametrization. U and V are local-admissibility classes; they are NOT asserted to arise from global rational points.

The Kummer injection gives
\(E(\mathbf Q)/2E(\mathbf Q)\hookrightarrow W\).
By finite generation and full rational two-torsion this quotient has dimension rank(E)+2. Therefore rank(E)<=3. The accepted H gives rank(E)>=1. No statement about Sha finiteness or the parity of the rank is needed, and no parity shortcut is invoked.

## 9. A finite certificate and a genuinely discriminating next question

A certifying consumer need only check fixed input/factorizations, the exceptional Kummer convention, the standard Kummer/kernel and local-index theorems with their hypotheses, each displayed local-point/Legendre/2-adic/Hensel witness, and the eleven independent F2 rows. Its evidence can be a short exact integer/residue and matrix transcript, without a global point census or 65,536 coverings. A different consumer should derive local-square tests and elimination independently, reject wrong coordinate order, omitted T0/zero-factor extension, a nonsquare Hensel unit, missing infinity/outside-S proof, a duplicated pivot, or treating U/V as global points. Finite arithmetic execution requires a lawful new unit/own authorization; none occurred for this paper.

The residual question is now two-dimensional rather than a blanket all-core classification. Modulo the known image generated by T0,TP,H, only U and V remain. A full certified 4-descent or a correctly sourced Cassels pairing on these two residual classes can distinguish the rank-one claim: a nonzero alternating pairing on the residual two-space, together with the theorem that rational Kummer images lie in its radical, would force dimension(E(Q)/2E(Q))<=3 and hence rank one. **No pairing value has been computed or assumed here.** If its entry is zero, that is not proof of rank three; one must return the surviving ambiguity or supply actual independent rational points/higher-descent evidence. The exact covering equations for U and V, with the fixed coordinate order, are reusable finite inputs, not certificates of global solubility.

Thus the next lawful publication can ask for the fixed upper-bound certificate, with a separately costed optional residual pairing question only after its primary formula and local-symbol consumer are fixed. It must not reopen the five accepted old Tasks or declare their former rank gap an unfinished old acceptance obligation. There is no proposed expansion to all-core ranks, H saturation, unsigned P11 group operations, native geometry, Working Truth or Foundation.

## 10. Source and verification boundary

The eight original immutable Source files were independently fetched and byte/SHA-256/Git-blob checked; see original_source_intake/EIGHT_ORIGINAL_SOURCE_FILES_OWN_VERIFIED.json. In particular the original diagonal RETURN explicitly stops at rank>=1; Driver 3B8E7F explicitly recommends assessing this separate fixed-core rank-upper-bound gap. The later R2 six-member unreviewed control-custody capsule was independently decoded and all member pins checked, see SOURCE_CAPSULE_AND_ALL_SIX_MEMBERS_OWN_VERIFIED.json. Control custody is not scientific acceptance. Current Goal/portfolio ownership and legal new-publication contracts are maintained separately; they cannot replace this proof or create an authorized arithmetic run.

All numerical identities and the linear reduction in this file are paper calculations. They are ready for independent challenge, not being relabeled as executed Native science. Exact primary reference locator output will be attached as a new sidecar; this frozen-note version must not acquire a claim that a locator independently verified the mathematics.
