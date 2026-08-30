# Seed-6 Degenerate Strata Global Gluing — Research Return

Status: `TASK_TERMINAL_RETURN`

- Task-ID: `RS-SEED6-DEGENERATE-STRATA-GLOBAL-GLUING`
- Publication-ID: `TP2-A7ABAC66EFCDCA27EF1B`
- Researcher-ID: `EM-S6DGG-697F07`
- Claim-ID: `chatgpt-s6dgg-20260830-697f07`
- Execution branch: `research/seed6-degenerate-strata-global-gluing-em-s6dgg-697f07`
- Execution base: `83d6594b6e15981fce2621a9e9bb5cceccfdefa9`
- Execution record: `ER-4834A942F8F4C0377CC8`
- Hard target: `SEED6_DEGENERATE_STRATIFIED_GLOBAL_GLUE_CLASSIFIED`
- Verdict: `RESONANCE_PINCHED_STRATIFIED_PRODUCT + CANONICAL_HEIGHT_DEFECT_CLASS + NO_H2 + LIFT_GAUGE_BOUNDARY`

## 1. Executive result

The clean support-faithful carrier complex remains the accepted product

\[
X_0(R)=K_R\times I.
\]

The accepted local degeneration data do **not** all alter global topology. Equality, seed-state collapse, overlap, prime-power thickness and composite-bundle thickness are either exact-object normalization, state-fibre degeneration, or valuation/support decoration. The unique accepted local mechanism that changes the underlying carrier CW topology is the exact `3:2` rectangle-position collision

\[
3r=2s
\qquad (r<s).
\]

The support-safe implementation is crucial:

- the collision is first formed **inside the single typed degenerate cell** from its accepted rectangle-position partition;
- the geometric 0-cell `(3,r)=(2,s)` becomes one multi-port singular point;
- both support ports, all incident edge identities, all face identities and all support/bundle labels remain distinct as germs;
- global attaching maps still glue cells only along equal typed support/bundle ports.

Thus no distinct support is erased. The underlying geometric point is pinched, while the typed link retains the two branches.

For a finite set \(R\) of \(k\) distinct exact outer-bundle objects, define

\[
m(R)=\#\{\{r,s\}\subset R:r<s,\ 3r=2s\}.
\]

Then the carrier part of `STRATIFIED_BRIDGE_COMPLEX_V1(R)` has the exact normal form

\[
\boxed{
X_{\mathrm{str}}(R)
=
(K_R\times I)\Big/\bigl((3,r)\sim(2,s)\text{ for every }3r=2s\bigr),
}
\]

with support ports retained at every quotient point. Each resonance identifies one pair of distinct typed vertices; different resonance identifications use different typed ports.

Consequently,

\[
\boxed{
X_{\mathrm{str}}(R)
\simeq
K_R\vee\bigvee^{m(R)}S^1.
}
\]

Hence

\[
H_0(X_{\mathrm{str}};\mathbb Z)\cong\mathbb Z,
\]

\[
\boxed{
H_1(X_{\mathrm{str}};\mathbb Z)
\cong
\mathbb Z^{(k-1)(k-2)/2+m(R)},
}
\]

and

\[
\boxed{
H_2(X_{\mathrm{str}};\mathbb Z)=0.
}
\]

So the first intrinsic departure from the clean product is real but narrow:

> exact `3:2` resonance creates support-faithful **pinch loops**, not 2-cycles.

The same resonance also creates a canonical cohomological defect. Orient every vertical carrier edge from row \(2\) to row \(3\), and define

\[
\alpha(e)=
\begin{cases}
1,&e\text{ vertical }(2\to3),\\
0,&e\text{ horizontal}.
\end{cases}
\]

Every square has two oppositely oriented vertical boundary edges, so \(\alpha\) is an integral 1-cocycle. In the clean product it is exact:

\[
\alpha=\delta h,\qquad
h(2,r)=0,\quad h(3,r)=1.
\]

At a resonance \(3r=2s\), the two vertices on which \(h\) takes values \(1\) and \(0\) are identified, so \(h\) no longer descends, while \(\alpha\) still does. The explicit resonance loop

