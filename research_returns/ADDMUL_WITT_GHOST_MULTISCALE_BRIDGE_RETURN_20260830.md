# ADDMUL Witt / Ghost Multiscale Bridge — Research Return

- Task: `RS-ADDMUL-WITT-GHOST-MULTISCALE-BRIDGE`
- Publication: `TP2-F876CFF74AF60A88D173`
- Researcher: `EM-AMWITT-6D3A91`
- Claim: `chatgpt-amwitt-20260830-1230-6d3a91`
- Execution branch: `research/addmul-witt-ghost-multiscale-bridge-em-amwitt-6d3a91`
- Execution base: `c8fd304565c858ae43b482bceaf5b47436624acf`
- Frozen taskbook blob: `sha1:4849e15731adea6688ff38dc3beb92504609dce1`
- Existing precision implementation audited: `src/enterprise_math/precision.py@sha1:0f028d00b2126b7a3b13bcfb8db627fc542af195`
- Method inventory audited: `research_method_inventory.json@main`
- Terminal verdict: `SUCCESS`
- Hard target:
  `WITT_GHOST_MULTISCALE_ADD_MUL_BRIDGE_ENTERPRISE_TRANSLATION_CLASSIFIED_OR_OBSTRUCTED`

## Executive result

The finite integer bridge is real, but its reusable content is narrower than “import Witt vectors”.

For a finite divisor-closed index set \(S\subset \mathbb N_{>0}\), define the big-Witt ghost packet

\[
g_n(a)=\sum_{d\mid n}d\,a_d^{\,n/d}\qquad(n\in S).
\]

This finite transform has four exact features that matter to Enterprise Math:

1. **Triangular exactness and a sharp integer-image gate.**  
   The forward map is integer-valued and triangular. The inverse is unique over \(\mathbb Z\) whenever it exists, and existence is decided at each index by one exact divisibility test.

2. **Operation linearization only on the image.**  
   Actual ghost images are closed under componentwise addition and multiplication, so the ghost layer is an exact add/multiply bridge. Arbitrary integer ghost packets are not valid states; the integrality/image gate is indispensable.

3. **Coordinate restriction is operation-local exactly on divisor-closed truncations.**  
   If retained indices are divisor-closed, restriction commutes exactly with the ghost map and the projection defect is zero. If a retained index \(n\) loses one of its divisors, the retained ghost coordinate still depends on the omitted Witt coordinate, so naive coordinate restriction is not a valid local projection. The omitted contribution has an explicit defect formula.

4. **p-typical packets are exact prime-power subinterfaces, but prime-power packets do not recover the full big-Witt packet.**  
   The p-typical chain is precisely the restriction to \(1,p,p^2,\ldots\). Composite indices such as \(6\) carry mixed divisor information invisible to every prime-power chain.

The correct Enterprise translation is therefore a **thin `WITT_LITE_BRIDGE` adapter** over the existing precision/divisibility machinery: retain finite nonlinear ghost packets, the exact image predicate, and divisor-closed restriction. Do **not** create a second scale calculus, a second holonomy formalism, or an infinite-coordinate substrate.

## 1. Frozen finite convention

Let \(S\) be a finite divisor-closed set: whenever \(n\in S\) and \(d\mid n\), then \(d\in S\).

A Witt-coordinate packet is \(a=(a_d)_{d\in S}\in\mathbb Z^S\). Its ghost packet is

\[
G_S(a)=(g_n(a))_{n\in S},\qquad
g_n(a)=\sum_{d\mid n}d\,a_d^{n/d}.
\]

Only finite packets are used in this return.

This convention matches the standard big-Witt ghost polynomial and the standard notion of truncation set. Classical Witt theory is prior art; the result here is the finite, operation-safe Enterprise translation and the exact boundary against existing scale tooling.

## 2. Theorem A — triangular inverse and exact integrality gate

For every \(n\in S\),

\[
g_n
=
n a_n+
\sum_{\substack{d\mid n\\d<n}}d\,a_d^{n/d}.
\]

Therefore, after all \(a_d\) for proper divisors \(d<n\) have been recovered,

\[
a_n=
\frac{
g_n-\sum_{\substack{d\mid n\\d<n}}d\,a_d^{n/d}
}{n}.
\]

### Consequences

