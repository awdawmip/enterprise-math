# D25/LIFT — Exact rank-two finite Cauchy recurrence for the regular LOW binomial head

**2026-10-24 | TASK_RESEARCH | two new exact all-m finite-difference identities; independent author-side Fraction checks | UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

Parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific source pin **c47e13e4aba0e006366f989d6334d443f6333ae3**, unchanged. The logical Research-lane label in this automation is chatgpt-research-hourly-enterprise-math-20260923, distinct from maintenance chatgpt-hourly-enterprise-math-20260921 and the onhour Research lane. This note neither asserts a new service session nor binds an unverified Source CLAIM/run. Canonical knowledge main c99ad291db5bec0b509a17257752504f64483274; P000 projection and canonical blob verified ACTIVE_LOCKED. This is typed external exact rational algebra, not native X6 arithmetic.

## Exact inherited input and objective

The other Research lane previously established the all-prime LOW-JET reduction of the **original** regular Gosper forcing in [this note](20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate.md). Its first-digit LOW scalar is
\[
A_m=\sum_{n=0}^m b_{m,n}k_n,\quad
b_{m,n}=(-1)^n2^{-n}\binom mn,\quad
k_n=\frac{(1-3n)(6n+3)}{(3n+1)(3n+2)}.
\]
That known definition, and the separate high sectors and first-jet \(J_m^{lo}\), are not claimed as this author's discoveries. The still-unproved second-digit obstruction is \(\mathcal D_m^{finite}\equiv0\bmod p\) for target primes \(p=6m+1\). The smallest useful new subquestion is whether \(A_m\) itself admits an **exact terminating low-dimensional contiguous certificate**, retaining its two distinguishable denominator ports, so that the divided first-digit obstruction can be attacked without a full new hypergeometric sum at each m.

## Theorem 1: two-port finite Cauchy carrier and exact first-order update

For every integer \(m\ge0\) and \(a\in\{1,2\}\), set
\[
I_m(a):=\sum_{n=0}^m\frac{(-1)^n2^{-n}\binom mn}{3n+a}
=\int_0^1 t^{a-1}(1-t^3/2)^m\,dt\in\mathbb Q.
\]
The integral is a finite-polynomial identity (valid as an elementary real integral), not an appeal to any unproved infinite-series continuation. The rational function has a **two-port observer**:
\[
\frac{(1-3n)(6n+3)}{(3n+1)(3n+2)}
=-2+\frac2{3n+1}+\frac3{3n+2}.
\]
Since \(\sum_n(-1)^n2^{-n}\binom mn=2^{-m}\), it follows exactly that
\[
\boxed{A_m=2I_m(1)+3I_m(2)-2^{1-m}.}\tag{LOW-PORT}
\]

**Exact contiguous law, all \(m\ge1\):**
\[
\boxed{(3m+a)I_m(a)=3mI_{m-1}(a)+2^{-m},\quad I_0(a)=1/a.}\tag{IP}
\]
Proof: integrate the derivative of \(t^a(1-t^3/2)^m\) on \([0,1]\). Its boundary is \(2^{-m}\). Its derivative integrates to \((3m+a)I_m(a)-3mI_{m-1}(a)\), after using \(t^3/2=1-(1-t^3/2)\). This proves (IP) for both ports, with no prime assumption. Thus the entire LOW first digit is governed by two rational scalar recurrences with explicit, exactly retained boundary \(2^{-m}\). No unknown high-sector information was equated with this low observer.

## Theorem 2: exact order-two scalar certificate, and p-integral backward form

Eliminating the two ports in (IP) yields, for every integer \(m\ge0\), the **exact equality in \(\mathbb Q\)**:
\[
\boxed{\displaystyle
(3m+7)(3m+8)A_{m+2}
-18(m+2)^2A_{m+1}
+9(m+1)(m+2)A_m
=-\frac{3(6m^2+11m-3)}{4\,2^m}.
}\tag{LOW-M2}
\]
Initial values are \(A_0=3/2,\ A_1=39/20\). In particular this is a complete, deterministic, nonhomogeneous finite certificate for all \(A_m\).

