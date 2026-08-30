# ADDMUL Bridge Integration — Strength / Information-Cost / Composability Atlas

Researcher-ID: `EM-AMINT-8E3C72`  
Task: `RS-ADDMUL-BRIDGE-INTEGRATION-STRENGTH-COST-ATLAS`  
Publication: `TP2-970ED4BA261B4270FCB6`  
Execution record: `ER-CDED03A1489613EE6B8C`

## 1. Terminal verdict

`SUCCESS / FINITE_SET_OF_INCOMPARABLE_BRIDGE_CLASSES_CLASSIFIED / OPERATION_SAFE_COMPOSITION_REQUIRES_EXPLICIT_DYNAMIC_STATE_AND_COST_LOWER_BOUND`

Hard target disposition:

`ADDMUL_BRIDGE_STRENGTH_INFORMATION_COST_COMPOSABILITY_ATLAS_CLASSIFIED`.

The six accepted positive routes do not collapse to one mathematical mechanism. The exact integration result is:

1. **A1/A3/A4 form an exact algebraic composition cluster.** A1 reconstructs product from addition plus one normalized quadratic observable; this evaluates the A3 law exactly over `Z`; and both A1 and A3 apply componentwise on A4's declared integral ghost image because that image is a subring.
2. **A2 is a prime-indexed defect extension of that cluster, not a separate global exact kernel.** At `p=2`, A2 is literally A1 with sign reversed: `delta_2=-Q_2`. For odd `p`, the anti-diagonal `x+y=0` is an unavoidable infinite lost-product fiber, so integration with an exact product-using route requires an explicit exceptional branch or additional state.
3. **A5 is genuinely different.** Its multiplication coordinate is exact, but exact addition through a compressed valuation state requires normalized unit/residue information whose required depth is unbounded. No fixed residue budget can be a global operation-safe replacement for dynamic refinement.
4. **A6 is an orthogonal spectral coordinate class.** Zero completion makes the Gauss transition exactly invertible, but this information-theoretic invertibility does not become a natural convolution-algebra intertwiner. Generic pullback/Fourier expansion of another route is therefore not counted as an exact bridge-law composition.

Accordingly there is a common **audit/state grammar**, but there is no nontrivial fixed finite **common bridge state** for all A1–A6 unless one pays the degenerate cost of retaining the full source plus route-specific operation metadata. This is the precise first-wave incomparability result.

No Working Truth, Foundation status, L4 status, canonical theorem promotion, or global-tool promotion is claimed.

---

## 2. Frozen inputs and reuse gate

This integration uses only the Driver-accepted A1–A7 returns and the frozen `BRIDGE_AUDIT_PACKET_V1`.

Existing mechanisms are reused rather than renamed:

- finite differences / cross-effects: existing mixed-difference and A1 calculus;
- integer precision/refinement: `src/enterprise_math/precision.py`;
- defect transport / staged-direct coherence: existing precision-holonomy family;
- operation-safe fibers/quotients: existing operation quotient machinery;
- valuation generation-versus-transport semantics: accepted A5 result.

No new generic precision, quotient, valuation, holonomy, or finite-difference engine is introduced.

Method harvest: `RESULT_ONLY`.

---

## 3. Common signature

The A7 packet is extended only by one required cost axis, `PRECISION_REFINEMENT`. The resulting task-local signature is:

`OPERATION_SAFE_BRIDGE_STATE_GRAMMAR_V1`

with fields

- route/mechanism class;
- A7 strength ceiling;
- domain and codomain;
- source-addition transport status;
- source-multiplication transport status;
- injectivity/fiber/kernel certificate;
- closure;
- exceptional locus;
- hidden coordinates;
- partiality;
- error;
- reconstruction rule;
- precision/refinement state;
- cost vector `DOMAIN / COLLISION / HIDDEN_COORDINATE / PARTIALITY / ERROR / PRECISION_REFINEMENT`.

This is an **audit grammar**, not a common target algebra. That distinction is essential: the same grammar can describe bridges that are algebraically incomparable.

### A1 — binomial cross-effect

Mechanism: `EXACT_DEFECT_RECONSTRUCTION`.

On `Z`,

\[
Q_2(x+y)-Q_2(x)-Q_2(y)=xy.
\]