- The forward map \(G_S:\mathbb Z^S\to\mathbb Z^S\) is exact.
- It is injective over \(\mathbb Z\): the recursion uniquely recovers every coordinate.
- A ghost packet \(g\in\mathbb Z^S\) is in the image iff every recursive numerator is divisible by \(n\).
- Arbitrary integer ghost packets are therefore **not** legitimate finite Witt states.

### Minimal failure witness

Take \(S=\{1,2\}\), \(g_1=0\), \(g_2=1\). Then

\[
a_1=0,\qquad a_2=\frac{1-0^2}{2}=\frac12.
\]

Thus `ghost integer vector` is strictly larger than `integral Witt ghost image`.

This kills any interface that stores unrestricted integer ghosts without an image predicate.

## 3. Theorem B — closed congruence form of the image gate over \(\mathbb Z\)

For the same finite divisor-closed \(S\), the recursive gate is equivalent to the classical Dwork congruence specialized to the identity Frobenius lift on \(\mathbb Z\):

\[
g_n\equiv g_{n/p}\pmod {p^{v_p(n)}}
\]

for every \(n\in S\) and every prime \(p\mid n\).

The return does not claim this congruence as new mathematics. Its role is to give the finite packet an inexpensive, coordinate-level validity predicate equivalent to the recursive inverse.

The exact checker exhaustively compares the recursive image predicate and this congruence predicate on all \(g\in[-2,2]^N\) for \(S=\{1,\ldots,N\}\), \(1\le N\le6\), with no mismatch.

## 4. Theorem C — divisor-closed restriction iff ghost locality

Let \(R\subseteq S\) be a retained index set, and define the retained-coordinate partial ghost expression

\[
g_n^{R}(a)=
\sum_{\substack{d\mid n\\d\in R}}
d\,a_d^{n/d}
\qquad (n\in R).
\]

### Positive direction

If \(R\) is divisor-closed, then every divisor of every retained \(n\) is retained. Hence

\[
g_n^R(a)=g_n(a)
\quad(n\in R),
\]

and therefore

\[
\operatorname{res}_R\circ G_S
=
G_R\circ \operatorname{res}_R
\]

exactly. The projection defect is zero.

### Converse at the frozen coordinate-restriction semantics

If \(R\) is not divisor-closed, choose \(n\in R\) and \(d\mid n\) with \(d\notin R\). Two full states that agree on all retained coordinates but differ only in \(a_d\) have the same retained Witt packet and different full \(g_n\). Therefore no deterministic recomputation of retained \(g_n\) from retained Witt coordinates can reproduce full ghost restriction.

The exact missing term is

\[
\Delta_n(R,a)
=
g_n(a)-g_n^R(a)
=
\sum_{\substack{d\mid n\\d\notin R}}
d\,a_d^{n/d}.
\]

So:

> **Within ordinary coordinate restriction using the same ghost polynomial, divisor-closedness is exactly the locality criterion.**

This is deliberately narrower than a universal claim about every conceivable quotient or enriched state.

### Minimal nonlocal witness

For \(S=\{1,2,3,6\}\), retain \(R=\{1,3,6\}\). With all coordinates zero except \(a_2=1\),

\[
g_6=2,
\]

while the retained-coordinate partial expression gives \(g_6^R=0\). Dropping divisor \(2\) destroys locality at retained index \(6\).

## 5. Theorem D — p-typical finite chain

Fix a prime \(p\) and coordinates \(a_0,\ldots,a_k\in\mathbb Z\). Define

\[
h_j
=
\sum_{i=0}^{j}p^i a_i^{p^{j-i}}
=
a_0^{p^j}+p a_1^{p^{j-1}}+\cdots+p^j a_j.
\]

Then

\[
a_j=
\frac{
h_j-\sum_{i<j}p^i a_i^{p^{j-i}}
}{p^j}.
\]

Hence the p-typical map is triangular, injective over \(\mathbb Z\), and has an exact stagewise integrality gate.

Over \(\mathbb Z\), the equivalent finite Dwork gate is

\[
h_j\equiv h_{j-1}\pmod{p^j}
\qquad(j\ge1).
\]

The checker validates this equivalence for \(p=2,3,5\) on all four-coordinate ghost packets in \([-2,2]^4\).

The failure witness \(h_0=0,h_1=1\) gives \(a_1=1/p\) for each tested prime.

## 6. Theorem E — p-typical is exactly the prime-power big-Witt subinterface

Take the big-Witt truncation set

\[
S_{p,k}=\{1,p,p^2,\ldots,p^k\}.
\]

