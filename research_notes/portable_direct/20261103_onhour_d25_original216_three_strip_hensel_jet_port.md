# D25 — exact original 216 three-strip Hensel/binomial second-jet port

Date: 2026-11-03 (+08). Status: **AUTHOR-DERIVED / EXACT ALGEBRA PROVED / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This is a portable author-side scientific lemma, not a Source checkpoint, native experiment, Result, review, or claim. Research logical conversation: `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance lane).

## Mother question, strict scope and source separation

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.

The frozen mother objective is `Delta_p-R_p=0 (mod p)` for all prime `p=13,19 (mod 24)`, equivalently the ORIGINAL 216 weighted hypergeometric sum `W216(p-1)=p (mod p^3)`. The objective remains **OPEN**. Consume accepted D24 UR/JT0 and first-digit results. This exact identity concerns only the finite original 216 binomial carrier; the already proved external elliptic E3/E4 de Rham first-jet, the concurrent sibling lane's reciprocal-index 3-atom product theorem, and native H0/B0 are separate sources. No cross-source mathematical identification is asserted.

## Theorem 1 — a finite original coefficient Hensel polynomial

Let `p=6r+1 >= 7` be prime and `a=2r, b=3r, c=4r`. Work throughout in the localization `Z_(p)`; denominators `2,3,k!` for `k<p` are units. The exact original coefficient is

```
B_k = binom(2k,k)^2 binom(3k,k) / 216^k
    = ((1/2)_k (1/3)_k (2/3)_k)/(k!^3 2^k).
```

For each `0<=k<p`, introduce the **explicit auxiliary parameter** `t` with

```
C_k(t) = ((-b+t/2)_k (-a+t/3)_k (-c+2t/3)_k)/(2^k (k!)^3).
```

By the literal equalities `-b+p/2=1/2`, `-a+p/3=1/3`, `-c+2p/3=2/3`, we have **C_k(p)=B_k exactly**, without an approximation. If `C_k(t)=C_{k,0}+t C_{k,1}+t^2 C_{k,2}+O(t^3)` denotes its Taylor polynomial at zero, then

```
W216(p-1) = sum_{k=0}^{p-1} (6k+1) C_k(p)
          = W0 + p W1 + p^2 W2 (mod p^3),
Wj = sum_{k=0}^{p-1} (6k+1) C_{k,j}.
```

Each coefficient of `C_k(t)` belongs to `Z_(p)`; the discarded terms are all divisible by `p^3`. The index `k`, original weight, p-adic valuation, and degree of the Hensel jet are retained.

## Theorem 2 — complete three-strip coefficient formulas (proved)

Exactly three integer roots occur in the three Pochhammer factors, at `j=a,b,c`, hence

```
0<=k<=a:      C_{k,0}, C_{k,1}, C_{k,2} may survive;
a<k<=b:       C_{k,0}=0; C_{k,1}, C_{k,2} may survive;
b<k<=c:       C_{k,0}=C_{k,1}=0; C_{k,2} may survive;
c<k<p:        C_{k,0}=C_{k,1}=C_{k,2}=0.
```

These are algebraic zero statements in `Z_(p)`, not numerical valuation heuristics.

**Low strip** `0<=k<=a`. Set

```
q_k = (-1)^k 2^(-k) binom(b,k) binom(a,k) binom(c,k);
H_k = sum_{j=0}^{k-1} [1/(2(j-b)) + 1/(3(j-a)) + 2/(3(j-c))];
K_k = sum_{j=0}^{k-1} [1/(4(j-b)^2) + 1/(9(j-a)^2) + 4/(9(j-c)^2)].
(C_{k,0}, C_{k,1}, C_{k,2}) = (q_k, q_k H_k, q_k (H_k^2-K_k)/2).
```

**Middle strip** `a<k<=b`. Define

```
U_k = [a! (k-a-1)! b! c!] / [3 (b-k)! (c-k)! (k!)^3 2^k],
H_k^[a] = (1/3) sum_{0<=j<k,j!=a} 1/(j-a)
          + (1/2) sum_{j=0}^{k-1} 1/(j-b)
          + (2/3) sum_{j=0}^{k-1} 1/(j-c).
(C_{k,0}, C_{k,1}, C_{k,2}) = (0, U_k, U_k H_k^[a]).
```

**Upper strip** `b<k<=c`. Define

```
V_k = (-1)^(b+k) [a! b! c! (k-a-1)! (k-b-1)!]
      / [6 (c-k)! (k!)^3 2^k].
