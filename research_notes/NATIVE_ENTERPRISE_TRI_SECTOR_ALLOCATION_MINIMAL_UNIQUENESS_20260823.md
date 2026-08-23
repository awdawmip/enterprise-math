# Native Enterprise tri-sector allocation: minimal uniqueness inside the linear C3 class

Status: `FREE_RESEARCH_EXACT_CONDITIONAL_UNIQUENESS / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

## 1. Question

The prime patterns are only meaningful as native-coordinate evidence if the shell allocation was not selected after looking at primality. This note classifies the allocation inside a deliberately narrow, transparent class of simple native rules.

No claim is made that every conceivable nonlinear Enterprise allocation must coincide with this one.

## 2. Unique C3-symmetric linear shell coordinate

Let a candidate shell readout on canonical addresses be linear:

`R(a,b,c)=alpha*a+beta*b+gamma*c`.

Require:

1. origin normalization `R(0,0,0)=0`;
2. cyclic axis symmetry `R(a,b,c)=R(b,c,a)`;
3. native axis unit normalization `R(n,0,0)=n` and cyclic equivalents.

Cyclic symmetry forces

`alpha=beta=gamma`.

Axis normalization forces the common coefficient to be 1.

Therefore the unique readout in this class is

`R(a,b,c)=a+b+c`.

Thus the tri-sector shell index `r=a+b+c` was not fitted to prime data; it is the unique C3-symmetric linear extension of the native unit axis coordinate.

## 3. Shell cardinality

Under the canonical `min(a,b,c)=0` atlas, use oriented half-open sector charts so shared axes are counted once.

At shell `r>=1` each of the three sectors contributes exactly r addresses. Hence

`|Shell(r)|=3r`.

This is a direct consequence of the three positive sectors and does not use a Euclidean radius.

## 4. Unique gap-free shell start

Require positive integers to be allocated shell by shell in increasing r with no gaps and no duplicates, starting at integer 1.

The first integer on shell r must then be

`B_r=1+sum_{j=1}^{r-1} 3j`

so

`B_r=1+3r(r-1)/2`.

No primality information enters this formula.

## 5. C3-equivariant within-shell allocation

Now impose the simple within-shell class:

- the three half-open sector blocks are contiguous;
- each block uses unit integer step along its side coordinate;
- cyclic sector relabeling uses the same side-coordinate rule in each block.

Choose a presentation slot `sigma in {0,1,2}` and side position `t in {0,...,r-1}`. Then the allocation is forced to

`N(r,t,sigma)=B_r+t+sigma*r`,

up to:

- which positive axis is chosen as the first cyclic slot;
- global orientation reversal of the half-open sector presentation.

Those are presentation choices, not changes to shell cardinality or the C3 block structure.

## 6. Consequences independent of prime fitting

Before primality is evaluated, the rule already implies:

- every folded C3 fiber is `B_r+t, B_r+t+r, B_r+t+2r`;
- its common arithmetic difference is exactly native shell index r;
- the equal-coordinate locus is the geometric side midpoint for even r;
- the midpoint label bouquet is the symmetric quadratic triplet already studied.

Therefore the main prime structures are consequences of a coordinate rule that is conditionally unique inside the C3-symmetric linear/gap-free/unit-step class.

## 7. Boundary

This is a conditional uniqueness theorem, not a claim that nonlinear, nonlocal, history-dependent, or alternative native shell notions are impossible.

The correct statement is:

`WITHIN LINEAR C3-SYMMETRIC AXIS-NORMALIZED SHELLS + GAP-FREE C3-EQUIVARIANT UNIT-STEP ALLOCATION, THE TRI-SECTOR RULE IS UNIQUE UP TO PRESENTATION.`

That is sufficient to remove the strongest post-selection concern for the current experiment while leaving broader native allocations open for later ablation.
