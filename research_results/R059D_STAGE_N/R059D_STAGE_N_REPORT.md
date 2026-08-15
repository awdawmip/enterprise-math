# R059D Stage N REISSUE — Pure-Algebra Coupled Complementary Collapse

Researcher-ID: `EM-R059D-9C6B2A`
Taskbook source: `0ded98e376b649cbe41e47e18ea23c8c2daf59ca`
Frozen parent: `d6cfcb3435deac50901581cd4fa82e6b3cf588d3`

The superseded Stage-N path-language task was not read, consumed, or extended.

## 1. Scalar binary collapse

For declared adjacent completed states `L<n<U`, set `G=U-L` and a Boolean upper-collapse bit `b in {0,1}`, `b^2=b`:

`C(n;b)=L+G b`.

No local selector for `b` is assumed. The exact signed residue is

`rho(n,b)=n-C(n;b)`.

For `5` between `4` and `9`, `C=4+5b`; the residues are `+1` and `-4`. Nearest-rounding or absolute-residue ranking is not used.

Freeze: `PURE_ALGEBRA_BINARY_COLLAPSE_NORMAL_FORM_ESTABLISHED`.

## 2. Mandatory affine-sheet case

For `X=(100,0,0)` on `x+y+z=100`, declaring `y+=1` makes `(100,1,0)` leave the sheet. Exact preservation requires

`Delta x + Delta z = -1`.

If each transverse completed displacement is explicitly restricted to the adjacent pair `{-1,0}`, the direct integer solution set is exactly

`{(-1,+1,0),(0,+1,-1)}`,

giving endpoints `(99,1,0)` and `(100,1,-1)`.

Without this local minimality/completed-state gate, integer sheet conservation alone gives the infinite family `(t,+1,-1-t)`, `t in Z`.

## 3. Symmetric half-state and complementary bits

With the additional pre-collapse exchange hypothesis `Delta x=Delta z=a`, sheet conservation gives

`2a+1=0`, hence `a=-1/2`.

This `-1/2` is a derived pre-collapse algebra/precision carrier state under exchange symmetry, not an unconditional native packet quantity.

At integer endpoint precision its adjacent completed states are `-1,0`. Write

`Delta x=-1+b_x`, `Delta z=-1+b_z`, with Boolean bits. Sheet conservation gives exactly

`b_x+b_z=1`.

Thus the bit solutions are `(0,1)` and `(1,0)`. With `b=b_z`, `b_x=1-b`:

`Delta_y^+(b)=(-b,+1,-(1-b))`.

The image of the two bit assignments is exactly the direct integer solution set. Freeze:

- `SYMMETRIC_PRECOLLAPSE_HALF_STATE_DERIVED_UNDER_EXCHANGE_SYMMETRY`;
- `COUPLED_COMPLEMENTARY_COLLAPSE_BIT_REDUCTION_ESTABLISHED`;
- `DIRECT_INTEGER_HALF_STATE_COUPLED_BIT_EQUIVALENCE_ESTABLISHED`.

## 4. Why two branches, and why six transfer states

The two-branch result is not implied by sheet conservation plus integrality alone. It additionally needs a local minimality/completed-state condition, expressed either as the adjacent endpoint pair `{-1,0}` or an equivalent nonpositive single-unit compensation rule.

Under unit recipient increment and that gate, one of the two other coordinates contributes `-1` and the other contributes `0`. Hence each recipient has exactly two donor choices.

For three recipients, the derived elementary displacement set is

`D_transfer={e_i-e_j : i!=j}`,

with exactly `3*2=6` elements. Only after this derivation is it compared with

`u=e_x-e_y`, `v=e_y-e_z`, `w=e_z-e_x`,

and the derived set equals `{+u,-u,+v,-v,+w,-w}`.

Therefore the correct freeze is:

`THREE_AXIS_TRANSFER_SIX_STATE_EMERGENCE = ESTABLISHED_ONLY_WITH_ADDITIONAL_MINIMALITY_ASSUMPTION`.

Remove the minimality gate and each recipient again has infinitely many integer compensation decompositions.

## 5. Assumption necessity

The A1-A7 audit distinguishes logical, route-specific, alternative, and redundant assumptions:

