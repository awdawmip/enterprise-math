# OWNER X6 stability: independent mathematical audit

Status: `PASS / INDEPENDENT_MATHEMATICAL_AUDIT`.
Scope: noncanonical independent audit; no Foundation admission, immutable
Driver disposition, theorem-novelty claim, or publication authority is created.

The dispatched claim was first audited independently, then compared formula
by formula against `research_notes/OWNER_X6_STABILITY_20260907.md`, SHA256
`2915e70210dce5bc136c915e45e96a7c8a1f6dd414fae1590a4687f41bff3127`.
The first reviewed hash was
`587e31726bf4047bab8b6aaab679ac26335685b7ed716e9c55a0856d3c12abad`;
the author then replaced the header/footer's unallocated identity metadata
with the auxiliary-work-package scope at the owner's request.
The proof below does not rely on the author's private derivation or tests.
No substantive mathematical defect was found in that frozen text. This
audit does not independently attest the author's separate CWM execution log.

## Claim and independent proof

Let `f` be a finitely supported rational array on a product of `n` coordinate
sets, and let `p(f)` count **distinct positive spatial cells**, not branch
labels or positive terms in an uncollected expression. Let `M_I f` sum over
the complementary coordinates while retaining the exact raw coordinates in
`I`. Put

`D(n,k;f) = sum_{|I|=k} ||M_I f||_1`.

For `0 <= k <= n`, the claim is

`p(f) < 2^k  =>  ||f||_1 <= C(n,k) D(n,k;f)`,

with `C(n,0)=C(n,n)=1` and the stated interior recurrence. The empty marginal
is the scalar total signed mass, and the full marginal is `f` itself.

The endpoints are valid: `k=0` forces `f<=0`, so total mass has no sign
cancellation; `k=n` is the identity. The zero array needs no slicing choice.

For `0<k<n`, fix an axis `j` and write its finite nonzero layers as `f_t`.
Their positive-cell counts add to `p(f)<2^k`, so at most one layer has
`p(f_t)>=2^(k-1)`. Choose that layer as `t0`; if none does, choose any layer.
Thus every `t != t0` satisfies the induction hypothesis at `(n-1,k-1)`.

Let `g=sum_t f_t`. Every positive cell of `g` has a positive summand in some
layer. Hence `p(g)<=p(f)<2^k`, even though projection may merge cells and
cancel signs. The induction hypothesis at `(n-1,k)` is therefore legitimate.
The exceptional layer is controlled without any smaller-support assumption:

`||f||_1 <= ||g||_1 + 2 sum_{t != t0} ||f_t||_1`.

For a fixed `(k-1)`-set `J` excluding `j`, the arrays `M_J f_t` are precisely
the disjoint `j`-layers of `M_(J union {j}) f`. Their norms add, rather than
cancel. Applying induction and enlarging the layer sum gives

`||f||_1 <= C(n-1,k) sum_{|I|=k, j notin I} ||M_I f||_1`

`             + 2 C(n-1,k-1) sum_{|I|=k, j in I} ||M_I f||_1`.

Sum over all `n` axes. Each fixed `k`-set is absent from `n-k` of them and
present in `k` of them. Division by `n` yields exactly

`C(n,k) = ((n-k)C(n-1,k) + 2k C(n-1,k-1))/n`.

This is a finite induction proof. No LP output, finite enumeration, Gaussian
approximation, presumed sparsity of negative cells, or algebraic independence
assumption enters it. No counterexample to the stated theorem was found;
the argument above proves the stated finite rational claim.

## Constant, noise, and semantic boundaries

Independent Fraction computation gives `C(6,3)=111/20`. As an algebraic
cross-check, multiplying the recurrence by `binom(n,k)` yields Pascal's
weighted recurrence and the closed expression

`C(n,k) = sum_{j=0}^k (-1)^(k-j) 2^j binom(n,j) / binom(n,k)`.

This is a sufficient constant. Optimality of `111/20` is **not** established.

For finite nonnegative measures `mu,nu`, if `mu` has at most seven distinct
spatial support cells, then the positive cells of `f=mu-nu` are contained in
`supp(mu)`. No sparsity assumption on `nu` is required. The same conclusion
holds if only `nu` is sparse, by reversing the sign. If both candidates fit a
common family `y` of 20 labeled raw tables with

