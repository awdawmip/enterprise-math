# D25/LIFT — Frobenius-sparse ALL Hasse-jet cutoff theorem

Date: 2026-10-25. TASK_RESEARCH, author-derived/author-checked portable result; **UNREVIEWED / NOT_ADMITTED / NO_NEW_NATIVE_SOURCE_CHECKPOINT**.
Parent Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; real Research logical lane `chatgpt-research-hourly-enterprise-math-20260923` (not CONTROL_PLANE_MAINTENANCE).
**Frozen scientific Source pin remains** `c47e13e4aba0e006366f989d6334d443f6333ae3`. This auxiliary formal finite-field calculation asserts no CM-original-class native Frobenius experiment and no P000-native X6 transfer.

## Smallest new scientific question

The earlier second-parameter-jet cutoff theorem gave forcing `-4 z^p (mod p)`, and the later third-jet study found a *zero* mod-p forcing with nontrivial `p`-adic residual. Do all higher jets simply vanish, or does a different derivative observer retain terminal source information? Answer **for the full Hasse divided-derivative hierarchy**, not from more finite-prime extrapolation.

For an **odd prime** `p` (in particular `p=6m+1>=7` for D25), put `N=p-1`, `theta=z d/dz` and

\[
 b_n(x)=\frac{(-x)_n(-2x)_n}{(n!)^2},\quad
 \Phi(x,z)=\sum_{n=0}^{N}b_n(x)z^n,\quad
 \mathcal L_x=\theta^2-z(\theta-x)(\theta-2x).
\]
All coefficients are `p`-integral polynomials in `x`: `n<p` makes the factorial denominator a unit.

### Theorem 1: polynomial Frobenius factorization (not merely a pointwise equality)

The *exact truncated differential equation* over the local rationals is
\[
 \mathcal L_x\Phi(x,z)=-\frac{(N-x)(N-2x)(-x)_N(-2x)_N}{(N!)^2}z^p.
\]
After coefficientwise reduction in `F_p[x,z]`, its entire source polynomial is
\[
 \boxed{\mathcal L_x\Phi(x,z)=-2(x^p-x)^2z^p.}\tag{A}
\]
This is a polynomial identity, **not** just equality on the `p` field points (where both sides vanish).

**Proof.** In `F_p[y]`,
\[
 \prod_{j=0}^{p-1}(j-y)=y-y^p,\qquad
 \prod_{j=0}^{p-2}(j-y)=\frac{y^p-y}{y+1}.
\]
The quotient is a polynomial because `y=-1` is a root of the numerator. Applying the same identity to `y=2x` and using `(2x)^p=2x^p` gives
\[
 (-x)_N=(-x)_{p-1}=\frac{x^p-x}{x+1},\qquad
 (-2x)_N=\frac{2(x^p-x)}{2x+1}\quad (\bmod p).
\]
Since `N=p-1=-1` in `F_p`,
`(N-x)(N-2x)=(x+1)(2x+1)`. These factors cancel **as polynomials**; Wilson's theorem gives `(N!)^2=1 (mod p)`. The negative cutoff sign proves (A). The rational recurrence `(n+1)^2b_{n+1}=(n-x)(n-2x)b_n` proves the exact differential equation coefficient by coefficient, including the nonzero terminal coefficient. QED.

### Theorem 2: three surviving Hasse cutoff ports

Fix any integer `m` with `m\bmod p\in F_p`; D25 takes `m=(p-1)/6`. Define the **Hasse parameter jets**
\[
 U_k(z)=[s^k]\Phi(m+s,z)\in F_p[z],\qquad U_k=0\ (k<0).
\]
They are well-defined for all `k` from the coefficient polynomial, including `k>=p` where dividing ordinary derivatives by `k!` is not a legal inverse operation mod `p`.