- A1 affine conservation is necessary for same-sheet complementarity; without it four local endpoint combinations survive.
- A2 unit recipient increment is necessary for the elementary two-branch event; allowing increment `2` adds `(-1,+2,-1)`.
- A3 integrality is redundant when A5 already explicitly fixes `{-1,0}`, but matters if A5 is weakened to a continuous interval.
- A4 exchange symmetry is needed only for the unique `-1/2` pre-collapse bridge, not for direct integer enumeration.
- A5 adjacent endpoints are one sufficient minimality gate.
- A6 single-unit compensation is redundant given A5, but is an alternative minimality gate when A5 is absent.
- A7 completed-state typing is semantically required for a completed-collapse claim, though algebraically redundant if A3/A5 already enforce discrete completed endpoints.

This explicitly answers why the branch count is two rather than three or infinite and why the three-axis transfer set has six rather than more states.

## 6. General coupled Boolean collapse algebra

For local states

`C_i=L_i+G_i b_i`, `b_i^2=b_i`,

substitute into exact constraints `F_r(C)=0` and reduce to Boolean polynomials `P_r(b)=0`. Define

`B(F)={b in {0,1}^m : P_r(b)=0 for all r}`.

Classify exactly:

- `|B(F)|=1`: `UNIQUE_COLLAPSE_ASSIGNMENT`;
- `|B(F)|>1`: `MULTIBRANCH_ADMISSIBLE`;
- `B(F)=empty`: `INCONSISTENT_CONSTRAINT_SET`.

Multiple exact assignments are never forced to a unique answer.

Freeze: `BRC_CONSTRAINT_SOLUTION_SET_ALGEBRA_ESTABLISHED`.

## 7. Exact post-credit finite differences

After Boolean reduction, write the multilinear normal form

`R(b)=sum_S c_S prod_{i in S} b_i`.

Define exact differences `Delta_i R=R(b_i=1)-R(b_i=0)` and higher differences `Delta_T`.

For complementarity `P=b_x+b_z-1`, the squared exact residual reduces to

`Q=1-b_x-b_z+2 b_x b_z`,

so

`Delta_x Q=-1+2b_z`, `Delta_z Q=-1+2b_x`, `Delta_x Delta_z Q=2`.

The interaction coefficient comes from the exact constraint, not an arbitrary reward weight. Higher-order coefficients are recovered by exact finite differences/Mobius inversion.

Freeze: `POST_CREDIT_DISCRETE_DIFFERENCE_ALGEBRA_ESTABLISHED`.

## 8. Scalar/vector bridge and straightness toy

The `5 -> 4 or 9` and `-1/2 -> -1 or 0` cases share: adjacent completed states in their declared completion semantics, a Boolean up/down bit, signed residue, and possible coupling by higher-level exact constraints.

They are not identified: the gaps are `5` and `1`, the half-state requires exchange symmetry, the sheet couples two transverse bits, and no common local selector law has been proved.

Only after the algebra gate, a downstream rank-one straightness toy was tested. Repeated identical transfer branches form rank-one integer submodules; mixing the two complementary transfer vectors gives rank two. Hence straightness imposes branch consistency after an initial branch is chosen, but does not identify that first branch. Freeze only:

`STRAIGHTNESS_POST_CREDIT_CONSISTENCY_WITHOUT_INITIAL_BRANCH_IDENTIFICATION`.

## 9. Large-background covariance

For arbitrary integer `K`, including probes near `10^36`, the two minimal endpoints are

`(K-1,1,0)` and `(K,1,-1)`.

Both remain on `Pi_K`, with displacements `(-1,1,0)` and `(0,1,-1)`. The law is invariant under affine background translation, coordinate permutation, and global displacement inversion. No huge enumeration is used. `K` is not length, norm, angle, precision, or probability.

## 10. Interpretation boundary and validation

Stage N establishes an algebraic collapse carrier, exact set-valued constraint solutions, and a post-credit finite-difference calculus. It does not establish a full local BRC selector.

No Euclidean distance, angle, norm, trig, nearest rounding, endpoint-count argmax, path-language merge, arbitrary reward weights, ML fitting, floating equality, or physical-probability interpretation is used in the positive derivation.

Final deterministic checker: `5684 / 5684 PASS`.

Checks digest SHA256: `ccd95c5a149ab3de6b8654e962fcb9b2a898981fcdf8a741562723c809dcf1c4`.

Checker source SHA256: `3042c34eec82ddaa95b9959bed9ec9b8574d14c609cb6ea748a2f2b4272877f9`.

Checker output SHA256: `d298be02aee5f09aaa0b5bb5d3285ab1a761625553b23cba4a2d941ca4f3b967`.

`STOP_FOR_DRIVER_REVIEW`.
