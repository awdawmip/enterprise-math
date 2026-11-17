# OAI7 — Distinct-prime, rank-one CRT coupling satisfies all abstract transfer assumptions with sparse joint output

Date: 2026-11-17. New proof author: EM-DVR-DEBB5E. Source-side mathematical extension of the earlier OAI7 shared-shift constructions by EM-EMF6D046-5A2844. Exact intended target: the **abstract** one-step coverage-transfer theorem in [openai/math fixed coverage-transfer.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex), with distinct coordinate-group prime orders. This does not assert the physical self-avoiding-walk displacement bounds or a native X6 realization.

## Theorem (distinct primes and rank-one lattice)

There is a sequence of abstract coverage-transfer experiments over the lattice \(\Lambda=\mathbb Z\), with **pairwise distinct** prime moduli \(p_j\in[T,2T]\), such that:

1. Every signed coordinate has exact conditional next-stage uniformity at every exact checkpoint and the conditional displacement trials are iid.
2. The theorem's high initial sampled joint entropy, common-data entropy budget, sample-size and logarithmic inequalities all hold.
3. All terminal signed-coordinate marginals are uniform, yet for the joint residue vector \(R\in\prod_{j=1}^k\mathbb F_{p_j}\),
\[
\frac{|\operatorname{supp}(R)|}{\prod_{j=1}^kp_j}\longrightarrow0,\qquad
\operatorname{TV}(\mathcal L(R),U_{\rm product})\longrightarrow1,\qquad
\frac{H(R)}{\sum_{j=1}^k\log p_j}\longrightarrow1.
\]

Thus the lack of a joint-uniformity conclusion is not an artifact of duplicate moduli, a high-rank lattice, or the earlier shared Bernoulli displacement.

## Prime selection, exact checkpoint, and shared conditional law

For sufficiently large \(T\), select
\[
 k=\left\lfloor \sqrt T(\log T)^2\right\rfloor
\]
different primes \(p_1,\ldots,p_k\) in \([T,2T]\). Existence follows from the standard prime number theorem, since the number of primes in that interval is asymptotic to \(T/\log T\), which dominates \(k\). Let
\[
m_j=\lceil\sqrt{p_j}\rceil,\quad L_j=p_j-m_j,\quad
V_j=\{m_j,\ldots,p_j-1\}\subset\mathbb F_{p_j},\quad
P=\prod_jp_j.
\]

Draw mutually independent residues \(C_j\), uniform on \(V_j\); let the **exact checkpoint** \(C=(C_1,\ldots,C_k)\). By the Chinese remainder theorem there is a unique \(y(C)\in\{0,\ldots,P-1\}\subset\mathbb Z\) with \(y(C)\equiv C_j\pmod{p_j}\) for each \(j\). Put \(Y=y(C)\). The signed homomorphisms are
\[
\phi_{j,\sigma}(x)=\sigma x\pmod {p_j},\qquad\sigma\in\{+,-\},
\]
and the two signs are counted as separate signed coordinate maps, exactly as in the external theorem.

Construct **one shared scalar integer displacement** by quantile coupling: let \(W\) be uniform on \([0,1)\) and set
\[
r_j(W)=\lfloor p_jW\rfloor\in\{0,\ldots,p_j-1\}.
\]
Each \(r_j\) is uniform on its group, while all \(r_j\) share the same \(W\). Let \(h(W)\in\{0,\ldots,P-1\}\) be their single CRT lift, so
\(h(W)\equiv r_j(W)\pmod {p_j}\).
The number \(N\) of values of \(h(W)\) is at most
\[
N\le 1+\sum_{j=1}^k(p_j-1)\le1+2kT.
\]
Reason: the joint quantile vector changes only at the union of the finitely many boundaries \(a/p_j\), for \(1\le a<p_j\). Therefore
\[
H(h(W))\le \log N\le\log(1+2kT)=O(\log T).
\]
Crucially, no product of the prime moduli appears in this entropy upper bound, even though the canonical CRT representative can be large.

At each exact checkpoint \(C=c\), let the conditional law \(\nu_c\) be the same law of \(h(W)\), independent of \(c\). Draw \(h_1,\ldots,h_n\) iid from this conditional law with fresh \(W_\ell\), set \(\mathcal H=(h_1,\ldots,h_n)\) and \(Z=Y+h_1\).
For every fixed \(c\), signed map \(j,\sigma\) and trial \(\ell\),
\[
\phi_{j,\sigma}(y(c)+h_\ell)
=\sigma(c_j+r_j(W_\ell))\pmod {p_j}
\]
is exactly uniform on \(p_j\) residues. Hence exact-start conditional \((\tau',\beta')\)-coverage holds for all signed maps and conditional iid is literal.

## The external theorem's numerical requirements

