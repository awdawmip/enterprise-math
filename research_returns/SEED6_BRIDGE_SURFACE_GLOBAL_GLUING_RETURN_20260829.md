# Seed-6 Bridge Surface Global Gluing — Research Return

Status: `TASK_TERMINAL_RETURN`

- Task-ID: `RS-SEED6-BRIDGE-SURFACE-GLOBAL-GLUING`
- Publication-ID: `TP2-3C47811A2BD4B67B28B8`
- Researcher-ID: `EM-S6G-76E296`
- Claim-ID: `S6G-3A124087`
- Execution branch: `research/seed6-bridge-surface-global-gluing-em-s6g-76e296`
- Execution base: `65d1cae115e648f5154a898cd3ba83a2a2b27223`
- Hard target: `SEED6_BRIDGE_SURFACE_GLOBAL_GLUE_CLASSIFIED`
- Verdict: `STANDARD_CELL_COMPLEX_REIDENTIFIED + GLOBAL_FLATNESS_PROVED + MODEL_DEPENDENT_BOUNDARY`

## 1. Main theorem

Let \(R_k=\{r_1,\dots,r_k\}\) be distinct primes \(>3\), and put
\(a_r=2r,\ b_r=3r,\ C_r=(a_r,b_r)\).

For every unordered pair \(\{p,q\}\subset R_k\), glue the bridge rectangle

\[
\begin{pmatrix}2p&2q\\3p&3q\end{pmatrix}
\]

along equal carrier/index vertices and equal carrier edges. The resulting support-faithful CW complex is exactly

\[
\boxed{X_k\cong K_k\times I}.
\]

Here \(K_k\) is the complete graph on the prime-column indices and \(I\) is the two-carrier interval with endpoints labelled \(2,3\). Hence the raw Seed-6 rank-one rectangles do not generate a new global surface geometry.

With \(N=\binom{k}{2}\),

\[
V_X=2k,\qquad E_X=k+2N=k^2,\qquad F_X=N.
\]

The 1-skeleton cycle rank is \((k-1)^2\). Since \(K_k\times I\) deformation retracts onto \(K_k\),

\[
H_0(X_k;\mathbb Z)=\mathbb Z,
\]

\[
H_1(X_k;\mathbb Z)\cong
\mathbb Z^{N-k+1}
=
\mathbb Z^{(k-1)(k-2)/2},
\]

\[
H_2(X_k;\mathbb Z)=0.
\]

The determinant/product identity

\[
(2p)(3q)=(2q)(3p)
\]

is exactly the rank-one outer-product identity and is classified `TAUTOLOGICAL`, not as a new invariant.

Every horizontal edge belongs to one square; every vertical carrier edge belongs to \(k-1\) squares. Therefore \(X_3\cong K_3\times I\cong S^1\times I\) is an annulus, while for \(k\ge4\) the vertical edges have valence at least three and \(X_k\) is a branched 2-complex, not a 2-manifold.

## 2. Flat transport / no intrinsic holonomy

Define the carrier-preserving column transport

\[
\tau_{p\to q}(cp)=cq,\qquad c\in\{2,3\}.
\]

Then for all \(p,q,r\),

\[
\tau_{q\to r}\circ\tau_{p\to q}=\tau_{p\to r}.
\]

Equivalently, the multiplicative transition factor

\[
\lambda_{pq}=q/p
\]

satisfies

\[
\lambda_{pq}\lambda_{qr}=\lambda_{pr},
\]

so every closed route has

\[
\prod \lambda=1.
\]

Indeed \(\lambda_{pq}=\phi(q)/\phi(p)\) with \(\phi(r)=r\); it is an exact multiplicative 1-coboundary. Thus natural carrier-preserving transport is path independent and has identically trivial holonomy.

If the carrier labels \(2,3\) are intentionally erased, an abstract two-point fiber admits a swap. Edgewise swap choices can manufacture a \(C_2\)-holonomy, but multiplication supplies no canonical choice of such swaps. Any such nontrivial holonomy is therefore `MODEL_DEPENDENT / EXTRA_DATA_REQUIRED`, not intrinsic Seed-6 geometry.

