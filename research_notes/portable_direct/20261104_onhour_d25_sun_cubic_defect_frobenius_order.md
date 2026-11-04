# D25 — Sun truncated-square third digit: Frobenius/derivative-order observer (2026-11-04)

Status: EXACT ALGEBRAIC REDUCTION / FINITE EXACT CHECKED / AUTHOR-SIDE PORTABLE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific input c47e13e4aba0e006366f989d6334d443f6333ae3.
Research lane: chatgpt-research-onhour-enterprise-math-20260923, separate from maintenance. This note is not a native Source checkpoint, Result, H0/B0 native computation, or reviewed theorem.

## Exact full-source setting

For p>=5 prime and alpha in Z_p, let c_k=binom(alpha,k)binom(-1-alpha,k), h_k=binom(2k,k)c_k,
F(X)=sum_{0<=k<p} c_k X^k, H(t)=sum_{0<=k<p} h_k t^k, t=X(1-X).
Zhi-Hong Sun 2015 Theorem 2.2 gives the *coefficientwise polynomial* congruence
F(X)^2-H(X(1-X))=p^2 E_full(X) over Z_p[X]; write E=E_full mod p.
At alpha=-1/3 and x_a=(2+s)/4, s^2=2, t=1/8, H is the FULL original unweighted 216 sum A=sum_{0<=k<p} binom(2k,k)^2 binom(3k,k)/216^k.
At alpha=-1/4 and x_b=(3+2s)/6, t=1/36, H is the FULL original unweighted 2304 sum B=sum_{0<=k<p} binom(2k,k)^2 binom(4k,2k)/2304^k.
M_A=sum k a_k, M_B=sum k b_k; W=A+6M_A, V=B+8M_B. No high-valuation layer is dropped.

## Theorem I: degree-p cancellation and finite-tail certificate

For every p>=5 and alpha in Z_p, the mod-p polynomial E(X) is divisible by X^(p+1), with deg E<=2p-2.
Proof: the exact infinite Clausen/Legendre formal series identity
(sum_{k>=0} c_k X^k)^2 = sum_{k>=0} h_k X^k(1-X)^k
implies coefficients below degree p of the truncated difference vanish exactly. The coefficient at degree p is
[X^p](F^2-H(X(1-X)))=(binom(2p,p)-2)c_p.
The generalized binomial c_p is p-integral, and Wolstenholme's binomial congruence binom(2p,p)=2 mod p^3 gives this coefficient zero mod p^3. Sun's mod-p^2 polynomial congruence then yields E=X^(p+1) Q, deg Q<=p-3.
For p<=j<=2p-2 the *exact* omitted-tail identity is
[X^j](F^2-H(X(1-X))) =
sum_{k=p}^j (-1)^(j-k) binom(k,j-k) h_k - 2 sum_{k=p}^j c_k c_{j-k},
with binom(k,j-k)=0 if j-k>k. This supplies the coefficient-level p^2 defect from original tail sources.

## Theorem II: complete third-digit identity, including weighted derivatives

Work in R=(Z/p^3Z)[s]/(s^2-2). Let T_a=2t_a/(1-2x_a)=-s/4, T_b=-s/24.
For a,b the two alpha values, evaluation of Sun's polynomial remainder and differentiation *before* evaluation prove, modulo p^3:
A=F_a(x_a)^2-p^2 E_a(x_a), B=F_b(x_b)^2-p^2 E_b(x_b),
M_A=T_a F_a(x_a)F'_a(x_a)-(p^2/2)T_a E'_a(x_a),
M_B=T_b F_b(x_b)F'_b(x_b)-(p^2/2)T_b E'_b(x_b).
These are exact source-preserving identities (not new universal W=V). The derivative uses t'=1-2x, which is a unit.

