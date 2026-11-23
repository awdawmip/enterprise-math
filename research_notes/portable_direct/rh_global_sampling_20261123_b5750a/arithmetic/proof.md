# 跨块误差分配：去掉稀疏正包络的强制对数加密

Date: 2026-11-23 (Asia/Hong_Kong).  
Status: author analytic proof, continuing the same full-road scalar observer.  
Parent research provenance: EM-DIRECT-B5750A / TASK_RESEARCH; this contribution creates no separate researcher, CLAIM or independent Review.

## 1. Scope, inputs and result

The native starting point remains P000 / Heartbeat X6. Choose a Cell anchor and use the native axis sequence `c_*+nE_1` only to index the declared auxiliary scalar observer. All integers, composites, unit, finite thickness labels, actual prefix, endpoints and original road remain available. The following sampling theorem compresses this one weighted positive-energy observation at the stated window. It does not erase the underlying state or assert any native positive-mass cancellation.

Let integers `4<=A<B` define the closed window. Let

\[
q(y)=\sum_{2\le n\le y}D_n(y/n-1)-y\log y+(1+\gamma)y,
\qquad -\Delta^2q_n=(\kappa_n-D_n)/n,
\]

and assume the already established uniform matched-road estimate

\[
|D_n-\Lambda(n)|\le\varepsilon_B\quad(n\le B),\qquad
1\le\kappa_n\le1+1/(2n^2).
\tag{1}
\]

The single finite thickness family is selected once at B and used throughout the prefix. The direct interpolation proof of the D estimate is the one in `rh_arithmetic_next_20261122/ARITHMETIC_FINE_REMAINDER_BOUNDS.md`, §1; it is not inferred by dropping divisor factors from `c-c*=mu I`.

Split the window into blocks `[X,Y]`, with `X=2^j A`, `Y=min(2X,B)`, and `b_X=Y-X`; retain the actual last endpoint. Write `N_b` for the number of blocks and define

\[
G_\alpha=\frac1{1-2^{-\alpha}},\qquad
C_A=1+\frac1{2A^2}+\varepsilon_B,\qquad
\rho_B=2\varepsilon_B+\frac1{2A^2}.
\tag{2}
\]

Choose a scale parameter

\[
\boxed{B^{-1/40}\le r\le1.}
\tag{3}
\]

For the block starting at X put

\[
H_X=rB^{-1/20}X^{4/5},\qquad
s_X=\max(1,\lfloor H_X\rfloor).
\tag{4}
\]

Use constant integer step `s_X` in that block, shortening only the final cell. This includes complete sampling whenever `H_X<2`. Set

\[
g_n=nH_n,\qquad H_n=\sum_{j=1}^n1/j,
\qquad U_\Pi=I_\Pi(q+C_Ag)-C_Ag.
\tag{5}
\]

The earlier rational-potential theorem gives `q<=U_Pi`, using only genuine node values and the exactly rational g. Here we prove a new allocation bound. Define

\[
\begin{aligned}
E_{\rm p}(A,B,r)
&=\frac{G_{1/5}}8r^4\left[
25\left(1+\frac{\log2}{\log A}\right)^2
+(\log2)B^{-7/40}\log(2B)\right],\\
E_{\rm pp}(A,B,r)
&=9G_{3/5}r^3B^{-3/20}A^{-3/5},\\
T(A,B,r)&=\frac{G_{1/5}}{120}r^4.
\end{aligned}
\tag{6}
\]

Then the finite, explicit estimate is

\[
\boxed{
0\le\|U_{\Pi,+}\|_w-\|q_+\|_w
\le\|U_\Pi-q\|_w
\le\sqrt{E_{\rm p}}+\sqrt{E_{\rm pp}}+\rho_B\sqrt T,
}
\tag{7}
\]

where `||v||_w^2=sum_{n=A}^B v_n^2/n^2`. Its sample count satisfies

