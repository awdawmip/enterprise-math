# D25 two-kernel cubic moment normal form and p^5 edge calibration

Date: 2026-11-03. TASK_RESEARCH author-side. Logical conversation: chatgpt-research-hourly-enterprise-math-20260923; distinct from maintenance chatgpt-hourly-enterprise-math-20260921. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3. AUTHOR-DERIVED / HAND-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

## The two original source kernels

Set b_k = C(2k,k)^2 C(3k,k)/216^k and c_k=(4k)!/((k!)^4 2304^k), with b_0=c_0=1. Their exact recurrences are

    b_(k+1)/b_k = A_b(k)/(36(k+1)^3),  A_b(k)=18k^3+27k^2+13k+2;
    c_(k+1)/c_k = A_c(k)/(576(k+1)^3), A_c(k)=64k^3+96k^2+44k+6.

The 2304 comparator is the one consumed by the sibling author result at Enterprise Math commit eeb6f882aae70ec0a2b37d74ea7b7f988ee1a9c4, which keeps the 216-to-2304 modulo-p^3 bridge a conjecture, and proves a separate -2p^3 last-weighted-term discrepancy modulo p^4.

## Theorem 1. Complete rational Gosper image, and exact three-moment normal form

For i=b,c set d_b=36, d_c=576 and T_i(S)(k) = A_i(k) S(k+1)/d_i - k^3 S(k). For polynomial P in Q[k], there is a rational function R(k) in Q(k) such that

    [f_(k+1)/f_k] R(k+1) - R(k) = P(k),  f=b or c,

if and only if P=T_i(S) for one unique S in Q[k], with R(k)=k^3 S(k). Every P decomposes uniquely into T_i(S)+u+vk+wk^2. This also holds integrally over Z[1/6].

Proof: Clear denominators: A_i(k)R(k+1)-d_i(k+1)^3 R(k)=d_i(k+1)^3 P(k). If R has poles, let z_- and z_+ be poles of minimal and maximal real part. The first forces A_i(z_--1)=0: z_- belongs to {1/2,1/3,2/3} for b or {1/4,1/2,3/4} for c. The second forces z_+=-1 (sole root of d_i(k+1)^3), a contradiction. Thus R is polynomial. Because A_i(-1) != 0, (k+1)^3 divides R(k+1), yielding R(k)=k^3S(k). The leading term of T_b(S) is -1/2 times the leading coefficient of S in degree deg(S)+3, and for T_c it is -8/9. This proves injectivity, and polynomial long reduction by top degree gives the unique remainder of degree <=2. Divisions involve only 2 and 3, proving the Z[1/6] assertion. QED.

Hence polynomial Euler/jet moments for either source have a three-dimensional quotient by exact single-index rational differences. Both original signed weights 6k+1 and 8k+1 represent nonzero quotient classes.

## Theorem 2. Finite boundary and universal Fermat quotient digit

For every integer N>=0 and polynomial S,

    sum_(k=0)^N T_i(S)(k) f_k = (N+1)^3 f_(N+1) S(N+1).

This telescopes termwise. For p>=5 prime and M_i,j=sum_(k=0)^(p-1) k^j f_k, S=1 gives the exact rational equalities

    -18 M_b,3 +27 M_b,2 +13 M_b,1 +2 M_b,0 =36 p^3 b_p;       (B216)
    -512 M_c,3 +96 M_c,2 +44 M_c,1 +6 M_c,0 =576 p^3 c_p.     (B2304)

Define q_p(a)=[a^(p-1)-1]/p (mod p), for a=216,2304. Then

    36 p^3 b_p == 2 p^3 -2 q_p(216) p^4 (mod p^5);
    576 p^3 c_p == 6 p^3 -6 q_p(2304) p^4 (mod p^5).

Proof: Exactly b_p=C(2p,p)^2 C(3p,p)/216^p and c_p=C(4p,p)C(3p,p)C(2p,p)/2304^p. The elementary p-block product and sum_(i=1)^(p-1) 1/i=0 (mod p) show C(mp,jp)=C(m,j) (mod p^2) for 0<=j<=m<=4, p>=5. Thus b_p=(1/18)[1-p q_p(216)] and c_p=(1/96)[1-p q_p(2304)] modulo p^2. Multiplication by 36p^3 and 576p^3 proves the formulas. QED.

For any S in Z[1/6][k], the arbitrary-weight exact telescoping boundary therefore has the p^4 reductions

    sum_(k=0)^(p-1) T_b(S)(k)b_k == (p^3/18) S(0) (mod p^4);
    sum_(k=0)^(p-1) T_c(S)(k)c_k == (p^3/96) S(0) (mod p^4).

These formulas yield boundary-aware evaluation of any polynomial original 216 or 2304 weight from its first three moments. The difference of the *two normalized cubic differential boundaries* is -4p^3 + [-2 q_p(216)+6 q_p(2304)]p^4 (mod p^5), distinct from the sibling's -2p^3 last-weighted-term difference.

## Theorem 3. Exclusion of rational one-index termwise 216-to-2304 scaling

If c_k/b_k were a rational function F(k) of k for all sufficiently large positive integers, then F(k+1)/F(k) tends to 1. The original ratio is A_c(k)/(16 A_b(k)), tending to 64/(16*18)=2/9. Contradiction. Thus a characteristic-zero p-independent rational *termwise* multiplier cannot transfer the 216 kernel into the 2304 kernel. This identifies a restricted class; finite two-index/parameter-dependent transformations remain available as candidates.

## Test, original mother and next precise unit

A Python standard-library integer checker generated the original coefficient recurrences modulo p^5 and passed all 301 primes from 5 through 2000 for both boundaries. Independent factorial/binomial endpoint evaluations passed for p=5,7,13,19,37,373. At p=373, q_p(216)=23, q_p(2304)=369; the two normalized boundaries are 6329803105841 and 464876458086 modulo p^5. These finite tests support the general algebraic derivation; they are not native H0/B0 or mathematical admission.

Next: construct a two-index or p-dependent 216-to-2304 creative-microscoping/WZ relation and reduce its separate original polynomial-weight sources to six base moments (three per kernel). Test p=13,19,373, original signed weights, the sibling's -2p^3 original-terminal difference and the distinct (2,6) cubic-boundary vector. A uniform p^3 bridge combined with the independently proved 2304 comparator would close the frozen scalar question W_216(p-1)=p (mod p^3) for p mod24 in {13,19}, equivalently Delta_p-R_p=0 (mod p).

Gateway 0.6.11 status on 2026-11-03: research_authority_granted=false, executor_binding_configured=false; upstream code gate UPSTREAM_CODE_REVIEW_REQUIRED, native control active quota 5/5. Read historical #6637 recovery and #6638 failed continuation; no reissue. Native Source claim/open/checkpoint/Result/admission not established. Keep previous service session, neutral staging, P000, ACTIVE world, frozen inputs, Research/maintenance separation and scheduled settings untouched. Control support #1558; unexecuted original p373 H0/B0 experiment support #1559.
