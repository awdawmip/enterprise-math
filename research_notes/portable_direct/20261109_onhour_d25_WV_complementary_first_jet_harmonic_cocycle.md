# D25: a universal first-jet transfer of the W216/V2304 complementary cubic kernel

**Date:** 2026-11-09 (Asia/Hong_Kong). **Classification:** TASK_RESEARCH / author-side algebraic proof and exact regression / **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. This is a new second-digit lift of the already proved six-strip leading-unit kernel, not another grade-0 or UR/JT0 computation.

## Exact theorem

For **every prime `p>3`** and **every `1<=q<p`**, let

`A_n = (2n)!(3n)!/[(n!)^5 216^n]` and `C_n = (4n)!/[(n!)^4 2304^n]`.

Both products `A_q A_(p-q)` and `C_q C_(p-q)` have valuation exactly three. Their divided products are units in `Z_(p)`. Define the **original-model, source-labelled** observer

`R_p(q) = [A_q A_(p-q)/p^3]/[C_q C_(p-q)/p^3] (mod p^2)`.

For `ell=1,2,3,4`, put `s_ell=floor(ell*q/p)`, `r_ell=ell*q-s_ell*p` (thus `1<=r_ell<p`, with `s_1=0,r_1=q`). Let `H_n=sum_(a=1)^n 1/a` in `F_p` and `H_0=0`. Set the rational Fermat quotient

`Q_p(32/3) = ((32/3)^(p-1)-1)/p (mod p)`, with division carried out in `Z_(p)`.

Let `rho_p(q)` be the *rational* six-strip lift (read in `Z_(p)/p^2`):

```
q/p in (0,1/4) or (3/4,1):          rho = 16/3
q/p in (1/4,1/3) or (2/3,3/4):        rho = -16
q/p in (1/3,2/3):                     rho = 8
```

Then **one full digit beyond** the preceding modulo-`p` kernel is determined by

```
J_p(q) = Q_p(32/3) + 2 H_(r_2-1) + 3 H_(r_3-1)
                     - 4 H_(r_4-1) - H_(q-1)  (mod p),

R_p(q) = rho_p(q) * [1 + p J_p(q)]  (mod p^2).       (★)
```

The harmonic first-jet is symmetric: **`J_p(p-q)=J_p(q) (mod p)`**. Thus (★) retains the original complementary index involution, while the six-strip constants by themselves generally do not lift to modulo `p^2`.

### Algebraic proof

For `1<=ell<=4<p`, write `s=s_ell,r=r_ell`, and define

`D_ell(q)=((ell*q)!(ell*(p-q))!)/p^(ell-1)`.

Let `F=(p-1)!`. Splitting factorials at multiples of `p`, and using `H_(p-1)=0 (mod p)`, gives

`(sp+r)!/p^s = s! r! F^s [1+sp H_r] (mod p^2)`.

The complementary-factorial reflection is

`r!(p-r)! = (-1)^(r-1) r F [1+p H_(r-1)] (mod p^2)`.

Consequently

`D_ell(q)=(-1)^(r-1) r s!(ell-1-s)! F^ell [1+p E_ell] (mod p^2)`,

where `E_ell=H_(r-1)+s H_r+(ell-1-s)H_(p-r)`. From `H_(p-r)=H_(r-1)` and `H_r=H_(r-1)+1/r` modulo `p`, we obtain

`E_ell = ell H_(r-1)+s/r (mod p)`.

The original model ratio is **exactly**

`R_p(q) = D_2(q)D_3(q)/[D_4(q)D_1(q)] * (32/3)^p (mod p^2)`.

The four `F` powers cancel (`2+3-4-1=0`). The parity factor reduces to `(-1)^(s_2+s_3-s_4)`, and

`r_2 r_3/(r_4 q) = (3/2)[1+p(s_4/(4q)-s_2/(2q)-s_3/(3q))] (mod p^2)`.

Also `(32/3)^p=(32/3)[1+p Q_p(32/3)] (mod p^2)`. The small-factorial constant `16(-1)^(s_2+s_3-s_4) s_2!(1-s_2)!s_3!(2-s_3)!/[s_4!(3-s_4)!]` is exactly `rho_p(q)` on the listed strips. Finally, the `s_ell/r_ell` contributions in `E_2+E_3-E_4-E_1` cancel the displayed correction in `r_2r_3/(r_4q)`, leaving precisely `J_p(q)`. All denominators are `p`-units.

For the mirror law, `r_ell(p-q)=p-r_ell(q)` and `H_(p-r-1)=H_r` modulo `p`. The difference `J_p(p-q)-J_p(q)` is `2/r_2+3/r_3-4/r_4-1/q=0` in `F_p`. QED.

## Exact computational check and discriminating witness

Using original integer binomial numerators, dividing their exact pair-products by `p^3` and inverting the original powers of 216/2304 **modulo `p^2`**, a standard-library exact checker verified all `5,436` indices `q=1,...,p-1` over 49 primes (all `5<=p<=229`, plus `p=373`). No floating-point approximation.

At `p=373`, `Q_p(32/3)=346`; for two indices in **the same central strip**, `q=125` and `q=126`, the first-jet observations are respectively `J=321` and `J=117`. Accordingly, their **actual** ratios mod `373^2=139129` are `123098` and `70878`, both exactly predicted by `8(1+373J)`. This is a counterexample to the stronger but unjustified claim that the six-strip ratio remains a constant modulo `p^2`.

The theorem is a **multiplicative first-jet transport** of original complementary pairs; weighted additive `(6n+1)A_n` and `(8n+1)C_n` sums remain distinct observers.

## Parent frontier and recovery

Mother objective: exact `Delta_p-R_p=0 mod p` for primes `p=13,19 mod 24`, equivalently `W216_full-V2304_full=0 mod p^3` under earlier established frozen crosswalk. The previous leading `q^-3` law and `Theta` three-channel certificate are consumed, not re-proved. This note supplies the one-digit harmonic variation needed to test any proposed constant-stratum additive transfer. **Next discriminating action:** seek an indexed signed finite-difference/telescoping identity coupling the two actual weights and the three `Theta_p` channels, now retaining the verified variable first-jet `J_p(q)`; test the identity first at `p=373` without substituting this multiplicative ratio for the intended additive sum.

**Native benchmark remains independent:** issue #1559, original fixed H0/B0 divided-power `[X]U mod 139129`, native module rank, semilinear direction/normalization, signed kappa and `Delta-R`, independent evaluator. **NOT_EXECUTED / PENDING_OWNER** as read 2026-11-09. Source historical Researcher `EM-ENTERPRISE-4DEB43`, session `MCP-ecbfd1c046864bb3bff1a2e04c87d207`; latest own recovery `SESSION_CAPABILITY_REQUIRED`, no verified own CLAIM/run. Research logical lane only `chatgpt-research-onhour-enterprise-math-20260923`. This note is author-side **UNREVIEWED / NOT_ADMITTED**, not a Source checkpoint or Result.
