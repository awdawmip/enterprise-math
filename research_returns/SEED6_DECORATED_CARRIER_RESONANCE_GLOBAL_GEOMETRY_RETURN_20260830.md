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

## 1. Executive theorem

Let the decorated carrier pair be

\[
\Sigma=(a,b),\qquad d=\gcd(a,b),\qquad a=dA,\quad b=dB,\quad \gcd(A,B)=1,
\]

and let `R` be a finite set of distinct exact outer-bundle objects.

For `A != B`, define

\[
m_\Sigma(R)=\#\{t\ge1:At\in R,\ Bt\in R\}.
\]

Then every legal cross-column resonance is exactly the support-typed point-pair

\[
e_t=\{(b,At),(a,Bt)\}.
\]

The two oriented equations

\[
br=as,\qquad ar=bs
\]

do not define two independent resonance species: after the exact bundle ports are retained they are the two orderings of the same unordered typed collision family `e_t`.

Most importantly, the family `{e_t}` is a **matching on typed ports**. Distinct `t` never share a typed vertex. A scalar bundle value can lie in two successive ratio relations, but then it occurs once on row `a` and once on row `b`; those are different ports and must not be merged. Therefore the apparent resonance-chain coupling seen after row erasure is not intrinsic.

For the support-faithful carrier complex,

\[
X_\Sigma(R)=
(K_R\times I)/\bigl((b,At)\sim(a,Bt)\text{ for every }At,Bt\in R\bigr),
\]

where only the geometric 0-cell is pinched and all row labels, exact bundle/support ports, valuation decorations, incident edge germs, and face germs remain retained. Then

\[
\boxed{X_\Sigma(R)\simeq K_R\vee\bigvee^{m_\Sigma(R)}S^1}
\]

and, for `k=|R|`,

\[
H_0(X_\Sigma;\mathbb Z)\cong\mathbb Z,
\]

\[
\boxed{H_1(X_\Sigma;\mathbb Z)
\cong\mathbb Z^{(k-1)(k-2)/2+m_\Sigma(R)}},
\]

\[
\boxed{H_2(X_\Sigma;\mathbb Z)=0}.
\]

Thus the fixed `(2,3)` theorem is not exceptional topologically: for every **distinct** decorated carrier pair, full support typing reduces the general resonance geometry to independent support-retaining point pinches. The valuation profile changes the arithmetic resonance ratio and its decoration, but creates no additional topology beyond those pinches.

The equality stratum `a=b` is different. Since `gcd(A,B)=1`, it is exactly `A=B=1`. Then same-column cross-row positions coincide for every bundle object. This is a carrier-row equality degeneration, not a cross-column resonance family. After exact duplicate-row normalization the carrier interval collapses fibrewise to the single-row base `K_R`; distinct normalized bundle objects create no resonance pinch and no carrier-row height holonomy. Counting every equality column as a pinch would be a duplicate-row artefact.

## 2. A. Exact resonance locus

Consider the four rectangle positions

\[
ar,\quad as,\quad br,\quad bs.
\]

The complete cross-row equalities are:

1. same-column collisions:
   \[
   ar=br\iff a=b,\qquad as=bs\iff a=b;
   \]
2. cross-column collisions:
   \[
   br=as\iff Br=As
   \iff (r,s)=(At,Bt)
   \]
   for a unique positive integer `t`;
3. the opposite orientation:
   \[
   ar=bs\iff Ar=Bs
   \iff (r,s)=(Bt,At)
   \]
   for a unique positive integer `t`.

The primitive parametrizations follow immediately from `gcd(A,B)=1`: `A|r` and `B|s` in the first equation, with the common quotient equal to `t`; the second equation is symmetric.

The two cross-column equalities can hold simultaneously only if

\[
A^2=B^2.
\]

Positivity and coprimality force `A=B=1`, and then both equations reduce to `r=s`. Hence for `a!=b` and distinct exact bundle objects there is no orientation conflict or overlap.

For an unordered pair `{r,s}` and `A!=B`, legal resonance is equivalently

\[
\boxed{\{r,s\}=\{At,Bt\}\text{ for a unique }t\ge1.}
\]

No freshness hypothesis occurs. Indeed the primitive family itself forces seed-support reuse whenever `A>1` or `B>1`; this reuse is part of the retained valuation decoration rather than an obstruction.

## 3. B. Support-faithful singular cell

For a resonance parameter `t`, the safe local cell is obtained inside the single typed rectangle by identifying only the geometric positions

\[
(b,At)\sim(a,Bt).
\]

The singular point carries two distinct germs:

- row `b`, exact bundle port `At`, with the full valuation/support data of `b` and `At`;
- row `a`, exact bundle port `Bt`, with the full valuation/support data of `a` and `Bt`.

