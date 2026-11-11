# PREFIX-700-R6 — Strict global-optimizer moment ordering for every real slot q >= 2

Date: 2026-11-11 (Asia/Shanghai).
Research role: TASK_RESEARCH / independent auxiliary BRC observer unit.
Native Researcher-ID: EM-DIRECT-6653A5.
Research-Activity-ID: RA-8E29AD2111E41EF38CEF51CA.
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Precursors: PREFIX-621 exact first-stop signed survivor recurrence; PREFIX-622 Poissonized clock identity; PREFIX-625 theorems A and B. New exact witness was recomputed independently from the 189-row recurrence.
Evidence: AUTHOR_DERIVED / EXACT_FRACTION_RECOMPUTED / UNREVIEWED / NOT_ADMITTED.

## Exact model and question

For two separately labelled signed informative streams, each direction receives positive and negative actions with probabilities `p_i/q` and `(1-p_i)/q`. The neutral-action probability is `1-2/q`; hence the statistical model is valid for every real `q>=2`. Each informative sign stream stops at the frozen PREFIX-621 first-passage confidence-width threshold (beta=1/40, width=1/4). First stop is possible at 25 informative signs, and every stream stops by count 189.

Let `Y(p,z)` be the maximum of two independent unit-rate Poisson-clock waiting times for completion. Put

```text
mu(p,z) = E[Y(p,z)]
W(p,z) = Var(Y(p,z))
V_q(p,z) = q^2 W(p,z) - q mu(p,z) = Var(T_q(p,z)).
```

We use the sign-symmetric compact square `D=[0,1/2]^2`; `p,z` are parameters of an auxiliary observation within the native X6 setting, **not** native spatial axes or a physical two-plane. The existing P000 and BRC substrate are unchanged.

PREFIX-625 proved that `mu` is strictly increasing in either coordinate on `[0,1/2]`, with strictly positive interior coordinate derivative; and for any real `2<=q1<q2`, global maximizers `x in Argmax_D V_q1`, `y in Argmax_D V_q2` satisfy

```text
d=mu(y)-mu(x)>=0,
d/q2 <= W(y)-W(x) <= d/q1.
```

Its strictness conclusion previously singled out the pair `(q1,q2)=(12,24)`, because it had a corner-exclusion certificate for q=12. The new computation extends this exclusion to **all real q>=2**.

## Theorem 700.1 — One exact rational witness excludes every corner for all q>=2

Define `e=(0,1/8)`. For each of the three corners

```text
c00=(0,0), c01=(0,1/2), c11=(1/2,1/2),
```

the same witness strictly dominates at **every** real `q>=2`:

```text
V_q(e)>V_q(c00),  V_q(e)>V_q(c01),  V_q(e)>V_q(c11).
```

In particular, none of the four original square corners (including the symmetric `(1/2,0)`) can maximize `V_q` for any `q>=2`.

**Exact rational certificate.** Let `delta_mu=mu(e)-mu(c)`, `delta_W=W(e)-W(c)` and `m_2=2 delta_W-delta_mu`. The accompanying executable replays the exact 189-row integer first-stop survivor recurrence (9,529 nonzero surviving cells), evaluates each pair of clock moments by the binomial/negative-binomial kernels using Python `Fraction`, and checks the following *strict rational* enclosures. Table entries `[a,b)` represent the interval `[a/10^6,b/10^6)`.

| Corner | delta_mu | delta_W | m_2 |
|---|---|---|---|
| c00 | [48811611,48811612) | [557257209,557257210) | [1065702807,1065702808) |
| c01 | [-111509701,-111509700) | [386820427,386820428) | [885150554,885150555) |
| c11 | [-119288768,-119288767) | [439711044,439711045) | [998710855,998710856) |

Additional exact comparisons prove `delta_W>0` at each corner, `delta_mu(c00)>0`, `10 delta_mu(c00)<delta_W(c00)`, and `delta_mu(c01),delta_mu(c11)<0`.

