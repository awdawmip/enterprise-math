# PREFIX-671-FW-R6 — A slot-uniform fixed-witness exclusion for the BRC variance strip

Date: 2026-11-10 (Asia/Shanghai). Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Status: `AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED`.

## Motivation and typed problem

The mother objective is the global maximum of the variance of the frozen 189-layer two-information-direction first-stop **statistical observer** on `[0,1]^2`. The two observer probabilities are not primitive X6 spatial coordinates. PREFIX-670 proved quantitative stability relative to a q-dependent, exactly defined boundary maximizer `(0,z_*(q))` on a narrow but two-dimensional region. A global interval solver also needs a **fixed rational benchmark**, independent of the sampling-slot parameter q, to discard boxes without recomputing a moving optimizer. This note converts the earlier certificates into such a benchmark.

Set `Q=19/128`, `I=[607/4096,609/4096]`, `R=[0,1/64] x I`. Let `mu(p,z)=E[Y(p,z)]`, `W(p,z)=Var(Y(p,z))`, and `V_q(p,z)=q^2 W(p,z)-q mu(p,z)`. We treat all real `12<=q<=24`, with integer q the actual sampling schemes.

## New theorem (fixed-witness full-slot strip pruning)

For every real `q in [12,24]`, every `z in I`, and every `p in [1/61317,1/64]`, the exact fixed rational competitor `(0,Q)` beats `(p,z)` by the **uniform strict rational margin**

```
V_q(0,Q) - V_q(p,z) > 38634449 / 2105217000000 > 0.
```

Thus the single q-independent rational point `(0,19/128)` strictly eliminates the entire closed substrip `[1/61317,1/64] x I` from the full-domain maximizer search for **every** slot parameter in `[12,24]`. This substrip is the exact area fraction

```
1-(1/61317)/(1/64) = 61253/61317 > 0.9989
```

of the prior certified rectangle `R`. The remaining strip `p<1/61317` is preserved for the stronger moving-optimizer analysis.

### Proof 1: a uniform bound for the moving edge optimum's advantage

Let `g_q(z)=V_q(0,z)` and `M(q)=max_{z in I}g_q(z)=g_q(z_*(q))`. Exact predecessor certificates give:

* PREFIX-659: `-451<g'_12(Q)<-449` and `11344<g'_24(Q)<11347`.
* PREFIX-660: for every `z in I`, `g''_12(z)<-12800000`, `g''_24(z)<-51500000`, and each q has a unique interior edge maximizer. These curvature and center-gradient bounds derive from the same frozen 189-layer observer.

For `q=12+12t`, `0<=t<=1`, the Gamma-clock identity `g'_q/q=q W_z(0,Q)-mu_z(0,Q)` is affine in q. It follows exactly that

```
|g'_q(Q)| <= q A(t),
A(t)=(1-t)*(451/12)+t*(11347/24).
```

The same affine identity `g''_q(z)/q=q W_zz(0,z)-mu_zz(0,z)` and the strict predecessor curvature signs imply, on the whole interval I,

```
-g''_q(z) > q B(t),
B(t)=(1-t)*(12800000/12)+t*(51500000/24)>0.
```

For any function `g` on an interval containing `Q` with `g''<-m<0`, integrating the second-derivative inequality yields

```
g(z)-g(Q) < g'(Q)*(z-Q)-(m/2)*(z-Q)^2
          <= g'(Q)^2/(2m)
```

for `z != Q`, with equality 0 at `z=Q` if the derivative vanishes. Applying the non-strict version of this standard quadratic majorization to the optimum gives

```
0 <= M(q)-g_q(Q) < [q*A(t)]^2/[2*q*B(t)]
                    = (q/2)*A(t)^2/B(t).
```

Set `a0=451/12`, `a1=11347/24`, `b0=12800000/12`, `b1=51500000/24`. Weighted Cauchy gives the exact algebraic identity

```
(1-t)*a0^2/b0+t*a1^2/b1 - A(t)^2/B(t)
 = t*(1-t)*(a0*b1-a1*b0)^2 / (b0*b1*B(t)) >= 0.
```

Since `q<=24` and

```
a0^2/b0 = 203401/153600000
        < 128754409/1236000000 = a1^2/b1,
```

we obtain the **uniform, closed-form fixed-witness gap**

```
0 <= M(q)-V_q(0,Q)
   < (24/2)*a1^2/b1
   = 128754409/103000000 =: D.
```

This calculation is for all real q in the interval: the seven rational samples in the executable checker validate arithmetic only; the universal inference is the displayed identities and inequalities.

### Proof 2: eliminate boxes by the proven normal coercivity

PREFIX-670 proves throughout `R` that

```
M(q)-V_q(p,z) >= L(q)*p+C(q)*p^2
                     +6400000*(z-z_*(q))^2,
L(q)=q*(76650/12+76595*(q-12)/144) >= 76650,
C(q)=(15000*q^2+221*q)/2 > 0.
```

Combining this with the fixed-witness bound above, for every `(p,z) in R` and real `q in [12,24]`:

```
V_q(0,Q)-V_q(p,z) > 76650*p-D.
```

At the new cutoff:

```
76650/61317 - 128754409/103000000
  = 38634449/2105217000000 > 0.
```

For larger p the margin increases. This completes the proof. The linear-budget threshold is integer-denominator sharp: `76650/61318<D`, so the same coarse estimate alone does not certify `p=1/61318`.

## Verification, reuse, and scope

`PREFIX671_R6_UNIFORM_FIXED_WITNESS_CERTIFICATE.py` checks 31 exact Python `Fraction` comparisons/identities. `PREFIX671_R6_FIXED_WITNESS_RESULTS.json` captures the exact gap, cutoff, area fraction and assumption scope. The run is an **implication certificate** of the existing PREFIX-659, 660, and 670 author-proven bounds; it does not rerun original 189-layer path generation. None of the statements above promotes a native 6D physical model or a full-square extremum claim.

Reusable interval-solver rule: for any box `B` within `[1/61317,1/64] x I` and any real `12<=q<=24`, mark it `FIXED_Q_UNIFORMLY_EXCLUDED` using the single exact point `(0,19/128)`. The comparison has a strict rational safety margin and therefore requires neither evaluation of `z_*(q)` nor interval recalculation at each q. It uses BRC frozen survivor-multiplicity observer results (`COMPOSE_APPLIED`).

Sources: PREFIX-659 (`65536b12a268b619e0e1e89f685de3fb2162bea3`), PREFIX-660 (`2026-11-10_prefix660_r6_moving_edge_maximum.md`), PREFIX-670 (`24c22a1496db5cb5da05ffef104b55b8d52f520e`). All use the same immutable scientific pin above.

Publication note: a parallel independent research note also used the numeric prefix PREFIX-671 for a different nonconcavity witness; this artifact is disambiguated as **PREFIX-671-FW-R6** and its machine results use the distinct `PREFIX671_R6_FIXED_WITNESS_RESULTS.json` path. The two results have separate statements and evidence; no existing file was overwritten.

## Next discriminating scientific action

Use a finer q-dependent gradient/curvature ratio instead of the q<=24 worst-case bound to shrink the p<1/61317 unresolved strip. In parallel, apply actual signed Bernstein box bounds on the remaining symmetry-reduced triangle `0<=p<=z<=1/2` and compare to certified fixed/optimized edge competitors. The full-domain global maximum remains the mother objective.
