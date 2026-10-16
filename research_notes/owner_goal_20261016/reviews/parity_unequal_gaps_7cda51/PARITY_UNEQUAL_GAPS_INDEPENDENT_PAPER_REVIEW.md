# Independent review: unequal-gap bounded-sector tail

Reviewer: Researcher EM-PUBLIC-7CDA51, session MCP-9030ae3a22074e3dbc31679b7090f6b0 and activity RA-6665DBCD10BC1C3E4DED3C04. Root delegated this nonauthor paper review after my P11 Source/RA chain completed. All Public129/CONTROL/CI/T6/P11 history and shared nonblind context remain disclosed. I had no part in the parity plan, mathematical construction or code. The P11 conclusions are not premises for this judgment. This is direct mathematical support, not a Native Driver vote or formal Task acceptance.

## Judgment and exact scope

I found no mathematical gap in the candidate theorem as written. For each fixed integer `m>=2` and supplied positive rational `A0,C0`, its finite coefficient construction gives a computable rational threshold valid simultaneously for all real `0<a<=A0`, `0<c<=C0` and `S` above that threshold. No positive lower bound on either gap is required. The uniform asymptotic for the complete gap divided by c, with leading coefficient `(m^2-1)/(S+a)`, is also supported by the stated explicit remainder.

The reviewed author manuscript is exactly 12768 bytes, SHA-256 `50e3f47d81036645d3f8cf08326095fa4d6753ff5a5c479bb1cd2f2b6fdafeaf`, Git blob `f05b0b5be5c7d78c7faf58ae1f818bc67cea103c`. It is an unreviewed frozen local author candidate at this review's construction time; Source publication and later same-byte binding remain separate. This report does not prove the all-S registered hard target, a uniform-in-m threshold, an unbounded-sector threshold, pointwise branch positivity, other mixed coefficients or parent completion.

I read the full manuscript, the complete equal-block tail paper at `df5869771ff760a0b57a5d757934f0ab9f56f07e`, the original signed-branch reduction and complete HCM0 handoff index at `623a4ee81911cc79d07ed5db1887a06ebe91ffd5`, and the exact current Task publication/Taskbook/Goal head at `03480f8024a5fd4492ad0bb599b51ab8d2d4b7aa`. Hashing, full Source reads and activity guards were custody operations. No coefficient generation, matrix program, parameter scan, enumeration, old checker or scientific program was run.

## Original domain and complete actual observer

The registered publication is `RS-PERFECT-PRIME-AP-HCM0-EXTREME-BRANCH-PARITY-DOMINATION / TP2-4F8D04C54528CFF5E1B2`. Its original target explicitly includes every integer `m>=2`, `S>=0`, `a,c>0`; the paper does not need to extrapolate an even-m or m>=3 statement to get its m-domain. It does not cover m=1. The full target also includes all small S, which this tail theorem leaves unresolved.

The original Source reduction gives precisely the normalized secant form `A=G_M^T D_r G_M`, `B=G_N^T D_s G_N`, with the same alternating metric and actual synchronization `r0=mS`, `M=ma`, `N=m(a+c)`. Its normalized secant average is the same rising-factorial difference quotient used in this manuscript. The same fixed sign-diagonal congruence acts at both endpoints, so the relative trace is invariant. No branchwise estimate or positive-spectrum substitute occurs in this return to the original complete normalized trace.

The original signed branch carrier and its endpoint/row/parity/magnitude labels must remain available for later branch operations. The exact trace identities justify only the declared complete-trace observer; they do not authorize erasing cancellation provenance for a different observer. The static algebra is an external representation within the fixed Heartbeat X6 semantics, not a native plane or a new spatial interpretation of the polynomial coordinates.

## Exact transfer and moving-frame cancellation

On polynomials of degree at most `n-1`, differentiation is nilpotent of order n. The normalized secant average is exactly

\[
g_b=\Psi_b(D_x)\phi',\qquad
\Psi_b(D_x)=\sum_{k=0}^{n-1}\frac{b^kD_x^k}{(k+1)!}.
\]

