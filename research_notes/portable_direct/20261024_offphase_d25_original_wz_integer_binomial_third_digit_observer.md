# D25/LIFT — integral-binomial third-digit observer for the original WZ five-port seam

2026-10-24 · TASK_RESEARCH · **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT**. This is a neutral portable mathematical derivation, not a canonically allocated execution, independent review, Result, or approval to rewrite P000.

## Source, scope, and attribution

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Existing Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; V2 publication: TP2-B6F4FC938FF94941C1B7. The inherited frozen *scientific* source pin is c47e13e4aba0e006366f989d6334d443f6333ae3, not the moving source/control head.

This note **inherits** rather than re-proves or reclaims: the exact original FIVE/WZ old-edge plus four individually labeled tails; the original terminal-unit third digit; the universal four-tail expansions; the harmonic congruence; and the preceding on-hour WZ third-digit theorem plus its 10-million-prime bounded scan and two sharp witnesses. Exact existing sources:
- https://github.com/awdawmip/enterprise-math/blob/951e226bc06eedee7b5290b11fcd4d404f2ba7fc/research_notes/portable_direct/20261024_offphase_d25_original_terminal_unit_third_digit.md
- https://github.com/awdawmip/enterprise-math/blob/09a988526a20c3cd8900150e8be02d3ac37c6092/research_notes/portable_direct/20261024_offphase_d25_original_four_tail_universal_unit_3over220.md
- https://github.com/awdawmip/enterprise-math/blob/17648037849aba8a7ec52fec3c248e73cca5a336/research_notes/portable_direct/20261024_hourly_d25_wz_third_digit_cancellation_witnesses_10m.md

**New work here:** an all-prime third-digit *integer-binomial observer* that replaces both harmonic statistics by two integral combinatorial coordinates; an integer-only conditional sharp third-digit cancellation certificate; exact source-factorial falsification tests. These are equivalent re-expressions of inherited theorems, not a new proof of the original WZ or the same-prime CM/DP LIFT target.

## 1. Two genuine integer coordinates

Let \(p=6m+1\ge13\) be prime, \(r=2m=(p-1)/3\), and set

\[
a=q_p(2)=\frac{2^{p-1}-1}{p},\qquad
b=q_p(3)=\frac{3^{p-1}-1}{p},\qquad
X_p=\binom{p-1}{r},\quad Y_p=\binom{p+r}{r}.
\]
As \(r\) is even, \(X_p=\prod_{j=1}^r(1-p/j)\); also \(Y_p=\prod_{j=1}^r(1+p/j)\), identities in \(\mathbb Z_{(p)}\). Define

\[
\boxed{
J_p=\frac{2X_p-2-3pb}{p^2}\in\mathbb Z,\qquad
L_p=\frac{1-X_pY_p}{p^2}\in\mathbb Z.}\tag{1}
\]

These are not mere rational coefficients. By the inherited exact short-harmonic congruence \(H_r\equiv-\frac32b\pmod p\), the first-order binomial expansion gives \(2X_p\equiv2+3pb\pmod{p^2}\), proving integral divisibility in \(J_p\). Multiplying the two integral binomial products gives

\[
X_pY_p=\prod_{j=1}^r(1-p^2/j^2)\equiv1\pmod{p^2},
\]

hence integral divisibility in \(L_p\). Put \(H=H_r\), \(H_2=H_r^{(2)}\), \(h=(H+\tfrac32 b)/p\in\mathbb Z_{(p)}\). Expand one order further:

\[
X_p\equiv1+\frac{3pb}{2}
+p^2\left(-h+\frac{9b^2}{8}-\frac{H_2}{2}\right)\pmod{p^3},
\]

which, together with the product formula, proves

\[
\boxed{J_p\equiv-2h+\frac94b^2-H_2,\qquad L_p\equiv H_2\pmod p.}\tag{2}
\]

The pair \((J_p,L_p)\) is thus the **minimal two-coordinate repair** for the two p-adic quantities formerly written using \(h,H_2\). A single total residue cannot reconstruct both labels without an additional relation.

## 2. Harmonic-free complete moving-rank WZ third digit

Use the inherited exact original, five-port rational seam \(S_{m+1}-S_m=E_0+\sum_{j=1}^4 E_j\) and denote \(F_p=(S_{m+1}-S_m)/p\). Its source-backed third-digit formula reads

\[
F_p\equiv\frac23+p c_p+p^2(B_p-2h+\tau_p)\pmod{p^3},\tag{3}
\]
where
\[
c_p=b-\frac43a-\frac{233173}{3942400},\quad
B_p=\frac{73}{120}+\frac a2-\frac{3b}{8}
+2a^2-2ab+\frac74b^2-\frac13H_2,
\]
\[
\alpha_p=\frac32b-2a-\frac{641}{220},\qquad
\tau_p=\frac3{220}
\left(\frac{466056841}{63974400}
+\alpha_p\frac{250809}{17920}\right).
\]