## 3. Model Y — numerical pairing-edge graph

Adjoin the three product-equal pairing edges for every \(p<q\):

\[
\{6,pq\},\qquad \{2p,3q\},\qquad \{2q,3p\}.
\]

The resulting graph decomposes exactly into two components:

1. a star with center \(6\) and leaves \(pq\);
2. \(K_{k,k}\) on \(A=\{2r\}\), \(B=\{3r\}\) with the diagonal perfect matching \((2r,3r)\) removed.

Thus

\[
V_Y=1+2k+N,\qquad E_Y=3N,
\]

and for \(k\ge3\),

\[
\beta_1(Y_k)=E_Y-V_Y+2=k^2-3k+1.
\]

The bipartite component has girth \(6\) for \(k=3\) and \(4\) for \(k\ge4\). For \(R_4=\{5,7,11,13\}\), one exact 4-cycle is

\[
10\to33\to14\to39\to10.
\]

This is an incidence cycle, not numerical-distance geometry.

Crucial boundary: the three equal-product pairings for one support are three graph edges, not three mutually adjacent pairing-state vertices. Common product alone does not create a re-pairing dynamics.

## 4. Model Z — exact-support matching cells

For each support \(S_{pq}=\{2,3,p,q\}\), take the three perfect matchings

\[
m^0_{pq}=\{\{2,3\},\{p,q\}\},
\]

\[
m^1_{pq}=\{\{2,p\},\{3,q\}\},
\]

\[
m^2_{pq}=\{\{2,q\},\{3,p\}\},
\]

and fill their triangle.

Glue two matching-state vertices only when the exact matching including prime support is equal. Distinct supports share no state, so the global object is a disjoint union of \(N\) filled triangles:

\[
V_Z=3N,\qquad E_Z=3N,\qquad F_Z=N,
\]

\[
\#\pi_0(Z_k)=N,\qquad H_1(Z_k)=H_2(Z_k)=0.
\]

Within one support, direct and two-switch paths have the same endpoint and are homotopic through the filled triangle; across supports there is no exact gluing. Therefore the local three-pairing cell is valid, but it does not itself form a global bridge surface.

## 5. Model Q — support-erasure falsification test

Now deliberately erase the support by identifying all \(m^0_{pq}\) to one type \(t_0\), all \(m^1_{pq}\) to \(t_1\), and all \(m^2_{pq}\) to \(t_2\), while retaining all \(N\) faces.

Then

\[
V_Q=3,\qquad E_Q=3,\qquad F_Q=N.
\]

All face boundaries coincide, so the boundary map \(\partial_2:\mathbb Z^N\to\mathbb Z^3\) has rank one. Hence

\[
H_1(Q_k)=0,\qquad
H_2(Q_k)\cong\mathbb Z^{N-1}.
\]

Already \(F_{5,7}-F_{5,11}\) is a nonzero quotient 2-cycle. At \(k=50\),

\[
\beta_2(Q_{50})=\binom{50}{2}-1=1224.
\]

This large \(H_2\) is created only after mathematically different prime supports are identified. Any future operation that needs the participating columns does not descend through this quotient. Therefore it is `MODEL_DEPENDENT / QUOTIENT_ARTIFACT`, and supplies a falsification test against pseudo-topology produced by over-gluing.

## 6. Exact census

The exact checker covers every \(k=3,\dots,50\) using integer/rational arithmetic. Selected rows:

| k | X \(V,E,F\) | X beta1 | X beta2 | Y \(V,E\) | Y beta1 | Y girth | Z components | Q beta2 |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| 3 | 6,9,3 | 1 | 0 | 10,9 | 1 | 6 | 3 | 2 |
| 4 | 8,16,6 | 3 | 0 | 15,18 | 5 | 4 | 6 | 5 |
| 5 | 10,25,10 | 6 | 0 | 21,30 | 11 | 4 | 10 | 9 |
| 10 | 20,100,45 | 36 | 0 | 66,135 | 71 | 4 | 45 | 44 |
| 50 | 100,2500,1225 | 1176 | 0 | 1326,3675 | 2351 | 4 | 1225 | 1224 |