Every divisor of \(p^j\) is \(p^i\) for some \(0\le i\le j\). Therefore

\[
g_{p^j}
=
\sum_{i=0}^{j}
p^i a_{p^i}^{p^{j-i}},
\]

which is exactly the p-typical ghost polynomial under the identification

\[
a_i^{(p\text{-typ})}\longleftrightarrow a_{p^i}^{(\text{big})}.
\]

Thus p-typical prefixes are not merely analogous to the big-Witt divisor geometry; they are exact finite prime-power subinterfaces of it.

Their ordinary lower-prefix restriction is automatically exact because the corresponding prime-power index set is divisor-closed.

## 7. Theorem F — prime-power skeleton does not recover composite mixed information

Prime-power chains omit genuine composite coordinates.

Take a finite big-Witt packet containing index \(6\), and compare:

- state \(A\): all Witt coordinates zero;
- state \(B\): all Witt coordinates zero except \(a_6=1\).

For every prime-power index \(q\), the ghost coordinate \(g_q\) is unchanged, because \(6\nmid q\). But

\[
g_6(B)-g_6(A)=6.
\]

Hence the union of all p-typical prime-power readouts is not injective on the full big-Witt state.

This is the exact information-loss boundary:

- p-typical chains give prime-local multiscale data;
- big-Witt composite indices retain mixed divisor interaction that no separate prime-power chain sees.

A `WITT_LITE_BRIDGE` must not silently replace the divisor lattice by independent p-chains if composite interaction is needed downstream.

## 8. Addition and multiplication on the ghost layer

Standard Witt theory equips the coordinate packet with the unique ring operations for which the ghost map is a ring homomorphism. At the finite integer level used here, this can be checked constructively:

1. start from two actual integral Witt packets;
2. compute their ghost packets;
3. add or multiply ghosts coordinatewise;
4. run the exact recursive inverse;
5. the inverse remains integral and reproduces the coordinatewise ghost result.

The checker performs this exact closure test on all pairs of coordinate packets in \(\{-1,0,1\}^4\) for:

- big Witt on \(S=\{1,2,3,4\}\);
- p-typical packets for \(p=2,3,5\).

Low-index big-Witt formulas illustrate what “ghost linearization” means and what it does **not** mean.

For addition \(c=a+_W b\),

\[
c_1=a_1+b_1,
\]

\[
c_2=a_2+b_2-a_1b_1,
\]

\[
c_3=a_3+b_3-a_1^2b_1-a_1b_1^2.
\]

For multiplication \(d=a\cdot_W b\),

\[
d_1=a_1b_1,
\]

\[
d_2=a_1^2b_2+a_2b_1^2+2a_2b_2.
\]

Thus addition and multiplication become coordinatewise only **after** the nonlinear ghost transform and only on its valid image. This is not an algebraic identification of ordinary coordinatewise Witt-state arithmetic with ordinary integer arithmetic.

## 9. Existing Enterprise tooling: reuse versus new payload

The current method inventory already lists:

- `precision.integer_projection_calculus` as canonical executable precision projection/detail/carry machinery;
- `holonomy.precision_defect_transport` as the canonical defect-transport/holonomy/cocycle family.

`src/enterprise_math/precision.py` already contains:

- divisibility-ordered precision factors;
- exact projection/detail/recomposition;
- precision chains;
- divisor enumeration and Möbius shells;
- nonlinear refinement defects.

Therefore the following would be duplicate infrastructure and are rejected:

- a new generic divisor-scale projection engine;
- a new mixed-radix detail layer;
- a new Witt-specific “precision holonomy” formalism;
- a second generic Möbius shell mechanism.

### What is genuinely additional at task scope

The finite Witt packet contributes a different, narrower mechanism:

1. a nonlinear divisor-power transform \(G_S\);
2. a validity predicate `INTEGRAL_GHOST_IMAGE`;
3. coordinatewise add/multiply semantics on that valid ghost image;
4. divisor-closed restriction as the exact locality gate;
5. explicit mixed-composite information absent from independent prime-power chains.

This is not already represented by the linear scale projection/detail machinery.

## 10. Minimal `WITT_LITE_BRIDGE`

A minimal reusable interface is justified, but only as an adapter.

