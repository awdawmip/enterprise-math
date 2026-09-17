# E001 Contact-Network Future-Safe Cycle Quotient — Research Return

- Task: `RS-E001-CONTACT-NETWORK`
- Researcher-ID: `EM-E001-0FB652`
- Claim: `chatgpt-e001cn-20260830-2027-c42f19`
- Execution branch: `research/e001-contact-network-witness-safety-em-e001-0fb652`
- Execution base: `cdfb6abd2c9ab15e6295a0c07125443c1d619f59`
- Direct predecessor surface: PR #234, owner head `a31dc25c90d36b64110d93e5ccf7349c9ca40673`
- Verdict: **PASS**
- Hard target: **ACHIEVED — exact quotient criterion plus minimal persistent-contact counterexample**

## 1. Scope and inherited algebra

PR #234 already establishes the owner-local incidence algebra.  With signed body/contact incidence matrix

\[
B\in \mathbb Z^{N\times E},\qquad D>0\text{ diagonal},\qquad K=B^TDB,
\]

the delivered contact allocation `j` changes body momentum by `Bj` and relative contact score by `Kj`.  Because `D` is positive,

\[
\ker K=\ker B.
\]

For a simple contact graph with `N` bodies, `E` contacts and `c` connected components, the invisible allocation space has dimension

\[
\beta=E-N+c.
\]

The unresolved owner-local question was not whether cycles create invisible allocation directions; that was already proved.  The question was exactly when those directions may be *identified without changing any allowed future behaviour*.

No novelty claim is made for the universal property of quotients, incidence rank, row-space duality, or the factorization lemma below.  The research contribution here is the exact E001 specialization and the minimal persistent-contact boundary.

## 2. Exact future-language criterion

Fix one pre-contact state.  Let the delivered allocation space be `J=Z^E`.  Define body-effect equivalence

\[
j\sim_B j'\quad\Longleftrightarrow\quad Bj=Bj'
\quad\Longleftrightarrow\quad j-j'\in\ker_{\mathbb Z} B.
\]

Let `F` be the declared future language.  A future experiment/continuation `f in F` includes all later legal transitions, all persistent state that can influence them, and its declared observable outcome.  Write its semantics, as a function of the current delivered allocation with the same pre-state fixed, as

\[
\Phi_f:J\to Y_f.
\]

### Theorem — future-safe cycle quotient

Identifying all cycle-related allocations by `~_B` is safe for the future language `F` **if and only if** every future semantics is constant on `ker B` cosets:

\[
\forall f\in F,\;\forall j\in J,\;\forall x\in\ker_{\mathbb Z}B,
\qquad
\Phi_f(j+x)=\Phi_f(j).
\]

Equivalently, for every `f in F` there exists a well-defined map

\[
\overline\Phi_f:\operatorname{im}_{\mathbb Z}B\to Y_f
\]

such that

\[
\Phi_f=\overline\Phi_f\circ B.
\]

This is the weakest possible future-language condition: it is necessary and sufficient, not merely sufficient.

### Proof

If `Phi_f = overline(Phi_f) o B`, then `x in ker B` gives `B(j+x)=Bj`, hence `Phi_f(j+x)=Phi_f(j)`.

Conversely, suppose `Phi_f` is constant on every `ker B` coset.  For `y in im B`, choose any `j` with `Bj=y` and define `overline(Phi_f)(y)=Phi_f(j)`.  If `Bj=Bj'`, then `j-j' in ker B`, so the assumed invariance gives `Phi_f(j)=Phi_f(j')`; therefore `overline(Phi_f)` is well defined and `Phi_f=overline(Phi_f) o B`.  This argument applies independently to every allowed future continuation.  QED.

## 3. Operational reading

The theorem gives an exact boundary between safe and unsafe witness collapse.

A **body-Markov** future language is safe: if every later transition and observation depends on the delivered contact event only through the body after-state (hence through `Bj`), then cycle allocations are semantically indistinguishable.

Persistent contact-local state is also safe *when it itself factors through `Bj`*.  The mere existence of contact-local storage does not force unsafety.

But if any allowed continuation can distinguish two allocations in the same `B`-fiber — directly by reading a contact reservoir/history field, or indirectly because such a field changes a later transition — the quotient is unsafe.  Choosing a minimum-norm or minimum-total representative cannot repair this: that is a representative-selection policy, not a proof that the discarded witness coordinates are future-invariant.

## 4. Exact linear persistent-state corollary

Suppose the future-relevant persistent contact state has a linear delivered-impulse update

\[
w' = w + Cj,\qquad C\in\mathbb Z^{m\times E}.
\]

