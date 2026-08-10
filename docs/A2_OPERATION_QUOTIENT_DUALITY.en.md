# A2 — Operation–Quotient Duality and the Order Core of P008

Status: `PROVED_WIP / EXECUTABLE_CHECKED / STACKED_ON_STAGE4 / NOT CANONICAL_MAIN`  
Owner: A2 future-compatible quotient mother layer  
Consumes: canonical P023/P024 quotient repair, canonical generic operation congruence, and frozen Stage-4 safe-operation algebra at `core/a2-safe-operation-algebra-v3@09450e3ac7a09e56895a2e6fdc6ecf0c521ba438`.

## 1. The reverse question needs one correction

Stage 4 defines the natural safe-operation spectrum of a quotient

\[
q:X\to Q,
\qquad
\theta=\ker q
\]

relative to a declared ambient operation family `A` by

\[
\operatorname{Spec}_{\mathcal A}(q)
=
\mathcal A\cap\operatorname{Pol}(\theta).
\]

It is tempting to reverse this arrow and ask whether an operation family determines a unique natural quotient.

For total operations, that is false without additional data.

The correct reverse problem is:

> which quotient geometries are congruences for the declared operation language, and which one is selected after the current observation/context is imposed?

This note makes that distinction exact.

## 2. A2-OQD-T01 — total operations alone cannot uniquely select a quotient

Let `X` have at least two states and let `A` be any family of total finitary operations on `X`.

Both the equality relation

\[
\Delta_X
\]

and the universal relation

\[
\nabla_X
\]

are congruences for every total operation in `A`.

Therefore

\[
\boxed{
|\operatorname{Con}(X,\mathcal A)|\ge2.
}
\]

In particular,

\[
\boxed{
\text{a family of total operations alone cannot select a unique quotient.}
}
\]

This is not a defect. The operation language determines an **admissible congruence geometry/lattice**, not an observed resolution by itself.

The statement is intentionally scoped to total operations. In a legality-sensitive partial-operation theory, the universal relation can fail compatibility because enabledness/domain membership is part of future behavior. That is why the FQ-006 partial-operation layer is a genuine extension rather than a cosmetic reformulation.

## 3. A2-OQD-T02 — finitary congruence reduces exactly to unary elementary translations

Let `f:X^r->X` be a total `r`-ary operation. Fix a coordinate `i` and fix values for every other coordinate. The resulting map

\[
T_{f,i,\mathbf a}(x)
=
f(a_1,\ldots,a_{i-1},x,a_{i+1},\ldots,a_r)
\]

is an **elementary unary translation/context** of `f`.

For an equivalence relation `theta`,

\[
\boxed{
\theta\text{ is a congruence for }f
\iff
\theta\text{ is preserved by every }T_{f,i,\mathbf a}.
}
\]

### Proof

The forward direction is immediate by fixing all unchanged coordinates.

Conversely, suppose every elementary translation preserves `theta`. If

\[
x_j\mathrel\theta y_j
\qquad(j=1,\ldots,r),
\]

change the inputs from `(x_1,...,x_r)` to `(y_1,...,y_r)` one coordinate at a time. Each step is one elementary translation applied to a `theta`-related pair, so the output remains `theta`-related at every step. Hence

\[
f(x_1,\ldots,x_r)
\mathrel\theta
f(y_1,\ldots,y_r).
\]

∎

This is classical universal algebra. Its Enterprise Math consequence is operational: **the existing unary finite-family P023 engine already suffices for arbitrary finite finitary operation languages after compiling basic operations to elementary translations.** No second quotient-repair mother theory is needed.

## 4. A2-OQD-T03 — operation + observation selects the largest compatible forgetting relation

Let `A` be a total finitary algebra on `X`, and let

\[
O:X\to Y
\]

be the current observation. Let `Pol_1(A)` denote all unary polynomial/context maps generated from the basic operations, identity and fixed parameters.

Define

\[
\boxed{
\Theta_{\mathcal A,O}
=
\bigcap_{p\in\operatorname{Pol}_1(\mathcal A)}
\ker(O\circ p).
}
\]

Equivalently,

\[
x\mathrel{\Theta_{\mathcal A,O}}y
\iff
O(p(x))=O(p(y))
\quad
\text{for every unary context }p.
\]

Then:

1. `Theta_(A,O)` is an equivalence relation;
2. `Theta_(A,O) subseteq ker O`, because the identity context is allowed;
3. `Theta_(A,O)` is an `A`-congruence;
4. every `A`-congruence `rho` satisfying `rho subseteq ker O` also satisfies
   `rho subseteq Theta_(A,O)`.

Hence

\[
\boxed{
\Theta_{\mathcal A,O}
=
\max\{\rho\in\operatorname{Con}(X,\mathcal A):\rho\subseteq\ker O\}.
}
\]

In partition language, this is the **coarsest refinement of the current observation on which every required operation is exact**.

### Why T03 is a congruence

Suppose `x_i Theta y_i` for every coordinate of a basic operation `f`. To test any outer observation context `p`, change the arguments of

