# D25 — Universal resonant Legendre primitive and the missing Frobenius carry

Date: 2026-11-10. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Fixed scientific pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`. Source's native frontier remains at `b58330b74576153cdadde5d80a3d92df3a819a0e`. **AUTHOR_SIDE / EXACT_PROOF / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0.**

## 1. Universal theorem: a lost p-adic digit becomes a Frobenius term

Let `p=4q+1` be any odd prime (`q>=1`). In the p-local integer polynomial ring put
\[
P(x)=P_q^{Leg}(1-2x)=sum_{k=0}^{q}c_{q,k}x^k,\quad
Q(x)=P_{3q}^{Leg}(1-2x)=sum_{k=0}^{3q}c_{3q,k}x^k,\quad
c_{n,k}=(-1)^k {n\choose k}{n+k\choose k}.
\]
Both have integer coefficients. Standard terminating hypergeometric coefficients give `Q(x)=P(x) (mod p)`: `-3q \equiv q+1`, `3q+1\equiv-q` modulo p; for `k>q` the second rising factorial has one zero modulo p.

Despite this coefficientwise congruence, the **integrated product** has the exact, uniform mod-p carry
\[
\boxed{
\overline{\int_0^x P(t)Q(t)\,dt}
=\int_0^x\bar P(t)^2\,dt-2x^p
\quad\text{in }\mathbb F_p[x].}\tag{RC}
\]
The left primitive is defined over `Z_(p)`; the right primitive has denominators `1,\ldots,2q+1<p`.

**Proof.** Since `deg(PQ)=4q=p-1`, every antiderivative coefficient has a p-unit denominator except the coefficient of `x^p`. Its numerator is `c_{q,q}c_{3q,3q}`, divisible by p: indeed `v_p({6q\choose3q})=1`. Thus the full primitive is p-integral. Every coefficient below degree p reduces to the primitive of `P^2`, since `Q\equiv P (mod p)`. The only possible discrepancy is `\rho_p x^p`, with
\[
\rho_p=\frac{c_{q,q}c_{3q,3q}}p\pmod p.
\]
Use the exact Legendre orthogonality `\int_0^1 P_q^{Leg}(u)P_{3q}^{Leg}(u)du=0`, changed to `x=(1-u)/2`. Hence `\int_0^1 P(x)Q(x)dx=0`. Likewise `\int_0^1P(x)^2dx=1/(2q+1)=2/(p+1)\equiv2 (mod p)`. Evaluating the primitive discrepancy at `x=1` proves `\rho_p=-2`. QED.

This is an explicit **noncommutation of observation/compression with a subsequent operator**: reducing `Q` modulo p before p-local integration loses the signed contribution `-2x^p`. In typed BRC language, retain all convolution branches `(i,j)` and their weights `c_{q,i}c_{3q,j}` until the primitive; the unique exceptional fiber `i+j=p-1` has `(i,j)=(q,3q)`, numerator valuation one, denominator valuation one, and residual `-2`. This is a signed valuation/observer carry, **not** a positive-mass BRC cancellation.

## 2. A new first-jet Wronskian with the Frobenius boundary intact

Set `J=(Q-P)/p\in Z_{(p)}[x]`. The two Legendre equations imply the **exact** Lagrange identity
\[
\left[x(1-x)(PQ'-P'Q)\right]'=-2pq\,PQ,
\]
because `3q(3q+1)-q(q+1)=2pq`. The boundary at `x=0` vanishes. Divide by p, use `Q=P+pJ`, integrate, and apply (RC):
\[
\boxed{x(1-x)(\bar P\bar J'-\bar P'\bar J)
=-2q\left(I_q(x)-2x^p\right)\quad\text{in }\mathbb F_p[x],}\tag{JW}
\]
where `I_q(x)=\int_0^x\bar P(t)^2dt`.

For any simple root `a\notin\{0,1\}` of `\bar P` in a finite extension, with `D=\bar P'(a)\neq0`, obtain
\[
\boxed{a(1-a)D\bar J(a)=2q\left(I_q(a)-2a^p\right).}\tag{ROOT-J}
\]
Note the second term is indispensable: `I_q(1)=2\pmod p` while `J(1)=0`; omitting it would contradict even the endpoint `x=1`.

