# HODGE H0I Semantic Checkpoint

Date: `2026-08-22`  
Researcher-ID: `EM-HODGE-H0I-7B2D94`  
Task: `RS-HODGE-H0I-CODIM2-CLASS-FIRST-VECTOR-BUNDLE-ZERO-LOCUS-LIFTING`  
Owner branch: `research/hodge-h0i-codim2-class-first-lifting`  
Taskbook source: `3726e64557d625e36915028d83421d1f47b26fd2`  
Parent H0H-R1 head: `ad63f59be91dd04a0575e3e3772cc34a2873d8b6`  
Parent H0H-R1 semantic core: `04a0abdad437e777bd2476e360fa17d30059580fd6fcbc4269bcb4844bfdb298`

## Frozen disposition

`H0I_SOURCE_VECTOR_BUNDLE_CHOW_NORMAL_FORM_ALREADY_COMPLETE`

Hard target:

`CODIMENSION_TWO_CLASS_FIRST_LIFTING_SOURCE_INSTANTIATES_ROBUST_ATTRIBUTED_R2 = NOT_ESTABLISHED`

R3 preseed: `NOT_ESTABLISHED`  
H1: `NOT_ADMISSIBLE`

## 1. Class-first target exists independently

H0I does not define its target from `c2(S)`, `c2(Q)`, a Schubert cycle, or a known Chow basis.

Use the compact symmetric presentation of `Gr(2,4)` and write the complexified tangent at the base point as

`p+ = Hom(E,F)`, `p- = Hom(F,E)`, with `dim E=dim F=2`.

For `X in p+`, `Y in p-`, let the first isotropy bracket block be the End(E)-valued two-form

`A = Y wedge X`.

Before any candidate bundle is searched, define

`tau1 = (tr A)^2`,  
`tau2 = tr(A^2)`.

An exact 36-dimensional `(2,2)` exterior carrier calculation with the infinitesimal `sl2(E)`, `sl2(F)`, and center-difference action gives invariant dimension exactly `2`. `tau1,tau2` are invariant and linearly independent, so freeze

`V_target = Q tau1 ⊕ Q tau2`.

Because the Grassmannian compact model is symmetric, `[p,p] subset k`, so invariant forms are closed. Classical compact-group averaging identifies the declared invariant forms with de Rham cohomology at the source/control layer. Both basis elements are of Hodge bidegree `(2,2)`.

The formal Q-coordinate carrier is not assumed a priori to be the singular rational lattice. Rationality is established only after the independently generated algebraic cycles are compared.

Frozen target descriptors before bundle search include `(1,0)`, `(0,1)`, `(1,1)`, `(1,-1)`, `(1/2,0)`.

## 2. Actual Gr(2,4) algebraic source

Use all six standard Plücker charts `U_ij`.

On `U_I`, normalize a row-basis matrix `F_I` so pivot columns `I` are `I_2`. On `U_I∩U_J`,

`F_J = F_I[:,J]^-1 F_I`.

Therefore

`G^S_(J<-I)=F_I[:,J]^-1`

and `S*` transitions are inverse transposes. The quotient bundle `Q` is generated from the exact quotient maps `R_I:C^4->C^2` with kernel `W`; its transition is `G^Q_(J<-I)=R_J[:,C_I]`.

On an exact rational generic matrix all `216` triple-chart cocycle checks pass for `S`, and all `216` pass for `Q`.

Only after `V_target` is frozen is the candidate grammar frozen to

`S*`, `Q`, `L⊕L`, `L^2⊕L`, with `L=det(S*)`.

## 3. Bundle-first controls are positive but receive no lifting credit

For the section `e4*|_W` of `S*`, the zero locus has Plücker ideal

`(p14,p24,p34)`,

is reduced of projective dimension `2`, and on `U12` has local regular-sequence equations `(b,d)`.

For the section `e4 mod W` of `Q`, the zero locus has ideal

`(p12,p13,p23)`,

is reduced of projective dimension `2`, and on `U14` has local equations `(-c,-d)`.

Using only the source Chern-Weil polynomial and the exact bracket identities

`tr(X wedge Y) = -tr(Y wedge X)`,  
`tr((X wedge Y)^2) = -tr((Y wedge X)^2)`,

one obtains after target freeze

`c2(S*) = 1/2 (tau1 - tau2)`,  
`c2(Q)  = 1/2 (tau1 + tau2)`.

The regular-section/top-Chern theorem then gives the corresponding cycle classes.

These are bundle-first controls and receive zero Hodge lifting credit by themselves.

## 4. I3 class-first lifting succeeds on the declared benchmark carrier

The class matrix with columns `(Z_Sstar,Z_Q)` is

`[[1/2, 1/2], [-1/2, 1/2]]`

with determinant `1/2`.

Hence for an input target fixed independently as

`v = r tau1 + s tau2`

the exact rational cycle lift is

`Z(v) = (r-s) Z_Sstar + (r+s) Z_Q`.