Checker:

`research_checks/SEED6_BRIDGE_SURFACE_GLOBAL_GLUING_CHECK_20260829.py`

Full machine-readable census:

`research_artifacts/SEED6_BRIDGE_SURFACE_GLOBAL_GLUING/census_k3_k50.csv`

Checker verdict:

```text
PASS RS-SEED6-BRIDGE-SURFACE-GLOBAL-GLUING k=3..50
```

Finite census is a regression certificate only; the classification is proved by the exact isomorphisms and formulas above.

## 7. Invariant audit

| Candidate | Classification |
|---|---|
| rank-one product equality / zero determinant | `TAUTOLOGICAL` |
| carrier/index incidence \((c,r)\) | `EXACT_STRUCTURAL / STANDARD_PRODUCT` |
| vertical-edge valence \(k-1\) | `EXACT_STRUCTURAL` |
| surviving base cycle rank \((k-1)(k-2)/2\) | `EXACT_STRUCTURAL / STANDARD_GRAPH` |
| \(\lambda_{pq}=q/p\) transport | `EXACT_STRUCTURAL / FLAT` |
| unlabeled swap holonomy | `MODEL_DEPENDENT / EXTRA_DATA_REQUIRED` |
| numerical pairing graph cycles | `EXACT_STRUCTURAL / STANDARD_GRAPH` |
| exact-support matching-cell global surface | `COUNTEREXAMPLE_FOUND` |
| support-erased \(H_2\) | `MODEL_DEPENDENT / QUOTIENT_ARTIFACT` |

Relevant existing Enterprise tools were reused: `T3_TYPED_INCIDENCE_CIRCUIT`, `T9_HOLONOMY_COCOYCLE_GLUING`, and `T6_OPERATION_SAFE_QUOTIENT`. No new general-purpose tool family is proposed.

## 8. Minimal legal interface

Define `SEED6_BRIDGE_COMPLEX_V1(R)` by:

- base \(K_R\);
- carrier fiber \(\{2,3\}\);
- vertices \((c,r)\) with numerical label \(cr\);
- vertical carrier edges;
- two horizontal carrier-row edges and one square over every base edge;
- projection to \(K_R\);
- carrier-preserving transport \(\tau_{p\to q}\).

Exact laws:

\[
SEED6\_BRIDGE\_COMPLEX\_V1(R)\cong K_R\times I,
\]

\[
\tau_{q\to r}\tau_{p\to q}=\tau_{p\to r}.
\]

Naming boundary:

- \(|R|=3\): `bridge annulus` is literal;
- \(|R|\ge4\): use `bridge complex`, `column-square complex`, or `branched I-bundle`, not an unqualified surface.

## 9. Handoff and terminal disposition

This result does not preempt the sibling Seed-6 tasks. It constrains them:

- a local-triangle decoration can enrich the product complex, but raw column transport is flat;
- a three-pairing switch is additional matching-state structure, not already present in the numerical pairing graph;
- degeneracies may change exact-support gluing and must be handled separately;
- bare \(ab\)-seed rank-one rectangles are expected to share the same product-complex skeleton, so any Seed-6 specificity must come from additional arithmetic decoration.

Hard target `SEED6_BRIDGE_SURFACE_GLOBAL_GLUE_CLASSIFIED` is met.

The strongest positive object is `SEED6_BRIDGE_COMPLEX_V1`. The strongest negative boundary is:

\[
\boxed{\text{raw Seed-6 rank-one bridge rectangles alone do not produce nontrivial global multiplicative surface curvature or holonomy}.}
\]

No factorization target, endpoint recovery, additive-distance geometry, or performance claim is introduced.
