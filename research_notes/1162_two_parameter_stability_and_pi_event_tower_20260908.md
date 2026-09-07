# #1162 — two-parameter rough stability phase and the rotation-pi event tower

Status: RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-two-parameter-stability-pi-event-tower-20260908
At: 2026-09-08T01:10:00+08:00
Parents:
- `research_notes/1162_rough_observer_neutrality_character_estimator_20260908.md`
- `research_notes/1162_alias_prime_valuation_thickness_semigroup_20260908.md`

## 1. Universal two-parameter rough-refinement phase

Let a parent positive branch mass x split into child masses t_i x, with t_i>0 and sum_i t_i=1. Let the child alias magnitudes relative to the parent be rho_i>=1, with at least two distinct magnitudes in a genuine label-revealing refinement. Consider the power-family observer

O_(alpha,s)=x^alpha r^(2-s), alpha>0.

The fine/parent ratio is

F_(alpha,s)=sum_i t_i^alpha rho_i^(2-s).

Elementary finite inequalities give:

- if alpha<=1 and s<=2, then F>=1; it is strict in every nontrivial refinement unless alpha=1 and s=2 and all active label factors are neutral;
- if alpha>=1 and s>=2, then F<=1, again strict away from the common neutral point under genuine splitting/label change.

The mixed quadrants have no universal direction. A two-child witness with one same-magnitude child and one farther child has

F=t^alpha+(1-t)^alpha rho^(2-s), 0<t<1, rho>1.

For alpha<1,s>2, F decreases through 1 at

rho_c=[(1-t)^alpha/(1-t^alpha)]^(1/(s-2));

for alpha>1,s<2, F increases through 1 at

rho_c=[(1-t^alpha)/(1-t)^alpha]^(1/(2-s)).

Thus in the mixed quadrants even the sign of refinement change depends on microscopic branch proportion/label stretch. If a rough quotient does not retain those coordinates, monotonicity does not factor through that quotient.

The unique observer invariant under all positive branch splittings and all alias-label redistributions in this power family is

(alpha,s)=(1,2).

This is the finite robust form of the earlier double-neutral characterization of Basel.

## 2. Endpoint atom and a rotation blow-up scale

Use the dyadic antiperiodic alias tree. Let Q=2^m and xi_(2Q) be the chosen oriented generator of the cyclic 2Q-th root carrier, so xi_(2Q)^Q=-1. The two endpoint cylinders at depth Q are the descendants that can still converge to the boundary aliases ell=0 or ell=-1, equivalently K=|2ell+1|=1.

Their total probability is the exact finite algebraic quantity

P_Q^(1)=8/[Q^2(2-xi_(2Q)-xi_(2Q)^(-1))].

The endpoint cylinders are nested; their intersection is the boundary atom K=1. Hence

P_Q^(1) -> P(K=1).

Define the rotation blow-up scale by

Pi_rot^2 := 8/P(K=1)
          = lim_(Q->infinity) Q^2(2-xi_(2Q)-xi_(2Q)^(-1)).

No numerical pi is required in the finite carrier. In the standard Euclidean complex embedding,

2-xi-xi^(-1)=|1-xi|^2,

and the classical tangent-circle calibration identifies

Pi_rot=pi.

Thus Pi_rot is a rebuilt G2/N3-compatible rotation blow-up constant, not asserted as a new native N0 primitive.

## 3. Basel from the event normalization

The antiperiodic boundary law is

P(K=2n+1)=8/[Pi_rot^2(2n+1)^2].

Probability normalization yields

sum_(n>=0)(2n+1)^(-2)=Pi_rot^2/8.

The exact even/odd decomposition of the positive-integer reciprocal-square sum gives

zeta(2)=Pi_rot^2/6.

Under Euclidean compatibility Pi_rot=pi, this is Basel.

## 4. Pi consistency tower from independent finite carriers

The finite determinant/Newton carrier produces exact rational constants

r_m=zeta(2m)/Pi_rot^(2m)

once the continuum alias blow-up is typed by Pi_rot. The prime-valuation/thickness carrier on the same boundary gives

P_m := P(K is m-power-free)
     =1/[(1-2^(-2m)) zeta(2m)].

Eliminating zeta(2m) gives

Pi_rot^(2m)=1/[r_m(1-2^(-2m))P_m].

Examples from the exact determinant coefficients:

Pi_rot^2  = 8 / P(K=1),
Pi_rot^4  = 96 / P(K squarefree),
Pi_rot^6  = 960 / P(K cube-free),
Pi_rot^8  = (161280/17) / P(K fourth-power-free),
Pi_rot^12 = (638668800/691) / P(K sixth-power-free).

Thus different observer pipelines on the same finite-refinement boundary determine the same rotation scale. This is a cross-observer consistency tower: additive spectral determinant coefficients and multiplicative prime-skeleton events must agree on Pi_rot.

## 5. BRC meaning

The two-parameter phase gives a strict observer admissibility statement: in mixed regions, missing branch-proportion/label-stretch provenance can reverse the sign of refinement change. The event tower gives an independent cross-observer calibration between:

- root-of-unity alias cylinders;
- determinant coefficient carrier;
- prime-valuation skeleton/thickness carrier.

No microscopic derivative is used in these finite objects. LOG, Euclidean angle and classical pi are readout/calibration layers only.

`REUSE_APPLIED` remains in force for the pointwise prime-valuation and m-power skeleton/thickness operations in `src/enterprise_math/brc_rational_holonomy.py`.

## 6. Status / novelty boundary

Power-sum convexity, roots of unity, Euler products, power-free probabilities and pi root-of-unity limits are classical ingredients. No historical-first claim is made. The candidate synthesis is the rough-observer stability phase plus the multi-carrier Pi_rot consistency tower built on the exact alias-refinement probability carrier.

## 7. Next

1. derive finite-depth certified bounds for P_m and hence for Pi_rot from power-free alias events;
2. test whether determinant and thickness estimators bracket the same Pi_rot monotonically from opposite sides;
3. use the two-parameter phase to classify which proposed BRC compressions can safely discard mass-shape or alias-label coordinates.
