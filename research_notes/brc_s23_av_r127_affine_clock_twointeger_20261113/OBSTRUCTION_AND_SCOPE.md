# R127.3 — Exact obstruction to silently deleting the third floor

Within the same S23 rotated Boolean observer, take `x=0`, `A=2`, `d=4`, `E=9`, `m=2`, and `J=(0,1/4)`. Here `gcd(A,d)=2` does not divide `E=9`, so the integer-affine relation `E=u*A+v*d` of R127.1 has no solution.

Take two rational parameters `theta_0=1/20` and `theta_1=3/20`, both inside J.

| theta | n=floor(A theta) | k=floor(d theta) | r=floor(E theta) | ({Z_0}<{E theta}, {Z_1}<{E theta}) |
|---|---:|---:|---:|---|
| 1/20 | 0 | 0 | 0 | (1,1) |
| 3/20 | 0 | 0 | 1 | (1,0) |

At `1/20`: `{2 theta}=1/10`, `{6 theta}=3/10`, `{9 theta}=9/20`. At `3/20`: `{2 theta}=3/10`, `{6 theta}=9/10`, `{9 theta}=7/20`. Both share `(n,k)=(0,0)`, yet have different `r` and distinct joint Boolean signatures.

Therefore **the pair `(n,k)` alone is not a sufficient observer state for this concrete input**. Any exact two-integer algorithm for this example must retain additional information, such as a real-phase region, an explicit branch, a bounded modular residue, or other equivalent witness. This counterexample applies only to the claim that `r` can be discarded as a function of `n,k`; it does not rule out other two-integer mixed-linear formulations.

This exact worked input also illustrates the project-wide joint-observer preservation rule: two states that agree under a coarse floor-coordinate projection can differ under a subsequent joint observer. The original signed phase coefficients and source semantics remain part of the model.

Next, investigate whether a rational-linear relation `qE=UA+Vd` leads to a two-integer congruence certificate with bit-polynomial rather than `O(q)` explicit residue branches.
