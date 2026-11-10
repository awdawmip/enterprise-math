# D25 / W216 — exact exceptional-band cubic Newton transport, grades 2 and 3

Date: 2026-11-10 (Asia/Hong_Kong). Classification: **AUTHOR_SIDE / EXACT ALGEBRAIC PROOF / 10-PRIME TWO-PATH INTEGER CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.

Mother Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication `TP2-B6F4FC938FF94941C1B7`. Scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. No Source Result or native CM computation is claimed.

## 1. Original source and exact grade labels

For prime `p=6m+1>=13`, set

```text
A_k = binom(2k,k)^2 binom(3k,k)/216^k
B_p(a) = sum_{b=0}^{p-1}(6pa+6b+1) A_{pa+b}
C_p(a) = B_p(a)/A_a
q_j = Delta^j C_p(0)
L(f) = f(3)-5f(2)+7f(1)-3f(0) = Delta^3 f(0)-2 Delta^2 f(0).
```

Each original residue index b has *typed* grade `v_b=floor(2b/p)+floor(3b/p)` (0,1,2,3), with no sign loss:
`I0=[0,2m]`, `I1=[2m+1,3m]`, `I2=[3m+1,4m]`, `I3=[4m+1,6m]`.
Let `C_{p,g}(a)` be the sum defining C over `b in Ig`, and `L_g=L(C_{p,g})`. Thus `q3-2q2=sum_g L_g` *exactly*, before reducing modulo any power of p.

## 2. All-grade leading transport lemma (exact symbolic proof)

For `0<=b<p`, write `r2=floor(2b/p)`, `r3=floor(3b/p)`, `s2=2b-pr2`, `s3=3b-pr3`, and `v=r2+r3`. For any nonnegative integer a the p-integral rational quotient satisfies

```text
 A_{pa+b}/A_a = A_b * [(2a+1)_{r2}(3a+1)_{r3}/(r2! r3!)]   (mod p^{v+1}).      (T)
```

Here (x)_r is the ordinary rising factorial; all congruences are in localized integers `Z_(p)`, even if A_a itself has positive valuation.

**Proof.** Define `U_p(n)=product_{1<=j<=n, p does not divide j} j`. Exactly,
`n! = p^{floor(n/p)} floor(n/p)! U_p(n)`.
Apply this to the five factorial factors in `A_{pa+b}/A_a`. The powers of p left after cancelling the macro-index a contribute exactly `p^{r2+r3}`; the macro factorials contribute `(2a+1)_{r2}(3a+1)_{r3}`. Every complete non-p block has residue `(p-1)!=-1 (mod p)`; the total number of complete blocks is `(2a+3a-5a)=0` relative to a=0. Each incomplete block is unchanged mod p, and `216^{-(p-1)a}=1 (mod p)`. Dividing the resulting expression by its a=0 specialization A_b gives (T), including the exact factorial denominators. QED.

## 3. New third-grade theorem: the terminal signed W216 band is unavoidable

For `b in I3`, `r2=1`, `r3=2`, `v=3`. Lemma (T) yields for every a>=0,

```text
 A_{pa+b}/A_a = A_b P3(a) (mod p^4),
 P3(a)=(2a+1)(3a+1)(3a+2)/2.
```

The original signed weight `6pa+6b+1` reduces to `6b+1` at this precision because `p^3 | A_b`. Therefore with `W3=sum_{b in I3}(6b+1)A_b`,

```text
 C_{p,3}(a) = P3(a) W3 (mod p^4),
 L_3 = -108 W3 (mod p^4).                                         (G3)
```

Indeed `(P3(0),P3(1),P3(2),P3(3))=(1,30,140,385)`; applying `L` gives -108.

Reuse the previously proved *all-grade original coefficient reflection*, not as a new theorem:
`W3/p^3 = sum_{h=1}^{2m}(6h-1)/(18 h^3 A_h) (mod p)`.
Consequently an original-grade-zero inverse observer gives the **new cubic-band source port**:

```text
 L3/p^3 = -6 sum_{h=1}^{2m} (6h-1)/(h^3 A_h) (mod p).             (G3-reflect)
```

In particular the signed grade-3 contribution is **not** generally zero: it equals 6 at p=13 and 5 at p=19 after dividing by p^3. Thus a three-band q3-2q2 proof must retain the explicit terminal correction.

## 4. New second-grade first jet and corrected two-band obstruction

For `b in I2`, `r2=r3=1`, `v=2`. Define the harmonic sums `H_n=sum_{j=1}^n 1/j (mod p)`, `H_0=0`, and the Fermat quotient `Q_p(216)=(216^{p-1}-1)/p (mod p)`. Put

```text
 lambda_b = 2 H_{2b-p} + 3 H_{3b-p} - 5 H_b - Q_p(216) (mod p),
 P2(a) = (2a+1)(3a+1).
```

An *additional order* beyond (T) gives the new exact formula

