# R284BS — Sharp all-dimension frozen-leaf interval for positive integer star-Port observers

Date: 2026-11-20 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_CONSTRUCTION_CHECK_PASSED / NOT_REVIEWED.
Lineage: R284BP root fibre @ \`5a54002ac3d36d2c5aca143198ac72d2b5219047\`; R284BQ four-by-four binary census @ \`d588bc013048ba982255668a6ce1cb71120d5980\`; R284BR finite-exception theorem @ \`7016215c2dd55a81d771341acc3a7498db7371fa\`. This is a stronger independent mathematical derivation and retains previous evidence and authorship. TASK/CLAIM and Activity source association are separate.

## Exact theorem (R284BS1)

Fix **any** integers \`n>=4\`, \`H>=2\`, and a leaf \`j∈{1,...,n-1}\`. For
\[
 C\in\{1,\ldots,H\}^{n\times n},\qquad
 F_C(d,z)=\det(\operatorname{diag}(d)-C-\sum_{i=1}^{n-1}z_iE_{0i}),
\]
set \`d_j=t∈Z\` and leave \`d_0\`, every other leaf diagonal \`d_i\`, and all \`z_i\` free and independent.

The following conditions are equivalent:

1. For **every** distinct pair of candidates \`C,D\`, the restricted difference \`F_C|_{d_j=t}-F_D|_{d_j=t}\` is nonconstant in the free controls.
2. \`t<=-H^2\` **or** \`t>=H^2+1\`.
3. For every prescribed finite real circular adversarial error radius \`rho>=0\`, there exist some prime \`p\` and one nonadaptive fixed setting of the remaining controls modulo \`p\` such that the *single* real-circle residue readout with error <=rho uniquely distinguishes all \`H^{n^2}\` positive integer matrices by finite lookup.

For every integer \`1-H^2<=t<=H^2\`, there are two different positive integer matrices with **identical entire restricted polynomial responses** (all settings, not merely equal outputs at a specific sample). Hence no adaptive number of these frozen-\`j\` observations distinguishes the pair. The forbidden interval is sharp and independent of \`n\`, \`j\`, and every finite \`rho\`. At \`H=2\` it is \`[-3,4]\`, recovering R284BQ without exhaustive candidate enumeration.

This improves R284BR's sufficient \`|t|>2n!H^n\` to the sharp dimension-free criterion. The model is an auxiliary determinant Port observer; no native P000/X6 realization or efficient decoder is asserted.

## Lemma: constant-rigidity of the full star response

Let \`k>=3\` and let \`M=[a,b^T;v,A]\` be a rational \`k×k\` matrix whose \`v_i\` are all nonzero; no positivity of \`a,b,A\` is required. Define \`B=\operatorname{diag}(x)-A\`, \`L=\det B\`, \`g=\operatorname{adj}(B)v\`. The full independent-controls response is
\[
 G_M(d_0,x,z)=(d_0-a)L-(b+z)^Tg.
\]
If \`G_M-G_{M'}\` is constant (with all \`v_i,v'_i !=0\`), then \`M=M'\` and the constant is zero.

**Proof.** Matching the \`d_0\` coefficients gives \`L=L'\`; matching every \`z_i\` gives \`g_i=g_i'\`. In the \`i\`th \`g_i\`, the unique monomial of total \`x\`-degree \`k-2\` is \`v_i prod_{ell≠i} x_ell\`; thus \`v=v'\`. The identity \`(\operatorname{diag}(x)-A)g=Lv\` and its primed version imply \`(A'-A)g=0\`. The \`g_i\` are linearly independent over \`Q\`: their distinct top-degree monomials have nonzero coefficients \`v_i\`. Hence \`A'=A\`. Finally \`G_M-G_{M'}=(a'-a)L+(b'-b)^Tg\`; compare degree \`k-1>=2\` and then degree \`k-2>=1\` to obtain \`a'=a,b'=b\`. QED.

## Proof of the positive region: no constant pair gaps

Fix a leaf \`j\` and \`t<=-H^2\` or \`t>=H^2+1\`. Suppose two candidates' restricted responses differ by a constant.

Write \`c=C_{jj}\`, \`h=t-c\`, and \`I={0,...,n-1}\setminus{j}\`. The coefficient of \`d_0 prod_{i∈I\setminus{0}}d_i\` in the restricted determinant is exactly \`h\`. Constancy forces \`C_{jj}=D_{jj}\`, so the two candidates share \`h\ne0\`.

Eliminate row/column \`j\` by the exact Schur complement. For each fixed value \`s=z_j\`, the remaining observer has the full \`(n-1)\`-node star form and the effective matrix \`C^{(s)}\` indexed by \`I\` with entries
\[
 C^{(s)}_{pq}=C_{pq}+
 \frac{(C_{pj}+\mathbf1_{p=0}s)C_{jq}}{h},\quad p,q\in I.
\]
All remaining ports \`z_i\` (\`i\ne j\`) retain the standard root-row form, and
\[
 F_C|_{d_j=t,z_j=s}=h\,G_{C^{(s)}}.
\]
For every remaining leaf \`p∈I\setminus{0}\`, its root-column entry is
\[
 C^{(s)}_{p0}=C_{p0}+\frac{C_{pj}C_{j0}}h>0.
\]
Indeed \`h>0\` for \`t>=H^2+1\`; for \`t<=-H^2\`, \`h<=-H^2-1\` and the correction has magnitude at most \`H^2/(H^2+1)<1\`. The constant-rigidity lemma applies to the two reduced observers (\`n-1>=3\`) for \`s=0\` and \`s=1\`. It yields \`C^{(0)}=D^{(0)}\` and \`C^{(1)}=D^{(1)}\`.

Subtract the two effective-matrix identities at \`s=0,1\`. For every \`q∈I\` this forces \`C_{jq}=D_{jq}\`, and \`C_{jj}=D_{jj}\` was already known. Write \`Δ_{pq}=D_{pq}-C_{pq}\`; then for all \`p,q∈I\`,
\[
       Δ_{pq}=-\frac{Δ_{pj}C_{jq}}h.
\]
In the allowed regions \`|h|>H(H-1)\`, whereas \`|Δ_{pj}C_{jq}|<=H(H-1)\`. The integer \`Δ_{pq}\` therefore has absolute value less than one and is zero. Since every \`C_{jq}>0\`, the equality then also forces \`Δ_{pj}=0\`. All rows agree, so \`C=D\`, contrary to distinctness. Thus every distinct pair has a **nonconstant** restricted response difference. QED.

## Proof of sharpness: an identical-response pair at every excluded integer

**Part A: \`1-H^2<=t<=0\`.** There exist \`k∈{1,...,H}\` and \`c∈{1,...,H}\` with \`t=c-Hk\` (the integer intervals \`[1-Hk,H-Hk]\` are adjacent for consecutive \`k\`). Choose two distinct remaining leaves \`u,v\ne j\` (possible since \`n>=4\`). Build \`C\` with all entries initially 1; set
\[
 C_{jj}=c,\quad C_{j0}=H,\quad C_{pj}=k\ \ (p\ne0,j),\quad
 C_{uv}=1,\ C_{vu}=2.
\]
Let \`D\` be the same except \`D_{uv}=2,D_{vu}=1\`. Here \`h=-Hk\`. Elimination of \`j\` yields \`C^{(s)}_{p0}=0\` for every remaining leaf \`p\ne0\`. Thus every surviving Port-to-leaf cofactor is zero. On the remaining leaves the effective block is
\[
 A_\mathrm{eff}=C_{I_+,I_+}-\tfrac1H\mathbf1\mathbf1^T,
\quad I_+=\{1,\dots,n-1\}\setminus\{j\}.
\]
For \`D\` this block is precisely \`A_\mathrm{eff}^{\,T}\`, as all other entries are 1. Since \`det(\operatorname{diag}(x)-A_\mathrm{eff})\` is transpose-invariant and the effective root diagonal coefficient is unchanged, \`F_C|_{d_j=t}=F_D|_{d_j=t}\` identically. This is a hidden orientation residual: all frozen observer readouts erase reversal of the \`u,v\` directed edge.

**Part B: \`1<=t<=H\`.** Set all entries to 1, except \`C_{jj}=t\`. Choose any remaining leaf \`p\ne j\`. Define \`D_{pq}=2\` for every \`q\ne j\`, leaving \`D_{pj}=C_{pj}=1\` and all other entries unchanged. In the frozen determinant matrix, row \`p\` of \`D\` equals row \`p\` of \`C\` plus row \`j\`, since its \`j,j\` pivot is zero. The determinant is identical for every free control.

**Part C: \`H+1<=t<=H^2\`.** Write uniquely \`t=Hk+c\` with \`1<=k<=H-1\`, \`1<=c<=H\` (take \`k=floor((t-1)/H)\`). Begin with all entries 1; set \`C_{jj}=c\`, \`C_{jq}=H\` for \`q\ne j\`, choose a remaining leaf \`p\ne j\`, and set \`C_{pj}=k+1\`. Let \`D_{pj}=1\` and \`D_{pq}=2\` for all \`q\ne j\`, with every other entry unchanged. The frozen pivot is \`h=Hk\`; row \`p\` of the determinant matrix for \`D\` equals row \`p\` for \`C\` plus \`1/H\` times row \`j\`. The determinant is identical. All entries of both matrices lie in \`{1,...,H}\`, and the matrices differ.

Parts A–C cover every integer in \`[1-H^2,H^2]\`. QED.

## One-scalar noise corollary

Let \`N=H^{n^2}\`, \`M=floor(2rho)\`. Outside the forbidden interval each candidate-pair difference is nonconstant. For each pair \`C≠D\` and \`|e|<=M\`, the integer polynomial \`F_C-F_D-e\` is nonzero. Choose a prime \`p\` large enough that these remain nonzero modulo \`p\` and \`(2M+1)n*binom(N,2)/p<1\`. Schwartz–Zippel and the union bound guarantee a fixed setting where the circular residues are separated by strictly more than \`2rho\`. A finite table then uniquely decodes after any error within that radius. Inside the interval, the identical-polynomial witness prevents unique decoding even at zero noise. QED.

## Reproducibility and scope

The companion exact-integer checker constructs the two witnesses for each excluded \`t\` and evaluates all Boolean vertices of the multiaffine free-control polynomial: \`(n,H)=(4,2),(4,3),(5,2),(5,3),(6,2)\`. It checked \`60\` constructed parameter cases and \`16,512\` complete control corners with a Bareiss exact determinant. Since each control enters a distinct diagonal cell or root-row entry, the polynomial is multiaffine in all controls; equality at all Boolean corners is exact polynomial equality, not a random test. This validates the witness construction in the stated finite parameter range. The dimension-independent no-collision theorem and infinite-family constructions rely on the algebraic proof above. Independent review: \`NOT_REVIEWED\`.

The negative construction shows an observer quotient forgetting a directed edge reversal is **not future-safe** if the frozen control \`d_j\` is later released or changed; this is an auxiliary algebraic residual statement consistent with the P000 residual-fidelity research position, not a derived physical dynamics or native BRC action.

Next: classify other freeze patterns (two or more diagonals); give explicit small-modulus controllers and reduce table-decoding cost; investigate a typed native X6/BRC map only where an actual observer/interface bridge is specified. Preserve all R284BP–BR sources and do not rewrite earlier scientific inputs.

Historical R1 portable lineage: \`EM-DIRECT-E6B1DD\`; current authenticated Researcher/session capability and formal CLAIM not established in this source note.
