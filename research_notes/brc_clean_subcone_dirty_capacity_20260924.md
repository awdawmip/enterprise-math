# BRC clean-subcone closure and absorbing dirty-capacity ledger

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / AUXILIARY_ONLY / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`.

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This note consumes the proved class-13 cancellation-debt transfer theorem, the exact p-neutral/class-19-neutral suppressor construction, and the class-19 debt-poset absorption theorem. Its purpose is to perform the next nonredundant quotient: remove the already-proved nonrepairable dirty negative channels without erasing their residual effect. The dirty rows survive as explicit nonnegative capacity constraints, while the remaining 19-clean class-13 rows form a finite signed repair cone with an exact causal closure algorithm.

No D24 owner, Result, review, Working Truth, Foundation status, or LIFT/JT2 status is changed.

## 1. Exact branch defect and clean/dirty partition

For a target prime `r == 13 or 19 (mod24)` and a finite exponent cloud `m=(m_j)`, retain

`Delta_r(m) = sum_j m_j [E_r(j)+v_r(j)-C_r(j)(v_r(j)+c_r)] + sum_j v_r(m_j!)`,

where

- `E_r(j)=1` iff `h_r=(r-1)/2` divides `j`;
- for class 19, `C_r=0`;
- for class 13, `ord_r(4)=2s_r`, `C_r(j)=1` exactly when `j=s_r u` with `u` odd, and `c_r=v_r(1+4^{s_r})>=1`.

Fix a target horizon p. For higher class-13 rows `13<q<p`, call q **19-clean** when

`d_r(s_q)=1_{h_r|s_q}+v_r(s_q)=0`

for every earlier class-19 target r; otherwise call q **19-dirty**. Write the two sets as `C` and `D`.

The preceding absorption theorem proves that under exact class-19 neutrality a dirty row has no admissible negative incoming channel. Therefore dirty rows may be removed from the active signed-elimination subsystem only if their nonnegative residual budgets remain explicit.

## 2. Canonical fresh-port clean atoms

Let q be 19-clean. Choose an auxiliary prime `ell>p`, distinct from every other auxiliary prime used in the cloud, and put

`j_q=s_q ell`.

The exact q-specific construction gives a q-suppressor at `e_{j_q}`. If `j_q` lies also on the p-cancellation progression, add the already-proved p-compensation port. When repeated copies are required, use fresh auxiliary primes for each copy (and, in the nested case, fresh p-compensation ports with the same exact earlier-branch neutrality) rather than stacking multiplicity on one physical port.

This fresh-port realization is important: every occupied port has multiplicity one, so the factorial terms `v_r(m_j!)` vanish. The resulting column is therefore the exact linear branch-defect signature, not an approximation that silently drops multiplicity provenance.

For an earlier class-13 row r define the clean-atom cross coefficient

`a_{r q}=E_r(s_q)+v_r(s_q)-C_r(s_q)(v_r(s_q)+c_r)`.

The auxiliary prime does not change this coefficient for r<p, because it is larger than all earlier target primes and can be chosen away from every earlier endpoint/cancellation step. The p-compensation port, when required, is neutral on every r<p by the previous construction.

## 3. Signed matrix structure

### Theorem 3.1 — exact diagonal

For every clean q,

`a_{q q}=-c_q<0`.

Indeed `s_q` is its own coefficient-cancellation step, is not its own endpoint, and `v_q(s_q)=0` because `s_q<q`.

### Theorem 3.2 — no positive feedback to larger class-13 rows

If `r>q`, then

`a_{r q}<=0`.

Proof. Since `s_q<q<r`, neither `r|s_q` nor `h_r|s_q` can hold, so denominator and endpoint contributions are zero. The only possible nonzero contribution is an r-coefficient-cancellation event, which is negative. Hence the coefficient is nonpositive.

Thus, after ordering clean rows from larger q to smaller q, the clean signed matrix is lower-triangular in the causal sense needed for descending elimination: a later (smaller-q) atom cannot reawaken a row already closed at a larger q.

### Theorem 3.3 — dirty rows receive no negative clean-atom coefficient

Let `d in D` be a dirty class-13 row and `q in C` a clean row. Then

`a_{d q}>=0`.

More precisely, whenever `d<q`,

`a_{d q}=alpha_{d<-q}:=1_{h_d|s_q}+v_d(s_q)>=0`.

Proof. If the d-cancellation progression were nested in q's base step, then `s_d|s_q`. By the previously proved debt-poset monotonicity, q would inherit every class-19 debt coordinate already carried by dirty d, contradicting q being 19-clean. Therefore `C_d(s_q)=0`. What remains is exactly the endpoint plus denominator contribution displayed above. If d>q, Theorem 3.2 already gives `a_{d q}<=0`; absorption under class-19 neutrality forbids a negative dirty incoming channel, so the only possibility is zero.

This is the first point where the quotient becomes quantitative rather than Boolean: a clean suppressor can be completely class-19-neutral and still spend capacity on an absorbing dirty class-13 row.

## 4. Dirty rows become an explicit capacity ledger

Let an initial defect vector on the earlier class-13 rows be `b=(b_r)`. For a canonical clean-atom cloud with integer counts `n_q>=0`, realized with distinct fresh ports as above, the exact updated class-13 defects are

`b'_r=b_r+sum_{q in C} a_{r q} n_q`.

