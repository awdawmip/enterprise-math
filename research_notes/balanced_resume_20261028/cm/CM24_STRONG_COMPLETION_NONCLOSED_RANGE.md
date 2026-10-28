# CM24: the actual strong-completion row cokernel is infinite dimensional

Status: author proof, pending independent review. This is a bounded supporting result for the previously open strong-completion comparison. It does not classify the strong horizontal kernel, its separated cohomology, or an explicit basis of its cokernel. No formal Task disposition or parent closure is claimed.

Author: EM-DIRECT-38A864; activity RA-BALANCE-CM-20261028-38A864. This is source-exposed direct TASK_RESEARCH under the observed activity registration, with no claim or formal execution binding. Root supplies control and publication, not a mathematical vote.

## 1. Exact ring, connection, and conclusion

Keep the original prime p congruent to 13 or 19 modulo 24, the complete unramified DVR O with perfect residue field k, uniformizer p, and fraction field K. Put

    S=4r^3-3r, f=1-r^2, q=4r^2-1, P=fq,
    D=(2P)^(-1) [[2S-1,1],[4S-5,-(2S-1)]],
    A=O[r,f^(-1),q^(-1)],
    Ahat=lim_n A/p^n A,
    Rhat=Ahat[1/p].

This is the p-adic completion of the indicated localized algebra, followed by inversion of p. It is not a Laurent-series ring by definition. Let X=Rhat^(1x2), with unit lattice X0=Ahat^(1x2), and consider the continuous K-linear operator

    L:X -> X,  h |-> dh/dr+hD.

The following statements hold for this actual strong-completion operator:

1. `dim_K ker L <= 2`.
2. `L(X)` is not closed in the p-adic Banach topology of X.
3. The algebraic quotient `X/L(X)` is infinite dimensional over K. Its quotient topology is not Hausdorff.
4. Consequently inclusion from the previously established six-dimensional weak row cokernel cannot be surjective onto this strong row cokernel.

The dimension bound in (1) is not a determination of the kernel. The nonclosedness in (2) is stronger than merely saying that some weak primitive denominators grow: finite strong horizontal ambiguity is explicitly removed in the proof. The infinite-dimensional quotient in (3) is an algebraic statement, not just a topological defect. No claim about the dimension of the separated quotient `X/closure(L(X))` is made.

P000 and Heartbeat remain fixed. These p-adic algebras, Laurent coefficients and linear topologies are typed external mathematical models used for the CM connection; they are not native spatial axes or a new native plane. No physical dynamics or extra time dimension is inferred. All negative Laurent data used below are retained rather than projected away.

## 2. Exact reused source and additional work

The literal integral iterate theorem used here is:

`research_notes/owner_goal_20261017/cm24_integral_weak_primitive_denominators_cf1677/ACTUAL_INTEGRAL_WEAK_COKERNEL_UNBOUNDED_P_TORSION_AUTHOR_COMPOSE_V1.md`

at `56f5938da3f707c1d9db1b39afde124eac4634e3`, Git blob `58ec6ce156797557758cd868d21bcaf2c4b4776c`. This full original was fetched and read for the present argument. Its author is EM-FREE-CF1677. Its matched independent technical whole is preserved at the same commit under

`research_notes/owner_goal_20261017/reviews/cm24_integral_weak_torsion_nonauthor_4a56e9/ACTUAL_INTEGRAL_WEAK_COKERNEL_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md`,

Git blob `bb9c97fd9a4d0d780f9a0a264c53ccee96e6968b`, reviewer EM-P11-4A56E9. The monthly catalogue is CM-ALG-13. The present proof uses the original literal identities, rather than treating that prior review as a new vote on this extension.

Write R0=A^dagger. The original theorem constructs actual rows u_n,b_n in R0^(1x2), for every n>=1, such that

    L(u_n)=p^n b_n.                                         (1)

In the actual good-infinity coordinate z=1/r and its fixed frame, the second component has

    (u_n)_2=z^(1-p^n) v_n(z),
    v_n(z) in O[[z]],  v_n(0)=beta^n in O^*.                (2)

Here beta is the original good-fiber unit; its numerical value is not needed. The original proof derives (2) from the actual canonical Frobenius product and the precise transpose/frame transformation, not from its determinant alone. This is the entire construction of the u_n used here. We do not rerun or reprove the old Frobenius theorem or re-count its p-torsion result.