From (A), since `(m+s)^p-(m+s)=s^p-s` in `F_p[s]`,
\[
 \boxed{-2((m+s)^p-(m+s))^2=-2s^2+4s^{p+1}-2s^{2p}.}\tag{B}
\]
Also
\[
 \mathcal L_{m+s}=\mathcal L_m+s z(3\theta-4m)-2s^2z.
\]
Matching each coefficient of `s^k` yields **for every integer `k>=0`**
\[
 \boxed{
 \mathcal L_mU_k+z(3\theta-4m)U_{k-1}-2zU_{k-2}
 =z^p\left(-2\mathbf1_{k=2}+4\mathbf1_{k=p+1}-2\mathbf1_{k=2p}\right).
 }\tag{C}
\]
Thus the *only* nonzero terminal source Hasse ports over `F_p` occur at orders **2, p+1, 2p**, with coefficients **-2, +4, -2**, respectively. All others have zero forcing; that does NOT state all corresponding solutions `U_k` vanish.

For *ordinary* un-divided derivatives `F_k=(\partial_x^k\Phi)(m,z)`, `F_k=k!U_k` as integral polynomials reduced mod `p`. Therefore the source forcing is `-4z^p` for `k=2` and zero for all `k!=2`; the nonzero `p+1` and `2p` ports are lost by multiplying by their nonunit factorial. This unifies the earlier second-jet `-4` and third-jet first-digit cancellation, and **adds two high-order divided-jet branches**.

At the actual point observer `z=1/2`, the respective Hasse forcing values become `(-1,+2,-1) (mod p)`, using `2^{-p}=2^{-1} (mod p)`. This evaluation is permitted *after* the polynomial equation is derived; `z^p` must not be replaced by `z` before applying `theta`.

**Top-degree boundary check.** Since `deg_x\Phi=2p-2`, `U_{2p}=U_{2p-1}=0`; the leading `x^{2p-2}` coefficient comes only from `b_{p-1}(x)z^{p-1}` and is `2^{p-1}/((p-1)!)^2=1 (mod p)`. Thus `U_{2p-2}=z^{p-1}`, and the last equation `k=2p` reduces to `-2zU_{2p-2}=-2z^p`, independently checking the final port.

## Verification and source/observer type

The adjacent pure-Python checker constructs the actual polynomial numerator factors over `F_p[x]`, multiplies by the exact cutoff polynomial, and checks **every coefficient** against the sparse `2,p+1,2p` support, including a nonzero high Hasse port. Author exact checks passed for `p=7,13,19,31,37,43,73,103,373` (9 cases); this is an illustration, not the reason the general theorem holds.

BRC resolution: **COMPOSE_APPLIED**: retain cutoff rank `p-1`, double-zero parameter source, exact sign, derivative kind (ordinary versus Hasse), coefficient provenance and subsequent `theta`/point-observation scope. Ordinary derivatives do not preserve the high Hasse jet ports. This is a finite-field auxiliary polynomial computation; neither positive-weight BRC nor a native CM Frobenius matrix is claimed.

## Durable continuation: parent remains OPEN

Consumed but not re-credited: existing second/third-jet boundary, harmonic/Fermat lifts, Jacobi-original/Clausen bridge, reflected corner, moment closure and inert self-Green no-go. **New immutable portable unit**: the *complete Hasse cutoff forcing support* and all-order recurrence (A)–(C). It is NOT a predecessor-native `completed_unit` nor an admitted theorem.

**Next smallest scientific unit:** determine whether the genuinely cross-source signed Jacobi/Clausen reflected-corner pairing can use the distinct `p+1` Hasse port as a conserved interface, rather than another self-Green tautology. Keep full `K_p z^p`, rank/jet valuations and finite-horizon observer. The all-target-prime `B_{01,p}+A_2H_0/72-T_{jet,p}=0` remains *unproved*. Original-class `H_0/B_0`, `[X]U mod p²`, Frobenius orientation/normalization and `kappa` mapping remain unavailable; native experiment NOT_RUN, independent review PENDING.

**Control barrier:** prior exact Research-lane continuation/Source recovery has cross-epoch predecessor/checkpoint mismatch; current read attempt returned `INVALID_ARGUMENT / CONTROL_QUOTA`. No current winning CLAIM, open/resume authorization or new native checkpoint established this turn. The actual recovery/support route is Enterprise Math Issue #1558, and no maintenance conversation ID, claim or session has been borrowed. Keep original request receipts, staged evidence and prior contribution history intact. Mother D25/LIFT/JT2 OPEN. No scheduler/notification changes.
