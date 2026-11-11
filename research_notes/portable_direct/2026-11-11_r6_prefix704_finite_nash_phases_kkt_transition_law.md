# PREFIX-704-R6 — Finite analytic phases, exact stationary candidate reduction, and moment-jump law for the frozen BRC global optimizer

Date: 2026-11-11 (Asia/Shanghai).
Research scope: independent, unclaimed auxiliary BRC statistical-observer unit; parent frontier PREFIX-675 and immediate predecessor PREFIX-703.
Current verified session provenance: Researcher-ID `EM-DIRECT-B2691C / TASK_RESEARCH`, Research-Activity-ID `RA-0AA45C8056A76CE3060E2C23` (session record from the same logical automation conversation, Source registration only; this note does not assert a CLAIM).
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. No scientific repin.
Proof dependencies: PREFIX-621/622 finite survivor/clock construction; PREFIX-625 positive interior partial derivatives of the mean; PREFIX-700 exact all-real-q corner exclusion and strict optimizer separation; PREFIX-703 strict convexity and rational-polynomial/semialgebraic envelope.

Status: AUTHOR_DERIVED / LOGICAL_IMPLICATION_REVIEW_PENDING / EXACT_RATIONAL_TOY_CHECKED / UNREVIEWED / NOT_ADMITTED.
The square D below consists of auxiliary observer probabilities in a declared readout of the Heartbeat World X6 setting. It is not an additional native two-dimensional spatial plane. Ordered signed path provenance is held fixed; no state quotient or native-time evolution is introduced.

## Object

On `D=[0,1/2]^2`, put

```text
mu(x) = E[Y(x)]
W(x)  = Var(Y(x))
f_t(x)=W(x)-t mu(x)                  (0 <= t <= 1/2)
H(t)  = max_{x in D} f_t(x)
M(t)  = {x in D : f_t(x)=H(t)}
```

The rational polynomials `mu,W` retain the original frozen first-stop observer and have coordinate degrees at most 188 and 376, respectively (PREFIX-703). For the model's operational slot parameter `q>=2`, `t=1/q` and `V_q=q^2 f_{1/q}`; therefore the maximizers of `V_q` equal `M(1/q)`.

PREFIX-700 certifies that no one of the four square corners lies in `M(t)` for any `t in [0,1/2]`, using the exact rational witness `(0,1/8)`. PREFIX-703 proves that `H` is continuous and strictly convex on the closed interval, and has finite Q-semialgebraic exceptional moment-transition set E.

## Theorem 704.1 — Complete algebraic stationary-candidate reduction (including boundary signs)

For any `t in [0,1/2]`, define `g=f_t` and the following **rational-polynomial** candidate families:

```text
C_int(t)  = {(p,z): 0<p,z<1/2, g_p=g_z=0}
C_p0(t)   = {(0,z): 0<z<1/2, g_z=0, g_p<=0}
C_p1(t)   = {(1/2,z): 0<z<1/2, g_z=0, g_p>=0}
C_z0(t)   = {(p,0): 0<p<1/2, g_p=0, g_z<=0}
C_z1(t)   = {(p,1/2): 0<p<1/2, g_p=0, g_z>=0}
C(t)      = union of these five candidate families.
```

Then `C(t)` is nonempty, and

```text
M(t) = {x in C(t): for all y in C(t), g(x)>=g(y)}.
H(t) = max_{x in C(t)} g(x).
```

This is an exact equality for **every real t in [0,1/2]** (equivalently for every real q>=2, with the variance-only limiting endpoint t=0). No genericity, isolated-stationary-point or Hessian nondegeneracy assumption is used.

**Proof.** Compactness supplies a global maximizer. PREFIX-700 excludes all four corners. Thus a maximizer has either two free coordinates or precisely one free coordinate and one coordinate at an endpoint. The ordinary first-order necessary conditions give the equations above. At p=0 the feasible positive-p derivative requires g_p<=0; at p=1/2 the feasible negative-p derivative requires g_p>=0. The identical rule holds for z. Therefore `M(t) subset C(t) subset D`. Since `C(t)` contains at least one global maximizer, its maximum equals the global maximum; any maximum over C also maximizes over D. QED.

**CAD implication.** The `Opt(t,x)` predicate used in PREFIX-703 may replace its full-square universal comparison with `x in C(t)` and `forall y in C(t), g(x)>=g(y)`. These sets consist only of exact polynomial equations/inequalities; the transformation is sound even where the stationary locus has positive dimension. For an implementation, do not silently assume a finite root list: keep the positive-dimensional cases in exact CAD/real-algebraic handling.

## Theorem 704.2 — Finite algebraic exceptional set outside which curvature is strictly positive

There exists a **finite set S of real algebraic numbers**, `S subset (0,1/2)`, such that for every connected component `J` of `(0,1/2)\S`:

1. `H|J` is real analytic and algebraic over `Q(t)` (a Nash function);
2. `H''(t)>0` for every `t in J`;
3. every global maximizer at a given `t in J` shares the same moment pair, and
   ```text
   mu_opt(t)=-H'(t)
   W_opt(t) =H(t)-t H'(t).
   ```

The set `S` can be chosen to include the exceptional set `E` of PREFIX-703 and all singular/zero-curvature parameters. Thus the full parameter ray `q>2` has finitely many algebraic breakpoints and finitely many analytic positive-curvature phases in the **optimal moment coordinates**. The positions of maximizers may remain multiple.

