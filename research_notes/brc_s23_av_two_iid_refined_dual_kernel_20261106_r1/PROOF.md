# S23/AV two-iid: stronger exact three-hypothesis dual and refined joint-kernel certificate

Date: 2026-11-06. Status: author analytic proof + executed exact-rational checker; independent review pending. Scientific input remains frozen at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Continuation of Draft PR #1777, previous verified certificate at `5220a5937dd588afdd695995b04e0e0c791e32fa`.

## Model and quantifier scope

For all **real** (a,c\in[1/2,7/8]), arbitrary (b\in[1/8,1/2]), set (z=(1-a)c), (A=(a,z,1-a-z)), (B=(z,1-z)). Two observations are conditionally independent given the **same** unknown pair ((a,c)). A reconstruction kernel (L) is a single row-stochastic (4\times9) matrix mapping (YY,YN,NY,NN) to (11,13,14,31,33,34,41,43,44), independent of the hidden parameters. Define
[
\delta_2=\inf_{L}\sup_{a,c\in[1/2,7/8]} \operatorname{TV}(A(a,c)^{\otimes2},B(a,c)^{\otimes2}L).
]

**Theorem (exact constructive two-sided certificate):**
[
\boxed{\frac{15383}{83769}\le\delta_2\le\frac{387769986271}{2048000000000}}
\quad (0.1836359512468813\le\delta_2\le0.1893408136088867).
]
Both are strict improvements over the previously proved `1491/8125 <= delta2 <= 7573633/40000000`. This is a statement about the conditional tagged AV experiment, not an unverified transfer to the ten-label S23 mother minimax problem.

## Exact lower: an explicit three-point dual

Choose three legal pairs
[
\theta_0=(1/2,1/2),\quad \theta_1=(11/16,7/8),\quad \theta_2=(23/32,7/8).
]
For (P_k=A_{\theta_k}^{\otimes2}), (Q_k=B_{\theta_k}^{\otimes2}), use nonnegative weights
[
(w_0,w_1,w_2)=(5983/11967,6176/83769,11904/27923), \qquad\sum_k w_k=1
]
and signed nine-coordinate vectors (each coordinate belongs to [-1,1])
[
v_0=(-1,-1,1,-1,0,1,1,1,1),\quad
v_1=(1,1,-1,1,4/35,-1,-1,-1,-1),\quad
v_2=(1,1,-1,1,-4/189,-1,-1,-1,-1).
]
For **any** row-stochastic (L), total-variation duality yields
[
\sup_\theta\mathrm{TV}(P_\theta,Q_\theta L)
\ge\sum_k w_k\mathrm{TV}(P_k,Q_kL)
\ge\frac12\sum_k w_k\langle v_k,P_k-Q_kL\rangle.
]
Put (C=\sum_k w_k\langle v_k,P_k\rangle) and (d_{rj}=\sum_k w_k Q_k[r]v_k[j]). Each row of (L) is a probability vector, hence
[
\frac12\left(C-\sum_{r,j}L_{rj}d_{rj}\right)
\ge\frac12\left(C-\sum_r\max_j d_{rj}\right).
]
Exact fractional computation proves
[
C/2=30773/167538,\quad
(\max_jd_{0j},\max_jd_{1j},\max_jd_{2j},\max_jd_{3j})
=(1/11967,0,0,0).
]
Subtracting half the sum of row maxima gives **exactly** (15383/83769). The calculation contains neither a sampling assumption nor a floating-point bound; it applies to all kernels and the entire continuous domain.

## Exact upper: one universal joint kernel

Define (K=M/10^9), with 4 input rows ordered YY,YN,NY,NN and 9 output columns ordered 11,13,14,31,33,34,41,43,44:
```text
0,0,0,0,1000000000,0,0,0,0
0,0,0,579190219,0,0,420809781,0,0
0,553921569,66364911,90824631,0,111111111,0,111111111,66666667
753350886,37581699,148315790,26583388,0,0,34168237,0,0
```
Every row is nonnegative and sums to the denominator; this is a valid hypothesis-independent stochastic kernel, not a result of rounding after the proof.

Let (\theta_i) be the lexicographic corners of ({1/2,7/8}^2), (A_i=A(\theta_i)), (B_i=B(\theta_i)). Define (F_{ij}=A_i\otimes A_j-(B_i\otimes B_j)K) and (G_{ii}=F_{ii}), (G_{ij}=(F_{ij}+F_{ji})/2) for (i<j). Both (A(a,c)) and (B(a,c)) are separately affine in (a,c); their bilinear-corner weights (\lambda_i(a,c)\ge0) sum to one. Because both trials share the same ((a,c)),
[
A^{\otimes2}-B^{\otimes2}K
=\sum_i\lambda_i^2G_{ii}
+\sum_{i<j}2\lambda_i\lambda_jG_{ij}.
]
These ten coefficients sum to one. Convexity of total variation therefore gives, **over the full real parameter square**,
[
\mathrm{TV}(A^{\otimes2},B^{\otimes2}K)\le\max_{i\le j}\mathrm{TV}(G_{ij}).
]
The attached exact checker evaluates all ten nine-coordinate signed fractions, establishing that the maximum is (387769986271/2048000000000), attained at corner $\theta_3=(7/8,7/8)$ by $\mathrm{TV}(G_{33})$. Thus the **worst-case error of this particular kernel** is exactly the stated upper bound.

## Interpretation / next discriminating steps

The improved lower witness replaces a prior interior parameter (47/64) with (23/32) while also adjusting rational weights and one signed test coordinate; the upper uses a refined denominator (10^9). The resulting uncertainty width is about 0.00570486236 (2.20% narrower than the prior rigorous interval). Numerical linear programming was used to discover candidate rational witnesses, but all the published inequalities rest on exact fractions and a domain-covering analytic interpolation identity. Neither mathematical independence nor a native CLAIM/owner is implied by author publication.

Next: (A) optimize a **fourth** or continuously movable legal hypothesis in an exact dual, or characterize optimality of the ten-corner relaxation; (B) inspect the frozen original ten-label encoder/decoder/source mixing to test a lawful quantifier-preserving bridge; (C) seek independent proof review.