# Addendum: an exact legal 13-arc Blackwell contact on the interior 14-arc wall

Date: 2026-11-10, continuation of this PR's four-dimensional product-face theorem. Frozen global and EM scientific inputs remain \`a01383f825ef9d43b4b754254303298c64041568\` and \`86149263e38c22292c9def1e0f69092efa1be77e\`. **This constructs 13-arc transport solutions; it does not yet establish that their minimum support is 13.** The original R5 mother question remains open at the exact optimality check for these new points.

Keep the fixed seven-likelihood ratio physical family, centre \`z_c\`, and 7D 14-arc hyperplane \`H\` from \`RESEARCH.md\`. The exact target row-1 mass at zc equals
\[
\alpha=\mu_1(z_c)=\frac{16932541854726549}{313632293625596000000}>0.
\]
Choose the exact tangent vector
\[
d=\left(-\frac{11579}{421},0,0,0,1,0,0,0\right),\qquad n\cdot d=0,
\]
and the new rational physical point \(\boxed{z_{13}=z_c+\alpha d}\).

The frozen parameter map gives \(\mu_1(z_{13})=0\). All five physical equalities remain exact; all 26 physical capacity slacks are nonnegative and the only zero indices are 4,15,19,23 (index 19 is the newly reached \(\mu_1=0\) face). The smallest strictly positive physical slack equals
\[
\frac{3836062555208901}{156816146812798000000}.
\]

The same 18-arc four-dimensional transport face is solvable at z13. Recalculate each of its 12 previously identified 14-column vertex solutions exactly. For **each** of the twelve product choices \(G_1\times G_2\times G_3\), the common edge \((1,5)\) has *exactly zero* mass and all other thirteen weights are strictly positive, with minimum among all choices
\[
\frac{131977087948072769}{313632293625596000000}.
\]
The resulting twelve positive-13-arc support sets are distinct. All twelve solutions satisfy the **full original 21 Blackwell marginal/martingale equalities**, not only the 15-row reduction. For instance one support is
\`\`\`text
(0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6),
(2,1),(3,2),(0,3)
\`\`\`

Therefore this exact lawful physical point satisfies **\(N_{\min}(z_{13})\leq13\)**. This is a constructive 13-arc special solution and the first such contact in the present 18-arc family. It is outside the small local neighborhoods used for earlier generic 14/15 claims, so their hypotheses are untouched. The 13-edge point is on a physical marginal-zero facet and inside the seven-dimensional affine H; it shows an explicit two-condition intersection of \(\mu_1=0\) and the internal sparse-support wall.

**Reproduction:** \`VERIFY_13_CONTACT.py\` invokes the same PR's independently verified \`VERIFY_FACE.py\`, constructs the exact new physical point and checks all twelve 13-arc supports, 21 original equations and 26 physical inequalities using exact \`Fraction\` and SymPy rationals. \`EXACT_OUTPUT_13.txt\` records an actual execution. The calculation makes no claim about 12-or-fewer support impossibility.

**Next decisive step:** Determine whether any 12-or-fewer-arc Blackwell coupling realizes the exact new right-hand side among the full 30 allowed arcs. Use a current exact dual/forced-edge certificate if valid at z13, or provide a separate complete finite rank/separation enumeration with scope. If excluded, the new point becomes a certified minimum-13 contact.