# D25/LIFT — Fourth-digit correction for the lifted Frobenius-compressed genuine WZ five-port observer

2026-10-25 | TASK_RESEARCH | **PORTABLE AUTHOR PROOF + EXACT AUTHOR CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT**.

This is a new, narrow arithmetic consequence of the *inherited* exact genuine five-port identity and the already published compressed p² seam. It is **not** a claim of ownership of any other conversation's native session, independent Driver review, original-class crystalline Frobenius identification, or completion of D25/LIFT. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; original scientific pin **`c47e13e4aba0e006366f989d6334d443f6333ae3` remains frozen**. P000 applies to native-world claims; the present external p-adic observer asserts no native X6 identification.

## Inherited exact objects and the new question

Let `p=6m+1>=13` be prime, `n=2m`, `q=q_p(108)=(108^(p-1)-1)/p`, `H_j^{(r)}=sum_(k=1)^j k^(-r)`, and work in `Z_(p)`. Preserve the earlier exact factor identities [source-factor all-precision](https://github.com/awdawmip/enterprise-math/blob/6a09b88e4ca545ef5400e2e80b101028cc2420d8/research_notes/portable_direct/20261025_offphase_d25_source_factor_jet_all_precision.md) and [lifted p² seam](https://github.com/awdawmip/enterprise-math/blob/745e569fc6bf9ccd8803a5cc3f169d3a33d0b335/research_notes/portable_direct/20261025_offphase_d25_lifted_frobenius_p2_seam_universal_third_digit.md):

```text
Q_p(z) = T_p(z)^2 (R_p(z)^2 A_p(z) + L_p(z)),
H_p(z) = A_p(z) + L_p(z),
Q_p(p) = (S_(m+1)-S_m)/p,
T_p(z) = product_(j=1)^(p-1) (1+z/j),
R_p(z) = (1-z)/(1+z/(p-1)),
A_p(z) = 2m*C(z)*K_U(z),
L_p(z) = (3z/220)*B(z)*P_base(z).
```

Here `C(z)=((z+1)(2z-1)^2(30z²+77z+40))/(2(z+2)(2z+1)(4z-1)(4z+5))`; `K_U` is the inherited old-edge compressed factor. In particular `L_p(p) in p Z_(p)` and the four genuine tail-port labels remain in `B*P_base`. This note asks for the **fourth-digit correction** of the compressed scalar `H_p(p)`, beyond the inherited `(4/3)p² mod p³` correction; it does not recompute the original WZ proof.

Define the integral divided harmonic observer
```text
theta_p := H_(p-1)^(2)/p in Z_(p).
```
The integrality follows from `sum_(j=1)^(p-1) j^(-2) = 0 mod p` for `p>3`.

## Theorem (uniform modulo p⁴, all admissible primes)

For **every** prime `p=6m+1>=13`, one has
```text
(S_(m+1)-S_m)/p
  = H_p(p) + (4/3)*p²
    + p³*(37/6 - (4/3)*(q_p(108) + 2*H_n^(1)
                         + H_(n-1)^(1) + theta_p))   (mod p⁴).
```
Every displayed denominator is a p-unit, so this is an integral p-adic congruence. The correction depends on the original Fermat-quotient and finite-harmonic observers; it is **not** a constant universal fourth digit and does **not** supply the missing CM/DP class representative.

### Proof (exact factors, no coefficient-index division)

At the true evaluation point `z=p`, direct algebra gives the **exact** rational relation
```text
R_p(p) = (1-p)^2/(1-2p) = 1 + p²/(1-2p)
       = 1 + p² + 2p³ (mod p⁴).
```
Also
```text
T_p(p) = product_(j=1)^(p-1)(p+j)/j = binom(2p-1,p-1).
```
Let `H_r=H_(p-1)^(r)`. Pairing j with p-j yields
```text
2H_1 = -p H_2 - p² H_3   (mod p³).
```
Finite-field power sums give `H_2 in p Z_(p)` and `H_3 in p Z_(p)`; hence `H_1 in p² Z_(p)`. The ordinary p-adic logarithm, used only in these low unit-denominator degrees, gives
```text
log T_p(p) = p H_1 - (p²/2) H_2 + (p³/3) H_3 (mod p⁴)
           = -p² H_2 (mod p⁴).
```
It follows that, putting `alpha_p=(T_p(p)-1)/p³`,
```text
T_p(p) = 1 + alpha_p p³   (mod p⁴),
alpha_p = -theta_p       (mod p).
```
This establishes Wolstenholme divisibility here without inserting a new axiom.

The compressed old-edge factor has
```text
K_U(z)=(1+qz)^(-1)
       * product_(k=2)^n(1-z/k)^2
       * (1-z)^(-2)
       * product_(j=1)^(n-1)(1+z/j)^(-1).
```
Differentiating at zero, all denominators being p-units,
```text
K_U(0)=1, K_U'(0)=4-q-2H_n^(1)-H_(n-1)^(1),
C(0)=-2, C'(0)=3/4.
```
Consequently
```text
A_0=A_p(0)=-4m,
A_1=A_p'(0)=2m*(-29/4+2q+4H_n^(1)+2H_(n-1)^(1)),
A_p(p)=A_0+p A_1 (mod p²).
```
The exact port-preserving difference is
```text
Q_p(p)-H_p(p)
 = (T_p(p)² R_p(p)²-1)*A_p(p)
   + (T_p(p)²-1)*L_p(p).
```
The second term is in `p⁴ Z_(p)` because `T_p(p)²-1` is divisible by `p³` and `L_p(p)` by p. In the first term,
```text
T_p(p)² R_p(p)² - 1
 = 2p²+(4+2alpha_p)p³ (mod p⁴).
```
Therefore
```text
Q_p(p)-H_p(p)
 = 2A_0 p² + (2A_1+(4+2alpha_p)A_0)p³  (mod p⁴).
```
Use `2A_0=-8m=(4/3)-(4/3)p`, `A_0=(2/3) mod p`, `2m=-1/3 mod p`, and `alpha_p=-theta_p mod p`. The p³ coefficient after extracting the inherited `(4/3)p²` is exactly
```text
37/6 - (4/3)*(q+2H_n^(1)+H_(n-1)^(1)+theta_p) mod p.
```
The inherited `Q_p(p)` source identity finishes the proof. This is a rational/p-adic proof for every declared prime, not an inference from the tests below.

## Exact author regression (separate port paths)

Standard-library-only integer/`Fraction` arithmetic was executed for **all 79 primes `13<=p<1000`, `p=1 mod 6`**. For all 79, the direct exact old-edge value `(T²R²-1)*A(p)` produced the theorem's p⁴ residue; the test compares it with an independently assembled harmonic/Fermat quotient expression. In 14 target primes `13<=p<=139`, a second author check assembled the genuine four-tail compressed factor `L(p)` separately and verified its entire contribution `(T²-1)L(p)` vanishes modulo p⁴. This is *author* source-factor validation (79/79 and 14/14), neither an independent Driver pass nor an original-factorial/native-CM experiment.

| p | 13 | 19 | 31 | 37 | 43 | 61 | 67 | 73 | 79 | 97 | 103 | 109 | 127 | 139 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| p³ coefficient modulo p | 5 | 1 | 6 | 7 | 5 | 17 | 4 | 24 | 18 | 73 | 65 | 76 | 24 | 127 |

Minimal executable regression for the all-79 path (Python 3, no external packages):
```python
from fractions import Fraction as F
from math import comb, isqrt

def h(n, power=1):
    return sum((F(1, j**power) for j in range(1, n+1)), F(0))

def residue(x, mod):
    return x.numerator * pow(x.denominator, -1, mod) % mod

def c(z):
    return F((z+1)*(2*z-1)**2*(30*z*z+77*z+40),
             2*(z+2)*(2*z+1)*(4*z-1)*(4*z+5))

def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))

def check(p):
    assert p >= 13 and p % 6 == 1 and prime(p)
    m, n = (p-1)//6, (p-1)//3
    q = (108**(p-1)-1)//p
    T = comb(2*p-1, p-1)
    assert (T-1) % p**3 == 0
    R = F((p-1)**2, 1-2*p)
    K = F(1, 108**(p-1)*(1-p)**2)
    for k in range(2, n+1):
        K *= F((k-p)**2, k*k)
    for j in range(1, n):
        K *= F(j, j+p)
    A = 2*m*c(p)*K
    actual = residue((T*T*R*R-1)*A, p**4)
    base = residue(F(4, 3)*p*p, p**4)
    assert (actual-base) % p**3 == 0
    delta = ((actual-base) % p**4) // p**3
    H2 = residue(h(p-1, 2), p*p)
    assert H2 % p == 0
    theta = H2 // p
    expected = residue(F(37, 6)-F(4, 3)*(q+2*h(n)+h(n-1)+theta), p)
    assert delta == expected, (p, delta, expected)
    return delta

targets = [p for p in range(13, 1000) if p % 6 == 1 and prime(p)]
assert len(targets) == 79
for p in targets:
    check(p)
print("79/79 PASS")
```

## Status, dependencies, next action

The full original WZ identity, source-factor jets, prior p and p² seams, full-port low-precision formula and another Researcher's Source Hesse/Green/p373 units are **inherited, not re-credited**. No `CLAIM`, native experiment, Source checkpoint, Result/freeze, reviewer independence or mathematical admission is implied by this portable file. The `em_control_continuation` query in this run returned `CONTROL_QUOTA`; current Sites identity is read-only and no own verified service execution key or winning claim is available. A different Researcher's `latest_checkpoint.json` cannot be adopted as our authority. This file is a neutral, review-pending external arithmetic observer and should be attached to a lawful Source continuation only after actual claim/session verification.

UR V2 remains separate: the original four-file artifact is historically 94,687 bytes with required SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; no authentic matching source bytes or upload/receipt were recovered in this run. Do not reconstruct these original bytes from the digest or redo completed UR mathematics. Required next action: recover original V2 location and original request/staging receipt, verify exact 94,687-byte bundle hash, then supply legitimate writer/provenance/checkpoint. D25 still requires actual same-prime, same-original-class H0/B0 divided-power/Frobenius representative, `[X]U mod p²`, semilinearity, `eta` normalization, and bridge to the inherited `kappa/Delta_p-R_p`. The current theorem proves none of those native dependencies.
