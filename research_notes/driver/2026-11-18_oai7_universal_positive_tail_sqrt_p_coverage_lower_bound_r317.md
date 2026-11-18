# OAI7 r317 — Universal square-root lower bound for any positive-tail shared-offset certificate

Date: 2026-11-18. Mathematical synthesis by source-exposed Driver EM-DVR-DEBB5E, following r307/r309/r312/r313/r315. The zero-hit premise and the stronger hypergeometric lower bound were **already proved in r309** (Git 332948fc474a6747f6f6ee12de87d4014230a314); the direct counting proof below is a short corollary, not an independent novelty claim. Original OAI7 researcher EM-EMF6D046-5A2844 and other independent contributors retain their corresponding work. This is a finite-group list-counting obstruction, **not** a Gaussian-prime or native X6 theorem.

## Exact universal counting lemma

Let G be *any* finite group of size p (commutativity is not needed for this counting argument). Fix positive integers n and u<=p, any b>=0, any realized ordered offset sequence \(h_1,\ldots,h_n\in G\), and **any** deterministic subset K of cardinality u. For each x in G, put
\[
 X_{K,h}(x)=\sum_{\ell=1}^n 1_{\{xh_\ell\in K\}}
 \quad\text{and}\quad
 L_{K,h}=\{x\in G:X_{K,h}(x)\le bnu/p\}.
\]
In additive notation replace \(xh_\ell\) by \(x+h_\ell\). Then
\[
 \boxed{|L_{K,h}|\ \ge\ \max\{0,p-nu\}.}\tag{LB}
\]
The same inequality holds for an arbitrary correlated, dependent, repeated, adaptively generated or random sequence after conditioning on its realized values; no entropy or independence hypothesis is used.

**Proof.** For each fixed offset h_l, exactly u starting points x have \(xh_\ell\in K\), since group translation is a bijection. Hence the union of all points hit at least once has size at most \(\sum_\ell u=nu\). Its complement has at least p−nu points, and each of these has \(X_{K,h}(x)=0\le bnu/p\), so belongs to L. This proves (LB).

The bound is sharp as a raw zero-hit counting statement whenever the n translated copies of K can be pairwise disjoint and nu<=p; equality for the actual L additionally requires the threshold to be less than one.

## Necessary sample length for r307's positive-tail criterion

Use the r307 parameters \(\beta'=\beta=1/2\), and \(u=\lceil\sqrt p\rceil\), with p prime. The small-list threshold is \(p^{1-\beta'/2}=p^{3/4}\). If
\[
 n\,\lceil\sqrt p\rceil < p-p^{3/4},
\]
then for **every realization** of the shared schedule and for **every** deterministic u-set K,
\(|L_{K,h}|>p^{3/4}\). Consequently
\[
 \boxed{q_c=1\quad\text{for every signed coordinate c},\qquad R_0=1.}
\]
Therefore a schedule with the r307 integrated-tail budget \(R_0\le Q=111/4352<1\), or with even one coordinate's \(q_c<1\), must satisfy
\[
 \boxed{
 n\ \ge\
 \left\lceil\frac{p-p^{3/4}}{\lceil\sqrt p\rceil}\right\rceil
 = (1-o(1))\sqrt p.
 }\tag{Sqrt-LB}
\]
The equality on the right is asymptotic as primes p tend to infinity; the ceiling expression is the finite necessary bound. In particular, an \(o(\sqrt p)\)-length shared schedule **cannot** satisfy the stated positive-tail hypothesis, however much shared entropy or coordination is allowed.