```text
WITT_LITE_PACKET
  truncation_set: finite divisor-closed S
  witt_coords:    a_d in Z, d in S
  ghost_coords:   g_n = sum_{d|n} d*a_d^(n/d)
  image_gate:
      recursive divisibility by n
      or equivalent Dwork congruences over Z
  operations:
      ghost-wise componentwise + and *
      followed by exact integral inverse when Witt coordinates are needed
  restriction:
      only to divisor-closed T subset S for zero-defect coordinate restriction
  p_typical_view:
      exact restriction to {1,p,...,p^k}
  composite_residual:
      retain composite indices when mixed divisor information is required
```

This interface should reuse Enterprise precision/divisibility indexing and existing defect/holonomy tools; it should not become a new ambient state theory.

## 11. Exact checker certificate

Checker:

`research_checks/ADDMUL_WITT_GHOST_MULTISCALE_BRIDGE_CHECK_20260830.py`

Deterministic exact run:

```text
PASS
big_dwork_vectors=19530
big_operation_pairs=6561
checks=156139
defect_cases=81648
prime_power_embedding_cases=243
ptyp_dwork_vectors=1875
ptyp_operation_pairs=19683
```

Coverage includes:

- recursive big-Witt image gate ↔ big Dwork congruences;
- explicit nonintegral ghost witness;
- big-Witt forward/inverse roundtrip;
- coordinatewise ghost addition and multiplication closure;
- divisor-closed restriction exactness;
- arbitrary retained-set defect identity;
- non-divisor-closed locality failure;
- p-typical forward/inverse and Dwork gates for \(p=2,3,5\);
- p-typical operation closure;
- exact big ↔ p-typical prime-power embedding;
- mixed-composite information-loss witness;
- prefix/nonprefix p-typical locality tests.

No floating point is used.

## 12. Prior-art / novelty firewall

The following are classical and are **not** claimed as Enterprise inventions:

- big and p-typical Witt ghost polynomials;
- truncation sets as divisor-closed subsets;
- the Witt ring structure making the ghost map a ring homomorphism;
- Dwork image congruences;
- restriction maps between truncation sets.

Primary classical reference used for verification:

- Lars Hesselholt, *Lecture notes on Witt vectors*, especially the definition of truncation sets and ghost components, Dwork’s lemma, the ring-homomorphism property, and restriction maps.

The research contribution here is the **finite translation boundary**:

- exact operation-safe packet semantics;
- recursive and congruence validity gates made explicit as runtime contracts;
- an iff locality statement for naive coordinate restriction;
- prime-power versus mixed-composite information-loss separation;
- deduplication against current Enterprise precision/holonomy tooling;
- the minimal adapter boundary for `WITT_LITE_BRIDGE`.

No claim of mathematical novelty beyond classical Witt theory is made.

## Hard-target disposition

`SUCCESS`

`FINITE_WITT_GHOST_BRIDGE_CLASSIFIED / DIVISOR_CLOSED_TRUNCATION_IFF_COORDINATE_RESTRICTION_LOCAL / PTYPICAL_IS_EXACT_PRIME_POWER_SUBINTERFACE / PRIME_POWER_SKELETON_LOSES_COMPOSITE_MIXED_COORDINATES / REUSE_EXISTING_PRECISION_AND_HOLONOMY_TOOLING / MINIMAL_WITT_LITE_INTEGRALITY_GATE_JUSTIFIED`

## Unresolved residue

The finite bridge is classified at the packet/interface level. What remains genuinely open is not the ghost algebra itself but whether a downstream Enterprise problem requires the mixed-composite divisor coordinates strongly enough to justify carrying a `WITT_LITE_PACKET` in production rather than generating it only as an analysis adapter.

No successor should be opened merely to derive more classical Witt identities. A successor is justified only by a concrete Enterprise consumer that needs one of:

- mixed-composite divisor interaction not recoverable from prime-power chains;
- exact ghost-image validity as a state invariant;
- divisor-closed multiscale restriction coupled to an existing Enterprise operation.

## Next control-plane recommendation

Driver-review this result at task scope.

If accepted:

1. freeze A4 as `FINITE_WITT_GHOST_BRIDGE_CLASSIFIED`;
2. register `WITT_LITE_BRIDGE` only as a thin finite adapter if a concrete consumer appears;
3. reuse `precision.integer_projection_calculus` and `holonomy.precision_defect_transport`;
4. prohibit unrestricted integer ghost states without `INTEGRAL_GHOST_IMAGE`;
5. prohibit replacing the full divisor lattice by independent p-typical chains when mixed-composite information is material;
6. do not open a generic “Witt holonomy” or “Witt precision” successor.
