# D25/LIFT — exact fourth p-adic digit of the authentic WZ terminal unit and old edge

2026-10-24 · Portable TASK_RESEARCH mathematics · **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT**.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Existing task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Logical research-lane label: chatgpt-research-hourly-enterprise-math-20260923 (not a platform-issued session credential). This note is neutral portable evidence, not a canonical Researcher/CLAIM/OPEN, mathematical acceptance, native experiment or fresh dispatch. The native task's frozen source pin is not modified.

## Exact inherited statement and scope

The [earlier source-authentic original terminal-unit proof](https://github.com/awdawmip/enterprise-math/blob/951e226bc06eedee7b5290b11fcd4d404f2ba7fc/research_notes/portable_direct/20261024_offphase_d25_original_terminal_unit_third_digit.md) already obtained the **exact rational identity**
\[
U_m=\frac{2m}{108^{p-1}}
\left(\prod_{k=2}^{2m}(1-p/k)\right)^2
\frac{\left(\prod_{j=1}^{p-2}(1+p/j)\right)^2}
{\prod_{j=1}^{2m-1}(1+p/j)},\qquad p=6m+1\ge13\text{ prime}.
\tag{1}
\]
Here \(U_m=A_mR_{m,4m}/p\) retains the ORIGINAL FIVE/WZ source normalization, and \(E_0/p=U_m C_m\) is the separately labelled old-edge port. The previous theorem proved \(U_m\bmod p^3\), not the fourth digit; its proof, the four authentic tail ports and the original five-port telescoping identity are reused inputs, not new contributions. This note extends only the original terminal and old edge to modulo \(p^4\). It does **not** evaluate the full five-port sum to that precision or settle the same-prime CM/divided-power LIFT observer.

Write \(H_n^{(r)}=\sum_{j=1}^{n}j^{-r}\) and \(H_n=H_n^{(1)}\), understood in the localization \(\mathbf Z_{(p)}\). Define
\[
q=\frac{108^{p-1}-1}{p}\in\mathbf Z,\qquad
T_p=\frac{H_{p-1}^{(2)}}p\in\mathbf Z_{(p)},
\tag{2}
\]
\[
A=4-q-2H_{2m}-H_{2m-1},\qquad
W=4+\frac{q^2}{2}-H_{2m}^{(2)}+\frac12H_{2m-1}^{(2)},\qquad
B=W+\frac{A^2}{2},
\tag{3}
\]
\[
D=\frac{16}{3}-2T_p-\frac{q^3}{3}
-\frac23H_{2m}^{(3)}-\frac13H_{2m-1}^{(3)},
\qquad
C=D+AW+\frac{A^3}{6}.
\tag{4}
\]

## Theorem 1 — all-target fourth digit (new)

For every prime \(p=6m+1\ge13\), the authentic rational terminal unit satisfies
\[
\boxed{U_m\equiv 2m(1+pA+p^2B+p^3C)\pmod{p^4}.}
\tag{5}
\]
Every displayed fraction is \(p\)-integral. The new fourth-digit coordinate is the precisely retained harmonic quotient \(T_p=H_{p-1}^{(2)}/p\) plus two low-index order-three harmonics; it is not assumed to be zero or replaced by a float.

**Proof without a Bernoulli or unverified CM premise.** First, in \(\mathbf F_p\),
\(\sum_{j=1}^{p-1}j^{-2}=\sum j^{-3}=0\), since \(2,3\) are not multiples of \(p-1\). Hence \(T_p\in\mathbf Z_{(p)}\). Pair \(j\) with \(p-j\):
\[
H_{p-1}
=\frac12\sum_{j=1}^{p-1}\left(\frac1j+\frac1{p-j}\right)
\equiv-\frac p2H_{p-1}^{(2)}-\frac{p^2}{2}H_{p-1}^{(3)}
\equiv-\frac{p^2}{2}T_p\pmod{p^3}.
\tag{6}
\]
Removing the last term and expanding \((p-1)^{-r}\) gives the three *exact-precision* congruences
\[
H_{p-2}\equiv1+p+p^2(1-T_p/2)\pmod{p^3},
\quad
H_{p-2}^{(2)}\equiv-1+p(T_p-2)\pmod{p^2},
\quad H_{p-2}^{(3)}\equiv1\pmod p.
\tag{7}
\]
All denominators in (1) are \(p\)-units. Expand its formal \(p\)-adic logarithm in \(\mathbf Z_{(p)}\) to degree three:
\[
\begin{aligned}
\ell:=\log\frac{U_m}{2m}\equiv{}&
p[-q-2(H_{2m}-1)+2H_{p-2}-H_{2m-1}]\\
&+p^2[q^2/2-H_{2m}^{(2)}+1-H_{p-2}^{(2)}+\tfrac12H_{2m-1}^{(2)}]\\
&+p^3[-q^3/3-\tfrac23(H_{2m}^{(3)}-1)+\tfrac23H_{p-2}^{(3)}-\tfrac13H_{2m-1}^{(3)}]
\pmod{p^4}.
\end{aligned}
\tag{8}
\]
Substituting (7), the terms at first, second and third orders are, respectively, \(A,W,D\). The third-order *constant* is \((2-T_p)+(2-T_p)+4/3=16/3-2T_p\); there is no silently dropped Wolstenholme correction. Thus \(\ell\equiv pA+p^2W+p^3D\pmod{p^4}\), and
\[
\exp(\ell)\equiv1+pA+p^2(W+A^2/2)+p^3(D+AW+A^3/6)\pmod{p^4},
\]
proving (5). The logarithm/exponential is used only as a truncated rational polynomial in the \(p\)-adic unit neighborhood, so no real-analytic limit or numerical approximation is involved. QED.

## Theorem 2 — authentic old-edge fourth digit (new)

The *original* exact rational Gosper/WZ coefficient, inherited rather than replaced, is
\[
C_m=\frac{(p+1)(2p-1)^2(30p^2+77p+40)}
{2(p+2)(2p+1)(4p-1)(4p+5)}.
\]
Taylor division with \(p\)-unit denominators gives the additional coefficient
\[
\boxed{C_m\equiv-2+\frac34p-\frac{393}{40}p^2-\frac{10051}{400}p^3\pmod{p^4}.}
\tag{9}
\]
Consequently
\[
\boxed{\begin{aligned}
\frac{E_0}{p}\equiv2m\bigg[&
-2+p\left(\frac34-2A\right)
+p^2\left(-\frac{393}{40}+\frac34A-2B\right)\\
&+p^3\left(-\frac{10051}{400}-\frac{393}{40}A+\frac34B-2C\right)
\bigg]\pmod{p^4}.
\end{aligned}}
\tag{10}
\]
The labelled full seam is still \(S_{m+1}-S_m=E_0+E_1+E_2+E_3+E_4\), and the \(E_1,\dots,E_4\) order-\(p^4\) contributions are **not** supplied by this result. Nor is this a same-prime proof of \(\Delta_p-R_p\).

## Exact author-run falsification checks

The standalone Python-stdlib checker below rebuilt the authentic original factorial unit *without* using (1), rebuilt (1) independently, checked their equality as rational numbers, checked (5) and (9) modulo \(p^4\), and checked the original exact old edge against (10). The actual check covered **all 79 primes \(13\le p<1000\) with \(p\equiv1\pmod6\)**: 79/79 exact-rational/projection matches, zero failures. This is a regression scope, not the all-prime proof; the proof is (1) together with (6)–(10).

Representative original-residue witnesses, columns ordered \(p\), \(U_m\bmod p^4\), \(C_m\bmod p^4\), \((E_0/p)\bmod p^4\):

| p | U_m | C_m | E_0/p |
|---:|---:|---:|---:|
| 13 | 12029 | 50 | 1669 |
| 19 | 75797 | 71400 | 65633 |
| 31 | 396593 | 283276 | 796060 |
| 37 | 1271036 | 86615 | 691839 |
| 67 | 15797483 | 13708332 | 16629222 |
| 211 | 1134527236 | 115342937 | 1603281883 |

## Scoped BRC/Enterprise observer and unfinished work

**COMPOSE_APPLIED:** retain the integer prime, explicit valuation, original factorial identity of the \(U_m\) port, source \(C_m\), and labels \(E_0,\dots,E_4\). The scalar mod-\(p^4\) projection discards original tail labels unless retained separately. The new \(T_p\) is a one-digit repair relative to the third-digit terminal observer, not proof that the total-only observer is sufficient for future CM/DP operations. The current classical rational computation introduces no six-axis Heartbeat dynamics, time coordinate, primitive triadic-force closure, Frobenius source normalization or project axiom.

Do not redo accepted D24 UR/JT0 or previous WZ third-digit proofs. Native successor first needs its own authorized Source session/RA/claim/open and the unchanged Source checkpoint; ordinary period coefficient 6 does not determine exact lifted \(c_p\) or \(\kappa_p\). The separate user-designated four-file UR V2 original bundle remains **UNVERIFIED / NOT LOCATED** at 94,687 historical bytes and SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76; no original-byte match or native writer/provenance is asserted. The existing Sites adapter is static read-only and this round's exact Source continuation attempt hit transient CONTROL_QUOTA. There was no replay, no new Source session, CLAIM, OPEN, checkpoint, frozen result, reviewer action, scheduler or automation configuration change.

## Reproducible stdlib checker

Save the following indented code as an independent .py file and run with Python 3. Its intended test domain and operations are explicit; no floating point or third-party packages.

    from fractions import Fraction as Q
    from math import factorial, gcd, isqrt
    
    def H(n, k):
        return sum((Q(1, j**k) for j in range(1, n+1)), Q(0))
    
    def residue(z, modulus):
        z = Q(z)
        assert gcd(z.denominator, modulus) == 1
        return z.numerator * pow(z.denominator, -1, modulus) % modulus
    
    def original_factorial_U(p):
        m = (p-1)//6
        x = Q(1, 108**(p-1) * factorial(2*m) * factorial(4*m)**2)
        for j in range(1, p-1):
            x *= (p+j)**2
        for j in range(1, 2*m):
            x /= p+j
        return x
    
    def exact_product_U(p):
        m = (p-1)//6
        x = Q(2*m, 108**(p-1))
        for k in range(2, 2*m+1):
            x *= (1-Q(p,k))**2
        for j in range(1, p-1):
            x *= (1+Q(p,j))**2
        for j in range(1, 2*m):
            x /= (1+Q(p,j))
        return x
    
    def exact_edge_coefficient(p):
        return Q((p+1)*(2*p-1)**2*(30*p*p+77*p+40),
                 2*(p+2)*(2*p+1)*(4*p-1)*(4*p+5))
    
    def fourth_digit_units(p):
        m = (p-1)//6
        q = (108**(p-1)-1)//p
        T = H(p-1,2)/p
        A = 4-q-2*H(2*m,1)-H(2*m-1,1)
        W = 4+Q(q*q,2)-H(2*m,2)+Q(1,2)*H(2*m-1,2)
        B = W+A*A/2
        D = Q(16,3)-2*T-Q(q**3,3)-Q(2,3)*H(2*m,3)-Q(1,3)*H(2*m-1,3)
        C = D+A*W+A**3/6
        u = 2*m*(1+p*A+p*p*B+p**3*C)
        c = -2+Q(3,4)*p-Q(393,40)*p*p-Q(10051,400)*p**3
        edge = 2*m*(-2+p*(Q(3,4)-2*A)
                    +p*p*(-Q(393,40)+Q(3,4)*A-2*B)
                    +p**3*(-Q(10051,400)-Q(393,40)*A+Q(3,4)*B-2*C))
        return u, c, edge
    
    def prime(n):
        if n < 2:
            return False
        for d in range(2, isqrt(n)+1):
            if n%d == 0:
                return False
        return True
    
    ps = [p for p in range(13,1000,6) if prime(p)]
    for p in ps:
        mod = p**4
        u0 = original_factorial_U(p)
        c0 = exact_edge_coefficient(p)
        u, c, edge = fourth_digit_units(p)
        assert u0 == exact_product_U(p), p
        assert residue(u0-u,mod) == 0, p
        assert residue(c0-c,mod) == 0, p
        assert residue(u0*c0-edge,mod) == 0, p
    assert len(ps) == 79
    print("79/79 exact original terminal and old-edge mod p^4: PASS")