The earlier paper explicitly makes no strong-completion claim. New obligations here are: a faithful strong-completion Laurent embedding, finite strong horizontal dimension, independence of the approximate-horizontal residues modulo p, and the closed-range contradiction. Bounded current searches for CM24 strong-completion/nonclosed-cokernel results returned no matches; no exhaustive repository or literature novelty claim follows.

## 3. A faithful Laurent completion, used as an embedding

Define E0 to consist of formal Laurent sums

    sum_(j in Z) a_j z^j,
    a_j in O, and a_j -> 0 p-adically as j -> -infinity.

There is no positive-tail decay requirement. Equivalently,

    E0 = lim_n (O/p^n O)((z)).                              (3)

Addition and multiplication are well defined: for each coefficient of a product, the summands tend to zero in both directions, since the negative tail of one factor occurs at either end. Reduction modulo p is the ordinary Laurent-series field k((z)); the ring is p-adically complete and separated and has no p-torsion. Any element not in pE0 has a nonzero reduction in this field, whose inverse lifts to E0; a geometric-series correction then gives an inverse in E0. Thus E0 is a complete DVR with uniformizer p. Put E=E0[1/p], a field containing K.

There is a natural map at every finite level

    A/p^n A -> (O/p^n O)((z)),
    r |-> z^(-1),
    f^(-1) |-> z^2/(z^2-1),
    q^(-1) |-> z^2/(4-z^2).                                (4)

The right-hand denominators are units. The map is injective: before localization, a polynomial in z^(-1) has a unique coefficient expansion, even over O/p^n; after localization the displayed denominator units preserve this injectivity. The inverse limit gives an injection

    i:Ahat -> E0,

and each reduction modulo p^n remains injective. Hence i preserves the p-adic lattice valuation exactly. This proves the required embedding; it does not identify Ahat with all of E0 and does not interchange localization with completion.

The weak completion maps naturally into Ahat. The old weak infinity expansion and (4) agree modulo every p^n: a weak presentation is p-adically convergent, and its reduction has only finitely many presentation terms. Thus (2) has the same coefficients in E0 as in its original weak annular interpretation. No assertion that every strong element converges on an analytic annulus is used.

The operator `d/dr=-z^2 d/dz` preserves E0 and is continuous for its p-adic norm, because the integer coefficient multipliers have norm at most one. It agrees with the derivation on A and on its completion. Since the characteristic is zero, a Laurent sum killed by d/dz has all coefficients at nonzero exponents equal to zero. Therefore

    E^(d/dr)=K.                                            (5)

In particular, the differential constants have not silently enlarged when passing to the ambient field.

## 4. At most two strong horizontal rows

Embed X in E^(1x2). Over a differential field with constant field K, the K-vector space of solutions of a rank-two linear homogeneous system has dimension at most two. Here is the short argument to make the field dependency explicit.

If K-independent horizontal rows were E-dependent, take an E-dependence of minimal length and normalize one nonzero coefficient to 1. Differentiate the relation and use h'=-hD for every row. The matrix terms cancel. The resulting relation has one fewer potentially nonzero coefficient. Minimality forces every normalized coefficient to have derivative zero, so by (5) they lie in K. That contradicts K-independence. Thus K-independent horizontal rows are E-independent, and at most two fit in E^(1x2).

It follows that H=ker(L:X->X) has dimension at most two over K. This argument does not import the old weak kernel-zero theorem into a larger ring.

## 5. Infinitely independent approximate-horizontal residues

The rows u_n,b_n from section 2 lie in X0. Under the faithful reduction of section 3, the second component of u_n modulo p has lowest exponent precisely 1-p^n and nonzero coefficient beta^n mod p. These lowest exponents are pairwise distinct and strictly decreasing with n.

Consequently the classes

    u_n mod pX0,  n>=1,

are linearly independent over k. Indeed, in any nontrivial finite relation select the largest index with nonzero coefficient. Its second component has a strictly lowest Laurent exponent absent from every earlier term, so that coefficient cannot cancel. This is stronger than knowing that each row individually is p-primitive.

The exact norm statements are therefore

    ||u_n||=1,      ||L(u_n)||<=|p|^n.                     (6)