\[
\gamma_{r,s}=-h^{(2)}_{r,s}+v_r
\]

closes only because \((3,r)\sim(2,s)\), and

\[
\boxed{\int_{\gamma_{r,s}}\alpha=1.}
\]

Therefore

\[
\boxed{[\alpha]=0\iff m(R)=0.}
\]

Modulo \(2\), this is a canonical carrier-row \(C_2\) holonomy class: horizontal transport preserves the row, a vertical edge swaps rows, and every resonance pinch generator has odd swap parity.

This holonomy is **not** an atom-level lift. Pairing-state \(S_3\) transport across distinct supports is not canonically supplied by the frozen data, and every single pairing-state transposition still has two atom-transposition lifts differing by a nontrivial \(V_4\) kernel element. Atom-level \(S_4\) holonomy therefore remains gauge/extra-data unless a future task supplies a canonical lift.

## 2. `STRATIFIED_BRIDGE_COMPLEX_V1`

For a finite family of outer bundle values, first normalize exact duplicate bundle objects. The global object set is therefore a set \(R\), while diagonal `r=s` degeneration is retained as a local self-cell record rather than duplicated as a second global column.

`STRATIFIED_BRIDGE_COMPLEX_V1(R)` is the tuple

\[
(X_{\rm car},\ \mathcal P_{\rm state},\ \mathcal S_{\rm port},
\ \mathcal V,\ \pi),
\]

with:

1. **Clean carrier precursor**
   \[
   X_0=K_R\times I.
   \]
   Vertices are typed ports
   \[
   (2,r),(3,r).
   \]
   Every \(r\) has one vertical carrier edge, and every unordered distinct pair \(\{r,s\}\) has one typed square.

2. **Internal rectangle-position quotient**
   For a single support pair \(\{r,s\}\), use the accepted local partition of
   \[
   A=2r,\ B=2s,\ C=3r,\ D=3s.
   \]
   If \(3r=2s\) (for \(r<s\)), identify the geometric positions
   \[
   C=(3,r),\qquad B=(2,s)
   \]
   into one singular point. Their two support ports remain distinct germs.

3. **No cross-support value quotient**
   A numerical equality outside an accepted local position partition is not an attaching rule. In particular, pairing-state values from different supports are never glued merely because their numerical values or role labels agree.

4. **Pairing-state fibre**
   Each support pair retains its local reduced `DEGENERATE_PAIRING_CELL_V1`:
   - generic: filled three-state triangle;
   - one state collision: reduced edge;
   - triple seed collision: point.
   State cells from distinct supports are not globally identified without exact matching-support identity.

5. **Support/bundle labels**
   Every edge germ, face germ and state carries its exact participating bundle/support data.

6. **Valuation decoration**
   Primewise valuations, gcd overlap and bundle thickness decorate the typed cell. They do not create new CW identifications unless the frozen equality or `3:2` position relation is met.

This separates three levels that must not be conflated:

- geometric position collision;
- support-port identity;
- operator/state transport.

A resonance can identify the first while preserving the second and leaving the third only partially determined.

## 3. Global normal-form theorem

Let \(R\) contain \(k\) distinct exact bundle objects and \(N=\binom{k}{2}\).

Before resonance pinches,

\[
V_0=2k,\qquad E_0=k^2,\qquad F_0=N.
\]

For \(r<s\), the only cross-row rectangle-position equality is

\[
3r=2s.
\]

Each such relation identifies exactly one top/bottom typed vertex pair. A typed vertex can occur in at most one such equality on a fixed row, so the \(m(R)\) point identifications are disjoint at the port level. The column resonance graph may form chains, but the top and bottom ports used by successive links are different.

Therefore

\[
V=2k-m(R),\qquad E=k^2,\qquad F=N.
\]

No edge or face is merged.

The complex remains connected, so

\[
\operatorname{rank}\partial_1=V-1.
\]

Moreover every square has its own support-specific top horizontal edge, and no such edge is merged with another square. Hence the face boundaries are linearly independent:

\[
\operatorname{rank}\partial_2=F.
\]

It follows directly that

\[
\beta_0=1,
\]