\[
p(f(x_1,\ldots,x_r))
\]

to the `y_i` one coordinate at a time. At each step, all other arguments are fixed parameters, so the tested map of the changed coordinate is itself a unary polynomial context. The definition of `Theta` preserves its observed value. Therefore the final outputs remain `Theta`-equivalent.

### Why T03 is maximal

If `rho` is any congruence below `ker O`, every polynomial/context operation preserves `rho`. Thus `x rho y` implies `p(x) rho p(y)`, and `rho subseteq ker O` then gives `O(p(x))=O(p(y))` for every `p`. Hence `rho subseteq Theta_(A,O)`.

The construction is standard congruence/context logic. In the finite unary case it is exactly the operation-word future-distinguishability closure already canonicalized in P023.

## 5. A2-OQD-C01 — canonical P023 is already a finitary congruence compiler

For finite `X` and finitely many basic finitary operations:

1. compile every basic operation into all of its elementary unary translations;
2. feed that finite unary family into canonical P023 `stable_family_partition`;
3. start from the current observation partition.

The stable result is exactly the largest algebra congruence contained in the observation kernel, or equivalently the coarsest observation refinement compatible with the entire finitary algebra.

New executable bridge:

- `src/enterprise_math/operation_quotient_duality.py`;
- `tests/test_operation_quotient_duality.py`.

The implementation deliberately reuses `src/enterprise_math/operation_quotient.py`; it does not duplicate P023 refinement.

## 6. A2-OQD-T04 — P008 interval quotients preserve the chain lattice exactly

Let

\[
V(0)=0<V(1)<V(2)<\cdots
\]

and define the P008 quotient by

\[
q_V(n)=k
\iff
V(k)\le n<V(k+1).
\]

Because the basin classes are ordered intervals, `q_V` is monotone. Hence for all `x,y`:

\[
\boxed{
q_V(\min(x,y))
=
\min(q_V(x),q_V(y)),
}
\]

and

\[
\boxed{
q_V(\max(x,y))
=
\max(q_V(x),q_V(y)).
}
\]

Therefore every P008 complete-growth quotient is a lattice homomorphism

\[
(\mathbb N_0,\min,\max)
\longrightarrow
(\mathbb N_0,\min,\max).
\]

Every lattice term generated from `min`, `max`, projections and constants consequently descends exactly.

This gives a positive counterpart to the Stage-4 arithmetic no-go:

\[
\boxed{
\text{order lattice survives every P008 interval collapse,}
}
\]

while ordinary addition, multiplication and nontrivial polynomial unary arithmetic are generally destroyed by nonlinear complete growth.

## 7. A2-OQD-T05 — convex partitions are exactly the congruences of a chain lattice

Let `(C,<=)` be a chain equipped with

\[
x\wedge y=\min(x,y),
\qquad
x\vee y=\max(x,y).
\]

An equivalence relation `theta` on `C` is a lattice congruence if and only if every `theta`-class is convex.

### Congruence implies convexity

Suppose

\[
a\le b\le c,
\qquad
a\mathrel\theta c.
\]

Meet both sides with `b`:

\[
a\wedge b=a
\mathrel\theta
c\wedge b=b.
\]

Thus `a theta b`; similarly join with `b` gives `b theta c`. So the whole interval between related points lies in the same class.

### Convexity implies congruence

If all classes are convex, distinct classes of a chain are totally ordered and disjoint intervals. Therefore the class containing `min(x,y)` depends only on the two input classes and is their lower class; similarly `max` lands in their upper class. Hence both lattice operations descend.

Thus

\[
\boxed{
\operatorname{Con}(C,\min,\max)
=
\{\text{convex interval partitions of }C\}.
}
\]

For `C=N_0`, P008 complete-growth quotients are precisely the subclass of these chain-lattice congruences whose consecutive classes are the finite basins

\[
[V(k),V(k+1)-1]
\]

with quotient order type `N_0`.

This is a mature lattice-theoretic fact, not an Enterprise Math novelty claim. Its project role is more important than its abstract novelty: **the P008 basin geometry is now generated/characterized by an operation algebra, not merely posited as an interval convention.**

## 8. A2-OQD-C02 — operation language determines geometry class before it determines scale

T01 and T05 together give the correct reverse interpretation.

The order language

\[
\mathcal L_{\mathrm{ord}}=\{\min,\max\}
\]

does not select one `V`. Instead it selects the admissible quotient geometry:

\[
\boxed{
\{\min,\max\}
\Longrightarrow
\text{convex/interval quotient classes}.
}
\]

Now add a fixed external translation `+t`. Under the Stage-3 P008 safe-translation hypotheses, a persistent positive safe translation forces the basin boundary/width pattern into periodic transport. Thus

\[
\boxed{
\{\min,\max,+t\}
\Longrightarrow
\text{periodically transported interval geometry}
}
\]

within the complete-growth regime, but the period-capacity `t` still need not determine the primitive width word.

