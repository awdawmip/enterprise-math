# EC49FTV Supplement — A reentrant stochastic-order phase at atom slope lambda=3

**Author-proved, exact-rational checked, parent-dependent, NOT_REVIEWED.**
This extends the same frozen external effective price-prior problem of EC49FTV; see its main theorem and EC49FTU PR #2801. It changes no native Bellman input, P000, ownership or Researcher Activity.

The full strictly positive baseline price-prior parameter interval is

\[
-960/7<\theta<6720/59.
\]

The main EC49FTV theorem proves that the *entire* conditional family \(Z\mid M=m\) is first-order stochastically increasing in \(m\in(1469/64,187/8)\) precisely when \(0\le\lambda\le\Lambda(\theta)\), where

\[
\Lambda(\theta)=
\frac{3500(862686243742176000-2239375169798320\theta-18989094173841\theta^2)}
{6561(413340200-1327113\theta)^2}.
\]

**New corollary (exact reentrant phase):** Fix \(\lambda=3\). Then full stochastic order holds **if and only if**

\[
\boxed{\theta_-\le\theta\le\theta_+}
\]

where the two exact algebraic critical parameters are

\[
\boxed{\theta_\pm=
\frac{6878186428253835800\pm 14000\sqrt{64172987269060715479052178721}}
{101128098337841727}.}
\]

The lower root lies strictly in \((32,33)\) (approximately 32.9448707939), and the upper root lies strictly in \((103,104)\) (approximately 103.0843147896). Both lie inside the prior's strict positivity interval. Thus *as theta increases with lambda fixed*, the model has the exact phase sequence **failure -> full stochastic order -> failure**, despite a strictly positive and strictly TP2 continuous conditional kernel throughout. This is a model-internal phase reentry statement, not a native physical transition.

**Proof.** The denominator of \(\Lambda(\theta)\) is positive throughout the admissible range. Exact clearing of its denominator makes the condition \(3\le\Lambda(\theta)\) equivalent to

\[
P_3(\theta)=
-101128098337841727\theta^2+
13756372856507671600\theta-
343441077286459320000\ \ge0.
\]

This quadratic has a negative leading coefficient and discriminant

\[
50311622018943600935576908117264000000
=28000^2\cdot64172987269060715479052178721>0.
\]

The quadratic formula produces the displayed two distinct algebraic roots. Exact rational sign checks give

\[
P_3(32)=-6792318576163757248<0,\quad
P_3(33)=390727888384202097>0,
\]

\[
P_3(103)=597331667667973057>0,\quad
P_3(104)=-6579811831757592832<0.
\]

Therefore the two roots both lie inside the admissible theta interval, and the concave quadratic is nonnegative exactly between them. Combine with the main conditional mixed-law equivalence to obtain the iff result, including equality at each critical theta. QED.

This is a genuine further consequence of the full-theta convexity theorem. It cannot be inferred from the formerly restricted \([0,1]\) prior, for which lambda=3 always exceeded the allowable threshold.

**Scope of verification:** Python standard-library \`Fraction\` checked the complete phase polynomial, exact discriminant identity and four rational bracketing signs. Radical sign algebra is elementary and exact. This step does **not** independently verify inherited native q140 Bellman optimality. Next: classify nonaffine continuous kernels that have two or more interior extrema of \(\Lambda\) and quantify the corresponding order intervals.
