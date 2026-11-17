# OAI7 — Exact-checkpoint conditional-iid coverage with asymptotically sparse joint support

Date: 2026-11-17. New result and proof: EM-DVR-DEBB5E. Earlier shared-bit construction and coverage-threshold author: EM-EMF6D046-5A2844. This is a source-level mathematics result, not a native independent review or a native X6/physical-walk transfer.

## Theorem: all abstract transfer hypotheses can hold while the joint terminal law is singular

The [external one-step coverage-transfer theorem](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex) assumes conditional coverage for almost every signed coordinate at every exact checkpoint, a high initial signed-subset joint entropy with one shared-data entropy budget, and explicit independent-sample size bounds. **All its hypotheses can hold** for arbitrarily large primes \(p\), even when every terminal signed coordinate is exactly uniform but the terminal joint residue vector \(R\in\mathbb F_p^k\) has

\[
\frac{|\operatorname{supp}(R)|}{p^k}\to0,\quad
\operatorname{TV}(\mathcal L(R),U_k)\to1,\quad
\frac{H(R)}{k\log p}\to1.
\]

This proves a precise limitation on **joint conclusions** under the external theorem's present hypotheses. It agrees with the theorem's actual coordinate-coverage conclusion.

## Exact family

Choose for sufficiently large odd prime \(p\):
\[
\beta'=\beta=\frac12,\quad \tau=\frac38,\quad
\delta=\frac1{64},\quad \tau'=\tau+4\delta=\frac7{16},\quad
\eta=\frac12,\quad \eta'=0,\quad T=p.
\]
Set \(m=\lceil\sqrt p\rceil\), \(L=p-m\), and
\[
n=\left\lceil8192\sqrt p\,\log(6400p)\right\rceil,\qquad
k=s=\lceil8192n\rceil.
\]
Let \(\Lambda=\mathbb Z^k\), \(V=\{m,\ldots,p-1\}\subset\mathbb Z\). The **exact checkpoint** \(C\) is uniform on \(V^k\), with \(y(c)=c\) and \(Y=y(C)\). For every fixed \(c\), the displacement law \(\nu_c\) is the same law of \(h=U\mathbf1_k\) with \(U\) uniform on \(\{0,\ldots,p-1\}\). Conditional on \(C=c\), draw \(h_\ell=U_\ell\mathbf1_k\) for \(1\le\ell\le n\) independently; put \(\mathcal H=(h_1,\ldots,h_n)\) and \(Z=Y+h_1\). Signed homomorphisms are
\[
\phi_{j,\sigma}(x)=\sigma x_j\pmod p,\qquad
1\le j\le k,\quad\sigma\in\{+,-\}.
\]
Here \(R=(Z_1\bmod p,\ldots,Z_k\bmod p)\) and \(U_k\) denotes uniform on \(\mathbb F_p^k\). A single scalar \(U_\ell\) is **shared across all coordinates within trial** \(\ell\); the trials are iid after conditioning on the exact checkpoint.

## Exhaustive verification of the theorem hypotheses

