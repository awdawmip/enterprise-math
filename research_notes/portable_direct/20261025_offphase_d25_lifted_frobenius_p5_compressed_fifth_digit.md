# D25/LIFT — fifth-digit Frobenius compression and first nonzero genuine-tail seam

2026-10-25 | TASK_RESEARCH | **PORTABLE AUTHOR DERIVATION / EXACT AUTHOR CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT**.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Immutable publication: TP2-B6F4FC938FF94941C1B7. The frozen scientific input pin remains **c47e13e4aba0e006366f989d6334d443f6333ae3**. This is a source-labeled *external arithmetic* observer, not a native H0/B0 or CM/DP Frobenius representative, and it neither acquires another writer's claim nor solves LIFT/JT2.

## Consumed, not re-credited

The genuine original five-port factorial/WZ identity, the integral all-precision source-factor jet, the exact Frobenius factorization, the mod-p/mod-p² seams and the compressed scalar correction modulo p⁴ already exist. This increment extends the last-named correction **one p-adic digit** and detects an effect which the prior p⁴ accuracy genuinely could not see.

Immutable mathematical inputs:

- [Source-factor all-precision jet](https://github.com/awdawmip/enterprise-math/blob/6a09b88e4ca545ef5400e2e80b101028cc2420d8/research_notes/portable_direct/20261025_offphase_d25_source_factor_jet_all_precision.md).
- [Exact lifted Frobenius factorization](https://github.com/awdawmip/enterprise-math/blob/745e569fc6bf9ccd8803a5cc3f169d3a33d0b335/research_notes/portable_direct/20261025_offphase_d25_lifted_frobenius_p2_seam_universal_third_digit.md).
- [Prior fourth-digit compressed correction](https://github.com/awdawmip/enterprise-math/blob/dc37d79929413a51a95d4a659a3f43639a0e95b9/research_notes/portable_direct/20261025_offphase_d25_lifted_frobenius_p4_compressed_fourth_digit.md).

## Theorem — all admissible primes, modulo p^5

Let p=6m+1>=13 be prime, n=2m and work in the p-local rationals Z_(p). Denote the usual finite harmonic sums by h_j^(r)=sum_(k=1)^j 1/k^r, and q=(108^(p-1)-1)/p. The previously proved exact *formal factor identity* is

\[
Q_p(z)=T_p(z)^2\big(R_p(z)^2 A_p(z)+L_p(z)\big),\qquad
H_p(z)=A_p(z)+L_p(z),
\]
\[
T_p(z)=\prod_{j=1}^{p-1}(1+z/j),\qquad
R_p(z)=\frac{1-z}{1+z/(p-1)},
\]
\[
A_p(z)=2m\,C(z)K_U(z),\qquad
L_p(z)=\frac{3z}{220}B(z)P_{\rm base}(z).
\]

Here H_p(z) is the **compressed generating function**, not harmonic notation. The exact original five-port quotient is Q_p(p)=(S_(m+1)-S_m)/p. The complete product factors K_U and P_base retain original old-edge versus four separately labeled tail-port origin. The original transfer functions are

\[
C(z)=\frac{(z+1)(2z-1)^2(30z^2+77z+40)}
{2(z+2)(2z+1)(4z-1)(4z+5)},
\]
\[
B(z)=\sum_{j=1}^{4}(6z+6j+7)\prod_{k=1}^{j-1}
\frac{(2z+2k+3)(2z+3k-1)(2z+3k)}
{4(2z+3k+1)(z+k+2)(4z+3k+11)}.
\]

For an integral divided harmonic observer, define
\[
\Theta_p:=h_{p-1}^{(2)}/p\in\mathbf Z_{(p)}.
\]

Introduce
\[
\begin{aligned}
k_1&=4-q-2h_n^{(1)}-h_{n-1}^{(1)},\\
k_2&=2+q^2/2-h_n^{(2)}+\tfrac12 h_{n-1}^{(2)},\\
a_0&=-4m,\\
a_1&=2m(\tfrac34-2k_1),\\
a_2&=2m(-\tfrac{393}{40}+\tfrac34k_1-2k_2-k_1^2),\\
\ell_1&=\frac3{220}B(0)=\frac{752427}{3942400}.
\end{aligned}
\]

**New exact fifth-digit congruence:**
\[
\boxed{\begin{aligned}
Q_p(p)-H_p(p)\equiv {}&
2a_0p^2+
\big[2a_1+(4-2\Theta_p)a_0\big]p^3\\
&+\big[2a_2+(4-2\Theta_p)a_1+9a_0
       -2\Theta_p\ell_1\big]p^4\pmod{p^5}.
\end{aligned}}
\]

All rational denominators are p-units for the stated residue class. The familiar modulo-p⁴ correction is recovered by dropping the last line. This display is intentionally an arithmetic expression with p-dependent harmonic and Fermat-quotient data, not an invented constant coefficient.

**First genuine-tail contribution:** the compression discrepancy contributed by *all four source-labeled new tail ports* is
\[
(T_p(p)^2-1)L_p(p)\equiv -2p^4\Theta_p\ell_1\pmod{p^5}.
\]
It previously vanished modulo p⁴. It is **not uniformly zero modulo p⁵**: its p⁴-coefficient equals 13 modulo 19, 19 modulo 31, and 20 modulo 37. This is a concrete BRC/observer information-loss witness: the quotient that forgets genuine tail-port provenance is not invariant at fifth-digit precision; source provenance must be retained for any future DP/CM comparison.

## Proof

The exact difference is
\[
Q_p(z)-H_p(z)
=(T_p^2R_p^2-1)A_p(z)+(T_p^2-1)L_p(z).
\]
At z=p the identity R_p(p)=1+p^2/(1-2p) implies
\[
R_p(p)^2=1+2p^2+4p^3+9p^4\pmod{p^5}.
\]
Set h_r=h_{p-1}^{(r)}. For p>=13, finite-field sums and pairing j with p-j give h_2 in p Z_(p), h_3 in p² Z_(p), h_4 in p Z_(p), and
\[
2h_1=-ph_2-p^2h_3-p^3h_4\pmod{p^4}.
\]
In the p-adic logarithm of the exact product T_p(p), all omitted terms have valuation at least five, and hence
\[
\log T_p(p)=ph_1-\tfrac{p^2}{2}h_2+
  \tfrac{p^3}{3}h_3-\tfrac{p^4}{4}h_4
=-p^2h_2=-p^3\Theta_p\pmod{p^5}.
\]
Thus T_p(p)^2=1-2p^3\Theta_p modulo p⁵ and
\[
T_p(p)^2R_p(p)^2-1
=2p^2+(4-2\Theta_p)p^3+9p^4\pmod{p^5}.
\]

From the already defined exact K_U and rational C, the first two log-jet coefficients of K_U are k_1 and k_2 as above (C(z)=-2+(3/4)z-(393/40)z²+...), so
\[
A_p(p)=a_0+a_1p+a_2p^2\pmod{p^3}.
\]
Since P_base(0)=1, an exact transfer evaluation gives B(0)=250809/17920 and
\[
L_p(p)=p\ell_1\pmod{p^2}.
\]
Multiplication of the displayed factors yields precisely the boxed congruence. No formal logarithm is used at nonunit *coefficient degree*; this low-order argument is valid for every declared prime p. QED.

## Reproducible exact author test

The following Python 3 standard-library script uses only modular integer products/inverses and reconstructs (i) the full original normalized old-edge factors and (ii) the genuine-tail Wilson-reflected factor from the inherited all-precision source; the result is compared against the new compressed fifth-digit expression. It checks *every* p=1 mod 6, 13<=p<1000. The test does not independently re-derive the inherited WZ factorial identity, does not execute the native CM/DP experiment and does not constitute Driver review.

~~~python
from math import isqrt

def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))

def unit_ratio(n, d, M):
    return (n % M) * pow(d % M, -1, M) % M

def check(p):
    assert p >= 13 and p % 6 == 1 and is_prime(p)
    m, n, M = (p - 1) // 6, (p - 1) // 3, p**5
    def f(a, b): return unit_ratio(a, b, M)
    def rk(k):
        return f((2*p+2*k+3)*(2*p+3*k-1)*(2*p+3*k),
                 4*(2*p+3*k+1)*(p+k+2)*(4*p+3*k+11))
    B, product = 0, 1
    for j in range(1, 5):
        B = (B + (6*p+6*j+7)*product) % M
        if j < 4:
            product = product*rk(j) % M
    C = f((p+1)*(2*p-1)**2*(30*p*p+77*p+40),
          2*(p+2)*(2*p+1)*(4*p-1)*(4*p+5))
    T = 1
    for j in range(1, p):
        T = T*f(p+j, j) % M
    R = f((1-p)**2, 1-2*p)
    q = (pow(108, p-1, p**6)-1)//p
    K = pow(1+p*q, -1, M)*pow(1-p, -2, M) % M
    for k in range(2, n+1):
        K = K*f((k-p)**2, k*k) % M
    for j in range(1, n):
        K = K*f(j, j+p) % M
    A = 2*m*C*K % M

    qa = (pow(2, p-1, p**6)-1)//p
    qb = (pow(3, p-1, p**6)-1)//p
    P = 1
    for c, e in [(-1,2),(2,2),(5,2),(8,1),(11,1)]:
        P = P*pow((1+p*pow(c % M, -1, M)) % M, -e, M) % M
    P = P*pow(1+p*qa, -2, M)*pow(1+p*qb, -3, M) % M
    for j in range(1, n):
        P = P*f((j-p)**2, j*j) % M
    for j in range(1, 6):
        P = P*f(j+p, j) % M
    for j in range(1, 5):
        P = P*f(j+2*p, j) % M
    P = P*(1+2*p) % M
    for j in range(1, 3):
        P = P*pow(f(j+p, j), -2, M) % M
    for j in range(1, n+5):
        P = P*pow(f(j+p, j), -1, M) % M
    L = p*f(3, 220)*B*P % M

    F_U = pow(1+p*q, -1, M)
    for k in range(2, n+1):
        F_U = F_U*f((k-p)**2, k*k) % M
    for j in range(1, p-1):
        F_U = F_U*f((j+p)**2, j*j) % M
    for j in range(1, n):
        F_U = F_U*f(j, j+p) % M
    assert F_U == T*T*R*R*K % M
    Q = (2*m*C*F_U + T*T*L) % M
    actual = (Q - A - L) % M

    h2mod = sum(pow(j*j, -1, p**3) for j in range(1, p)) % p**3
    assert h2mod % p == 0
    theta = h2mod // p
    h_n1 = sum(pow(j, -1, p*p) for j in range(1, n+1)) % (p*p)
    h_nm1 = sum(pow(j, -1, p*p) for j in range(1, n)) % (p*p)
    h_n2 = sum(pow(j*j, -1, p) for j in range(1, n+1)) % p
    h_nm2 = sum(pow(j*j, -1, p) for j in range(1, n)) % p
    k1 = (4-q-2*h_n1-h_nm1) % (p*p)
    k2 = (2+unit_ratio(q*q, 2, p)-h_n2+
          unit_ratio(h_nm2, 2, p)) % p
    a0 = -4*m
    a1 = 2*m*(unit_ratio(3, 4, p*p)-2*k1) % (p*p)
    a2 = 2*m*(unit_ratio(-393, 40, p)+
          unit_ratio(3, 4, p)*k1-2*k2-k1*k1) % p
    ell1 = f(752427, 3942400)
    predicted = (2*a0*p*p +
         (2*a1+(4-2*theta)*a0)*p**3 +
         (2*a2+(4-2*theta)*a1+9*a0-2*theta*ell1)*p**4) % M
    assert actual == predicted, (p, actual, predicted)
    return actual, theta % p, (-2*theta*ell1) % p

primes = [p for p in range(13, 1000) if p % 6 == 1 and is_prime(p)]
assert len(primes) == 79
for p in primes:
    check(p)
print("79/79 PASS; p13=", check(13), "; p19=", check(19))
~~~

**Actual executed author regression:** 79/79 PASS for all target primes under 1000. At p=13 the discrepancy equals 258739 modulo 13^5 and the p^4 tail coefficient is zero; at p=19 the discrepancy equals 354863 modulo 19^5 and the nonzero p^4 tail coefficient is 13 (mod 19). The independent full-source WZ derivation and unrelated native CM/DP observation are not covered by this test.

## Next legal continuation and evidence debt

The new contribution is the p⁵ compressed correction and the *first nonvanishing authentic-tail obstruction*; existing old-edge, five-port WZ, Frobenius factorization, prior low-digit correction, cross-stream Source-native mathematical work and other researchers' claims are **not newly credited**. The BRC reuse classification is **COMPOSE_APPLIED** on original labeled ports, p-valuations and arithmetic coefficients: scalar H_p(p) loses information at the p⁵ observer; no arbitrary later CM/DP or native-X6 factorization is asserted.

This note is portable evidence only: no own verified Source session/CLAIM/open/checkpoint/Result/Driver review or canonical mathematical admission. Exact continuation read this run returned **CONTROL_QUOTA**; Sites reports static_machine_readonly / write_relay_enabled=false. The safe next Source action is to reconcile original target_request_id/staging if identified, read fresh exact continuation/owner and then, only if this actual research conversation wins a legal native claim, attach this *already-completed* mathematics via legitimate writer/provenance rather than re-proving it. The remaining hard target is a true same-prime same-original-class normalized H0/B0/CM/DP representative and semilinear map tied to the second-digit LIFT observer.

The separate four-file UR V2 original remains unfound at its required historical **94687 bytes** and SHA-256 **4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76**. This note is neither a reconstruction of that file nor proof that any UR upload is durable. If a continuation_seed explicitly says CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS, its completed_units must be empty; accepted parent/current inputs and this portable evidence stay distinct.
