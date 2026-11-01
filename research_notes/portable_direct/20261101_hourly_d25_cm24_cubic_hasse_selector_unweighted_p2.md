# D25: CM(-24) cubic Hasse selector and universal unweighted 216 congruence

Date: 2026-11-01 +08. Status: AUTHOR-DERIVED / CLASSICAL-SUN-DEURING-DEPENDENT / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.
Research logical lane: `chatgpt-research-hourly-enterprise-math-20260923`; maintenance lane not used. Frozen scientific input `c47e13e4aba0e006366f989d6334d443` unchanged. This is an author-side portable mathematical artifact, not a native Source checkpoint, Result, authorized run, experiment or independent review.

## Theorem T1: previously open mod-p zero selector

Let p=6r+1 >= 7 be prime, Y_p(z)=sum_{k=0}^{p-1} ((1/6)_k (1/3)_k/(k!)^2) z^k and P_n the Legendre polynomial normalized P_n(1)=1. Choose t in an algebraic closure of F_p with 2t^2=1; either root gives the same value. Then

  Y_p(1/2) = P_{2r}(t) (mod p),

and this scalar is ZERO if and only if the Kronecker/Legendre symbol (-6/p)=-1. Equivalently it vanishes for exactly the classes p mod 24 in {13,19} among p=1 mod 6, and is nonzero in classes {1,7}. In particular the entire target 13/19 mod-p prerequisite of the earlier Hensel analysis is discharged.

Proof (precisely including the non-rational square root). Write m=3r=(p-1)/2. Let
  a(t)=3(4t-5), b(t)=2(2t^2-14t+11),
  H_p(t)=[X^(p-1)] (X^3+a(t)X+b(t))^m.
Zhi-Hong Sun (Acta Arith. 159, 2013), Eq. (1.5), gives for t in F_p:
  P_{floor(p/3)}(t) = -(p/3) sum_{x in F_p} LegendreSymbol(x^3+a(t)x+b(t);p) (mod p).
Since p=1 mod 3, (p/3)=1 and floor(p/3)=2r. Euler's criterion, plus sums of powers over F_p, identify the character sum as -H_p(t): the degree in X is 3m=9r<2(p-1), and the only positive multiple of (p-1) in that degree range is p-1; constant terms sum to 0 mod p. Thus P_{2r}(t)=H_p(t) for every t in F_p.

For completeness, H_p is a polynomial of degree <=2r in t. In the multinomial expansion, a contributing term containing i copies X^3, j copies aX, and k copies b has i+j+k=3r, 3i+j=6r, so j=6r-3i and k=2i-3r. Its t-degree is at most j+2k=i<=2r. Therefore H_p-P_{2r} has degree <p and p roots, so it is identically zero in F_p[t]. This EXACT polynomial identity extends by base change to F_{p^2}; one does not merely substitute extension-field t into an F_p character-sum formula.

Previous project result, for the entire polynomial Y_p: Y_p(z)=P_{2r}(sqrt(1-z)) in F_p[z], with the right side polynomial as P_{2r} is even. Consequently Y_p(1/2)=H_p(t) for either t satisfying 2t^2=1.

Now consider over Q(sqrt 2) the cubic elliptic curve E_t: y^2=X^3+a(t)X+b(t) at t=sqrt 2/2. In Q[t]/(2t^2-1) a direct expansion yields 4a(t)^3+27b(t)^2=-108(4t+3); its reduction is nonsingular for all p>=7 because 4t+3 cannot vanish when 2t^2=1. Its j-invariant is
  j=2417472-1707264 sqrt 2,
  j^2-4834944j+14670139392=0.
This is the Hilbert class polynomial for fundamental discriminant -24, so E_t has CM by Q(sqrt(-6)). Deuring's good-reduction criterion states it is supersingular exactly when p is inert in this quadratic CM field, i.e. when (-6/p)=-1. Its Hasse coefficient H_p(t) vanishes exactly when E_t mod p is supersingular. This proves the theorem and converse. The field t may be in F_{p^2} for the target classes; the polynomial identity above makes this legitimate. This statement concerns the external classical elliptic auxiliary representation, not a native X6 embedding.

## Theorem T2: universal unweighted companion modulo p^2

Let U_p(z)=sum_{k=0}^{p-1} ((1/2)_k (1/3)_k (2/3)_k/(k!)^3) z^k. For every prime p>=7, p mod 24 in {13,19},

  U_p(1/2) = 0 (mod p^2).

Proof. The exact Clausen power-series identity is
  2F1(1/6,1/3;1;z)^2=3F2(1/2,1/3,2/3;1,1;z).
For 0<=k<p, u_k=(1/6)_k(1/3)_k/(k!)^2 has exact valuation v_p(u_k)=1_{k>r}+1_{k>2r}. Hence for i,j<p with i+j>=p, necessarily at least one index >2r (if both <=2r their sum <=4r<p), and v_p(u_i u_j)>=2. All terms beyond degree p-1 in the finite Clausen square are p^2-divisible. Therefore Y_p(z)^2-U_p(z) belongs to p^2 Z_(p)[z]. With Y_p(1/2)=0 mod p from T1, this establishes T2. The signed weighted high-index cutoff is still required to lift W_p(1/2)=(6 theta+1)U_p(1/2) to p mod p^3.

## Exact check, provenance and next action

A separately executed standard-library Python checker evaluated all 207 primes p<=3000, p=1 mod 6: 46 class-1 and 54 class-7 nonzero; 53 class-13 and 54 class-19 zero. All 207 original terminating Y, Legendre, cubic Hasse, discriminant and selector checks PASS; all 107 target original unweighted 3F2 sums vanish mod p^2. The code and runtime log are in the per-run portable evidence bundle. These finite checks corroborate the general proof; they do not replace the cited classical ingredients.

Important next scientific unit: apply now-unconditional s=Y_p(1/2) in p Z_(p) to the exact Hensel conditions from `20261101_hourly_d25_legendre_hensel_observer_inverse.md`. Find a universal CM/trace or WZ certificate for the first weighted digit 12 a_0 d_0=1 mod p, then the second digit including the signed high-index cutoff C_p and integer carry. Target W_p(1/2)=p mod p^3 for all p mod24 in {13,19} stays OPEN. Do not repeat the mod-p zero selector as unproved. This author artifact is pending native CLAIM/OPEN/Source checkpoint and independent admission; original p=373 H0/B0 remains with #1559. Exact Research lane continuation #6638 has terminal UPSTREAM_CODE_REVIEW_REQUIRED, tracked in control #1558; no current Research authority is inferred. Keep source pins and P000/ACTIVE worldview unchanged.

Sources:
- Zhi-Hong Sun, "Legendre polynomials and supercongruences", Acta Arith. 159 (2013), Eq. (1.5), DOI 10.4064/aa159-2-6, https://www.impan.pl/shop/en/publication/transaction/download/product/82338
- Deuring CM supersingular criterion, classical theorem, discussed at https://link.springer.com/article/10.1007/s10231-024-01528-x
- Project prior D25 finite Legendre/Hensel note `research_notes/portable_direct/20261101_hourly_d25_legendre_hensel_observer_inverse.md`.
