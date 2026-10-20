# R040 — Polygonal Refinement Asymptotic Coding: Branch Geometry, Arithmetic Phase, and Limit Support

Status: `L2 SEMANTIC CHECKPOINT / EXECUTABLE_CHECKED / NOT CANONICAL`

Researcher-ID: `EM-R040-09A7B7`

Source base: `enterprise-math@ef6cafcde36d82808838a6a1d8cf1a2ed837a312`

Return classification:

`POLYGONAL_TWO_AXIS_ONTOLOGY_REPLACED / SMALLER_UNIFIED_CODING_OBJECT_FOUND / NOT_CANONICAL`

## 1. Disposition

R040 kills the proposed `branch geometry × arithmetic coding` picture **as a primitive ontology**. The two coordinates remain useful projections, but both factor through one smaller exact carrier on the polygonal discriminant lattice.

Set

\[
a=s-2,\qquad c=s-4,\qquad P_s(k)=\frac{ak^2-ck}{2},\qquad z_k=2ak-c,
\]
so
\[
z_k^2=c^2+8aP_s(k).
\]
Let
\[
B=(r-1)c^2,\qquad \Lambda_s=2a\mathbf Z-c.
\]
Then endpoint collapse is exactly the bracketing, in the affine lattice `Lambda_s`, of
\[
W(z)=\sqrt{rz^2-B}.
\]
Equivalently the exact real inverse is
\[
\Phi_{s,r}(k)=\frac{c+\sqrt{rz_k^2-B}}{2a}.
\]
The same rounded nonlinear dilation controls parent overlap, lower-jump coding, square affine stabilization, nonsquare defects, Pell exact hits, cardinality loss, and normalized limit support.

The replacement object is therefore

\[
\boxed{(\Lambda_s,\; z\mapsto \operatorname{bracket}_{\Lambda_s}\sqrt{rz^2-B})}.
\]

## 2. Provenance

Frozen R035 shared input: discriminant coordinate, `r=4` critical structure, universal singleton-root interval iff `r<=4`, exact `r=4` children, and generalized-Pell exact-hit surface.

`R035_PROJECT_ARM`: ordered lower map/local collision law, exact finite-support loss accounting, no distinct-parent recoalescence iff `r=1` or `r>=4`, interval/separated carriers, eventual jump restriction near `sqrt(r)`.

`R035_ISOLATED_ARM`: square `r=q^2,s!=4` eventual affine two-child law, stable base-`q` `{0,1}` supports, `q=2` interval versus `q>=3` sparse digit geometry, `s=4` rounded dilation, high-index separation for `r>=5`.

`R040_NEW`: exact inverse asymptotics, closed square offset and exact linear threshold, nonsquare Pell-strip trichotomy, mechanical coboundary formula, explicit non-Sturmian witness, continued-fraction boundary/counterexample, uniform normalized branch-limit theorem, nonsquare separated positive binary-entropy growth, finite bound on consecutive exact-hit runs, and the coupling witness replacing the proposed two-axis ontology.

Generic generalized-Pell existence/recurrence is treated as prior art, not project novelty.

## 3. Exact asymptotics

Write `alpha=sqrt(r)` and
\[
\beta=\frac{c(1-\alpha)}{2a}.
\]
For `z=z_k -> infinity`,
\[
\sqrt{rz^2-B}=\alpha z-\frac{B}{2\alpha z}-\frac{B^2}{8\alpha^3z^3}+O(z^{-5}),
\]
therefore
\[
\boxed{\Phi(k)=\alpha k+\beta-\frac{B}{4a\alpha z_k}-\frac{B^2}{16a\alpha^3z_k^3}+O(z_k^{-5}).}
\]
The first correction in `k` is
\[
-\frac{B}{8a^2\alpha}\frac1k.
\]
Degenerate cases are exact: `r=1 => Phi(k)=k`; `s=4 => c=B=0 => Phi(k)=sqrt(r)k`.

The analytic expansion does not itself split square/nonsquare `r`; the split occurs when the negative `O(1/k)` curvature is compared with the arithmetic phase of `alpha k+beta`.

## 4. Square refinement sharpened

