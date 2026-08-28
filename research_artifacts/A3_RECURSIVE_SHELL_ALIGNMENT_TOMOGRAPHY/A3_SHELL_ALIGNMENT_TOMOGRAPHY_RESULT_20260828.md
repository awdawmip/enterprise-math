# A3 Recursive Shell Alignment Tomography — Exact Result Package

Task: `RS-A3-RECURSIVE-SHELL-ALIGNMENT-TOMOGRAPHY`  
Researcher: `EM-A3SHELL-19C7D4`  
Status: `EXACT FINITE PACKAGE / COMPOSE_EXISTING_TOOLS / NO FOUNDATION PROMOTION`

## 1. Frozen carrier and operational state model

Let

\[
\Lambda_3=\{x=(x_1,x_2,x_3,x_4)\in\mathbb Z^4:\sum_i x_i=0\},
\qquad
r(x)=\max_i|x_i|.
\]

Define

\[
B_n=\{x\in\Lambda_3:r(x)\le n\},
\qquad
S_n=B_n\setminus B_{n-1}.
\]

For a finite label alphabet \(A\), use the exact finite state space

\[
X_n=A^{B_n}.
\]

Restriction is literal restriction

\[
\rho_{n+1,n}:X_{n+1}\to X_n.
\]

For \(\sigma\in S_4\), let

\[
R_\sigma=\operatorname{sgn}(\sigma)P_\sigma|_{\Lambda_3}.
\]

The active action on a labeled state is the push-forward of labels along the carrier
bijection \(R_\sigma\). A passive `FRAME_ROTATION` uses the same bijection only as
a change of frame and is not identified with an active state change.

For the shell-alignment prototype fix

\[
a_n=(n,-n,0,0)\in S_n,
\]

and let the boundary target \(\beta_n\) be a one-marker shell state with the marker
at \(a_n\).

For \(1\le d\le n\), define the task-local prefix-shell action

\[
D_{n,d}(\sigma)(x)=
\begin{cases}
R_\sigma x,&r(x)\ge n-d+1,\\
x,&r(x)\le n-d.
\end{cases}
\]

This yields the exact semantics:

- `SHELL_SUPPORTED_TWIST`: \(d=1\);
- `LAYER_COUPLED_TWIST`: \(d\ge2\);
- `REVEAL_EXPANSION`: a compatible tower followed by restriction;
- `ACTIVE_EXTENSION`: attach a new shell payload to an existing \(X_n\) state;
- `REGLUE_ALIGN`: the relation of all legal aligners, not an arbitrary solver word.

The prefix action is a task-local domain operator. It is **not** proposed as a new
shared Enterprise tool family.

## 2. H1 — exact A3 shell theorem

### Theorem 2.1 — ball and shell counts

For every \(n\ge0\),

\[
\boxed{
|B_n|
=
\binom{4n+3}{3}-4\binom{2n+2}{3}
=
\frac{16n^3+24n^2+14n+3}{3}.
}
\]

For every \(n\ge1\),

\[
\boxed{|S_n|=|B_n|-|B_{n-1}|=16n^2+2.}
\]

Proof. Put \(y_i=x_i+n\). Then \(0\le y_i\le2n\) and
\(\sum_i y_i=4n\). Inclusion-exclusion for the coefficient of \(t^{4n}\) in

\[
(1+t+\cdots+t^{2n})^4
\]

has only the zero-violation and one-violation terms: two simultaneous
\(y_i\ge2n+1\) would force a negative residual sum. This gives the displayed
formula. Taking the finite difference gives the shell formula.

Exact first radii:

| \(n\) | \(|B_n|\) | \(|S_n|\) |
|---:|---:|---:|
| 0 | 1 | — |
| 1 | 19 | 18 |
| 2 | 85 | 66 |
| 3 | 231 | 146 |

### Theorem 2.2 — exact 24-frame action

The maps \(R_\sigma\) form a faithful \(S_4\)-action on every \(B_n\) and preserve
\(r\). Every \(R_\sigma\) has determinant \(+1\) on the three-dimensional real
span of \(\Lambda_3\).

Proof. The coordinate sum is multiplied by \(\operatorname{sgn}(\sigma)\), so the
sum-zero hyperplane is preserved. Max absolute coordinate is unchanged.
Moreover

\[
R_\sigma R_\tau=R_{\sigma\tau}.
\]

On the standard three-dimensional representation,
\(\det(P_\sigma)=\operatorname{sgn}(\sigma)\); multiplying by the scalar
\(\operatorname{sgn}(\sigma)\) contributes
\(\operatorname{sgn}(\sigma)^3\). Hence

\[
\det(R_\sigma)=\operatorname{sgn}(\sigma)^4=1.
\]

