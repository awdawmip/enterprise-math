# D25/LIFT — exact Wolstenholme/finite-port classification of the genuine-tail valuation jump

2026-10-25 | TASK_RESEARCH | **PORTABLE AUTHOR-SIDE PROOF / EXACT FINITE CERTIFICATES / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT / NONBLIND**.

**Provenance and scope.** Parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; published Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source `c47e13e4aba0e006366f989d6334d443f6333ae3` is NOT repinned by this note. The source-labeled original WZ/factorial identity, two-group observer and earlier p^5/p^6 seam are **inherited**, not recredited. Exact factors used below are from `20261025_offphase_d25_frobenius_seam_mod_p6_exceptional_tail.md` and `20261025_offphase_d25_source_factor_jet_all_precision.md` in this folder.

## Exact typed interface

For any prime `p=6m+1>=13`, work in `Z_(p)`; all following denominators are p-units. Preserve the original old edge and four genuine tail labels. Define the *four-tail-group compression discrepancy only* by

```text
T_p = binom(2p-1,p-1) = product_{j=1}^{p-1}(1-p^2/j^2),
L_p = (3p/220) B(p) P_base(p),      P_base(p) = 1 (mod p),
E_p = (T_p^2-1) L_p.
```

Here `B(z)` is the previously fixed rational four-port transfer, not an arbitrary positive-mass BRC branch. In the existing source normalization, direct differentiation of its four-term recurrence yields

```text
B(0)  = 250809/17920,
B'(0) = 466056841/63974400,
[z]L_p(z) = (3/220)B(0) = 752427/3942400.
```

Explicit recurrence (sufficient to recompute those two rationals): put `c_1(z)=1`, for `j=1,2,3`

```text
c_(j+1)(z)/c_j(z)
 = ((2z+2j+3)(2z+3j-1)(2z+3j))
   / (4(2z+3j+1)(z+j+2)(4z+3j+11));
B(z)=sum_{j=1}^{4} (6z+6j+7)c_j(z).
```

The small denominators in `B(0)`, `B'(0)`, and the source product `P_base(p)` are units for every admitted prime; the exceptional 17 in a derivative denominator has `17=5 (mod 6)` and is outside the population. The declared observation is the exact valuation of `E_p`; no quotient of the individual four port labels is asserted safe for other operations.

## Theorem: all-prime exact valuation law

For every prime `p=6m+1>=13`, let `w_p=v_p(T_p-1)`. Then

```text
v_p(E_p) = w_p + 1 + 1_{p in {13,109}}.                     (1)
```

In particular, the following is an **if and only if** assertion, not a finite-scan extrapolation:

```text
E_p = 0 (mod p^5)
  iff p in {13,109} OR binom(2p-1,p-1) = 1 (mod p^4).       (2)
```

The last congruence is the classical **Wolstenholme-prime condition**. Thus both kinds of exceptional fifth-digit disappearance are characterized: zero of the four-tail leading transfer, or extra divisibility of the binomial/Frobenius observer. They have different provenance and must not be merged into one cause.

**Proof.** `T_p=1 (mod p)` and `T_p+1=2 (mod p)`, hence `v_p(T_p^2-1)=v_p(T_p-1)=w_p`. Every factor of `P_base(p)` is a p-unit and its residue is 1, while `3/220` is a p-unit. Therefore `v_p(L_p)=1+v_p(B(p))`. The numerator of `B(0)` is

```text
250809 = 3*13*59*109.
```

Of these prime factors, only 13 and 109 belong to the admitted `p=1 (mod 6)` range. For all other admitted primes `B(p)=B(0) (mod p)` is a unit, hence `v_p(B(p))=0`. For the two exceptional primes, the p-integral Taylor expansion gives `B(p)/p = B(0)/p + B'(0) (mod p)`, and direct p-unit modular arithmetic gives residues `7 (mod 13)` and `68 (mod 109)`, both nonzero. Therefore `v_{13}(B(13))=v_{109}(B(109))=1`. This proves (1).

Wolstenholme's theorem gives `w_p>=3` for p>=5. Thus `v_p(E_p)>=5` for the two transfer exceptions, and for every other admissible p it holds exactly when `w_p>=4`. This is (2). No assertion is made that the set of Wolstenholme primes is exhausted by currently known examples. QED.

**Harmonic/BRC observer refinement.** Define `Theta_p = H_(p-1)^(2)/p`, where `H_(p-1)^(2)=sum_{j=1}^{p-1}1/j^2`. The exact finite even-product identity gives

```text
T_p^2 - 1 = -2 p^3 Theta_p (mod p^5);
E_p/p^4 = -2 Theta_p * (752427/3942400) (mod p).
```

Consequently, at the declared fifth-digit observer, `v_p(E_p)>=5` precisely when `Theta_p=0 (mod p)` **or** the authentic four-port leading transfer vanishes. The first condition is equivalent to the Wolstenholme-prime condition because `T_p-1 = -p^2 H_(p-1)^(2) (mod p^4)`. This retains separately the harmonic/Frobenius observer, exact rational four-port incidence and prime class.

## New exceptional certificate beyond the prior p<3000 check: p=16843