Assume `r=q^2`, `q>=2`, `s!=4`. Because the curvature tends to zero from below, the eventual lower-child offset is
\[
\boxed{d=\lceil\beta\rceil-1.}
\]
For integer `j`, define
\[
\Delta_j(k)=q^2P_s(k)-P_s(qk+j).
\]
Quadratic terms cancel:
\[
2\Delta_j(k)=L_jk+C_j,
\]
with
\[
L_j=q(c(1-q)-2aj),\qquad C_j=j(c-aj).
\]
For `d=ceil(beta)-1`, `L_d>0` and `L_{d+1}<=0`. The stable pair
\[
E_s(q^2P_s(k))=\{qk+d,qk+d+1\}
\]
holds exactly when
\[
L_dk+C_d>0,\qquad L_{d+1}k+C_{d+1}<0,\qquad qk+d\ge0.
\]
Thus the minimal stable threshold is the maximum of explicit integer linear-inequality thresholds. A forward-invariant threshold is
\[
K^\to=\max\left(K,\left\lceil\frac{-d}{q-1}\right\rceil\right).
\]

Square exact hits for `c!=0` are finite because target discriminant `y` satisfies
\[
(qz-y)(qz+y)=(q^2-1)c^2,
\]
a fixed nonzero factorization problem. For `s=4`, the right side degenerates to zero and every positive parent is an exact hit: `k -> qk`.

From a singleton `k_0>=K^to`,
\[
S_t=q^tk_0+d\frac{q^t-1}{q-1}+
\left\{\sum_{j=0}^{t-1}\epsilon_jq^j:\epsilon_j\in\{0,1\}\right\},
\]
so `|S_t|=2^t` exactly. The normalized limit is
\[
K_q=\left\{\sum_{j\ge1}\epsilon_jq^{-j}:\epsilon_j\in\{0,1\}\right\}.
\]
`q=2` gives `[0,1]`; `q>=3` gives the strongly separated two-digit deleted-digit set with dimension `log 2/log q`.

## 5. Nonsquare Pell-strip theorem

Assume nonsquare `r` and `c!=0`. Define the mechanical baseline
\[
G(k)=\left\lfloor\sqrt r\,k+\beta\right\rfloor,
\qquad y_k=2aG(k)-c\in\Lambda_s,
\]
and the live Pell norm
\[
\boxed{N_k=rz_k^2-y_k^2>0.}
\]
Since
\[
\sqrt r\,z-\sqrt{rz^2-B}=\frac{B}{\sqrt r\,z+\sqrt{rz^2-B}},
\]
there is an explicit integer threshold above which the nonlinear target can cross at most one lattice step below the linear baseline. There the endpoint decision is exactly
\[
\boxed{
\begin{array}{rcl}
0<N_k<B&\Rightarrow&E=\{G-1,G\},\\
N_k=B&\Rightarrow&E=\{G\}\quad\text{(exact hit)},\\
N_k>B&\Rightarrow&E=\{G,G+1\}.
\end{array}}
\]
This is the central R040 theorem: mechanical defects are the **interior** `0<N<B` of a finite Pell-norm strip; exact hits are the **boundary** `N=B`.

All legal states retain the lattice congruence
\[
y,z\equiv-c\pmod{2a},
\]
so the active arithmetic object is not merely `sqrt(r)` but the norm class together with the affine-lattice residue.

## 6. Exact lower word as a Pell coboundary

Let
\[
h_k=G(k)-F(k),\qquad b_k=G(k+1)-G(k),\qquad d_k=F(k+1)-F(k).
\]
Then identically
\[
\boxed{d_k=b_k+h_k-h_{k+1}.}
\]
In the stable nonsquare regime,
\[
h_k=1\iff 0<N_k<B,
\]
and otherwise `h_k=0`, including the exact-hit boundary. Therefore for every interval `[u,v]`,
\[
\sum_{k=u}^v(d_k-b_k)=h_u-h_{v+1},
\]
so cumulative deviation from the mechanical baseline is bounded by one after stabilization.

For a fixed interior norm `N`, defects solve
\[
y^2-rz^2=-N,
\qquad y,z\equiv-c\pmod{2a}.
\]
If one positive residue-compatible stable solution exists, a suitable power of a Pell unit is congruent to the identity modulo `2a`, so that orbit yields infinitely many defects. Since only finitely many norm classes `1<=N<B` exist and each orbit grows exponentially, the ambient defect count is `O(log K)` up to index `K`, hence zero density.

