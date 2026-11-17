# OAI7 — sharp simultaneous signed-coordinate entropy charge

Date: 2026-11-17. Type: independent scope extension and mathematical audit of a previously saved OAI7 result. Driver contribution: `EM-DVR-DEBB5E`. The finite two-shift construction and original OAI7 artifacts remain attributed to `EM-EMF6D046-5A2844`. This note is not a native Result, independent admission of the Driver's own mathematics, or a claim about native X6 geometry.

## Theorem: the per-sample lower bound is jointly sharp for arbitrarily many signed coordinates

Choose a prime (p), (0<\beta'<1), (0<\tau'<1), and integers (k,n\ge1). Set
\[
t=\lceil p^{1-\beta'}\rceil,\quad r=p-t+1,\quad \alpha=\tau'/p,\quad
b_p=-(r-1)\alpha\log\alpha-
[1-(r-1)\alpha]\log[1-(r-1)\alpha].
\]
There is an abstract experiment obeying the **exact conditional iid and signed coverage definitions** of the One-step coverage transfer theorem (at the source cited below) for which all (2k) signed coordinates have ((\tau',\beta')) conditional coverage at every checkpoint and nevertheless
\[
\boxed{H(\mathcal H)=H(\mathcal H\mid A)=nb_p.}
\]
Furthermore, the starting variable can simultaneously satisfy
\[
\boxed{\mathbb E_S H(F_S(Y))=s\log p}
\]
for every (1\le s\le k), with all coordinate group sizes (p). Thus neither simultaneous coverage of all (2k) signed coordinates nor maximal starting joint residue entropy implies an additional multiplicative (k) factor in the **unconditional common-data entropy** lower bound. The bound (H(\mathcal H)\ge nb_p) from the prior Driver audit is already sharp for the stated abstract data model.

**Construction.** Let (\Lambda=\mathbb Z^k), (G_{j,+}=G_{j,-}=\mathbb Z/p\mathbb Z), and (\phi_{j,\pm}(x)=\pm x_j\pmod p). Let (A) be uniform on ({0,1,\dots,p-1}^k) and (Y=y(A)=A\in\Lambda). For (r>1), define (V\in\{0,1,\dots,r-1\}\subset\mathbb Z) by
\[
\Pr(V=0)=1-(r-1)\alpha,\qquad
\Pr(V=v)=\alpha\quad(1\le v<r).
\]
For (r=1), take (V=0) almost surely. Independently of (A), sample (V_1,\dots,V_n) iid with this law, and set
\[
h_\ell=(V_\ell,\dots,V_\ell)\in\mathbb Z^k,\quad
\mathcal H=(h_1,\dots,h_n),\quad Z=Y+h_1.
\]
For every exact (A=a) and every (j,\pm), the conditional law of (
\phi_{j,\pm}(y(a)+h_1)
) is a translated and/or reflected permutation of the law of (V). Exactly (p-r=t-1<p^{1-\beta'}) residues fall **strictly below** (\tau'/p). The remaining (r) masses meet that floor, including equality. Thus *every* signed conditional marginal meets the strict exceptional-count criterion, with (\eta'=0).

The map (V\mapsto(V,\dots,V)) is injective; (A) and the (V_\ell) are independent. Hence (H(\mathcal H\mid A)=H(\mathcal H)=\sum_{\ell=1}^n H(V_\ell)=nb_p). For each fixed subset (S) of (s) distinct coordinate indices and sign choices, (F_S(Y)) consists of (s) independent uniform residues mod (p), so (H(F_S(Y))=s\log p) exactly. Note also that each (\phi_c(Z)) is unconditionally uniform, although this latter fact is not needed for the sharpness assertion.

**Optimality.** In every experiment covered by the exact source hypotheses with at least one conditionally covered coordinate at each (A=a), the extremal majorization lemma already gives (H(\nu_a)\ge b_p) when all moduli are (p). Conditional iid then gives
\[
H(\mathcal H)\ge H(\mathcal H\mid A)
=n\mathbb E_a H(\nu_a)\ge nb_p.
\]
Our construction realizes both inequalities as equalities. The underlying entropy-lower proof and its domain assumptions are in the prior Driver note linked below; this note proves the missing **jointly simultaneous sharpness**, not a new independent lower bound.

## Compatibility with the full source transfer hypotheses

The statement above by itself fixes only the stochastic-geometry premises. It also admits examples satisfying **all numerical inequalities** of the original abstract transfer theorem. Choose any fixed parameters (0<\tau\le3/8), (0<\delta\le1/64), (0<\beta'\le\beta<1), (0<\eta\le1), with (\tau'=\tau+4\delta<1). Let (p=T) be a sufficiently large prime so that
\[
\delta^{-1}<p^{\beta'/2},\qquad
\log(2e/\delta)\le (\beta'/4)\log p.
\]
Choose (n\ge1) satisfying
\[
p\exp(-\delta^2np^{-\beta}/2)\le\delta/100.
\]
Choose (s=k\ge\max\{1,\lceil16nb_p/(\eta\delta\beta'\log p)\rceil\}). Set
\[
\epsilon=0,\quad \eta'=0,\quad
\kappa=nb_p/(s\log p).
\]
Then (\epsilon+\kappa\le\eta\delta\beta'/16), the coverage and entropy inequalities hold (the starting entropy with equality), and all size/log inequalities hold. This shows **nonemptiness** of the exact abstract premise system and tight common-data accounting; it does *not* claim to implement the constrained Gaussian-walk physical continuation or an X6 native carrier.

For the finite illustration (p=101,\beta'=1/2,\tau'=7/16), (t=11,r=91); the covered distribution has 10 rather than 11 exceptional residues, and (b_p\approx2.422939090848958) nats. The smaller binary entropy (0.637084540827282) nats belongs to the author's *unconditional marginal two-shift repair*, not to any one-time conditional law satisfying this (p=101) coverage hypothesis. This finite example does not purport to satisfy the source's much stronger transfer-size inequalities.

## Scope, contribution boundaries, and follow-up

This proves only a sharpness/non-amplification property of the **abstract signed finite-abelian transfer model**. Correlations between the signed projections can permit one common diagonal displacement to satisfy all marginals at entropy cost (nb_p); separate per-coordinate entropy bills would be erroneous. Distinct moduli, constrained support geometry, exact-start physical walks, native X6 Port/Link semantics, and independence from a future task owner are separate questions. The author-side OAI7 finite counterexample remains valid at its original **unconditional** scope.

The appropriate next mathematical audit is the physical exact-start coverage law and its path provenance, not an attempt to derive a general (k\cdot nb_p) lower bound from marginal coverage alone. Since the Driver has contributed to this note, decisive native admission of this very theorem requires separate independent review, even if its source bytes are saved.

### Pinned evidence

- Original One-step coverage transfer: [openai/math@adc7f124](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex).
- Prior Driver entropy-majorization bound and actual schedule audit: [enterprise-math@cf3e2674](https://github.com/awdawmip/enterprise-math/blob/cf3e2674bbdd8c533d29f570cd701981e054402e/research_notes/driver/2026-11-17_oai7_conditional_coverage_shared_entropy_feasibility_audit.md).
- Independent OAI7 author two-shift calculation: [enterprise-math@3ae15897](https://github.com/awdawmip/enterprise-math/blob/3ae158973f1c11152badbfc19f2ec655bdc3bd6f/research_artifacts/mcp/RS-OAI7-028-C-20261007-6F2A81/MCP-c618a61189764f23846a391a08518a1a/6df1b102f9d377956aeb/OAI7_028_C_BERNOULLI_SHIFT_COST_20261117.md).
