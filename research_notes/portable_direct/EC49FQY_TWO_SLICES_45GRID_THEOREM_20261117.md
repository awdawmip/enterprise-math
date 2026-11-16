# EC49FQY — Two exact native BRC slices, 45-node certification, and area–regret coupling

Date: 2026-11-17. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Frozen scientific object and provenance

Frozen scientific Source: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Previous frontier: EC49FQX [PR #2583](https://github.com/awdawmip/enterprise-math/pull/2583) @ `1ae6c76586a084ac3375360ea95cb3e58b8b464a`; 43 already certified price nodes. Frozen original master SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; original named-root profile CSV SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

Native BRC category 16943: 310 original configurations, 141 distinguishable *complete named-root* profiles, 144 terminal observations, 84 named-root observations, 228 physically labeled legal queries, 209 distinct response partitions. Original profile multiplicities, named-root identity, response branches and provenance are retained. The calculation uses positive-weighted sensing; it does not assert signed amplitude cancellation or modify P000/Heartbeat World.

For root price \(r=xt\), terminal price \(t>0\), \(x\ge1\), and \(\lambda\in[0,1]\), use \(p_\lambda(i)=(1-\lambda)/141+\lambda m_i/310\), where \(m_i\) is the original configuration multiplicity. The objective \(V(\lambda,x)\) is the global minimum expected cost, divided by \(t\), over all *finite legal adaptive decision trees* distinguishing the 141 profiles. There is no depth cap.

Three previously saved, fully replayed feasible tree families give:
\[
\begin{aligned}
 A&=(1-\lambda)(6x+290)/141+\lambda(6x+751)/310,\\
 B&=(1-\lambda)(5x+293)/141+\lambda(5x+704)/310,\\
 C&=(1-\lambda)(5x+295)/141+\lambda(5x+685)/310.
\end{aligned}
\]
Set \(K(x)=7557-169x\), \(\gamma(x)=310(3-x)/K(x)\) for \(1\le x\le3\), and \(\beta=620/3299\).

## Theorem 1 — Two new exact all-real-prior slices

For both \(x=75/32\) and \(x=77/32\), for **every real** \(0\le\lambda\le1\),
\[
V(\lambda,x)=\min(A,B,C).
\]
Their first transition points are respectively \(\gamma(75/32)=2170/76383\) and \(\gamma(77/32)=190/7381\). The complete sets of optimal *physically labeled* first observations are \(\{32,34\}\) on \(0\le\lambda<\gamma(x)\), \(\{32,34,140,142\}\) at \(\gamma(x)\), \(\{140,142\}\) on \(\gamma(x)<\lambda<\beta\), \(\{16,23,140,142\}\) at \(\beta\), and \(\{16,23\}\) on \(\beta<\lambda\le1\).

**Proof.** Eight full exact integer unrestricted subset-Bellman computations cover the four anchors \(0,\gamma(x),\beta,1\) for each new price. Every physical first observation was checked; all tied optimal complete decision trees were replayed against the frozen 141 profiles. A structurally independent weighted-subset Bellman implementation reconstructed the profiles and 228 actions from the original input and verified all eight objectives and all optimal first-query labels. Every nontrivial query strictly partitions a finite state set at positive cost, so the recursion covers *all* finite legal decision trees. For fixed \(x\), any fixed tree cost is affine in \(\lambda\), and the unrestricted optimum is their concave lower envelope. At both endpoints of each phase interval the appropriate feasible affine branch agrees with the unrestricted optimum; concavity and feasibility give equality throughout. For a fixed first label, its constrained optimum is also concave in \(\lambda\), and its difference from an exactly optimal affine branch is nonnegative and concave. A label missing from at least one endpoint's minimizer set is strictly suboptimal throughout the open interval; this establishes *all* first-query sets and boundary ties. QED.

## Theorem 2 — Certified fraction of the full continuous parameter rectangle

Add \(75/32,77/32\) to the previous 43-point price grid on \([1,3]\), producing 45 price nodes and 44 intervals. At a fixed price endpoint every prior in each of the three phases is solved by Theorem 1 and its predecessors. The cost difference between any two *fixed* complete trees is bilinear in \((x,\lambda)\); nonnegativity at the four corners of a price/prior rectangle implies nonnegativity throughout. For \([a,b]\), this certifies the A-region through \(\lambda\le\gamma(b)\), the B-region over \(\gamma(a)\le\lambda\le\beta\), and the C-region for \(\lambda\ge\beta\). Every potentially uncertified part lies inside \(\gamma(b)<\lambda<\gamma(a)\).

The exact area of these containing strips is
\[
S_{45}=\sum_{[a,b]}(b-a)(\gamma(a)-\gamma(b))
=\frac{162317745998378463895}{39951040674583873370736}.
\]
Thus the *rigorously certified fraction* of \([1,3]\times[0,1]\) is at least
\[
1-S_{45}/2
=\frac{79739763603169368277577}{79902081349167746741472}
=99.7968541704326089\ldots\%.
\]
The previous 43-node lower bound was 99.7885176148383968...%. The inherited independent exact result for \(x\ge3\) remains unchanged.

## Theorem 3 — Improved all-price regret guarantee

For **all** real \(\lambda\in[0,1]\), \(x=r/t\ge1\) and \(t>0\), the best of the three explicitly feasible full trees satisfies
\[
0\le C_{\rm strategy}-C_{\rm optimal}\le
\frac{50(37/16-9/4)}{
  (\sqrt{K(9/4)}+\sqrt{K(37/16)})^2}\,t
=0.0001089386474593920050\ldots\,t.
\]
The inherited exact chord/concavity certificate gives interval regret upper bound \(R(a,b)=50(b-a)/(\sqrt{K(a)}+\sqrt{K(b)})^2\,t\); the inherited \(x\ge3\) exact theorem gives zero beyond the finite grid. All 44 bounds were compared by exact rational arithmetic and *integer-square-root brackets* of width \(10^{-18}\). The unique maximum is on \([9/4,37/16]\), with its certified lower bracket strictly exceeding the upper bracket for all other intervals. The predecessor bound was 0.0001092604962592316995... t. This is a uniform worst-case *guarantee*, not a claim that the regret is attained. QED.

## Theorem 4 — Exact certification area–regret coupling

For every \(1\le a<b\le3\), define the containing-strip area \(S(a,b)=(b-a)(\gamma(a)-\gamma(b))\) and the interval certificate \(R(a,b)\) above. Put \(q=\frac{169}{50}R(a,b)/t\). Then
\[
\boxed{S(a,b)=\frac{16\cdot2185500}{169^2}\,
\frac{q^2}{(1-q^2)^2}}.
\]
**Proof.** \(\gamma(a)-\gamma(b)=2185500(b-a)/(K(a)K(b))\). With \(u=\sqrt{K(a)}\), \(v=\sqrt{K(b)}\), the identity \(169(b-a)=u^2-v^2\) gives \(q=(u-v)/(u+v)\) and
\(S=(2185500/169^2)(u/v-v/u)^2\).
But \(u/v-v/u=4q/(1-q^2)\). QED.

An exact local refinement law follows: inserting any \(c\in(a,b)\) decreases this strip-area upper bound by
\[
\Delta S=\frac{2185500(c-a)(b-c)}{K(c)}
 \left(\frac1{K(a)}+\frac1{K(b)}\right)>0.
\]
Thus the finite-grid area and minimax regret certificates are governed by one exact rational/log-price spacing mechanism. This is a new *derived identity within the saved BRC certificate formulas*, not an independent physical-world theorem.

## Executed verification, storage and next question

The accompanying compact index records the eight independently recomputed integer objectives, all physical first labels and witness SHA256s. The accompanying standalone 45-grid script checks exact rational areas and integer-square-root envelopes. The **full 8 raw JSON certificates**, frozen master and CSV, two source-reconstruction/Bellman implementations, all witness trees, successful independent run logs, full predecessor EC49FQX evidence archive and per-file SHA256 manifest are in the attached self-contained archive:
`EC49FQY_TWO_SLICES_45GRID_AREA_REGRET_IDENTITY_EVIDENCE_20261117.tar.xz` (SHA256 `d471c8e43bfdf3dfb89362019aa5a728acb2da91f262d0e6fced43048df3ed00`; 34 manifest entries verified). The compact GitHub representation intentionally references that complete conversation artifact rather than claiming those raw witness JSON bytes are in this PR.

Open scientific problem: establish a parametric native Bellman lower bound over the remaining 44 narrow strips or exhibit a complete physically labeled adaptive tree with an *exact* strict cost improvement at a rational interior point. Attempted independent computations at \(73/32\) and \(191/64\) remained incomplete and are excluded from the theorem.

## Control/authority observation

The old `RS-EC49AS` control directory was absent. A fresh 2026-11-17 01:28 +08:00 Sites continuation request `r4-20261117-0128-ec49as-current-continuation` was **not sent** due to `BACKEND_IDENTITY_CHECK_UNAVAILABLE`. Own historical registered session `MCP-44cfc4e6f2094f96861854ebefc77e84` was read through recovery metadata, with `execution_authorized=false`. This file is independent portable scientific evidence: no active formal CLAIM, authenticated owner takeover, Result, Review, or Activity scientific checkpoint is claimed.