Thus

`cl(Z(v)) = v`

for every declared `v in V_target`.

In particular,

`tau1 = [Z_Sstar]+[Z_Q]`,  
`tau2 = -[Z_Sstar]+[Z_Q]`.

The second direction is linearly independent from the divisor-product line: if `h=c1(det S*)`, then `h^2=tau1`, while `tau2` is independent in the exact exterior carrier. Therefore H0I is not merely replaying products of the p=1 divisor source.

The comparison also proves post-search that `tau1,tau2` lie in the rational cycle-class image on this benchmark; that rationality was not used to choose the candidates.

## 5. I1 has strict future compression but source attribution

Use four standard charts and the finite order-8 signed-permutation subgroup of constant `GL2` gauges.

For base bundle IDs `S*` and `Q`, the nonfinal raw gauge-prefix counts are

`[2,16,128,1024]`

for total

`1170`.

Complete future cocycle/gauge/class/section signatures have two classes per cut, total

`8`.

So the abstract operational reduction is

`1170 -> 8`

with exact dependency reduction and compositional factoring.

But this is exactly the ordinary nonabelian Čech bundle/gauge quotient already admitted to `B_std^codim2`.

`I1 attribution = SOURCE_INHERITED_LEVERAGE`.

## 6. I2 proves Boolean support is too weak, but source ideal algebra already repairs it

The sections

`(p12,p34)` of `L⊕L`

and

`(p12^2,p34)` of `L^2⊕L`

have the same radical support, but generic scheme multiplicity `1` versus `2`, and cycle classes `tau1` versus `2 tau1`.

Thus Boolean support would make an incorrect recoalescence.

Meanwhile

`(p12,p34)` and `(p12,p34+p12)`

generate the same ideal and must be recoalesced.

A provenance-aware scheme/ideal carrier therefore gives a real strict reduction from three section presentations to two cycle-provenance states while retaining multiplicity.

However exact ideal, radical, Gröbner/saturation, complete-intersection multiplicity and Chow readout are already admitted to the fair source baseline.

`I2 attribution = SOURCE_INHERITED_LEVERAGE`.

## 7. Why I3 also fails robust attribution

Against `B_raw^codim2`, the class-first map

`(r,s) -> (r-s,r+s)`

replaces a bundle/cycle search by a direct two-coefficient normal form.

But `B_std^codim2` already owns:

- source-generated Chern-class vectors;
- regular-section/top-Chern comparison;
- exact rational lattice/matrix inversion;
- Chow linear combinations.

Therefore it independently inverts the same `2x2` class matrix and constructs the same rational cycle.

`I3 attribution = SOURCE_INHERITED_LEVERAGE`.

No candidate is `ROBUST_TRANSFORM_ATTRIBUTED`.

## 8. Presentation and target leakage

Plücker chart relabeling, constant local `GL2` gauge changes, ambient `GL4` coordinate permutations, section generator recombination, and target-basis changes all transport the declared constructions exactly at the stated scope.

Known Schubert cycles, known Chow bases, known Hodge ranks and known `c2(S/Q)` answers are absent from generators.

The only classical algebraicity theorem used for bundle-first controls is the regular-section/top-Chern source theorem; it is not used to define `V_target`.

All load-bearing H0I mathematics is coordinate-free relative to the Enterprise native plane. No historical signed-origin-one or other obsolete native-coordinate semantics is used.

## 9. Scientific boundary

H0I reaches a stronger point than H0H-R1:

- a genuine degree-four `(2,2)` class-first carrier is constructed independently;
- a genuine codimension-two algebraic lift is constructed on that benchmark carrier;
- one target direction is not merely a divisor product;
- multiplicity/provenance is treated scheme-theoretically.

But every load-bearing normal form is still independently present in fair standard source mathematics.

Therefore the terminal classification is

`H0I_SOURCE_VECTOR_BUNDLE_CHOW_NORMAL_FORM_ALREADY_COMPLETE`.

The missing Hodge-special object is not existence of a benchmark cycle lift. It is a transform-caused class-first lifting mechanism whose proof leverage is not already Chern/ideal/Chow/rational-linear-algebra source structure.

`CODIMENSION_TWO_CLASS_FIRST_LIFTING_SOURCE_INSTANTIATES_ROBUST_ATTRIBUTED_R2 = NOT_ESTABLISHED`.

`CODIMENSION_TWO_ENTERPRISE_R3_PRESEED = NOT_ESTABLISHED`.

`H1_ADMISSIBLE = false`.

`Hodge_proved = false`.

`CI_NOT_REQUIRED_FOR_RESEARCH`.

## Semantic digest

`HODGE_H0I_SEMANTIC_CORE_SHA256 = 46978c8e27574b7c76e5677687ec4d5678e7beb379c9bd4393d0523250a42d0d`

This digest is over the canonical H0I semantic-core JSON, not a Git commit hash.
