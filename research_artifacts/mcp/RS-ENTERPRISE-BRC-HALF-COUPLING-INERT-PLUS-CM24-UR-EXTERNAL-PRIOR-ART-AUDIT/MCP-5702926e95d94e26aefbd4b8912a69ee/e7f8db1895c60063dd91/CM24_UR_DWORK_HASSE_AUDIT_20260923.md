# CM(-24) UR prior-art audit — Dwork/Hasse supersingular exclusion increment

Date: 2026-09-23
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-UR-EXTERNAL-PRIOR-ART-AUDIT
Publication: TP2-E133E3FC788A867C5BAD
Researcher: EM-DIRECT-AE0AE8
Session: MCP-5702926e95d94e26aefbd4b8912a69ee
Claim: MCP-818d06b9b91f91b46b4c3f3f
Run request: resume-20260923T013100Z-15
Source authority checked before upload: enterprise-math main aa895b880ebc259e91f97506ef2fc63b8cd1842b.

## Frozen frontier consumed without replay

For p=6m+1 with p mod 24 in {13,19}, retain the parent exact-rational carrier
B_0=1, B_{k+1}/B_k=((6k+1)(3k+1))/(36(k+1)^2), g_p=sum_{k=0}^{p-1}B_k, G_p=g_p/p, and Q'_m(1/2). The exact target certificate is

UR: G_p * (-6 Q'_m(1/2)) = 1 (mod p).

The verified predecessor checkpoint already proved the finite Clausen mod-p^2 bridge, classified Sun A14(ii) and Zhi-Hong Sun 2011 as partial antecedents, Shvets 2026 as adjacent method, and checked 77 target primes below 2000. None of those units is repeated here.

BRC carrier for this audit is therefore not Boolean supersingularity and not g_p mod p. The smallest currently adequate observer retains at least {CM(-24) fiber / Hasse-zero status, divided p-adic digit G_p mod p, transverse tangent Q'_m(1/2) mod p, normalization/provenance}. Any literature interface that factors through only zero-order Hasse data loses information needed by the future operation G_p*(-6Q'_m).

## New theorem-level exclusion: the target cannot be an ordinary unit-root specialization

For every target prime p congruent to 13 or 19 mod 24, the quadratic character (-6/p) is -1. Explicitly:
- p=13 mod 24: (-1/p)=+1, (2/p)=-1, (3/p)=+1, so (-6/p)=-1;
- p=19 mod 24: (-1/p)=-1, (2/p)=-1, (3/p)=-1, so again (-6/p)=-1.
Thus p is inert/non-split in Q(sqrt(-6)), the CM field underlying the discriminant -24 fiber already pinned by the frozen parent source.

Deuring's reduction criterion says that for a CM elliptic curve with good reduction at p>=5, reduction is supersingular iff p does not split in the CM field. A modern self-contained statement is M. Mula, N. Murru, F. Pintore, 'On random sampling of supersingular elliptic curves', Ann. Mat. Pura Appl. 204 (2025), Theorem 4.1, published 2024-12-02, https://link.springer.com/article/10.1007/s10231-024-01528-x . Hence the target CM(-24) reductions are supersingular.

For p>3 and E/F_p supersingular, #E(F_p) congruent to 1 mod p, so a_p=p+1-#E(F_p) is divisible by p. Hasse's bound gives |a_p|<=2 sqrt(p)<p for p>=5, hence a_p=0. Therefore the p-Frobenius polynomial is T^2+p. Its two roots have p-adic valuation 1/2. In particular there is no slope-zero / p-adic unit Frobenius root at the target fiber.

Consequently an ordinary Dwork unit-root formula cannot itself be an exact duplicate/equivalent of UR on these target fibers. Any Dwork/Frobenius prior-art route that is genuinely equivalent to UR must include a supersingular continuation/regularization, or a first normal derivative/residue at the Hasse-zero divisor, and must recover the divided coordinate G_p together with the transverse normalization.

## Primary Dwork/Hasse source classification

F. Beukers and M. Vlasenko, 'Dwork Crystals III: From Excellent Frobenius Lifts Towards Supercongruences', IMRN 2023, https://academic.oup.com/imrn/article/2023/23/20433/7174376 , Theorem 1.1 assumes the relevant Hasse-Witt matrix is invertible; the paper explicitly identifies this with Cartier being an isomorphism mod p and works over rings in which the relevant Hasse-Witt determinant/truncation is inverted. Since the target is supersingular/Hasse-zero, that ordinary-locus hypothesis fails at the target point.

Classification: DWORK_ORDINARY_UNIT_ROOT_FAMILY = ADJACENT_METHOD / STRUCTURALLY_EXCLUDED_AS_EXACT_DUPLICATE_AT_TARGET_WITHOUT_SUPERSINGULAR_REGULARIZATION. This is a theorem-level domain exclusion, not a novelty claim and not an assertion that no supersingular Dwork derivative theorem exists elsewhere.

Alan Adolphson and Steven Sperber, 'Hasse invariants and mod p solutions of A-hypergeometric systems', arXiv:1209.2448 (2012; JNT 2014), https://arxiv.org/abs/1209.2448 , states that the Legendre-family Hasse invariant is a mod-p Gaussian hypergeometric solution and more generally represents Hasse invariants by mod-p A-hypergeometric solutions. This is relevant zero-order Hasse/supersingular-locus information, but the theorem statement does not provide the divided first p-adic digit g_p/p or the target reciprocal normalization against Q'_m(1/2).

Classification: HASSE_MOD_P_HYPERGEOMETRIC_FAMILY = PARTIAL_ANTECEDENT_ZERO_ORDER_ONLY. The information-loss witness is exact: if g_p=pG_p, the reduction g_p mod p is 0 for every possible G_p mod p, so a zero-order mod-p observer cannot distinguish the UR value.

## BRC information audit

Retained: target residue branch (13 versus 19 mod 24), CM(-24) provenance, inert/supersingular status, G_p as divided p-adic digit, Q'_m(1/2) as transverse tangent, and the multiplication/normalization operation defining UR.

Erased by ordinary Hasse-only observer: G_p and all first-normal p-adic information.
Erased/undefined by ordinary unit-root observer at target: the slope-zero Frobenius eigenline itself; at supersingular target the two slopes are 1/2.

Thus the next literature query must be typed to the missing carrier, not merely to 'unit root' or 'Hasse invariant': look for supersingular Frobenius derivative / first Hasse-normal coefficient / divided hypergeometric truncation / Gross-Koblitz-Jacobi-p-adic-Gamma formula that retains a first p-adic digit at the CM(-24) point and supports a bidirectional translation to UR.

## Disposition

CM24_TARGET_INERTNESS_ON_13_19_MOD24 = PROVED.
CM24_TARGET_SUPERSINGULARITY_BY_DEURING = PROVED_FROM_FROZEN_CM_IDENTIFICATION_PLUS_STANDARD_THEOREM.
NO_SLOPE_ZERO_FROBENIUS_ROOT_AT_TARGET = PROVED.
ORDINARY_DWORK_UNIT_ROOT_AS_IS_EXACT_DUPLICATE = EXCLUDED.
ADOLPHSON_SPERBER_HASSE_MOD_P = PARTIAL_ANTECEDENT_ZERO_ORDER_ONLY.
EXACT_SUPERSINGULAR_DERIVATIVE_OR_GROSS_KOBLITZ_EQUIVALENT = STILL_UNRESOLVED.

No claim of historical novelty is made from search silence. No ordinary formula is promoted across its failed Hasse-Witt hypothesis.
