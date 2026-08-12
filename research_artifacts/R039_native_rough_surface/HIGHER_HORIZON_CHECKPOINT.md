# R039 — Higher-Horizon Surface Precision and Finite Surface Alphabet

Status: `SEMANTIC_CHECKPOINT_EXTENSION / L2.1 RESEARCH / NOT CANONICAL`  
Researcher-ID: `EM-R039-9F3C27`  
Parent checkpoint: `ddfa2dba2d57a97b466b8b1bfcb8471ca7626106`  
Task: `RS-R039-NATIVE-ROUGH-SURFACE-ALGEBRA-COLLAPSE-CALCULUS`  
CI: `CI_NOT_REQUIRED_FOR_RESEARCH`

## 0. Extension verdict

The first R039 checkpoint established

```text
full native incidence -> local surface types -> H -> S
```

and a second-order frontier residual `R2` sufficient for exact two-addition terminal-`S`
futures.

This extension sharpens that result in four directions:

1. the local 12-slot surface alphabets are finite and exactly enumerable under the
   declared lattice symmetry actions;
2. the previously stored `b_x` coordinate of `R2` is algebraically redundant;
3. the reduced second-order residual is not recursively Markov and, in FCC, provably
   loses scalar terminal-surface information by horizon four;
4. the right finite-horizon object is an operational exterior-incidence cone, not a
   scalar "roughness" coordinate.

A separate prior-art bridge then identifies the asymptotic FCC edge-isoperimetric
shape as the FCC contact zonotope. That is a *post-native asymptotic readout* of the
same contact relation, not a reintroduction of native radius or sphere semantics.

---

## 1. Exact finite local surface alphabet

For a boundary cell `u`, the raw occupied-neighbor mask is a subset of its 12 native
contact slots. There are `2^12=4096` raw masks before quotienting local symmetry.

### R039-T5 — FCC mask orbit polynomial

The 48 signed coordinate permutations act on the 12 FCC contact slots. Their cycle
types are

```text
1^12                 multiplicity 1
1^4 2^4              multiplicity 3
2^6                  multiplicity 4
3^4                  multiplicity 8
6^2                  multiplicity 8
4^3                  multiplicity 12
1^2 2^5              multiplicity 12
```

Hence Burnside/Pólya gives

\[
A_{FCC}(z)=
1+z+4z^2+9z^3+18z^4+24z^5+30z^6
+24z^7+18z^8+9z^9+4z^{10}+z^{11}+z^{12}.
\]

The coefficient of `z^d` is the number of occupied-slot mask orbits of local degree
`d`.

Therefore:

```text
FCC degree d:       0  1  2  3  4  5  6  7  8  9 10 11 12
FCC mask orbits:    1  1  4  9 18 24 30 24 18  9  4  1  1
total: 144
surface-only (d<12): 143
```

### R039-T6 — HCP mask orbit polynomial under the frozen action

For an A-centered HCP cell, the phase-preserving site action induced by the frozen
24-coset implementation has order 12. Its slot cycle types are

```text
1^12                 multiplicity 1
1^6 2^3              multiplicity 1
1^2 2^5              multiplicity 3
2^6                  multiplicity 3
3^4                  multiplicity 2
3^2 6                multiplicity 2
```

Thus

\[
A_{HCP}(z)=
1+2z+10z^2+25z^3+54z^4+78z^5+96z^6
+78z^7+54z^8+25z^9+10z^{10}+2z^{11}+z^{12}.
\]

So, relative to the currently frozen HCP symmetry implementation:

```text
HCP degree d:       0  1  2  3  4  5  6  7  8  9 10 11 12
HCP mask orbits:    1  2 10 25 54 78 96 78 54 25 10  2  1
total: 436
surface-only (d<12): 435
```

The existing crystallographic caveat remains unchanged: before L4, independently
audit that the frozen HCP cosets implement the intended full `P6_3/mmc` equivalence.

### Consequences

- Local rough-surface composition is a finite exact alphabet.
- FCC and HCP differ already at local degree `1`: one FCC orbit versus two HCP
  orbits, matching the basal/interlayer distinction seen at `N=2`.
- The coefficient sequences are palindromic because mask complementation commutes
  with the slot permutation action.
