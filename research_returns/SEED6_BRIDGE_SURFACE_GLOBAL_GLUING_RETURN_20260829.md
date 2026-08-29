# Seed-6 Bridge Surface Global Gluing — Research Return

Status: `TASK_TERMINAL_RETURN`

- Task-ID: `RS-SEED6-BRIDGE-SURFACE-GLOBAL-GLUING`
- Publication-ID: `TP2-3C47811A2BD4B67B28B8`
- Researcher-ID: `EM-S6G-76E296`
- Claim-ID: `S6G-3A124087`
- Execution branch: `research/seed6-bridge-surface-global-gluing-em-s6g-76e296`
- Execution base: `65d1cae115e648f5154a898cd3ba83a2a2b27223`
- Hard target: `SEED6_BRIDGE_SURFACE_GLOBAL_GLUE_CLASSIFIED`
- Return verdict: `STANDARD_CELL_COMPLEX_REIDENTIFIED + GLOBAL_FLATNESS_PROVED + MODEL_DEPENDENT_BOUNDARY`

## 1. Executive result

Fix distinct primes

\[
R_k=\{r_1,\ldots,r_k\},\qquad r_i>3,
\]

and write

\[
a_r=2r,\qquad b_r=3r,\qquad C_r=(a_r,b_r).
\]

The natural support-faithful global gluing of all pairwise bridge rectangles is **not a new surface**. It is exactly the standard product CW complex

\[
X_k\cong K_k\times I,
\]

where the complete graph \(K_k\) records the prime-column index and \(I\) records the two Seed-6 carriers \(2,3\).

Consequences:

1. the natural column transport is strictly compositional and every loop has trivial holonomy;
2. \(H_2(X_k)=0\), while the surviving \(H_1\) is exactly the ordinary cycle space of \(K_k\);
3. \(X_3\) is an annulus, but for \(k\ge4\) the object is not a 2-manifold because every vertical carrier edge belongs to \(k-1\ge3\) square cells;
4. the numerical pairing graph obtained by adjoining \(6\) and the vertices \(pq\) splits as a star plus \(K_{k,k}\) with a perfect matching removed; its cycles are standard graph cycles, not a new bridge holonomy;
5. exact-support three-pairing 2-cells for different \(\{p,q\}\) do not glue at all;
6. a support-erasing quotient can manufacture a large \(H_2\), but that homology is a quotient artifact caused by identifying mathematically different prime supports.

Thus the word **bridge surface** is literally justified only for the \(k=3\) annulus. For general \(k\), the smallest honest term is **Seed-6 bridge complex**, more precisely a labelled column-square \(I\)-bundle over \(K_k\).

No factorization, endpoint-recovery, additive-distance, or performance interpretation is used anywhere in this return.

---

## 2. Model X — support-faithful column-square complex

### 2.1 Definition

For every \(r\in R_k\) introduce two vertices

\[
(2,r),\ (3,r)
\]

with numerical labels \(2r,3r\). Add:

- one vertical edge \(v_r:(2,r)\leftrightarrow(3,r)\) for every \(r\);
- one horizontal edge \(h^2_{pq}:(2,p)\leftrightarrow(2,q)\) and one \(h^3_{pq}:(3,p)\leftrightarrow(3,q)\) for every unordered \(\{p,q\}\subset R_k\);
- one square 2-cell \(F_{pq}\) with oriented boundary

\[
\partial F_{pq}=h^2_{pq}+v_q-h^3_{pq}-v_p.
\]

The numerical labels on its four corners are

\[
\begin{pmatrix}
2p&2q\\
3p&3q
\end{pmatrix},
\]

and satisfy

\[
(2p)(3q)=(2q)(3p).
\]

The equality is the rank-one determinant-zero identity. It is not counted as a new invariant.

### 2.2 Exact identification

Let the two vertices of \(I\) be labelled \(2,3\). Then the assignments

\[
(r,2)\mapsto(2,r),\qquad (r,3)\mapsto(3,r)
\]