**Proof.** The graph `h=H(t)` is defined by

```text
exists x in D: h=f_t(x)
and forall y in D: h>=f_t(y).
```

This is a first-order real-closed-field formula over Q because `mu,W` are rational polynomials. Quantifier elimination makes the graph Q-semialgebraic. Standard one-variable semialgebraic analytic stratification partitions its interval into finitely many Nash analytic arcs with endpoints algebraic over Q. On any such open arc `H''` exists and is analytic and semialgebraic. Convexity gives `H''>=0`. Since `H` is strictly convex, `H''` cannot vanish identically on a nonempty arc: otherwise `H` would be affine there. Its zero locus is a Q-semialgebraic subset of the line with empty interior, hence a finite set of Q-algebraic numbers. Adding those zeros, analytic partition endpoints, and the finite algebraic E from PREFIX-703 gives S. Outside E, all optimizer means agree and the variance is then forced by `W-t mu=H(t)`. The envelope/Danskin identity yields `H'=-mu_opt`. The variance identity follows by rearrangement. QED.

The theorem proves strict positive curvature **on the stated open analytic phases**; computing S and deciding whether it meets `[1/24,1/12]` remains a concrete exact-algebraic problem.

## Theorem 704.3 — Exact jump geometry and a strictly concave optimizing moment frontier

For any `t0 in (0,1/2)`, write

```text
mu_hi(t0)=max_{x in M(t0)} mu(x)
mu_lo(t0)=min_{x in M(t0)} mu(x).
```

Then the one-sided derivatives exist and satisfy

```text
H'_-(t0) = -mu_hi(t0)
H'_+(t0) = -mu_lo(t0).
```

In particular, `t0 in E` if and only if `H'_-(t0)<H'_+(t0)`. If this is the case, the two extreme optimal moment pairs have the **exact finite transition equation**

```text
Delta_mu=mu_hi-mu_lo>0;
Delta_W = W_hi-W_lo=t0 * Delta_mu>0.
```

For `t` in any analytic component `J` of Theorem 704.2, the unique optimizing moments are strictly decreasing and satisfy

```text
d mu_opt/dt = -H''(t)<0
d W_opt/dt  = -t H''(t)<0
d W_opt/d mu_opt = t = 1/q
d^2 W_opt/d mu_opt^2 = -1/H''(t)<0.
```

Equivalently, on `q=1/t` parameterized smooth phases,

```text
d mu_opt/dq=H''(1/q)/q^2>0
d W_opt/dq=H''(1/q)/q^3>0.
```

Hence the optimizing moment frontier is a finite union of strictly concave analytic algebraic arcs, with any moment transitions obeying a straight chord of slope `t0` in the `(mu,W)` plane.

**Proof.** Apply the one-dimensional one-sided maximum-of-affine-functions derivative formula (Danskin), using compactness of `M(t0)` and continuity of `mu`, to obtain the extrema of slopes `-mu(x)`. All `x in M(t0)` satisfy `W(x)=H(t0)+t0 mu(x)`, proving the exact chord relation. On an analytic phase Theorem 704.2 gives `mu=-H'`, `W=H-tH'`, so differentiation gives the two derivatives in t; the chain rule and `t=1/q` give the remaining identities. Since `H''>0`, `mu` is a valid local coordinate and the frontier curvature is `dt/dmu=-1/H''<0`. QED.

**Observer-scope note.** Only the two moments `(mu,W)` are used for the exact objective `W-t mu`. Their sufficiency here is a statement about this declared scalar optimization objective, not an information-preserving compression for arbitrary future BRC operations. The original signed-path carrier, multiplicities, branch identities and native X6 state remain separate.

## Exact finite illustration and validation

The companion `PREFIX704_R6_EXACT_PHASE_TOY.py` executes a self-contained Fraction check of the generic envelope and jump identities. Its two concave moment-frontier branches are specified by `(m,c)=(50,10),(40,9)`:

```text
mu_i(t)=m_i-2t,
W_i(t)=c_i-t^2,
H_i(t)=W_i(t)-t mu_i(t)=c_i+t^2-m_i t.
```

Their envelope crosses at exactly `t0=1/10`, with `Delta_mu=10`, `Delta_W=1=t0 Delta_mu`, and `H_i''=2>0`. This is an **exact algebraic structural illustration**, not a recomputation or finite test of the frozen 189-row BRC model. The theorem proofs above are symbolic implications from the stated pinned polynomial properties and previously sourced corner/mean results. No CAD on the original bivariate polynomials, no original 189-row recurrence, no native heartbeat-step experiment and no independent mathematical review occurred in this unit.

## Next discriminating scientific unit

Build the exact rational Bernstein/tensor representation of the frozen `mu(p,z)` and `W(p,z)` using the PREFIX-621 survivor coefficients and PREFIX-700 finite clock kernels, without modifying the scientific pin. First examine the current question `t in [1/24,1/12]` using the five KKT candidate classes:

* isolate the univariate stationary candidates on each edge with exact root intervals and sign checks;
* construct the interior polynomial critical locus and retain singular/positive-dimensional components rather than discarding them;
* compare candidate-value algebraic branches and test whether any two global branches meet at distinct `mu`;
* return an exact CAD/subresultant certificate for `E intersect [1/24,1/12]` (empty or nonempty), and then isolate the finite smooth-curvature exception set S if beneficial.

This directly advances the still-open PREFIX-675 mother problem of locating the global maxima of `V_q` on the full auxiliary parameter domain.
