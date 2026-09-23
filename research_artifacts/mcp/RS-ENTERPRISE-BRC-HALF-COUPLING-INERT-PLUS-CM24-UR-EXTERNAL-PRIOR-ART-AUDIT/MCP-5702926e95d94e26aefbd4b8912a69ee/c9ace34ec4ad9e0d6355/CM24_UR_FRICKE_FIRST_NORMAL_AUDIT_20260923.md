# CM(-24) UR prior-art audit — exact Fricke derivative translation and level-3 first-normal antecedent

Date: 2026-09-23
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-UR-EXTERNAL-PRIOR-ART-AUDIT
Publication: TP2-E133E3FC788A867C5BAD
Researcher: EM-DIRECT-AE0AE8
Session: MCP-5702926e95d94e26aefbd4b8912a69ee
Claim: MCP-818d06b9b91f91b46b4c3f3f
Run request: resume-20260923T013100Z-15
Authority/head checked before upload: enterprise-math main 0b024d8b8be71add2d0db47c2d1256d2f95e73f3.

## Frozen carrier consumed without replay

For p=6m+1 with p mod 24 in {13,19}, retain the proved parent identities
H_m(z) = _2F_1(-m,-2m;1;z) = Q_m(1-z) in F_p[z],
Q_m(1/2)=0, Q'_m(1/2) != 0,
and the successor certificate
UR: G_p*(-6 Q'_m(1/2)) = 1 (mod p), where G_p=g_p/p mod p.
The preceding checkpoint also proved that these target CM(-24) fibers are supersingular and cannot carry an ordinary slope-zero Dwork unit root. None of those units is reproved here.

## 1. Sakai's level-3 Fricke supersingular polynomial matches the frozen hypergeometric carrier exactly

Source: Yuichi Sakai, 'On modular solutions of fractional weights for the Kaneko-Zagier equation for Gamma_0^*(2) and Gamma_0^*(3)', Ramanujan Journal 37 (2015), published 2014-06-17, https://link.springer.com/article/10.1007/s11139-014-9563-x . Definition 1 gives, for p congruent to 1 mod 6,

S_p^(3A)(X) = X^m * F_Fp(1/6,1/3;1;108/X),  m=floor(p/6)=(p-1)/6.

For 0<=k<=m, coefficientwise in F_p,
(-m)_k(-2m)_k/(k!)^2 = (1/6)_k(1/3)_k/(k!)^2,
because -m=-(p-1)/6 = 1/6 mod p and -2m=1/3 mod p. At k=m+1, (1/6)_{m+1} contains the factor m+1/6=p/6=0 mod p, so the finite-field hypergeometric branch terminates. Therefore the Sakai branch is exactly

S_p^(3A)(X) = X^m H_m(108/X)  in F_p[X].   (FRICKE-TRANSPORT)

This is not merely a shared-parameter analogy: it is a coefficientwise equality with the frozen terminating polynomial.

## 2. New exact transverse derivative identity at X=216

Put z=108/X. Differentiate FRICKE-TRANSPORT:
S'(X)=X^(m-1)[m H_m(z)-z H'_m(z)].
At X=216, z=1/2. The inherited CM0 gives H_m(1/2)=Q_m(1/2)=0, while H_m(z)=Q_m(1-z) gives H'_m(1/2)=-Q'_m(1/2). Hence

S_p^(3A)'(216) = (216^(m-1)/2) Q'_m(1/2)  (mod p).   (D216)

Since SIMPLE proves Q'_m(1/2) != 0, 216 is a simple root of Sakai's level-3 Fricke supersingular polynomial on every target prime. Thus the entire derivative side of UR has an exact pre-existing modular coordinate:

-6 Q'_m(1/2) = -12*216^(1-m) S_p^(3A)'(216),
so

UR  <=>  G_p * S_p^(3A)'(216) = -216^(m-1)/12  (mod p).   (UR-FRICKE)

This is a strictly smaller prior-art audit target: after this identity, an exact duplicate need not rediscover the transverse derivative; it must identify the divided first p-adic digit G_p and its normalized pairing with the Fricke supersingular derivative.

A deterministic exact modular regression checked D216 on all 77 target primes p<2000 (40 of class 13 mod24, 37 of class 19 mod24), with zero failures. This regression is falsification evidence only; D216 is proved symbolically above.

Classification: SAKAI_LEVEL3_FRICKE_SUPERSINGULAR_POLYNOMIAL = PARTIAL_ANTECEDENT_DERIVATIVE_SIDE_EXACT. It does not provide G_p or UR-FRICKE.