and

\[
\{p,q\}\times I\mapsto F_{pq}
\]

identify the full CW structure with

\[
\boxed{X_k=K_k\times I.}
\]

This is an isomorphism of labelled incidence complexes, not merely a homotopy equivalence.

### 2.3 Closed formulas

Let \(N=\binom{k}{2}\). Then

\[
V_X=2k,
\]

\[
E_X=k+2N=k^2,
\]

\[
F_X=N.
\]

The 1-skeleton is connected and has cycle rank

\[
\beta_1(X_k^{(1)})=E_X-V_X+1=(k-1)^2.
\]

Attaching the \(N\) square faces leaves

\[
H_0(X_k;\mathbb Z)\cong\mathbb Z,
\]

\[
H_1(X_k;\mathbb Z)\cong
\mathbb Z^{N-k+1}
=\mathbb Z^{(k-1)(k-2)/2},
\]

\[
H_2(X_k;\mathbb Z)=0.
\]

Proof: projection \(K_k\times I\to K_k\) is a deformation retraction. Equivalently, the \(N\) square boundaries are independent in the 1-skeleton cycle space and kill exactly the product-square cycles, leaving the cycle space of the base \(K_k\).

The Euler characteristic is

\[
\chi(X_k)=V_X-E_X+F_X
=k-\binom{k}{2}
=\frac{k(3-k)}2.
\]

### 2.4 Incidence and boundary

- every horizontal edge \(h^c_{pq}\) belongs to exactly one square;
- every vertical edge \(v_r\) belongs to exactly \(k-1\) squares;
- the natural combinatorial boundary subcomplex is

\[
K_k\times\partial I.
\]

For \(k=3\), every vertical edge has two incident squares, so \(X_3\cong S^1\times I\) is an annulus.

For \(k\ge4\), every vertical edge has at least three incident squares. Therefore no neighborhood of an interior point of \(v_r\) is a half-disk or disk. Hence \(X_k\) is a branched 2-dimensional CW complex, not a surface.

This gives a precise boundary for the word `surface`.

---

## 3. Flat transport and loop classification

### 3.1 Natural carrier-preserving transport

For columns \(C_p,C_q\), define

\[
\tau_{p\to q}(cp)=cq,
\qquad c\in\{2,3\}.
\]

This is the unique transport preserving the declared carrier label \(c\).

For every triple \(p,q,r\),

\[
\tau_{q\to r}\circ\tau_{p\to q}=\tau_{p\to r}.
\]

Therefore every loop has identity transport.

At the numerical multiplier level, write

\[
\lambda_{pq}=\frac qp.
\]

Then

\[
\lambda_{pq}\lambda_{qr}=\lambda_{pr},
\]

and for every closed route

\[
p=r_0\to r_1\to\cdots\to r_m=p,
\]

\[
\prod_{i=0}^{m-1}\lambda_{r_i r_{i+1}}=1.
\]

Indeed \(\lambda_{pq}=\phi(q)/\phi(p)\) with \(\phi(r)=r\); the multiplicative 1-cocycle is exact.

Hence

\[
\boxed{\text{natural Seed-6 column holonomy is identically trivial}.}
\]

### 3.2 Path dependence

For any two base columns \(p,q\), every carrier-preserving composite along a path from \(p\) to \(q\) equals \(\tau_{p\to q}\). Thus the transport depends only on endpoints.

If the carrier labels \(2,3\) are deliberately forgotten, each two-point fiber has an abstract swap automorphism. One may then *choose* edgewise swaps and manufacture nontrivial \(C_2\)-holonomy. But no multiplicative datum in the present model selects such swaps. Therefore such a cocycle would be extra gauge data, not an intrinsic Seed-6 invariant.

Classification:

- carrier-preserving holonomy: `EXACT_STRUCTURAL / IDENTICALLY_TRIVIAL`;
- arbitrary unlabeled-fiber swap holonomy: `MODEL_DEPENDENT / EXTRA_DATA_REQUIRED`.

---