Faithfulness is also replayed by the checker on \(B_1\), where all 24 permutation
images are distinct.

This is an exact carrier-level 24-frame rotation group. It is not by itself a
claim about physical three-space.

## 3. H2 — alignment relation, stabilizer, and all five cases

For a state \(x\in X_n\), define

\[
\mathcal W_{n,d}(x)
=
\{\sigma\in S_4:
\partial_n(D_{n,d}(\sigma)x)=\beta_n\}.
\]

For the pointer target \(\beta_n\),

\[
\boxed{
H=\operatorname{Stab}_{S_4}(a_n)
=\{e,(12)\}
}
\]

for every \(n\ge1\). Its orbit has size \(12\).

If \(\sigma_0\) is one aligner, then all aligners are exactly

\[
\boxed{\mathcal W_{n,d}(x)=H\sigma_0.}
\]

Indeed, \(h\sigma_0\) aligns for every \(h\in H\), and two aligners differ on the
left by an element fixing the target.

This immediately separates the taskbook cases.

### `UNREACHABLE_SHELL`

A one-marker boundary at

\[
c_n=(n,n,-n,-n)
\]

is unreachable from the pointer target. Its orbit has size \(6\), and every point
in that orbit has zero zero-coordinates, whereas the target orbit has exactly two
zero-coordinates. Zero-coordinate count is preserved by signed permutation.

### `UNIQUE_ALIGNMENT`

Use the rigid two-color target with distinct markers at

\[
a_n=(n,-n,0,0),\qquad b_n=(n,0,-n,0).
\]

The first marker has stabilizer \(\{e,(12)\}\), the second
\(\{e,(13)\}\), and their intersection is \(\{e\}\). Every alignable rigid
two-marker shell therefore has exactly one aligner.

### `MULTIPLE_ALIGNMENT_SAME_INTERIOR`

Under `SHELL_SUPPORTED_TWIST` (\(d=1\)), all aligners fix \(B_{n-1}\)
pointwise. Thus every raw interior readout is literally identical.

### `MULTIPLE_ALIGNMENT_STABILIZER_EQUIVALENT`

Under \(d\ge2\), distinct aligners can move the observed interior, but all outputs
form one residual-\(H\) orbit. If the retained observation language is
\(H\)-invariant, the operation-safe quotient collapses this orbit to one exact
aligned-interior value.

### `MULTIPLE_ALIGNMENT_GENUINELY_AMBIGUOUS`

If the retained observation language contains an \(H\)-odd datum, quotienting by
\(H\) is not semantics-preserving. Section 7 gives an exact A2 orientation
witness. In this case the aligned interior must remain set-valued or carry an
orientation/stabilizer tag.

This realizes the taskbook's required distinction between raw relation branching,
observable determinism, and quotient safety.

## 4. H3 — shielding theorem and the minimal coupled semantics

### Theorem 4.1 — exact shell shielding

For every \(n,d,\sigma\),

\[
D_{n,d}(\sigma)|_{B_{n-d}}=\operatorname{id}.
\]

Any word generated entirely by depth-\(\le d\) prefix actions also fixes
\(B_{n-d}\) pointwise, because every generator does.

Consequently:

\[
\boxed{
d=1 \Longrightarrow
\text{outer-shell alignment cannot change the exact }B_{n-1}\text{ interior}.
}
\]

So the literal "align the outer shell, then inspect the interior" recursion is
active-bulk trivial if the legal moves are truly shell-supported.

Within this exact prefix-shell model,

\[
\boxed{d=2}
\]

is the smallest nontrivial coupled depth: it can move \(S_{n-1}\) while still
fixing \(B_{n-2}\).

An explicit \(n=2\) witness is

\[
p=(1,0,-1,0)\in S_1,\qquad
R_{(12)}p=(0,-1,1,0)\ne p,
\]

while the origin remains fixed.

This is the first hard obstruction to a naive Rubik analogy: **nontrivial
tomography requires radial coupling.**

## 5. H4 — choice-independent radial defect

Suppose each shell is alignable and choose one aligner \(g_n\) at radius \(n\).
The actual choice is only the left coset

\[
A_n=Hg_n.
\]

Define the radial defect between adjacent scales by

\[
\boxed{
\Delta_n
=
H g_n g_{n+1}^{-1} H
\in H\backslash S_4/H.
}
\]

### Theorem 5.1 — representative and frame invariance

If \(g_n\mapsto h_ng_n\) and \(g_{n+1}\mapsto h_{n+1}g_{n+1}\) with
\(h_n,h_{n+1}\in H\), then \(g_ng_{n+1}^{-1}\) is changed by left and right
multiplication by \(H\); hence \(\Delta_n\) is unchanged.

