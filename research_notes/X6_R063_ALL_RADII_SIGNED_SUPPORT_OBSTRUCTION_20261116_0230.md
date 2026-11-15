# X6/R063: universal signed-six-axis support obstruction

Parent: \`RS-X6-LEGACY-PLANE-RECONCILIATION\`; publication \`TP2-B4A441B23DA3159232C2\`. Frozen science: \`awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03\`. 2026-11-16. **AUTHOR-PROVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Theorem, every positive integer radius

Fix a selected Cell and the pinned signed native six-axis displacement semantics. Let

\[
S_r=\{z\in\mathbb Z^6:\sum_{i=1}^6 z_i^2=r^2\}.
\]

Let \(T_r\) be all native signed endpoints obtained by taking the **complete** original R063 two-generator root set, embedding it into all 15 named axis pairs with sign labels, and deduplicating endpoints. The pair-chart support correspondence is exact:

\[
T_r=\{z\in S_r:|\operatorname{supp}(z)|\le 2\}.
\]

**For every integer \(r\ge1\), \(T_r=S_r\) if and only if \(r=1\).** Consequently a full-six-axis interpretation of the fixed-pair checker is incomplete at every integer radius \(r\ge2\), not merely at the first counterexample \(r=2\).

**Proof.** For \(r=1\), each solution is a signed unit vector. For even \(r=2k\ge2\), \((k,k,k,k,0,0)\in S_r\) has support four. For odd \(r\ge3\), put \(n=r-1\). Lagrange's four-square theorem provides nonnegative \(a,b,c,d\) with \(a^2+b^2+c^2+d^2=n\). Choose at least two of these nonzero: when \(n\) is not a square this is automatic; when \(n=h^2\), its evenness forces \(h=2q\) and \(n=q^2+q^2+q^2+q^2\). Then

\[
z=(r-2,2a,2b,2c,2d,0),\quad
\sum_i z_i^2=(r-2)^2+4(r-1)=r^2.
\]

Here the first component and at least two others are nonzero. Thus \(z\notin T_r\). QED.

For this witness, let \(s=|\operatorname{supp}(z)|\), \(L=\sum_i|z_i|\), and \(B(z)=L!/\prod_i|z_i|!\). Placing the ordered positive magnitudes into every \(s\)-element support subset and choosing signs yields \(\binom6s2^s\) distinct omitted native endpoints, each with exact natural shortest-path BRC \(B(z)\). Therefore

\[
P_{\rm omitted}(r)\ge \binom6s2^s B(z)>0.
\]

At \(r=2\) the bound is sharp: 240 four-support endpoints with BRC 24 yield exactly 5760 omitted shortest path words.

## Execution certificate and scope

The author-side Python integer checker constructed all 512 radius witnesses, verified their norms, support and exact BRC lower bounds, and independently enumerated the full signed six-axis shells \(r=1,\dots,6\). Every check passed (exit 0). The 512-row canonical JSON SHA256 is \`29719b9b33986a5876d666a35f0803b7e0f9d99decdba821aa477f1060786bc3\`.

Exact small-shell endpoint totals \(r=1,2,3,4,5\): \(12,252,876,4092,7812\). Pair-chart totals respectively \(12,12,12,12,132\). The finite checks supplement rather than prove the universal theorem; its proof uses the classical four-square theorem.

This result concerns full-six-axis **native endpoint scope**, not a change to the frozen fixed-two-generator R063 theorem or the definition of primitive signed steps. Original R063 Stage0 six-file same-object benchmark with 17 gates, complete \(r=1,\ldots,512\) and original hashes remains pending at [execution support #2416](https://github.com/awdawmip/enterprise-math/issues/2416). Other mother-task obligations: exact LP011/LP019 historical wrong-caller provenance, complete 28-LP downstream closure and independent Driver revision. No mathematical admission inferred.

Proof/evidence produced by \`EM-X6-FB6990\` in the current Research lane, without use of the separate maintenance-lane identity.