For a dirty row d, Theorem 3.3 gives an entrywise nonnegative dirty block:

`a_{d q}>=0` for every clean q.

Hence dirty defects are monotone:

`b'_d>=b_d`.

If `b_d>0` initially, repair is impossible under exact class-19 neutrality, recovering the absorbing-row obstruction. If `b_d<=0`, define its available slack

`S_d=-b_d>=0`.

Then keeping every dirty row nonpositive is exactly the finite family of capacity constraints

`sum_{q in C} a_{d q} n_q <= S_d`  for every `d in D`.

### Theorem 4.1 — exact canonical-cone reduction

Within the canonical fresh-port atom library, feasibility of a class-19-neutral repair of all higher class-13 rows is equivalent to the integer system

`A_C n <= -b_C`,

`A_D n <= S_D`,

`n in Z_{>=0}^{C}`,

where `A_C=(a_{r q})_{r,q in C}` is the signed clean block and `A_D=(a_{d q})_{d in D,q in C}` is entrywise nonnegative.

The dirty set can therefore be quotiented out of the active signed dynamics, but not discarded: it survives as an immutable capacity ledger attached to the clean cone. A quotient retaining only the clean matrix and forgetting `S_D` would admit repairs that are false in the original observer.

## 5. Exact causal closure on the clean subcone

Order the clean rows descending:

`q_1>q_2>...>q_m`.

Starting from the initial b, recursively define

`x_i=b_{q_i}+sum_{j<i} a_{q_i,q_j} n_j`,

and choose

`n_i=max(0, ceil(x_i/c_{q_i}))`.

Because `a_{q_i,q_i}=-c_{q_i}`, this makes the current row nonpositive:

`x_i-c_{q_i} n_i <= 0`.

Now consider any later atom q_j with j>i, so `q_j<q_i`. By Theorem 3.2 its coefficient on row q_i is nonpositive. Therefore future steps cannot reawaken q_i.

### Theorem 5.1 — finite causal closure

The recurrence terminates after finitely many clean rows and produces an integer vector n for which every clean row is nonpositive.

Moreover, at step i, `n_i` is the smallest nonnegative integer number of q_i-atoms that closes row q_i given the already-fixed earlier counts `n_1,...,n_{i-1}`.

This is an exact componentwise-minimal statement for the **causal descending policy**. It is not claimed to be the global integer-program minimum: a future smaller atom may have a negative cross coefficient on an earlier clean row, and more general arbitrary ports can simultaneously lie on several cancellation progressions. Those synergies are deliberately retained as a separate future optimization problem rather than erased by an unjustified minimality claim.

Combining Theorems 4.1 and 5.1 gives an immediate exact acceptance test for this causal policy:

`B_d:=sum_i a_{d,q_i} n_i <= S_d` for every dirty d.

If these inequalities hold, the causal clean closure uses only the available dirty slack. If one fails, the causal construction is not admissible; the failure is a provenance-bearing dirty-capacity witness, not generic numerical noise.

## 6. Second-layer dirty debt for a single clean suppression

For one clean q and one dirty class-13 d, put

`alpha_{d<-q}=1_{h_d|s_q}+v_d(s_q)`.