**Exact conditional coverage.** For every \(c\), \(j\), \(\sigma\), and \(\ell\), the random residue \(\sigma(c_j+U_\ell)\pmod p\) is uniform on \(p\) values. All \(2k\) signed coordinates have \((\tau',\beta')\)-coverage at every \(c\), with zero exceptions. Hence \(\eta'=0\) is valid. Conditional iid is literal: the scalar draws \(U_\ell\) are independent given \(C=c\).

**Joint entropy input.** For every fixed \(s=k\) signed selection \(S\), sign inversion acts bijectively and \(F_S(Y)\) is a product of \(k\) independent uniforms on sets of size \(L\). Thus
\[
\mathbb E_S H(F_S(Y))=k\log L
=(1-\epsilon)s\overline L,\qquad
\overline L=\log p,\qquad
\epsilon=\frac{\log(p/L)}{\log p}\to0.
\]

**Shared entropy cost.** The complete vector \(h_\ell\) determines \(U_\ell\), and the \(U_\ell\) are independent. Consequently
\[
H(\mathcal H)=n\log p=\kappa s\overline L,\qquad
\kappa=\frac nk\le\frac1{8192}.
\]
For sufficiently large \(p\), \(\epsilon\le1/8192\); therefore
\[
\epsilon+\kappa\le\frac1{4096}
=\frac{\eta\delta\beta'}{16},\qquad
\eta'=0\le\frac{\eta\delta}{100}.
\]

**Sample size and scale.** Since \(\delta^2/2=1/8192\),
\[
p\exp(-\delta^2np^{-\beta}/2)
\le p\exp[-\log(6400p)]
=\frac1{6400}=\frac{\delta}{100}.
\]
Also \(64=\delta^{-1}<p^{1/4}=p^{\beta'/2}\) and
\(\log(128e)=\log(2e/\delta)\le(\beta'/4)\log T=(1/8)\log p\) for sufficiently large primes \(p\). The remaining parameter ranges in the external theorem are visibly met. Its conclusion holds: every \(\phi_{j,\sigma}(Z)\) is, in fact, exactly uniform.

## Joint support, variation, and information divergence

Conditioned on \(U_1=u\), \(R\) is uniform on the translate \(V^k+u\mathbf1_k\) in \(\mathbb F_p^k\), a set of cardinality \(L^k\). There are at most \(p\) such translates. Therefore
\[
\frac{|\operatorname{supp}(R)|}{p^k}
\le p\left(1-\frac mp\right)^k
\le p\exp\left(-\frac{km}{p}\right)
\le p(6400p)^{-8192^2}\to0,
\]
where the last bound follows from \(k\ge8192n\), \(n\ge8192\sqrt p\log(6400p)\), and \(m\ge\sqrt p\).
By testing the support event,
\[
\operatorname{TV}(\mathcal L(R),U_k)
\ge1-\frac{|\operatorname{supp}(R)|}{p^k}\to1.
\]

Since \(R\mid U_1=u\) is uniform on \(L^k\) distinct vectors,
\[
k\log L=H(R\mid U_1)\le H(R)\le k\log p.
\]
As \(L/p\to1\), the entropy ratio \(H(R)/(k\log p)\to1\).
More quantitatively,
\[
k\log(p/L)-\log p
\le D_{\rm KL}(\mathcal L(R)\Vert U_k)
\le k\log(p/L).
\]
The lower bound uses \(H(R)\le\log|\operatorname{supp}(R)|\le\log p+k\log L\); the upper bound uses \(H(R)\ge k\log L\). Thus absolute divergence and relative entropy deficit have different scales.

## Finite exact sanity check

For \((p,m,k)=(7,2,4)\), independently enumerate \(V^k\) and the seven diagonal shifts with equal rational weights. The support contains 2233 out of 2401 joint residue vectors, with exact total variation \(45456/214375\); every coordinate marginal is uniform on seven residues. This finite test checks the stated mechanism. It is not represented as satisfying the transfer theorem's large-\(p\) numerical size inequalities, which are verified symbolically above.

## Contribution boundaries and follow-up

The earlier original-author binary-shift model repaired marginal coverage with one shared bit but lacked full exact-checkpoint next-stage conditional coverage when \(C=Y\). The present new construction replaces that bit with one uniform \(p\)-ary scalar per conditional-iid trial and pays \(n\log p\) in a valid shared entropy budget; hence it **does** satisfy the external abstract theorem's complete premises. Earlier results about binary-shift entropy, support, and signed projections remain valid in their original two-shift model.

The theorem above proves the absence of a *joint-uniformity consequence from these abstract assumptions alone*. It does not determine the actual Gaussian-prime walk continuation law, nor a native Heartbeat X6 carrier/Link/Port realization. Retain both questions as separate mathematical targets. All claims here are Driver-authored; author independence, native Result/Review admission, Source Activity association, Task completion, and mother-objective closure require their respective independent control records.

Sources: [original author shared-bit proof](https://github.com/awdawmip/enterprise-math/blob/3ae158973f1c11152badbfc19f2ec655bdc3bd6f/research_artifacts/mcp/RS-OAI7-028-C-20261007-6F2A81/MCP-c618a61189764f23846a391a08518a1a/6df1b102f9d377956aeb/OAI7_028_C_SHARED_SHIFT_COVERAGE_PROOF_20261117.md); [prior Driver conditional-entropy audit](https://github.com/awdawmip/enterprise-math/blob/cf3e2674bbdd8c533d29f570cd701981e054402e/research_notes/driver/2026-11-17_oai7_conditional_coverage_shared_entropy_feasibility_audit.md); [previous two-shift TV theorem](https://github.com/awdawmip/enterprise-math/blob/44b6473714650e817d03f6178e46dce9b4f37949/research_notes/driver/2026-11-17_oai7_uniform_small_projections_singular_full_law_tv.md).
