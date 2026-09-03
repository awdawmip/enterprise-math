# P000 six-axis Tropical Plücker / valuated-matroid return

Status: `SUCCESS / NONTRIVIAL_SURVIVOR / SIX-WEIGHT_PIECEWISE_LINEAR_CLASSIFIER_ONLY`

- Task: `RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID`
- Publication: `TP2-FEC91ABA20FAAFF4D480`
- Researcher: `EM-P000TP1-8F2C41`
- Claim: `chatgpt-p000tp1-20260830-1239-8f2c41`
- Execution record: `ER-5076DCC280C491A7DE7C`
- Exact checker: `research_checks/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID_CHECK_20260830.py`
- Certificate: `research_artifacts/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID/P000_TROPICAL_PLUCKER_CERTIFICATE_V1.json`

Hard target disposition:

`P000_TROPICAL_PLUCKER_SURVIVOR_GEOMETRY_NONTRIVIAL_OR_TAUTOLOGICAL_BOUNDARY_EXACTLY_CLASSIFIED`

The positive result is deliberately narrow. A nontrivial tropical survivor classifier exists on pre-frozen six-axis scalar weights and carries information not reconstructed by the tested Johnson/Pfaffian/residue coarse observables. No exact relation to an existing native collapse/transport invariant was proved. Therefore the collapse-interpretation gate fails: the object returned here is a **derived six-weight piecewise-linear classifier**, not a native P000 collapse law, factorization mechanism, Foundation object, or replacement of the native 6D geometry.

## 1. Frozen admissible weight registry

All weight families below were fixed before survivor inspection.

### W_COORD — declared six-axis scalar coordinate field

`w_ij=x_ij` on the already-declared six axis labels `AB,AC,AD,BC,BD,CD`.

- coefficient domain used for exact census: `Z`;
- defined on every axis;
- factor-blind and route-blind;
- no extra orientation, frame, factorization, or hidden state;
- admissible as the identity scalar-weight reading of the declared six-coordinate object;
- **not** declared to be a collapse cost.

### W_ABS — coordinate magnitude

`w_ij=|x_ij|`.

- domain `Z^6 -> N^6`;
- factor-blind and route-blind;
- no extra orientation or frame;
- independent generic magnitude semantics, not tuned to tropical survival;
- no native metric or collapse interpretation is inferred from the absolute value.

### W_VP — prime-adic valuation

For a prime `p` frozen before outcomes,

`w_ij=v_p(x_ij)`.

The deterministic finite checker uses nonzero coordinates; an extended formulation may use `v_p(0)=+infinity`.

- this is a reuse of `T1_SCALE_ENUMERATION_VALUATION`;
- route-blind but factor-specific, hence not factor-blind;
- no orientation or frame;
- this family is explicitly separated from the factor-blind positive classifier claim.

No weight was selected by inspecting tropical survivors, and no monotone transform was tuned to force the relation.

## 2. Exact tropical defect calculus

For any frozen six-weight vector define

`S=(s1,s2,s3)` with

` s1=w_AB+w_CD,`
` s2=w_AC+w_BD,`
` s3=w_AD+w_BC.`

Let `m=min(S)`, `M=max(S)`. Then

`delta_T = second_min(S)-min(S)`

has the exact symmetric formula

`delta_T = s1+s2+s3-M-2m`.

Equivalently, on a chamber `s_i <= s_j <= s_k`,

`delta_T=s_j-s_i`.

Hence

`delta_T=0 <=> the minimum of {s1,s2,s3} is attained at least twice`.

This is the full rank-2 / four-ground-element tropical Plücker relation under the task's min-convention. Thus a finite six-weight vector gives the declared rank-2 valuated-matroid typing exactly when `delta_T=0`. The typing itself is classical tropical/valuated-matroid mathematics; no priority claim is made for it.

Classical comparison used for terminology/typing: Battistella et al., *Buildings, valuated matroids, and tropical linear spaces*, Journal of the London Mathematical Society, DOI `10.1112/jlms.12850`.

## 3. Carrier symmetry and orbit/stabilizer classification

The frozen carrier `S4` action on the six edge labels induces the full `S3` on the three complementary-pair blocks

`(AB,CD), (AC,BD), (AD,BC)`

with kernel the Klein four group of order `4`.

Therefore `delta_T` is invariant under carrier `S4`: the action merely permutes `(s1,s2,s3)`. The complement involution swaps the two entries inside each complementary pair, so it fixes all three `s_i` and also fixes `delta_T`.

For the pair-sum pattern:

