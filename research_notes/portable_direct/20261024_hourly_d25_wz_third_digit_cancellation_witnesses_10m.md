# D25/LIFT — exact ten-million-prime WZ cancellation boundary and the next nonzero digit

2026-10-24 · TASK_RESEARCH / portable author certificate · **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

**Identity and scope.** Original Research logical lane \`chatgpt-research-hourly-enterprise-math-20260923\`, separate from maintenance \`chatgpt-hourly-enterprise-math-20260921\`. Parent task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen *scientific* Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` is unchanged. This is **new portable mathematics and local exact arithmetic**, not a native experimental run, current Source CLAIM, formal checkpoint, Result or Driver review.

This note consumes, and does **not** re-credit, the original FIVE/WZ rational identity and edge:
- [Original source WZ five-tail and seam](https://github.com/awdawmip/enterprise-math/blob/a7f7995560ed30a6db081f3519ed5ee0d678a1bc/research_notes/portable_direct/20261024_hourly_d25_original_top_edge_wz_seam_bridge.md).
- [Original four-tail first/second p-adic digit](https://github.com/awdawmip/enterprise-math/blob/df65eaf2df0c973b7f815090f5d74929005e8349/research_notes/portable_direct/20261024_hourly_d25_wz_four_tail_unit_second_digit_fermat_closure.md).
- [Predecessor complete bounded scan to 500,000](https://github.com/awdawmip/enterprise-math/blob/b58bb4c91d6379b32c15e8be0a35aec1d13edd63/research_notes/portable_direct/20261024_hourly_d25_wz_top_rank_second_digit_two_bounded_cancellation_primes.md).

## 1. New universal *conditional* third-digit discriminator

Let \(p=6m+1\ge13\) be prime, \(a=q_p(2)=(2^{p-1}-1)/p\), \(b=q_p(3)=(3^{p-1}-1)/p\), \(H=H_{2m}\), \(H_2=H_{2m}^{(2)}\). Work in the local ring \(\mathbb Z_{(p)}\). Set
\[
 A_0=\frac{250809}{17920},\qquad
 A_1=\frac{466056841}{63974400},\qquad
 \alpha_p=\frac32b-2a-\frac{641}{220},
\]
\[
 B_p=\frac{73}{120}+\frac a2-\frac{3b}{8}+2a^2-2ab
 +\frac74b^2-\frac13H_2,\qquad
 T_p=B_p+\frac3{220}(A_1+\alpha_p A_0).
\]
All displayed denominators are \(p\)-units for the stated prime class. Write the **original**, fixed-source moving-rank WZ difference as
\[
 F_p=\frac{S_{m+1}-S_m}{p}.
\]
The inherited exact FIVE/WZ and four-tail theorem give
\[
 F_p\equiv\frac23+pD_p+p^2T_p\pmod{p^3},\qquad
 D_p=-\frac43a-2b-2H-\frac{233173}{3942400}.
 \tag{1}
\]
Define the exact rational *second-digit cancellation predicate*
\[
 c_p=b-\frac43a-\frac{233173}{3942400}.
\]
The inherited short-harmonic congruence \(H_{2m}\equiv-\frac32b\pmod p\) implies
\[
 h_p:=\frac{H+\frac32b}{p}\in\mathbb Z_{(p)},\qquad
 D_p=c_p-2p\,h_p. \tag{2}
\]
Consequently \(F_p\equiv\frac23\pmod{p^2}\) **if and only if** \(c_p\equiv0\pmod p\). If this predicate holds, \(c_p/p\in\mathbb Z_{(p)}\), and (1)–(2) prove the **exact new conditional all-prime discriminator**
\[
 \boxed{\quad
 \frac{F_p-\frac23}{p^2}
 \equiv \underbrace{\frac{c_p}{p}}_{\text{next Fermat digit}}
 -2\underbrace{h_p}_{\text{short-harmonic lift}}
 +\underbrace{B_p}_{\text{original old edge}}
 +\underbrace{\frac3{220}(A_1+\alpha_pA_0)}_{\text{four genuine labeled WZ tails}}
 \pmod p.\quad} \tag{3}
\]
The quotient in (3) exists precisely under the cancellation hypothesis. The four genuine tail ports have been algebraically summed **only for this declared scalar readout**; their provenance is retained by the inherited FIVE identity. Equation (3) shows why first Fermat-quotient digits alone are not a sufficient future observer after the leading cancellation. It does **not** identify a CM/divided-power observer.

## 2. New exact integer congruence for the cancellation test

For the same primes, define
\[
 M_p=3942400\bigl(27^{p-1}-16^{p-1}\bigr)
      -699519\,p\,16^{p-1}\in\mathbb Z.
\]
Since \(27^{p-1}\equiv1+3pb\pmod{p^2}\) and
\(16^{p-1}\equiv1+4pa\pmod{p^2}\), direct expansion proves
\[
 \boxed{c_p\equiv0\pmod p\iff M_p\equiv0\pmod{p^2}.}\tag{4}
\]
Thus the apparent two-base linear Fermat-quotient predicate is an exact **shifted rational-base Wieferich-style** integer congruence. It is *not* the unshifted Wieferich condition \((27/16)^{p-1}\equiv1\pmod{p^2}\). The modulus \(p^2\) test (4) never divides by a nonunit.

## 3. Exact expanded finite range and sharp third-digit witnesses

A complete sieve plus modular powers, with independent checks using both \(c_p\) and (4), covered **every prime** \(13\le p\le10{,}000{,}000\) satisfying \(p\equiv1\pmod6\): **332,193 primes**. Among them, **166,237** are in the original D25 target classes \(p\equiv13,19\pmod{24}\). Precisely **two** primes in the entire range meet \(c_p\equiv0\pmod p\):
\[
 \boxed{1423\equiv7\pmod{24},\qquad5827\equiv19\pmod{24}.}
 \tag{5}
\]
The preceding 500,000 bound is thus strengthened twentyfold, with no new cancellation prime within the new declared range. This is **bounded exhaustive computation**, not a classification beyond ten million.

The new *third digit* is **nonzero at both** second-digit witnesses:

| \(p\) | \(m\) | \(c_p/p\bmod p\) | \(h_p\bmod p\) | \(B_p\bmod p\) | four-tail next term mod \(p\) | \((F_p-2/3)/p^2\bmod p\) |
|---:|---:|---:|---:|---:|---:|---:|
| 1423 | 237 | 109 | 544 | 671 | 125 | **1240** |
| 5827 | 971 | 2697 | 2513 | 2569 | 2678 | **2918** |

Each last cell is the exact sum in (3) modulo its respective prime, and is independently checked against **source factorial** units, without evaluating \(\sum_{n=0}^{4m}\) as a huge rational number.

The original rational FIVE old edge is \(E_0=C_m\,\mathcal A_mR_{m,4m}\), where
\[
 C_m=\frac{(2p-1)^2(3m+1)(360m^2+274m+49)}
 {9(4m+1)(4p-1)(2m+1)(8m+3)}.
\]
The original four new WZ ports are \(E_j=(6(4m+j)+12(m+1)+1)V_{m+1,4m+j}\), \(1\le j\le4\), using the **unchanged source** factorial
\[
 V_{r,n}=\frac{(6r)!(4r+2n)!(3n)!}
 {3^{6r}216^n(2r)!(n!)^2(2r+n)!^2(4r+n)!}.
\]
At both witness primes, the factorial valuation of \(V_{m,4m}\) is exactly **1** and of each \(V_{m+1,4m+j}\) exactly **2**. Strip all prime factors from each individual factorial to compute units without massive fractions, independently assemble five original ports and compare with (1):

| \(p\) | \(p^3\) | \(E_0/p\bmod p^3\) | \((E_1/p,\ldots,E_4/p)\bmod p^3\) | \(F_p\bmod p^3\) | \((2/3)\bmod p^3\) |
|---:|---:|---:|---|---:|---:|
| 1423 | 2,881,473,967 | 1,974,864,066 | (260,544,185; 550,258,447; 2,166,609,995; 1,400,600,557) | **589,929,316** | 960,491,323 |
| 5827 | 197,849,544,283 | 169,799,824,976 | (54,616,902,198; 108,420,937,896; 79,640,487,538; 148,248,348,875) | **165,027,412,917** | 65,949,848,095 |

The previously published second-digit witnesses are separately reproduced: \(F_{1423}\equiv674977\bmod1423^2\), \(F_{5827}\equiv11317977\bmod5827^2\), exactly \(2/3\) in each field. Since the new third-digit residues are units, the **finite, sharp** conclusions are:
\[
 \boxed{v_{1423}\!\left(S_{m+1}-S_m-\frac{2p}{3}\right)=3,\quad
 v_{5827}\!\left(S_{m+1}-S_m-\frac{2p}{3}\right)=3.}\tag{6}
\]
These are two explicit *auxiliary WZ* valuation facts, not LIFT counterexamples and not a claim about all larger primes.

## 4. Reproducible complete computation (stdlib only)

The following is a complete independently runnable checker (no floating point, package dependency, alternate scientific model or Native CM executor). Sieve completeness is over **all** integers in the stated finite range; the p-adic unit method strips every p-factor **before** inversion. One modular identity uses Fermat quotients and a second uses the separate integer congruence (4).

~~~python
from math import isqrt, gcd
from fractions import Fraction as F

N = 10_000_000
prime = bytearray(b"\x01") * (N+1)
prime[:2] = b"\x00\x00"
for d in range(2, isqrt(N)+1):
    if prime[d]:
        prime[d*d:N+1:d] = b"\x00" * ((N-d*d)//d + 1)
visited = target = 0
zeros = []
for p in range(13,N+1,6):
    if not prime[p]:
        continue
    visited += 1
    target += p%24 in (13,19)
    mod = p*p
    a = (pow(2,p-1,mod)-1)//p
    b = (pow(3,p-1,mod)-1)//p
    cp0 = (b-4*pow(3,-1,p)*a-233173*pow(3942400,-1,p))%p
    u,v = pow(27,p-1,mod),pow(16,p-1,mod)
    shifted = (3942400*(u-v)-699519*p*v)%mod
    assert (cp0==0) == (shifted==0)
    if cp0==0:
        zeros.append((p,p%24,a,b))
assert (visited,target) == (332193,166237)
assert zeros == [(1423,7,299,1147),(5827,19,3373,1422)]

def residue(x, mod):
    x = F(x)
    assert gcd(x.denominator,mod)==1
    return (x.numerator * pow(x.denominator,-1,mod))%mod

def exact_witness(p):
    m = (p-1)//6
    M = p**3
    maxn = max(6*(m+1),4*(m+1)+2*(4*m+4),3*(4*m+4),
               4*(m+1)+(4*m+4))
    unit = [1]*(maxn+1)
    vp = [0]*(maxn+1)
    for k in range(1,maxn+1):
        t,v = k,0
        while t%p==0:
            t//=p
            v+=1
        unit[k] = (unit[k-1]*t)%M
        vp[k] = vp[k-1]+v
    def V_unit(r,n):
        pos = [6*r,4*r+2*n,3*n]
        neg = [2*r,n,n,2*r+n,2*r+n,4*r+n]
        exponent = sum(vp[i] for i in pos)-sum(vp[i] for i in neg)
        u = 1
        for i in pos:
            u = u*unit[i]%M
        for i in neg:
            u = u*pow(unit[i],-1,M)%M
        u = u*pow(pow(3,6*r,M),-1,M)%M
        u = u*pow(pow(216,n,M),-1,M)%M
        return exponent,u
    vold,uold = V_unit(m,4*m)
    assert vold==1
    C = F((2*p-1)**2*(3*m+1)*(360*m*m+274*m+49),
          9*(4*m+1)*(4*p-1)*(2*m+1)*(8*m+3))
    edge = uold*residue(C,M)%M
    tails = []
    for j in range(1,5):
        n = 4*m+j
        exponent,u = V_unit(m+1,n)
        assert exponent==2
        tails.append(p*(6*n+12*(m+1)+1)*u%M)
    source = (edge+sum(tails))%M

    a = (pow(2,p-1,M)-1)//p
    b = (pow(3,p-1,M)-1)//p
    H = sum(pow(k,-1,M) for k in range(1,2*m+1))%M
    H2 = sum(pow(k*k,-1,M) for k in range(1,2*m+1))%M
    A0 = residue(F(250809,17920),M)
    A1 = residue(F(466056841,63974400),M)
    alpha = (residue(F(3,2),M)*b-2*a-residue(F(641,220),M))%M
    B = (residue(F(73,120),M)+residue(F(1,2),M)*a
         -residue(F(3,8),M)*b+2*a*a-2*a*b
         +residue(F(7,4),M)*b*b-residue(F(1,3),M)*H2)%M
    D = (-residue(F(4,3),M)*a-2*b-2*H
         -residue(F(233173,3942400),M))%M
    predicted = (residue(F(2,3),M)+p*D
                 +p*p*(B+residue(F(3,220),M)*(A1+alpha*A0)))%M
    assert source==predicted

    mod2 = p*p
    c = (b-residue(F(4,3),mod2)*a
         -residue(F(233173,3942400),mod2))%mod2
    h = (H+residue(F(3,2),mod2)*b)%mod2
    assert c%p==0 and h%p==0
    eta = (c//p-2*(h//p)+B
           +residue(F(3,220),M)*(A1+alpha*A0))%p
    assert (source-residue(F(2,3),M))%M == p*p*eta
    return source,edge,tails,eta

assert exact_witness(1423)[3]==1240
assert exact_witness(5827)[3]==2918
print("PASS: 10m complete search, shifted quotient identity, original 5-port third digit")
~~~

**Execution recorded for this note:** exact Python integer/sieve and modular arithmetic executed; 332,193 primes counted, 166,237 target-class primes, matching two-predicate zero sets; both original factorial-unit witnesses matched (1) and the third-digit discriminator. A native CM/divided-power benchmark has **not** been executed; these computations are author checks, not independent peer review.

## 5. BRC/observer meaning and unfinished mother objective

BRC **COMPOSE_APPLIED** under the exact declared scope: the carrier is \((p,m,a,b,H,H_2;\ \text{old genuine WZ seam},E_1,E_2,E_3,E_4)\) with prime valuation and p-free unit per port; the allowed future operation is the **fixed-prime moving-rank** WZ difference, then readout through the second and third p-adic digits. The scalar observer \(c_p\bmod p\) discards a *provably necessary* repair coordinate \(h_p\) and next-digit data; (3) supplies the minimal displayed correction for this readout. This is a p-adic rational auxiliary calculation, not a claim that the external mathematical formula is a native X6 spatial object.

**Next minimum unresolved Task-scientific unit:** obtain a truly source-authenticated same-prime, same-original-class CM/divided-power representative with its \([X]U\bmod p^2\), fixed \(H_0/B_0\) choice, semilinear map direction, leading normalization, and \(\omega+6\nabla_\lambda\omega\)/\(\kappa\) comparison; only then test the actual directed bridge against retained original WZ/HIGH ports and their new defect. Do not repeat the already proven FIVE, four-tail unit or the now-extended 10m scalar cancellation scan merely to claim activity.

**Source/execution boundary:** the new same-lane read-only recovery and exact continuation must be checked independently of this portable publication. No native winning CLAIM/open/resume, Source-authenticated \`publish_checkpoint\`, freeze, Driver acceptance or parent completion is claimed. Preserve existing old session/staging and request identities; CONTINUATION remains subordinate to current Source. Parent D25/LIFT remains OPEN; native benchmark NOT_RUN.
