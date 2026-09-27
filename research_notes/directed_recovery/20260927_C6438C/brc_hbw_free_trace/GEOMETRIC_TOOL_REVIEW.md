# Geometric scope and Kummer valuation: shared-context review

Status: **FULL_TEXT_SYMBOLIC_REVIEW / NO_SCIENTIFIC_EXECUTION / NOT_ADMISSION**.

Reviewed final sources:

- `LINEAR_X6_ORDER_SCOPE.md`: SHA-256 `ca04beb3a4b807d93337ac598615ebfa2f19e16a4da3f968880252fd7295eee1`.
- `KUMMER_RETURN_VALUATION.md`: SHA-256 `3b7a522fdb487bb5fdbe054a8e41a517f7f067881fdd5ac1822d367a1975f222`.

Both complete texts were read. **No substantive mathematical defect found.** This record does not report an elliptic implementation, a numerical experiment, or independent formal admission.

For the linear scope, the semisimple eigenvalue orders divide p^d_i-1 and each nilpotent Jordan part is killed by p^e at the stated largest block size. Their common bound gives the claimed matrix-order divisibility. Unit integer determinant guarantees invertibility after reduction. The p>d specialization, affine homogeneous dimension increase, and exclusions for adaptive/nonlinear/branching computation are correct. A factor observation may occur before full return, so no general factoring lower bound follows. A fuller scope discussion is in `LINEAR_X6_SCOPE_REVIEW.md`.

For the Kummer identity, let p^e be one proof-only component. Away from O modulo p, the x-coordinate is finite and the full-point identity ideal and Kummer infinity ideal are both units. Near O, Y is a unit; write u=X/Y and v=Z/Y. The exact local residue-ring equation is `h*v=u^3` with `h=B-A*u^2-u*v` a unit. Thus `(u,v)=(u)`, without needing any inverse of u. The regular primitive Kummer representative is `[h:u^2]`. Its second coordinate has valuation `min(2*v_p(u),e)`, whereas the full-point identity ideal has depth `min(v_p(u),e)`. Local unit changes of either projective representation preserve these ideals, so the capped valuation equalities yield the exact global divisor formula `gcd(L,N)=gcd(g_point^2,N)`.

The source correctly distinguishes a regular extension of a morphism from illegally cancelling a nonunit in a stored tuple. It also requires actual geometric point representations and primitive/unimodular coordinates. For arbitrary unrelated tuples the theorem would be false, and the admission contract must establish the relation rather than infer it from a convenient gcd.

The practical implication is accurately limited: x-only arithmetic may save coordinates, inversions and work while retaining prime support, yet it does not retain unsquared full-point return depth at prime powers. A proper denominator gcd is still a valid factor with an exact division certificate. Saturation is not a factor or proof of failure of the full-point observer. No free square-root recovery, useful exponent selection or factoring success probability is asserted.

The new `GEOMETRIC_NEXT_TOOL.md` is this reviewer's separate design, hence not independently peer-reviewed by this record. It explicitly proposes a fixed-unit-difference Montgomery ladder, whose chart-closure proof avoids per-step content gcds, while keeping the Kummer valuation limitation. That design remains unimplemented and should receive the parent's separate review.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