If F_a(x_a),F_b(x_b) belong to pR, set U_a=F_a/p, U_b=F_b/p mod p. Then
(A-B)/p^2 = U_a^2-U_b^2-E_a(x_a)+E_b(x_b) mod p.
Let C=6T_aF_aF'_a-8T_bF_bF'_b. If additionally C belongs to p^2 R (the target-class first-moment signed pairing, not universally established), then
(W-V)/p^2 =
[U_a^2-U_b^2-E_a+E_b] + [C/p^2-3T_a E'_a+4T_b E'_b] mod p.
This isolates the missing signed terminal cancellation into period, truncation defect, period derivative, defect derivative with independent origin.

## Theorem III: Frobenius evaluation is NOT interchangeable with formal differentiation

For p=13 or 19 mod24, (2/p)=-1, so s^p=-s, x^p=1-x for x_a and x_b modulo p. Since E=X^(p+1) Q:
E(x)=x^p x Q(x)=t Q(x) mod p;
E'(x)=x^p(Q(x)+xQ'(x))=(1-x)(Q(x)+xQ'(x)) mod p.
Do not differentiate the *evaluated* identity x^p=1-x: formally (X^p)'=0 in char p, whereas (1-X)'=-1. The missing derivative term is an actual information loss when swapping Frobenius reduction and the observer.

The generalized Legendre symmetry F(X)=(-1)^r F(1-X) mod p^2, r=<alpha>_p (Z.-H. Sun 2014, Theorem 2.2), further implies, conditional on F(x)=0 mod p: U_a is scalar at both target classes; U_b is pure-s when p=13 mod24 and scalar when p=19 mod24. Under the same condition E(x) is scalar mod p, while E'(x) may have a nonzero s-component. These are external auxiliary quadratic observers, not authenticated native H0/B0 Frobenius.

## Executed exact evidence

Python standard-library checker separately constructs F^2 and H(X(1-X)) from ORIGINAL factorial coefficients modulo p^3, verifies zero coefficients through degree p, all polynomial divisions by p^2, evaluations, derivatives, weighted moments, and Frobenius for all 23 primes p<=500 in classes 13,19 mod24 (zero failures).

p | U_a^2-U_b^2 | E_b-E_a | D=(A-B)/p^2 | C/p^2 (scalar,s) | -3T_aE'_a+4T_bE'_b (scalar,s) | (6M_A-8M_B)/p^2
---|---:|---:|---:|---|---|---:
13 | 12 | 8 | 7 | (2,10) | (4,3) | 6
19 | 2 | 18 | 1 | (11,1) | (7,18) | 18
373 | 236 | 5 | 241 | (283,2) | (222,371) | 132

For p=373, 236+5=241 and (283,2)+(222,371)=(132,0) mod 373; 241+132=0. The s-components of the two derivative-source observers do not individually vanish: exact cancellation depends on retaining the truncated-square defect. These checks are finite; no all-prime W-V proof is claimed.

References: Zhi-Hong Sun, Note on super congruences modulo p² (2015), Thm 2.2, https://arxiv.org/abs/1503.03418 ; Zhi-Hong Sun, Generalized Legendre polynomials and related supercongruences, J. Number Theory 143 (2014), Thm 2.2, DOI 10.1016/j.jnt.2014.04.012; classical Wolstenholme binomial congruence.

## Next exact scientific action

Target universal elimination of one of four source-resolved observers [U_a^2-U_b^2, E_b-E_a, C/p^2, -3T_aE'_a+4T_bE'_b] via a coefficientwise WZ/Clausen/Green transport, testing the precise signed terms at p=13,19,373 before generalized proof. Independently discharge B-period vanishing and the 2:9 derivative pairing; retain frozen Delta_p-R_p, original G_p/h/Phi_xx observers, BRC information-loss audit and p=373 native H0/B0 benchmark #1559 as unmet.
Gateway em_status v0.6.11 checked 2026-11-04: research_authority_granted=false, CODE_UPGRADE_AVAILABLE, full_snapshot_verified=false. Original exact request onhour-d25-20261104-1702-continuation-read remains FAILED / SOURCE_TREE_SIZE_LIMIT files=20001/20000. No replay, role-bound mutation, CLAIM/run/Source checkpoint or Result. Three historical staging sources not adopted.