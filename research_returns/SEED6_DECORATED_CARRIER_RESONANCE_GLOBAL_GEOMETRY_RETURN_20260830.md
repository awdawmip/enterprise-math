# Seed-6 Decorated Carrier Resonance Global Geometry — Research Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

- Task-ID: `RS-SEED6-DECORATED-CARRIER-RESONANCE-GLOBAL-GEOMETRY`
- Publication-ID: `TP2-BC2BE52EDC1F8926FFF3`
- Researcher-ID: `EM-S6DCRG-D37306`
- Claim-ID: `chatgpt-s6dcrg-20260830-1725-d37306`
- Execution branch: `research/seed6-decorated-carrier-resonance-global-geometry-em-s6dcrg-d37306`
- Execution base: `9dac612533d1dc93ce2839df3e1dbdd29a39b6aa`
- Hard target: `DECORATED_CARRIER_RESONANCE_STRATIFIED_GLOBAL_GEOMETRY_CLASSIFIED`
- Terminal verdict: `SUCCESS`

## 1. Exact theorem

Let
\[
d=\gcd(a,b),\qquad a=dA,\quad b=dB,\quad \gcd(A,B)=1,
\]
and let `R` be a finite set of distinct exact outer-bundle objects.

The complete cross-row equalities in
\[
\begin{pmatrix}ar&as\\br&bs\end{pmatrix}
\]
are
\[
ar=br\iff a=b,\qquad as=bs\iff a=b,
\]
\[
br=as\iff (r,s)=(At,Bt),
\qquad
ar=bs\iff (r,s)=(Bt,At)
\]
for a unique positive integer `t`.

The primitive parametrizations are immediate from coprimality: `Br=As` forces
`A|r`, `B|s`, and the two quotients agree; the opposite equation is symmetric.

Both cross-column equations can hold simultaneously only when `A=B=1` and
`r=s`. Hence for `a!=b` and distinct bundle objects there is no orientation
conflict. For an unordered pair,
\[
\boxed{\{r,s\}=\{At,Bt\}}
\]
is the exact resonance criterion.

No freshness assumption is valid or needed. The resonance family itself
generically reuses carrier support when `A>1` or `B>1`; the complete primewise
valuation data remain attached to the exact ports.

## 2. Support-faithful local singular cell

Assume `A!=B`. For every `t` with `At,Bt in R`, define the typed collision
\[
e_t=\{(b,At),(a,Bt)\}.
\]

The operation-safe singular cell identifies only the geometric 0-cell
\[
(b,At)\sim(a,Bt),
\]
while retaining separately:

- carrier row;
- exact bundle/support port;
- complete valuation decoration;
- incident horizontal and vertical edge germs;
- support-specific face germ.

Thus the two oriented equations are not two resonance species: they are the two
orderings of the same unordered typed point-pair.

A value-only quotient is not a legal global attaching rule. For `(A,B)=(2,3)`
and `R={4,6,9}`, the safe collisions are
\[
(b,4)\sim(a,6),\qquad (b,6)\sim(a,9).
\]
The two occurrences of scalar `6` are different typed ports. Erasing the row
label fabricates a scalar chain `4-6-9` and a false shared port.

## 3. Matching lemma and global normal form

For `A!=B`, the family `{e_t}` is a matching on typed vertices. If two
resonances share their row-`b` endpoint then `At=At'`, hence `t=t'`; if they
share their row-`a` endpoint then `Bt=Bt'`, hence `t=t'`. Cross-row equality of
typed ports is forbidden by the retained row label.

Therefore scalar resonance chains can occur only after forgetting row type.
They never create an intrinsic shared-port dependency.

Define
\[
m_\Sigma(R)=\#\{t\ge1:At\in R,\ Bt\in R\}.
\]
Starting from the accepted clean carrier complex `K_R x I`, with `k=|R|`,
\[
V_0=2k,\qquad E_0=k^2,\qquad F_0=\binom{k}{2}.
\]
The `m=m_\Sigma(R)` disjoint point pinches merge vertices only, so
\[
V=2k-m,\qquad E=k^2,\qquad F=\binom{k}{2}.
\]
The complex remains connected. Every square retains a support-specific
horizontal edge germ, so the face boundaries remain independent. Hence
\[
\operatorname{rank}\partial_1=V-1,\qquad
\operatorname{rank}\partial_2=F.
\]
Consequently
\[
\boxed{X_\Sigma(R)\simeq K_R\vee\bigvee^{m_\Sigma(R)}S^1},
\]
\[
H_0\cong\mathbb Z,
\qquad
\boxed{H_1\cong
\mathbb Z^{(k-1)(k-2)/2+m_\Sigma(R)}},
\qquad
\boxed{H_2=0}.
\]

This proves the general one-legal-pinch/one-circle rule at support-faithful
typed-CW strength.

For a hypothetical non-safe quotient with genuine shared precursor vertices,
the correction is the rank of the identification relation, not the raw number
of written equalities: an equivalence class of `q` precursor vertices has only
`q-1` independent identifications. The exact decorated resonance relation never
needs that correction because the matching lemma forces all legal classes to
have size two.

## 4. Equality stratum

