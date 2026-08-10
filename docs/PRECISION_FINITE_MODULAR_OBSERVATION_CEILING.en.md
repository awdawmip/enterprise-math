# Finite Modular Observation Ceiling

Status: `RESEARCH BRIDGE / NONCANONICAL`

A finite family of modular observations has one exact combined arithmetic precision ceiling.

## 1. LCM is the joint finite precision

Let

`M_family={M_1,...,M_k}`

be a finite nonempty set of positive moduli and let

`D=lcm(M_1,...,M_k)`.

For integer values z,z':

`z == z' mod every M_i`

iff

`z == z' mod D`.

Thus the tuple of all declared finite modular observations has exactly the equality precision of one mod-D observation.  The several moduli may expose different prime-power directions, but their joint refinement is their lcm and is still finite.

## 2. Integer model data have a mod-D lift fiber

Consider a total integer linear/affine model whose actions, observations, offsets and other algebraic parameters are integer data.  Reduce every datum modulo D.

Any two exact integer lifts with the same mod-D data generate congruent outputs modulo D under every corresponding finite action word, because addition and multiplication respect congruence.  Therefore they generate identical outputs under every modulus M_i dividing D.

For the declared finite modular experiment family, all exact lifts inside one mod-D data fiber are operationally indistinguishable.

## 3. Identifiability criterion for exact properties

Let P be an exact integer property of the underlying model data: hidden free rank, Smith torsion, exact target reachability, unimodularity, exact action algebra, or another exact invariant.

A necessary condition for P to be certified from the finite modular experiment family is:

> **P must be constant on every admissible mod-D lift fiber consistent with the experiment.**

If two integer lifts have identical mod-D data but different P, no experiment restricted to the declared finite modulus family can distinguish them, regardless of how many corresponding finite action words are executed.

This is a deterministic identifiability statement, not a statistical limitation.

## 4. FIBER no-go as one lift-fiber witness

For any finite family with lcm D, compare

`diag(1,0)`

and

`diag(1,D)`.

They are identical modulo every M_i.  Exact integer structure differs:

- the first has one free hidden direction;
- the second has full rational rank and finite Smith torsion D.

Hence finite modular tests cannot certify that an apparently persistent hidden direction is genuinely free rather than a deeper finite torsion lift.

## 5. IMAGE no-go as another lift-fiber witness

Using the same scalar coefficient `q=D+1`, compare targets

`b_reach=q`,

`b_bad=q+D`.

The first exact equation `q x=q` is reachable; the second `q x=q+D` is not.  The targets are identical modulo every M_i, so the complete modular equations and solution sets coincide under all declared tests.

Hence finite modular tests cannot certify exact integer target reachability either.

## 6. Dynamic depth does not break a coefficient ceiling by itself

If two total integer dynamic models are congruent in all action/observation/offset data modulo D, running longer corresponding action words cannot escape that coefficient quotient.  Every future output remains congruent modulo D.

Future depth and arithmetic precision are separate resources:

- longer words can expose distinctions already present in the chosen coefficient world;
- they cannot recover integer information that was annihilated by the mod-D coefficient quotient if the complete model data are already congruent there.

To break such a lift ambiguity one must refine the coefficient precision (replace D by a nontrivial divisibility refinement), add non-modular/exact information, or impose an independent bound restricting the admissible lifts.

## 7. Refining a finite experiment family

Adding another modulus N changes the ceiling only by

`D -> lcm(D,N)`.

If N divides D, it adds no new equality precision.

If N does not divide D, the ceiling becomes strictly finer in the divisibility lattice.  A previously invisible exact lift difference becomes visible precisely when the new lcm no longer annihilates that difference.

No finite sequence of modular levels by itself equals exact integer access without a separate finite bound on the unknown integer structure.  Exact equality corresponds to surviving all modular refinements, not one fixed finite modulus.

## 8. Architecture consequence

The finite-modular ceiling principle unifies several current precision boundaries:

- p-adic free-vs-deep-torsion ambiguity;
- exact IMAGE reachability vs deeper congruence mimic;
- model-difference content divisor regions;
- CRT parallel prime-power refinement;
- modulus precision lattice `meet=gcd`, `join=lcm`.

The practical rule is:

> **Before interpreting a finite modular experiment as evidence for an exact integer property, ask whether that property factors through the experiment's lcm reduction.  If it does not, construct or rule out alternative integer lifts first.**

CRT, congruence, lcm refinement and polynomial compatibility are standard prior mathematics.  The project value is the exact finite-precision identifiability architecture.