Under a common passive frame change \(q\), aligners transform as
\(g_k\mapsto g_kq^{-1}\), so

\[
(g_nq^{-1})(g_{n+1}q^{-1})^{-1}
=
g_ng_{n+1}^{-1}.
\]

Thus \(\Delta_n\) is exactly frame-invariant.

### Theorem 5.2 — scale-square criterion

For the depth-2 prefix model, align-at-\(n+1\)-then-restrict and
restrict-then-align-at-\(n\) induce the same transformation on the strongest
residual-\(H\) quotient for **all** interior states iff

\[
\boxed{\Delta_n=H.}
\]

If \(\Delta_n\ne H\), a rigidly labeled state on \(S_n\) witnesses the failure.
Thus the failure is not a numeric subtraction; it is a typed gauge-comparison
defect.

### Exact double-coset classification

For \(H=\{e,(12)\}\),

\[
|H\backslash S_4/H|=7.
\]

The canonical classes in the certificate are:

| class | representative | size |
|---|---|---:|
| \(C_0\) | \(e\) | 2 |
| \(C_1\) | \((34)\) | 2 |
| \(C_2\) | \((23)\) | 4 |
| \(C_3\) | \((234)\) | 4 |
| \(C_4\) | \((243)\) | 4 |
| \(C_5\) | \((24)\) | 4 |
| \(C_6\) | \((13)(24)\) | 4 |

The crucial point is that \(H\) is not normal. For example,

\[
(23)(12)(23)=(13)\notin H.
\]

Therefore the compressed radial defects do **not** form a group under
single-valued multiplication.

A minimal exact witness is

\[
\boxed{C_2 C_2=\{C_0,C_2\}.}
\]

So radial defect composition is naturally relation-valued after stabilizer
compression. This is precisely where the existing relation/BRC and holonomy
machinery is needed.

## 6. H5/H6 — exact three-radius prototype and recursive spectrum

Use the three radii \(B_1\subset B_2\subset B_3\).

Choose aligner representatives

\[
g_1=e,\qquad g_2=(23),\qquad g_3=e,
\]

and choose each shell marker by

\[
p_n=R_{g_n}^{-1}a_n.
\]

Then

\[
p_1=(1,-1,0,0),\qquad
p_2=(-2,0,2,0),\qquad
p_3=(3,-3,0,0).
\]

The adjacent radial defects are

\[
\Delta_1=C_2,\qquad \Delta_2=C_2,
\]

but the exact endpoint transport from radius 1 to radius 3 is

\[
H g_1g_3^{-1}H=C_0.
\]

This lies in the relation-valued product
\(C_2C_2=\{C_0,C_2\}\). Hence the three-radius prototype gives an explicit
certificate that **compressing each intermediate transport to a double coset
loses enough information to make composition multivalued**.

A coherent positive control is \(g_n=e\) at all three scales, giving
\(\Delta_1=\Delta_2=C_0\).

An adversarial unreachable control is the shell marker \(c_n\) above.

An ambiguity control at \(n=2\) uses the already aligned pointer target plus the
interior marker

\[
p=(1,0,-1,0).
\]

The two aligners \(e,(12)\in H\) give two distinct depth-2 raw interiors
\(p\) and \((0,-1,1,0)\), while depth 1 gives the same interior.

### Typed recursive observables

For an alignable finite tower define

\[
\Sigma_N
=
\bigl(
[\mathcal I_1]_H,\Delta_1,
[\mathcal I_2]_H,\Delta_2,\ldots,
[\mathcal I_N]_H
\bigr),
\]

replacing \([\mathcal I_n]_H\) by the raw set-valued orbit whenever the declared
observation does not descend through \(H\).

The following taskbook readouts are now exact definitions in this model:

- `DEFECT_BIRTH_RADIUS`: first outer radius \(n+1\) with \(\Delta_n\ne C_0\);
- `DISTINGUISHING_RADIUS`: first radius/transition where two typed signatures differ;
- `SHIELDING_DEPTH`: depth \(d\) protects \(B_{n-d}\);
- `STABILIZATION_RADIUS`: first radius after which both aligned quotient values and
  radial defects remain unchanged under the declared extension rule;
- `PERIODIC_SCALE_ORBIT`: periodic sequence of alignment cosets \(Hg_n\);
- `BOUNDARY_TO_BULK_COLLISION`: distinct raw states with the same retained
  quotient signature.

For the exact alternating construction

\[
g_n=
\begin{cases}
e,&n\text{ odd},\\
(23),&n\text{ even},
\end{cases}
\]

the alignment-coset sequence has period two, while every adjacent defect is
\(C_2\). This is a finite-rule family for every bounded \(N\), not an assertion
of a physical or completed infinite world.

