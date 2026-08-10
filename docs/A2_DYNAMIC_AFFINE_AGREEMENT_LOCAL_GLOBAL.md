# Dynamic Affine Agreement: Finite Future Closure × Finite Arithmetic Certificate

Status: `L3 RESEARCH BRIDGE / NONCANONICAL`

This note is a consumption bridge between the frozen dynamic affine model-separation owner and the sibling A2/P023 affine local-global theorem. It introduces no new generic lattice mathematics.

## 1. The infinite-word agreement problem

Take two finite-dimensional total-affine integer models with the same named action alphabet. Ask whether there exists an integer initial state x such that the two models produce identical declared outputs after **every corresponding future action word**.

Homogeneous augmentation converts every affine action and observation into an integer linear system. The paired-model construction then generates the Z-row module of all homogeneous future-output differences.

After HNF closure, split a basis row as

`(a_i,c_i)`.

The complete all-word agreement condition is one finite affine system

`A_infinity x = -c_infinity`.

## 2. Infinite future language has a finite exact closure stage

The homogeneous paired future rows form a finitely generated Z-action module. The HNF action-module compiler reaches an invariant row lattice after finitely many horizon steps.

Therefore the infinite word language does not require an infinite history search. There is a finite stabilization horizon `h_*` such that the affine difference equations through `h_*` already generate every later equation.

This finite future closure is the **semantic timing certificate**. A scalar summary such as difference content is not sufficient; earlier work gives a sharp content plateau followed by later refinement.

## 3. The final affine equation has a finite target-specific arithmetic certificate

Once the final system

`A_infinity x=-c_infinity`

is known, exact agreement existence is an ordinary integer affine IMAGE problem.

The sibling local-global theorem supplies a finite certificate modulus for this **fixed** target:

- choose integer rational-left-null rows Q of `A_infinity`;
- let

  `B=||Q(-c_infinity)||_infinity`;

- let

  `E=exp(Tor(coker(A_infinity)))`;

- choose any D with

  `D>B` and `E|D`.

Then

`A_infinity x=-c_infinity over Z`

iff

`A_infinity x == -c_infinity (mod D)` is solvable.

So for one fixed pair of dynamic models, the all-future exact agreement-existence question has a finite arithmetic certificate even when no finite modulus could work uniformly over all possible affine offsets/model lifts.

## 4. Two independent finite resources

The exact decision therefore needs two conceptually different finite resources:

1. **future-language closure depth** — enough horizon to obtain the full invariant homogeneous difference module;
2. **arithmetic separation precision** — enough modulus to decide IMAGE membership for the final fixed affine target.

Neither substitutes for the other.

A deep-enough modulus applied too early can miss a future equation.

A complete future equation family observed at too coarse a modulus can still admit spurious modular agreement states.

## 5. Sharp two-axis witness

Use one state and the common action

`x -> x-1`.

Compare current observations whose difference is

`2x+2`.

### Horizon zero

Agreement requires

`2x+2=0`,

which has exact solution

`x=-1`.

### Horizon one

After the common translation, the same output difference becomes

`2x`.

Complete agreement through horizon one therefore requires both

`2x+2=0`,

`2x=0`.

The exact agreement set is empty.

### Mod 2 is too coarse

Both equations reduce to

`0=0 mod2`.

So mod2 still reports agreement states even though the exact system is inconsistent.

### Mod 4 is exact

Modulo4 the two equations are inconsistent, matching the exact world.

The generic local-global certificate reproduces this threshold:

- the linear equation map has Smith/torsion exponent `E=2`;
- a rational left-null difference between the two rows sees target obstruction magnitude `B=2`;
- the least multiple of2 strictly above2 is

  `D=4`.

Thus this one model pair needs both

`h>=1`

and

`arithmetic precision >= the mod-4 certificate`

for an exact finite decision.

## 6. Full-row-rank uniform-offset boundary

If the stabilized linear constraint map `A_infinity` has full row rank, its cokernel is finite. Then one modulus

`E=exp(coker(A_infinity))`

uniformly decides exact agreement existence for **every** affine target/offset vector on that same stabilized linear system.

If a free cokernel remains, no finite modulus can do this uniformly over unrestricted affine offsets. A fixed model pair still has a target-specific finite certificate, and a bounded offset family has a uniform bounded certificate.

This is exactly the IMAGE open/closed distinction consumed in a dynamic setting.

## 7. Agreement-state multiplicity remains a separate FIBER question

After IMAGE solvability is established, the exact agreement states form an affine coset of

`ker_Z(A_infinity)`.

Modulo D, a nonempty agreement set is a coset of `ker(A_infinity mod D)` and its cardinality is given by the Smith kernel formula.

Therefore the finite existence certificate does not replace the FIBER analysis:

`IMAGE says whether any common initial state exists;`

`FIBER says how many state directions remain indistinguishable once it does.`

## 8. Scope boundary

This theorem depends on:

- finite-dimensional integer state;
- total-affine actions/observations;
- the Z-module future closure;
- profinite-exact descent of integer affine equations.

It must not be carried automatically to nonlinear or general relational world laws. The profinite-ghost boundary gives a concrete nonlinear equation with compatible solutions at every finite modulus but no integer solution.

## 9. Prior-art boundary

Finite-dimensional observability modules, affine homogeneous coordinates, HNF/Smith theory and linear congruence local-global facts are standard prior mathematics. The Enterprise Math value is the exact separation and recomposition of two precision resources:

`finite future closure × finite arithmetic certificate`.