## 3. Betina-Lecouturier already supply first-normal p-adic supersingular geometry at full level 3

Source: Adel Betina and Emmanuel Lecouturier, 'On the p-adic periods of the modular curve X(Gamma_0(p) intersect Gamma(2))', arXiv:1611.01044v3, https://arxiv.org/abs/1611.01044 . Their Theorem 1.1 expresses the residual diagonal Manin-Drinfeld pairing at a supersingular level-2 point as
p * product_{k!=i}(lambda_i-lambda_k)^(-(p+1))
modulo principal units. Crucially for the present residue lane, their Remark 1 states that an analogue holds for N=3 when p congruent to 1 mod3, and Appendix 7.2 constructs a full-level-3 Hauptmodul H and states that the analogue of Theorem 1.1 follows with lambda replaced by H. Our target p=6m+1 is always 1 mod3.

If P_H(T)=product_j(T-H_j) is the corresponding supersingular H-polynomial, the diagonal factor is therefore the inverse (p+1)-power of P_H'(H_i), multiplied by p, in the residual pairing. This shows that 'p times an inverse supersingular derivative norm' is established level-3 p-adic period geometry, not a new mechanism created by UR.

A companion source makes the divided first-normal nature explicit at level 2: Betina-Lecouturier, 'Congruence formulae for Legendre modular polynomials', arXiv:1704.06941, https://arxiv.org/abs/1704.06941 . For the Legendre p-th modular polynomial F_p(X,Y), they define
R(X)=F_p(X,X^p)/p in Z[X]
and give its value at supersingular lambda, relating it to the same Manin-Drinfeld pairing and, for F_p-rational supersingular lambda, to a CM lift. Their Taylor expansion has p R(beta) as the first nonzero normal term at the supersingular point.

Classification: BETINA_LECOUTURIER_SUPERSINGULAR_FIRST_NORMAL_GEOMETRY = STRUCTURAL_ANTECEDENT. It substantially narrows any novelty claim about dividing by p at a supersingular modular point.

However, it is NOT an exact duplicate of UR-FRICKE. The cited N=3 period theorem uses a full-level-3 Hauptmodul H on Gamma(3)-type moduli, whereas Sakai's S_p^(3A) uses the Fricke Hauptmodul for Gamma_0^*(3). The cited papers do not supply a checked source-level map taking their divided modular/period coordinate to this task's G_p=g_p/p, nor the exact constant -216^(m-1)/12 in UR-FRICKE. No such map is inferred from shared level number alone.

## 4. BRC carrier/observer audit

Population/branches retained: p mod24 =13 and 19 remain labeled; both lie in p=1 mod6 and p=1 mod3.
Exact carrier retained: {G_p mod p, Q'_m(1/2), S_p^(3A)'(216), CM(-24) provenance, full-level-3 H provenance, operation/normalization}.
Exact composition proved: Q' <-> S_p^(3A)'(216) via D216.
Composition NOT proved: Betina-Lecouturier H-period/divided-modular coordinate <-> G_p.
Information-loss guard: a zero-order supersingular polynomial only locates X=216 and cannot recover G_p; a derivative-only antecedent still cannot recover the divided p-adic digit. Conversely, a generic first-normal p-adic period cannot be identified with G_p without a coordinate map and normalization proof.

BRC_REUSE_RESOLUTION = COMPOSE_APPLIED for the frozen H_m/Q_m transport with Sakai's supersingular Fricke polynomial; REUSE_APPLIED for Betina-Lecouturier as a typed first-normal antecedent; no false cross-coordinate quotient is taken.

## 5. New frontier

Completed here:
- exact source-level identification S_p^(3A)(X)=X^m H_m(108/X) on p=1 mod6;
- exact derivative identity D216 and simple Fricke root at X=216;
- exact equivalent reformulation UR-FRICKE;
- source-backed classification that level-3 p-adic period theory already contains p-scaled inverse supersingular derivative norms.

Smallest unresolved unit: derive or refute a source-level coordinate bridge from the Gamma(3) / full-level-3 first-normal invariant (or an equivalent Gross-Koblitz/Jacobi/p-adic-Gamma object) to G_p=g_p/p at the CM(-24) Fricke point. The bridge must preserve the exact normalization in UR-FRICKE. If the full-level-3 H-to-Fricke quotient map changes local degree or branches, retain that ramification/provenance rather than identifying derivatives naively. Search silence is not novelty evidence.
