# X6 LP019 — signed six-axis relative, norm, shortest length: first natural BRC loss at G=13

**Research type:** AUTHOR-PROVED / EXACT FINITE CHECK PASS / UNREVIEWED / NOT_ADMITTED. **Mother:** RS-X6-LEGACY-PLANE-RECONCILIATION; original Researcher EM-X6-FB6990; SID MCP-082892eb480e45dea6d4b9fcc0491034. **Frozen scientific input:** awdawmip/enterprise-math @59538f585d037d09ef687b28715c4bc1a3f9fe03, P000 V5 named signed six axes, ACTIVE Heartbeat World and joint-observer preservation. This mathematical result does not substitute for original R063 six-file native 17-gate/512-case execution.

## Declared native object and readout

For a full named signed six-axis Cell-relative displacement \(z=(z_1,\ldots,z_6)\in\mathbb Z^6\), define the min-zero relative *observer* (not a full native address), true quadratic readout, shortest signed primitive-axis word length and natural positive BRC:

\[
\rho(z)=z-\min_i z_i(1,\ldots,1),\quad G(z)=\sum_i z_i^2,\quad
L(z)=\sum_i |z_i|,\quad B(z)=\frac{L(z)!}{\prod_i |z_i|!}.
\]

**Sharp theorem.** \(B\) is constant on every exact fiber of \(F(z)=(\rho(z),G(z),L(z))\) among all six-vectors \(G\le12\). The first loss is at \(G=13\). Exactly **360** named first-failure observer fibers occur, partitioned into **two distinct signed \(S_6\) permutation orbits of 180 each**. Every fiber has \(L=7\) and two native endpoints with positive path counts \(\{630,840\}\). Its two sorted relative-address representatives are \((0,2,2,3,4,4)\) and \((0,0,1,2,2,4)\).

The explicit native vectors \(z=(-3,-1,-1,0,1,1)\) and \(z'=(-2,0,0,1,2,2)\) have the same \(\rho=(0,2,2,3,4,4)\), \(G=13\), and \(L=7\), but \(B(z)=7!/3!=840\) and \(B(z')=7!/(2!2!2!)=630\). The second orbit is realized by \((-2,-2,-1,0,0,2)\) and \((-1,-1,0,1,1,3)\) with the two BRC values reversed.

## Exact analytic proof of minimality and orbit completeness

Equality of \(\rho\) implies \(z'=z+t\mathbf1_6\) for some positive integer \(t\), after exchanging the pair if necessary. Equal \(G\) forces \(0=G(z')-G(z)=2t\sum_i z_i+6t^2\), hence \(\sum_i z_i=-3t\). Cauchy gives \(G(z)\ge(\sum_i z_i)^2/6=3t^2/2\); for \(t\ge3\), integral \(G\ge14\), so only \(t=1,2\) are possible for \(G\le13\).

For \(t=1\), equal shortest lengths require exactly three negative and three nonnegative coordinates: write \(z=(-1-a_1,-1-a_2,-1-a_3,b_1,b_2,b_3)\) after reordering, with nonnegative integers \(a_i,b_j\). Equal \(G\) implies \(\sum a_i=\sum b_j=A\), giving
\[
G=3+2A+\sum a_i^2+\sum b_j^2.
\]
At \(A=0\) or \(A=1\) the absolute coordinate multisets of the two depth lifts are equal, and \(G=3\) or \(7\). At \(A=2\), the only triple partition shapes are \((1,1,0)\) (square sum 2) and \((2,0,0)\) (square sum 4). Identical shapes give \(G=11\) or \(15\) and equal BRC. **Different shapes give precisely \(G=13\), unequal BRC, and exactly two shapes/orbits.** Each has \(6!/(2!2!)=180\) distinct named coordinate permutations. At \(A\ge3\), both sum-of-squares terms are at least 3, whence \(G\ge3+6+6=15\).

For \(t=2\), put \(y=z+\mathbf1_6\); then \(\sum y_i=0\), \(G(z)=\sum y_i^2+6\). Equal \(L\) means the number of positive integer \(y_i\) equals the number of negative ones. When \(G\le13\) we have \(\sum y_i^2\le7\). The only cases are all \(y_i=0\) (\(G=6\)), or \(m=1,2,3\) pairs of \(+1\) and \(-1\) with the rest zero (\(G=8,10,12\)); magnitudes \(\ge2\) are incompatible with the sum and sign-count constraints at this bound. Each case has equal absolute-step-count multisets before and after the \(t=2\) shift, hence identical BRC. This proves the lower bound and exact first-loss orbit classification without numerical search.

Across all 360 different-multiplicity fibers, positive native BRC on both sides sums to \(360(630+840)=529200\); the sum of absolute pairwise differences is \(360(840-630)=75600\). Those are **positive path counts, not signed amplitudes to be cancelled**.

## Actually executed independent exact certificate

The [standalone pure-stdlib checker](https://github.com/awdawmip/enterprise-math/blob/c844b56982b7352cb1c96455e22dd8eb9f871282/research_checks/X6_LP019_SIX_AXIS_BRC_G13_PUBLIC_CHECK_20261116.py) uses three routes: direct enumeration of the \(7^6=117649\) signed ordered vectors in \([-3,3]^6\), selection by \(G\le13\); an independent sorted-coordinate orbit enumeration; and independent depth-pair generation using \(\sum z_i=-3t\) for \(t=1,2\). This finite range is exhaustive for all \(G\le13\) because any \(|z_i|\ge4\) already contributes square \(\ge16\).

Verified: **12,277** native six-vectors, **11,396** distinct \((\rho,G,L)\) fibers, **881** two-point fibers, **360** BRC-nonconstant fibers; all at \(G=13,L=7\). Both independent tests exactly match, and the two relative-address permutation orbits each have 180 named fibers. The checker was actually executed using ordinary Python and optimization modes Python -O and -OO; unconditional exception checks all passed with exit code 0 and exact 360-row digest SHA256 06da3e155ede1dbdd02652aeffbc79a42e5ca58d0eb028b028e96294c9f1c45b.

## Scope and remaining mother obligations

This is a distinct **full signed six-axis** strengthening of the [selected three-axis sharp G18 theorem](https://github.com/awdawmip/enterprise-math/blob/00cdfb5234494a6459aa1e467c47e6c34008b637/research_notes/X6_LP019_RELATIVE_NATIVE_G_AND_SHORTEST_LENGTH_SHARP_BRC_G18_20261115_1515.md). The former three-axis min-zero observer does not equal the full six-axis min-zero observer with three zero-extended coordinates. For an exact natural BRC-sensitive six-axis consumer, retaining \((\rho,G,L)\) alone is therefore unsafe. Preserve full signed named step-count/provenance or prove an operation-specific sufficient quotient.

This does not locate an actual historic LP019 wrongly subtracting positive BRC counts, nor the historic LP011 incorrect singleton-dominant caller. Full 28-LP actual downstream closure and independent Driver REQUEST_REVISION remain outstanding. Original [R063 execution support #2416](https://github.com/awdawmip/enterprise-math/issues/2416) still requires an authorized executor of six frozen original files, 17 original acceptance gates, r=1..512, true output hashes and exit status. This new calculation does NOT execute or discharge that experiment, and it is NOT Native semantic PROGRESS or a formally admitted Result.