## 7. H8 — A2 slice transport and an exact stabilizer-leakage obstruction

For each coordinate \(i\), set

\[
L_i=\{x\in\Lambda_3:x_i=0\}.
\]

Then \(L_i\) is an A2 root-lattice slice and

\[
R_\sigma(L_i)=L_{\sigma(i)}
\]

for the declared permutation convention.

For the slice \(L_4\),

\[
|B_n\cap L_4|
=
1+3n(n+1),
\qquad
|S_n\cap L_4|=6n.
\]

The first exact slice ball counts are \(7,19,37\).

The residual stabilizer element \(h=(12)\in H\) preserves \(L_4\), but its
determinant on the two-dimensional A2 slice is

\[
\boxed{\det(R_h|_{L_4})=-1.}
\]

This is the key integration result for planar NollM/Eisenstein transport:

- the three-dimensional frame action is orientation-preserving;
- the residual shell stabilizer can nevertheless reverse the orientation of a
  preserved A2 slice;
- therefore an orientation-sensitive planar observable cannot in general descend
  through the pointer-target \(H\)-quotient as an untagged scalar.

Any transport of oriented path jets, signed-area/holonomy readouts,
positive-axis/path-order data, or chiral slice moments must carry at least

\[
(\text{slice index},\text{slice orientation},\text{layer/carrier tag}).
\]

If the orientation tag is erased, the aligned interior is genuinely ambiguous.
If orientation is declared gauge, the result is a two-sheet stabilizer orbit
rather than a canonical orientation.

This conclusion is carrier/readout-level. It does not promote the A3 shell, A2
slice, NollM hexagon, or any Euclidean orientation to native ontology.

## 8. Tool-reuse verdict

The task does **not** reveal a missing general-purpose tool family.

| Existing tool | Exact role in this package |
|---|---|
| T1 Scale Enumeration / Valuation | coefficient/inclusion-exclusion shell count and finite shell extraction |
| T2 Block Finite Certificate | bounded unreachable-orbit and orientation-leakage certificates |
| T4 Fiber Capacity / Collision Minima | first distinguishing/defect radius and quotient-collision witnesses |
| T5 Precision / Refinement | \(B_n\subset B_{n+1}\), restriction, reveal vs extension typing |
| T6 Operation-Safe Quotient | exact criterion for whether residual \(H\) may be erased |
| T7 Finite Symmetry / Equivariance | S4 orbit, stabilizer, rigid-target and canonical-choice analysis |
| T8 Relation Observable / Spectrum | set-valued aligners and relation-valued double-coset composition |
| T9 Holonomy / Cocycle / Gluing | staged-vs-direct scale transport and radial defect |
| T0 BRC | provenance-preserving composition once compressed defects become multivalued |

Verdict:

\[
\boxed{\texttt{COMPOSE_EXISTING_TOOLS}}
\]

with one task-local operator \(D_{n,d}\). No new shared tool is justified.

## 9. Semantic ledger

| Object | Type/status |
|---|---|
| \(\Lambda_3\), \(B_n\), \(S_n\) | exact relational/carrier construction for this task |
| \(r=\max|x_i|\) | operational shell radius |
| \(R_\sigma\) | exact finite carrier symmetry |
| \(D_{n,d}\) | task-local active move semantics |
| \(\beta_n\), rigid target | chosen boundary readouts |
| \(H\) | exact residual stabilizer of the chosen pointer target |
| \(\Delta_n\) | derived double-coset radial defect |
| shortest alignment word | algorithmic complexity only; not energy |
| A2 slice orientation | typed carrier orientation |
| NollM/Eisenstein planar observables | transferable only with their own layer/orientation/native tags |
| infinite completion | **not constructed or claimed** |
| physical Rubik-world ontology | **not claimed** |

## 10. Killed branches and unresolved frontier

Killed:

1. pure shell-supported moves as a source of nontrivial exact \(B_{n-1}\) response;
2. arbitrary selection of one aligner as a canonical solver;
3. treating double-coset defects as a group;
4. erasing residual \(H\) while retaining orientation-sensitive A2 data;
5. importing commercial Rubik-cube parity/orientation invariants.

The next exact theorem is now sharply localized:

> **Radial relation coherence problem.** For a declared family of coupled generators
> beyond the prefix-shell control model, classify when the scale-dependent
> stabilizers \(H_n\), restriction morphisms, and relation-valued defects admit an
> associative BRC/groupoid lift whose projection is the observed double-coset
> spectrum; then characterize the first radius at which no operation-safe
> quotient can make the scale square commute.

That is a genuine continuation because the current package proves the first
finite model and exposes the exact information lost by stabilizer compression.
