# D25 — Original E3 Tate-parameter differential versus cubic Hasse: exact second-digit correction

Date: 2026-11-08, Asia/Hong_Kong. Status: **AUTHOR-SIDE PROVED / EXACT 8-PRIME TWO-ROUTE CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin **unchanged**: `c47e13e4aba0e006366f989d6334d443f6333ae3`. Input provenance: previous original-E3 cubic Hasse two-jet author note and canonical Source continuation; actual source-exposed, not an independent review.

## Exact original curve and two coefficient observers

For every prime `p>3`, in the p-local quadratic coefficient algebra `Z_(p)[T]/(T²-2)`, fix the **original** Weierstrass curve

\[
E_3:\quad y^2+xy+cy=x^3,\qquad c=(2-T)/108,\qquad T^2=2.
\]

Its invariant differential is `ω=dx/(2y+x+c)`. At infinity take the explicit Tate parameter `t=-x/y` and put `Z=t²x`. The formal branch `Z(0)=1` satisfies

\[
Z^2-(1-t)Z+ct^3=0,\qquad x=Z/t^2,\quad y=-Z/t^3.
\]

Direct implicit differentiation yields

\[
\boxed{\omega=\frac{dt}{\sqrt{(1-t)^2-4ct^3}}.}
\]

Define the *original formal differential coefficient* `B_p(c)=[t^(p-1)](ω/dt)`. Keep it distinct from the previous *original cubic Hasse coefficient*

\[
H_p(c)=[x^{p-1}](4x^3+(x+c)^2)^{(p-1)/2}.
\]

Both use the original parameter `c`. The ordinary Hesse polynomial `A_p(c)` is a third, separately labelled carrier.

## New all-prime exact finite-sum transport

Set `m=floor((p-1)/3)`, `a_k=(3k)!/(k!)³`, `H_k=Σ_{j=1}^k j^(-1)` (`H_0=0`). The binomial theorem in the original Tate parameter gives the *exact p-local identity*

\[
\boxed{B_p(c)=\sum_{k=0}^{m}{2k\choose k}{p-1-k\choose2k}c^k
=\sum_{k=0}^{m}a_k c^k\prod_{j=k+1}^{3k}(1-p/j).}\tag{1}
\]

Consume the previously proved cubic identity

\[
H_p(c)=\sum_{k=0}^{m}a_k c^k\prod_{d\in D_k}(1-p/d),\quad
D_k=\{1,3,\ldots,2k-1\}\sqcup\{2k+1,\ldots,3k\}.\tag{2}
\]

Every denominator is a p-unit (`3k≤p-1`). The first-order logarithmic differences obey

\[
\sum_{d\in D_k}\frac1d-\sum_{j=k+1}^{3k}\frac1j
=\sum_{j=1}^k\frac1{2j-1}-\sum_{j=k+1}^{2k}\frac1j
=\frac12H_k.
\]

Subtracting the two *source-labelled* products proves for **all primes p>3**

\[
\boxed{H_p(c)-B_p(c)\equiv-\frac p2\sum_{k=0}^{m}a_kc^kH_k\pmod{p^2}.}\tag{3}
\]

Therefore `H_p=B_p (mod p)`, but the chosen second-digit coefficient observers have a specific *signed harmonic correction*. For the frozen supersingular target primes `p≡13,19 (mod24)` where accepted CM0 supplies `p|H_p`, also `p|B_p`, and

\[
\boxed{(H_p-B_p)/p\equiv-\tfrac12\sum_{k=0}^m a_kc^kH_k\pmod p.}\tag{4}
\]

The formal curve and coordinate are fixed; this is **not** a native H0/B0 divided-power Frobenius or its `[X]U` coefficient.

## Two-path exact reproducibility; p=373 witness

Checker `research_notes/portable_direct/d25_original_e3_formal_differential_second_digit_check_20261108.py` was actually executed. It computes `B_p` independently from formula (1) and from the differential equation of `f(t)=ω/dt`, yielding a recurrence

\[
2nf_n=2(2n-1)f_{n-1}-(2n-2)f_{n-2}+4c(2n-3)f_{n-3},
\quad f_0=1,\ f_{n<0}=0.
\]

All `2n` in `1≤n<p` are invertible modulo `p³`. It additionally constructs the original cubic Hasse sum directly and tests (3) with modular harmonics. **All eight primes 13,19,37,43,61,67,211,373 passed**, in exact integer algebra `R_3=(Z/p³Z)[T]/(T²-2)`. The executable emits the actual full per-prime data; summary JSON in the same directory.

For `p=373`, `p²=139129`, `p³=51895117`, all tuples in the fixed basis `(1,T)`:

| Original labelled observer | Exact tuple |
|---|---|
| formal `B_373 mod p³` | `(46042747,33130606)` |
| cubic `H_373 mod p³` | `(7225756,36025459)` |
| previously computed ordinary Hesse `A_373 mod p³` | `(34338380,8126924)` |
| **formal `B_373/p mod p²`** | **`(123439,88822)`** |
| **cubic `H_373/p mod p²`** | **`(19372,96583)`** |
| `(H_373-B_373)/p mod p` | **`(0,301)`** |
| `Σ a_kc^kH_k mod p` | `(0,144)` |

Equation (4) holds since `-144/2=301 (mod373)`. The nonzero difference is in the ordered **T-odd** source port. The norm of the original formal quotient is `120550 mod139129`, compared with original cubic quotient norm `134077` and ordinary Hesse quotient norm `122102`: three distinct **ordinary** coefficient observers, none a native Frobenius eigenvalue.

## BRC discipline and honest native boundary

BRC **COMPOSE_APPLIED**. The retained carrier consists of original E3 and c, labelled parameters x/t and index k, p-adic valuation/precision, the original formal/cubic/ordinary Hesse coefficients, signed harmonic residual and permitted future native comparison operation. Mod-p compression identifies B and H, but erases the nonzero second digit, restored by formula (3). This is external elliptic algebra, not a redefinition of P000 X6 or an independent native spatial plane.

The frozen mother target `Δ_p-R_p≡0 (mod p)` in both target classes and the genuine original-class H0/B0 benchmark remain **OPEN**. Existing support Issue **#1559** remains `PENDING_OWNER`. Highest-priority actual next action: run authenticated original H0/B0 divided-power `[X]U mod139129` at p=373 with module rank, semilinear direction/eta, signed Green/Hesse κ and original Δ-R plus independent reproduction; only then compare it with labelled B/H through an explicit proven original-coordinate/DP comparison. This author proof does not replace that experiment.

Native Source: prior read-only request `onhour11-20261106-1400-exact-research-lane-continuation` has `SUCCEEDED` receipt; own `recovery_status` returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`; current Site says `research_authority_granted=false`. No own native Researcher session/CLAIM/run/Result or checkpoint is verified. Author-side only, `UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`. Research lane provenance label `chatgpt-research-onhour-enterprise-math-20260923` is separated from excluded maintenance lane `chatgpt-hourly-enterprise-math-20260921`. No scheduler, scientific pin or predecessor ownership mutated.