\[
\boxed{\#\Pi\le1+N_b+2G_{1/5}\,\frac{B^{1/4}}r.}
\tag{8}
\]

If `epsilon_B` is bounded, the right side of (7) is `O(r^2)` with a uniform constant. Thus for any `r=r(B)->0` satisfying (3),

\[
\boxed{\#\Pi=O(B^{1/4}/r+\log B),\qquad
\|U_{\Pi,+}\|_w-\|q_+\|_w=O(r^2)\to0.}
\tag{9}
\]

This holds for all `4<=A<B`; it does not require `B=A^lambda` or `lambda<16`. For a fixed power window it applies directly. The parameter restriction (3) is a sufficient range used to make the displayed constants simple, not an asserted optimal restriction.

The previous rule `h_X<=X^(3/4)/(log X)^alpha`, `alpha>1/4`, paid the same asymptotic error on every block. The present rule charges geometrically smaller error to earlier blocks. In particular `r=1/log log B` is admissible for sufficiently large B and gives

\[
\#\Pi=O(B^{1/4}\log\log B),\qquad
\|U_{\Pi,+}\|_w-\|q_+\|_w=O((\log\log B)^{-2}).
\tag{10}
\]

Any more slowly diverging function may replace `log log B`, provided its reciprocal eventually satisfies (3). There is no required positive power of `log B` in this sufficient node bound.

## 2. Already established Green and arithmetic ingredients

On a cell `[L,R]` of integer length `h=R-L`, the zero-endpoint Green kernel is

\[
G_h(i,j)=\frac{\min(i,j)(h-\max(i,j))}{h}.
\]

The following exact or inequality statements were proved in the prior arithmetic-fine-remainder note:

\[
\|G_hv\|_2\le(h^2/8)\|v\|_2,
\quad \max_j\sum_iG_h(i,j)^2\le h^3/32,
\quad \sum_i\left(\sum_jG_h(i,j)\right)^2=(h^5-h)/120.
\tag{11}
\]

The last equality uses `sum_j G_h(i,j)=i(h-i)/2`. All interior Green images vanish when `h=1`. The elementary Chebyshev and prime-power bounds are

\[
\psi(t)\le4(\log2)t,\qquad
Q(t):=\sum_{p^a\le t,\ a\ge2}\log p\le12\sqrt t.
\tag{12}
\]

For ordinary primes, the only external input is Montgomery–Vaughan, *The large sieve*, Mathematika 20 (1973), Theorem 2, printed page 121, equation (1.12):

\[
\pi(M+N)-\pi(M)\le2N/\log N\qquad(M>0,N>1).
\tag{13}
\]

The original [author-hosted PDF](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf) was opened and its page-121 text verified in this continuation. This is a classical input, not a new prime-count theorem. No RH, local square-root cancellation or randomness assumption is used below.

For h>=2 in a block `[X,Y]`, the same positive-source argument gives

\[
\|G(\Lambda\mathbf1_{\rm prime}/n)\|_{w,\mathrm{cell}}^2
\le\frac{(\log Y)^2}{8X^4}\frac{h^5}{(\log h)^2}.
\tag{14}
\]

Alternatively, without a local prime-count input, the row-sum bound and `Lambda^2<=Lambda log Y` give

\[
\|G_\Pi(\Lambda\mathbf1_{\rm prime}/n)\|_{w,[X,Y]}^2
\le\frac{\delta^4}{64X^4}(\log Y)\psi(Y),
\tag{15}
\]

where delta is the maximum length of cells that contain an interior integer. When there are no such cells the left side is zero.

## 3. Exact error decomposition preserves the actual road

Let `e_n=D_n-Lambda(n)`. On each cell, both `U-q` and every Green image below have zero endpoints. From (1), (2), and `Delta^2 g_n=1/n`,

\[
U-q=G_\Pi((D-\kappa+C_A)/n),
\]

\[
0\le D_n-\kappa_n+C_A
\le\Lambda(n)+2\varepsilon_B+\frac1{2A^2}
=\Lambda(n)+\rho_B.
\]

Consequently

\[
0\le U-q\le B_{\rm p}+B_{\rm pp}+\rho_BV,
\tag{16}
\]

where `B_p=G_Pi(Lambda 1_prime/n)`, `B_pp=G_Pi(Lambda 1_higher-prime-power/n)`, `V=G_Pi(1/n)`, all nonnegative. All integers still enter the complete q; this prime-power split is used only to upper-bound a declared auxiliary error. Formula (16) is why this task can use positive-source estimates without discarding the unknown signed cancellation inside q itself.

## 4. Smooth-source cost is a geometric series

If h>=2 then `h<=H_X`, even when the final cell is shortened. If h=1 its error is exactly zero. Therefore

\[
\|V\|_{w,[X,Y]}^2
\le\frac1{120X^4}\sum_{\rm cells}(h^5-h)
\le\frac{b_XH_X^4}{120X^4}
\le\frac{r^4}{120}(X/B)^{1/5}.
\tag{17}
\]

The harmless middle inequality remains valid when `H_X<1`, because every term on its left is zero. Dyadic starts form a geometric progression and their largest member is less than B, so

\[
\sum_X(X/B)^{1/5}\le G_{1/5}.
\tag{18}
\]

This proves `||V||_w^2<=T` in (6).

## 5. Prime cost: the small blocks need a different bound

For a fixed power window with large lambda, `H_A` may be below one. It is therefore invalid to suppose `log H_X` is a fixed fraction of `log X` on every block. We split the proof at `X=B^(1/8)`; the algorithm itself does not need this split.

### 5.1 Blocks with X>=B^(1/8)

By (3),

\[
\log H_X
=\frac45\log X-\frac1{20}\log B+\log r
\ge\frac45\log X-\frac3{40}\log B
\ge\frac15\log X.
\tag{19}
\]

On blocks with an h>=2 cell, `H_X>=2`. The function `t^4/(log t)^2` increases on `[2,infinity)`, since `4-2/log t>0`. Thus (14) gives

\[
\begin{aligned}
\|B_{\rm p}\|_{w,[X,Y]}^2
&\le\frac{(\log Y)^2}{8X^4}
\frac{b_XH_X^4}{(\log H_X)^2}\\
&\le\frac{25}8\left(1+\frac{\log2}{\log A}\right)^2
r^4(X/B)^{1/5}.
\end{aligned}
\tag{20}
\]

For blocks with only h=1 cells the left side is zero, so the conclusion is unchanged. Summing (20) and using (18) proves the first term of E_p.

### 5.2 Blocks with X<B^(1/8)

Apply (15), (12), and `Y<=2X`. On nontrivial cells delta<=H_X, so

\[
\|B_{\rm p}\|_{w,[X,Y]}^2
\le\frac{\log2}{8}r^4(X/B)^{1/5}\log Y.
\tag{21}
\]

For h=1-only blocks it again holds with zero left side. Their starts satisfy

\[
\sum_{X<B^{1/8}}(X/B)^{1/5}
\le G_{1/5}B^{-7/40},\qquad \log Y\le\log(2B).
\tag{22}
\]

This proves the second term of E_p. It explicitly pays the weaker small-block bound; no false uniform estimate for `log Y/log H_X` is used.

## 6. Higher prime powers and whole-window estimate

For a cell c let `M_c=sum_{L<p^a<R,a>=2}log p`. By (11),

\[
\|B_{\rm pp}\|_{w,c}^2\le\frac{h^3M_c^2}{32X^4}.
\]

Cell interiors are disjoint. Summing, using h<=H_X when h>=2 and (12),

\[
\|B_{\rm pp}\|_{w,[X,Y]}^2
\le\frac{H_X^3Q(Y)^2}{32X^4}
\le9r^3B^{-3/20}X^{-3/5}.
\tag{23}
\]

The dyadic sum from A is at most `G_(3/5) A^(-3/5)`, proving E_pp. The triangle inequality applied to (16) proves (7). Nodes have zero error and can be counted once; true endpoints are included.

Finally, (3) gives the uniform ratio

\[
E_{\rm pp}/r^4
\le9G_{3/5}B^{-1/8}A^{-3/5},
\tag{24}
\]

while `B^(-7/40)log(2B)` is bounded and tends to zero. For A>=4 the factor `1+log2/logA` is bounded. If epsilon_B is bounded, (7) is therefore uniformly `O(r^2)`. In the actual stable matching family epsilon_B tends to zero, so its contribution is even smaller. None of these estimates bounds the unknown `||q_+||_w`; they bound only the difference between the observable upper bound and that quantity.

## 7. Sample count, exact construction and finite precision

For every H>0, `max(1,floor H)>=H/2`: this is immediate for H<2 and follows from floor H>=H-1 for H>=2. A block therefore has at most

\[
\lceil b_X/s_X\rceil\le2b_X/H_X+1
\]

cells. Since `b_X<=X`,

\[
\sum_X b_X/H_X
\le\frac{B^{1/20}}r\sum_X X^{1/5}
\le G_{1/5}\frac{B^{1/4}}r.
\tag{25}
\]

The whole path has exactly one more distinct grid node than cells, proving (8), including all integer saturation cases and the final short block.

For rational `r=u/v`, s_X can be chosen exactly by an integer twentieth-root comparison:

\[
\lfloor H_X\rfloor=
\max\{k\in\mathbb Z_{\ge0}:v^{20}B k^{20}\le u^{20}X^{16}\}.
\tag{26}
\]

Thus no floating choice of node positions or near-threshold power is needed. A block step can exceed b_X; then it has one shortened cell, already covered above. The construction visits `#Pi` genuine q values. It does not provide a faster oracle for obtaining one q value from its full arithmetic prefix.

If node values are certified rational upper approximations with errors at most delta, the earlier nonnegative barycentric argument adds exactly the separate bound

\[
\|\widehat U_+\|_w-\|q_+\|_w
\le\sqrt{E_{\rm p}}+\sqrt{E_{\rm pp}}+\rho_B\sqrt T
+\frac\delta{\sqrt{A-1}}.
\tag{27}
\]

Fixed absolute node precision is therefore still sufficient on A->infinity windows. The node count is an observation count; actual prefix evaluation, exact harmonic arithmetic and final energy summation have their own costs.

## 8. What changed and what remains

The new result distributes a fixed total error budget across the entire window. The characteristic `4/5` here is the optimizer's spatial mesh exponent, with a terminal normalization `B^(-1/20)`; it does not replace the earlier local `3/4` automatic-curvature threshold. Indeed `H_X<=r X^(3/4)` for X<=B.

For a fixed requested root tolerance tau in the unsaturated asymptotic regime, r proportional to sqrt(tau) produces `O(B^(1/4)/sqrt(tau))` genuine observations. For a tolerance tending to zero, one may use any admissible r->0, and the additional factor need not be a power of log B.

This removes a representation and sampling loss from the preceding theorem. The arithmetic problem of proving an appropriately small positive energy for the complete actual road remains the target. The exact integer information-class lower bound and optimal finite allocation are handled by the sibling proof; no arithmetic impossibility claim is inferred from such a broader information class.

## References and reproducibility

- Prior exact rational upper envelope and matching error: `rh_sparse_root_20261122/SPARSE_UPPER_ENVELOPE_WITH_VANISHING_LOSS.md`.
- Prior Green norms, elementary Chebyshev bound and Q(t)<=12sqrt(t): `rh_arithmetic_next_20261122/ARITHMETIC_FINE_REMAINDER_BOUNDS.md`.
- H. L. Montgomery and R. C. Vaughan, *The large sieve*, Mathematika 20 (1973), 119–134, Theorem 2, equation (1.12), DOI 10.1112/S0025579300004708. [Original PDF](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf).
- The attached `verify_mesh.py` uses integer arithmetic to verify node construction and exact rational smooth-source costs on declared finite examples, including lambda>16 saturation. These checks support the implementation of the displayed finite formulas; the all-window theorem is the proof above.
