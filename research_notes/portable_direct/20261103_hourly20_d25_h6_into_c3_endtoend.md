# D25 — consume H6 in C3: full p⁵ Clausen reconstruction with no direct high-edge unit

**2026-11-03, TASK_RESEARCH portable test.** Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Research logical lane `chatgpt-research-hourly-enterprise-math-20260923`. `AUTHOR-DERIVED / EXECUTED-EXACT-CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`.

## Executed follow-through on the next unit

H6 was proved in the earlier same-turn note, commit `66bcdfef879f4691f7787ffc2310a889a43cf42e`. It expresses the finite Gauss high-edge unit `U_p=c_(p-1)/p² (mod p³)` using only the two short harmonic lengths r+1 and 2r+1.

Starting from the **existing** C3 checker `d25_clausen_p5_sixmoment_full_20261103.py` at immutable project commit `3b3d5e6449fd46243f7fa5a6845ce44f392b55bd`, the author created a focused variant. All direct original 3F2/2F1 finite polynomial construction, the original weighted Euler observer, the six-prefix low/middle source sums, the ordered high/high triangle, and their p⁵ modular comparison stayed the same. Exactly the line

```python
U=(c[-1]//(p*p))%m
```

was replaced by the following H6 short-harmonic construction (`m=p**3`):

```python
Hshort=Hlong=H2short=H2long=0
for j in range(1,2*r+2):
    inv=pow(j,-1,m)
    Hlong=(Hlong+inv)%m
    H2long=(H2long+inv*inv)%m
    if j<=r+1:
        Hshort=(Hshort+inv)%m
        H2short=(H2short+inv*inv)%m
h=(Hshort+Hlong)%m
U=(1+p*h+p*p*(h*h*pow(2,-1,m)+2*H2short*pow(3,-1,m)+5*H2long*pow(6,-1,m)))*pow(10,-1,m)%m
```

This is a reproducible exact patch; it does not relabel earlier C3 proof/checks as a new mathematical theorem. The author's local executable variant `d25_clausen_p5_h6_harmonic_compose_20261103.py` actually ran through **all 148 primes** p=6r+1 in 7..2000 and returned **PASS 148/148** against the independent original full finite-F/G observer. It verified that replacing U with H6 leaves the entire existing C3 precision-typed source reconstruction intact.

For p=373, the new pipeline returned the same full observer

`E_373^[3]=20942635=177+196*373+150*373² (mod373³)`,

with low/high `9731747`, middle/high `32358496`, high/high `30747509=221*373²` (all mod `373³=51895117`) and edge unit `U_373=36237435 (mod373³)`.

**BRC transport:** the original high-edge coefficient need not be separately evaluated for this scalar at p³ precision. H6 is an exact observer-factorization certificate; the C3 high/high ordered-pair source remains a necessary separately retained port in the already proved representation. No source/precision/valuation or signed-weight provenance was discarded. Reuse resolution: `REUSE_EXECUTED / COMPOSE_APPLIED`.

## Next exact scientific unit

Use the newly executable H6+C3 source interface with the existing H3 Gauss Hensel second-digit equation to search for an exact CM/WZ boundary certificate for `12*j*h_Gauss=1 (mod p)` for target primes p mod24 in {13,19}, or a valid in-hypothesis counterexample. The symbol `h_Gauss=G(1/2)/p` is distinct from the H6 harmonic sum. Separately construct an exact observation map back to frozen `Delta_p-R_p`; the current auxiliary relation is not automatically parent-objective closure.

Gateway status observed this turn: `UPSTREAM_CODE_REVIEW_REQUIRED`, `research_authority_granted=false`, `executor_binding_configured=false`, quota 5/5. No native CLAIM/OPEN/Source checkpoint/Result/review; older #6637/#6638 and staged state untouched. The code was run **locally**, not as the original native p373 H0/B0 experiment (tracked separately in issue #1559).
