# #1162 — Viète, Wallis, Basel and Euler as readouts of one dyadic alias tree

Status: RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-viete-wallis-basel-single-alias-tree-20260908
At: 2026-09-08T01:20:00+08:00
Parents:
- `research_notes/1162_q_chain_markov_gauge_stabilization_20260908.md`
- `research_notes/1162_alias_prime_valuation_thickness_semigroup_20260908.md`
- earlier project Viète/Wallis rotation-product lines as compatibility context

## 1. One antiperiodic dyadic probability tree

Start with the nonzero antiperiodic phase theta_0=1/2. Under dyadic alias refinement the positive branch transition is

p_r(theta)=sin^2(pi theta)/[4 sin^2(pi(theta+r)/2)], r=0,1.

For the left endpoint child r=0,

p_0(theta)=cos^2(pi theta/2).

Along the all-left path,

theta_j=1/2^(j+1),

so the depth-m cylinder probability is

P_m(left^m)=prod_(j=0)^(m-1) cos^2(pi/2^(j+2)).

The path converges to the signed boundary alias L=0. Therefore

P(L=0)=prod_(j=0)^infinity cos^2(pi/2^(j+2)).

The already-proved alias boundary law gives

P(L=ell)=4/[Pi_rot^2(2ell+1)^2], ell in Z,

where Pi_rot is the root-of-unity identity blow-up constant, classically pi. Thus

P(L=0)=4/Pi_rot^2.

Taking the positive square root gives

prod_(j=0)^infinity cos(pi/2^(j+2))=2/Pi_rot.

Under classical compatibility Pi_rot=pi, this is the Viète half-angle product.

## 2. Wallis is a second factorization of the same atom amplitude

The classical Wallis product may be written

2/pi=prod_(n=1)^infinity [(2n-1)(2n+1)/(2n)^2].

Therefore, after Pi_rot=pi calibration,

sqrt(P(L=0))
=
Viète dyadic path product
=
Wallis adjacent-integer product.

The two products do not define two unrelated appearances of pi in this framework: they are two factorizations of the square root of one boundary atom probability.

No novelty is claimed for either product identity itself.

## 3. Every alias atom is a generalized Viète path

Every signed integer alias ell has a finite dyadic digit prefix followed by an eventual endpoint tail. Its exact path probability telescopes to

P(L=ell)=4/[Pi_rot^2(2ell+1)^2].

Hence

sqrt(P(L=ell)/P(L=0))=1/|2ell+1|.

Thus the odd integer alias magnitude is directly the inverse relative branch amplitude. Prime valuation of the odd alias is therefore an exact algebraic re-coordinate of branch-probability ratios, but positive BRC uses the squared probabilities; phase/amplitude signs are not silently reintroduced.

## 4. Basel is normalization of all generalized Viète branches

Total probability gives

1=sum_(ell in Z)P(L=ell)
 =4/Pi_rot^2 sum_(ell in Z)(2ell+1)^(-2).

Therefore the positive odd reciprocal-square sum is Pi_rot^2/8, and the even/odd integer decomposition yields

zeta(2)=Pi_rot^2/6.

With Pi_rot=pi this is Basel.

Thus:
- Viète reads one deterministic endpoint path/atom;
- Basel normalizes all endpoint atoms of the same tree.

## 5. Euler product is the multiplicative coordinate factorization of all atoms

Passing from the positive odd alias magnitude K=|2L+1| to its odd-prime valuation vector is lossless. Under the native inverse-square alias probability, the prime valuations are independent geometric variables:

P(v_p=k)=(1-p^(-2))p^(-2k).

Therefore the same total-probability normalization factorizes as

1=(8/Pi_rot^2) prod_(p odd)(1-p^(-2))^(-1),

or

prod_p(1-p^(-2))=6/Pi_rot^2.

After Pi_rot=pi this is the Euler product at s=2.

Thus:
- additive/radix coordinates expose the refinement tree;
- multiplicative/prime coordinates expose the Euler product;
- both are coordinates on one boundary carrier.

## 6. Structural synthesis

The same boundary quantity admits four readouts:

1. `Viète`: square root of one atom probability, factored by dyadic refinement depth;
2. `Wallis`: square root of the same atom probability, factored by adjacent integer ratios;
3. `Basel`: normalization after summing all atom probabilities;
4. `Euler`: normalization after lossless prime-valuation factorization of atom labels.

This is not a historical-priority claim. DFT/Viète/Wallis/Basel/Euler ingredients are classical. The project-level candidate synthesis is that one rough-stable dyadic alias probability carrier realizes all four without using microscopic differentiation.

## 7. BRC meaning

This bridge respects typed information levels:
- a single path is deterministic branch provenance;
- all atom weights form a positive exact-weight distribution;
- prime valuations are a lossless integer coordinate on odd labels;
- phase/amplitude information is separate from positive squared branch mass.

Do not collapse to total probability when future prime/alias/path observers are requested.

## 8. Next

1. connect the finite Viète cylinder probabilities to explicit error bounds for Pi_rot without continuum derivatives;
2. identify whether the project’s previous Wallis/sine-product route has an exact finite port/determinant realization of the same atom;
3. test analogous single-atom/all-atom decompositions for rational holonomy phases and Dirichlet L-values.