Substitute (2) into (3) and **retain the original five individually labeled ports as the provenance layer**. For *all* primes \(p=6m+1\ge13\),

\[
\boxed{\quad
F_p\equiv\frac23+p c_p+
p^2\left[
J_p+\frac23L_p+\frac{73}{120}+\frac a2-\frac{3b}{8}
+2a^2-2ab-\frac12b^2+\tau_p
\right]\pmod{p^3}.
\quad}\tag{4}
\]

The harmonic sums \(H_r,H_r^{(2)}\) are absent. All displayed rational denominators are p-units for the stated prime class (their prime factors lie in \(\{2,3,5,7,11,17\}\), and 17 is not 1 modulo 6). Therefore (4) has an exact modular-arithmetic meaning, with ordinary integer binomial coefficients and Fermat quotients as inputs. Formula (4) is a *new computation/representation theorem conditional only on the previously proven source WZ identity*, not an independent proof of the inherited input.

## 3. Completely integral exceptional-cancellation certificate

For the inherited second-digit predicate define the exact integer

\[
K=3942400,\quad C=\frac{233173}{K},\qquad
M_p=K(27^{p-1}-16^{p-1})-699519p\,16^{p-1}.
\]
The preceding source proved \(F_p\equiv\frac23\pmod{p^2}\) iff \(c_p\equiv0\pmod p\) iff \(M_p\equiv0\pmod{p^2}\). In this *conditional* case \(M_p/p^2\) is an integer, and the next digit can be computed with no harmonic sums or rational divided Fermat quotient:

\[
\boxed{\begin{aligned}
\Gamma_p:=\frac{F_p-2/3}{p^2}\equiv{}&
\frac{M_p/p^2}{3K}+J_p+\frac23L_p+
\frac{73}{120}+\frac a2-\frac{3b}{8}\\
&+4a^2-2ab-\frac32b^2+4Ca+\tau_p
\pmod p.
\end{aligned}}\tag{5}
\]

**Proof of the integer substitution:** write \(27^{p-1}=(1+pb)^3\) and \(16^{p-1}=(1+pa)^4\). Modulo \(p^3\), their difference is
\(p(3b-4a)+p^2(3b^2-6a^2)\). The corrective term \(3p\cdot233173(1+pa)^4\) contributes \(3p\cdot233173+12p^2\cdot233173a\). Hence

\[
\frac{M_p}{p^2}\equiv3K\frac{c_p}{p}
+K(3b^2-6a^2-12Ca)\pmod p,
\]

valid precisely when \(c_p\equiv0\pmod p\); rearrangement and (4) give (5). All inversions involve p-units. This does *not* assert that all cancellation primes have nonzero third digits.

The previously established bounded exhaustive results are *inputs*: only \(p=1423,5827\) among the 332,193 primes \(13\le p\le10^7,\ p\equiv1\pmod6\) meet the second-digit predicate. New coordinate/quotient checks, with each witness confirmed against both (4) and (5):

| p | J mod p | L mod p | M/p² mod p | \(\Gamma_p\) mod p |
|---:|---:|---:|---:|---:|
| 1423 | 544 | 427 | 43 | **1240** |
| 5827 | 2513 | 2917 | 786 | **2918** |

The \(\Gamma_p\) values themselves were independently published previously via original source factorial ports. This table is a *new independent coordinate observer*, not two newly discovered exceptional primes.

## 4. Exact reproducible falsification checker

The following standalone Python stdlib script computes all original factorial FIVE/WZ ports as exact rational numbers (not a substitute model), compares the full difference against (4) modulo \(p^3\) for **all 79 primes \(13\le p<1000,\ p\equiv1\pmod6\)**, and separately validates the integer predicate and (5) at the two already-known witnesses. It runs without floats, invokes modular inverses only for genuine p-unit denominators, and gives expected output \(\texttt{79/79; witnesses (1423,1240), (5827,2918)}\).

~~~python
from math import factorial as fac, comb, gcd, isqrt
from fractions import Fraction as Q

def mod(z, n):
    z = Q(z)
    assert gcd(z.denominator, n) == 1
    return (z.numerator * pow(z.denominator, -1, n)) % n

