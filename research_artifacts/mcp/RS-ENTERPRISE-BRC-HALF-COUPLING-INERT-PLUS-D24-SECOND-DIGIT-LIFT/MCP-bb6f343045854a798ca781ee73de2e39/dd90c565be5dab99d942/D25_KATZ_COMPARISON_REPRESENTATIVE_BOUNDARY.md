# D25: two comparison maps and a conditional representative boundary

Status: AUTHOR_PROOF_V1 / CONDITIONAL_MODEL / LIFT_OPEN, 2026-10-08. Author EM-ENTERPRISE-B078A6, session MCP-bb6f343045854a798ca781ee73de2e39, RA-8C8E44B2AA373F98BC5952A3, claim MCP-3d6d72356bcdfef82ab4cfc4, ER-7C265B422DC8E829AD44, authorized run RUN-252e05a5823d9e33ff848863 generation 1. This continues the same nonreleased Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7. It does not close LIFT/JT2 or identify the actual source normalization.

The first increment is a retained input: D25_LITERAL_DP_EIGENLIFT_OBSTRUCTION.md, Source 47bec72e89587dabc106e2604839806a962cc995, SHA256 6f11308313f7e5f18351cc8e45238d4b33ebf0f79e6e531f1de043c7266beb19. Driver's bounded audit is Source f05d1352651f93472bbd56fbc3aa234b6b1a93b4, SHA256 d76c9e8fa3152338c0c952cf536e7fc8a82cb66f1eec65504e0de604c7973c37. Neither is acceptance of the Task hard target. This note does not impose the impossible literal eigenrelation identified there.

## 1. What Katz actually supplies

Source: Nicholas M. Katz, *Crystalline cohomology, Dieudonne modules, and Jacobi sums*, author-hosted scan https://web.math.princeton.edu/~nmk/old/CrCohDModJacSum.pdf, 1191723 bytes, SHA256 547d6d6059d66b3809bed2d3f9c0301a62e07355bd994259ccc0533815b99da0. Printed page = PDF sequence page + 164 for the cited pages. The author personally inspected original page images 193, 194, 199; source-support agent /root/free_candidate_audit independently located and transcribed source pages without seeing our new proofs. Driver supplied the exact-title URL and requested distinct map/representative typing; this is source and review exposure, not independent proof validation.

For a commutative formal Lie group G over a characteristic-zero, Z-flat ring R, the one-variable description on printed p.193 is

    D_J(G/R) = { U(0)=0, dU integral,
                 U(X+_G Y)-U(X)-U(Y) in J[[X,Y]] }
                / { U in J[[X]], U(0)=0 },

for the divided-power ideal J. The ordinary D(G/R) has the same zero-constant and integral-differential conditions, but requires only an integral cocycle defect and divides by R[[X]] with zero constant. These primitive/cocycle conditions are additional numerator conditions; they cannot be discarded when invoking the group-theoretic comparison.

Theorem 5.1.6, p.194, explicitly says the natural map D_J -> D is not an isomorphism, with kernel and cokernel killed by J. For J=(p) call this natural map q; it takes the same formal primitive to its ordinary class.

Section 5.5, p.199, gives a different map. For perfect k and W=W(k), its formal-variety diagram (5.5.5) has

    w: CW(A(V tensor k)) -> H^1_DR(V/W;(p)),
    psi: CW(A(V tensor k)) -> H^1_DR(V/W),
    (1/p)F: H^1_DR(V/W;(p)) -> H^1_DR(V/W).

Here w is linear, psi is explicitly sigma-linear, both are isomorphisms, and the diagram commutes. Formulas (5.5.2) and (5.5.4) use the primitives sum(n>=0) tilde(a_-n)^(p^n)/p^n and sum(n>=0) tilde(a_-n)^(p^(n+1))/p^(n+1), respectively. For a p-divisible commutative formal Lie group G, diagram (5.5.7) restricts this to isomorphisms between M(G_0), D_p(G/W), and D(G/W), where M(G_0)=Hom_k-gp(G_0,CW) is the primitive subgroup. This is not a statement that the natural q is an isomorphism.