\[
\beta_1
=
E-(V-1)-F
=
\frac{(k-1)(k-2)}2+m(R),
\]

\[
\beta_2=F-\operatorname{rank}\partial_2=0.
\]

Equivalently, identifying one pair of points in a connected CW complex adds one wedge \(S^1\); performing the \(m(R)\) disjoint resonance identifications gives

\[
X_{\rm str}(R)\simeq X_0(R)\vee\bigvee^{m(R)}S^1
\simeq K_R\vee\bigvee^{m(R)}S^1.
\]

This is the requested exact non-product witness and normal form at the same time.

## 4. Local link and valence table

For the global complex with \(k\) distinct bundle objects, a clean carrier vertex has one vertical edge germ and \(k-1\) horizontal edge germs. Its link is

\[
K_{1,k-1}.
\]

The resonance pinch merges two distinct clean vertices but does **not** merge their germs. Therefore its typed link is

\[
\boxed{
K_{1,k-1}\ \sqcup\ K_{1,k-1}.
}
\]

It is disconnected. The singular vertex has \(2k\) incident edge germs and \(2(k-1)\) incident face corners. This is a genuine non-manifold pinch signature, not a visual analogy.

| stratum | carrier cell | pairing-state cell | link / valence effect |
|---|---|---|---|
| clean distinct bundles | square | filled triangle | clean global link \(K_{1,k-1}\) |
| `r=s` | diagonal square reduces to existing vertical carrier edge | triangle -> edge | no new global loop; diagonal cell adds no 2-cell |
| one seed collision (`r=2`, `r=3`, `s=2`, or `s=3`) away from `{2,3}` | ordinary square | triangle -> edge | carrier link unchanged |
| `3r=2s` / `2r=3s`, distinct bundles | opposite-corner pinched square | usually filled triangle | singular link \(K_{1,k-1}\sqcup K_{1,k-1}\); one new \(H_1\) generator |
| overlap `gcd(r,s)>1` without resonance/equality | ordinary square with gcd decoration | unchanged | no topological link change |
| prime-power thickness | ordinary square unless equality | unchanged unless exact equality | valuation fibre only |
| composite bundle intersection | ordinary or resonance-pinched according to exact position relation | support-local | bundle decoration does not merge germs |
| `{r,s}={2,3}` | resonance-pinched square | reduced edge | genuine mixed cell: pinch topology + state collapse |
| `r=s=2` or `r=s=3` | reduced carrier edge | point | deepest equality/seed degeneration; no 2-cell |

For a single resonance cell (\(k=2\)), the pinch link is simply two disjoint intervals and the pinched disk has \(\beta_1=1,\beta_2=0\).

## 5. Exact singular-strata intersections

### 5.1 Equality versus resonance

For positive integers,

\[
r=s
\quad\text{and}\quad
3r=2s
\]

cannot hold simultaneously. Thus

\[
\boxed{E\cap R=\varnothing.}
\]

Equality is therefore not the source of the resonance loop.

### 5.2 Resonance normal form

For \(r<s\),

\[
3r=2s
\iff
(r,s)=(2t,3t)
\]

for a unique positive integer \(t\).

Hence the resonance stratum splits exactly:

- \(t=1\): \((r,s)=(2,3)\), the double-seed cell with joint signature
  \[
  (n_P,n_V)=(2,3),
  \]
  and no external gcd overlap beyond \(1\);

- \(t>1\): automatically
  \[
  \gcd(r,s)=t>1,
  \]
  no seed collision occurs, and the joint signature is
  \[
  (n_P,n_V)=(3,3).
  \]

Therefore every non-seed resonance is automatically an overlap stratum, but overlap contributes only valuation/support decoration on top of the same pinched carrier cell.

### 5.3 Equality and overlap

If \(r=s>1\), overlap is automatic. The global exact-object normalization removes duplicate columns; the diagonal local cell reduces to the existing vertical carrier edge. The state fibre is an edge, except at `r=s=2` or `r=s=3`, where all three symbolic pairing states collapse to a point.

### 5.4 Seed collision plus overlap without resonance