## 3. Direct specialization to the original CM(-24) fourth-digit obligation

For primes `p=13 (mod 24)` set `s=1/2-T/3` in `F_p[T]/(T^2-2)`. Here `s^p=1-s`, `s(1-s)=1/36`. Consume the earlier (author-side) Hasse zero `P(s)=0 (mod p)`, simple derivative `D=P'(s)\in F_p^×`, and first-jet identity `4G_p(x)\equiv3P(x)+Q(x) (mod p^2)` for
\[
G_p(x)=\sum_{k=0}^{p-1}\frac{(1/4)_k(3/4)_k}{(k!)^2}x^k.
\]
All divisions by p below occur **after** evaluating integral-coefficient representatives modulo `p^2`. Write `U_p=P(s)/p (mod p)`, `g_pT=G_p(s)/p (mod p)`, and `I=I_q(s)`. By (ROOT-J),
\[
\bar J(s)=\frac{72q}{D}\{I-2s^p\}
=-\frac{18}{D}\{I-2s^p\}\pmod p.
\]
Consequently the previous fourth-digit expression has a distinct, exact primitive form:
\[
\boxed{\frac{G_p(s)}p
=U_p-\frac9{2D}\left(I_q(s)-2s^p\right)\pmod p.}\tag{CM-RC}
\]
The target `Tr A_p(s)=24g_p`, using the already-proved `Tr A_p(s)=36/D`, is **equivalent** to the new explicit Frobenius-corrected Hasse-lift criterion
\[
\boxed{2DU_p-9\left(I_q(s)-2s^p\right)\stackrel?=3T\pmod p.}\tag{CM-TARGET}
\]
This is a strict observer-preserving reformulation of the previous unproved `UD`, not a proof of the all-prime target. It removes the entire degree-`3q` Legendre evaluation from the fourth digit and identifies its necessary `x^p` correction. For odd q the conjugate symmetry yields `I_q(s)+I_q(1-s)=I_q(1)=2`, so `I_q(s)-2s^p` has zero rational trace and retains the odd `T` observer.

## 4. Exact regression and signed CM coordinates

A standard-library integer program checks (RC) and (JW) **coefficient-by-coefficient**, including `\rho_p=-2`; it also computes `P(s)/p`, `J(s)`, `I_q(s)`, and `G_p(s)/p` independently in the quadratic ring modulo `p^2`. All **22** primes `p<1000, p=13 (mod24)` passed. The remaining (CM-TARGET) itself passed those 22 finite tests; universal validity is not inferred.

In the basis `(1,T)` modulo `373`, at the fixed `p=373`, `q=93`:
\[
\rho_{373}=371=-2,\quad D=193,\quad I_q(s)=(1,115),\quad
\bar J(s)=(0,372),\quad U_{373}=(0,22),\quad
G_{373}(s)/373=(0,115).
\]
Thus the independently evaluated left side of (CM-TARGET) minus `3T` is precisely `(0,0)`. The separate even and odd observers and the original p-adic division are all retained.

## 5. Durable scientific frontier

**Proved:** universal p-local signed primitive carry (RC); exact first-jet Wronskian (JW); conditional CM specialization (CM-RC), with its prior fixed input assumptions. **Checked:** 22 target-prime coefficient and ring certificates. **Open:** uniform (CM-TARGET)/(UD); frozen `Delta_p-R_p` parent across both classes; exact native original-class H0/B0 divided-power `[X]U mod 139129`, module rank, Frobenius direction/eta, signed kappa and independent replication. The native benchmark remains `NOT_RUN`, tracked at Issue #1559, with no confirmed executor.

Next discriminating mathematical action: study the p-adic Hasse lift `U_p` against the now isolated Frobenius-corrected primitive `I_q(s)-2s^p` using the original CM isogeny/period port, **without deleting the -2x^p carry**. For native execution, retain the exact fixed H0/B0 task and acquire an authorized executor rather than substituting this auxiliary Legendre calculation.

Classification: `AUTHOR_SIDE_PROVED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`.