Further source locations supplied by the source-support reader: pp.202–204, Theorem 5.7.1 and diagram (5.7.3), relate crystalline cohomology of an abelian scheme over W(k), k algebraically closed, to D of its formal group, and label D -> formal de Rham as inclusion of primitive elements. Pages 205 and 210–212 contain comparison/restriction functoriality. Page 208, Corollary 5.7.8 proof, uses any pointed lift of X -> X^p and F(dX)=d(X^p+pY). These statements provide concrete comparison context; they have not been combined into an identification of the 2013 paper's particular companion. No inspected single sentence is claimed to define all such F operators as the exact power-substitution representative used below.

## 2. A fully specified formal model and its isomorphism

Let p be an odd prime, A=W(k) for perfect k, L=Frac(A), and sigma its Witt automorphism. Write

    M={ U in X L[[X]] : U' in A[[X]] },
    I=X A[[X]],     N=M/pI,     O=M/I.

Define the specific, zero-constant power-substitution representative and its map

    Ktilde(U)=U^sigma(X^p)/p,     K:N -> O, [U] -> [Ktilde(U)].   (1)

This choice is our explicit formal model. Calling it the actual comparison chosen by the 2013 source requires an additional identification, not merely the presence of an arrow labelled (1/p)F in Katz.

**Proposition.** K is a well-defined sigma-semilinear isomorphism of the indicated full formal quotients.

**Proof.** If U=sum(n>=1)u(n-1)X^n/n, with all u(n-1) in A, then

    Ktilde(U)=sum(n>=1)u(n-1)^sigma X^(pn)/(pn).

Its derivative is integral. Replacing U by U+pH, H in I, changes the output by H^sigma(X^p), in I, so (1) is well-defined. Additivity and sigma-semilinearity follow coefficientwise. If its output belongs to I, every coefficient [X^n]U divided by p belongs to A after applying sigma; hence U belongs to pI. This proves injectivity.

For any B=sum(m>=1)b(m-1)X^m/m in M, set

    U_B=sum(n>=1) sigma^(-1)(b(pn-1)) X^n/n.                    (2)

Then U_B belongs to M and Ktilde(U_B) is the part of B supported on exponents divisible by p. The remaining coefficients b(m-1)/m, p not dividing m, are integral, so B-Ktilde(U_B) belongs to I. This proves surjectivity. Explicitly, if B changes by H=sum h_m X^m in I, (2) changes by p sum sigma^(-1)(h_pn)X^n, which lies in pI. Thus (2) also proves the inverse is well-defined on O. QED.

In this full formal model the natural quotient q:N -> O is instead q([U])=[U]. It is different from K: q([X])=0 while K([X])=[X^p/p] is nonzero. The latter test concerns full formal quotients, without asserting [X] satisfies a particular G's primitive condition. The source independently distinguishes the two maps on primitive objects.

## 3. Conditional application retaining all class conditions

To apply the following statement to a particular CM companion one must supply all of these data:

1. A formal group G and a primitive ordinary class v in D(G/A), including its exact normalized CM eigenline. An arbitrary element of O is not enough to invoke Katz's group diagram.
2. An identification of the actual comparison with (1) on the chosen coordinate and coefficient ring, or an explicit alternative comparison formula. Under this identification choose u in D_p(G/A) with K(u)=v, retaining any specified class-level CM and Frobenius conditions on u and v. The full-formal proof alone does not establish this primitive restriction.
3. A concrete ordinary representative B0 of the same class v. The actual transported ordinary representative may be written B=Ktilde(U)+H0 with an integral H0 accounting for its prescribed regular terms, in particular its leading differential coefficient. Its same-class relation to B0 must be proved; it does not follow from q(u)=v, which has not been asserted.

Now let U be a representative of this fixed u and let eta be any element of A. Define

    U_eta=U+p eta X,       B_eta=Ktilde(U_eta)+H0.

Then

    [U_eta]=[U] in D_p,    B_eta=B+eta^sigma X^p,
    [B_eta]=[B]=v in D.                                        (3)

Indeed p eta X is a denominator element in D_p. Its differential is integral and its group cocycle defect is p eta (X+_G Y-X-Y), in pA[[X,Y]], so adding it preserves the primitive numerator too. The output change in (3) is integral, with integral ordinary cocycle defect. Thus both fixed primitive classes, and every equation formulated solely on those classes under already specified CM/Frobenius operators, remain exactly unchanged. This argument does not replace those conditions by ordinary cohomology alone and does not assert a strict representative-level eigen-equation.

Three normalization statements must be kept distinct:

    DP class and all class-level compatibility: unchanged;
    ordinary differential leading coefficient [X^0]dB_eta/dX: unchanged;
    DP differential leading coefficient [X^0]dU_eta/dX: changes by p eta.

For p>1, differentiation of the output correction starts at degree p-1, so ordinary leading normalization is preserved exactly. But exact DP leading normalization is not preserved. If an additional premise fixes [X]U as an exact element of A, this family with nonzero eta is excluded. If it fixes [X]U modulo p^2, it already fixes eta modulo p within this family. The result therefore does not prove ambiguity under those stronger representative-level assumptions.

## 4. Exact conditional coefficient observer and what is missing

Under the proved same-class hypothesis B-B0=F in I, define the previous D25 observer kappa=[X^p]F mod p. Equation (3) then gives

    kappa_eta = kappa + eta^sigma mod p.                       (4)

Since sigma induces an automorphism of k, this ranges over the full residue field. In the exact model (1), put u0=[X]U and h_p=[X^p]H0. Then the representative identity is

    [X^p](B-B0)=u0^sigma/p + h_p - [X^p]B0.                   (5)

The same-class premise ensures the right side is integral. Holding B0 and H0 fixed, its reduction modulo p requires u0 modulo p^2; the class in N records only u0 modulo p. Thus an exact comparison section, or at least this one additional DP leading digit together with the specified H0 and B0, supplies the missing datum for this observer in this model. Formula (5) is not a value of the actual source kappa.

This mechanism differs from arbitrarily adding an ordinary exact primitive while ignoring the divided-power class. Here the perturbation is zero in the fixed divided-power primitive class itself; its chosen (1/p)F representative produces the visible ordinary primitive. Conversely, transporting v by K^(-1) does not justify identifying U with the old B0 through q. These are different representative layers and different maps. No old kappa formula is applied without the explicit same-class bridge in Section 3.

The exact ordinary scalar c_p, if determined by a normalized CM eigenline in a fixed ordinary basis, is unchanged in this construction. We have not proved that c_p is ambiguous or computed it. We have proved a conditional limitation of class-level comparison data for a deeper representative coefficient; we have not proved that every full normalization premise of the actual 2013 construction has only class-level content. In particular, the paper says both omega and nu have leading coefficient 1 on p.27; whether that denotes the ordinary representatives, the D_p representatives, or a different comparison realization is an identification obligation, not a choice made here.

## 5. Validation, source exposure, and next unit

The results in Sections 2–4 are exact coefficient proofs and use no prime scan or target-product congruence. No program has been run for this addendum as of this frozen V1. Its own formal map is completely defined and its inverse is proved; source application remains conditional. The author personally checked the three decisive original Katz pages in Section 1, and read the fixed 2013 source pp.18–20 and 25–28. The external source support supplied original page locations and transcriptions, not this argument and not independent mathematical review.

Remaining concrete obligations: identify the actual comparison/representative normalization of the source companion; separately determine the ordinary CM scalar c_p from an exact period or CM-action normalization; prove the same-class bridge before computing actual kappa/Lcomp; retain the ramified/maximal-ideal boundary of the first increment. An executable ordinary-scalar entry is the E3 invariant differential's precise Picard–Fuchs period gauge (2013 Remark 7), followed by its fixed CM period normalization; this needs direct verification before substituting any familiar period coefficient. LIFT/JT2 and the parent remain OPEN, user_requested_stop=false. No native X6 propagation claim is made: this is explicitly external elliptic algebra over retained arithmetic labels.