Addition is native and multiplication is exactly reconstructed. The normalized unary quadratic observable `Q_2` is one fixed hidden coordinate; A1 itself proves uniqueness up to an additive linear term, and the normalization `q(1)=0` singles out `Q_2`.

Cost:
- `DOMAIN=0`;
- `COLLISION=0` when the integer carrier is retained;
- `HIDDEN_COORDINATE=ONE_UNARY_Q2`;
- `PARTIALITY=0`;
- `ERROR=0`;
- `PRECISION_REFINEMENT=top-arity graded reuse; filtered correction below top arity`.

### A2 — delta / Frobenius defect

Mechanism: `PRIME_INDEXED_DEFECT_RECONSTRUCTION_WITH_SINGULAR_FIBER`.

At `p=2`,

\[
\delta_2(n)=\frac{n-n^2}{2}=-Q_2(n),\qquad D_2(x,y)=-xy.
\]

For odd `p`, `(s=x+y,D_p)` determines `xy` uniquely on the semantic image when `s!=0`, while

\[
D_p(a,-a)=0
\]

for every integer `a`, so the anti-diagonal has an infinite product-loss fiber.

Cost:
- domain/exact-branch cost at `s=0`;
- infinite collision there unless the product/equivalent branch state is retained;
- exact semantic-image/root gate for odd `p`;
- unit-ratio residue needed for its refined equal-valuation footprint;
- zero approximation error.

### A3 — formal-group interpolation

Mechanism: `EXACT_LAW_REPARAMETRIZATION`.

\[
F_c(x,y)=x+y+cxy,\qquad T_c(x)=1+cx,
\]

and

\[
T_c(F_c(x,y))=T_c(x)T_c(y).
\]

Fibers are exactly `Ann_R(c)`. The monoid law is global, while inversion is restricted to `1+cx` units. Finite formal jets are exactly associative only in the declared nilpotent cell; naive ordinary-polynomial truncation is not operation safe.

Cost:
- parameter/image-domain typing;
- collision `Ann(c)` when `c` is a zero divisor;
- inverse-locus partiality;
- depth-dependent primorial or nilpotent-cell precision condition;
- zero approximation error.

### A4 — Witt / ghost packet

Mechanism: `EXACT_HIDDEN_COORDINATE_IMAGE_BRIDGE`.

For finite divisor-closed `S`, the ghost map is triangular and injective over `Z`; its image is a subring of `Z^S`, and Witt addition/multiplication become componentwise `+/*` there. Arbitrary integer ghost packets are invalid; exact restriction requires divisor-closedness.

Cost:
- finite divisor-closed index domain;
- zero collision on the valid image;
- hidden state scaling with `|S|`;
- integral-image and locality gate;
- irreducible composite coordinates;
- zero approximation error.

### A5 — valuation / tropical collapse

Mechanism: `LOSSY_INVARIANT_WITH_DYNAMIC_CANCELLATION_REFINEMENT`.

Multiplication is exact:

\[
V(xy)=V(x)+V(y).
\]

Addition is

\[
V(x+y)=\min(V(x),V(y))+K(x,y),
\]

and `K` is not determined by a finite valuation window.

Cost:
- finite-window collision and missing sign/cofactor;
- normalized unit/residue hidden state;
- exact-zero/infinity typing;
- dynamic residue-depth refinement;
- zero numerical error if refinement is performed.

The decisive lower bound is

\[
v_p(1)=v_p(p^k-1)=0,\qquad
\kappa_p(1,p^k-1)=k.
\tag{A5-LB}
\]

Thus exact cancellation depth is unbounded at one fixed input valuation state.

### A6 — Gauss / Jacobi spectrum

Mechanism: `INVERTIBLE_TYPED_LINEAR_SPECTRAL_BRIDGE_WITH_OPERATION_OBSTRUCTION`.

After adding the zero atom, the Gauss transition is full rank. The unit-only image is equivalently the codimension-one hyperplane `sum_t A_t=0`. But the natural transition does not intertwine multiplicative convolution with additive-convolution Fourier multiplication.

Cost:
- one zero type, or equivalently one image constraint;
- no collision after zero completion;
- sparse Jacobi/resonance metadata;
- zero approximation error;
- no precision-refinement cost.

