# #1158 ↔ #1162 bridge — Viète principal-path amplitude, alias probability normalization, and internal Basel

Status: RESEARCH_NOTE / CROSS-ROUTE SYNTHESIS / NOT PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1158-1162-viete-probability-internal-basel-20260908
At: 2026-09-08T01:25:00+08:00
Sources:
- `research_notes/VIETE_1158_FINAL_SYNTHESIS_20260905.md`
- `research_notes/1162_viete_wallis_basel_single_alias_tree_20260908.md`
- `research_notes/1162_finite_determinant_even_zeta_20260908.md`

## 1. Deduplication: Pi_rot already belongs to #1158

#1158 already defines the internal rotation-completion constant `Pi_rot` before classical pi is named. Its finite Viète character chain proves, up to its fixed indexing convention,

Pi_m^rot = 2 / product c_j,

and the completion gives

product c_j = 2/Pi_rot.

The same #1158 synthesis independently identifies the Wallis completion by

Pi_rot = 2 W_infinity,

and only afterward uses classical analysis to identify Pi_rot with classical pi.

Therefore #1162 does not define a second pi-like constant. Its alias probability tree supplies a new probabilistic meaning for the already-existing #1158 Pi_rot.

## 2. Viète product is one alias atom amplitude

In the dyadic antiperiodic alias tree, the all-left principal path has transition probabilities

p_j=c_j^2

where c_j is exactly the corresponding positive Viète half-angle/character readout. Hence

P(L=0)=product_j c_j^2=(2/Pi_rot)^2=4/Pi_rot^2.

Thus the #1158 Viète product is the positive square root of one #1162 boundary atom probability:

sqrt(P(L=0))=2/Pi_rot.

Using Pi_rot=2W_infinity, the same atom also satisfies

P(L=0)=1/W_infinity^2.

Therefore the internal Wallis and Viète completions are two factorizations/readouts of the same principal alias atom.

## 3. All alias atom ratios without classical small-angle differentiation

Let z=xi_(2Q) be the oriented depth-Q root. For a fixed nonnegative signed alias ell, the depth-Q cylinder ratio is

P_(Q,ell)/P_(Q,0)
=|1-z|^2/|1-z^(2ell+1)|^2
=1/|1+z+...+z^(2ell)|^2.

As the root carrier refines, z->1. This is evaluation of a finite geometric polynomial at the identity, so

P(L=ell)/P(L=0)=1/(2ell+1)^2.

No microscopic derivative and no classical pi value is needed for this ratio.

Hence

P(L=ell)=4/[Pi_rot^2(2ell+1)^2], ell in Z.

## 4. Internal Basel before classical pi compatibility

Probability normalization gives

1=4/Pi_rot^2 * sum_(ell in Z)(2ell+1)^(-2).

Therefore

sum_(n>=0)(2n+1)^(-2)=Pi_rot^2/8.

Using only the integer even/odd decomposition

zeta(2)=sum_odd n^(-2)+(1/4)zeta(2)

yields the project-internal identity

zeta(2)=Pi_rot^2/6.

Only after invoking the already-established #1158 compatibility Pi_rot=pi does this become the classical notation

zeta(2)=pi^2/6.

This cleanly separates:
- #1158: construct/select/complete the principal rotation path amplitude and Pi_rot;
- #1162: construct the full positive alias probability carrier and normalize all branches.

## 5. Integer Renyi moments: internal cross-check with the determinant route

Define

M_m=sum_(ell in Z) P(L=ell)^m, m>=1.

From the atom law,

M_m
=2(4/Pi_rot^2)^m sum_(n>=0)(2n+1)^(-2m)
=2(4^m-1) zeta(2m)/Pi_rot^(2m).

The independent finite determinant/Newton route produces the exact rational constants

r_m=zeta(2m)/Pi_rot^(2m)

without Bernoulli input, so

M_m=2(4^m-1)r_m

is rational. Exact first values are

M_1=1,
M_2=1/3,
M_3=2/15,
M_4=17/315,
M_5=62/2835,
M_6=1382/155925.

Thus the probability-tree route and determinant-coefficient route already cross-check each other internally before classical Pi_rot=pi calibration. The Bernoulli numerator 691 at m=6 appears equivalently inside the rational sixth Renyi concentration through `1382=2*691`.

## 6. Unified readout table

One boundary carrier now supports:

- principal path amplitude -> Viète product;
- same atom amplitude via adjacent-integer factorization -> Wallis product;
- sum over all atoms -> Basel normalization;
- prime-valuation coordinates of atom labels -> Euler product;
- integer power moments of atom probabilities -> even-zeta / determinant rational hierarchy.

These are not claimed as new classical identities. The project-level synthesis is that #1158 and #1162 are two observer levels of one rough-stable finite-refinement carrier rather than separate formula-reconstruction projects.

## 7. BRC meaning

The bridge demonstrates an observer lattice:
- deterministic principal path;
- full labeled branch distribution;
- total mass normalization;
- unlabeled weight moments;
- prime-valuation relabeling.

The principal-path quotient is sufficient for Viète but not Basel/Euler. Total mass is sufficient for Basel but not higher Renyi or prime observers. Retaining the full carrier avoids later recovery by unstable microscopic differentiation.

## 8. Next

1. determine whether #1158's independent Wallis finite approximants can be mapped to explicit finite statistics of the same alias atom, not only the shared limit;
2. derive the rational Renyi recurrence directly from branch splitting and compare term-by-term with determinant Newton recursion;
3. explore whether other completed constants/AGM routes in #1158 correspond to nonlinear statistics of the same alias probability carrier.
