# J1 external prior-art audit — exact finite-field Joukowski/Dickson image boundary

Task: RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT
Publication: TP2-39ACFC69F85D8661CFBF
Researcher: EM-DIRECT-5DD273
Run: open-20260923-0602-c71d-23
Source base consumed: 56ad8c023de193aefe3b0494e04d38c31e1af6bd

## Frozen input consumed, not re-proved

The accepted Driver review fixes J1 as follows. For odd q with q not dividing 2s,
Lambda_s(a) = -s a - 1/(2a),
and Lambda_s(a)=Lambda_s(b) iff a=b or ab=(2s)^(-1). Thus the fibers are the orbits of a -> c/a with c=(2s)^(-1), and
|Im Lambda_s| = (q + eta(c))/2.
The Enterprise saturation statement is separately typed as Im Lambda_s subseteq J_s. The q|s boundary remains outside the formula.

Authoritative frozen evidence:
driver_reviews/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260829.md
blob sha1 80b550aa21d0695d0ca9e4853bd707319f6413e4
sha256 5f08f144d6b4729d661556062411698739b1e4d077519db0dcae6f7e6728e6d5

## Previously established unpublished comparison preserved

Set u=sa and alpha=s/2. Then
Lambda_s(a)=-(u+alpha/u).
The already-derived fiber identity is
u+alpha/u = v+alpha/v
iff
(u-v)(1-alpha/(uv))=0,
so the nontrivial pairing is uv=alpha, which is the same as ab=(2s)^(-1).
Fixed points satisfy u^2=alpha. This comparison was a research draft only and was not previously treated as canonical Source progress.

## New authoritative external antecedent

Yanbin Zheng, Xi-Yu Wang, Shudi Yang, Qiang Wang,
"Rational functions of degree two or three that are many-to-one on the projective line",
Finite Fields and Their Applications, article 102901,
DOI 10.1016/j.ffa.2026.102901.
Publisher page: https://www.sciencedirect.com/science/article/pii/S1071579726001127
DOI: https://doi.org/10.1016/j.ffa.2026.102901

Chronology relevant to the audit: the manuscript records Received 20 Oct 2025, revised 4 Apr 2026, accepted 27 Jul 2026; author-posted full text was publicly available on 6 Aug 2026. The journal volume is issue-dated February 2027, so the evidence should be described as an accepted/publicly available 2026 article rather than pretending the 2027 volume date had already elapsed at this audit.

Theorem 3.1 treats
g(x)=(a x^2+b x+c)/(d x+e)
and defines A=a^2 e^2+a c d^2-a b d e. Equation (3.2) gives an explicit linear-fractional/affine normalization to
x + alpha/x,
with alpha=A/(a^2 d^2).
For odd q, the theorem proves:
1. if alpha is nonsquare, x+alpha/x is 2-to-1 on P^1(F_q);
2. if alpha is square, the only exceptional domain points are the two roots of x^2=alpha, and the map is 2-to-1 off them;
3. in the square case the paper explicitly computes the projective value-set cardinality as (q+3)/2.
The proof itself gives the same collision kernel F(x,y)=xy-alpha.

This is substantially stronger than the previous generic Dickson/Joukowski resemblance: it is an external finite-field theorem for the same rational normal form and the same involution.

## Exact affine value-set consequence

Let
f_alpha(u)=u+alpha/u,  alpha in F_q^*, q odd.

If eta(alpha)=-1, Theorem 3.1 says f_alpha is 2-to-1 on P^1(F_q). Hence its projective image has (q+1)/2 points. The value infinity has exactly the two projective preimages 0 and infinity. Restricting the domain to F_q^* and the target to F_q therefore removes exactly that projective image value:
|f_alpha(F_q^*)|=(q-1)/2.

If eta(alpha)=+1, the two roots +/-sqrt(alpha) are the two exceptional singleton fibers and have distinct values because q is odd. The remaining q-1 projective domain points form 2-element fibers, so the projective image has
(q-1)/2 + 2 = (q+3)/2,
as also written explicitly in the paper. Again removing the unique infinity image coming from {0,infinity} gives
|f_alpha(F_q^*)|=(q+1)/2.

Therefore, uniformly,
|{u+alpha/u : u in F_q^*}| = (q+eta(alpha))/2.

For J1, alpha=s/2 and c=(2s)^(-1). Since
alpha/c=(s/2)*(2s)=s^2,
eta(alpha)=eta(c). Domain scaling u=sa and target negation are bijections. Hence the external theorem reproduces exactly
|Im Lambda_s|=(q+eta((2s)^(-1)))/2
and its nontrivial two-point fiber involution.

Validation range: odd prime-power q and s nonzero in F_q, equivalently the accepted J1 assumption q not dividing 2s. No prime-field-only Legendre notation is used; eta denotes the finite-field quadratic character.

## Prior classical context retained

1. Encyclopedia of Mathematics, "Dickson polynomial":
https://encyclopediaofmath.org/wiki/Dickson_polynomial
It records the classical functional equation based on x=u+a/u. This remains the historical/name-level Dickson antecedent.

2. W.-S. Chou, J. Gomez-Calderon, G. L. Mullen,
"Value sets of Dickson polynomials over finite fields",
Journal of Number Theory 30(3) (1988), 334-344,
DOI 10.1016/0022-314X(88)90006-6.
This establishes the mature finite-field value-set context for Dickson polynomials, but it is not needed to derive the exact rational-map count above.

3. S. Ugolini,
"On the iterations of certain maps X -> K (X+X^{-1}) over finite fields of odd characteristic",
Journal of Number Theory 142 (2014), 274-297,
DOI 10.1016/j.jnt.2014.02.024.
This is an older direct finite-field study of the same x+x^{-1} rational-map family and remains a structural/dynamical antecedent.

## Refined duplication classification

The J1 rational-map kernel — normalization to u+alpha/u, collision involution uv=alpha, square/nonsquare fixed-point behavior, and the resulting affine image-cardinality formula — now has an exact external antecedent. At subclaim granularity this should be classified as EXACT_DUPLICATE under the explicit domain scaling/target negation and the projective-to-affine restriction above.

The whole Enterprise J1 row should remain PARTIAL_ANTECEDENT at this stage. The external theorem does not contain the project-defined object J_s or the additional saturation/recombination statement Im Lambda_s subseteq J_s. No novelty is inferred from that absence.

This replaces the weaker draft boundary "J1 only structurally resembles a classical Joukowski/Dickson map" with the sharper boundary:
- exact external duplication: rational-map/fiber/image-cardinality kernel;
- still-unresolved Enterprise-specific layer: the J_s saturation/recombination criterion.

## Completed unit

The previously open question "find an authoritative finite-field theorem yielding the exact image formula for u+alpha/u" is closed positively by Zheng et al., Theorem 3.1 plus its explicit square-case value-set count.

## Next unresolved unit

Determine whether the remaining Enterprise-specific J1 saturation layer Im Lambda_s subseteq J_s has a material external antecedent under the exact project definition of J_s. If no exact/structural match is found in the bounded authoritative set, record only NO_MATERIAL_MATCH_IN_AUDITED_SET for that sublayer; do not infer novelty. After the J1 boundary is closed, continue to the next unclassified H/J/C row without replaying J1.