For any `q>0`,

```text
V_q(e)-V_q(c)=q [q delta_W-delta_mu].
```

For every `q>=2` the bracket is at least `m_2>0`, since `delta_W>0`. Indeed the purely algebraic comparison already holds for `q>=1/10`; the operational thinning model retains its actual domain `q>=2`. This establishes the theorem.

## Theorem 700.2 — Global strict comparative statics for every pair q1<q2

For all real numbers `2<=q1<q2`, every choice

```text
x in Argmax_{D} V_q1,  y in Argmax_{D} V_q2
```

satisfies

```text
mu(y)>mu(x),  W(y)>W(x),
(mu(y)-mu(x))/q2 <= W(y)-W(x)
                  <= (mu(y)-mu(x))/q1.
```

Consequently `Argmax_D V_q1` and `Argmax_D V_q2` are disjoint for every distinct pair of parameters `q1,q2>=2`. The conclusion holds even if the maximizer set at some fixed q is non-singleton.

**Proof.** Compactness of `D` and continuity yield nonempty Argmax sets. Optimality at `q1` and `q2`, after dividing `V_q` by `q^2>0`, gives the displayed sandwich as in PREFIX-625. If `d=mu(y)-mu(x)<0`, the inequalities contradict `1/q2<1/q1`; hence `d>=0` and `W(y)-W(x)>=0`.

Assume `d=0`. The sandwich then forces `W(y)=W(x)`, so **each of x and y is a maximizer at both q values**. Take any such common maximizer `u`. At any coordinate `0<u_i<1/2`, interior first-order stationarity for both q values gives

```text
q1 W_i(u)-mu_i(u)=0,
q2 W_i(u)-mu_i(u)=0.
```

Subtracting yields `W_i(u)=0`, then `mu_i(u)=0`, contradicting the strict interior-coordinate mean derivative from PREFIX-625 Theorem A. Thus every coordinate of a common maximizer belongs to `{0,1/2}`, i.e. `u` is a corner. Theorem 700.1 excludes all corners for both q values. Hence `d>0` and the original sandwich gives `W(y)-W(x)>=d/q2>0`. Disjointness follows immediately. QED.

## Numerical meaning, verification and provenance

The companion program `PREFIX700_R6_STRICT_OPTIMIZER_ORDER.py` reconstructs the inherited discrete first-passage predicate with denominator `2^18`, checks extinction at step 189, 9,529 survivor cells and row symmetry, computes exact one- and two-clock moments with finite rational sums and certifies the signed corner gaps. The local equivalent self-contained exact checker returned `ALL_CHECKS_PASS PREFIX700-R6` with all 3 corner cases. Its arithmetic is integer/`Fraction`; the short displayed intervals are certified rational floor intervals and not floating tests. The displayed proof is a deduction from the newly certified corner signs and the explicitly cited PREFIX-625 derivative/optimizer lemmas.

This is a statement about the frozen auxiliary Poissonized two-stream statistical observer, preserving its ordered signed-path provenance. It does not solve the full two-coordinate argmax location question, perform a native heartbeat time update, or claim independent mathematical review.

## Next scientific unit

Apply the new **all-real-q** disjointness/order property to sharpen the global optimizer localization problem. In particular, identify exact bivariate Bernstein exclusion cells on `D` valid simultaneously for the continuum `12<=q<=24`: after dividing the comparison by q, all witness-versus-candidate inequalities are affine in q, so one common fixed rational witness with strict endpoint margins provides the entire interval of q. Begin with the `p>=1/64` region and the already certified edge competitor near `z=0.1483`. Preserve shared owner authority separately from independent mathematical publication.

Artifacts: `PREFIX700_R6_STRICT_OPTIMIZER_ORDER.py` (exact executable) and `PREFIX700_R6_RESULTS.json` (compact strict rational intervals).