Fix
\[
\beta=\beta'=\frac12,\quad
\tau=\frac38,\quad\delta=\frac1{64},\quad
\tau'=\frac7{16},\quad
\eta=\frac12,\quad\eta'=0.
\]
Use \(s=k\) and choose
\[
n=\left\lceil8192\sqrt{2T}\log(12800T)\right\rceil.
\]
Every signed selection of \(s=k\) indices contains each index once, with arbitrary signs. By independent checkpoint residues and sign bijectivity,
\[
\mathbb E_S H(F_S(Y))=\sum_{j=1}^k\log L_j
=(1-\epsilon)k\overline L,\quad
\overline L=\frac1k\sum_j\log p_j,\quad
\epsilon=\frac{\sum_j\log(p_j/L_j)}{\sum_j\log p_j}
=O\left(\frac1{\sqrt T\log T}\right).
\]
Furthermore, the shared data entropy satisfies
\[
H(\mathcal H)=nH(h(W))\le n\log(1+2kT),
\quad
\kappa:=\frac{H(\mathcal H)}{k\overline L}
=O\left(\frac1{\log T}\right).
\]
The last bound uses \(n=O(\sqrt T\log T)\),
\(k\asymp\sqrt T(\log T)^2\), and \(\overline L\asymp\log T\).
Hence for large enough \(T\),
\[
\epsilon+\kappa\le\frac1{4096}
=\frac{\eta\delta\beta'}{16},\qquad
\eta'=0\le\frac{\eta\delta}{100}.
\]

For every coordinate size \(p_j\in[T,2T]\), the sample-size condition follows exactly:
\[
p_j\exp\left(-\frac{\delta^2np_j^{-\beta}}2\right)
\le 2T\exp\left(-\frac n{8192\sqrt{2T}}\right)
\le\frac1{6400}=\frac{\delta}{100}.
\]
And for sufficiently large \(T\),
\[
64=\delta^{-1}<p_j^{1/4}=p_j^{\beta'/2},\qquad
\log(128e)=\log(2e/\delta)\le\frac18\log T.
\]
Thus **each** hypothesis (including distinct signed maps, exact-checkpoint conditioning, single shared data, correct quantifiers, and all inequalities) is satisfied. The theorem's terminal coordinate-coverage conclusion is indeed true, since all terminal signed marginals are uniform.

## Sharp joint-versus-marginal distinction

Conditional on \(h_1=h\), the joint residue vector
\(R=(Z\bmod p_1,\ldots,Z\bmod p_k)\) is uniform on the product translate \(\prod_j(V_j+h\bmod p_j)\), whose cardinality is \(\prod_jL_j\). Since the shared displacement has at most \(N\le1+2kT\) possible values,
\[
\frac{|\operatorname{supp}(R)|}{P}
\le (1+2kT)\prod_{j=1}^k\left(1-\frac{m_j}{p_j}\right)
\le (1+2kT)\exp\left(-\sum_{j=1}^k\frac{m_j}{p_j}\right).
\]
Here \(m_j/p_j\ge p_j^{-1/2}\ge(2T)^{-1/2}\), so
\[
\frac{|\operatorname{supp}(R)|}{P}
\le(1+2kT)\exp[-k/\sqrt{2T}]
\longrightarrow0
\]
because \(k/\sqrt{2T}\sim(\log T)^2/\sqrt2\), whereas \(\log(1+2kT)=O(\log T)\). The event \(\operatorname{supp}(R)\) gives
\[
\operatorname{TV}(\mathcal L(R),U_{\rm product})
\ge1-\frac{|\operatorname{supp}(R)|}{P}\to1.
\]

On the other hand, \(H(R\mid h_1)=\sum_j\log L_j\), so
\[
\sum_j\log L_j\le H(R)\le\sum_j\log p_j.
\]
Therefore \(H(R)/\sum_j\log p_j\to1\). The finite joint support can be sparse even though nearly the whole maximum relative entropy is present and each signed marginal is fully uniform.

## Small exact check and provenance

For moduli \(p_1=5,p_2=7\), a common \(W\) has exactly \(1+(5-1)+(7-1)=11\) quantile cells. Their lengths are rational, so all masses can be enumerated exactly; each induced residue is uniform on its prime group. Choose independent \(C_1\in\{2,3,4\}\), \(C_2\in\{2,3,4,5,6\}\), then CRT-lift \(Y\); exact rational enumeration gives all 35 possible final joint residues supported and total-variation distance \(4/35\) from uniform. This check tests the coupling/CRT construction, not the theorem's eventual-support limit.

The result is a scope test of the external **abstract** transfer theorem, not a disproof of it. Its Gaussian-prime physical application uses a specified self-avoiding-walk continuation, bounded physical displacement and geometric entropy-enrichment lemmas. The CRT lift may take values as large as \(P-1\); this proof does not establish those separate physical-size constraints. Nor does it transfer to native Heartbeat X6 without its typed carrier, Link/Port and ordered-path provenance.

The distinct-prime quantile/CRT construction and all new conclusions here belong to EM-DVR-DEBB5E, based on the earlier OAI7 source-line work of EM-EMF6D046-5A2844. It is GitHub author-side proof, not an independent Native Result/review, Task completion, or mother-objective closure. No other lane's CLAIM or DA was used.

Related fixed-source records: [prior exact-checkpoint shared uniform shift](https://github.com/awdawmip/enterprise-math/blob/11244f642ec5a5fba8d211bdb0edff7863012be5/research_notes/driver/2026-11-17_oai7_exact_checkpoint_shared_uniform_shift_full_transfer_hypotheses_sparse_joint.md); [original researcher two-shift proof](https://github.com/awdawmip/enterprise-math/blob/3ae158973f1c11152badbfc19f2ec655bdc3bd6f/research_artifacts/mcp/RS-OAI7-028-C-20261007-6F2A81/MCP-c618a61189764f23846a391a08518a1a/6df1b102f9d377956aeb/OAI7_028_C_SHARED_SHIFT_COVERAGE_PROOF_20261117.md).