`sum_{|I|=3} ||M_I mu-y_I||_1 <= epsilon` and
`sum_{|I|=3} ||M_I nu-y_I||_1 <= epsilon`,

the triangle inequality gives `||mu-nu||_1 <= 111 epsilon/10`. Here epsilon
is the **sum across all 20 tables**, not a per-table bound. If every table
separately has error at most epsilon, the resulting bound is `222 epsilon`.
No assumption that noisy `y` itself has a nonnegative joint realization is
needed for this inequality. This audit does not supply a noisy LP algorithm.

The strict support threshold matters. Four-axis parity inside raw X6 has
eight positive and eight negative unit cells, every three-axis marginal
zero, and `||f||_1=16`. Replacing `<8` with `<=8` would be false.

The raw observation condition also matters. For
`f=delta_(0,0,0,0,0,0)-delta_(1,1,1,1,1,1)`, every triple's local min-zero
(`can3`) image is identical, although `||f||_1=2` and there is only one
positive spatial cell. Thus can3 data admit no such finite stability
constant. The theorem does not recover branch labels, weight histograms,
ports, path histories, or provenance from their aggregated raw mass tables.

Finite rational arrays and nonnegative candidate measures are the audited
scope. The proof must not be cited as an infinite-support theorem or as a
signed-candidate recovery guarantee under a support count that no longer
controls `p(mu-nu)`.

## Additional frozen-author claims checked

- **Approximate sparsity, equation (8): PASS.** The top-seven truncation
  `mu_7` retains original masses and is not renormalized. For the nonnegative
  tail `r=mu-mu_7`, each raw table preserves its total mass `tau`, hence
  `D(r)=20 tau`. Therefore
  `||mu-nu||_1 <= tau+C D(mu_7-nu) <= C D(mu-nu)+(1+20C)tau`,
  and `1+20*(111/20)=112` exactly.
- **Fixed at most 15 spatial cells, signed weights: PASS.** The two disjoint
  sign supports have total size at most 15; at least one has size at most 7.
  Apply the theorem to `f` or `-f`. This does not relax the nonnegative
  unknown-support competitor condition by itself.
- **Finite-domain nonnegative residual minimization: PASS.** Since
  `||Mv||_stack=20||v||_1` for `v>=0`, the stated lower bound gives bounded
  closed sublevel sets in a finite-dimensional space. An optimum exists;
  rational LP data admit a rational optimal solution. This is not evidence
  that the current executable recovery adapter implements noisy optimization.
- **Bounds `3/4 <= C_* <= 111/20`: PASS in the stated arbitrary-mass scope.**
  The punctured four-axis parity distribution has norm 15 and stacked defect
  20 in X6. Its two sides have different total masses, as the author discloses;
  it is not asserted to settle the normalized-probability optimum.
- **Bounded spatial observations: PASS.** The norm-duality estimate
  `|sum F(x)f(x)| <= ||F||_infinity ||f||_1` is immediate on the common
  coordinate set. Cell-aggregated total mass `W` and maximum cell mass `M`
  are each 1-Lipschitz in that norm. Support count `C` and `E=W/M` do not
  inherit uniform absolute-error continuity through the zero-mass boundary;
  the author's examples establish this without recovering erased paths.
- **Unbounded four-axis product: PASS.** In the author's probability example,
  every triple contains at least one of the four active coordinates, so all
  20 individual table distances are `2t`. The joint moment difference is
  `t R^4`. Taking integer `R>=2` and `t=R^-4` keeps the stipulated `0<t<1`,
  gives stacked error tending to zero, and keeps the moment error equal to 1.
  Thus an unbounded-observer conclusion would be invalid.

## Reproducible independent checks

Command: `python experiments/owner_joint_observer_20260907/audit_stability.py`.

Observed result: `PASS`; all arithmetic uses `Fraction`. It checked 12,960
array/order instances from the complete ternary-valued binary `n=3` cube,
160 rational `n=6,k=3` instances, the two boundary counterexamples above,
and the recurrence/closed expression through `n=12`. A punctured parity
array also realizes equality `15=(15/4)*4` for `n=4,k=3`; this does not prove
optimality at `n=6,k=3`. These checks are regressions; the induction is the
general mathematical evidence.