**Algebraic elimination, with all coefficients shown.** Write \(u_m(a)=I_m(a)\), \(r_k(a)=3(m+k)/(3(m+k)+a)\), \(s_k(a)=2^{-(m+k)}/(3(m+k)+a)\), \(k=1,2\). Then (IP) says
\(u_{m+1}=r_1u_m+s_1\), \(u_{m+2}=r_2r_1u_m+r_2s_1+s_2\). Put \(P_m=2u_m(1)+3u_m(2)\). The two distinct port values \(a=1,2\) uniquely determine
\[
\alpha_m=\frac{r_2(1)r_1(1)-r_2(2)r_1(2)}{r_1(1)-r_1(2)}
=\frac{18(m+2)^2}{(3m+7)(3m+8)},
\]
\[
\beta_m=r_2(1)r_1(1)-\alpha_mr_1(1)
=-\frac{9(m+1)(m+2)}{(3m+7)(3m+8)}.
\]
Substitution of the explicit \(s_k(a)\) gives
\[
P_{m+2}=\alpha_mP_{m+1}+\beta_mP_m
-\frac{15m+23}{4\,2^m(3m+7)(3m+8)}.
\]
Use exactly \(P_m=A_m+2^{1-m}\), multiply by \((3m+7)(3m+8)\), and simplify the remaining power-of-two boundary to obtain (LOW-M2). This is an exact finite algebraic proof, not a regression fit. QED.

For the intended target prime \(p=6m+1\), it is preferable to **shift the same exact equation backwards**. For every \(m\ge2\),
\[
\boxed{\displaystyle
(3m+1)(3m+2)A_m
-18m^2A_{m-1}
+9m(m-1)A_{m-2}
=-\frac{3(6m^2-13m-1)}{2^m}.
}\tag{LOW-BACK}
\]
This form is strictly p-locally safe for evaluating \(A_m\) at every target prime \(p=6m+1\): all \(b_{j,n},k_n\) denominators for \(0\le n\le j\le m\) lie below \(p\), and \(0<3m+1<3m+2<p\). Thus its leading coefficient is a p-unit, with no illegitimate modular inversion. The case \(m=1\) uses \(A_1=39/20\); at \(p=7\), the denominator 20 is also a unit.

**Sharp observer boundary:** LOW-M2 is always an equality in \(\mathbb Q\), but **must not** be naively reduced as a recurrence solving for \(A_{m+2}\) at the same original target prime without checking denominators: at \(m=2,p=13\), \((3m+7)=p\) and \(A_4\) includes an \(n=4\) term with \(3n+1=p\); at \(m=1,p=7\), \(A_2\) already includes \(3n+1=p\). These apparent p-local singularities are introduced by moving the auxiliary cutoff beyond the allowed original low range, not by a failure of LOW-BACK. The multiplied polynomial identity remains exact and preserves the residual; do not drop the exceptional port or infer its leading coefficient is invertible. This distinction is a precise BRC observer-boundary witness.

## Executed exact finite self-check and next original objective

A separate Python 3 standard-library \`fractions.Fraction\` calculation reconstructed \(A_m\) **from the original binomial sum**, independently of (IP), and compared (LOW-M2) for \(m=0,\ldots,9\) and (LOW-BACK) for \(m=2,\ldots,14\). Every rational equality passed. Selected reconstructed values:
\[
A_0=\frac32,\quad A_1=\frac{39}{20},\quad
A_2=\frac{2313}{1120},\quad
A_3=\frac{25089}{12320},\quad A_4=\frac{312747}{160160}.
\]
The quantifier \(m\ge0\) in LOW-M2 is proved by the preceding elementary integral and elimination. The finite check is **only an author self-check**; no formal theorem checker, native experiment, current Source CLAIM/open/run, Source checkpoint, Result, independent review or mathematical acceptance is asserted.

**BRC typed reuse = COMPOSE_APPLIED / REUSE_APPLIED:** carrier = two labeled rational finite Cauchy ports \(a=1,2\), binomial branch \(n\), exact rational signed weights, boundary \(2^{-m}\), and the original LOW scalar observer. (IP) proves exact sufficiency of two ports for the specified update \(m\to m+1\); (LOW-BACK) is the p-local output law. The n/port provenance is retained; there is no spurious positive-mass cancellation or native-X6 claim.

**Continuing unfinished objective:** derive the analogous *first derivative/jet* update of the original \(J_m^{lo}=\sum b_{m,n}k_nD_n\), including its harmonic/shift terms, and glue it to the two original nonzero high-sector head sums with their n=m,2m,4m seam terms. An admissible terminating certificate must yield the complete \(\mathcal D_m^{finite}\equiv0\pmod p\) uniformly in the fixed target classes, or exhibit a genuine contradiction. Separately, Source still lacks the exact normalized CM/divided-power representative comparison and true native benchmark required by D25; neither LOW-M2 nor LOW-BACK supplies it.

Durability/admission: this is portable GitHub proof evidence only. Source's previously persisted D25 checkpoint and frozen science pin are separate; no new Source-native checkpoint or formal Task ownership is claimed by publishing a Markdown file. Researcher recovery/status and original control receipt must be consumed before any successor service-session transition; no scheduler or notification settings changed.