- Every degree-`d` mask orbit is realized by the connected cluster consisting of the
  center plus the selected `d` neighbors. Hence every exposed surface type (`d<=11`)
  is realized by some connected cluster of size at most `12`; the full interior mask
  occurs by size `13`.

The alphabet is finite, but a multiset of alphabet letters is still not a
future-safe state: the first checkpoint's `N=4` counterexamples already show loss of
spatial correlation.

---

## 2. `R2` can be compressed exactly

The first checkpoint stored, for each frontier candidate `x`,

\[
P_C(x)=(k_x,A_x,b_x),
\]

where `k_x` is the number of occupied neighbors, `A_x(j)` counts current frontier
neighbors of `x` in attachment bin `j`, and `b_x` counts neighbors of `x` outside
`C union F(C)`.

### R039-T7 — `b_x` is redundant

Because the contact graph is 12-regular, the 12 neighbors of `x` partition into:

1. occupied neighbors: `k_x`;
2. other current frontier neighbors: `sum_j A_x(j)`;
3. not-yet-frontier neighbors: `b_x`.

Therefore

\[
\boxed{
b_x=12-k_x-\sum_j A_x(j).
}
\]

Define the reduced record

\[
\bar P_C(x)=(k_x,A_x)
\]

and

\[
\bar R_2(C)=\{\bar P_C(x):x\in F(C)\}_{multi}.
\]

The exact successor histogram update becomes

\[
\boxed{
H'=
H-e_{k_x}-A_x+\operatorname{shift}_{+1}(A_x)
+\left(12-k_x-\sum_j A_x(j)\right)e_1.
}
\]

Thus `b_x` carries zero additional information in this 12-regular language.
`\bar R_2` preserves exactly the same declared two-step terminal-`S` future as the
old `R2`, with strictly fewer stored coordinates.

This is an exact precision reduction, not an approximation.

---

## 3. Higher-horizon failure of the second-order residual

A finite-horizon sufficient state need not be recursively sufficient at the next
horizon.

### R039-CE5 — same `R2`, different successor-`R2` futures at `N=6`

Exact exhaustive search shows:

```text
FCC:
  no R2 collisions among symmetry classes for N<=5
  first collisions at N=6
  collision-group sizes: 2, 3, 2

HCP:
  no R2 collisions among symmetry classes for N<=5
  first collisions at N=6
  four collision groups, each of size 2
```

Within those `N=6` collision classes, the set of possible successor `R2` states is
not equal between all members. Equivalently, the current `R2` state is not a Markov
state for iterating the same second-order description.

The first information debt is therefore a correlation among frontier candidates:
`R2` stores each candidate's local environment as a bag, but not the full
candidate-to-candidate incidence structure needed to update that bag after a choice.

### R039-CE6 — same `R2`, different four-step terminal `S` in FCC

The following two FCC clusters have

```text
N=6
S=62
H=((1,24),(2,10),(3,6))
same reduced R2
```

but unequal exact terminal surface support after exactly four additions:

```text
C=((0,0,0),(0,0,2),(0,1,-1),(1,-1,4),(1,0,1),(1,0,3))

D=((0,0,0),(0,0,2),(0,1,-1),(0,1,1),(1,0,3),(1,1,-2))
```

Exact four-addition supports:

```text
C: {82,84,86,88,90,92,94,96,98,100,102}
D: {80,82,84,86,88,90,92,94,96,98,100,102}
```

So the second-order collapse, though exact for the originally declared two-step
terminal-`S` language, is definitely unsafe by horizon four.

A concrete `D` attachment set reaching `S=80` is

```text
{(1,0,1),(1,1,0),(1,0,-1),(1,1,2)}
```

with legal order

```text
(1,0,1)
(1,1,0)
(1,0,-1)
(1,1,2)
```

and total new contact count `15`.

For `C`, exact exhaustive four-cell attachment enumeration gives maximum total new
contact count `14`, hence minimum terminal surface `82`.

No claim is made here that horizon four is the globally minimal scalar-`S` failure
of `R2` over every possible cluster size; the witness is a rigorous kill test.

---

## 4. Order-free finite-horizon surface optimization

Let `A` be a finite set of newly occupied cells, disjoint from connected `C`.
Write:

- `E(C,A)` for native contacts between `C` and `A`;
- `E(A)` for native contacts internal to `A`.

### R039-T8 — terminal surface depends only on the final added set

