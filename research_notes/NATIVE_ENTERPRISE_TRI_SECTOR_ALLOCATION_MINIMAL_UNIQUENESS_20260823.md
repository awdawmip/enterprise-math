# Native Enterprise typed tri-sector allocation：minimal uniqueness inside the linear C3 class

Status: `FREE_RESEARCH_EXACT_CONDITIONAL_UNIQUENESS / TYPED_CELL_CORRECTION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

## 1. Question

The prime patterns are meaningful as native-coordinate evidence only if the integer allocation was fixed without looking at primality. This note classifies the allocation inside a deliberately narrow, transparent class of simple rules **on the canonical typed affine Cell charts**.

This typed version supersedes the earlier research interpretation that deduplicated shared-axis Cell states through one global half-open min-zero address. Canonical Enterprise semantics distinguishes `VADDR` from `CADDR` and retains distinct sector-local Cell trajectories/anchors.

No claim is made that every nonlinear, nonlocal, or history-dependent allocation must coincide with this rule.

## 2. Typed Cell charts

For each open native sector use its canonical affine Cell chart:

- `C_12(a,b)`;
- `C_23(b,c)`;
- `C_31(a,c)`;

with both local components in `N_0`.

The three `C_ij(0,0)` are distinct origin-anchor Cells.

The three sectors are related by the native cyclic symmetry `C3`.

## 3. Unique linear component-step shell coordinate

Fix one sector and write its typed local Cell coordinates as `(u,v) in N_0^2`.

Let a candidate linear shell readout be

`S(u,v)=alpha*u+beta*v`.

Require:

1. anchor normalization `S(0,0)=0`;
2. one step in either positive native component increases shell by one:
   `S(u+1,v)-S(u,v)=1` and `S(u,v+1)-S(u,v)=1`;
3. the same rule is transported cyclically to all three sectors.

The unit-step conditions force

`alpha=beta=1`.

Therefore the unique linear typed-Cell shell coordinate in this class is

`s=u+v`.

This selection is prime-free and uses native component content rather than carrier Euclidean radius.

## 4. Shell cardinality

At fixed `s>=0`, one typed sector contains exactly

`(u,v)=(s-t,t)`, `0<=t<=s`,

so exactly `s+1` Cells.

Because the three sector Cell charts are typed/distinct, the full shell contains

`|Shell_C(s)|=3(s+1)`

Cells.

At `s=0` these are exactly the three distinct anchor Cells incident to the origin.

## 5. Unique gap-free shell start

Require positive integers to be allocated shell by shell in increasing s, with no gaps and no duplicate typed Cell states, starting at integer 1.

The first integer on shell s is forced to be

`B_s^C = 1 + sum_{j=0}^{s-1} 3(j+1)`

so

`B_s^C = 1 + 3s(s+1)/2`.

No primality information enters this formula.

## 6. C3-equivariant unit-step within-shell allocation

Now impose the minimal within-shell class:

- the three typed sector blocks are contiguous;
- each block uses consecutive integer labels along the side coordinate t;
- the same side-coordinate rule is transported cyclically to all three sector blocks.

Choose presentation slot `sigma in {0,1,2}` and `0<=t<=s`. Then the allocation is forced to

`N_C(s,t,sigma)=B_s^C+t+sigma*(s+1)`

up to:

1. cyclic choice of which sector is numeric block 0;
2. simultaneous reversal `t -> s-t` in all three sector blocks.

These six choices form the natural `C3 x C2` / dihedral presentation family.

## 7. Relation to the legacy research variable r

Earlier experiments used

`N(r,t,sigma)=1+3r(r-1)/2+t+sigma*r`,

with `r>=1`, `0<=t<r`.

Set

`r=s+1`.

Then identically

`N(r,t,sigma)=N_C(s,t,sigma)`.

Thus all numerical experiments remain valid. The corrected meaning is

`LEGACY r = TYPED CELL TRACE SHELL s + 1`.

## 8. Consequences independent of prime fitting

Before primality is evaluated, the rule already implies:

- exact elementary triple-Cell incidence label formulas;
- the local second-difference curvature pair `{2,4}` up to orientation presentation;
- the seven-Cell star Poisson law;
- the shell/transverse filament coordinate;
- the global typed carrier seam label identities.

Prime-incidence results are therefore consequences of a prime-free allocation that is conditionally unique inside this linear/component-step/gap-free/C3-equivariant class.

## 9. Presentation audit

The strongest global connectivity statements were independently replayed over all

`3 cyclic starts x 2 side orientations`.

Every presentation gives:

- zero fully-prime cross-sector seam bridges;
- mod-30 maximum eligibility component size 9.

So the sharp-nine/prime-5 connectivity results do not depend on selecting one visually favorable member of the six-presentation family.

## 10. Boundary

This is a conditional uniqueness theorem for a deliberately simple allocation class. It does not rule out every nonlinear or nonlocal native integer allocation.

Correct freeze:

`WITHIN TYPED AFFINE CELL CHARTS + LINEAR UNIT COMPONENT SHELL + GAP-FREE C3-EQUIVARIANT UNIT-STEP ALLOCATION, N_C(s,t,sigma) IS UNIQUE UP TO D3 PRESENTATION.`