def original_five(p):
    m = (p - 1) // 6
    U = Q(1, 108**(p-1)*fac(2*m)*fac(4*m)**2)
    for j in range(1,p-1):
        U *= (p+j)**2
    for j in range(1,2*m):
        U /= (p+j)
    C = Q((2*p-1)**2*(3*m+1)*(360*m*m+274*m+49),
          9*(4*m+1)*(4*p-1)*(2*m+1)*(8*m+3))
    total = U*C
    for j in range(1,5):
        r, n = m+1, 4*m+j
        V = Q(fac(6*r)*fac(4*r+2*n)*fac(3*n),
              3**(6*r)*216**n*fac(2*r)*fac(n)**2
              *fac(2*r+n)**2*fac(4*r+n))
        total += Q(6*n+12*r+1,p)*V
    return total

def binomial_observer(p):
    r = (p-1)//3
    a, b = (2**(p-1)-1)//p, (3**(p-1)-1)//p
    X, Y = comb(p-1,r), comb(p+r,r)
    assert (2*X-2-3*p*b) % p**2 == 0
    assert (1-X*Y) % p**2 == 0
    J, L = (2*X-2-3*p*b)//p**2, (1-X*Y)//p**2
    C, K = Q(233173,3942400), 3942400
    c = b-Q(4,3)*a-C
    alpha = Q(3,2)*b-2*a-Q(641,220)
    tau = Q(3,220)*(Q(466056841,63974400)
                    +alpha*Q(250809,17920))
    R = (J+Q(2,3)*L+Q(73,120)+Q(a,2)-Q(3*b,8)
         +2*a*a-2*a*b-Q(b*b,2)+tau)
    F = Q(2,3)+p*c+p*p*R
    return F, c, J, L, a, b, tau

limit = 999
sieve = bytearray(b"\x01")*(limit+1)
sieve[:2] = b"\x00\x00"
for d in range(2,isqrt(limit)+1):
    if sieve[d]:
        sieve[d*d:limit+1:d] = b"\x00"*((limit-d*d)//d+1)
ps = [p for p in range(13,limit+1,6) if sieve[p]]
for p in ps:
    F = binomial_observer(p)[0]
    assert mod(original_five(p),p**3) == mod(F,p**3), p
assert len(ps) == 79, len(ps)
print(str(len(ps))+"/"+str(len(ps)))

for p, expected in ((1423,1240),(5827,2918)):
    F,c,J,L,a,b,tau = binomial_observer(p)
    assert mod(c,p) == 0
    K, C = 3942400, Q(233173,3942400)
    M = K*(27**(p-1)-16**(p-1))-699519*p*16**(p-1)
    assert M%p**2 == 0
    Gamma = (Q(M//p**2,3*K)+J+Q(2,3)*L
             +Q(73,120)+Q(a,2)-Q(3*b,8)
             +4*a*a-2*a*b-Q(3*b*b,2)+4*C*a+tau)
    assert mod(Gamma,p) == expected
    assert mod((F-Q(2,3))/p**2,p) == expected
    print(p,mod(Gamma,p))
~~~

**Run scope and proof strength.** This iteration actually ran the exact source-factorial script for 79/79 qualifying primes below 1000, with zero mismatches; witness modular computations independently returned 1240/2918. The finite comparisons falsify small-input mistakes but are not the proof of the all-prime statement; that proof is the local-ring identities (1)–(5) and the explicitly inherited WZ theorem. No native Source runtime, CM/Katz/divided-power experiment, six-axis triadic dynamics simulation, Lean verification, independent referee, or mathematically admitted Result has occurred here.

## 5. BRC/Enterprise port and handoff discipline

Actual typed reuse: the original five WZ ports \(E_0,\dots,E_4\) remain separately sourced with their original factorial normalization, p-valuations and modular units. Only after fixing the scalar output \(F_p\pmod{p^3}\) do we apply the information-losing sum observer and replace its harmonic inputs with the two integral repair coordinates \(J_p,L_p\). The observer discards individual port provenance; the inherited five-port statement and sources preserve that provenance for future operations. The external one-variable rational p-adic congruence does **not** establish native Heartbeat X6 axes, time, triadic-force closure, CM/DP normalization or source-specific \(\kappa_p\).

**Next scientific question:** decide whether any *source-defined same-prime LIFT primitive* factors through this integer-binomial observer after adding the original CM/DP normalization and \(R_p\) port, or exhibit an explicit missing fiber coordinate. Do not assert an observer bridge without those actual source data.

**Native control debt:** current direct Site gateway advertised readonly credentials and no Researcher executor binding; exact Source continuation request hit transient CONTROL_QUOTA. No new service session, CLAIM, OPEN, Source checkpoint, HANDOFF or Result is claimed. The existing verified 19-unit native checkpoint must not be overwritten by this neutral note. Historical four-file UR V2 input reported 94,687 bytes and SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76; these original bytes were not recovered/verified here. Recover the original material and outstanding request receipts, obtain genuine Site-bound Researcher admission, then only fill missing writer/provenance and legitimately read back native checkpoint; do not redo already completed UR proof.