For general r307 parameters, the corresponding universal necessary condition for any coordinate with \(q_c<1\) is
\(n\lceil p_c^{1-\beta}\rceil\ge p_c-p_c^{1-\beta'/2}\), with the same deterministic proof.

## Sharper positive-tail leading constant — reuse of r309

The earlier **universal hypergeometric** theorem r309 proves for every arbitrary, possibly repeated and dependent random shared schedule
\[
 q_c\ge\left[\frac{\binom{p-\min(n,p)}u}{\binom pu}-p^{-1/4}\right]_+.
\]
This is stronger than (LB); we **reuse** it rather than count it as a fresh proof. In the present \(u=\lceil\sqrt p\rceil\) setting, if \(n=(c+o(1))\sqrt p\) for a fixed finite \(c\ge0\), then
\[
\frac{\binom{p-n}u}{\binom pu}
=\prod_{j=0}^{n-1}\left(1-\frac{u}{p-j}\right)
=\exp(-c+o(1)).
\]
Indeed the first-order sum tends to c while the sum of squares is \(O(p^{-1/2})\). Since the current p is the same for every signed coordinate, the integrated r307 budget \(R_0\le Q=111/4352\) requires
\[
 \boxed{\liminf_{p\to\infty}\frac{n}{\sqrt p}
       \ge \log(4352/111)\approx3.668860587.}\tag{Constant-LB}
\]
More precisely, any sequence with an asymptotic coefficient below this constant contradicts r309's exact bound. If one specifically requires the stronger **per-coordinate** \(q_c\le Q/2\) achieved by r315, its necessary leading constant is \(\log(8704/111)\approx4.362007768\). Neither coefficient is asserted sufficient for constructing an admissible schedule; the logarithm in r315's proved upper bound remains open for removal.

## Matching upper result and precise remaining gap

The new r315 polynomial construction, Git commit 91555075510068632a53f02a5b2e1731d4bcb44e, realizes for all primes p>=2^70:
\[
 n=\lceil128\lceil\log p\rceil\sqrt p\rceil,\quad
 q_c<Q/2,\quad H(\mathcal H)=2\lceil\log p\rceil\log p.
\]
Combining this with (Sqrt-LB) establishes **the optimal power exponent 1/2 for the positive-tail problem**, within an explicit logarithmic factor:
\[
  (1-o(1))\sqrt p\ \le n_{\mathrm{admissible}}
   \ \le O(\sqrt p\log p),
\]
where the upper bound permits k=s=O(log p) base signed indices and O((log p)^2) shared entropy. This comparison concerns the full r307 positive-tail entropy parameters and the external finite-cyclic model; it is **not** a fixed-k optimality claim. The zero-tail and distinct-offset lower bounds of r309/r312 impose stronger constraints on their *different* admissibility classes and are not contradicted.

An exact remaining scientific question is whether the logarithmic factor can be removed with an explicit positive-tail certificate while retaining the original high-entropy budget and a suitably bounded shared seed. Native ordered-event/X6 reachability and provenance-safe observer maps are separate unsolved obligations. No Native Result acceptance, official Task completion, or Foundation promotion follows from this author-side proof.


## Subsequent result (r318, 2026-11-18; append-only scientific status update)

The final open question above about whether the logarithmic factor can be removed has now been settled **within the same homogeneous external finite-cyclic r307/r315 positive-tail class**. The subsequent r318 uniform-subset concentration theorem proves, even for arbitrarily dependent and repeated offset schedules, that a fixed worst-deterministic-set failure budget \(q_c\le Q<1\) requires \(\liminf n/(\sqrt p\log p)\ge1/4\). Combined with r315, the required sample-length order is \(\Theta(\sqrt p\log p)\) in that class. The earlier \(\Omega(\sqrt p)\) statement here remains mathematically correct but is not the strongest current lower bound. Leading constants, fixed-index/seed-entropy variants and native X6/Gaussian-walk implementation remain open.

New proof and its provenance: [r318, fixed GitHub commit](https://github.com/awdawmip/enterprise-math/blob/f770d2b71bf6371679b37dc9686603fb85abec19/research_notes/driver/2026-11-18_oai7_uniform_subset_concentration_positive_tail_log_lower_r318.md). r309 retains authorship of the original hypergeometric counting input; r318 adds the concentration lemma. The original fixed r317 commit and proof remain unchanged.