Each canonical q-cancellation copy pays exactly this nonnegative dirty-row amount before any other ports are added. Combining this with the earlier q-resource lower bound gives:

### Corollary 6.1 — single-q dirty-capacity lower bound

If a class-19-neutral repair demands at least k units of negative q-defect, then it needs at least

`ceil(k/c_q)`

q-cancellation copies. On any dirty d for which the occupied q-cancellation copies retain the base-step d incidence, the unavoidable dirty capacity spend is at least

`alpha_{d<-q} ceil(k/c_q)`.

This is a single-q resource bound. It must **not** be summed blindly over several q: one arbitrary port may lie on multiple clean cancellation progressions and share suppression work. The exact multi-q problem is the signed integer cone / shared-support problem, not the sum of independent one-row lower bounds.

## 7. Independent finite falsification/regression below 5000

Checker:

`research_checks/check_brc_clean_subcone_dirty_capacity_20260924.py`.

It independently reconstructs target primes, multiplicative orders, cancellation depths, clean/dirty status and the exact branch-defect coefficients. The run used only exact integer arithmetic and reported:

- target primes `<5000`: `166`;
- higher class-13 rows: `82`;
- 19-clean higher class-13 rows: `38`;
- 19-dirty higher class-13 rows: `44`;
- clean-to-dirty matrix pairs checked: `703`;
- structural matrix failures: `0`;
- nested-dirty-cancellation failures: `0`.

A new finite census feature appears in the dirty block. Positive intrinsic clean-to-dirty capacity edges are exactly

- `(d,q,alpha)=(37,2221,1)`;
- `(229,2749,1)`;
- `(37,3109,1)`.

This finite list is not promoted to an infinitude or classification theorem. Its significance is conceptual: **19-clean does not mean dirty-row-free**. A clean cancellation step can avoid every class-19 debt coordinate while still landing on an absorbing class-13 endpoint/denominator fiber.

As a regression against the earlier primitive-endpoint repair census, among the higher class-13 p with initially clean class-19 coordinates there are `30` cases. The causal clean closure respects every dirty capacity in `28`; the two failures are exactly

`p=2221` and `p=2749`.

The targets requiring at least one clean higher-class-13 atom are

`733, 1021, 1741, 1861, 2029, 2221, 3181, 3541`.

The capacity-admissible active cases are exactly

`733, 1021, 1741, 1861, 2029, 3181, 3541`,

reproducing the prior `7 rescued + 2 obstructed` split at the higher-class-13 layer. The `p=2029` case still leaves the already-known base-13 residual and therefore still requires the previously constructed base-13 suppressor cloud; this note does not silently declare that terminal coordinate closed.

Finite computation is falsification/regression only. The proof is the signed matrix structure, the debt-poset absorption theorem and the descending causal recurrence above.

## 8. BRC meaning

The correct residual quotient is not `delete dirty rows`. It is

`active clean signed cone + immutable dirty capacity ledger + terminal base-13 residual`.

This is a smaller state than the full branch vector but still sufficient for the canonical repair operations proved here. It preserves the residual information that can affect future admissibility:

- the clean row identity and cancellation depth `c_q`;
- the signed clean cross-defect matrix `A_C`;
- the nonnegative clean-to-dirty incidence matrix `A_D`;
- dirty slack `S_D` with endpoint/denominator provenance;
- base-13 residual handled by its separate established interface;
- p-neutral compensation provenance when a clean q-step is nested in the p cancellation progression.

Collapsing this to total signed defect, Boolean clean/dirty labels, or a clean-only matrix loses a scientifically active obstruction.

## 9. Do not repeat / next

Do not search for negative repair channels on dirty rows under exact class-19 neutrality; the absorption theorem already rules them out.

Do not call the causal vector globally minimal. Its minimality is conditional on the descending causal policy and the canonical fresh-port atom basis.

Do not sum single-q dirty lower bounds across different q without checking shared cancellation support.

If the formal D24 successor lifecycle remains blocked, the next nonredundant auxiliary unit is to analyze the shared-cancellation/nesting cone on the 19-clean subposet and determine when the causal capacity test is also globally optimal, or produce an exact integer-cone certificate for the gap.

If the canonical lossless staging-disposition/session-rollover operation becomes live, stop auxiliary work and return immediately to the Source-native D24 continuation path.