The missing operation intertwiner is **not** a collision cost. This is the first exact proof in the atlas that information injectivity and operation transport are independent axes.

---

## 4. Exact algebraic cluster theorem: A1 / A3 / A4

### Theorem 4.1 — A1 and A2 at `p=2` are the same quadratic core

For every integer `n`,

\[
\delta_2(n)=\frac{n-n^2}{2}=-\frac{n(n-1)}2=-Q_2(n).
\]

Therefore

\[
D_2(x,y)
=-\left(Q_2(x+y)-Q_2(x)-Q_2(y)\right)
=-xy.
\]

So the `p=2` portion of A2 is not merely analogous to A1; it is exactly the same normalized quadratic refinement with the opposite sign.

This is the only `REDUNDANT_ON_DECLARED_DOMAIN` subroute found in the first wave.

### Theorem 4.2 — A1 evaluates A3 exactly over `Z`

Using A1,

\[
F_c(x,y)
=x+y+c\bigl(Q_2(x+y)-Q_2(x)-Q_2(y)\bigr).
\tag{4.2}
\]

Hence addition plus the single A1 observable `Q_2` evaluates every integer-parameter A3 law exactly; no division or approximation is needed.

A3 remains nonredundant because it contributes the exact transformed-law semantics, image `1+cR`, annihilator fibers, inverse locus, and finite formal-jet boundary.

### Theorem 4.3 — A1 composes exactly with A4 on the declared ghost image

Let `G_S(a)=g` and `G_S(b)=h` be valid integral ghost packets. A4 gives

\[
G_S(a\cdot_W b)=g\,h
\]

componentwise. Apply A1 coordinatewise:

\[
Q_2(g_n+h_n)-Q_2(g_n)-Q_2(h_n)=g_nh_n.
\]

Thus A1 reconstructs the exact ghost product using only ghost addition plus one coordinatewise quadratic observable.

The intermediate `Q_2(g_n)` values need not themselves form a ghost packet; they are auxiliary observables. The reconstructed product vector **is** a valid ghost packet because A4's valid image is closed under componentwise multiplication.

### Theorem 4.4 — A3 composes exactly with A4

A4's valid ghost image is a subring of `Z^S`. Hence, for valid `g,h`,

\[
F_c(g,h)=g+h+cgh
\]

is again in the valid ghost image, componentwise. Therefore the A3 law may be applied inside A4 without weakening A4's integral-image predicate or divisor-locality gate.

This answers the special A3/A4 question positively:

> the two routes fit one operation-safe **state grammar** containing `VALID_IMAGE`, `FIBER_KERNEL`, `LAW`, and `LOCALITY_GATE`, but their predicates must remain typed and distinct.

A3's `Ann(c)` is not a substitute for A4's recursive divisibility/Dwork gate, and A4's divisor locality is not a substitute for A3's inverse locus.

---

## 5. Defect generation versus defect transport: A1/A2 compared with A5

A1 and A2 defects are unary coboundaries:

\[
\operatorname{cr}_2 Q_2(x,y)=Q_2(x+y)-Q_2(x)-Q_2(y),
\]

\[
D_p(x,y)=\delta_p(x+y)-\delta_p(x)-\delta_p(y).
\]

Consequently their raw associativity 2-cocycle identity is exact and has zero unprojected holonomy.

A5's `kappa_p`, in contrast, is not a unary additive coboundary on the valuation quotient. It is a **generated correction selected by hidden unit data at a tied-valuation wall**. Multi-step coherence requires the accepted A5 split

\[
E_{\mathrm{parent}}=\tau+\kappa,
\]

where `tau` transports inherited cancellation height and `kappa` generates new cancellation at the current merge.

This yields the common task-local grammar

`DEFECT_STATE = (BASE, GENERATED_DEFECT, TRANSPORTED_DEFECT, DETAIL_BUDGET, OVERFLOW_TYPE)`.

The first three fields are common in spirit across A1/A2/A5 and reuse current holonomy semantics. The fourth is the obstruction to a fixed finite common state.

### Theorem 5.1 — fixed-depth defect-state no-go