From the 12-regular handshake,

\[
\boxed{
S(C\cup A)-S(C)
=
12|A|-2\bigl(E(C,A)+E(A)\bigr).
}
\]

Thus, for a fixed final set `A`, terminal `S` is independent of the order in which
its cells were legally added.

Moreover, a size-`h` set `A` is realizable by some frontier-addition order exactly
when `C union A` is connected: repeatedly choose a vertex of `A` adjacent to the
already built connected component.

Define the exact native contact-closure potential

\[
\Lambda_h(C)=
\max_{\substack{
A\cap C=\varnothing,\ |A|=h\\
C\cup A\ \mathrm{connected}
}}
\left(E(C,A)+E(A)\right).
\]

Then the best terminal surface after exactly `h` additions is

\[
\boxed{
S_{\downarrow,h}(C)
=
S(C)+12h-2\Lambda_h(C).
}
\]

### R039-T9 — Bellman recursion

\[
\boxed{
\Lambda_0(C)=0,
\qquad
\Lambda_h(C)=
\max_{x\in F(C)}
\left[
k_C(x)+\Lambda_{h-1}(C\cup\{x\})
\right].
}
\]

This isolates the exact reason one-step greedy can fail: maximizing immediate `k`
is only the first term of a horizon-dependent Bellman value.

The earlier collapse counterexamples can now be restated as precision debts for
`\Lambda_h`:

```text
scalar S does not preserve Lambda_1      (CE1, N=3)
frontier histogram H does not preserve the two-step terminal language (CE2, N=4)
reduced R2 does not preserve Lambda_4    (CE6, FCC N=6)
```

For CE6 specifically:

```text
Lambda_4(C)=14
Lambda_4(D)=15.
```

---

## 5. A finite operational state that is sufficient for arbitrary fixed horizon

The failures above do not imply that exact finite-horizon prediction requires the
entire infinite lattice or the deep cluster interior.

Define exterior candidate layers operationally:

```text
L0(C) = F(C)

L_{r+1}(C) =
  neighbors of L_r(C)
  minus C
  minus L0(C),...,L_r(C).
```

These are *operation-horizon layers*, not a native global radius or root-distance
field.

For fixed horizon `h`, define `J_h(C)` to retain:

1. `S(C)` when absolute terminal `S` is an observable;
2. the induced native contact graph on
   `L0(C) union ... union L_{h-1}(C)`;
3. each candidate's layer tag;
4. initial attachment count `k_C(x)` on `L0` (zero for deeper candidates).

### R039-T10 — finite-horizon exterior-cone sufficiency

Every cell that can be added within at most `h` legal additions lies in
`L0 union ... union L_{h-1}`.

Given a partial chosen set `{x_1,...,x_t}`, the attachment count of another
candidate `x` is

\[
\boxed{
k_t(x)=k_C(x)+
\#\{i\le t:x_i\sim x\}.
}
\]

Therefore the exact legal transition relation and every surface increment

\[
\Delta S=12-2k_t(x)
\]

through horizon `h` can be simulated from `J_h(C)` alone.

So `J_h` is an explicit finite, metric-free, addition-only future-safe state.
Minimality is not claimed.

This gives a constructive hierarchy:

```text
future horizon grows
=> required exterior correlation depth can grow
=> deep interior still remains discardable for addition-only surface futures.
```

The second-order residual is a quotient of the `h=2` exterior-incidence data; CE5
shows that quotienting away candidate correlations creates the next horizon debt.

---

## 6. FCC asymptotic edge-isoperimetric bridge

This section is explicitly **prior-art application + R039 specialization**, not a
claim that Enterprise Math discovered general lattice edge isoperimetry.

Barber & Erde, *Isoperimetry in Integer Lattices*, Discrete Analysis 2018:7,
arXiv:1707.04411, prove that for every Cayley graph on `Z^d`, the minimum edge
boundary is asymptotically governed by the zonotope generated by its Cayley
generators, with

\[
\partial^*(n)
=
\left(d\,\operatorname{vol}(Z)^{1/d}+o(1)\right)
n^{1-1/d}.
\]

Barber, Erde, Keevash & Roberts, *Isoperimetric Stability in Lattices*,
arXiv:2007.14457, further show that near-isoperimetric sets are close to scaled
copies of that zonotope.

