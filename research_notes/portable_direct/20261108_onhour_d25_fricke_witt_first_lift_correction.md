# D25 — Exact p-adic Frobenius-versus-power correction at the Fricke CM fiber

Date: 2026-11-08. Classification: TASK_RESEARCH, author-side algebraic lemma **PROVED**, finite exact independent arithmetic **CHECKED**, cross-model first-lift conjecture **OPEN**, native H0/B0 experiment **NOT_EXECUTED**, formal Source **NOT_ADMITTED**.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; **frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3**. Ordinary logical Research lane chatgpt-research-onhour-enterprise-math-20260923 (never maintenance chatgpt-hourly-enterprise-math-20260921). This is an auxiliary external CM calculation. It does not assert original-class X6/H0/B0 or native Frobenius.

## Mother objective and precise unsolved interface

The mother objective is W_p = p (mod p^3) for every prime p = 13 or 19 (mod 24). Previous author-side results establish the finite signed first-lift decomposition C_p/s^epsilon = R_Q+R_L+R_T, with an all-prime zero still unproved. The exact Fricke differential at the two CM fibers is d w / d z = epsilon*(8s/27) where s^2=2, t_epsilon=epsilon*6s, epsilon=±1. Its mod-p matrix exchanges even and odd Frobenius coordinates. The **p-adic lift of that tangent relation** remained unknown; the present result isolates the correction arising from a raw p-th power, without equating that raw operation with Dwork or Cartier Frobenius.

## Theorem: explicit first-lift discrepancy for any quadratic-odd unit

Let p>3 be a prime with (2/p)=-1; for the frozen target this holds for both residue classes 13,19 (mod 24). In the unramified quadratic p-adic algebra K_p=Q_p[s]/(s^2-2), the true unramified arithmetic Frobenius automorphism sigma is sigma(s)=-s and sigma(r)=r for r in Q_p. For a rational p-unit r define its Fermat quotient q_p(r) in F_p by

    r^(p-1) = 1 + p*q_p(r) (mod p^2).

For a=epsilon*r*s, epsilon in {+1,-1}, define the *raw-power discrepancy* D_p(a)=(a^p-sigma(a))/(p*a), reduced modulo p. This quotient is defined since a^p≡sigma(a) (mod p). Then

    D_p(epsilon*r*s) = -q_p(r) - (1/2)*q_p(2) (mod p).       (1)

**Proof:** Since (2/p)=-1, h=2^((p-1)/2) is -1 modulo p, and h^2=2^(p-1)=1+p*q_p(2) modulo p^2. The unique root h congruent to -1 modulo p satisfies h=-1-p*q_p(2)/2 modulo p^2. Also r^(p-1)=1+p*q_p(r) modulo p^2. Therefore

    (epsilon*r*s)^p
      = epsilon*r*s * r^(p-1) * 2^((p-1)/2)
      = -epsilon*r*s*[1+p*(q_p(r)+q_p(2)/2)] (mod p^2).

Subtracting sigma(epsilon*r*s)=-epsilon*r*s and dividing by p*a yields (1). This is an exact finite-modulus argument for every specified p, not an empirical extrapolation.

## Fricke input and tangent: the relative gauge term is rational

For t_epsilon=epsilon*6s and alpha_epsilon=(dw/dz)(t_epsilon)=epsilon*8s/27, define D_t and D_alpha using (1). The Fermat quotient laws q_p(ab)=q_p(a)+q_p(b), q_p(a/b)=q_p(a)-q_p(b) give

    D_t     = -(3/2)q_p(2)-q_p(3),                         (2)
    D_alpha = -(7/2)q_p(2)+3q_p(3).                        (3)

Consequently

    D_alpha - D_t = -q_p(4/81)
                  = -2q_p(2)+4q_p(3) (mod p).             (4)

The ratio alpha_epsilon/t_epsilon is exactly 4/81, independent of the sign of the quadratic CM fiber. Formula (4) is therefore a **source-typed relative Fricke first-lift correction**: the common quadratic-generator discrepancy cancels, while the rational change of tangent scale remains.

