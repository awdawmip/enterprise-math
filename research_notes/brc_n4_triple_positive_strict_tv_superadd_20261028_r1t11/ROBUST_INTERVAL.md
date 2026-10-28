# Exact robust interval around the triple-positive strict-TV-superadditivity witness

**Author-side additional analytic consequence; external N4 two-law BRC tree, UNREVIEWED / NOT_ADMITTED.** Same fixed snapshots and same F_epsilon, strategy classes and 16-coordinate (T,D) observer as PROOF.md.

## Lemma (exact target-law variation)

For every real 0≤ε,ε'≤1/2,

\[
\rho(\mu^{F_\varepsilon},\mu^{F_{\varepsilon'}})=\frac{|\varepsilon-\varepsilon'|}{4}.
\]

Indeed, the only modified action is BU at t=2, where Q(BU)=P(BU)=1/4. Changing ε to ε' transfers absolute mass |ε−ε'|/4 under *each* law between STOP Q at event (2,Q) and its future t=3/4 subtree. The future law is supported entirely on later time events, carries precisely the transferred nonnegative total mass (because BU descendants preserve both P and Q mass), and is independent of ε. Its support cannot cancel the mass change at (2,Q). Thus each of the two TV distances is exactly |ε−ε'|/4.

For any fixed nonempty policy output set C_J, the distance function d_J(ε)=inf_{z∈C_J}ρ(μ^{F_ε},z) is 1-Lipschitz in its argument even if C_J is nonconvex. Therefore

\[
|d_J(\varepsilon)-d_J(9/20)|\le |\varepsilon-9/20|/4, \quad J\in\{2,3,23\}.
\]

Put G=d23−d2−d3 and G*=243712321/1847261790000. It follows for all ε in the valid domain that G(ε)≥G*−3|ε−9/20|/4. For the **explicit closed real interval**

\[
\boxed{\frac{4499}{10000}\le\varepsilon\le\frac{4501}{10000}},
\]

we have |ε−9/20|≤1/10000 and hence

\[
\boxed{G(\varepsilon)\ge\frac{420670747}{7389047160000}>0.}
\]

By the same Lipschitz inequality, d2(ε)≥37/30360−1/40000=36241/30360000>0. By the separately proved complete S3 phase formula and ε≥4499/10000>255/572,

\[
\boxed{d_3(\varepsilon)\ge\frac{5857}{310000000}>0.}
\]

Thus the **same two-law tree and the entire stated continuum of complete-history real behavioral strategies** satisfy all four strict properties, including both single-stage positive losses and genuinely superadditive joint TV. This is a real interval, not a finite numerical grid; the proof uses one exact mass-transfer identity, metric Lipschitzness, and the already proved analytic d3 law. `VERIFY_ROBUST.py` checks all rational constants and the exact relation between the endpoint target laws; universal coverage follows from the symbolic argument.

Do not interpret this external sequential model as a Heartbeat World X6 simulation or as a general TV theorem for all trees. Independent review/Source Result/CLAIM remain pending.
