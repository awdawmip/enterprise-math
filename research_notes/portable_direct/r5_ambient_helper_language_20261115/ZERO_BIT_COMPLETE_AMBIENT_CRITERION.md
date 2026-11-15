# R5 — exact zero-bit criterion for old-helper sufficiency (all suffix languages)

Date: 2026-11-15. Frozen science: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`.
Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.
Scope: the auxiliary mixed weighted indexed-center observer with an explicitly declared one-step radius-two replacement operation. Inherits the fixed core and suffix decomposition of [AMBIENT_OLD_HELPER_GAP_THEOREM.md](AMBIENT_OLD_HELPER_GAP_THEOREM.md), saved earlier in the same directory.

## Theorem — a single old-language membership bit exactly determines repair cost

For integers \`d>=r>=3\`, take \`Y={e_0,...,e_(r-1)}⊂Q_d\`, where \`e_i\` is the indexed binary unit vector. Allow **any** old-state suffix language \`X\` satisfying \`Y⊆X⊆Q_d\`. Retain all five old mixed-optimal seven-event cores and both old first-suffix bits, with residual suffix \`u∈X\`. New a/ab targets have the prior exact core table with \`v∈Y\`; repair means directed center replacement distance at most two.

Then for every such X,

\`\`\`
kappa_a(X,Y;2) =
     r+2  if 0^d belongs to X,
     2r   if 0^d does not belong to X;

kappa_ab(X,Y;2) = 2r   in either case.
\`\`\`

Thus the **single typed residual bit** \`z(X)=1_{0^d∈X}\` is a complete statistic for these two minimum-library cardinality observers when the new language \`Y\`, radius, core table and one-step future operation are held fixed. This result covers every choice of old helper suffixes besides \`0^d\`, including arbitrary unions of weight-two neighbor states.

## Proof

### 1. Available upper bounds and forced baseline

For every \`e_i\`, the new target \`(1346,0,e_i)\` can be repaired only by \`(O1,0,e_i)\` or \`(O4,0,e_i)\` because the corresponding core distances to old cores are \`(3,2,3,3,2)\`. These \`r\` pairwise distinct *baselines* are required for every X. The old library
\`{(O1,0,e_i),(O0,1,e_i):0<=i<r}\`
exists since \`Y⊆X\` and repairs every a and ab target, proving \`kappa_a,kappa_ab<=2r\`.

If \`0^d∈X\`, the smaller a-library
\`{(O1,0,e_i):0<=i<r} ∪ {(O0,1,0^d),(O4,1,0^d)}\`
repairs every a target, giving \`kappa_a<=r+2\`. The preceding theorem's one-helper contradiction establishes a **language-independent** lower bound \`kappa_a>=r+2\` for all \`d>=r>=3\`, so this case is exact.

### 2. Four critical target types

For each \`e_i\`, consider exactly the four new a-targets:

- \`B_i=(1245,1,e_i)\`;
- \`C_i=(1246,1,e_i)\`;
- \`D_i=(1345,0,e_i)\`;
- \`E_i=(1346,0,e_i)\`.

There are \`4r\` distinct targets; covering these is necessary for a valid repair library.

**Key incidence lemma.** If an old suffix \`u≠0^d\`, then any single old configuration \`(Oj,s,u)\` can repair **at most two** of the \`4r\` critical targets.

Proof by Hamming weight \`w=|u|\`:

- \`w=1\`. If \`u=e_i∈Y\`, all other target suffixes are Hamming distance two, hence unavailable because every new-core/old-core base distance is at least one. For the one possible target suffix \`e_i\`, the explicit core-distance matrix shows that each old \`(Oj,s)\` repairs at most two of \`B_i,C_i,D_i,E_i\`. If \`u\` is a unit vector outside \`Y\`, its distance from all \`e_i∈Y\` is two and it repairs none.
- \`w=2\`. The old suffix can have Hamming distance one from at most two target unit vectors (the two coordinates in its support); all other distances are at least two. At suffix distance one, a repair must have core distance exactly one and matching first suffix bit. From the core table this permits only one critical *type* for a fixed old configuration: \`D_i\` from \`(O1,0,u)\`, \`B_i\` from \`(O0,1,u)\` or \`(O3,1,u)\`, or \`C_i\` from \`(O4,1,u)\`. Thus at most two critical targets are repaired.
- \`w>=3\`. Every \`e_i\` has Hamming distance at least two from \`u\`. Since every critical new-core/old-core distance is at least one, all repair distances exceed two. No critical target is covered.

This proves the incidence lemma. Notice that the excluded suffix \`u=0^d\` would be within one bit of **all r** target suffixes, precisely the state capable of violating this two-incidence bound.

### 3. Lower bound when 0^d is unavailable

If \`0^d∉X\`, the incidence lemma applies to every old entry in the candidate library. Covering the \`4r\` critical targets requires at least \`ceil(4r/2)=2r\` entries. The explicit same-suffix library from Step 1 attains this lower bound. Therefore \`kappa_a(X,Y;2)=2r\` for every such X, regardless of its other old helper states.

### 4. Double closure is unchanged by the ambient language

In the ab case, the additional new target \`(1236,1,e_i)\` has base core distance at least two from every old core, so each \`e_i\` forces a **distinct** old entry with first bit one and suffix exactly \`e_i\`. The \`r\` \`E_i\` targets force another r old entries with first bit zero and suffix exactly \`e_i\`; no entry satisfies both types. Hence \`kappa_ab>=2r\` for every X, and Step 1 attains it. QED.

## Finite reproducibility and observer scope

The companion \`VERIFY_ZERO_BIT_DICHOTOMY.py\` enumerates **all 32** admissible old languages \`X\` in the entire \`d=r=3\` cube, using exhaustive minimum set cover for a and ab with exact integers. It confirms:
- 16 languages without \`0\`: \`kappa_a=6\`;
- 16 languages with \`0\`: \`kappa_a=5\`;
- every language: \`kappa_ab=6\`.

The general theorem is proved by the incidence lemma and constructions; the finite run checks its first nontrivial dimension.

The quotient \`X↦1_{0∈X}\` preserves **only the declared output pair** \`(kappa_a,kappa_ab)\` for fixed Y and the given operation. It is not a certificate to erase other old-state provenance, individual shortest-repair witnesses, or consequences of future operation sequences. For example, the explicit optimal repair library still uses the full target-indexed suffix information \`e_i\`, and an alternate observer may distinguish nonzero members of X.

## Next open research unit

For arbitrary regular old language \`X\` and independently selected regular target language \`Y\`, compute a relation-preserving residual kernel for the **minimum library and the actual optimal witness family**, not only the minimum cardinality. Determine when a DFA quotient retains all old-helper-to-new-target repair incidences; attach a precise future-operation horizon to any further collapse.

Formal Task-ID/CLAIM/Activity authority remains independent of this author-side Draft PR publication.