Fix a prime `p` and any residue budget `D`. At the identical valuation input state

\[
(v_p(x),v_p(y))=(0,0)
\]

take

\[
x=1,\qquad y=p^k-1.
\]

Then

\[
\kappa_p(x,y)=k.
\]

Choosing `k>=D` exceeds the fixed budget without changing the input valuations.

Equivalently, when normalized units are known only modulo `p^D`, the condition

\[
u+w\equiv0\pmod{p^D}
\]

certifies only `kappa>=D` (or exact cancellation); it does not determine the exact output.

Therefore:

> No fixed finite residue-depth augmentation of the A5 valuation quotient gives globally exact integer addition.

An operation-safe common defect state must either

1. refine dynamically;
2. expose an explicit `DEPTH_AT_LEAST_D / OVERFLOW` branch; or
3. retain enough full-source information that the valuation collapse has ceased to be a compressed bridge.

This is a genuine lower bound on `PRECISION_REFINEMENT`, not a failure of algebraic ingenuity.

### Corollary 5.2 — finite-log data from A2 does not pay A5's cost

A2's equal-valuation finite-log residue detects extra divisibility of `D_p` at the index prime. It is a valuable arithmetic fingerprint, but it is not the normalized-unit state that determines `v_p(x+y)` at arbitrary depth.

Thus A2 and A5 compose only with extra state. Their defects are not interchangeable merely because both are `p`-indexed.

---

## 6. A6 pressure test: invertibility is not operation safety

A6 is the clean counterexample to any atlas that ranks bridges by injectivity alone.

For `F_3`, let `chi_0` be the trivial unit character and `chi_1` the nontrivial character. Under multiplicative convolution on `F_3^×`,

\[
\chi_0 *_\times \chi_1=0
\]

because distinct normalized character idempotents are orthogonal.

At a nonzero additive frequency, however,

- the Fourier column of `chi_0` is `-1`;
- the Fourier column of `chi_1` is a nonzero Gauss sum.

Hence the pointwise product of their additive Fourier columns is nonzero.

So the natural Gauss transition cannot turn multiplicative convolution into additive-convolution Fourier multiplication. Full rank and exact inversion do not change this equation.

This proves:

`ZERO_COLLISION != OPERATION_INTERTWINING`.

The zero atom is nevertheless a clean **cost trade**: one may either

- add `delta_0` and obtain a full `p`-dimensional invertible transform, or
- omit it and restrict the Fourier image to the codimension-one hyperplane
  \[
  \sum_t A_t=0.
  \]

That is a genuine exchange between `HIDDEN_COORDINATE` and `DOMAIN/IMAGE_PREDICATE` cost. It does not create an operation algebra isomorphism.

For this Integration task, generic Fourier expansion or pullback of A1–A5 data is not counted as `COMPOSES_EXACTLY`: any full-state invertible basis can be generically composed with any formula. A composition earns that verdict only when a declared bridge law survives without reconstruct-and-reapply bookkeeping. A6 fails that operation-level test against the algebraic routes.

---

## 7. Pairwise composability matrix

The matrix is symmetric. Each cell below has one of the four required verdicts.