### R039-D1 — FCC contact zonotope

Use the FCC Bravais basis

```text
b1=(1,1,0)
b2=(1,0,1)
b3=(0,1,1)
```

whose physical-coordinate determinant has absolute value `2`.

For the six undirected FCC contact directions, the centered zonotope is

\[
Z_{FCC}=\sum_{i=1}^{6}[-v_i,v_i].
\]

The standard 3D zonotope determinant formula gives

\[
\operatorname{vol}_{phys}(Z_{FCC})
=
2^3\sum_{1\le i<j<k\le6}
|\det(v_i,v_j,v_k)|.
\]

Among the 20 triples, 16 have determinant magnitude `2` and 4 are singular, so

\[
\boxed{\operatorname{vol}_{phys}(Z_{FCC})=256.}
\]

Dividing by the FCC lattice covolume `2` gives the lattice-normalized volume

\[
\boxed{\operatorname{vol}_{L}(Z_{FCC})=128.}
\]

The same zonotope has the exact polyhedral description

\[
\boxed{
|x|,|y|,|z|\le4,
\qquad
|x|+|y|+|z|\le6,
}
\]

with 24 vertices given by all coordinate permutations of

```text
(0, ±2, ±4).
```

It is combinatorially/geometrically the usual truncated-octahedral zonotope in
these implementation coordinates.

### R039-D2 — FCC asymptotic native-surface law

Applying Barber-Erde after identifying the FCC Bravais lattice with `Z^3` gives

\[
\boxed{
S_{\min}^{FCC}(N)
=
\left(12\,2^{1/3}+o(1)\right)N^{2/3}.
}
\]

The exact `N<=8` atlas is finite-size evidence only; it is not used to prove this
asymptotic law.

This asymptotic polyhedron is not a native "sphere". It emerges only after asking
the separate optimization question:

```text
among N-cell clusters, minimize the native contact cut.
```

That distinction is important: the same substrate may support different
macroscopic shapes under different future/optimization semantics.

### HCP boundary

The direct Barber-Erde theorem is a Cayley-`Z^d` result. The frozen HCP graph has a
two-site periodic basis rather than the one-site Bravais Cayley presentation used
above. This checkpoint therefore does **not** transfer the FCC constant/zonotope to
HCP by analogy.

A high-value next theorem problem is to derive the HCP periodic-graph cell problem
or find the appropriate periodic-graph edge-isoperimetric theorem, then determine
whether HCP retains or loses stacking memory at the leading `N^(2/3)` surface scale.

---

## 7. Updated collapse hierarchy

The current exact hierarchy is now better written as:

```text
Q0 full native cluster/incidence
  |
  v
J_h finite operational exterior-incidence cone
  |
  | horizon-specific exact quotienting
  v
R2bar = multiset of (k_x, A_x)            [two-step terminal-S SAFE]
  |
  v
H = attachment histogram                  [one-step SAFE; two-step UNSAFE]
  |
  v
S = scalar cut size                       [current-S SAFE; one-step UNSAFE]
```

Key negative lesson:

> A representation can be exact for a declared horizon without being closed under
> its own successor update.

Key positive lesson:

> Future-relative precision is not "keep the whole world". For fixed addition
> horizon, a finite exterior incidence cone is sufficient and the deep interior can
> be collapsed away.

---

## 8. Verification status and next action

New exact checks in `verify_higher_horizon.py` cover:

- FCC and HCP 12-slot orbit counts;
- Burnside coefficient reconstruction;
- exact `b_x` redundancy;
- the FCC same-`R2` witness;
- exact four-addition support split `{82,...}` versus `{80,82,...}`;
- `Lambda_4=14` versus `15`;
- FCC zonotope determinant volume `256` and lattice-normalized volume `128`.

The prior exhaustive `N<=8` atlas remains frozen and is not recomputed here.

### Next action

Priority order:

1. build the minimal practical `R3`/incidence quotient between `R2bar` and full
   `J_h`, with kill tests for horizon 3/4;
2. derive or source the correct two-site periodic edge-isoperimetric/Wulff theorem
   for HCP and compute its exact leading surface shape/constant;
3. only then spend substantial compute on `N=9,10` exhaustive/branch-and-bound
   extension, unless those sizes become necessary to kill a theorem candidate.
