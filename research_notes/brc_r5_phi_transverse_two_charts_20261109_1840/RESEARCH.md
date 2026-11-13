# R5: Exact two-chart 14-edge Blackwell feasibility across a physical face

Date: 2026-11-09 (Asia/Shanghai). Research status: AUTHOR_DERIVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED.

## Source and frozen model

Continues the frozen seven-likelihood-ratio P/Q-BRC **auxiliary statistical observer** of PR #1859 (immutable commit `f63a0250714f2445e8b406754b85f26d983ec3a6`), with P's 13-edge transport and affine physical maps, as developed through PR #1866. Scientific pins unchanged: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Current behavioral policy was loaded independently. The auxiliary 7-node model does not modify P000 six-native-space-plus-independent-time ontology.

The ordered physical flows (g,a,b,u,v,w,z), LR values and stopping times are:
```text
X = (999/1000, 1/6, 999/1000, 1/20, 29/240, 11/160, 1/120)
Y = (1, 2002911/10904720, 26095487/40892700,
     442758619/6542832000, 11037627/68154500,
     394502727/2180944000, 2002911/109047200)
r = (1/10, 1/2, 3/4, 1, 5/4, 3/2, 19/10)
```
The canonical seven-component marginal map `M(f)`, two stopping-time maps and 13 physical capacity slacks are given verbatim as executable rational formulas in `VERIFY.py`. `Y` is on the seedless F face: slack indices 6,10,12 are zero. `X` has g=b and hence source mass nu_4=0. The frozen P transport's 13 strictly positive entries are listed in the verifier. Legal E_(i,j)>=0 must satisfy the 21 linear row, column and LR-moment equations: sum_j E_(i,j)=mu_i=M(Y)_i, sum_i E_(i,j)=nu_j=M(X)_j and sum_i r_i E_(i,j)=r_j nu_j. The zero column 4 and LR-extreme columns 0 and 6 leave the same 30 candidate edges as PR #1859.

## Theorem: complete one-dimensional physical feasibility classification

Define
```text
D = (2502928, -18774008, 2502928, 6045767, -1139688, 726533, 0) / 1477565
X(theta) = X + theta*D
L = -295513/24183068
theta0 = 219439/545236000
U = 295513/500585600
```
with the target Y fixed. For **all real theta**, X(theta) is physically legal and keeps g=b precisely on [L,U]. Both stopping times match the fixed Y throughout [L,U]. For every lawful source/target pair on this entire interval,

**Blackwell feasibility holds if and only if theta >= 0.**

For all 0<=theta<=U, an explicit **at most 14-positive-edge** nonnegative Blackwell matrix is given by the two affine charts below. The point theta=0 has 13 edges; theta=theta0 has 13 edges; each other positive parameter has exactly 14. Both 14-column carrier matrices have exact rank 14.

### Proof 1 — exact physical and observable directions

Direct substitution into the frozen marginal map gives

```text
M(X(theta)) = M(X) + theta*(2, -41/5, 36/5, 0, 0, -1, 0).
```
The mass derivative sums to zero; g=b is preserved since D_g=D_b. Both stop-time directional derivatives vanish. Every physical source capacity slack is affine in theta. Taking all 13 lower/upper bounds yields exactly [L,U]: the lower endpoint saturates source slack index 5 (u>=0); the upper endpoint saturates slack index 2 (1-g>=0). The target's seedless F-face equalities and physical capacities remain fixed. These conclusions cover real and irrational theta by affine identities and endpoint inequalities.

Reuse the PR #1859 linear dual functional
```text
Phi(mu,nu) = (23/5)*(mu0-nu0) + 3*(mu1-nu1)
             + 2*(mu2-nu2) + (mu3-nu3).
```
Substitution gives the **exact transverse coordinate** Phi(M(Y),M(X(theta)))=theta. Each of the 30 permitted edge columns has nonnegative Phi price; the edge (5,1) has price 1. In any nonnegative legal E, Phi is the sum of these prices weighted by edge mass, so Phi>=0. Therefore every lawful theta<0 is Blackwell **infeasible**, independently of any proposed sparse support.

### Proof 2 — chart A, 0<=theta<=theta0

Let P be the frozen 13-edge coupling of PR #1859 and let E_A(theta)=P+theta H_A. The **complete** nonzero entries of H_A are:

| edge | H_A coefficient |
|---|---:|
| (0,0) | 2 |
| (0,1) | -118/23 |
| (4,1) | -468/115 |
| (0,2) | 72/23 |
| (4,2) | 468/115 |
| (5,5) | -1 |
| (5,1) | 1 |

The 7 target-row increments vanish; the 7 source-column increments equal (2,-41/5,36/5,0,0,-1,0); and the 7 LR-column increments equal that vector multiplied componentwise by the source r_j. Thus all 21 equations hold identically for every real theta. The first original P edge to reach zero is

```text
E_A(5,5)(theta) = 219439/545236000 - theta.
```
All other original P edges are strictly positive at both endpoints. The newly introduced (5,1) mass equals theta. By affine nonnegativity E_A is valid throughout [0,theta0]; it has 13 positive edges at its endpoints and 14 inside.

### Proof 3 — pivot and chart B, theta0<=theta<=U

At theta0 put P0=E_A(theta0). This is a legal 13-positive-edge coupling with (5,5)=0 and (5,1)>0. Let s=theta-theta0 and E_B(theta)=P0+s H_B. Complete nonzero coefficients:

| edge | H_B coefficient |
|---|---:|
| (0,0) | 2 |
| (0,1) | -123/23 |
| (4,1) | -328/115 |
| (0,2) | 72/23 |
| (4,2) | 468/115 |
| (0,3) | 5/23 |
| (3,3) | -1 |
| (4,3) | 18/23 |
| (4,5) | -2 |
| (3,5) | 1 |

Again all 7 row derivatives are zero; all 7 column and 7 LR-moment derivatives match X(theta). Exact endpoint nonnegativity and 21 equalities hold at theta0 and U, hence for the entire real interval. E_B keeps (5,5)=0 and grows the new (3,5) edge by s. At theta0 it is exactly P0; for theta0<theta<=U precisely 14 edges have positive mass. At U, the source physical boundary 1-g=0 is reached with all 14 chart-B edges positive. The two support matrices each have full column rank 14 (Fraction elimination in the verifier).

Combining Phi<0 exclusion on [L,0) and the two explicit positive-side transports on [0,U] proves the stated **iff** on every physically legal pair of this chosen one-dimensional family. The first chart's sharp endpoint is specific to its support: another 14-edge chart carries feasibility through the full physical upper bound.

## Exact verification, scope and next unit

`VERIFY.py` uses only Python standard-library Fraction. It checks physical slacks and their sharp bounds, both stopping times, mass normalization, the F face, all 30 Phi dual prices, exact Phi=theta, all 21 equations, carrier cardinalities/ranks and strict positivity at the defining endpoints. `EXACT_OUTPUT.txt` records the local successful execution. Affineness supplies the proof for every real parameter between those endpoints.

This is a constructive feasibility boundary and a two-chart 14-edge cover for **one fixed target and a complete physical source line**, not yet a uniform 14-edge theorem over every physical g=b pair. The next research unit is to thicken the source line into a positive-dimensional transverse physical neighborhood, constructing new pivot charts or an exact minimal 15-edge certificate if it exists. All theorem admission and active task ownership remain governed by separate current Source records.
