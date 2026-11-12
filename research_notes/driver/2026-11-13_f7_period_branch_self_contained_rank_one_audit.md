# F7 Driver supplementary audit — self-contained rank-one descent
Date: 2026-11-13 (+08)
Status: supplementary mathematical proof audit; **not** a native Driver Review/Result admission.
Context: source-exposed Driver inspection of the original author's existing revision, not a claim of clean-blind independent discovery.

## Exact target and provenance

The F7 same-task revision, `research_returns/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_20260903.md` at commit `9016c2add9fca51ccd1fb18133827acfb543cef2`, §5, invokes an already accepted F4 rank-one signed-permutation theorem to eliminate the branch where `f` has a nonzero period. The exact frozen F7 Result is `RR-AA38973D56330E59D315` (Result record blob `3366edeae347e76b1f6a50bc45a6c6e4cd2dd472`). The following elementary proof verifies that dependency *within the stated F7 assumptions* without needing an external F4 theorem. This does not alter the author's Result, provenance or review admission.

## Lemma — one-dimensional exact additive isometry

Let `g:Z -> R` satisfy `g(0)=0`, `g(-n)=g(n)`, and `g(n)>0` for every `n != 0`. Suppose
```
B = [[a,b],[c,d]] in GL_2(Z),
g(ax+by)+g(cx+dy)=g(x)+g(y) for all x,y in Z.
```
Then `B` is a signed permutation matrix.

**Proof.** If each row of `B` has at most one nonzero entry, invertibility forces precisely one nonzero entry in each row and column, and `det B=+-1` forces both entries to be `+-1`.

Otherwise, one output row is mixed. Without loss, `ab != 0`. Apply the mixed finite difference `Delta_1^x Delta_1^y` to the identity. The input side vanishes, while the output side is
```
Delta_a Delta_b g(ax+by)+Delta_c Delta_d g(cx+dy)=0.
```
Because `B` is a lattice bijection, the two displayed output arguments range independently over `Z`. Hence `Delta_a Delta_b g` is a constant function. Reversing a signed step only translates and negates its finite difference. Put `L=lcm(|a|,|b|)`. Each `Delta_L` is an integer finite sum of translates of `Delta_|a|` and likewise of `Delta_|b|`; therefore `Delta_L^2 g` is constant.

It follows from exact discrete integration that `t -> g(Lt)` is a polynomial of degree at most two on all `t in Z`. Evenness and `g(0)=0` give `g(Lt)=alpha*t^2`, with `alpha=g(L)>0`. Substituting `(x,y)=(Lt,0)` and `(0,Lt)` into the exact conservation identity yields
```
alpha*(a*a+c*c)*t*t = alpha*t*t,
alpha*(b*b+d*d)*t*t = alpha*t*t.
```
Thus `a*a+c*c=b*b+d*d=1`. Both integer columns are signed coordinate vectors; because `det B=+-1` they occupy distinct coordinate axes. Therefore `B` is a signed permutation. QED.

## Application — F7 period branch

Assume the exact F7 hypotheses of the revised theorem: `f:Z^2 -> R_{>=0}`, `f(0,0)=0`, `f(-n,m)=f(n,m)`, and `n!=0 => f(n,m)>0`. Suppose `f` has a nonzero period and the four-dimensional integer automorphism `A` exactly conserves the sum of two copies of `f`.

Every period has zero old coordinate because its value at the origin must be zero. The nontrivial period subgroup is therefore `{0} x kZ` for some `k>=1`. The pair scalar has period subgroup exactly the direct sum of the two copies: any constant first difference in either independent slot must vanish by the nonnegative two-sided iteration argument. Preservation of the pair scalar by `A` therefore makes `A` preserve that subgroup and descend to an automorphism of `(Z x Z/kZ)^2`.

The induced automorphism of the free quotient `Z^2` is some `B in GL_2(Z)`. For `g(n)=min_{m mod k} f(n,m)`, finite minimization gives `g(0)=0`, `g(-n)=g(n)`, `g(n)>0` for `n!=0`. At each fixed pair of free old coordinates, the descended automorphism acts bijectively on the torsion fiber; minimizing the exact conservation law over this fiber gives `g(B(x,y)_1)+g(B(x,y)_2)=g(x)+g(y)`. The lemma makes `B` a signed permutation.

F7's A0 requires the first old input to have **nonzero old projection in both output slots**, i.e. both entries in the first column of `B` are nonzero. This contradicts signed permutation. Hence the F7 nonzero-period branch is impossible by a fully elementary internal argument.

## Review boundary

This is a dependency-reduction audit of §5 only. The remaining block-rank proof (§§6–8), current reviewer independence and current Source native review CAS have separate obligations. No mathematical Result or mother objective closure follows from this supplementary note. Original authorship remains with `EM-CBRCF7-83A1D4`.