Its constant term is I and all remaining terms are divisible by the nilpotent operator, so its inverse is a finite polynomial, without division by b or by D. Since these polynomials commute, `Psi_M Psi_N^{-1}` sends the later frame to the earlier one in the stated direction. The equal-block specialization reduces to the old Euler transfer, but that special formula is not used for unequal gaps.

After `z=1+epsilon*x`, the matrix is polynomial over `Q[a,c,epsilon]`, with epsilon degree at most `n-1=m-2`: any product with total derivative degree at least n vanishes. It is triangular with diagonal 1. Its first derivative is `(M-N)D/2=-(mc/2)D` and has trace zero.

For positive epsilon the later secant columns form a polynomial basis: their degrees are `0,...,n-1` with nonzero leading coefficients. The affine monomial change is also invertible then. The same matrix C transforms both endpoint forms after applying U, so it cancels from `B^{-1}A` by similarity. The resulting formula `tr(J^{-1}U^T F U)` has the correct transposes and endpoint order. This exact cancellation precedes taking epsilon to zero; no invertibility of C at zero or omitted derivative of the diverging initial layer is assumed.

## Confluent Gram family and first coefficient

The reused two-parameter H is jointly analytic near `(epsilon,v)=(0,0)`: its signed sum is an n-th finite difference with step `epsilon/m` of a rational function whose denominators stay nonzero there. Dividing by epsilon to the n-th power has an analytic extension by the repeated fundamental theorem of calculus. This is joint analyticity, sufficient for the path `v=mc*epsilon`, not merely a pathwise limit.

The original maximal-minor law and sigma identity give the displayed exact determinant `K(1+v+lambda*epsilon)/Q`. The monomial Vandermonde contributes the stated factorial product in kappa. Thus `det H(0,v)=K(1+v)^(1-m^2)` and H at zero is nondegenerate. K is a nonzero rational, possibly negative; the calculation needs no positive definiteness or logarithm of a negative real number.

With `F=H(epsilon,0)` and `J=H(epsilon,mc*epsilon)`, the derivative difference is `J'-F'=mc*partial_v H`. The two moving-frame derivative terms each have trace `tr U'=0` by cyclicity. Jacobi's determinant identity therefore gives the full trace derivative `mc(m^2-1)`. This is independent of a, and exactly linear in c. It is a calculation of the complete trace, rather than an individual residue or parity mass.

## Polynomial identity and exact division by c

Multiplying H by Q gives a polynomial W. Indeed the proposed numerator is polynomial in epsilon and v; analytic divisibility near every v in an interval forces all lower epsilon coefficients to vanish as polynomials in v. Hence the cancellation is an identity in `Q[epsilon,v]`, and substitution of `v=mc*epsilon` is legitimate.

The rational trace formula obtained by replacing J with `W_B/Q_B` is exactly the manuscript's adjugate numerator over `Q_A det W_B`. Multiplication by the sign of K gives

\[
D_{gap}=|K|Q_A[1+(mc+\lambda)\epsilon]Q_B^{n-1}.
\]

Every displayed product factor is positive on `epsilon,c>=0`, with constant term `d0=|K|`; all coefficients are nonnegative. The denominator is independent of a. No unproved determinant sign is hidden here.

At c=0 the finite polynomial transfer is I, and both endpoint polynomial matrices coincide. The adjugate identity gives `N_gap(epsilon;a,0)=0` as a polynomial, without dividing by a determinant or assuming invertibility at a special point. Therefore `N_gap=c*Z` in `Q[epsilon,a,c]`. Since `N_gap(0)=0`, the quotient Z also vanishes at epsilon=0. Combining the exact derivative with `D_gap(0)=|K|` gives the first coefficient

\[
[\epsilon]Z=|K|m(m^2-1)=\alpha>0,
\]

independent of both gap parameters. The use of the polynomial ring matters: no residual `1/a` or `1/c` survives to destroy the uniform estimate near zero.

The degree bound is valid: each W entry after substitution has epsilon degree at most `m^2-3`; the adjugate has at most `(n-1)(m^2-3)`, and the two U factors add at most `2(m-2)`. Including Q_B yields `m^3-m-1`. Dividing by c does not increase epsilon degree. At m=2 the derivative space has dimension one, U=I, the empty products are defined, and the 1-by-1 adjugate is I, so this endpoint of the stated m-domain is included without an exceptional unsupported formula.