## 4. Model Y — numerical pairing-edge graph

### 4.1 Definition

For every pair \(p<q\) include the three product-equal pairings

\[
\{6,pq\},\qquad\{2p,3q\},\qquad\{2q,3p\}
\]

as graph edges between their numerical endpoints.

The vertex set is

\[
\{6\}\cup\{pq:p<q\}\cup\{2r:r\in R_k\}\cup\{3r:r\in R_k\}.
\]

### 4.2 Exact decomposition

The graph is the disjoint union of:

1. a star with center \(6\) and leaves \(pq\), one leaf for each pair \(p<q\);
2. the bipartite graph on
   \(A=\{2r:r\in R_k\}\) and
   \(B=\{3r:r\in R_k\}\),
   with every cross edge except \((2r,3r)\).

Thus the second component is exactly

\[
K_{k,k}\setminus M,
\]

where \(M\) is the diagonal perfect matching. This is a standard graph object; no novelty is claimed for the identification.

### 4.3 Exact counts

Again \(N=\binom{k}{2}\):

\[
V_Y=1+2k+N,
\]

\[
E_Y=3N,
\]

and for \(k\ge3\) there are exactly two connected components. Hence

\[
\beta_1(Y_k)
=E_Y-V_Y+2
=k^2-3k+1.
\]

The bipartite component has girth

\[
6\quad(k=3),
\qquad
4\quad(k\ge4).
\]

For the required concrete sample \(R_4=\{5,7,11,13\}\), a 4-cycle is

\[
10\to33\to14\to39\to10,
\]

that is

\[
2\cdot5\to3\cdot11\to2\cdot7\to3\cdot13\to2\cdot5.
\]

This is an incidence cycle, not a statement about numerical distance.

### 4.4 Important negative boundary

For each \(\{p,q\}\), the three edges above have the same endpoint-product \(6pq\), but **they are not three mutually adjacent state vertices in this numerical graph**. The common product gives a weight/fiber relation; it does not itself supply a switch edge or a global gluing law between the three pairings.

Therefore the numerical pairing graph alone cannot support a claim that the three pairings form a dynamical triangle.

---

## 5. Model Z — exact-support three-pairing cells

For each support

\[
S_{pq}=\{2,3,p,q\}
\]

let

\[
m^0_{pq}=\{\{2,3\},\{p,q\}\},
\]

\[
m^1_{pq}=\{\{2,p\},\{3,q\}\},
\]

\[
m^2_{pq}=\{\{2,q\},\{3,p\}\}.
\]

Make these three states the vertices of a filled triangular 2-cell.

Use the strict gluing rule:

> two state vertices are identified iff the exact perfect matchings, including prime support, are equal.

If \(\{p,q\}\ne\{u,v\}\), no matching state in the first cell equals a matching state in the second. Consequently the global complex is a disjoint union of \(N\) filled triangles.

Therefore

\[
V_Z=3N,
\quad
E_Z=3N,
\quad
F_Z=N,
\]

\[
\#\pi_0(Z_k)=N,
\qquad
H_1(Z_k)=H_2(Z_k)=0.
\]

Within one support, a two-switch route and a direct switch can be different edge paths, but the filled triangle gives the standard homotopy between them. If only the final matching state is observed, endpoint state is path independent. Across supports there is no gluing from which a global holonomy could arise.

Thus the exact three-pairing cell is a valid **local** object, but exact-support equality does not turn the family into a global surface.

---

## 6. Model Q — support-erasing quotient and the false-H2 test

To test whether a visually attractive global topology can be manufactured by over-gluing, quotient Model Z by forgetting \(p,q\) completely and identifying every state only by abstract pairing type:

\[
m^0_{pq}\sim t_0,
\qquad
m^1_{pq}\sim t_1,
\qquad
m^2_{pq}\sim t_2.
\]

Keep all \(N\) 2-cells distinct. Then every 2-cell is attached along the same triangle boundary.

Thus

\[
V_Q=3,
\quad E_Q=3,
\quad F_Q=N.
\]