The exact lower word need not remain Sturmian. At `(s,r)=(8,8)`, length-six factors `011110` and `111111` occur in the binary jump coding, with one-counts 4 and 6; this violates Sturmian 1-balance.

## 7. Continued fractions: useful but not complete

For a fixed norm class,
\[
\sqrt r-\frac yz=\frac{N}{z^2(\sqrt r+y/z)}.
\]
When the fixed norm is small enough, sufficiently large solutions satisfy the classical convergent approximation criterion, so principal continued-fraction convergents control part of the Pell skeleton.

They do not enumerate every defect. Exact witness:
\[
(s,r,k)=(9,10,11),\qquad (y,z,N)=(471,149,169),
\]
and `471/149` is not a principal convergent of `sqrt(10)` within the exact checked prefix. Continued fractions are therefore a diagnostic/generative coordinate, not the complete defect state.

## 8. Minimal coupling witness: same coarse axes, different coding

Take `r=10`. Both cells have `sqrt(10)>2` (separated-parent geometry) and irrational square root (nonsquare arithmetic).

For `s=3`, `a=1,c=-1,B=9,Lambda=2Z+1`. At `k=18`,
\[
z=37,\quad G=58,\quad y=117,\quad N=10\cdot37^2-117^2=1,
\]
so `0<N<B`, and
\[
E(18)=\{57,58\}.
\]
Moreover `117^2-10*37^2=-1`; multiplying by `19+6sqrt(10)` preserves odd residue classes and generates an infinite defect orbit.

For `s=5`, `a=3,c=1,B=9,Lambda=6Z-1`. Legal `y,z` are `-1 mod 6`, hence
\[
y^2\equiv z^2\equiv1\pmod{12},\qquad N=10z^2-y^2\equiv9\pmod{12}.
\]
But a defect would require `0<N<9`, impossible. The exact stable threshold is `K=1`, so every positive lower decision is mechanical.

Thus the proposed two coarse axes do not reconstruct the exact word. Their missing invariant is the discriminant-lattice modulus/residue interacting with the Pell norm strip. Because the old axes themselves are derived from the same rounded-lattice map, R040 selects Outcome C, not merely a patched two-axis atlas.

## 9. Exact-hit process and support growth

Let
\[
\mathcal H_{s,r}=\{k\ge1:rP_s(k)\in P_s(\mathbf N)\}.
\]
Checkpoint classification:

- `r=1`: all positive parents hit;
- `s=4`, square `r`: all positive parents hit;
- `s=4`, nonsquare `r`: no positive hits;
- `s!=4`, square `r`: finitely many hits by the fixed factorization above;
- `s!=4`, nonsquare `r`: **empty or infinite**. One compatible positive Pell/residue orbit implies infinitely many hits, but an admissible orbit may be absent.

Exact hits are not mechanical defects: they are `N=B`, not `0<N<B`.

If `c!=0`, consecutive exact hits cannot continue arbitrarily long. Two consecutive hits imply a fixed factorization
\[
(rz_t-z_{t+2})(rz_t+z_{t+2})=(r+1)B,
\]
so only finitely many starting discriminants can begin a consecutive pair; exact transitions strictly increase polygonal value, excluding an exact cycle. Hence each fixed `(s,r)` has a finite global bound on consecutive exact-hit run length.

For `r>=4`, R035 distinct-parent separation gives the exact recursion
\[
\boxed{|S_{t+1}|=2|S_t|-H_t,\qquad H_t=|S_t\cap\mathcal H_{s,r}|.}
\]
Equivalently
\[
|S_t|=2^t|S_0|-\sum_{j<t}2^{t-1-j}H_j.
\]
This kills the claim that ambient exact-hit density alone determines support growth: only the support-aligned visits `H_t` matter.

For nonsquare `r>=5`, ambient hits are `O(log X)` up to spatial scale `X`, while support spatial scale is `O((sqrt r)^t)`, so `H_t=O(t)`. Combined with the finite maximum exact-hit run length and no recoalescence, the normalized branching mass has a positive limit:
\[
\boxed{\frac{|S_t|}{2^t}\longrightarrow L_{s,r,S_0}>0}
\]
for every finite nonempty positive initial support in this separated nonsquare regime. Pell pruning changes the multiplicative prefactor, not the binary branching entropy `log 2`.

## 10. Uniform normalized branch-limit theorem