## Uniform threshold and epsilon domain

For supplied rational upper bounds A0,C0, the absolute coefficient sum B_sector is a finite rational number. For `0<=epsilon<=1`, `0<=a<=A0` and `0<=c<=C0`, each higher epsilon power is bounded by epsilon squared, giving the displayed remainder estimate for Z. Including a=0,c=0 here is an algebraic bounding extension, not a change to the actual positive-gap theorem.

When `R=max(1,2B_sector/alpha)`, `S>=R/m` implies `r=m(S+a)>=R` and hence `0<epsilon<=1/R`. Thus `Z>=alpha*epsilon/2>0`, including the case B_sector=0 without division by zero. Multiplication by the actual c>0 and division by the positive D proves the strict complete-trace inequality. The threshold does not deteriorate through a lower bound on a or c, because alpha is constant after the exact division by c.

The physical substitution for a fixed a>0 and S>=0 has range `0<epsilon<=1/(ma)`. That upper endpoint is not the old equal-block `1/m` unless a=1. The paper's polynomial bound on the auxiliary rectangle `0<=epsilon<=1` may include nonphysical parameter combinations. This causes no gap: it is an identity/bound on a larger polynomial domain, and the final implication restricts to the actual `epsilon=1/[m(S+a)]` with `S>=R/m>0`, automatically satisfying the physical range. No extra actual S values are inferred from the auxiliary extension. The conservative threshold `R/m` need not subtract a and is valid uniformly in a.

## Uniform divided-gap remainder and computability boundary

Nonnegative denominator coefficients and its parameter-independent constant term imply

\[
0\leq D_{gap}(\epsilon;c)-d0
\leq [D_{gap}(1;C0)-d0]\epsilon.
\]

Writing `Z/D-(alpha/d0)*epsilon` as `(Z-alpha*epsilon)/D + alpha*epsilon*(1/D-1/d0)` gives exactly the stated constant `B_sector/d0+alpha*L_sector/d0^2` times epsilon squared. Substituting `epsilon=1/[m(S+a)]` yields leading term `(m^2-1)/(S+a)` and the claimed uniform error `E_sector/[m^2(S+a)^2]` whenever r>=1. This is the full gap divided by c, including its bounded extension as c tends to zero. It does not assert a strictly positive c-independent lower bound for the unscaled gap.

The threshold is computable from integer m and rational A0,C0 by finite rational polynomial operations and coefficient absolute values. Nilpotence makes every inverse construction finite; it is not an appeal to an unspecified analytic modulus or a root-finding oracle. This is a computability/existence proof, not an executed threshold value or an efficiency guarantee uniform in m.

The quantifier includes arbitrary real actual a,c within the supplied rational bounds; no algorithm for reading an uncomputable real is required. The fact that each positive real pair lies in some rationally bounded sector is an existential Archimedean fact, not an algorithm to extract upper bounds from an arbitrary inaccessible real representation. The manuscript explicitly keeps this distinction. Nothing supplies one threshold for all m or all unbounded sectors.

## Persistent and scientific boundary

The exact current Taskbook's all-S hard target and the OPEN mother objective are not closed by this eventual theorem. Existing small-m/tangent results and closed-route counterexamples remain inputs, not newly executed evidence. The observer equality and uniform tail do not prove individual branch positivity, positivity of a derivative kernel pointwise, other mixed coefficients or all HCM0 cells.

Own startup used the actual Source-bound RA at `03480f8024a5fd4492ad0bb599b51ab8d2d4b7aa`, SHA-256 `31a343579d04f3469ece1bc752a4eebec08bfda8aaa1f17a925fd4a325ccbf77`, preserving all four earlier events and all contribution/coverage history. The activity guard permits direct activity/persistence, with all formal authority flags false. No frozen Public run or another actor's RA is used.

This report supports the bounded-sector paper theorem at the exact stated scope. The author manuscript is still a frozen local input at construction, and exact later Source matching plus my own new semantic checkpoint require separately coordinated publication. No Native Result/review/vote, Task completion, role upgrade, Source mutation or scientific execution is created by this file.

Researcher-ID: EM-PUBLIC-7CDA51 / TASK_RESEARCH
