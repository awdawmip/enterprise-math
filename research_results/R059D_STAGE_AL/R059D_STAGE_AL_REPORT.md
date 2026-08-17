# R059D Stage AL — Canonical Native Resolver Rigidity Report

Researcher-ID: `EM-R059D-AL-5A9D31`

Task: `RS-R059D-STAGE-AL-CANONICAL-NATIVE-RESOLVER-RIGIDITY`

## Primary disposition

`UNIQUE_CANONICAL_ENTERPRISE_NATIVE_RESOLVER_PROVED`

## Result

Stage AL closes the canonicality gap left by AK within an explicit non-tautological Enterprise-native admissible class.

The initial native axioms A0–A7 — fixed anchor class, one-edge locality, radius-uniform constant-size state, sampling-free target runtime, translation covariance, D6/reversal covariance, simple closure and axis-anchor completeness — are not sufficient. A pure-axis hexagon resolver satisfies them for every radius and differs from N first at `r=5`.

Even adding first-sector monotonicity, Motzkin/single-peak typing and the exact AG `J_N` count / accepted period remains insufficient. The packed-count law

`1^J 2^(r-J) 3^J`

has the exact accepted counts and period but differs from N already at `r=5`.

The missing native property is therefore local outer-support selection rather than count data.

## Final rigidity axiom A8

AL derives a primitive-support carrier from target triangular incidence and D6 symmetry.

The native rotation `R(a,b)=(-b,a+b)` uniquely fixes, up to scale, the integral invariant quadratic support index. Primitive normalization gives

`Q_E(a,b)=a^2+ab+b^2`.

`Q_E` is typed only as an incidence/support rank. It is not Enterprise length and not a Euclidean distance.

Elementary-triangle barycentric numerators are ranked by `Q_E`; each primitive edge receives the maximum rank of its two incident triangles; each vertex receives the minimum of those incident-edge pair ranks. The radius-r carrier is the sublevel set whose support rank does not exceed the anchor level `Q_E(3r,0)=9r^2`.

A8 requires the circle path to be the oriented outer monotone frontier of this carrier.

AG's accepted support theorem is used only to prove the coordinate certificate

`SUP(a,b)=9(a^2+ab+b^2)-9max(a,b)+3`

in the first sector. It is not used as the runtime definition of length or the AK turn operator.

## Uniqueness proof

The support finite differences show sectorwise downward closure and force a unique successor at every frontier state. At any hypothetical first divergence, an alternative either moves outside the carrier or refuses an available outward supported move. Both violate A8. The bisector move is fixed by D6/reflection compatibility.

Thus for every `r>=1` the admissible first-sector path is unique and equals `W_N(r)`. D6 covariance and axis-anchor completeness then make the full simple endpoint orbit unique. It is exactly the accepted AK fixed-length N turn orbit.

The uniqueness is geometric/orbit-level. AL does not claim one unique register encoding of that orbit.

## Canonical circle consequences

Within final `ADM_E` the terminology is upgraded from

`accepted N native circle`

to

`canonical Enterprise native circle`.

Its exact minimal turn period/circumference is

`T_r=C_E(r)=C_N(r)=6*(r+J_N(r))`,

with

`J_N(r)=floor(alpha*r+1/3)`, `3alpha^2+6alpha-1=0`, `alpha>0`.

Therefore the canonical native circle constant remains

`lim T_r/(2r)=kappa_E`,

`kappa_E^2=12`, `kappa_E>0`.

AI endpoint-convention robustness and AJ finite-sampling readout robustness survive unchanged.

## C_s typing

The inherited `C_s` family is not a co-equal primitive member of `ADM_E` because its pointwise law explicitly consumes the finite subdivision parameter `s` and majority coverage `2K_s>=s^2`, violating sampling-free A3.

The distinction is operational: at `r=5`, exact inherited replay gives

`J_C_1=1`, `J_C_2=1`, `J_C_3=0`,

while `J_N=1`.

AJ's theorem remains binding: all `C_s` are at most one layer behind N, their circumference differs by at most 6, and they share `kappa_E` uniformly in `s`. This makes them bounded finite-precision/readout perturbations, not separate primitive circle laws.

## BRC consequence

Orthogonal/source realizations may remain teacher/compatibility surfaces. But under A0–A8 the target orbit is no longer an arbitrary rasterization choice: target primitive-support frontier rigidity selects one native fixed-length turn orbit. The BRC bridge compares to that target state rather than defining it by Euclidean distance.

This conclusion is scoped to the frozen R059D admissible class and does not classify all imaginable discretization algorithms.

## Adversarial validation

The deterministic checker independently validates:

- D6 invariance of the primitive support index;
- `r=1..4096` equality of the AK/AH N word and the independently extracted A8 support frontier;
- checkpoints `8192,16384`;
- exact count/period consequences;
- simple D6 cycles on the direct bounded range;
- every Motzkin sector candidate for `r<=7` (`10,878` candidates total), with exactly one A8 survivor at each radius and that survivor equal to N;
- pure-hexagon and packed-count counterexamples;
- the operational C sampling-dependence witness at `r=5`;
- canonical AK runtime firewall.

Core checker result before external history compare:

`14267/14267 PASS`

Digest:

`bf1bee3b6baedab95a5d9dfc63dc47e2a88e1bbe4523ff4cfa43312e8cecb7ad`.

Finite enumeration/replay is adversarial implementation validation only. The all-radius uniqueness theorem is the first-divergence support-frontier proof.

## Boundaries kept open

AL does not prove:

- uniqueness among rules that reject one of final A0–A8;
- a unique information-theoretic internal turn-machine encoding;
- a sampling-free canonical C limit resolver;
- pointwise N/C_s equality;
- any theorem identifying `kappa_E` with the standard real number `pi`.

No AL-later stage is consumed.