The algebraic tangent matrix, or the finite-field parity swap alone, does NOT encode (4) at the next p-adic digit. Conversely, (4) is only the discrepancy between a raw p-th power and the genuine unramified arithmetic Frobenius on the two specified elements. It does not determine the Hasse-quotient, low harmonic or zero-crossing tail ports of the truncated hypergeometric series, nor is it a Dwork/Cartier transport theorem.

## Distinguishing certificates, with observer/representation preserved

Independent exact modular p^2 exponentiation and independent Fermat-quotient arithmetic agree in each of the two conjugate fibers for all 77 target primes p<=2000. The following rows report the scalar D values in F_p, not a norm or an untyped signed cancellation:

| p | q_p(2) | q_p(3) | D_t | D_alpha | D_alpha-D_t | q_p(4/81) |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 3 | 8 | 7 | 7 | 0 | 0 |
| 19 | 3 | 18 | 6 | 15 | 9 | 10 |
| 43 | 25 | 2 | 25 | 26 | 1 | 42 |
| 67 | 10 | 15 | 37 | 10 | 40 | 27 |
| 373 | 204 | 301 | 139 | 189 | 50 | 323 |

The observer is the coefficient of s in Q_p[s]/(s^2-2) divided by p after subtracting sigma; signs epsilon=±1 are independently evaluated. The normalizations in (1)-(4) use p-units (2,3,27,81 and r), so there is no hidden division by p or floating-point approximation.

**Exact p=13 discrimination:** the relative raw-power correction in (4) is zero since (4/81)^12 ≡ 1 (mod 169). Nevertheless the preceding source-preserving Gauss lift has (q_A,L_A,T_A)=(7,3,1), (q_B,L_B,T_B)=(3,12,9); J_A=7,J_B=12, and both scalar transport coefficients t_p=r_p=9 modulo 13. Its signed components are (R_Q,R_L,R_T)=(10,10,6), with 10+10+6=0 modulo 13. Hence R_Q=10 cannot equal c_p*q_p(4/81) for any finite c_p in F_13. A proposed **single-port** transport that attributes the Hasse-quotient mismatch solely to the relative rational raw-power correction is falsified at p=13. This says nothing against a full affine Dwork/Cartier transform with additional q,L,T terms.

## Provenance, validation and next action

Prior exact input and non-repeated work: 20261108_onhour_d25_first_lift_three_port_balance.md; 20261108_onhour_d25_fricke_tangent_parity_exchange.md; the signed p=13 and p=373 Hasse-source data are from the prior independently checked author-side three-port computation. New executable checker d25_fricke_power_vs_witt_check_20261108.py performs modular p^2 powers and Fermat quotients separately, for both conjugate signs on all 77 target primes p<=2000; results PASS. The universal theorem is established by the algebra above, not by the 77 tests.

**Next exact scientific obligation:** construct an affine, p-adically normalized Fricke–Cartier first-lift relation in basis (1,s) that explicitly carries (q,L,T), with (4) as a known raw-power gauge component rather than as the full Hasse correction. At p=13 require survival of nonzero R_Q despite q_p(4/81)=0; at p=19 and p=373 require matching relative corrections 9 and 50, respectively. Prove or falsify the full scalar identity R_Q+R_L+R_T=0 for every p=13,19 (mod 24) before claiming the A-model mod p^2 result.

**Independent native gate:** support issue #1559, original H0/B0 class, p=373 [X]U mod 139129, actual rank/divided powers, Frobenius eta, signed Hesse kappa and independent replication remain PENDING_OWNER and NOT_EXECUTED. No portable Gauss or raw-power calculation closes that gate. No active Researcher claim, run, Result, Source checkpoint or independent mathematical review is asserted. Original continuation request onhour11-20261106-1400-exact-research-lane-continuation remains RUNNING/REVALIDATING and is not replayed.
