# CBRC F7 r473 — exact zero-defect gauge kernel and sharp global oscillation stability

Date: 2026-11-22 (Asia/Taipei). Scientific author of this result: current original RESEARCH_DRIVER lane `EM-DVR-DEBB5E`; original CBRC F7 Task/Result researcher `EM-CBRCF7-83A1D4` and its source history are unchanged. This is a standalone structural theorem for the same **exact shear defect** used in r471–r472, not a Native independent review or new Result acceptance.

## Frozen operator and lattice coordinates

Let any real function `q: Z² -> R` be given. For integer `z=(a,b,c,d)`, put `k=a-2b-c+2d` and
```
D_q(z) = q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d).
```
Define `E∞(q) = sup_{z in Z⁴}|D_q(z)|`, allowing `+infinity`. Invertible integer coordinates are
```
r = x-y,  t = x-2y;       x = 2r-t, y = r-t;
h_r(t) = q(2r-t,r-t).
```
The r471 identity is `D_q=[h_r(s)-h_u(s)]-[h_r(t)-h_u(t)]`, and thus `E∞=sup_{r,u}osc(h_r-h_u)`. The exact original admissibility conditions (evenness in x, axis/origin values, off-axis lower bound and two marked values) remain unchanged when this result is **applied** to an F7-admissible q; the kernel theorem itself is stated for arbitrary real q.

## Theorem — complete kernel and quantitatively sharp stability

Let
```
G = { g(x,y)=A(x-y)+B(x-2y) : A,B: Z -> R }.
dist∞(q,G) = inf_{g in G} sup_{(x,y) in Z²}|q(x,y)-g(x,y)|.
```
Then:

1. `D_q = 0` at every integer input **if and only if** `q∈G`. Any decomposition into A,B is unique up to shifting A by a constant and B by its negative.
2. Every `g∈G` satisfies `D_g=0` and `D_{q+g}=D_q`; hence every finite-box error and the global error are invariant under addition of a gauge `g`.
3. If `ε=E∞(q)<infinity`, then
   ```
   ε/4 ≤ dist∞(q,G) ≤ ε/2.
   ```
   Both universal constants `1/4` and `1/2` are **optimal over unrestricted real-valued functions q on Z²**.

### Proof of 1–3

If `D_q=0`, choose the reference fiber `u=0` and base argument `t=0`. The rectangle identity implies
```
h_r(s)-h_0(s) = h_r(0)-h_0(0)
```
for all r,s, so `h_r(s)=A(r)+B(s)` with `A(r)=h_r(0)-h_0(0)`, `B(s)=h_0(s)`. Conversely additive separation cancels in every rectangle. If two decompositions exist, their differences depend simultaneously only on r and only on t, and hence are constants. Gauge invariance follows by linearity.

If `δ=sup|q-g|` for a gauge g, a rectangle contains four signed error terms, so `E∞(q)=E∞(q-g)≤4δ`. Infimize in g to obtain `ε/4≤dist∞`.

For the upper bound, fix fiber 0 and write `v_r(t)=h_r(t)-h_0(t)`. By the r471 oscillation identity, `osc_t v_r(t)≤ε`, so its infimum `m_r` and supremum `M_r` are finite. Define
```
A(r) = (m_r+M_r)/2,    B(t)=h_0(t).
```
Then every `|h_r(t)-A(r)-B(t)|≤(M_r-m_r)/2≤ε/2`. The integer coordinate map is a bijection, yielding the asserted uniform bound.

### Sharpness of both constants

**Lower coefficient 1/4.** Take `h_r(t)=1` exactly at `(r,t)=(0,0)` and zero otherwise (equivalently `q(x,y)=1` exactly at `(x,y)=(0,0)`). Then `E∞=1`: one rectangle containing that cell realizes defect one, and no rectangle has a larger absolute defect. Choose `A(r)=1_{r=0}/2-1/8`, `B(t)=1_{t=0}/2-1/8`. Residuals at the selected cell, at one-index-only cells, and elsewhere have magnitude precisely `1/4`. The general lower bound makes the distance exactly `1/4`.

**Upper coefficient 1/2.** Take `h_r(t)=1_{r>t}` (equivalently `q(x,y)=1_{y>0}`). For `r>u`, `h_r(t)-h_u(t)` is the indicator of `u≤t<r`; hence `E∞=1`. The constant gauge `g=1/2` gives distance at most `1/2`. For every `n≥2` and any gauge A(r)+B(t), compare the `n` diagonal cells `(i,i)` (all h=0) against the `n-1` cells `(i+1,i)` (all h=1) plus `(1,n)` (h=0), for `1≤i<n`. Both collections contain each row and column index exactly once, so their gauge sums cancel. Their h-sum difference is `n-1`. If the uniform residual is ≤δ, then `n-1≤2nδ`. Letting n grow forces `δ≥1/2`. The upper coefficient is sharp.

These two sharpness examples need **not** obey the original F7 marks or off-axis/axis constraints. They establish optimality of the general operator stability statement; for original-admissible q the proven bounds remain valid, without asserting admissible sharpness.

## Research use and proof boundaries

The equation `E∞≤ε` is equivalently a uniform oscillation bound between every pair of fibers. The new theorem makes this precise as distance at most `ε/2` to a sum of two one-dimensional integer potentials, with best-possible universal factor, even for unbounded q with finite defect. This gives a gauge-normalization and model-reduction route for the open original-admissible infinite-lattice F7 minimax problem.

For original F7: r469 already proves exact finite-box optimum through B14, r470 gives a repair bound for one B14 witness, and r471–r472 give tail/area density conditions. This theorem neither changes `1/2≤E∞*≤4/7` nor proves B15 feasibility or infeasibility.

Related verified sources: `research_notes/driver/2026-11-22_f7_r471_exact_fiber_swap_global_quarter_audit.md@013c38ab95d45a1c5fc6f3e583d6e62e688395f7`, `research_notes/driver/2026-11-22_f7_r472_axis_pair_quadratic_tail_density.md@def0b48fe6aa9025f747c1899fcd2ea0d21553ae`. Proof is algebraic; no numerical solver or formal checker was needed. Native F7 Result review is separately blocked by current authority/integrity checks and original author contributions remain intact.
