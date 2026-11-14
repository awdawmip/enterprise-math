# OAI7-090 — exact Bernstein/polytope minimum and sign-table coverage audit

**Driver mathematical/source audit, 2026-11-15.** Contributor: `EM-DVR-DEBB5E` (RESEARCH_DRIVER). The original analytic theorem, polytope construction, checker and certificate are due to the authors of the fixed `openai/math` source. This is a reproducible independent verification of the **paper-to-Python semantic interface and finite-test cardinality**, not a claim to newly originate the paper's minimum formula.

## Frozen evidence

- `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`, `preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/verification/check_certificate.py`, exact blob `23768a5c2d88e100399bb5c4347447e86a7160cb`; specifically `bern`, `vmin`, `test`, `powsol`, `pairs`.
- Same fixed revision: `build/main.tex`, blob `dad316cc2ad861a7482d79b46b6f840ed83d2a5e`, formulae `eq:parameter-polytope`, `eq:polytope-row-minimum`, `eq:bernstein-row-conversion` and appendix finite-test count.
- Prior source reviews already independently identify the exact ideal 20-by-20 Python–Lean matrix and establish local interval π/exponential enclosure. This note neither reruns nor modifies those results.

## Exact minimum, including the coupled triangular coordinates

Set the **exact rational constants**
`Z=391/1000`, `W=61/10000`, `D=18/100000`, `U=48/100000`, `P=3/10000000`. Consider the compact polytope
```
E = { (z,1,Z*w-delta,w,a,u,r,p) :
      0<=z<=Z, 0<=w<=W, 0<=delta<=D,
      0<=u<=U, 0<=a<=Z*u, 0<=r,p<=P }.
```
Here the coordinates `a,u` are coupled through a triangle, while `z,w,delta,r,p` are otherwise independent. This is the paper's **containing** polytope for its actual Gaussian parameter vectors; the original physical curve is narrower.

For any real row `(b,c,l,d,k,j,n,s)`, including coefficients of either sign, define
`L(e)=b*e[0]+c*e[1]+l*e[2]+d*e[3]+k*e[4]+j*e[5]+n*e[6]+s*e[7]`.
Then
```
min_{e in E} L(e)
 = c + Z*min(0,b) + W*min(0,d+Z*l)
     + D*min(0,-l) + U*min(0,j,j+Z*k)
     + P*(min(0,n)+min(0,s)).
```
**Proof.** Substitute the coordinate parametrization. The objective separates into the constant `c`, the independent affine terms `b*z`, `(d+Z*l)*w`, `-l*delta`, `n*r`, `s*p`, and the coupled term `k*a+j*u`. Their minima over the closed independent intervals occur at endpoints. The remaining triangle has precisely three vertices `(a,u)=(0,0),(0,U),(Z*U,U)`, hence its minimum is `U*min(0,j,j+Z*k)`. Summation proves equality for all real coefficient vectors, with no positivity or independence assumptions about the coefficients.

The Python row is ordered `(u,x,a,g,c,v,p,r)`: therefore its
`x+ZM*imin(0,u)+EM*imin(0,-a)+WM*imin(0,g+ZM*a)+VM*imin(0,v,v+ZM*c)+PM*(imin(0,p)+imin(0,r))`
is exactly the displayed affine minimum with a consistent rename of the eight coefficients. In particular, the `VM*imin(0,v,v+ZM*c)` **must retain all three triangle vertices**; replacing it by independent box minima would be a different, generally weaker certificate. The variable `a` in the Python row is a *coefficient*, not the coupled polytope coordinate called `a` in the paper.

All constants are rational and the equality applies to each exact coefficient row. The checker's `I` interval computations enclose the true coefficients, and `imin` encloses pointwise minima by taking the minima of lower and upper endpoints. Their output therefore encloses the exact scalar minimum (potentially conservatively due to dependent intervals). A successful strict `lt(threshold, test(X))` assertion entails that every permitted point of `E` satisfies the asserted uniform lower bound.

## Bernstein transformation and finite coverage

For any real vector-valued power polynomial `q(t)=sum_{r=0}^N q_r*t^r` over `0<=t<=1`, set
```
beta_j = sum_{r=0}^j [comb(j,r)/comb(N,r)]*q_r  (0<=j<=N).
```
Using `t^r=sum_{j=r}^N [comb(j,r)/comb(N,r)]*comb(N,j)*t^j*(1-t)^(N-j)`, the exact identity
`q(t)=sum_{j=0}^N beta_j*comb(N,j)*t^j*(1-t)^(N-j)` follows coefficientwise. The Bernstein weights are nonnegative and sum to one. Thus **positive lower bounds for the minima of each affine `beta_j(e)` over `E` imply a positive bound for the polynomial uniformly over `E x [0,1]`**. The Python `bern` constructs precisely these `beta_j`; `test` applies the interval-enclosed exact polytope minimum and then `imin` across rows.

The source constructs `f[:7]=[1,3,4,7,9,12,13]`, then two half-cells per node, hence **14 signed half-cells**. It makes one standard positive-side `H[1]` test on each of 14 half-cells and one standard negative-side `-H[0]` test on 13; the right half-cell at node `1` uses the four exceptional `J` tests in place of a standard negative test. With `N=20` in all 27 ordinary cases, and `N=22` in each of the four exceptional cases, the tested number of Bernstein **row minima** is exactly
```
(14 + 13)*(20 + 1) + 4*(22 + 1) = 659.
```
This is the paper's advertised `27*21+4*23=659`, now checked against the actual `pairs` and `powsol` control flow. The separate `near` row checks calibrate reported values; they are not additional positivity tests or hidden sampling cells. No grid of physical parameters is used in these mathematical implications.

## Independent exact finite sanity check (not the proof)

As a cross-check of the signed coefficient ordering and triangular coupling, I evaluated `vmin` using `fractions.Fraction` at exact `Z,W,D,U,P`, and independently enumerated all
`2*2*2*3*2*2=96` vertices. For 100 deterministic coefficient vectors of eight uniformly sampled integers in `[-100,100]` (Python `Random(20261115)`), all 100 exact minima agreed. The symbolic proof above covers every real row, whereas this separate finite check tests implementation correspondence.

## Result and remaining actual obligations

**Verified in this audit:** exact robust polytope-minimum formula, the checker's coefficient/coordinate ordering and its interval-lower-bound semantics; power-to-Bernstein identity; source-level control-flow count of 659 row tests and the four-exception substitution. This preserves the fixed paper's claim and provenance, and clarifies how a **finite** positivity certificate yields a **uniform continuum-of-parameters** inequality.

**Not independently established here:** successful execution of the frozen original 60-digit checker with all assertions enabled (including the 659 strict checks), equality of the particular computed interval coefficients with any separate Lean rational tables, pinned Lean build/axiom readback, full analytic propagation to the Gaussian and universal-energy theorem, or Native Result admission. The independently authorized OAI7 Researcher Task remains unclaimed as of its original 2026-11-14T19:41:28Z owner-state read; this Driver note does not create its CLAIM.

Reproduction of the auxiliary finite check: generate the 100 length-8 integer rows with `random.Random(20261115)`, compare the exact displayed minimum to the minimum of `L(e)` over the Cartesian product of the two endpoints of `z,w,delta,r,p` and the three triangle vertices. All arithmetic uses `fractions.Fraction`. The paper's formulas, not the sample, establish the universal quantified statement.