`16843` is prime and `16843=1 (mod 6)`. Its exact combinatorial binomial and four-tail-leading coefficients yield

```text
p = 16843;
(T_p-1)/p^4 = 3323 (mod p),  with T_p-1 = 0 (mod p^4);
(T_p^2-1)/p^4 = 6646 (mod p);
L_p/p = (752427/3942400) = 1120 (mod p);
E_p/p^5 = 6646*1120 = 15757 (mod p).
```

Therefore `v_16843(E_16843)=5`, although `16843` does **not** divide the authentic four-tail leading numerator. Its exception is entirely the binomial/Wolstenholme route. This is a **new fifth-digit exception for the original labeled WZ tail observer outside the predecessor's p<3000 sample**, not discovery of Wolstenholme primes themselves (16843 is classically known).

For the earlier exceptional primes, the same exact certificate gives `(T_p-1)/p^3=1,106` at `p=13,109` respectively; `B(p)/p=7,68`; `L_p/p^2=5,102`; and `E_p/p^5=10,42`, respectively. The old 13/109 phenomenon is reproduced only as a consistency check, not new credit.

## Standalone exact checker (stdlib Python)

```python
from fractions import Fraction as F
from math import comb, isqrt

def coeffs_B():
    b0 = b1 = F(0)
    c, cp = F(1), F(0)
    for j in range(1, 5):
        b0 += (6*j+7)*c
        b1 += 6*c + (6*j+7)*cp
        if j < 4:
            a = F((2*j+3)*(3*j-1)*(3*j),
                  4*(3*j+1)*(j+2)*(3*j+11))
            dlog = (F(2,2*j+3)+F(2,3*j-1)+F(2,3*j)
                    -F(2,3*j+1)-F(1,j+2)-F(4,3*j+11))
            cp, c = cp*a+c*a*dlog, c*a
    return b0, b1

def unit(a, b, p):
    return a * pow(b % p, -1, p) % p

assert coeffs_B() == (F(250809,17920), F(466056841,63974400))
for p in (13, 109, 16843):
    assert all(p % d for d in range(2,isqrt(p)+1))
    assert p % 6 == 1
    t = comb(2*p-1,p-1)
    if p in (13,109):
        assert (t-1) % p**3 == 0 and (t-1) % p**4 != 0
        b = (unit(250809//p,17920,p)
             + unit(466056841,63974400,p)) % p
        l = 3 * pow(220,-1,p) * b % p
        e = 2*((t-1)//p**3)*l % p
        assert (b,l,e) == ({13:(7,5,10),109:(68,102,42)}[p])
    else:
        assert (t-1) % p**4 == 0 and (t-1) % p**5 != 0
        l = unit(752427,3942400,p)
        t4 = ((t-1)//p**4) % p
        e = 2*t4*l % p
        assert (t4,l,e)==(3323,1120,15757)
print("PASS: B(0), B'(0), p=13/109 transfer, p=16843 Wolstenholme-tail")
```

The author executed an independent full source-product modular reconstruction at `p=13,19,109,16843` to p^7 and obtained, for p=16843, `v_p(L_p)=1`, `v_p(T_p^2-1)=4`, `v_p(E_p)=5`; the shorter checker above is independently reproducible from the stated rational recurrence and binomial expression. Finite evidence is kept separate from the all-prime proof (1)–(2).

## Prior art, status and continuation

The Wolstenholme-prime definition and classical harmonic/binomial results predate this note; see [Wolfram MathWorld: Wolstenholme Prime](https://mathworld.wolfram.com/WolstenholmePrime.html) and [R. Meštrović, *Congruences for Wolstenholme primes* (2011)](https://arxiv.org/abs/1108.4178). The new result here is the source-specific **exact all-prime tail-valuation equivalence** and its original five-port exceptional certificate at p=16843. No claim of priority over all mathematical literature or independent review.

This does not produce the authentic same-prime/same-original-class CM/DP representatives or prove `Delta_p=(G_p h-1)/p = R_p (mod p)`. D25/LIFT remains open. The grouping into the genuine-tail scalar `L` is valid only for the declared `E` observer; individual four-port provenance, source factors, and the joint relation background remain retained in inherited files. No native X6/Heartbeat physical transfer is inferred from this external integer/p-adic theorem.

Native `recovery_status` has no exposed method on this Site-scoped tool surface; bounded canonical task inventory returned `CONTROL_QUOTA`, own checkpoint list returned `ACCESS_DENIED`, and site connection status reports `research_authority_granted=false` / `write_relay_enabled=false`. No active personal CLAIM, session, open/run, Source checkpoint, Result, freeze, handoff or independent Driver verdict is claimed. UR V2 original four-file bytes (historical 94687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) remain unverified; don't redo completed UR proof.

**Next exact action:** if Source authorization later becomes available, first read this real conversation's recovery_status/original request receipts and exact Task continuation, preserve Source-verified predecessor frontier and ownership; attach this already-published portable evidence only through the valid writer/provenance/checkpoint path. For mathematics, move toward actual second-digit scalar/class interface rather than unbounded new WZ precision.
