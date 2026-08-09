# A3 Guard-Image Lattice Supplement 04 — Reachable-Effect Quotients and State-Local Branch Erasure

Status: `RESEARCH WIP / EXACT RANK-ONE/TWO BRANCH-ERASURE CHECKER`

## 1. From branch reachability back to future-safe precision

The general A2/P023 principle says that a quotient is safe only when distinctions erased by it cannot produce different declared coarse futures.

A3 packages the hidden predicate geometry of a multi-guard coarse fiber as

\[
L_G=W(K_A).
\]

But reachability alone is not the final retention obligation. What matters is whether the branch patterns that are actually reachable produce different coarse effects.

Fix a coarse fiber `y` and let

\[
R_y\subseteq\{\mathrm F,\mathrm T\}^r
\]

be its reachable threshold patterns. Let

\[
E:\{\mathrm F,\mathrm T\}^r\to\mathcal Y
\]

be a caller-declared branch-effect map. Depending on the future language, `E(sigma)` may denote the current one-step coarse output, a full descended affine transition object, or another hashable coarse effect.

## 2. A3-G16 — Reachable-Effect Erasure Criterion

For the fixed coarse fiber,

\[
\boxed{
\text{hidden branch identity is erasable}
\iff
E|_{R_y}\text{ is constant}.
}
\]

Equivalently,

\[
\boxed{
|\{E(\sigma):\sigma\in R_y\}|=1.
}
\]

If two reachable patterns have different effects, two fine lifts of the same coarse state produce different declared coarse futures, so the quotient is not exact.

If all reachable patterns have the same effect, the coarse future is independent of which fine branch is taken. Unreachable patterns never occur in that fiber and impose no precision obligation.

This strictly extends the binary hidden-guard theorem: there both hidden signs occur in every fiber, whereas partial-rank multi-guard systems require comparing only the actually reachable set.

## 3. Unreachable branches create no precision obligation

\[
\boxed{
\text{a syntactically present branch}
\not\Rightarrow
\text{the current coarse state must distinguish it}.
}
\]

If

\[
\sigma\notin R_y,
\]

then `E(sigma)` may differ arbitrarily from every reachable effect without affecting exactness of the current fiber.

Future precision must therefore be indexed by reachable behavior, not by the total theoretical branch count of program syntax.

## 4. A3-G17 — Rank-one reachable patterns by a switch sweep

For rank-one hidden scores

\[
g+t h,\qquad t\in\mathbb Z,
\]

every nonconstant guard is monotone and flips its Boolean threshold exactly once.

If `h_j>0`, the first integer `t` with `g_j+t h_j>=0` is

\[
\boxed{t_j=-\lfloor g_j/h_j\rfloor.}
\]

If `h_j<0`, the last true point is `floor(g_j/(-h_j))`, so the next integer flips false:

\[
\boxed{t_j=\lfloor g_j/(-h_j)\rfloor+1.}
\]

A zero step coordinate is constant across the whole fiber.

Thus one can:

1. write the pattern at `t -> -infinity` directly;
2. sort all integer switch points;
3. flip all guards sharing each switch simultaneously;
4. emit the next reachable pattern.

If `q` guards are nonconstant,

\[
\boxed{|R_y|\le q+1.}
\]

This is sharper than the generic rank-one face bound `2q+1` because the integer binary convention assigns score zero to `True`, and each guard changes state only once along the line.

No `2^r` pattern enumeration is required.

## 5. Exact rank-two erasure

For rank two, Supplement 02 supplies exact reachability in the hidden parameter plane. If the program representation already contains an explicit branch-effect table over all Boolean patterns, checking its entries does not enlarge the representation asymptotically: each explicit pattern is tested by the exact rank-two solver.

Only effects of reachable patterns are collected. More than one distinct effect is an immediate non-exactness certificate; one common effect permits branch-identity erasure in that fiber.

For implicitly represented branch rules, future work should traverse the arrangement faces from Supplement 03 instead of materializing all `2^r` syntactic branches.

## 6. A3-G18 — State-local effect ambiguity

Define

\[
\boxed{a_E(y)=|\{E(\sigma):\sigma\in R_y\}|.}
\]

Then:

- `a_E(y)=1`: the current coarse fiber is exact for the declared effect language;
- `a_E(y)>1`: at least two fine lifts produce different declared coarse effects, so the quotient is not exact.

This is a finite cardinality witness, not a new entropy definition. It may later be related to P011/P023 fiber-ambiguity tools.

In low hidden rank,

\[
\boxed{a_E(y)\le |R_y|\ll 2^r}
\]

can be a strong reduction.

## 7. Implementation

Added:

- `src/enterprise_math/guard_branch_erasure.py`;
- `tests/test_guard_branch_erasure.py`.

Main APIs:

- `rank_one_reachable_patterns`;
- `rank_one_branch_erasure_report`;
- `rank_two_branch_erasure_report`;
- `BranchErasureReport`.

The report returns the exact reachable patterns, the distinct reachable effects, and a `safe_to_erase` Boolean.

Regression cases preserve two key examples:

1. a rank-one diagonal hidden lattice where mixed patterns are unreachable; arbitrary effects on those mixed branches do not force refinement if the two reachable branch effects agree;
2. a rank-two system `scores=(s,t,s+t)` where `(F,F,T)` is impossible, so a unique effect attached only to that unreachable branch creates no obligation, while a different effect on any reachable branch makes erasure unsafe.

## 8. Precision meaning

The precision obligation is refined from

`must know branch identity`

to

\[
\boxed{
\text{must distinguish only reachable branch classes with different coarse effects}.
}
\]

Hence:

- if `a_E(y)=1`, this state needs no additional relation refinement for the declared effect language;
- if `a_E(y)>1`, the state needs refinement or some retained relation/witness detail that separates the effect classes.

The latter does not yet determine the minimum refinement rank because piecewise exactness is known not to be monotone under arbitrary refinement; a structural minimum-partition solver is still required.

## 9. Ownership boundary with A2/P023

The criterion that `E` be constant on reachable future behaviors is a state-local specialization of general future-compatible quotient semantics, whose mother theory belongs to A2/P023.

A3 owns the computable reachable-set specializations:

- rank one: integer switch sweep;
- rank two: exact lattice halfplane solver;
- fixed higher rank: Supplement 03 reduces to lattice basis plus established fixed-dimension ILP.

A3 does not duplicate behavioral-equivalence mother theory.

## 10. Next

1. turn `a_E(y)>1` effect classes into a minimum guard/relation refinement obligation;
2. determine when state-local erasure over many coarse states can be compiled into a finite coarse program without exposing every guard;
3. traverse rank-two arrangement faces for implicit branch rules rather than explicit `2^r` tables;
4. connect branch-erasure reports directly to relation-rank / relation-quantum precision profiles;
5. pressure-test on an actual P021 or A3-to-A4 staged-support predicate family.