All incident horizontal/vertical edge germs and the support-specific face germ remain distinct. This is the direct decorated analogue of the Driver-accepted `(2,3)` multi-port pinch.

An operation-safe quotient therefore remembers at least

`(carrier row, exact bundle object, primewise valuation decoration, edge germ, face germ)`.

A value-only quotient is invalid as a gluing authority. Example: with `(A,B)=(2,3)` and `R={4,6,9}`, the legal typed resonances are

\[
(b,4)\sim(a,6),\qquad (b,6)\sim(a,9).
\]

They use four distinct typed ports. Erasing rows changes this into the scalar chain

\[
4-6-9
\]

and falsely makes the middle value `6` a shared port. The checker includes this as a mandatory negative control.

## 4. C. Global normal form and the chain-correction question

Let `k=|R|` and begin with the accepted clean carrier complex `K_R x I`. Its typed vertices are `(a,r),(b,r)`, it has one vertical edge per bundle, two row-specific horizontal edges per unordered bundle pair, and one square per unordered pair. Hence

\[
V_0=2k,\qquad E_0=k^2,\qquad F_0=\binom{k}{2}.
\]

### Matching lemma

For `A!=B`, the resonance pair for parameter `t` is

\[
e_t=\{(b,At),(a,Bt)\}.
\]

If two resonance pairs share their row-`b` endpoint, then `At=At'`, so `t=t'`. If they share their row-`a` endpoint, then `Bt=Bt'`, so again `t=t'`. A row-`a` port can never equal a row-`b` port as a typed port. Therefore distinct `e_t` are vertex-disjoint.

This proves that all scalar resonance chains, shared numerical bundle values, and mixed `t` sequences are harmless after exact row/support typing. No decorated O1/O2 exception exists.

Consequently `m=m_\Sigma(R)` pinches give

\[
V=2k-m,\qquad E=k^2,\qquad F=\binom{k}{2}.
\]

No edge or face is merged. The complex is connected, so `rank d1=V-1`. Every support-specific square still has a horizontal edge germ not appearing in any other face boundary with the same typed identity, hence the face boundaries are independent and `rank d2=F`.

Thus

\[
\beta_0=1,
\]

\[
\beta_1=E-(V-1)-F
=\frac{(k-1)(k-2)}2+m,
\]

\[
\beta_2=F-\operatorname{rank}d_2=0.
\]

Equivalently, the disjoint typed point identifications give the wedge normal form in Section 1.

### General correction rule versus the actual arithmetic case

If one deliberately leaves the support-faithful model and imposes a family of non-disjoint point identifications, the correct loop contribution is the rank of the identification relation, not the raw number of written equalities: an equivalence class of `q` distinct precursor vertices contributes only `q-1` independent point identifications. This is the correction requested by the taskbook for hypothetical shared-port chains.

For the exact decorated arithmetic resonance relation, however, the matching lemma proves every legal class has size two and the correction reduces exactly to `m_\Sigma(R)`. The unsafe value-only quotient is therefore not a counterexample to one-pinch/one-circle; it changes the object being studied.

## 5. D. Carrier-height cohomology

Assume `a!=b`. Orient every vertical edge from row `a` to row `b` and define the integral 1-cochain

\[
\alpha(v_r)=1,\qquad \alpha(h)=0
\]

on every horizontal edge. Every square contains two vertical edges with opposite boundary orientations, so `alpha` is closed.

In the clean product it is exact:

\[
\alpha=\delta h,
\qquad h(a,r)=0,\quad h(b,r)=1.
\]

At a legal resonance,

\[
(b,At)\sim(a,Bt),
\]

the clean primitive `h` takes values `1` and `0` on the two identified vertices and therefore cannot descend. The cocycle `alpha` still descends because no edge germ is merged.

For each resonance parameter `t`, take the vertical edge at `At` followed, through the pinch, by the row-`a` horizontal path from `Bt` back to `At`. This is a closed loop `gamma_t` and

\[
\boxed{\int_{\gamma_t}\alpha=+1}
\]

with the chosen orientation; reversing it gives `-1`. Hence

\[
\boxed{[\alpha]=0\iff m_\Sigma(R)=0.}
\]

The period is **not** `A`, `B`, `d`, an SNF invariant, or a valuation thickness. It is exactly the unit row-height change. Under the wedge decomposition, one canonical height class has coordinate `+1` on every consistently oriented resonance generator; this does not assert `m` independent height classes.

Reduction mod 2 yields the same intrinsic two-row `C2` holonomy as in the fixed `(2,3)` theorem: every resonance generator has odd row-swap parity. This statement depends only on the retained row typing.

For `a=b`, the two-row carrier has already degenerated to one exact row after normalization, so this carrier-row height distinction is absent rather than becoming a family of artificial nonexact classes.

## 6. E. Interaction with decorated strata

