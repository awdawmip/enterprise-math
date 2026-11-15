# X6 LP019 / LP003 — sharp native N-BRC non-factorization through (min-zero address, native squared norm)

**Date:** 2026-11-15 15:00 Asia/Hong_Kong. **Mother:** \`RS-X6-LEGACY-PLANE-RECONCILIATION\`; publication \`TP2-B4A441B23DA3159232C2\`. **Researcher:** \`EM-X6-FB6990\`, own Research SID \`MCP-082892eb480e45dea6d4b9fcc0491034\`. **Status:** \`AUTHOR-PROVED / EXACT FINITE CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED\`.

## Source and previous frontier

Frozen native mathematics: \`awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:p000_reality_foundation.json\`, the centered signed X6 Cell torsor, and the named signed three-axis research slice with omitted native components **explicitly set to zero in this selected embedding**. Historical comparison pin: \`fd2bcff10ca6e147348b6c1236027fc0d2877df3\`. Current joint-observer preservation remains binding. All native shortest path counts are nonnegative integers; source labels and path histories are preserved before quotienting.

Prior genuine result, already published and **not recomputed**: [NGSVC signed-cube depth-fiber repair](https://github.com/awdawmip/enterprise-math/blob/dded9b63ea7723053d73a8f2f8070d7d8e37c583/research_notes/X6_LP019_NGSVC_MINZERO_CUBE_FIBER_AND_SIGNED_BRC_LOSSLESS_LIFT_20261115_1400.md) proved that \`r=minzero(z)\` alone does not determine native norm or native N-BRC. This new result asks the sharper question: does additionally retaining the *correct native squared norm* repair the BRC loss?

## Theorem — sharp first information loss

On the selected signed native \(\mathbb Z^3\) displacement slice, define

\[
 h=\min_i z_i,\qquad r_i=z_i-h,\quad \min_i r_i=0,\quad
 G(z)=\sum_{i=1}^{3}z_i^2,\quad
 B(z)=\frac{(\sum_i |z_i|)!}{\prod_i |z_i|!}.
\]

Then:

1. On the **entire unbounded set** of triples whose relative spread \(\max_i r_i\le2\), the observable pair \((r,G)\) determines \(B\) exactly.
2. At relative spread **3**, this property fails. One explicit pair is
   \[
   z=(0,0,3),\qquad z'=(-2,-2,1).
   \]
   Both have \(\rho(z)=\rho(z')=(0,0,3)\) and \(G(z)=G(z')=9\), while \(B(z)=1\) and \(B(z')=5!/(2!2!1!)=30\).
3. The first such failure in ascending nonnegative native squared norm is **\(G=9\)**. All selected signed triples with \(G\le8\) have a BRC value fixed by \((r,G)\). At \(G=9\) exactly six **ordered** relative-address fibers have differing BRC values; each contains one BRC-1 endpoint and one BRC-30 endpoint.

The two paths' lengths are respectively \(L=3\) and \(L=5\); the squared native norm is equal. Hence **even the exact intrinsic native norm together with a complete min-zero relative address cannot replace the integer common depth for native shortest-path counting**.

## Proof

For fixed \(r\), all native lifts have the form \(z=r+h\boldsymbol1\), \(h\in\mathbb Z\). Write \(s=\sum_i r_i\), \(q=\sum_i r_i^2\). Then

\[
 G(r+h\boldsymbol1)=3h^2+2sh+q.
\]

If distinct integer depths \(h\ne h'\) share the norm, subtraction yields

\[
 0=(h-h')[3(h+h')+2s],\qquad h+h'=-2s/3.
\]

Thus \(3\mid s\). This is an exact arithmetic *candidate* criterion, not a sufficient condition for BRC loss.

For \(\max r\le2\), after coordinate permutation \(r=(0,a,b)\), with \(0\le a\le b\le2\). The condition \(3\mid s=a+b\) leaves only \((a,b)=(0,0)\) or \((1,2)\). For \((0,0,0)\), equal norm depths are \(h'=-h\), and all coordinate magnitudes agree. For \(r=(0,1,2)\), \(h'=-2-h\), so

\[
 (h',h'+1,h'+2)=(-h-2,-h-1,-h)
\]

is the coordinate-reversed, sign-negated form of \((h,h+1,h+2)\). Thus the multiset of absolute step counts, length and multinomial BRC are identical for *all* integer depths. This proves the unbounded first statement.

For a pair at \(G\le8\), its spread satisfies
\[
(\max_i z_i-\min_i z_i)^2\le 2G(z)\le16;
\]
so \(\max r\le4\). Spread 0–2 was covered above. At spread 3, the divisibility criterion permits only \(r=(0,0,3)\) and \(r=(0,3,3)\), up to permutation. Each norm quadratic has its integer vertex at \(h=-1\) or \(h=-2\), with minimum \(G=6\); two **distinct** reflected integer depths first occur one step either side, yielding \(G=9\). At spread 4, the only divisible case is \(r=(0,2,4)\), whose integer quadratic vertex is \(h=-2\), norm \(G=8\); the first distinct equal-norm pair is \(h=-1,-3\), norm \(G=11\). Hence no failure occurs at \(G\le8\), while the displayed \(G=9\) pair attains the bound.

At \(G=9\), the six differing ordered fibers correspond to the three coordinate permutations of \((0,0,3)\) and the three permutations of \((0,3,3)\). Each has native BRC multiset \(\{1,30\}\), completing the classification.

## Exact execution certificate

The [standalone checker](https://github.com/awdawmip/enterprise-math/blob/b470f97bd2c4fb3280691624fd18e872746b4041/research_checks/X6_LP019_RELATIVE_PLUS_NORM_SHARP_BRC_G9_20261115_1500.py) is immutable at commit \`b470f97bd2c4fb3280691624fd18e872746b4041\`, Git blob \`b7d34277deca5f342aad2c926f63bf71d8f48ce7\`, source SHA256 \`3a041723dcae8347cf1ed1ffb37eed3ebfea0764101f1f2bdd88f242a8724dca\`.

Executed Python stdlib exact enumeration of all 343 signed integer triples in \([-3,3]^3\), retaining the 3D subset with \(G\le9\), and separately testing every min-zero \(r\in\{0,1,2\}^3\) over integer depths \(h=-20,\ldots,20\). Exit code **0**, all assertions passed:

\`\`\`text
PASS_X6_LP019_SHARP_RELATIVE_PLUS_NORM_BRC_LOSS_G9
exact_fibers=110 differing_fibers=6
earliest_G=9; differing_BRC_values=1,30; spread_threshold=3
\`\`\`

The printed Python runtime also had an unrelated startup warning from spreadsheet runtime warmup, after which the actual checker terminated successfully. The theorem itself follows from the exact argument above; finite verification is supporting evidence.

## Information-preservation and actual consumer scope

The compressed \((r,G)\) readout preserves full quadratic length but can erase **native path multiplicity and primitive-step provenance**. A future consumer of \(B\), ordered paths or branch identity must retain \(h\), original \(z\) or an independently proved operation-specific sufficient path carrier. This is a stronger loss witness than the preceding \`r\`-only example and a precise test case for LP003/LP005/LP019/LP026 native consumer contracts.

No particular **historical erroneous LP011 argmax** or **historical LP019 positive-N-BRC sign subtraction** invocation has been established by this proof; those provenance issues remain open. Original R063 Stage0 17 gates/512 regression, issue [#2416](https://github.com/awdawmip/enterprise-math/issues/2416), remains a separate same-object execution requirement.

## Durable continuation

- **Mother / frozen inputs:** above exact Task, publication, P000/source pins.
- **Preserved Source:** 31 Native semantic units last confirmed via current original continuation, GitHub #32 Stage3 ordered-source-rank result and Activity #51, GitHub #33 NGSVC signed-depth repair and Activity #52.
- **New exact source:** this note plus checker commit \`b470f97bd2c4fb3280691624fd18e872746b4041\`; new author-side contribution awaits proper Activity CAS and Native semantic publication under the same valid Researcher/CLAIM/RUN.
- **Do not repeat:** prior 31 native units, source #32/#33 science, historical accepted 72/846 and R063 N2500 certificate, earlier failed/denied writes; no borrowing another lane.
- **Next:** reconcile original pending semantic request under the same SID/RUN; publish saved #32/#33/new result if current winning claim permits; continue exact LP011/LP019 caller provenance and 28-LP consumer closure; follow real #2416 runner intake and independent Driver revision.
