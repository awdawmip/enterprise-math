# JT2 / UR — Frobenius-drift correction and a lift-invariant norm–jet scalar

Date: 2026-11-16. **PROVED SCOPED ALGEBRAIC REDUCTION / SOURCE-EXPOSED DRIVER AUTHOR SIDE**, not independent Native Result review, formal check, or a proof of the uniform UR congruence.

Author of the present calculation: the existing line Driver `EM-DVR-DEBB5E` using the real session `MCP-9b4714dc46b948afa4875a86c89c713c`. The original UR Legendre/norm–jet problem and frozen reduction belong to `EM-JT2-EF9380`; earlier admitted stage review to `EM-DVR-57CCCE`. The lift sensitivity and all-order balancing-root proofs already published by this Driver are **reused**, not counted here as new proofs. This note adds an explicit Frobenius-lift correction and canonical lift-independent scalar.

## 1. Fixed inputs, domain and statement

Let `p>3` be prime, `p≡13 or 19 (mod 24)`, `n=(p-1)/3=2m`; write the **ordinary** Legendre polynomial as `P_n(X)=Q_m(X^2)` with coefficients in `Z_(p)`. Put

```text
J_m(Y)=Σ_{r=0}^{2m} [Y^r](Q_m(Y)^2) Y^r/(2r+1).
E_p(a)=18 (Q_m(a)/p)Q_m'(a)-2J_m(a)-3      (mod p).
```

Here `E_p(a)` is defined only when `Q_m(a)≡0 (mod p)`. The denominators of `J_m` are p-units since `4m+1=2n+1<p`. The previously proved ordinary-Legendre separability gives `d=Q_m'(β)≠0 (mod p)` at each mod-p root `β`. We will first allow any nonzero **nonsquare** mod-p root `β` of `Q_m`, then specialize to the frozen `β=1/2`. In the specified prime classes, `(2/p)=-1`, so the latter is indeed nonsquare.

For a chosen `p`-integral lift `a≡β (mod p)`, define the anti-Frobenius drift

```text
D_p(a) = (a^((p-1)/2)+1)/p                 (mod p).
H_p(β) = E_p(a)-36 β d^2 D_p(a)            (mod p).
```

The quotient defining `D_p` is legal by Euler's criterion. **Theorem A:** `H_p(β)` is independent of the chosen lift `a` of `β` modulo `p²`. In particular, it is an invariant of the fixed root and the specified full Legendre/J polynomial, not a new free scalar or an extra axiom.

Let `a_T≡a^p (mod p²)` be the unique Teichmüller representative of `β` modulo `p²`. **Theorem B:**

```text
a_T^((p-1)/2) ≡ -1 (mod p²),  D_p(a_T)=0,
H_p(β)=E_p(a_T).
```

At the original fixed rational port `a_0=1/2`, put the Fermat quotient `q_p(2)=(2^(p-1)-1)/p mod p`. **Theorem C (exact second-digit decomposition):**

```text
D_p(1/2) ≡ q_p(2)/2                           (mod p),
a_T ≡ 1/2 - p q_p(2)/2                        (mod p²),
epsilon_p = E_p(1/2)
         ≡ H_p(1/2) + 9 q_p(2) Q_m'(1/2)^2  (mod p).
```

Consequently the full UR target `epsilon_p=0` for all admissible primes is **equivalent**, not proved, to the arithmetic identity

```text
E_p(a_T) ≡ -9 q_p(2) Q_m'(1/2)^2 (mod p).
```

This splits the frozen rational-port second digit into a canonical residue-lift contribution and an explicit Fermat-quotient drift. Neither term may be dropped when lifting `t^p=-t (mod p)` to precision `p²`, where `t²=1/2`.

## 2. Proof of Theorems A–C

Put `r=(p-1)/2`. If `a' = a+pλ`, the binomial theorem yields

```text
D_p(a')-D_p(a) ≡ r a^(r-1) λ
              ≡ [(-1/2)(-β^(-1))] λ
              ≡ λ/(2β)                       (mod p).
```

We used `a^r≡-1 (mod p)`. The prior exact Taylor computation for the *same full* `Q_m,J_m` gives

```text
E_p(a')-E_p(a) ≡ 18λd²                  (mod p).
```

Subtracting `36βd²` times the first difference proves Theorem A. No independent coefficient freedom is assumed.

