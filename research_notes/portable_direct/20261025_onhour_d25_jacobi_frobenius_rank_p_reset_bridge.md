# D25/LIFT — first excluded rank Frobenius reset from the Jacobi terminal forcing

**2026-10-25 · TASK_RESEARCH · portable author proof · UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.** Scientific frozen pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`. Original task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. This is neither Source-native checkpoint nor CLAIM/run/Result/review/native benchmark. It extends the **distinct** prior exact terminal coefficient and p³ expansion in `20261025_hourly_d25_terminal_jet_p3_harmonic_fermat.md` at Git commit `b8f3037621f986e5ee78832080c50d0e8ced26c3`. It does not extend the original frozen W sum beyond its legitimate cutoff.

## Full quantified result

For any prime p=6m+1 >=7, put

```text
r_n = (1/6)_n (1/3)_n / (2^n (n!)^2)
w_(p-1) = 2(-1)^m m!(2m)!(5m-1)!(4m-1)! / ((p-1)!)^2
K_p = -40m^2 w_(p-1),    J_p=K_p 2^(-p)
H_s^(2) = sum_(a=1)^s a^(-2), C_m=H_m^(2)/6+H_(2m)^(2)/3.
```

The polynomial Jacobi forcing **K_p z^p** and the evaluated scalar **J_p** are different typed ports; do not replace z^p by z before differential operations.

Define the finite product, with every denominator a p-unit:

```text
E_p = product_(0<=i<p, i!=m) (1 + p/[6(i-m)])
      * product_(0<=i<p, i!=2m) (1 + p/[3(i-2m)]).
```

**Theorem A (exact Q and third digit):**

```text
r_p = -(J_p/72) E_p                              [exact rational]
E_p = 1 + p^2 C_m                      (mod p^3)
r_p = -(J_p/72)(1+p^2 C_m)             (mod p^3).
```

In particular r_p=1/36 (mod p) and r_p=-(J_p/72) (mod p²). **The rank n=p is a p-adic unit**, not a negligible omitted coefficient.

**Proof:** For b_n(x)=(-x)_n(-2x)_n/(n!)², at x=m, both numerator factors vanish simply by rank p and

```text
w_p=b_p''(m)/2=2(-1)^m m!(2m)!(5m)!(4m)! / (p!)²,
p² w_p = 20m² w_(p-1) = -K_p/2                      [exact].
```

At x=m-p/6=-1/6, factor out the two zero factors displaced by p/6 and p/3. Their product is p²/18, whereas the second Taylor coefficient includes a 2; the rest of the factors give exactly E_p. Thus b_p(-1/6)=(p²/36)w_p E_p=-K_p E_p/72 and r_p=2^(-p)b_p(-1/6)=-J_p E_p/72. No illegal p-inversion or formal Taylor expansion at rank p was used.

To get the mod-p³ expression let

```text
L=(H_(5m)-H_m)/6 + (H_(4m)-H_(2m))/3
D=(H_(5m)^(2)+H_m^(2))/36+(H_(4m)^(2)+H_(2m)^(2))/9.
E_p = 1+pL+p²(L²-D)/2                                  (mod p³).
```

For every p>=5, the elementary Wolstenholme and inverse-square sums give H_(p-1)=0 (mod p²), H_(p-1)^(2)=0 (mod p). Reflecting terms 1/(p-j) proves H_(p-1-k)-H_k=p H_k^(2) (mod p²) and H_(p-1-k)^(2)+H_k^(2)=0 (mod p). At k=m,2m these imply L=p C_m (mod p²) and D=0 (mod p). Consequently E_p=1+p² C_m (mod p³). The independently known terminal value J_p=-2 (mod p) implies r_p=1/36 (mod p).

**Theorem B (entire low-rank shifted Frobenius jet):** For 0<=j<=m set

```text
S_j=sum_(i=0)^(j-1) [6/(6i+1)+3/(3i+1)-2/(i+1)]
T_j=sum_(i=0)^(j-1) [36/(6i+1)^2+9/(3i+1)^2-2/(i+1)^2].
```

The exact rational quotient and p³ expansion are

```text
r_(p+j)/(r_p r_j)
 = product_(i=0)^(j-1) [(1+6p/(6i+1))(1+3p/(3i+1))/(1+p/(i+1))²];
r_(p+j) = -(J_p/72) r_j
          [1+p S_j+p²(C_m+(S_j²-T_j)/2)]               (mod p³).
```

**Proof:** divide the exact consecutive rank recurrences for r_(p+i) and r_i. All small-rank denominators are p-units for j<=m. Expand the finite logarithmic product to second order and multiply by A. This retains cross-rank observer data instead of erasing the p² correction.

**Theorem C (complete finite-field block):** For every 0<=j<p, r_(p+j)=r_j/36 (mod p). Induct using the same rational recurrence, as all denominators j+1 and p+j+1 remain units while j<=p-2; no need to invert potentially vanishing numerator factors. For p>=13, exact valuation is v_p(r_(p+j)) = [j>m]+[j>2m]. At **p=7** there is a genuine exceptional extra valuation at index p+m because 7p=p²: v_7(r_(7+j))=2[j>m]+[j>2m]. The modular statement remains valid. The p=7 exception cannot be silently omitted.

## Verified author evidence, limitations and next action

An independently implemented original-integer p-factor recurrence was executed for 95 primes (94 p<1200 and p=19963), with 12,044 shifted low-rank coefficients checked through mod p³. The full residue block mod p, valuation including p=7 exception, and factorial terminal-source checks passed; direct Fraction rational identity passed p=7,13,19. Representative (p,r_p mod p³,J_p mod p³,C_m mod p): (7,239,285,0), (13,82,1701,3), (19,769,3836,6), (211,6975197,5547821,111), (19963,3557648560987,2519162671242,5129). This is **author finite verification**, not independent mathematical review, native benchmark, or a proof of the ultimate LIFT.

Scientific next action is to insert the distinct K_p z^p polynomial port / J_p point port and the correction C_m into a signed Jacobi/formal-adjoint telescoper of `B_01,p+A_2 H_0/72-T_jet,p`, preserving the full Clausen reflected corner and original cutoff. The mother conjecture remains W_p=p (mod p³) for p=13,19 mod24, equivalent to original Delta_p-R_p under the accepted first-digit premises, and **OPEN**. Native same-original-class CM Hasse/[X]U mod p², Frobenius direction/kappa and independent review remain unsatisfied. P000 is unaffected: x,z are auxiliary algebraic parameters, not native spatial axes. BRC/residual-fidelity application retains rank, p-adic valuation, original numerator-factor provenance, coefficient/polynomial/evaluation ports and signed observer.

Operationally Gateway 0.6.11 reported `research_authority_granted=false`; exact Source continuation read returned `CONTROL_QUOTA` (one bounded attempt). No role-bound write/CLAIM, Source checkpoint, accepted Result, or native benchmark is claimed. Research ordinary-control lane `chatgpt-research-onhour-enterprise-math-20260923` stays separate from maintenance `chatgpt-hourly-enterprise-math-20260921`. Issues #1539/#1558 record recovery support; prior staging/unknown receipt not touched. Original hourly task cadence, enabled state and notifications were not altered.