By contrast, if the language contains ordinary internal binary addition, its elementary translations contain every map

\[
x\mapsto x+a,
\]

including `+1`. Stage 4 then forces every basin to be a singleton:

\[
\boxed{
\{\min,\max,+\}
\Longrightarrow
\text{identity quotient}.
}
\]

The same elementary-translation viewpoint explains multiplication: internal binary multiplication supplies all scalar maps `x->ax`, and Stage 4 proves that an unbounded P008 quotient with any non-singleton basin is separated by some scalar.

So the language hierarchy is not merely syntactic. Different operation signatures generate different admissible quotient geometries.

## 9. A2-OQD-T06 — the fixed-block gcd theorem is the closed-form reverse closure for a restricted language

Take the current fixed-block observation

\[
q_d(n)=\left\lfloor\frac nd\right\rfloor
\]

and declare only external additive generators

\[
U=\{u_1,\ldots,u_r\}.
\]

Stage 3 proves that the coarsest exact future-safe refinement is

\[
q_g,
\qquad
\boxed{g=\gcd(d,u_1,\ldots,u_r)}.
\]

In the present language, this says

\[
\boxed{
\Theta_{\langle+U\rangle,q_d}
=\ker q_g.
}
\]

Thus the gcd is not an independently postulated precision law. It is the closed-form value of the general operation+observation congruence closure inside the scalar fixed-block family.

This also marks its boundary: a general causal quotient need not possess a single scalar `d` at all.

## 10. A2-OQD-C03 — forward and reverse directions now close

The causal algebra can now be written as two coupled maps.

### Reverse / quotient selection

A required total-operation language determines a congruence lattice:

\[
\boxed{
\mathcal A_{\rm req}
\longmapsto
\operatorname{Con}(X,\mathcal A_{\rm req}).
}
\]

The current observation/context selects the maximal safe forgetting relation below what is already observable:

\[
\boxed{
(\mathcal A_{\rm req},O)
\longmapsto
\Theta_{\mathcal A_{\rm req},O}
=
\max\bigl(
\operatorname{Con}(X,\mathcal A_{\rm req})
\cap\downarrow\ker O
\bigr).
}
\]

### Forward / surviving-operation audit

Once a quotient `theta` is fixed, any wider candidate ambient language `B` can be audited by

\[
\boxed{
\theta
\longmapsto
\operatorname{Spec}_{\mathcal B}(\theta)
=
\mathcal B\cap\operatorname{Pol}(\theta).
}
\]

If `B=A_req`, every required operation survives by construction. If `B` is larger, the spectrum reports which additional operations survive for free.

This gives the closed loop

\[
\boxed{
\text{operation requirements}
\to
\text{admissible quotient geometry}
\to
\text{observation-selected natural quotient}
\to
\text{surviving operation spectrum}.
}
\]

A scalar natural scale appears only when the selected quotient family admits a faithful scalar coordinate, as in fixed blocks. The quotient is primary; scale is a representation when available.

## 11. Partial-operation boundary

T01 uses total operations. For a partial operation, a compatibility notion that preserves enabledness must require

\[
x\mathrel\theta y
\Longrightarrow
(x\in D\iff y\in D)
\]

in addition to target compatibility on the enabled domain. The universal relation then fails whenever enabled and disabled states coexist.

Therefore the FQ-006 legality-sensitive extension changes the admissible congruence geometry itself. It should be treated as a genuine extension of the total-operation duality, not collapsed into the total theory.

Equality remains compatible, so partial operations may reduce—but need not automatically eliminate—all quotient-selection ambiguity.

## 12. Prior-art boundary

The following generic statements are classical and are not novelty claims:

- congruence lattices of universal algebras;
- elementary/fundamental unary translations and congruence testing;
- largest operation-compatible indistinguishability below an observation/context relation;
- congruences of chains/lattices and convex blocks;
- finite partition refinement / future distinguishability.

Enterprise Math's research claim under pressure test is the bridge joining these facts to the existing P008/P018/P023/P024 complete-growth system:

1. `min/max` characterize the interval geometry already used by P008;
2. Stage-3 translation rigidity further restricts that geometry to periodic transport when a positive fixed step survives;
3. ordinary arithmetic collapses the admissible geometry to equality;
4. fixed-block gcd refinement is the scalar closed form of the general observation-congruence closure;
5. scalar precision is therefore secondary to the selected causal quotient and its surviving operation algebra.

## 13. Executable evidence

`operation_quotient_duality.py` compiles finite finitary operations to elementary unary translations and delegates refinement to canonical P023.

Current regressions check:

- direct finitary congruence testing agrees with the elementary-translation compiler over all partitions of a three-state set for several binary algebras;
- all elementary coordinate contexts are actually generated;
- `min/max` leave convex interval observations unchanged;
- `min` detects a nonconvex observation and forces refinement;
- equality and universal relations are both congruences for total operation families;
- the exact P008 `min/max` identities hold on irregular, square and cubic basin samples.

These tests are executable witnesses for the bridge; the theorems above are structural proofs.