(C_{k,0}, C_{k,1}, C_{k,2}) = (0,0,V_k).
```

All factorial and harmonic denominators are p-units because their integer arguments are less than p and the excluded roots are not inverted.

**Proof.** Each factor is `(j-root + alpha*t)`. For the low strip all constants are nonzero, so first- and second-order Taylor product rules yield `H_k` and `(H_k^2-K_k)/2`. In the middle strip the unique zero at `j=a` contributes `t/3`; the nonzero factors give `U_k`, while their logarithmic derivative gives `H_k^[a]`. The integer sign of the product is positive because `a=2r` is even. In the upper strip, exactly two zeros `j=a,b` contribute `(t/3)(t/2)=t^2/6`; the remaining factors have sign `(-1)^(a+b+k)=(-1)^(b+k)`. Beyond `c` all three zero factors are present. The factors reconstruct all coefficients claimed, with no division by a vanishing term. QED.

## Theorem 3 — a six-source weighted law and the sharp live residue

Define six **signed, indexed source ports**, each in `Z_(p)`:

```
L0 = sum_{k=0}^{a}   (6k+1) q_k;
L1 = sum_{k=0}^{a}   (6k+1) q_k H_k;
L2 = sum_{k=0}^{a}   (6k+1) q_k (H_k^2-K_k)/2;
M1 = sum_{k=a+1}^{b} (6k+1) U_k;
M2 = sum_{k=a+1}^{b} (6k+1) U_k H_k^[a];
H2 = sum_{k=b+1}^{c} (6k+1) V_k.
```

Then **for every prime** `p=6r+1>=7`,

```
[THEOREM] W216(p-1) = L0 + p (L1+M1) + p^2 (L2+M2+H2) (mod p^3).
```

The theorem is an exact `p^3` identity in the original weighted finite carrier; it does **not** establish the proposed all-prime `W216=p` residue.

The source-port `H2` coincides modulo p with the already established original 216 high-strip observation `A_p=(sum_{k=(p+1)/2}^{floor(2p/3)}(6k+1)B_k)/p^2`; this is **REUSE_APPLIED** at the exact original input/observable, not newly invented higher-strip output. The existing terminating `4F3` observation therefore evaluates `H2` without replacing the low and middle source terms.

For the frozen two target classes, the **accepted first-digit** `W216=p (mod p^2)` guarantees `L0+p(L1+M1)-p` is divisible by `p^2`. Thus the current second-digit proof obligation is exactly

```
[OPEN] (L0+p(L1+M1)-p)/p^2 + L2+M2+H2 = 0 (mod p),
        p = 13 or 19 (mod 24).
```

It is a proved equivalent reformulation with three distinct order-two carriers (low, middle, upper). It is NOT a proof of the OPEN cancellation. The quotient is taken in `Z_(p)` after the divisibility theorem, never silently on a mod-p-only representative.

## BRC/observer audit and limits

`BRC_COMPOSE_APPLIED / REUSE_APPLIED`: use the prior original 216 coefficient/valuation bands and its terminating upper-strip `4F3` as named exact interfaces; retain `k`, p-adic valuation, root/zero order, six signed contribution ports, original `6k+1` weight and future operations (sum and divided second-digit). Compressing all six ports to a mod-p total early destroys the divided second digit. The new `t` is an auxiliary p-adic shift coordinate, **not** a native ENTERPRISE_X6 axis or a claim about physical continuous reality. No new general tool-family registration, X6 native transfer, or CM period identification is claimed.

The concurrent other researcher lane's reciprocal-index 3-atom moment law concerns the product `B_k B_{p-1-k}`, NOT `B_k` or the scalar sum here. No identification with the frozen `Q_p`, native H0/B0 or the external E3/E4 first-jet is asserted.

## Executed exact checks, finite domain

The accompanying standalone Node.js/BigInt script independently rebuilds EVERY original binomial coefficient `B_k mod p^3`, compares it with the evaluated degree-two auxiliary polynomial recurrence, separately evaluates every low/middle/upper coefficient by factorial and harmonic formulas, checks all triple-zero suffix coefficients, then checks the six-source weighted identity. It **actually ran**, with all assertions passing, for primes `7,13,19,37,43,109,181,373` (788 individual original coefficients).

At p=373, `L2=82, M2=158, H2=266 (mod 373)`; `W0=15521276, W1=16326002, W2=133 (mod 373^3 for W0,W1 and mod 373 for W2)`. The original weighted sum equals 373 modulo `373^3=51895117`; the half-cutoff second digit equals 107 and its high companion equals 266, giving 107+266=373. The latter is a numerical regression of the OPEN all-prime equality, not a universal proof. Results JSON and exact executable source are separate immutable files.

## Durable independent native/control obligations

The exact original fixed `p=373` H0/B0 divided-power native benchmark at Enterprise Math #1559 remains `NOT_EXECUTED / PENDING_OWNER`: genuine `[X]U mod139129`, native module rank, semilinear Frobenius direction/eta, signed Hesse/Green kappa and independent replay. The portable original 216 binomial computation is NOT that native experiment. Control support #1558 remains separate. Current Sites gateway 0.6.11 reports `research_authority_granted=false`, `executor_binding_configured=false` and the exact Source continuation read `CONTROL_QUOTA`; historical request `research-onhour-20261031-0205-dispatch-r15` failed/was missing in current gateway. No session/claim/run/source checkpoint/Result/review was issued by this work; staging kept isolated.

**Next exact mathematical step:** Seek a single terminating WZ/contiguous certificate relating the divisible base-and-first-jet quantity `(L0+p(L1+M1)-p)/p^2` to `-(L2+M2+H2) (mod p)`; preserve individual root crossings `a,b,c`, especially `H2` and its existing terminating `4F3`, while testing the candidate against original `p=13,19,373`. Independently preserve #1559 as the unfinished native proof/experiment rather than counting this auxiliary lemma as its completion.