`a=b` is equivalent to `A=B=1`. Then every same-column cross-row pair already
coincides. This is carrier-row equality degeneration, not a cross-column
resonance family. After exact duplicate-row normalization the `I` fibre
collapses to the single-row base `K_R`. Distinct normalized bundle objects
therefore create no resonance pinch and no carrier-row height class.

Counting equality columns as independent pinches would duplicate an exact row
object and manufacture topology.

## 5. Carrier-height cohomology

Assume `a!=b`. Orient each vertical edge from row `a` to row `b` and put
\[
\alpha(v_r)=1,\qquad \alpha(h)=0
\]
for horizontal edges. Every square has two oppositely oriented vertical boundary
edges, so `alpha` is closed.

On the clean product,
\[
\alpha=\delta h,\qquad h(a,r)=0,\quad h(b,r)=1.
\]
At a resonance `(b,At)~(a,Bt)`, the primitive `h` takes values `1` and `0` on
the two identified vertices and cannot descend, while `alpha` does descend
because edge germs are not merged.

For each resonance, take the vertical edge at `At` and close it through the
pinch by a row-`a` horizontal path from `Bt` back to `At`. The resulting loop
`gamma_t` has
\[
\boxed{\int_{\gamma_t}\alpha=+1}
\]
for the chosen orientation and `-1` when reversed. Therefore
\[
\boxed{[\alpha]=0\iff m_\Sigma(R)=0}.
\]

The period is independent of `A`, `B`, `d`, SNF data, and valuation thickness:
it measures one row transition. Under the wedge normal form there is one
canonical height class whose value on every consistently oriented resonance
generator is `+1`; this does not assert `m` independent height classes.

Modulo two, every resonance generator has odd row-swap parity, so the intrinsic
carrier-row `C2` holonomy from the fixed `(2,3)` theorem survives unchanged.

## 6. Decorated-strata interaction

The full valuation profile remains necessary for state identity and safe
attaching, but the resonance locus depends only on the reduced coprime excess
pair `(A,B)`; the common core `d` cancels from the equality equations.

- `C0_DISTINCT_PRIME_PAIR`: standard independent pinches; `(2,3)` is the
  reference case.
- `C1_COPRIME_PRIME_POWER_THICK`: valuation thickness decorates the same
  primitive resonance law.
- `C2_COPRIME_MULTISUPPORT`: multisupport and forced seed-support reuse decorate
  the ports but add no incidence relation.
- `O1_OVERLAP_COMMON_BASE_RANK1`: reduce to `(A,B)` first; overlap does not
  couple pinches.
- `O2_OVERLAP_RANK2`: again the reduced ratio controls resonance; no
  O2-specific `H2` or shared-port effect appears.
- `E_EQUALITY`: duplicate-row degeneration; no distinct-bundle resonance graph.

Thus O1/O2 and valuation thickness can change the arithmetic ratio and local
decoration but do not create a valuation-sensitive topological correction after
row/support typing.

## 7. Operator boundary

A resonance loop canonically records only two-row carrier transport. The frozen
data supply no support-independent identification of the local three pairing
states across distinct cells, so there is no canonical pairing-state `S3`
connection.

Likewise no intrinsic section through the known `V4` kernel is supplied.
Choosing one atom-transposition lift would be gauge choice, not a canonical
`S4` holonomy.

## 8. Exact checker and falsification

The independent checker is

`research_checks/SEED6_DECORATED_CARRIER_RESONANCE_GLOBAL_GEOMETRY_CHECK_20260830.py`.

Observed run:
`PASS checks=5395236`.

It checks both symbolic iff parametrizations over `2<=a,b<=30`,
`1<=r,s<=40`; simultaneous-collision and equality conditions; all six decorated
strata; mixed resonance families; the typed matching theorem; the unsafe
`4-6-9` scalar-chain control; exact cellular Betti numbers and height-cocycle
exactness/nonexactness; and an exhaustive shared-typed-port falsification for
all `2<=a,b<25` with bundle set `{1,...,60}`.

No counterexample to the support-faithful normal form was found. The census is
only regression evidence; the coprime divisibility theorem and matching lemma
are the proof.

## 9. Boundary and disposition

The generalization yields a sharp separation:

\[
\text{complete valuation-decorated state}
+\text{ reduced-ratio resonance}
\Longrightarrow
\text{standard typed point pinches only}.
\]

There is no new valuation-sensitive global topology beyond the independent
pinch loops and the existing carrier-height class. Stronger chain effects after
scalarization are quotient artefacts.

No additive-distance, Fermat/square-shell, smooth curvature/manifold,
factor-recovery, factorization-performance, canonical `S3`, or canonical `S4`
claim is made.

Hard target:

`DECORATED_CARRIER_RESONANCE_STRATIFIED_GLOBAL_GEOMETRY_CLASSIFIED = SATISFIED`.

Recommended Driver freeze strength:

`REDUCED_RATIO_CONTROLS_RESONANCE + SUPPORT_TYPED_MATCHING + ONE_LEGAL_PINCH_ONE_CIRCLE + UNIT_CARRIER_HEIGHT_PERIOD + NO_VALUATION_SENSITIVE_TOPOLOGICAL_COUPLING`.

No automatic successor is recommended absent genuinely new support-faithful
structure.