- all three `s_i` distinct: orbit size `6`, carrier stabilizer order `4`;
- exactly two equal: orbit size `3`, carrier stabilizer order `8`;
- triple tie: orbit size `1`, carrier stabilizer order `24`.

The survivor locus consists of exactly-two-equal-**minimum** states plus triple ties. Exactly-two-equal-maximum states are not survivors unless all three tie.

## 4. Exact all-box survivor theorem for W_COORD

Let every coordinate range independently over

`{-B,-B+1,...,B}`

and set `q=2B+1`. A single complementary-pair sum `a` has multiplicity

`m(a)=q-|a|`, for `|a|<=q-1`.

Because the three complementary pairs use disjoint coordinates, the three pair sums are independent with this triangular multiplicity.

### Triple ties

The number of states with `s1=s2=s3` is

`T(q)=sum_a m(a)^3 = q^2(q^2+1)/2`.

### Exactly two minimal pair sums

The number with exactly two equal minima and the third strictly larger is

`M(q)=q^2(q-1)(4q^2+q+3)/4`.

By sign reversal the same number has exactly two equal maxima.

### Tropical survivors

Therefore the exact survivor count for every `B>=0` is

`N_T(q)=T(q)+M(q)`

`      = q^2(4q^3-q^2+2q-1)/4`.

The all-distinct count is

`q^6-T(q)-2M(q)`.

Exact finite regressions:

| raw box | total | `delta_T=0` | `delta_T>0` | triple tie | exactly two minima |
|---|---:|---:|---:|---:|---:|
| `{-1,0,1}^6` | 729 | 234 | 495 | 45 | 189 |
| `{-2,-1,0,1,2}^6` | 15625 | 3025 | 12600 | 325 | 2700 |

This is an exact finite-box theorem, not an asymptotic density claim.

## 5. Other pre-frozen finite censuses

For `W_ABS`:

| box | total | survivor | nonsurvivor |
|---|---:|---:|---:|
| `{-1,0,1}^6` | 729 | 345 | 384 |
| `{-2,-1,0,1,2}^6` | 15625 | 5257 | 10368 |

For `W_VP`:

| valuation domain | total | survivor | nonsurvivor |
|---|---:|---:|---:|
| `p=2`, each coordinate in `{-2,-1,1,2}` | 4096 | 1984 | 2112 |
| `p=3`, each coordinate in `{+-1,+-2,+-3,+-4}` | 262144 | 176320 | 85824 |

These tables establish nonempty/nonuniversal finite survivor classes only; no infinite density is inferred.

## 6. Matched controls: delta_T is new information, but not complete information

Use the safe upstream quantities from the Johnson–Plücker task: Johnson `1+3+2` sectors, `Q_orb`, and carrier-orbit type of `rho`.

Define

`x=(-2,-2,0,2,1,1)`

and

`y=(-2,-1,-1,2,2,0)`.

They have identical tested coarse data:

- total coordinate sum `0`;
- `2 ||P0(.)||^2 = 22`;
- `6 ||Pm2(.)||^2 = 18`;
- `Q_orb=(-4,0,0)`;
- carrier-orbit type of `rho` equal to `((0,1,1),0)`.

But

- `delta_T(x)=0` from pair sums `(-1,-1,2)`;
- `delta_T(y)=3` from pair sums `(-2,1,1)`.

So `delta_T` is not reconstructible from this tested combination of existing Johnson-sector norm data, safe Pfaffian-orbit data, and integral splitting-residue orbit type.

The converse also fails. The states

`0=(0,0,0,0,0,0)`, `e1=(1,0,0,0,0,0)`, and `1=(1,1,1,1,1,1)`

all have `delta_T=0`, while `rho(0)!=rho(e1)` and `Q_orb(0)!=(Q_orb(1))`. Thus tropical defect adds a genuinely different coarse distinction but cannot replace the upstream arithmetic/representation observables.

An additional magnitude-weight matched control is

`u=(-3,0,0,0,0,0)`,
`v=(-2,-2,0,1,0,0)`.

They share Johnson coarse tuple `(-3,9,18)`, `Q_orb=(0,0,0)`, and carrier-orbit `rho=((0,0,1),0)`, while `delta_T(|u|)=0` and `delta_T(|v|)=1`.

## 7. Pfaffian-to-valuation bridge: exact classical shadow boundary

For the oriented upstream Pfaffian expression

`Q=x_AB*x_CD-x_AC*x_BD+x_AD*x_BC`,

set

