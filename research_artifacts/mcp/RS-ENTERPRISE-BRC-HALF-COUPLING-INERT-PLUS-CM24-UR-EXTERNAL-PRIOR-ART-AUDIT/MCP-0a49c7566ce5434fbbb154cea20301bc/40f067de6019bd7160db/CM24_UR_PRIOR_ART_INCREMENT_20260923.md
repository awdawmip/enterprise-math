# CM(-24) UR external-prior-art audit — bounded increment

Date: 2026-09-23
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-UR-EXTERNAL-PRIOR-ART-AUDIT
Publication: TP2-E133E3FC788A867C5BAD
Researcher: EM-DIRECT-01C0C9
Parent source pin consumed without replay: enterprise-math@1726c6804f791eab17ded699437fc8839c021278, research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md and its accepted Driver review.

## Frozen target and BRC carrier

For p=6m+1 with p mod 24 in {13,19}, retain the parent exact-rational carrier
B_0=1, B_{k+1}/B_k=((6k+1)(3k+1))/(36(k+1)^2), g_p=sum_{k=0}^{p-1}B_k, G_p=g_p/p, and the transverse Legendre/Hasse coordinate Q'_m(1/2). The exact successor certificate is

UR: G_p*(-6 Q'_m(1/2)) = 1 (mod p).

The observer/operation distinction is load-bearing: an observation that only g_p is divisible by p does not retain the divided coordinate G_p mod p needed by UR. No parent CM0/SIMPLE/JT2 reduction is reproved here.

## New exact finite-Clausen bridge

Let F(z) = _2F_1(1/6,1/3;1;z) = sum b_k z^k. Then B_k=b_k/2^k. By Clausen's product formula,

F(z)^2 = _3F_2(1/3,2/3,1/2;1,1;z).

At z=1/2 the kth term on the right is exactly

C_k = binom(2k,k)^2 binom(3k,k) / 216^k.

For p=6m+1 and 0<=k<p, the exact p-adic valuation profile of B_k is

v_p(B_k)=0 for k<=m; 1 for m<k<=2m; 2 for 2m<k<p.

Reason: denominators are p-units for k<p; the numerator first acquires p from 6j+1 at j=m and then from 3j+1 at j=2m, with no additional multiples of p in the range.

Now square g_p. For total degree n<p, the coefficient is exactly the nth Clausen coefficient, because all pairs i+j=n lie inside 0<=i,j<p. For every tail pair i+j>=p=6m+1, at least one of i,j is >2m, hence the corresponding B-factor has valuation at least 2. Thus the whole omitted tail is 0 mod p^2. Therefore, for every prime p=6m+1,

(*)  g_p^2 = sum_{k=0}^{p-1} binom(2k,k)^2 binom(3k,k)/216^k   (mod p^2).

This is an exact theorem-level bridge from the parent 2F1 truncation to the classical 3F2/binomial sum. It is not a proof of UR.

## Source classification 1: Zhi-Wei Sun, Conjecture A14(ii)

Source: Zhi-Wei Sun, Open Conjectures on Congruences, arXiv:0911.5665v59, Conjecture A14(ii), https://arxiv.org/abs/0911.5665 . A14(ii) gives the same C_k sum and predicts 0 mod p^2 when (-6/p)=-1, i.e. p mod 24 in {13,17,19,23}. On the present target p mod 24 in {13,19}, combine A14(ii) with (*) to obtain g_p^2=0 mod p^2, equivalently p|g_p. This loses the first divided p-adic digit: if g_p=pG_p, then g_p^2 is automatically 0 mod p^2 for every possible G_p mod p. Hence A14(ii) cannot determine G_p, still less the normalized reciprocal G_p*(-6Q'_m(1/2)).

Classification: PARTIAL_ANTECEDENT. Exact missing coordinate: the divided quotient G_p mod p plus its reciprocal normalization against -6Q'_m(1/2). Search silence is not novelty evidence. The 2011 compilation labels A14 in its Part A of conjectures; no claim is made here about global present-day theorem status solely from that label.

## Source classification 2: Zhi-Hong Sun 2011 CM/Legendre treatment

Source: Zhi-Hong Sun, Congruences involving binom(2k,k)^2 binom(3k,k) m^{-k}, arXiv:1104.2789v3, https://arxiv.org/abs/1104.2789 . The paper proves a general square relation between the binomial sum and P_[p/3](t), and a lift: if the Legendre value vanishes mod p then the binomial sum vanishes mod p^2. For m=216 it identifies the relevant t=sqrt(2)/2. Its CM argument explicitly uses an elliptic curve with CM by the order of discriminant -24. Theorem 4.5 proves the m=216 zero branch for p mod 24 in {17,23}; Remark 4.3 restates Z.W. Sun's full A14 prediction; for precisely p mod 24 in {13,19}, Conjecture 4.1 leaves P_[p/3](sqrt(2)/2)=0 mod p as conjectural in that paper.

This is a materially closer antecedent than a generic hypergeometric congruence because it shares the m=216 sum, the Legendre carrier, and the CM(-24) geometry. But on the exact target residue classes it does not supply the target-case theorem there, and in any event it does not retain the divided quotient G_p mod p or prove the transverse derivative reciprocal normalization required by UR.

Classification: PARTIAL_ANTECEDENT (strong geometric/method antecedent; target-class and quotient/derivative gaps explicit), not EXACT_DUPLICATE_OR_EQUIVALENT.

## Source classification 3: current mixed-parameter modular method

Source: Alex Shvets, Split-prime supercongruence at the mixed CM point (1/6,1/3;1), arXiv:2605.19773, https://arxiv.org/abs/2605.19773 . The paper studies coefficients A_n^mix = 108^n[z^n] _2F_1(1/6,1/3;1;z)^3 and proves a p^4 coefficient supercongruence for p=1 mod 3, using a Gamma_0(3)/Cartier-Hecke framework attached to j=0. This overlaps the hypergeometric parameters and split-prime arithmetic but is not an evaluation at z=1/2, not the discriminant -24 Hasse zero/derivative carrier, and not the G_p reciprocal certificate.

Classification: ADJACENT_METHOD.

## Exact validation

A deterministic exact modular regression was run on every target prime p<2000: 77 primes total, 40 with p mod24=13 and 37 with p mod24=19. For every prime, the valuation profile above was checked for all 0<=k<p, g_p was computed modulo p^2 by the exact recurrence, the 216-binomial sum was computed directly modulo p^2, and (*) held with zero failures. The inherited target divisibility p|g_p and the corresponding 216-sum zero mod p^2 also had zero failures. This regression is falsification evidence only; the proof of (*) is the finite Clausen-plus-valuation argument above, and neither the regression nor the source search proves UR or historical novelty.

## Source boundary and next unresolved unit

Authoritative identity source: NIST DLMF §16.12.2 (Clausen formula), https://dlmf.nist.gov/16.12 . External literature search was bounded to exact parameter/residue/CM(-24)/Legendre/216-binomial and supersingular derivative terms. Queries included A14(ii), the exact 216 binomial sum, (1/6,1/3;1;1/2), discriminant -24 + Hesse/Legendre + supersingular, Q'_m(1/2), Gross-Koblitz/Jacobi-sum and p-adic Gamma variants.

Current unfinished unit: search theorem-level CM(-24) Hasse-derivative, Dwork/unit-root, finite-field Jacobi-sum/Gross-Koblitz, and p-adic Gamma literature for an identity that retains the divided first p-adic digit G_p mod p and translates bidirectionally to G_p*(-6Q'_m(1/2))=1 on p mod24 in {13,19}. Do not infer novelty if no match is found.