The accepted carrier atlas divides the local state into the following strata.

| stratum | resonance arithmetic | topological effect |
|---|---|---|
| `C0_DISTINCT_PRIME_PAIR` | ratio determined by coprime `A=a`, `B=b`; `(2,3)` is the reference case | standard independent typed pinches |
| `C1_COPRIME_PRIME_POWER_THICK` | same primitive law `{At,Bt}`; valuation exponents decorate the ports | no extra topology |
| `C2_COPRIME_MULTISUPPORT` | same primitive law; resonance normally reuses carrier support | no extra topology |
| `O1_OVERLAP_COMMON_BASE_RANK1` | reduce first to coprime excess `(A,B)`; e.g. `(4,8)` gives `(A,B)=(1,2)` | overlap decorates the pinch; matching lemma still holds |
| `O2_OVERLAP_RANK2` | again controlled exactly by reduced `(A,B)`; e.g. `(2,6)` gives `(1,3)` | no O2-specific coupling or `H2` |
| `E_EQUALITY` | `A=B=1`; all same-column row positions coincide, while distinct bundles have no cross-column resonance | duplicate-row normalization collapses the carrier `I` fibre; no resonance-loop count |

Thus the full valuation profile is indispensable for operation safety and stratum identity, but the resonance **locus** depends only on the reduced coprime excess pair `(A,B)`. The common core `d` cancels from the equality equation. This is a sharp separation between arithmetic decoration and global incidence topology.

O1/O2 can change which ratio occurs and the valuation decoration at a singular point, but they do not change the typed incidence theorem. In particular there is no valuation-sensitive correction to `m_\Sigma(R)` once row/support ports are retained.

## 7. F. Operator boundary

A resonance loop canonically records only carrier-row transport. The frozen data do not specify a support-independent identification of the local three pairing states across distinct support cells. Therefore the pinch does not produce a canonical pairing-state `S3` connection.

Likewise, selecting one atom-level transposition lift would not solve the known `V4` kernel ambiguity. No intrinsic section through that kernel is supplied here. Consequently there is no canonical `S4` holonomy or atom-level lift in this result.

## 8. G. Exact checker and falsification

The independent checker is

`research_checks/SEED6_DECORATED_CARRIER_RESONANCE_GLOBAL_GEOMETRY_CHECK_20260830.py`.

It uses exact integer arithmetic and Python standard-library rational row reduction. The run completed with

`PASS checks=5395236`.

It verifies:

- both symbolic iff parametrizations for all `2<=a,b<=30`, `1<=r,s<=40`;
- the simultaneous-collision theorem and equality same-column theorem;
- equivalence of the two orientations as one unordered typed resonance family;
- representatives of all six decorated strata;
- the typed-port matching theorem across mixed resonance families;
- a negative control where row erasure fabricates the scalar chain `4-6-9`;
- exact cellular `beta_0`, `beta_1`, `beta_2` for several mixed C0/C1/O1/O2 families;
- exactness of the clean height cocycle and nonexactness after every tested legal pinch;
- exhaustive falsification of shared typed ports for all `2<=a,b<25` using bundle set `{1,...,60}`.

No counterexample to the support-faithful normal form was found. The finite search is only a regression certificate; the matching lemma and coprime divisibility argument are the proofs.

## 9. What is genuinely new and what is not

The general decorated result has one positive arithmetic input and one negative structural conclusion.

Positive: the complete cross-row resonance locus is controlled exactly by the coprime excess ratio `(A,B)` and necessarily includes non-fresh support reuse.

Negative but decisive: after full row/support typing, the general resonance relation never develops intrinsic chain coupling. O1/O2 valuation geometry does not create a new global invariant beyond the standard support-retaining pinch loops and the existing row-height class. All stronger chain effects found after scalarization are quotient artefacts.

No additive-distance, Fermat, square-shell, smooth curvature/manifold, factor-recovery, factorization-performance, canonical `S3`, or canonical `S4` claim is made.

## 10. Disposition

Hard target:

`DECORATED_CARRIER_RESONANCE_STRATIFIED_GLOBAL_GEOMETRY_CLASSIFIED = SATISFIED`.

Recommended Driver action: review the exact resonance iff theorem, typed matching lemma, equality-row normalization boundary, and checker evidence. If accepted, freeze the general decorated-carrier resonance geometry at the strength

`REDUCED_RATIO_CONTROLS_RESONANCE + SUPPORT_TYPED_MATCHING + ONE_LEGAL_PINCH_ONE_CIRCLE + UNIT_CARRIER_HEIGHT_PERIOD + NO_VALUATION_SENSITIVE_TOPOLOGICAL_COUPLING`.

No automatic successor is recommended. A further task would be justified only by genuinely new structure not erased by the support-faithful quotient boundaries.