Examples such as `(2,4)` and `(3,6)` have a pairing-state collapse and nontrivial overlap but no rectangle resonance. Their carrier square is unpinched. Therefore state collapse + overlap alone does not generate new global homology.

### 5.5 Prime-power thickness

For same-base prime powers \(p^a,p^b\), unequal exponents change valuation thickness while leaving the pairing/rectangle incidence generic. A ratio \(p^{a-b}=3/2\) is impossible for a prime \(p\), so pure same-prime thickness does not itself create the `3:2` pinch. Exact equality \(a=b\) is handled by the diagonal normalization.

### 5.6 Composite resonance

If \(t\) is composite in `(2t,3t)`, the resonance point is the same topological cell type as for prime \(t\): a support-retaining pinch. Composite support merely thickens/decorates the two retained port branches. No additional link component or \(H_2\) appears.

Thus the only new incidence type produced by crossing accepted strata is the already-exact double-seed resonant cell `{2,3}`; all \(t>1\) resonance/overlap/composite intersections are decorated instances of the same pinched carrier type.

## 6. Holonomy and path-dependence audit

### 6.1 Carrier-preserving horizontal transport

The accepted transport

\[
\tau_{r\to s}(cr)=cs,\qquad c\in\{2,3\},
\]

is unchanged on the horizontal subgroupoid. It still satisfies

\[
\tau_{s\to t}\tau_{r\to s}=\tau_{r\to t}.
\]

Thus the horizontal carrier-preserving transport remains flat and endpoint-only. Resonance does not create path dependence inside that subgroupoid.

### 6.2 Canonical carrier-height defect

The extended typed carrier graph has a canonical distinction between horizontal edges and the vertical `2<->3` carrier edge. The integral cocycle

\[
\alpha(v_r)=1,\qquad
\alpha(h^{(2)}_{r,s})=\alpha(h^{(3)}_{r,s})=0
\]

is closed on every square.

Clean case:

\[
\alpha=\delta h,\qquad h(2,r)=0,\ h(3,r)=1.
\]

Resonant case \(3r=2s\):

\[
(3,r)\sim(2,s),
\]

so \(h\) cannot descend. The cycle

\[
\gamma_{r,s}=-h^{(2)}_{r,s}+v_r
\]

has zero boundary after the pinch and satisfies

\[
\alpha(\gamma_{r,s})=1.
\]

This proves an intrinsic, support-retaining cohomology class.

Modulo 2, assign identity to horizontal edges and the unique row swap to vertical edges. The holonomy of \(\gamma_{r,s}\) is the nontrivial element of \(C_2\). This is canonical at the carrier-row level because the row labels and vertical-edge type are frozen data.

### 6.3 Pairing-state-only transport

The three perfect matchings are support-typed local states. Distinct support pairs do not share an exact matching state. Therefore the frozen data do not supply a canonical global \(S_3\) parallel transport merely from equal role names `M0,M1,M2`.

Role-normalizing state vertices across supports is a forgetful quotient. Any global \(S_3\) holonomy that requires that quotient is `MODEL_DEPENDENT`.

At the double-seed resonance `{2,3}`, the local state fibre is only an edge, not a loop, so the carrier pinch does not create an independent pairing-state holonomy.

### 6.4 Atom-level lift and `V4`

The accepted map

\[
S_4\to S_3
\]

has kernel \(V_4\). Every pairing-state transposition has two single-atom-transposition lifts, and the two lifts differ by a nontrivial \(V_4\) element.

Therefore even if a future task canonically supplies an \(S_3\) state path, its atom-level lift is not determined by the current data. Selecting one lift per edge is a gauge/extra-data choice.

The checker explicitly constructs two lifts of one state transposition and verifies that their ratio is a nonidentity double transposition fixing all three pairing states.

### 6.5 Verdict

| transport / operator | result |
|---|---|
| horizontal carrier-preserving | intrinsic and flat |
| carrier-height integral cocycle | intrinsic; nonexact iff resonance exists |
| carrier-row \(C_2\) holonomy | intrinsic; resonance pinch generator -> swap |
| global pairing-state \(S_3\) transport | not canonically supplied across distinct supports |
| atom-level \(S_4\) lift | nonunique |
| `V4` residue | gauge/extra data unless a canonical section is later supplied |