For `a_T=a^p` modulo `p²`, Fermat's little theorem gives `a^(p-1)=1+pc` for some p-adic integer `c`, so

```text
a_T^(p-1) ≡ (1+pc)^p ≡1 (mod p²).
```

As `a_T^r≡-1 (mod p)` and `(a_T^r)^2≡1 (mod p²)`, the odd-prime factorization `(x-1)(x+1)` implies `a_T^r≡-1 (mod p²)`. Hence `D_p(a_T)=0`, and Theorem A yields Theorem B. The representative `a^p` mod `p²` is independent of changing `a` by `pλ`.

At `a_0=1/2`, let `z=2^r`, so `z≡-1 (mod p)` because `(2/p)=-1`. Since `z²=1+pq_p(2)` exactly, write `z=-1+ps`; then `s≡-q_p(2)/2 (mod p)`, and inversion gives

```text
(1/2)^r = z^(-1) ≡ -1 + p q_p(2)/2 (mod p²).
```

Thus `D_p(a_0)=q_p(2)/2`. Also `a_T=a_0^p=a_0 (2^(p-1))^(-1)≡a_0-pq_p(2)/2`. Plug `β=1/2` into `H_p(β)` to obtain `epsilon_p=H_p(1/2)+9q_p(2)d²`. This proves Theorem C.

**Square-root port interpretation (typed correctly):** for any `t²=a` in the unramified quadratic extension, `t^p=t,a^r`. Consequently, at the frozen rational `a=1/2`,

```text
t^p ≡ -t + p (q_p(2)/2)t (mod p²).
```

The familiar `t^p=-t` is only a mod-p equality for that fixed rational port. The polynomial/norm–jet obstruction is **not** inferred from anti-fixation alone.

## 3. Two exact checks using a separate polynomial calculation

For `p=13`, `Q_2(Y)=(35Y²-30Y+3)/8`; exact rational modular evaluation gives `u=Q_2(1/2)/p=2`, `d=12`, `J_2(1/2)=0`, `epsilon=0`; `q_p(2)=3`, `D_p(1/2)=8`, and `H=12` in `F_13`. On the shifted lift `a'=1/2+13`, `E_p(a')=5`, `D_p(a')=9`, and `H=5-18·12²·9=12`. The Teichmüller lift gives `E_p(a_T)=12`.

For `p=19`, `Q_3(Y)=(231Y³-315Y²+105Y-5)/16`; exact rational modular evaluation gives `u=4`, `d=17`, `J_3(1/2)=12`, `epsilon=0`; `q_p(2)=3`, `D_p(1/2)=11`, `H=6` in `F_19`. At `a'=1/2+19`, `E_p(a')=15`, `D_p(a')=12`, giving the same `H=6`; the Teichmüller lift gives `E_p(a_T)=6`.

These are auxiliary exact rational/integer checks for the displayed identities, **not** an all-prime test or theorem proof. Theorem A–C already follow from the symbolic p-adic argument.

## 4. Meaning, contribution and uncompleted target

This new statement **does not** prove `epsilon_p(1/2)=0` for every admissible prime, give a new native Result admission, or satisfy the UR task/mother objective. It pinpoints the precise Fermat-quotient correction between (i) a mod-p Frobenius-anti-fixed square-root port and (ii) the original fixed rational lift. The canonical nonzero lift-invariant value `H_p` is not equivalent to UR vanishing without its explicit correction term. A useful next arithmetic route is to evaluate the full Legendre polynomial and polynomial norm at the Teichmüller lift and compare to `-9q_p(2)d²`. This is a conditional reformulation, not a claim of novelty over external prior art.

Frozen parent Result: `RR-60983E048B55C2AC7F66` / `research_returns/EMW59A_JT2_UR_SUN_PARITY_DEFECT_RETURN_EF9380_20260910.md` at `969846f1d451b3e086f34a19b217e333c8a90c8d`. Original stage review: `driver_reviews/JT2_UR_NORM_JET_STAGE_REVIEW_57CCCE_20260920.md`. Reused Driver source: `research_notes/driver/2026-11-16_jt2_ur_norm_jet_hensel_lift_sensitivity.md`, `research_notes/driver/2026-11-16_jt2_ur_legendre_automatic_simple_all_order_balanced_hensel.md`. The previous 575-prime computational evidence is independent in status and is not converted into a proof by this argument.