The boundary map

\[
\partial_2:\mathbb Z^N\to\mathbb Z^3
\]

has rank one because every oriented face has the same boundary. Therefore

\[
H_1(Q_k)=0,
\]

\[
H_2(Q_k)\cong\mathbb Z^{N-1}.
\]

For example, already with supports \(\{5,7\}\) and \(\{5,11\}\),

\[
F_{5,7}-F_{5,11}
\]

is a nonzero 2-cycle in the quotient.

At \(k=50\), this quotient produces

\[
\beta_2=\binom{50}{2}-1=1224.
\]

But this homology appears only because different prime supports were erased before gluing. Any operation that later needs to know which columns or primes participated does not descend through this quotient. In operation-safe quotient language, support erasure is legitimate only for a deliberately support-blind observable; it is not a free identification of the original multiplicative object.

Therefore:

\[
\boxed{\text{large }H_2\text{ after support erasure is quotient-induced pseudo-topology}.}
\]

This provides a useful falsification criterion for future bridge-surface proposals.

---

## 7. Candidate invariant audit

| Candidate | Verdict | Reason |
|---|---|---|
| \((2p)(3q)=(2q)(3p)\) / vanishing 2x2 determinant | `TAUTOLOGICAL` | exactly the rank-one outer-product identity |
| labelled carrier/index product incidence \((c,r)\) | `EXACT_STRUCTURAL` | gives a precise support-faithful object, but it is the standard product \(K_k\times I\) |
| square-face incidence and vertical-edge valence \(k-1\) | `EXACT_STRUCTURAL` | proves the annulus/branched-complex boundary exactly |
| base cycle rank \((k-1)(k-2)/2\) | `EXACT_STRUCTURAL / STANDARD_GRAPH` | survives square filling because \(X_k\simeq K_k\) |
| multiplicative transport \(\lambda_{pq}=q/p\) | `EXACT_STRUCTURAL / FLAT` | exact coboundary; all loop products are 1 |
| arbitrary unlabeled row-swap holonomy | `MODEL_DEPENDENT` | requires an additional edgewise swap choice not supplied by multiplication |
| cycles of the numeric pairing graph | `EXACT_STRUCTURAL / STANDARD_GRAPH` | star plus \(K_{k,k}\setminus M\) |
| global gluing of exact-support matching triangles | `COUNTEREXAMPLE_TO_SURFACE_GLUING` | cells are disjoint |
| \(H_2(Q_k)=\mathbb Z^{N-1}\) after support erasure | `MODEL_DEPENDENT / QUOTIENT_ARTIFACT` | created by identifying distinct supports |

No candidate found in this task gives a nontrivial intrinsic curvature or holonomy beyond standard graph/cell-complex structure.

---

## 8. Exact census, k=3,...,50

The exact checker enumerates the first \(k\) primes greater than 3 for every \(k=3,\ldots,50\), constructs the finite graphs/cells, and verifies the formulas with integer/rational arithmetic.

Selected rows:

| k | X: V,E,F | X beta1 | X beta2 | Y: V,E | Y beta1 | Y girth | Z components | Q beta2 |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| 3 | 6,9,3 | 1 | 0 | 10,9 | 1 | 6 | 3 | 2 |
| 4 | 8,16,6 | 3 | 0 | 15,18 | 5 | 4 | 6 | 5 |
| 5 | 10,25,10 | 6 | 0 | 21,30 | 11 | 4 | 10 | 9 |
| 10 | 20,100,45 | 36 | 0 | 66,135 | 71 | 4 | 45 | 44 |
| 50 | 100,2500,1225 | 1176 | 0 | 1326,3675 | 2351 | 4 | 1225 | 1224 |

Machine-readable full census:

`research_artifacts/SEED6_BRIDGE_SURFACE_GLOBAL_GLUING/census_k3_k50.csv`

Exact checker:

`research_checks/SEED6_BRIDGE_SURFACE_GLOBAL_GLUING_CHECK_20260829.py`