Then cycle quotienting is safe for this persistent state exactly when

\[
\ker_{\mathbb Z} B\subseteq\ker_{\mathbb Z} C.
\]

Equivalently,

\[
\operatorname{row}_{\mathbb Q}(C)\subseteq\operatorname{row}_{\mathbb Q}(B),
\]

or, in exact rank form,

\[
\operatorname{rank}_{\mathbb Q}\begin{bmatrix}B\\C\end{bmatrix}
=
\operatorname{rank}_{\mathbb Q}(B).
\]

Equivalently there exists a rational matrix `A` with `C=AB`; restricted to `im_Z B`, this defines the required integer-valued factor map because `Cj` is integral for integral `j`.

### Proof

Safety is exactly `C(j+x)=Cj` for every integer `x in ker B`, i.e. `ker_Z B subset ker_Z C`.  Multiplying rational kernel vectors by common denominators shows this is equivalent to the corresponding rational kernel containment.  Over `Q`, kernel containment is dual to row-space containment, which is equivalent to unchanged row rank after stacking `C` below `B`, and to the existence of `A` with `C=AB`.  QED.

This gives a directly checkable owner-local rule: **a linear contact memory may be quotiented with the body state exactly when it carries no row-space component transverse to the incidence row space.**

## 5. Minimal persistent-contact counterexample

For simple undirected contact graphs, the smallest graph with nonzero cycle rank is the triangle.  Orient contacts `1->2`, `2->3`, `3->1` and take equal mass scale `D=I`:

\[
B=
\begin{bmatrix}
-1&0&1\\
1&-1&0\\
0&1&-1
\end{bmatrix},
\qquad
x=(1,1,1)^T.
\]

Then

\[
Bx=0,
\qquad
Kx=B^TBx=0.
\]

Thus allocations

\[
j=0,
\qquad
j'=x
\]

produce exactly the same body momentum increment and exactly the same relative-score increment.

Now let each contact keep its delivered reservoir,

\[
w'=w+j,
\]

so `C=I_3`.  Starting from the same `w=0`, the two executions yield

\[
w'_j=(0,0,0),
\qquad
w'_{j'}=(1,1,1).
\]

A future observable as weak as “read the first contact reservoir”, or a later transition whose legality/response depends on that reservoir, distinguishes them.  Hence the body quotient is not future-safe.

This counterexample is minimal in the current **simple-graph** contact model: with fewer than three vertices a simple graph has no cycle, so `beta=0`, `ker B=0`, and there are no distinct cycle-related allocations to identify.  (If parallel-contact multigraphs were admitted, a two-body two-edge cycle-space example would be smaller, but that is outside the current PR #234 simple-contact model.)

## 6. Exact checker

`research_checks/E001_CONTACT_NETWORK_FUTURE_SAFE_CYCLE_QUOTIENT_CHECK_20260830.py` uses exact integer/rational arithmetic and verifies:

1. the triangle cycle vector has `Bx=0` and `Kx=0`;
2. `rank_Q(B)=2`;
3. the safe linear memory `C=B` leaves stacked rank at `2`;
4. the unsafe persistent allocation memory `C=I_3` raises stacked rank to `3` and exposes `x`;
5. for all 27 one-row matrices `C=(c1,c2,c3)` with coefficients in `{-1,0,1}`, the kernel test `C x=0` agrees exactly with the stacked-rank criterion.

Frozen report: `research_artifacts/E001_CONTACT_NETWORK_FUTURE_SAFE_CYCLE_QUOTIENT/check_report.json`.

## 7. Disposition

**Task residue: NONE at the stated frontier.**

The requested alternative was “exact quotient criterion or minimal persistent-contact counterexample.”  This return supplies both:

- a necessary-and-sufficient semantic quotient criterion for the declared future language;
- an exact linear specialization `ker B subset ker C` / row-space containment / stacked-rank equality;
- the minimal simple-cycle persistent-contact counterexample.

### Owner/canonicalization boundary

The general factor-through-a-quotient statement belongs to generic future-quotient mathematics (A2/P023 territory) and should not be re-owned by E001.  The E001 owner-local result is the contact-network specialization: cycle impulse allocations can be erased exactly when every future-relevant contact memory/continuation is invariant on `ker B` fibers.

Recommended Driver action: accept this as closure of the legacy `RS-E001-CONTACT-NETWORK` witness-safety frontier, then decide separately whether the E001 linear rank test deserves a small owner API or whether only the theorem-level return should be retained.  Do not promote a representative-selection rule as a substitute for the factorization condition.
