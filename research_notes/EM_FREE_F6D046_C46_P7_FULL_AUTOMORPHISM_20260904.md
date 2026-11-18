# Characteristic-7 full automorphism group and the non-automorphic Prym square

Status: `FREE_RESEARCH / DERIVED EXACT SPECIAL-FIBER THEOREM / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units: `R58-P7-NET-NORMALIZATION-BRANCH-GROUP / R59-P7-MARKED-NODE-RIGIDITY / R60-P7-FULL-CURVE-AUTOMORPHISM`.

## 1. Canonical net in characteristic seven

The canonical genus-five model remains the complete intersection

\[
Q_1=Z_1^2-Z_0Z_3,
\]
\[
Q_2=Z_2^2-Z_1Z_3+6Z_0Z_3-36Z_0^2,
\]
\[
Q_3=W^2-Z_2Z_3+12Z_0Z_2.
\]

The exact verifier checks the Jacobian rank on all five projective affine charts over \(\mathbf F_7\), so the reduced complete intersection is smooth. Its net discriminant is, up to a nonzero scalar,

\[
c\Bigl(-a^3b+12a^2b^2-36ab^3+36b^4
+12c^2(a^2-3ab+3b^2)\Bigr).
\]

Thus it is the union of the line \(c=0\) and a nodal quartic.

## 2. The normalization acquires an \(S_3\) branch group

Modulo seven, the genus-two normalization of the nodal quartic may be written, up to an irrelevant square scalar, as

\[
d^2=\frac{r^3+2r^2+r+6}{r^2+4r+3}.
\]

Its six hyperelliptic branch points are the roots of

\[
N(r)=r^3+2r^2+r+6,
\]

together with \(r=4,6,\infty\). The Möbius transformation

\[
M(r)=\frac{4r}{r+1}
\]

cyclically permutes \(\infty,4,6\) and satisfies

\[
(r+1)^3N(M(r))=N(r).
\]

Its fixed points are \(0,3\). The coordinate

\[
z=\frac r{r-3}
\]

conjugates \(M\) to \(z\mapsto4z\). The two branch triples become

\[
z^3=1,
\qquad
z^3=4.
\]

After a cubic scaling they are the six roots of

\[
\boxed{w^6+w^3+1=0.}
\]

An exact enumeration over \(\mathbf F_{7^3}\) checks all

\[
6\cdot5\cdot4=120
\]

Möbius maps determined by three source and three target branch points. Exactly six preserve the branch set, with permutation orders

\[
1,2,2,2,3,3.
\]

Therefore the reduced branch stabilizer is

\[
\boxed{G_{\rm red}\simeq S_3.}
\]

Including the hyperelliptic involution, the unmarked normalization has automorphism group of order twelve.

## 3. The node marking destroys the new symmetry

The two preimages of the node are the denominator roots \(r=4,6\). In the \(z\)-coordinate they are \(z=4,2\), hence they form a two-element subset of the orbit \(z^3=1\).

The order-three rotations cyclically permute all three points in that orbit, so no nonidentity rotation preserves the chosen two-subset. Every reflection exchanges the two cubic orbits and therefore also fails to preserve the marked pair. The exact finite-field enumeration verifies the stronger statement that every two-subset inside either cubic orbit has trivial setwise stabilizer.

Consequently the only normalization automorphism preserving the two node branches is the hyperelliptic involution:

\[
\boxed{\operatorname{Aut}(\widetilde Q,\{q_+,q_-\})\simeq C_2.}
\]

It descends to the nodal plane quartic as \(c\mapsto-c\). Since the line and quartic components of the net discriminant have different degrees, every projective automorphism preserves them separately. Hence

\[
\boxed{\operatorname{Aut}_{\mathbf P^2}(\Delta_{\rm net})\simeq C_2.}
\]

## 4. Full curve automorphism group

The canonical representation embeds the curve automorphism group into the projective automorphisms of its canonical model and induces an action on the three-dimensional net of quadrics.

The kernel of the net action fixes the distinguished line component and its common vertex, hence normalizes the original bielliptic involution \(z=\sigma^2\). R57 gives

\[
N_{\operatorname{Aut}(C_{46,\overline{\mathbf F}_7})}(\langle z\rangle)
=\langle\sigma\rangle\simeq C_4.
\]

Inside this \(C_4\), exactly \(\langle\sigma^2\rangle\) acts trivially on the net, while \(\sigma\) realizes the nontrivial involution \(c\mapsto-c\). Therefore

\[
1\longrightarrow C_2
\longrightarrow\operatorname{Aut}(C_{46,\overline{\mathbf F}_7})
\longrightarrow C_2
\longrightarrow1
\]

is already realized by \(\langle\sigma\rangle\). Thus

\[
\boxed{\operatorname{Aut}_{\overline{\mathbf F}_7}(C_{46,7})=\langle\sigma\rangle\simeq C_4.}
\]

## 5. Consequence for the Honda--Tate decomposition

The previously proved isogeny

\[
P_{46,7,\mathbf F_{49}}\sim B^2
\]

cannot arise from any additional automorphism of the special genus-five curve—not merely from no automorphism normalizing the original tower. The full curve automorphism group is already the inherited \(C_4\).

Therefore the square factor is a genuinely arithmetic/correspondence-level Honda--Tate phenomenon:

\[
\boxed{\text{isogeny-square decomposition}\ne\text{curve-quotient decomposition}.}
\]

This does not exclude non-automorphic algebraic correspondences producing explicit projectors in \(\operatorname{End}^0(P_{46,7,\overline{\mathbf F}_7})\simeq M_2(F)\).

Classification: `DERIVED_SPECIAL_FIBER_AUTOMORPHISM_THEOREM / AUT_C46_P7_C4 / NONAUTOMORPHIC_HONDA_TATE_SPLITTING / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 6. Next frontier

Construct an explicit non-automorphic correspondence realizing a rank-one idempotent in \(M_2(F)\), or prove that no correspondence of bounded bidegree can realize it. This is now the first unresolved geometric mechanism behind the Honda--Tate square.