Checker terminal output:

```text
PASS RS-SEED6-BRIDGE-SURFACE-GLOBAL-GLUING k=3..50
```

The census is a regression certificate only; the classifications above are proved by exact formulas and isomorphisms, not inferred statistically.

---

## 9. Minimal legal global interface

### `SEED6_BRIDGE_COMPLEX_V1`

For a finite support set \(R\) of distinct primes greater than 3, define:

1. base graph \(B_R=K_R\);
2. carrier fiber \(F=\{2,3\}\) with declared labels;
3. vertex set \(F\times R\), labelled numerically by
   \(\ell(c,r)=cr\);
4. one vertical carrier edge over every \(r\);
5. for every base edge \(\{p,q\}\), one horizontal edge in each carrier row and one square product cell;
6. projection
   \(\pi:X_R\to B_R\);
7. carrier-preserving transport
   \(\tau_{p\to q}(cp)=cq\).

Exact structural law:

\[
X_R\cong K_R\times I.
\]

Flatness law:

\[
\tau_{q\to r}\tau_{p\to q}=\tau_{p\to r}.
\]

Naming rule:

- \(|R|=3\): `bridge annulus` is literally valid;
- \(|R|\ge4\): use `bridge complex`, `column-square complex`, or `branched I-bundle`; do not call it a surface without qualification.

This interface does **not** predefine any future global topology beyond its exact incidence data.

---

## 10. Tool/method reuse and novelty boundary

Relevant existing Enterprise Math methods were reused rather than replaced:

- `T3_TYPED_INCIDENCE_CIRCUIT` for cycle/incidence classification;
- `T9_HOLONOMY_COCOYCLE_GLUING` for staged-vs-direct transport and loop flatness;
- `T6_OPERATION_SAFE_QUOTIENT` for the support-erasure audit.

No new general-purpose tool family is proposed.

Standard object identifications such as \(K_k\times I\), the cycle space of \(K_k\), and \(K_{k,k}\) minus a perfect matching are not claimed as novel mathematics. The task-level contribution is the exact classification of which of these structures the Seed-6 bridge data actually induces, plus the proof that nontrivial apparent \(H_2\) emerges only after a support-erasing quotient.

---

## 11. Handoff to sibling Seed-6 lanes

This return constrains, but does not preempt, the other parallel tasks:

- **local triangle lane:** any new local decoration may be attached to `SEED6_BRIDGE_COMPLEX_V1`, but absent extra decoration the global column transport is flat;
- **three-pairing orbit lane:** an internal three-state switch is additional matching-state structure; it is not already supplied by the numerical pairing graph;
- **degeneracy lane:** repeated atoms/support collisions can change exact-support gluing and therefore must be studied separately;
- **seed-specificity lane:** the product-complex proof suggests the bare two-carrier column-square construction is generic for a seed \(ab\); any genuine Seed-6 specificity must come from extra arithmetic decoration, not from the raw rank-one rectangle itself.

A future claim of nontrivial bridge curvature/topology should therefore exhibit an exact support-faithful decoration or transition law that survives these reductions. Merely drawing the rank-one rectangles, or erasing supports until 2-cycles appear, is insufficient.

---

## 12. Terminal disposition

Hard target `SEED6_BRIDGE_SURFACE_GLOBAL_GLUE_CLASSIFIED` is met.

Final task classification:

- `STANDARD_CELL_COMPLEX_REIDENTIFIED` — natural bridge rectangle gluing is exactly \(K_k\times I\);
- `GLOBAL_FLATNESS_PROVED` — canonical carrier-preserving transport has trivial holonomy and no path dependence;
- `MODEL_DEPENDENT_BOUNDARY` — support-erasing quotients can create large but non-intrinsic 2-homology.

The strongest preserved positive object is `SEED6_BRIDGE_COMPLEX_V1`; the strongest negative boundary is that **raw Seed-6 rank-one bridge rectangles alone do not generate a nontrivial global multiplicative surface geometry**.