```text
 A_{pa+b}/A_a = A_b P2(a) (1+p a lambda_b) (mod p^4).             (T2)
```

**Proof.** For the p-free full block `D_p(t)=product_{j=1}^{p-1}(tp+j)`, `D_p(t)=(p-1)! (mod p^2)`, because `sum_j 1/j=0 (mod p)`. The `2a+3a-5a=0` full-block excess therefore cancels mod p^2. The incomplete factors have ratios `1+2ap H_{2b-p}`, `1+3ap H_{3b-p}`, and `1+ap H_b` (fifth power in denominator). Finally `216^{-(p-1)a}=1-apQ_p(216) (mod p^2)`. Multiplication proves (T2). Because `p^2|A_b`, the result has the asserted modulus p^4. QED.

Define the original-weighted grade-2 mass and its first harmonic repair:

```text
 W2 = sum_{b in I2}(6b+1) A_b,
 J2 = sum_{b in I2} A_b [6+(6b+1)lambda_b].
```

Using (T2) and retaining the `6pa` signed-weight carry,

```text
 C_{p,2}(a) = P2(a) W2 + p a P2(a) J2 (mod p^4).
```

Now `L(P2)=-24` and `L(aP2)=-56`. Hence the new **all-prime first-jet theorem** is

```text
 L2 = -24 W2 - 56 p J2 (mod p^4).                                 (G2)
```

Combining the proved (G2) and (G3) gives the exact reduced original cubic-Newton obstruction:

```text
 q3-2q2 = L0+L1 -24 W2 -56 p J2 -108 W3 (mod p^4).                (R)
```

It follows that the still-open *uniform* p^4 cubic Newton congruence is equivalent to

```text
 L0+L1 = 24 W2 + 56 p J2 + 108 W3 (mod p^4).                       (R*)
```

This fixes the previously unresolved p^4 proof target without redoing the already completed p^5 falsification. It preserves all four valuations and the original signed observer.

## 5. Reproducible exact checks

The companion standard-library script `d25_w216_grade23_cubic_jet_20261110.py` reconstructs all original coefficients in **two independent paths**: integer binomial formulas and p-free factorial valuation/unit products. For each original b and each a=0,1,2,3 it checks (T2) or (G3), then independently evaluates (G2), (G3), the grade-3 inverse reflection and (R).

All ten tested primes `13,19,31,37,43,61,67,73,109,373` pass. Representative original signed residues:

| p | L2 mod p^4 | L3 mod p^4 | W3/p^3 mod p | L3/p^3 mod p | total L mod p^4 (finite only) |
|---:|---:|---:|---:|---:|---:|
| 13 | 18759 | 13182 | 5 | 6 | 0 |
| 19 | 100358 | 34295 | 4 | 5 | 0 |
| 37 | 1520959 | 202612 | 26 | 4 | 0 |
| 373 | 14213279511 | 9808177113 | 278 | 189 | 0 |

The proof of (T), (G3), (T2), (G2) and (R) is symbolic for all primes p=6m+1>=13; the last column is finite evidence only for the *separate* unsolved cancellation (R*).

BRC application: **COMPOSE_APPLIED**. The carrier is `(original a,b,grade,valuation,unit,signed weight)`; the `L` observer is applied only after recording the separate graded branches, and (R) retains their repair terms. The result is not a native H0/B0 or an independent mathematical review.

## 6. Continuation / authority / missing native experiment

Last exact canonical Source continuation read: `onhour11-20261110-1515-exact-cont` = SUCCEEDED at Source `407d531b4048b4094f317eac892832f847ef621e`. Previous real researcher registration had request `onhour11-20261110-1515-research-session`, issued `EM-ENTERPRISE-43C218` / `MCP-5378d3819d8947bda9049c9428493e2d` but its private capability was lost client-side. A bounded current `recovery_status` probe returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`; a current original receipt probe returned transient `BACKEND_IDENTITY_CHECK_UNAVAILABLE` with `operation_sent=false`. There is **no verified own winning CLAIM/open run**, no Source-native publication/release, and no replayed session registration.

Mother target remains original signed `Delta_p-R_p=0 mod p` for **both** p=13,19 mod24 with immutable Source inputs; native same-original-class fixed H0/B0 divided-power `[X]U mod139129`, rank, semilinear Frobenius and eta, signed odd port, kappa, Delta-R and independent check are still **NOT_RUN/PENDING_OWNER** under existing support Issue #1559. Existing D24 ACCEPTED results and source checkpoint are not recredited. Prior three staging artifacts remain independent provenance.

Next precise mathematical action: prove or find an exact same-object counterexample to (R*) by constructing the **grade-0 and grade-1 jets at p^4**, with the explicit nonzero W2/J2/W3 correction retained. Highest native action remains the exactly pinned #1559 benchmark under an authorized executor, not a surrogate computation. Original session/recovery request must be reconciled by its original ID if the private capability becomes accessible; do not re-register or borrow maintenance lane.
