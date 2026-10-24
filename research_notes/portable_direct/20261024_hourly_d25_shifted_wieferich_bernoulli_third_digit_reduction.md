# D25/LIFT — third-digit cancellation as a shifted Wieferich quotient and a mod-3 Bernoulli character

2026-10-24 · TASK_RESEARCH portable certificate · **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

## Status, source and scope

This is an author derivation in the ordinary research lane chatgpt-research-hourly-enterprise-math-20260923. It neither assumes nor grants a canonical CLAIM/open authorization; it does not replace the unchanged scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. The source-sensitive CM/divided-power representative has not been supplied, and the original D25/LIFT mother target remains OPEN. All formulas below concern the *auxiliary original-source fixed-prime moving-rank WZ readout*, not the CM target.

The exact previously established FIVE/WZ formula, constants, and two exceptional-prime witnesses are consumed (not re-credited) from:
- [Original WZ five-tail/seam](https://github.com/awdawmip/enterprise-math/blob/a7f7995560ed30a6db081f3519ed5ee0d678a1bc/research_notes/portable_direct/20261024_hourly_d25_original_top_edge_wz_seam_bridge.md)
- [Four original labeled tails and second digit](https://github.com/awdawmip/enterprise-math/blob/df65eaf2df0c973b7f815090f5d74929005e8349/research_notes/portable_direct/20261024_hourly_d25_wz_four_tail_unit_second_digit_fermat_closure.md)
- [Exact ten-million range and conditional third digit](https://github.com/awdawmip/enterprise-math/blob/17648037849aba8a7ec52fec3c248e73cca5a336/research_notes/portable_direct/20261024_hourly_d25_wz_third_digit_cancellation_witnesses_10m.md)

**New unit:** reduce the third digit under cancellation to one *integral shifted-Wieferich quotient*, the two small exact residual coordinates, and a generalized Bernoulli number for the primitive odd character modulo 3. In particular, the apparent q_p(3) dependence of the explicit four-tail correction cancels entirely upon imposing the second-digit predicate. This is a proven algebraic compression for the declared third-digit scalar observer, not an identification of external and native mathematical objects.

## 1. Precisely typed inputs

Let p >= 13 be prime with p = 6m+1; all congruences are in the p-local ring Z_(p). Define integer Fermat quotients a=q_p(2)=(2^(p-1)-1)/p and b=q_p(3)=(3^(p-1)-1)/p. Write H=H_(2m) and H2=H_(2m)^(2). Put

D = 3,942,400,  k = 233173/D,  A0 = 250809/17920,
A1 = 466056841/63974400,  alpha = 3b/2 - 2a - 641/220,

B = 73/120 + a/2 - 3b/8 + 2a^2 - 2ab + 7b^2/4 - H2/3,

T = B + (3/220)(A1 + alpha*A0),
c = b - 4a/3 - k,
h = (H + 3b/2)/p.

The inherited short harmonic congruence H_(2m) = -3b/2 (mod p) ensures h belongs to Z_(p). All rational denominators displayed here and below are p-units for this prime class.

For the genuine original-source moving-rank WZ difference let F=(S_(m+1)-S_m)/p. The preceding exact finite derivations give

F = 2/3 + p*(-4a/3 - 2b - 2H - k) + p^2*T (mod p^3)
  = 2/3 + p*c + p^2*(T - 2h) (mod p^3).            (1)

The **cancellation condition** is c=0 (mod p); it is equivalent to F=2/3 (mod p^2). Under this condition the integral third digit exists:

eta = (F - 2/3)/p^2 = c/p - 2h + T (mod p).        (2)

The zero condition in (2) means further fourth-order cancellation of S_(m+1)-S_m-2p/3.

## 2. New cancellation-fiber polynomial (proof)

Suppose c=0 (mod p). Then b = 4a/3 + k (mod p), and consequently

alpha = 3k/2 - 641/220 (mod p),                   (3)

which is **independent of a and b** on this cancellation fiber. Direct substitution in B gives

B = (22/9)a^2 + (8/3)k*a
    + 73/120 - 3k/8 + 7k^2/4 - H2/3    (mod p).

Define the exact constant

C = 73/120 - 3k/8 + 7k^2/4
    + (3/220)(A1 + (3k/2 - 641/220)*A0)
  = 483423834516059 / 3170673623040000.

Then

T = (22/9)a^2 + (8/3)k*a + C - H2/3 (mod p),    (4)

and the four original tail channels, already source-labelled in the inherited exact FIVE certificate, contribute the *constant* (3/220)(A1+(3k/2-641/220)A0). Equation (4) is only a scalar compression after the declared cancellation observer; it does not discard the provenance of the source five ports.

## 3. New integral shifted-Wieferich lift (proof)

Use the inherited integer

M = D*(27^(p-1) - 16^(p-1)) - 699519*p*16^(p-1).

Since 2^(p-1)=1+pa and 3^(p-1)=1+pb exactly as integers, expansion through p^2 yields the **exact modulo-p^3 identity**

M/p = 3D*c + p*[D*(3b^2 - 6a^2) - 4*699519*a] (mod p^2).  (5)

The right-hand expansion is valid without a divisibility hypothesis; all terms of M/p are integers. The old predicate c=0 (mod p) is equivalent to p^2 dividing M, and then (5) implies

c/p = M/(3D*p^2) - b^2 + 2a^2 + 4k*a (mod p).  (6)

Put

Cstar = C - k^2
      = 472332426338543 / 3170673623040000.

Substitute (6) and b=4a/3+k (mod p) into (2) and (4). The quadratic and linear terms simplify *exactly* to

eta = M/(3D*p^2) - 2h + (8/3)a^2
      + 4k*a + Cstar - H2/3 (mod p).             (7)

In particular, this replaces division of the cancellation rational c by p with a direct integer quotient M/p^2. Do not use it without checking p^2 | M.

## 4. New Bernoulli/Dirichlet-character port (proof)

Let chi=chi_(-3) be the primitive odd Dirichlet character modulo 3, with chi(1)=+1, chi(2)=-1, chi(3)=0. Let B_n(x) be the *ordinary classical Bernoulli polynomial*, and define the generalized Bernoulli number

B_(n,chi) = 3^(n-1) * [B_n(1/3) - B_n(2/3)].

For n=p-2, n is odd >=11. By Fermat and finite Faulhaber,

H2 = sum_(j=1)^(2m) j^(-2)
   = sum_(j=1)^((p-1)/3) j^(p-3)
   = [B_(p-2)((p+2)/3) - B_(p-2)(1)] / (p-2) (mod p).

Here B_(p-2)(1)=B_(p-2)=0 and (p+2)/3=2/3 (mod p); the coefficients of B_(p-2)(x) are p-integral by von Staudt–Clausen since their Bernoulli indices are <p-1, and 3 is a p-unit. The odd reflection B_n(2/3)=-B_n(1/3) therefore gives

H2 = (1/2) B_(p-2)(1/3) (mod p).

Because B_(p-2,chi) = 2*3^(p-3)*B_(p-2)(1/3) and 3^(p-3)=3^(-2) (mod p), this proves

**H2 = (9/4) B_(p-2,chi) (mod p).**                 (8)

This is an *auxiliary character* of conductor 3; it is **not** an assertion identifying the original D25 CM primitive class or Frobenius operator.

Combining (7) and (8) yields the main new theorem:

**If p=6m+1>=13 is prime and p^2 divides M, then**

eta = (S_(m+1)-S_m-2p/3)/p^3
    = M/(3D*p^2) - 2h + (8/3)a^2 + 4k*a
      + Cstar - (3/4) B_(p-2,chi)   (mod p).      (9)

The p-local quotient in the left member is defined under the stated condition. Thus eta=0 (mod p) if and only if the concrete right member vanishes; this is a **new exact conditional universal third-digit zero criterion** for the original-source auxiliary WZ readout. The source dependence has been compressed to a sharply typed pair of residual coordinates (M/p^2, h), a single Fermat quotient a, and the character-Bernoulli scalar.

Equivalently, without explicit generalized Bernoulli computation, replace -(3/4)B_(p-2,chi) by -H2/3 in (9). That exact computational specialization uses only modular integer arithmetic and a finite harmonic sum.

## 5. Independent arithmetic author checks, finite witness scope

The author checked the polynomial reduction symbolically and evaluated both forms of (9) via exact modular arithmetic for the only two previously identified cancellation primes <=10,000,000. The finite 10M completeness is inherited; no new prime search or independent peer review is claimed.

| p | a mod p | M/p^2 mod p | h mod p | H2 mod p | B_(p-2,chi) mod p | eta mod p |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1423 | 299 | 43 | 544 | 427 | 506 | **1240** |
| 5827 | 3373 | 786 | 2513 | 2917 | 649 | **2918** |

The last column matches the independently inherited original five-port factorial-unit calculation, so v_p(S_(m+1)-S_m-2p/3)=3 at both specific p. Separately checked (8) using exact Bernoulli polynomial rationals for p=13,19,31,37,43; it agreed with the short inverse-square harmonic sum each time. These computations are author verification; the universal assertions rely on the algebraic proofs in §§2–4.

A minimal integer-only verification of (7), using modular inversion of p-units and the known two witnesses, is reproducible:

~~~python
from fractions import Fraction as Q
D = 3942400
k = Q(233173, D)
Cstar = Q(472332426338543, 3170673623040000)
def loc(x, p):
    x = Q(x)
    return x.numerator * pow(x.denominator, -1, p) % p
for p, expected in [(1423, 1240), (5827, 2918)]:
    m = (p-1)//6
    a = (pow(2,p-1,p**3)-1)//p
    b = (pow(3,p-1,p**3)-1)//p
    M = (D*(pow(27,p-1,p**3)-pow(16,p-1,p**3))
         -699519*p*pow(16,p-1,p**3)) % p**3
    assert M % p**2 == 0
    hnum = (sum(pow(j,-1,p*p) for j in range(1,2*m+1))
            +loc(Q(3,2),p*p)*b) % (p*p)
    assert hnum % p == 0
    H2 = sum(pow(j*j,-1,p) for j in range(1,2*m+1)) % p
    eta = (loc(Q(1,3*D),p)*(M//p**2) -2*(hnum//p)
           +loc(Q(8,3),p)*a*a + loc(4*k,p)*a
           +loc(Cstar,p) -loc(Q(1,3),p)*H2) % p
    assert eta == expected
print("PASS: integral lifted predicate at both genuine FIVE/WZ witnesses")
~~~

## 6. BRC/observer audit and next scientific step

**BRC COMPOSE_APPLIED, exact stated scope.** The input carrier retains the original five separate WZ ports with each prime valuation, source factorial and p-free unit; the allowed future operation is the fixed-p moving-rank WZ difference followed by the third-digit scalar observer. Compression to (9) is proved sufficient for *that observer under cancellation*, not for arbitrary future CM class maps. The residuals h and M/p^2 are indispensable to this declared compression; dropping either is not justified. No native 6D spatial interpretation is inferred from this external arithmetic formula.

**Mother target still open:** identify an authenticated same-prime, same-original-class CM/divided-power representative; its [X]U mod p^2 and fixed H0/B0 coefficients; actual semilinear map direction, leading normalization, and the omega+6 nabla_lambda omega / kappa comparison. The derived chi_(-3) arithmetic is a narrowly typed possible number-theoretic input, **not** that missing representative. An authorized owner/Driver must determine whether a justified Source map exists, rather than assume it.

**Do not repeat:** completed original five-tail rational WZ proof, original four-tail unit, previous 10M scan, or the old third-digit two-witness computation as new units. Keep source-published checkpoints, portable evidence, and independent admission distinct. Current Source claim/run and any original staging must be resolved solely through actual control receipts. Native CM experiment remains NOT_RUN; this proof is UNREVIEWED/NOT_ADMITTED.
