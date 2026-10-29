# EC49AR — a sharp information-strength plateau in the causal auxiliary BRC observer

Date: 2026-10-30 (Asia/Shanghai). Author mathematical continuation of EC49AQ's exact fixed-parameter theorem in PROOF.md. Status: AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_PARAMETER_CERT_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Statement

Keep the exact 18+18 strictly positive probability BRC observer, the causal history-erasure rule, the same source parametrization \(t(w,u)=\frac12+(2u-1)(1-w)\eta\), and fixed expected costs \(C_1=43/48,\ C_2=13/16\), support coefficient \(k=177/172\). Allow arbitrary real-valued first-stage action probabilities, independent conditional sensor purchase fractions \(r(c,u)\) and terminal acceptance probabilities based only on realized observations.

**Theorem A (complete real interval).** For every real \(0\le\eta\le175/674\),
\[
\boxed{\max_{\rm legal}[\alpha-(177/172)\beta]=77/688.}
\]
The same first-stage rational witness and terminal rule from EC49AQ are globally optimal throughout this interval.

**Theorem B (sharp departure).** For every \(175/674<\eta<1/2\) there exists an explicit lawful rational-first-stage causal strategy, with an information-dependent terminal event rule, such that
\[
\boxed{H=77/688+\frac{674\eta-175}{16512}>77/688.}
\]
Thus \(\eta_*=175/674\) is the *exact largest endpoint of the constant-optimum plateau starting at \(\eta=0\)*. For \(\eta>\eta_*\), the exact global optimum remains to be determined; Theorem B is a lower witness, not a global equality claim.

## Proof A: fixed polytope and convexity in information strength

For each fixed \(\eta\), the previously derived observational bound and resource feasibility imply
\[
H\le F_\eta(x)=\sum_{c<4,u,z}\left[P_\eta(c,u,z)-\frac{177}{172}Q_\eta(c,u,z)\right]_+,
\qquad c(x)\ge13/16.
\]
Since \(\sum_u t(w,u)=1\) for each hidden \(w\), both first-stage action costs and maximal second-stage purchase mass \(c(x)=\frac13\sum_{w,c<4}x[w,c]\) are **independent of \(\eta\)**. Hence the truncated cost polytope \(\mathcal P\) from PROOF.md, with exactly 24 high original plus 144 purchase-cut vertices, is fixed over the entire \(0\le\eta<1/2\).

For each fixed first-stage \(x\), every purchased observation score \(P_\eta(c,u,z)-kQ_\eta(c,u,z)\) is affine in \(\eta\), and its positive part is convex. Thus \(F_\eta(x)\) is convex in \(\eta\). Equivalently, \(M(\eta)=\max_{x\in\mathcal P}F_\eta(x)\) is convex as a pointwise supremum of convex functions.

Exact rational exhaustive evaluation of all 168 vertices at the **two** parameter endpoints gives

| Parameter endpoint | Max \(F_\eta\), 24 high vertices | Max \(F_\eta\), 144 cutoff vertices | Number cutoff ties |
|---|---:|---:|---:|
| \(\eta=0\) | \(243/2752\) | \(77/688\) | 24 |
| \(\eta=175/674\) | \(36/337\) | \(77/688\) | 24 |

Each result is an actual Fraction computation using the same exact 1365+3003 complete support enumeration from EC49AQ; VERIFY_PARAMETER.py recalculates raw purchased P/Q observation masses at both endpoints and verifies every inequality. Consequently \(M(0)=M(175/674)=77/688\), and convexity proves \(M(\eta)\le77/688\) at **every real parameter** between the endpoints.

The EC49AQ witness's decision rule ignores \(u\), so \(\sum_u t(w,u)=1\) ensures its expected costs, \(\alpha=25/64\), \(\beta=13/48\) and \(H=77/688\) remain constant for all \(\eta\in[0,1/2)\). Upper and lower bounds coincide throughout the interval, proving Theorem A.

## Proof B: new positive leaf and sharp counterexample beyond \(\eta_*\)

Keep **exactly** the EC49AQ witness first-stage rows
\[
x[0]=(0,3/16,1/4,0,9/16),\quad x[1]=(1,0,0,0,0),\quad x[2]=(0,1,0,0,0),
\]
buy all paid sensors, and retain the three original accepted observable pairs \((A0,z=1),(A1,z=2),(B0,z=0)\) for either \(u\). Add one more purchased acceptance event
\[
(c,u,z)=(A1,1,0).
\]
This event is observable and disjoint from the original three events. In the retained positive BRC fiber at \((A1,u=1)\),
\[
q_0=\frac1{32}+\frac\eta{16},\qquad
q_2=\frac16-\frac\eta3,\qquad
T=\frac{19}{96}-\frac{13}{48}\eta.
\]
It contributes the exact **signed support difference**
\[
P_\eta(A1,1,0)-\frac{177}{172}Q_\eta(A1,1,0)
=\frac{43q_0-16T}{172}
=\frac{674\eta-175}{16512}.
\]
The added event changes no action probability, observation purchase, source distribution, first-stage resource cost, or second-stage resource cost. Therefore it is legal for every \(\eta<1/2\); for \(\eta>175/674\), it strictly improves the original constant value and proves Theorem B. At the rational test \(\eta=13/50\):
\[
H_{\mathrm{improved}}=\frac{7701}{68800},
\qquad H_{\mathrm{improved}}-\frac{77}{688}=\frac1{68800}.
\]
The threshold is **sharp for the constant plateau**. The optimum's shape beyond it may involve other first-stage strategies and purchase rules.

## Exact validation and epistemic scope

Re-run the bounded source-independent calculation:
```bash
python3 VERIFY.py > EXACT_REPORT.json
python3 VERIFY_EDGE.py > EDGE_REPORT.json
python3 VERIFY_PARAMETER.py > PARAMETER_REPORT.json
```
(The original edge checker can optionally be run with `--certificate EDGE_CERTIFICATES.tsv`; only the two endpoint certificates are needed for the parameter theorem.)

VERIFY_PARAMETER.py imports the complete support sets from VERIFY.py and recomputes P/Q leaf scores at \(\eta=0,175/674\); its rational output was actually executed and captured as PARAMETER_REPORT.json on 2026-10-30. Its witness check also evaluates \(\eta=13/50\) and a second \(\eta=499/1000\) diagnostic point. The convexity argument, not a finite grid, proves the full uncountable parameter interval. AUTHOR-side independently structured pointwise verifiers are not a substitute for an independent mathematical review or formal Lean checker.

This remains an **auxiliary strictly positive probability BRC** theorem. Any native signed/phase BRC, six-axis X6 / native three-dimensional slice, or heartbeat dynamics implication requires an explicit typed observer-and-future-operation preservation map. The ACTIVE P000 and worldview files are not changed.

**Next research (EC49AS):** characterize the actual envelope \(H_{\max}(\eta)\) for \(\eta>175/674\) near the sharp transition. Determine whether the additional single-atom decision rule is globally optimal on a nonzero right neighborhood, or produce another exact admissible policy with strictly larger \(H\). Use the same 168-vertex certificate with a cost-sensitive subbudget optimizer; do not extrapolate the sharp *plateau* endpoint to the full envelope.
