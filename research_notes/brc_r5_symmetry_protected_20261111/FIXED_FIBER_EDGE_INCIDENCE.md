# R5 — Exact fixed-fiber edge incidence via at most two stationary arcs

Date: 2026-11-11 (Asia/Shanghai). Status: exact linear-algebraic criterion, author-side proof; intended next computational unit following the 14832 circuit census in `RESEARCH.md`. Frozen science and all P000 commitments unchanged. Prior context: R5 PR #2045, #2038 and #2021.

## Definitions and scope

Let C be the frozen 21-by-30 Blackwell observation matrix of rank 15, with its 30 allowed transfer arcs. For a **fixed** right-hand side b in im C, define the nonnegative fiber F_b={x in R^30: Cx=b, x>=0}. A `sharp candidate` S is one of the 14832 observed 14-arc supports with rank(C_S)=13 and a unique nonzero kernel direction d supported on every element of S. This direction has both positive and negative coordinates because target-mass conservation makes every nonzero kernel vector sign-changing.

The **direction support** of an edge is the set S where its endpoint difference is nonzero. The **relative-interior support** U of that edge additionally includes arcs with strictly positive constant mass along the edge; write T=U\S.

The support-only test CE=b, supp(E) subset S is in general insufficient for deciding whether a direction S occurs as an edge in the given fixed fiber: actual endpoints may carry stationary positive arcs outside S. The previously proved physically legal length-four edge in PR #2038 has 14 nonzero direction arcs but union support 16.

## Theorem — exact edge-incidence equivalence

For a sharp 14-arc candidate S, its direction appears as an edge of F_b **if and only if** there exists a subset T of the 16 remaining arcs, with |T|<=2, such that

1. rank(C_{S union T}) = 13+|T| (i.e. each stationary arc is independent modulo span C_S); and
2. there exists x with C_{S union T} x=b and x_i>0 for every i in S union T.

Every such T yields exactly one edge with relative-interior support U=S union T; different T give different edges. Therefore an exhaustive incidence census for a fixed b requires at most C(16,0)+C(16,1)+C(16,2)=137 candidate lifts per S. For b outside the finite union of all spans of C_U with rank(C_U)<=14, only the 120 **two-stationary-arc** choices can be feasible.

### Proof

Take any actual edge of F_b with direction support S. Its relative interior has exactly U positive entries; all entries outside U vanish on the whole edge. Because the relative interior is strictly positive on U, the face of F_b with coordinates outside U set to zero is locally an affine space of dimension |U|-rank(C_U). It coincides with the minimal face containing the edge, hence has dimension 1. (Equivalently: an edge cannot lie in the strict interior of a higher-dimensional support face.) Thus nullity(C_U)=1.

S is a 14-column circuit with nullity(C_S)=1. Writing T=U\S and comparing ranks gives
```
1 = |S|+|T| - rank(C_U)
  = 14+|T| - rank(C_U),
rank(C_U)=13+|T|.
```
Since rank C=15, |T|<=2. Positivity of the edge relative interior proves the necessity of (2).

Conversely suppose (1) and (2) hold. The strictly positive solution x defines a nonempty one-dimensional face F_b[U]={y>=0: Cy=b, supp(y) subset U}, because its affine dimension equals one. The unique direction is the extension by zeros of d supported on S. Every nonzero kernel vector of C has both signs, so the line meets the nonnegative orthant in a **nondegenerate bounded segment** whose endpoints are distinct vertices and whose relative interior support is exactly U. This segment is an edge of F_b and its difference support is S. Distinct T yield distinct U and therefore distinct edges. QED.

## Exact two-dimensional quotient and one-interval certificate

Select any 15 independent rows D of C (same row space) so D has full row rank 15. The 15-by-14 restriction D_S has rank 13. Choose two rational independent left annihilators ell_1, ell_2 of D_S and write
```
q(z)=(ell_1*z,ell_2*z).
```
For a two-arc choice T={t1,t2}, a rank-15 lift occurs precisely when det(q(D_t1),q(D_t2)) !=0. The stationary arc masses (mu1,mu2) are the **unique exact rational** solution
```
[ q(D_t1)  q(D_t2) ] [mu1,mu2]^t = q(b_rows),
```
where b_rows denotes b restricted to the selected row coordinates.

An edge with this T exists iff mu1>0 and mu2>0 and the residual right-hand side b_rows-mu1*D_t1-mu2*D_t2 admits a strictly positive S-coordinate solution. Since the residual lies in span(D_S), solve
```
D_S*x0=b_rows-mu1*D_t1-mu2*D_t2.
```
Its complete solution set is x0+t*d. Because d has no zero coordinates on S, strict positivity is the **single exact rational interval test**
```
max_{i in S, d_i>0} (-x0_i/d_i)
    <
min_{i in S, d_i<0} (-x0_i/d_i).
```
The lower/upper bounds give both endpoint transfers, and the rank certificate gives vertexhood and adjacency.

For |T|=0 or 1, use the analogous quotient-zero or quotient-line membership test and the same one-dimensional positivity interval. A zero or one-stationary-arc lift necessarily has b in a proper subspace of the 15-dimensional observable image; this is why the generic fixed-b case uses exactly two stationary arcs. The **frozen physical b** has not yet been classified as generic, so a complete census should retain all 137 possibilities until lower-dimensional membership is explicitly ruled out.

## Numerical meaning, exact algorithm, and next step

The theorem is exact and does not need floating-point LP. For each of the 14832 S:

1. Form rational rank-13 D_S; cache its 2D annihilator basis and one full-support circuit vector d.
2. Check 0/1 stationary-arc quotient membership (at most 17 cases) and 120 pairs T via rational 2-by-2 determinants and solves.
3. On positive quotient solutions, perform one rational S-affine solve and the strict lower-vs-upper interval test.
4. Count feasible distinct (S,T) pairs and store exact endpoint witnesses (and explicit failed membership/rank/sign/interval reason for discarded pairs).

Total candidate pairs before cheap rank/positivity pruning: 14832*137=2,031,984, of which 14832*120=1,779,840 are two-arc pairs. A concrete implementation may precompute row-reduction maps and 2D quotient coordinates once per S to reduce full rational solves.

**Scientific frontier:** Theorem gives the correct finite exact decision problem for counting sharp length-four edge directions in the *single pinned physical fiber*. The actual resulting count and representative endpoints still require running this algorithm against the precise pinned physical b, rather than replacing it with an arbitrary observer fiber.

Mathematical status: proof at the declared linear-model level; independent review/formal Result pending.