The norm of b_n need not equal one; its integrality is sufficient. The vectors form an infinite independent residue family while their images tend to zero. Merely observing the second part of (6) would not by itself exclude a nonzero strong kernel; that issue is addressed next.

## 6. Closed range would force an impossible finite residue space

X is a K-Banach space: Ahat is p-adically complete and separated, and every Cauchy sequence in Ahat[1/p] is bounded, so a common p-power rescales it into Ahat. Differentiation preserves A and all its p^n ideals, and D is integral in A. Hence L is bounded, with operator norm at most one.

Suppose for contradiction that L(X) is closed. H=ker L is closed, so X/H and L(X) are Banach spaces. The induced bounded bijection

    X/H -> L(X)

has bounded inverse by the Banach open-mapping theorem over the complete nontrivially valued field K. Thus there is a constant C such that

    dist(x,H) <= C ||L(x)||,  x in X.                     (7)

For all sufficiently large n, (6)--(7) imply dist(u_n,H)<1. By the definition of the infimum choose h_n in H with ||u_n-h_n||<1. Since the norm is p-discrete, u_n-h_n lies in pX0. The ultrametric inequality and ||u_n||=1 also give h_n in H0=H intersect X0. Hence

    u_n mod pX0 lies in the image of H0 in X0/pX0           (8)

for every sufficiently large n.

That image has k-dimension dim_K H<=2. To justify the lattice statement without compactness assumptions on the residue field, choose a K-basis of the finite-dimensional H. Equivalence of norms in finite dimension places H0 between two p-power multiples of the corresponding standard O-lattice. As an O-submodule of a finite free O-module, H0 is finite free of rank dim_K H. Moreover H0 intersect pX0=pH0, since p^(-1)h remains in H. Therefore its image modulo p has exactly that finite rank.

Equation (8) now places infinitely many k-linearly independent residue vectors from section 5 into a space of dimension at most two, a contradiction. Thus L(X) is not closed.

This proof does not assume spherical completeness of K, a compact unit ball, or the existence of a convergent subsequence of the u_n. It uses the Banach open-mapping theorem, finite-dimensional norm equivalence, and the DVR lattice property only.

## 7. Infinite algebraic cokernel and the failed weak comparison

For a bounded linear operator between Banach spaces over K, a range of finite algebraic codimension is closed. A proof avoids assuming the conclusion: if the codimension is d, choose y_1,...,y_d representing a quotient basis and consider the bounded surjection

    X direct-sum K^d -> X,
    (x,c) |-> Lx+sum c_j y_j.

The open-mapping theorem supplies bounded-size preimages. The coefficient vector c is unique for the image, because the y_j are independent modulo L(X). Thus the resulting linear quotient-coordinate map X->K^d is bounded, and L(X) is its closed kernel. This contradicts section 6. The codimension of L(X) is therefore infinite.

The quotient topology is non-Hausdorff precisely because the range is not closed. The established weak cokernel in the same row connection has K-dimension six. Its inclusion-induced map into this infinite-dimensional strong cokernel cannot be surjective. The result supplies a definite negative answer to a finite-dimensional strong extension of the weak normal form. It does not determine which of the six weak classes survive, nor the dimension or structure after taking closure of the image.

## 8. Reuse, harvest, and remaining research

The new conclusion is a same-connection composition of the original exact Frobenius rows with faithful Laurent completion and standard nonarchimedean functional analysis. The integral torsion construction and its original authorship remain unchanged. This is `RESULT_ONLY_STANDARD_COMPOSE` / `COMPOSE_APPLIED`, not a new general toolbox family. A fresh coverage lookup is retained as `strong_tool_coverage.json`.

No mathematical program, prime enumeration, numerical sample, or symbolic solver is used in this proof. The earlier finite-field decoder regression is a separate artifact and supplies no evidence for this p-adic theorem.

Remaining concrete boundaries are: determine dim_K H in {0,1,2}; identify closure(L(X)) and the separated cohomology; decide the kernel of the weak-to-strong cokernel map; and, if useful, exhibit a specified strong input outside the image. The present proof does not manufacture such an explicit input from the b_n, all of which already have weak primitives. Finite functional Y/Z/kappa evaluation and the relative-chain geometry remain separate open obligations. Selecting among them is a portfolio decision, not an automatic successor caused by this result.

Researcher-ID: EM-DIRECT-38A864 / TASK_RESEARCH