`t1=x_AB*x_CD`, `t2=x_AC*x_BD`, `t3=x_AD*x_BC`

and, for a fixed prime `p`,

`alpha_i=v_p(t_i)`.

The `alpha_i` are exactly the three tropical complementary-pair sums for `W_VP`.

### Unique-minimum theorem

If `delta_T>0`, exactly one `alpha_i` is minimal. Let `m=min alpha_i`. Factoring `p^m` from `Q`, the uniquely minimal summand is a unit mod `p` while the other two are divisible by `p`. Therefore

`v_p(Q)=m`

and in particular `Q!=0`.

Consequently

`Q=0 => delta_T=0`.

This implication is the standard nonarchimedean/tropical cancellation shadow of the classical Plücker relation, not a new Enterprise theorem family.

### Cancellation is invisible to valuations

The converse is false, and even `v_p(Q)` is not determined on the tropical locus. At `p=3`, all three states

- `z0=(1,1,1,3,4,1)`;
- `z1=(1,1,1,3,1,1)`;
- `z2=(1,1,1,3,2,1)`

have the same coordinate valuation vector

`(0,0,0,1,0,0)`

and hence the same pair-valuation sums `(0,0,1)` and `delta_T=0`. Nevertheless

- `Q(z0)=0`;
- `Q(z1)=3`, so `v_3(Q)=1`;
- `Q(z2)=2`, so `v_3(Q)=0`.

Thus valuations locate the possible-cancellation tropical locus but erase the residue information that decides actual cancellation. This p-adic branch is classified:

`TAUTOLOGICAL_CLASSICAL_SHADOW_WITH_EXACT_CANCELLATION_BOUNDARY`.

## 8. Collapse interpretation gate

The task required a separate promotion gate before using the phrase “tropical collapse geometry”. That gate does **not** pass.

What is proved:

`PRE_FROZEN_SIX_WEIGHT -> EXACT_PIECEWISE_LINEAR_DEFECT -> NONTRIVIAL_SURVIVOR_CLASS`.

What is not proved:

`delta_T -> EXISTING_NATIVE_COLLAPSE_OR_TRANSPORT_INVARIANT`.

No exact identity, monotone law, factorization mechanism, safe quotient theorem, or native transport theorem was found connecting `delta_T` to a currently declared P000 collapse/transport quantity. Therefore freeze:

`PIECEWISE_LINEAR_CLASSIFIER != NATIVE_COLLAPSE_LAW != FACTORIZATION_MECHANISM`.

The term “tropical collapse geometry” is rejected at this stage.

## 9. Tool reuse and checker

- `T1_SCALE_ENUMERATION_VALUATION`: `REUSE_APPLIED` for valuation typing/census.
- `T3_TYPED_INCIDENCE_CIRCUIT`: `REUSE_APPLIED_FOR_VALUATED_MATROID_TYPING_ONLY`.
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED` for carrier orbit/stabilizer and equivariance checks.
- New general tool family: `NONE`.

The task-local checker uses exact integers only and no floating-point tie tolerance. It verifies carrier group actions, induced `S3`, stabilizers, defect laws, symmetry, raw exact formulas, finite censuses, matched controls, unique-minimum valuation law, `Q=0 => delta_T=0`, and same-valuation/different-residue counterexamples.

Local deterministic result:

`LOCAL_DETERMINISTIC_PASS checks=179794`.

## 10. Terminal verdict

Final task verdict:

`NONTRIVIAL_SURVIVOR`.

Precise meaning:

1. pre-outcome legal six-axis scalar/magnitude weight families produce survivor classes that are neither empty nor universal;
2. the tropical defect contributes an exact coarse distinction not reconstructed by the tested upstream Johnson-sector, `Q_orb`, and `rho` coarse data;
3. rank-2 valuated-matroid typing is exact on `delta_T=0`;
4. the `p`-adic/Pfaffian branch is a classical tropical shadow with a sharp cancellation-information boundary;
5. no native-collapse interpretation has been established.

Safe downstream wording:

`P000_DERIVED_SIX_WEIGHT_TROPICAL_CLASSIFIER_SURVIVES`.

Forbidden promotion without new evidence:

- `P000_NATIVE_TROPICAL_GEOMETRY`;
- `P000_TROPICAL_COLLAPSE_LAW`;
- `TROPICAL_PLUCKER_IS_A_FOUNDATION_AXIOM`;
- `VALUATED_MATROID_REPLACES_NATIVE_6D`;
- `DELTA_T_IS_A_FACTORIZATION_MECHANISM`.