For `r>1`, let
\[
\kappa=\frac{\beta}{1-\sqrt r},
\]
so `sqrt(r) kappa+beta=kappa`. Every legal child can be written
\[
k_{t+1}=\sqrt r\,k_t+\beta+e_t
\]
with a uniform bounded error `|e_t|<=C_{s,r}`. Therefore
\[
X_t=(\sqrt r)^{-t}(k_t-\kappa)
\]
satisfies
\[
X_{t+1}-X_t=(\sqrt r)^{-(t+1)}e_t.
\]
Every branch is Cauchy uniformly, and finite normalized support sets converge in Hausdorff distance to a compact branch-limit set with geometric tail bound.

For separated regimes,
\[
\dim_H K\le\overline{\dim}_B K\le\frac{\log2}{\log\sqrt r}.
\]
Equality is frozen at this checkpoint only in the square stable two-digit branch. Nonsquare equality remains open.

Regime consequences: `r=2,3` interval carriers normalize to intervals; `r=4,s=3` and `s>=5` normalize to intervals; `r=4,s=4` and square `s=4` are singletons; square `q>=3,s!=4` gives exact `K_q`; nonsquare `r>=5` has an exact compact rounded-nonlinear limit whose full classical identification is open.

## 11. Killed and narrowed claims

Killed: `sqrt(r)>=2` alone determines all dynamics; integrality of `sqrt(r)` alone determines all dynamics; branch geometry and arithmetic coding are primitive independent axes; nonsquare coding is always Sturmian; Pell exact hits are mechanical defects; every defect is a principal continued-fraction convergent; ambient exact-hit density alone determines support growth.

Narrowed: square normalized support is a classical deleted-digit/Cantor-type object only after the exact affine stable regime is defined (`q=2` is an interval); generic beta-expansion/Bernoulli-convolution language for nonsquare supports remains comparison language only because the exact map is state-dependent rounded nonlinear dilation with Pell pruning.

## 12. Prior-art boundary

Polygonal-multiple/generalized-Pell recurrence is rooted to Chahal–Griffin–Priddis, *When are Multiples of Polygonal Numbers again Polygonal Numbers?* (arXiv:1806.07981; Hardy-Ramanujan Journal, 2019). Mechanical/Sturmian words are classical (Morse–Hedlund). Contractive self-similar digit-set theory is classical (Hutchinson). R040 claims only the task-specific endpoint-dynamics interface and exact carrier/coupling results above, not generic novelty for these classical theories.

## 13. Executable evidence

Artifacts:

- `experiments/r040_polygonal_asymptotic_coding.py`
- `tests/test_r040_polygonal_asymptotic_coding.py`
- `research_outputs/r040/R040_TWO_AXIS_DISPOSITION.json`
- `research_outputs/r040/R040_CODING_ATLAS.json`
- `research_outputs/r040/R040_EXACT_HIT_ATLAS.json`
- `research_outputs/r040/R040_LIMIT_SUPPORT_ATLAS.json`
- `research_outputs/r040/R040_PROVENANCE_MATRIX.json`
- `research_outputs/r040/R040_KILLED_NARROWED_CLAIMS.json`
- `docs/R040_UNRESOLVED_FRONTIER.md`

Validation: 14 focused test groups pass. The exact discriminant inverse is cross-checked against an independent monotone binary-search oracle; endpoint sets are independently checked; Pell-strip equivalence/trichotomy is exhaustively checked over a small multi-family domain and large exact ranges; square threshold/digit formulas, the `r=10` coupling witness, the nonprincipal-convergent defect witness, the non-Sturmian balance witness, `r=4` formulas, `s=4` degeneracy, and cardinality loss identity are all executable checks.

`CI_NOT_REQUIRED_FOR_RESEARCH`: ordinary L1/L2/L3 checkpoint; no workflow-status query was made.

## 14. Open frontier

Not overclaimed:

1. Whether a single nonsquare `c!=0` branch can return to the exact-hit set infinitely often with non-hit steps between returns.
2. Exact Hausdorff dimension/equality for nonsquare `r>=5` branch limits.
3. Closed residue-orbit criterion deciding which finitely many interior Pell norms are populated for arbitrary `(s,r)`.
4. Minimal substitutive/automatic description of the sparse defect schedule across all compatible norm classes.
5. Full classical identification of the `s=4`, nonsquare `r>=5` rounded-dilation limit.

None is a current `HARD_BLOCK`.
