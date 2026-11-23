# EC49FXV — Sharp height-bounded genuine-Farey fixed-probe staircase

Date: 2026-11-23 (Asia/Shanghai). Frozen scientific input: **BRC16943**, unchanged. Parent: EC49FXU at \`5e33d4576bb0c1ef09e9169f8e17df469b8b7692\`; EC49FWS at \`95507f064ee46910b32e26d1c49e6df4a05b84fc\`. Status: **AUTHOR_PROVED / EXACT_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**.

## Model and question

Use precisely the frozen original projective predicate
\[
C_{11}(h,n)=P_{10}(h\bmod10,n\bmod10)\mathbf1_{9h+10n\not\equiv0\pmod{11}}
\]
and the lexicographic determinant-minus-one rephasing of EC49FXU. For every reduced anchor \(q=a/b\in(0,1)\) with \(b=a+c\le B\), \(a,c>0\), let \(W_{a,c}(j,v)=U(j)V(v)\) be its normalized \(10\times11\) Boolean trace. Let \(\mathcal W_B\) be the distinct normalized traces realized under this height bound (different anchors producing the same trace are one state).

The observer knows the **full indexed reflection-defect spectrum** of the hidden normalized trace, exactly as in EC49FWS. It also knows the exogenous *upper bound* \(b\le B\), but not the actual anchor or affine origin. Before learning which spectrum occurs, it must select a fixed set \(S\subset\mathbb Z/10\times\mathbb Z/11\) of physical Boolean membership sites. \(N_B\) is the minimum \(|S|\) for which every two different traces in \(\mathcal W_B\) having the same indexed spectrum differ at some site of \(S\). This is Hamming separation \(r=1\), no corrupted readings. Acquiring the bound \(B\) is not counted as an observation; if it must itself be measured, that cost belongs to a different information model.

## Theorem (sharp height staircase)

For every integer \(B\ge2\),
\[
\boxed{N_B=
\begin{cases}
0,&2\le B\le13,\\
1,&B=14,\\
2,&15\le B\le16,\\
3,&17\le B\le51,\\
4,&52\le B\le57,\\
5,&58\le B\le63,\\
6,&B\ge64.
\end{cases}}
\]

Thus the unrestricted six-probe lower bound already becomes sharp at denominator height **64**, although the normalized product image only reaches all 600 states at height **139**. All 122 equal-spectrum doubletons appear by height **109**.

An optimal fixed layout at each plateau endpoint is:

| Valid height range | Fixed sites \((j,v)\) |
|---|---|
| \(2\le B\le13\) | empty |
| \(B=14\) | \((9,10)\) |
| \(15\le B\le16\) | \((7,9),(8,10)\) |
| \(17\le B\le51\) | \((7,6),(8,6),(9,9)\) |
| \(52\le B\le57\) | \((7,6),(8,0),(9,8),(9,9)\) |
| \(58\le B\le63\) | \((7,4),(7,5),(8,0),(9,0),(9,1)\) |
| \(B\ge64\) | \((1,0),(1,1),(2,0),(2,1),(3,0),(3,1)\) |

## Proof

**Finite-state reduction and coverage.** The actual Farey normalization of EC49FXU maps every reduced anchor to one of the 50 ten-bit words \(U\) and twelve full/one-hole 11-factors \(V\). Enumerate by **denominator** \(b=2,3,\ldots,139\), and for each \(b\) all \(1\le a<b\) with \(\gcd(a,b)=1\); use \(c=b-a\), the inverse \(e=a^{-1}\pmod b\), \(h_0=(ae-1)/b\), \(n_0=e-h_0\), and the lexicographically fixed mod-10 representative to find the unique \(t_0\bmod10\). This produces every anchor with bounded denominator, without omitted branches. Each first appearance height is an exact integer minimum. There are 600 distinct products by \(B=139\), 599 at \(B=138\), and no further products are possible in the fixed 50-by-12 ambient family.

Recompute the entire 110-entry indexed spectrum for every distinct product by
\[
D_{U,V}(s,t)=2\bigl(|U||V|-|U\cap(s-U)|\,|V\cap(t-V)|\bigr).
\]
This gives 478 spectra, with 356 singleton and 122 doubleton fibers, all doubletons having a common \(V\). For an equal-spectrum pair, its Boolean difference support is precisely
\[
G\times V,\qquad G=\{j:U(j)\ne U'(j)\}.
\]
With a single deleted column \(z\), one probe \((j,v)\) separates the pair exactly when \(j\in G\) and \(v\ne z\). For full \(V\), every \(v\) is allowed. The companion program verifies each plateau's layout against **every** equal-spectrum pair present for **every** integer \(2\le B\le139\); the count of such height-pair tests is 11,644. It also independently evaluates the original integer \(C_{11}\) on each of the 600 first-appearance anchors at every one of the 110 indices (66,000 direct equalities).

**Lower bounds 1, 2, 3.** The first equal-spectrum doubleton appears at \(B=14\), with difference support \(F=\{3,4,8,9\}\) (missing column 8), so one probe is necessary. At \(B=15\) another equal-spectrum doubleton has support \(D=\{1,2,6,7\}\) (missing column 10). Since \(D\cap F=\varnothing\), at least two probes are necessary. By \(B=17\), the four actual doubleton supports
\[
C=\{3,8\},\quad
A=\{1,4,6,9\},\quad
D=\{1,2,6,7\},\quad
E=\{2,4,7,9\}
\]
all occur. \(C\) is disjoint from each of \(A,D,E\), while \(A\cap D\cap E=\varnothing\). A two-site layout would require one site in \(C\) and a second site belonging simultaneously to \(A,D,E\), impossible. Thus \(N_{17}\ge3\). These row-support arguments remain valid after excluding one column.

**Lower bounds 4, 5, 6.** Three disjoint minimal difference supports are
\[
A=\{1,4,6,9\},\qquad B_*=\{2,7\},\qquad C=\{3,8\}.
\]
At height 52, **all eleven deleted columns** occur among the genuine doubletons with support exactly \(A\). A layout with only one site in \(A\) is defeated by the doubleton whose hole equals its column, so at least **two** sites in \(A\) are needed. Doubletons with supports \(B_*,C\) are already present and force at least one site in each, giving \(N_{52}\ge4\). At height 58 all eleven holes also occur for \(B_*\), forcing two there, hence \(N_{58}\ge5\). At height 64 all eleven holes occur for \(C\), forcing two there, hence \(N_{64}\ge6\). The three supports are pairwise disjoint, so these bounds add. For \(B>139\), the ambient family is already exhausted. For intermediate heights, the monotonicity \(\mathcal W_B\subseteq\mathcal W_{B+1}\Rightarrow N_B\le N_{B+1}\) and the explicitly certified upper layouts at the right endpoints prove all the displayed plateaus.

The exact first heights when all 11 one-hole choices are present for the three minimal supports are \(52,58,64\), respectively. At height 13 the spectrum has no repeated trace; the companion certificate explicitly checks the entire finite enumeration for all preceding height bounds.

## Scientific meaning and remaining questions

The full normalized product-state surjection is not necessary for the unrestricted **fixed, no-error** observation budget to become sharp: the minimal-support ambiguity witnesses already saturate the lower bound much earlier, at \(B=64\). Height information below that threshold is an exact, observer-specified resource reduction; it does not recover anchor or origin by itself. The stronger zero-error cost with \(r\ge2\), the acquisition/verification cost of a height promise, and a typed transfer to real Heartbeat X6 are separate open questions.

Parent dependency: EC49FWQ/EC49FWS frozen 44-residue predicate and indexed spectrum semantics; EC49FXU genuine-anchor normalization. The new finite census independently reconstructs these semantics but does not re-review the frozen parent theory. No formal Task CLAIM, Result or independent Review is asserted.

**Reproduction:** run the companion \`EC49FXV_HEIGHT_BOUNDED_FAREY_VERIFY.js\` with Node.js; it outputs the JSON certificate including all 600 first-appearance witnesses, 122 equal-spectrum pair constraints, 138 height-census rows, threshold layouts, and the above direct checks. Pure integer arithmetic; no floating-point approximation.