| Pair | Verdict | Exact reason |
|---|---|---|
| A1–A2 | `COMPOSES_EXACTLY` | `p=2` core is literally redundant; odd `p` adds extra defect/valuation observables on the same additive carrier. |
| A1–A3 | `COMPOSES_EXACTLY` | Equation (4.2). |
| A1–A4 | `COMPOSES_EXACTLY` | Coordinatewise A1 cross-effect reconstructs valid ghost multiplication. |
| A1–A5 | `COMPOSES_WITH_EXTRA_STATE` | A5 tied addition still needs dynamically refined unit/residue state. |
| A1–A6 | `INCOMPATIBLE_OR_NOT_NATURAL` | Generic spectral expansion does not cure A6's operation non-intertwining. |
| A2–A3 | `COMPOSES_WITH_EXTRA_STATE` | `p=2` exact; odd `p` needs a lost-product/equivalent branch on `s=0`. |
| A2–A4 | `COMPOSES_WITH_EXTRA_STATE` | `p=2` works coordinatewise; odd-prime singular branches remain and A4 image/locality gates are independent. |
| A2–A5 | `COMPOSES_WITH_EXTRA_STATE` | Finite-log footprint does not replace normalized-unit residue/dynamic cancellation depth. |
| A2–A6 | `INCOMPATIBLE_OR_NOT_NATURAL` | Integer semantic-image inversion and A6's natural convolution semantics do not form one preserved bridge law. |
| A3–A4 | `COMPOSES_EXACTLY` | A4 valid image is a subring, so componentwise `F_c` stays valid. |
| A3–A5 | `COMPOSES_WITH_EXTRA_STATE` | Valuation of `x+y+cxy` needs unit-residue cancellation data among three terms. |
| A3–A6 | `INCOMPATIBLE_OR_NOT_NATURAL` | Pullback along `T_c` is a generic coordinate pullback; A6's operation obstruction remains. |
| A4–A5 | `COMPOSES_WITH_EXTRA_STATE` | Ghost validity/composite locality and valuation unit residues are independent costs. |
| A4–A6 | `INCOMPATIBLE_OR_NOT_NATURAL` | Mod-`p` reduction loses `a_p` whenever `p` is a retained index; keeping an integer/p-adic lift leaves the frozen A6 interface and still gives no natural intertwiner. |
| A5–A6 | `INCOMPATIBLE_OR_NOT_NATURAL` | Finite-field spectral invertibility supplies no canonical valuation unit/cancellation refinement. |

No full-route pair is classified `REDUNDANT_ON_DECLARED_DOMAIN`; the only exact redundancy is the explicitly frozen A1 = A2(`p=2`) core.

---

## 8. Minimal information-cost atlas

The six cost coordinates are deliberately **not summed into one scalar**. They are only partially ordered.

### 8.1 Exact exchangeable costs

Three clean trades are proved.

#### A6: zero atom versus image constraint

`delta_0` may be stored as one extra type, or omitted while restricting to the exact hyperplane `sum_t A_t=0`.

So

\[
\text{HIDDEN\_COORDINATE} \leftrightarrow \text{DOMAIN/IMAGE\_PREDICATE}
\]

is exact here.

#### A3: annihilator collision versus parameter-domain restriction

For zero-divisor `c`, fibers are `Ann(c)`. Restricting to regular/unit `c` removes collision at the price of a domain restriction.

#### A2: anti-diagonal domain cost versus exact branch state

For odd `p`, excluding `s=0` removes the infinite lost-product fiber. Alternatively, retaining `q=xy` (or an equivalent exact coordinate) on that branch converts domain loss into hidden-coordinate cost.

### 8.2 Nonexchangeable costs

#### A4 composite state cannot be replaced by prime-only refinement

Take `S={1,2,3,6}` and compare two Witt states differing only by `a_6=1`. Every prime-power ghost readout is unchanged, while `g_6` changes by `6`.

Thus the mixed-composite coordinate is not a finite precision refinement of separate prime-power views; it is an independent hidden-coordinate requirement.

#### A5 dynamic depth cannot be replaced by any fixed residue depth

This is Theorem 5.1.

#### A6 information injectivity cannot pay operation-law cost

The `F_3` idempotent/Gauss witness proves that zero collision and full rank do not imply a convolution intertwiner.

### 8.3 Error coordinate

All accepted A1–A6 routes in this Integration are exact at their declared scope.

Therefore

\[
\boxed{\text{ERROR}=0\quad\text{for every A1--A6 signature}.}
\]

Approximation is not the reason the routes are incomparable. Domain, information, hidden state, partiality, and refinement are.

---

## 9. Minimal common bridge kernel theorem

There are two different meanings of "common kernel", and they must not be conflated.

### 9.1 Positive: a common exact algebraic kernel exists for A1/A3/A4 and A2 at `p=2`

On `Z`, take native addition plus the normalized unary quadratic observable `Q_2`.

Then:

1. A1 multiplication is recovered by `cr_2 Q_2`;
2. A2 at `p=2` is the same observable with sign reversed;
3. every A3 law `F_c` is evaluated by equation (4.2);
4. on an A4 valid ghost packet, the same construction applies coordinatewise.

So the first-wave exact algebraic routes share a small kernel:

