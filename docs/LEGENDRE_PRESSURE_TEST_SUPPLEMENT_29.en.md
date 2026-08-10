# Legendre Pressure Test — Supplement 29

Status: `PROVED RESEARCH NOTE`  
Scope: branch-local Bonferroni proof precision for realized factor-to-root splitting  
Depends on: P017 L069 exact Mobius rough counts and finite inclusion-exclusion  
Discipline: Bonferroni inequalities are classical. This supplement does not replace exact Mobius semantics; it measures how much truncated factor-overlap information is sufficient to certify the required positivity.

## 1. Exact occupancy need not require exact full inclusion-exclusion

L069 expresses each root-branch occupancy as an exact p-rough count

\[
R_p[a,b]
=
N-S_1+S_2-S_3+\cdots,
\]

where

\[
N=b-a+1
\]

and `S_j` is the sum of counts divisible by every prime in each `j`-element subset of the primes below `p`.

To prove

\[
R_p[a,b]>0,
\]

one does not always need the complete alternating sum.

## 2. Odd Bonferroni lower bounds

For odd depth

\[
d=2m-1,
\]

define

\[
\boxed{
B_d
=N-S_1+S_2-\cdots-S_d.
}
\]

The usual Bonferroni inequalities for the union of small-prime divisibility events give

\[
\boxed{
B_d\le R_p[a,b]
\qquad(d\text{ odd}).
}
\]

Therefore

\[
\boxed{
B_d>0
\Longrightarrow
R_p[a,b]>0.
}
\]

This is a rigorous early-stop certificate.

## 3. P017-L070-A — Branch-local proof depth

Status: `PROVED`.

For an occupied p-rough interval `I=[a,b]`, define

\[
\boxed{
h_B(I,p)
=
\min\{d\ge1:d\text{ odd and }B_d(I,p)>0\},
}
\]

when such an odd truncation exists.

For `p=2`, there are no smaller primes, so occupancy is exact at depth zero:

\[
\boxed{h_B(I,2)=0.}
\]

If no odd truncation becomes positive before the finite small-prime family is exhausted, write

\[
h_B(I,p)=\mathrm{FULL}
\]

to mean that one should fall back to the exact Mobius count.

Crucially,

\[
\boxed{
h_B=\mathrm{FULL}}
\]

does **not** mean the interval is empty. It means only that this particular lower-bound proof language did not certify positivity early.

## 4. P017-L070-B — Split-shell proof precision

Let

\[
W_p^-,W_p^+
\]

be the two L068 subwindows of an actually split shell.

Define

\[
\boxed{
h_p^-(k)=h_B(W_p^-,p),
\qquad
h_p^+(k)=h_B(W_p^+,p).
}
\]

If both are finite odd depths, the shell split is certified at

\[
\boxed{
h_p^{\rm split}(k)=\max(h_p^-(k),h_p^+(k)).}
\]

The maximum is required because the theorem needs positivity on **both** root branches.

If either side is `FULL`, then the shallow Bonferroni language alone does not close the split proof and exact inclusion-exclusion or another certificate must finish it.

## 5. P017-L070-C — Proof precision genuinely jumps

Status: `PROVED BY EXACT FINITE CERTIFICATES`.

The following realized split shells have different minimum Bonferroni depths.

### k=8, p=3

Both branch occupancies are already proved at first order:

\[
\boxed{
(h_p^-,h_p^+)=(1,1),
\qquad
h_p^{\rm split}=1.
}
\]

### k=18, p=7

First-order inclusion-exclusion is insufficient on both branches, while depth three succeeds:

\[
\boxed{
(h_p^-,h_p^+)=(3,3),
\qquad
h_p^{\rm split}=3.
}
\]

### k=104, p=13

The two branches no longer have the same proof burden:

\[
\boxed{
(h_p^-,h_p^+)=(5,3),
\qquad
h_p^{\rm split}=5.
}
\]

Thus proof precision is neither constant in `p` nor symmetric across the two sides of the same root boundary.

## 6. P017-L070-D — Exact semantic state and proof state must remain separate

The represented shell split bit is simply

\[
\mathbf1[R_p^->0]\mathbf1[R_p^+>0].
\]

Its truth value does not depend on which proof method establishes positivity.

Bonferroni depth records a different object:

\[
\boxed{
\text{how much small-prime intersection information is sufficient to certify that truth}.
}
\]

Therefore

\[
\boxed{
\text{semantic precision}
\neq
\text{proof precision}.
}
\]

Two branches can represent the same Boolean truth while requiring different proof horizons.

## 7. Relation to P018/P023 task precision

The exact branch truth is an observable. Truncating inclusion-exclusion depth is a hierarchy of proof-state partitions over possible local divisibility configurations.

As depth grows, the proof state refines. Once a positive lower bound appears, the occupancy certificate is permanent under further exact refinement.

This is the same structural pattern already seen in P018 adaptive precision:

\[
\boxed{
\text{refine observations until a predicate certificate becomes permanent}.
}
\]

L070 supplies a concrete sieve-theoretic instance tied directly to the L067 repair spectrum.

## 8. Potential algorithmic use

For computing or proving `S(k)`, one may proceed per branch:

1. use the L068 overshoot test to discard raw nonsplits;
2. try low odd Bonferroni depth on both sides;
3. stop as soon as both lower bounds are positive;
4. only difficult branches escalate to deeper inclusion-exclusion, exact Mobius, rough recursion, or CRT/Jacobsthal tools.

This is exact adaptive proof precision rather than approximate counting.

## 9. Executable specification

- `src/enterprise_math/rough_bonferroni.py`
- `src/enterprise_math/p017_root_split_proof_precision.py`
- `tests/test_p017_root_split_proof_precision.py`

Tests verify that every odd truncation is below the exact rough count and pin the proof-depth jumps `1 -> 3 -> 5` at the explicit split-shell witnesses above.

## 10. Foundation feedback

The new chain is

\[
\boxed{
\text{exact state truth}
\to
\text{finite proof-language hierarchy}
\to
\text{minimum certificate depth}.
}
\]

This suggests that Enterprise Math should keep **proof precision** as a first-class quantity distinct from represented state precision whenever theorem discovery or finite verification cost matters.