The new intrinsic holonomy is therefore a **carrier-row singular holonomy**, not a promoted atom-lift holonomy.

## 7. Quotient-safety test

The task reuses the operation-safe quotient principle rather than inventing a new general quotient formalism.

### Safe / conditionally safe

1. **Exact duplicate bundle normalization.**  
   Replacing repeated occurrences of the same exact bundle object by one global column is topology-safe. Event multiplicity must remain metadata if later operations need it.

2. **Internal resonance position collision with port retention.**  
   The accepted local rectangle-position partition may identify the geometric 0-cell at `3r=2s`, provided both support ports, edge germs, face identities and bundle labels survive. This is the positive singular model used here.

3. **Forget switch preimage multiplicity.**  
   Safe for reduced state-cell topology; unsafe for event-history questions.

4. **Forget valuation decoration.**  
   Safe only for the carrier CW homotopy type after the exact collision partition is already known. Unsafe for overlap, thickness or bundle-sensitive operations.

### Unsafe

1. **Cross-support state-role quotient.**  
   Identifying all `M0` states, all `M1` states and all `M2` states across supports reproduces the known false
   \[
   H_2\cong \mathbb Z^{N-1}.
   \]

2. **Global value-only gluing not licensed by a local collision partition.**  
   Equal integers from unrelated support cells are not a support-safe attaching rule.

3. **Dropping resonance port provenance and then inferring a unique operator lift.**  
   The geometric pinch survives, but operator semantics do not. A support-sensitive downstream operation cannot be reconstructed from a naked value vertex.

4. **Arbitrary atom lift.**  
   Choosing one of the two single-transposition lifts of each state switch can manufacture \(V_4\) residues. No such residue is intrinsic here.

5. **Composite-bundle collapse into prime atoms without an explicit expansion morphism.**  
   Outer-bundle and expanded-prime models are distinct frozen model classes.

The exact positive loop found in this task survives without any unsafe quotient: its two port branches are still visible in the disconnected typed link.

## 8. Minimal positive and negative witnesses

### Positive witness: `(r,s)=(4,6)`

The rectangle is

\[
(2r,2s,3r,3s)=(8,12,12,18).
\]

The two middle positions collide exactly:

\[
(3,4)=(2,6)=12.
\]

The support-retaining cell is a disk with opposite corners pinched and both port germs retained.

For the single pair \(R=\{4,6\}\),

\[
(V,E,F)=(3,4,1),
\]

\[
(\beta_0,\beta_1,\beta_2)=(1,1,0).
\]

The pinch link is two disjoint intervals, and

\[
\int_{\gamma_{4,6}}\alpha=1.
\]

This is the smallest non-seed positive witness.

### Mixed positive witness: `{2,3}`

The same carrier pinch occurs at value \(6\), while the pairing-state fibre also collapses from three states to two. It is a genuine intersection cell:

- carrier: pinched square;
- state: reduced edge;
- carrier-height period: \(1\).

### Negative witness: overlap without resonance

For `(35,55)`,

\[
\gcd(35,55)=5,
\]

but there are three pairing states and four rectangle positions. The cell remains an ordinary square with valuation/support decoration. No new carrier loop or holonomy occurs.

### Negative witness: support-erased state triangles

For \(k=4\), there are \(N=6\) support-specific filled matching triangles. If their three vertex/edge types are incorrectly identified across supports while retaining all six faces, then

\[
\beta_2=N-1=5.
\]

For \(k=10\),

\[
\beta_2=45-1=44.
\]

The checker reproduces these as deliberately unsafe controls.

## 9. Exact checker

Checker:

`research_checks/SEED6_DEGENERATE_STRATA_GLOBAL_GLUING_CHECK_20260830.py`

Machine-readable census:

`research_artifacts/SEED6_DEGENERATE_STRATA_GLOBAL_GLUING/census.json`

The standard-library checker verifies:

1. all `40,000` ordered pairs `1<=r,s<=200` reproduce the accepted local joint-signature census;
2. all `66` unordered resonances `r<s<=200` have the exact form `(2t,3t)`;
3. `t=1` is exactly the double-seed `(2,3)` signature `(2,3)`;
4. every `t>1` resonance is overlap with signature `(3,3)`;
5. mixed clean/resonant/overlap/prime-power/composite examples satisfy
   \[
   \beta_1=\frac{(k-1)(k-2)}2+m,\qquad \beta_2=0;
   \]
6. every resonance pinch has two link components of size \(k\);
7. every explicit resonance cycle has integral height period `1`;
8. support-erasure produces the expected false `H2`;
9. two atom lifts of the same state transposition differ by a nontrivial kernel element.

Local execution verdict:

```text
PASS RS-SEED6-DEGENERATE-STRATA-GLOBAL-GLUING
joint_signature_census {(1, 2): 2, (2, 2): 198, (2, 3): 2, (2, 4): 792, (3, 3): 130, (3, 4): 38876}
unordered_resonances_r<s<=200 66
mixed (5, 7, 11) m=0 betti=(1, 1, 0)
mixed (4, 6, 11) m=1 betti=(1, 2, 0)
mixed (4, 6, 9) m=2 betti=(1, 3, 0)
mixed (2, 3, 5) m=1 betti=(1, 2, 0)
mixed (35, 55, 77) m=0 betti=(1, 1, 0)
mixed (12, 18, 25) m=1 betti=(1, 2, 0)
mixed (16, 24, 36, 54, 81) m=4 betti=(1, 10, 0)
mixed (25, 125, 7, 11) m=0 betti=(1, 3, 0)
support_erasure_beta2_k4 5
```

Finite checks are regression certificates. The classification itself follows from the exact CW boundary formulas, the point-identification normal form and the explicit cocycle witness.

## 10. Hard-target audit

A. `STRATIFIED_BRIDGE_COMPLEX_V1`: **PASS**.  
Support-retaining carrier CW complex, state fibres, typed ports and valuation decoration are separated explicitly.

B. Local singular links/valence: **PASS**.  
Equality, seed collision, resonance, overlap, prime-power and composite cases classified; resonance link is exactly disconnected.

C. Global `H0,H1,H2`: **PASS**.  
\[
H_1=\mathbb Z^{(k-1)(k-2)/2+m(R)},\quad H_2=0.
\]

D. Path dependence / holonomy: **PASS**.  
Horizontal carrier transport remains flat; canonical carrier-height defect and mod-2 row holonomy are nontrivial exactly when resonance exists; pairing-state and atom-lift boundaries are separated.

E. Mixed-strata intersections: **PASS**.  
`E∩R=empty`; resonance is `(2t,3t)`; `t=1` is double seed; `t>1` is automatically overlap; valuation/composite data decorate the same pinch type.

F. Quotient safety: **PASS**.  
Internal typed resonance collision distinguished from support erasure; unsafe state quotient and arbitrary lift controls reproduced.

G. Normal form / minimal witness: **PASS**.  
\[
X_{\rm str}\simeq K_R\vee\bigvee^{m(R)}S^1,
\]
with `(4,6)` as the minimal non-seed exact witness.

H. Exact checker: **PASS**.  
Standard-library regression covers the frozen 40,000-case local census and multiple mixed global configurations.

## 11. Boundary and next frontier

This result does **not** claim:

- a manifold or smooth curvature model;
- additive distance;
- factor recovery or factorization performance;
- a canonical global pairing-state \(S_3\) connection;
- a canonical atom-level \(S_4\) lift;
- any external historical novelty.

The new structure is much narrower and exact:

\[
\boxed{
\text{clean product}
\;\longrightarrow\;
\text{support-retaining resonance pinches}
\;\longrightarrow\;
\text{extra }H_1
+
\text{carrier-height defect},
\quad H_2=0.
}
\]

The clean successor frontier is therefore not “more rectangles”. It is to test whether the canonical integral class \([\alpha]\), its mod-2 carrier-row holonomy, and the resonance-chain incidence survive the next decorated-carrier generalization \((a,b)\), and whether a genuinely canonical operator connection can ever couple to that class without choosing an \(S_4\) lift gauge.

**Hard target satisfied at the stated support-faithful typed-CW strength.**