`ADDITIVE_CARRIER + NORMALIZED_QUADRATIC_REFINEMENT + TYPED_IMAGE_GATE_WHERE_REQUIRED`.

A4 still requires its own ghost coordinates and image/locality certificate; the kernel does not erase that cost.

### 9.2 Negative: no nontrivial fixed finite common state exists across A1–A6

A candidate common state that preserves all accepted strengths has to satisfy simultaneously:

- A5 exact addition at arbitrary cancellation depth;
- A4 composite-index information;
- A6 exact typed spectral inversion and its explicit non-intertwining boundary.

A fixed finite residue-depth state fails A5 by (A5-LB). Prime-only hidden refinement fails A4 by the `a_6` witness. Even a collision-free linear completion fails to turn A6 into an operation homomorphism by the `F_3` witness.

The only universal escape is to retain the full source together with all route-specific metadata and reconstruct/reapply every operation. That is a trivial embedding, not a bridge compression or a common mechanism.

Therefore the exact first-wave conclusion is:

\[
\boxed{
\text{COMMON AUDIT GRAMMAR EXISTS;}\quad
\text{NONTRIVIAL FIXED FINITE COMMON BRIDGE STATE DOES NOT.}
}
\]

The surviving bridge classes are:

1. `EXACT_ALGEBRAIC_CLUSTER = {A1,A3,A4}` with A2(`p=2`) overlapping;
2. `PRIME_DEFECT_EXTENSION = {A2 odd p}`;
3. `DYNAMIC_LOSSY_REFINEMENT = {A5}`;
4. `SPECTRAL_LINEAR_COORDINATE = {A6}`.

This is a finite incomparability classification, not a claim that no future route can connect the classes.

---

## 10. Exact checker and certificate

Checker:

`research_checks/ADDMUL_BRIDGE_INTEGRATION_STRENGTH_COST_ATLAS_CHECK_20260830.py`

Atlas:

`research_artifacts/ADDMUL_BRIDGE_INTEGRATION_STRENGTH_COST_ATLAS/atlas.json`

The deterministic checker uses standard-library exact arithmetic only and freezes the following witnesses:

- A1/A2 `p=2` identity;
- A1 -> A3 exact law construction and shifted transport;
- A2 odd-prime anti-diagonal infinite product-loss fiber;
- A3 `Ann(c)` fiber witness on `Z/8Z`;
- A4 invalid ghost image and irreducible composite-index witness;
- A1/A3 exact composition on small valid A4 ghost packets;
- A5 arbitrary cancellation-depth and fixed-depth overflow witnesses;
- A4-to-finite-field mod-`p` information-loss witness at index `p`;
- A6 exact `F_3` non-intertwining witness;
- A6 zero-atom / hyperplane cost trade.

Deterministic run:

`PASS / 22870 exact checks`.

The finite regression is a certificate only. The all-domain claims above are supplied by the symbolic arguments and the already-accepted A1–A7 theorems.

---

## 11. Scope firewall

This return does **not** claim:

- that addition and multiplication are the same operation;
- that A1 definability eliminates multiplication from every foundational language;
- that odd-prime A2 globally reconstructs product across `x+y=0`;
- that A3's full carrier is always a group;
- that arbitrary integer ghost packets are valid A4 states;
- that A5 valuation windows determine addition without unit/residue refinement;
- that A6 invertibility is a convolution-algebra isomorphism;
- that the task-local audit grammar is a new global Enterprise tool;
- that the negative common-kernel result excludes future typed/dynamic interfaces outside the frozen cost model.

---

## 12. Next control-plane recommendation

Do **not** open six route-specific continuations.

The Integration task is terminal at its requested scope. A successor is justified only if a concrete downstream objective needs one of these two sharply typed interfaces:

1. `DYNAMIC_DEFECT_STATE` — implement and test a real operation sequence carrying `(generated_defect, transported_defect, residue_budget, overflow)` using existing precision-holonomy machinery; or
2. `ALGEBRAIC_CLUSTER_ADAPTER` — a concrete consumer needing A1/A3 on A4 ghost packets while preserving A4's integral-image and divisor-locality gates.

Do not open a successor merely to rename `OPERATION_SAFE_BRIDGE_STATE_GRAMMAR_V1` as a new generic tool.
