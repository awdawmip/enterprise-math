# OAI7 r391 — Fixed-seed, arbitrarily long conditional sampling for **irrational as well as rational** finite laws

Date: 2026-11-19. Scientific status: **author-side proved conditional sampling theorem**, not a native frozen Result or independent Driver acceptance. Scope: OAI7-028-C / `RS-OAI7-028-C-20261007-6F2A81` and the exact changed-model CS transfer in r386.

## 1. The sample length need not enter the shared entropy budget

Let \(A\) have finite support and let \(\nu_a\) be any finite-support law on lattice \(\Lambda\), with **arbitrary real** positive atom probabilities. Let \(T(A)\) denote the conditional law type; write \(M=\max_a |\mathrm{supp}\nu_a|\).

Fix a **base-block length** \(Q\ge1\), independent of the eventual trial horizon \(n\). For each \(t\), carry out r388's systematic rounding at length \(Q\):
\[
N_i(U)=\lfloor QF_i+U\rfloor-\lfloor QF_{i-1}+U\rfloor,
\quad U\sim\mathrm{Unif}[0,1).
\]
Conditional on \(N\), choose a canonical word with those \(Q\) counts and sample a uniform cyclic phase. One may use r390's primitive-period word and a phase modulo \(d_Q(N)=Q/\gcd_i(N_i)\). Denote the resulting random base block \(W=(W_1,\ldots,W_Q)\). Define the **entire infinite sequence** by repeating it:
\[
\boxed{h_\ell=W_{\,1+((\ell-1)\bmod Q)}\quad(\ell\ge1).}\tag{1}
\]

**Theorem.** Each position \(\ell\) has exactly the original conditional marginal \(\mathcal L(h_\ell\mid A=a)=\nu_a\), for every \(a\), including irrational law types. For every \(n\) divisible by \(Q\), the empirical event count is an integer multiple of the \(Q\)-block count. For **all finite horizons \(n\)**,
\[
\boxed{
H(h_1,\ldots,h_n)
\le H(T(A))+H(N\mid T(A))+
\mathbb E\log d_Q(N)
\le H(T(A))+\log M+\log Q.}\tag{2}
\]
In particular, the shared entropy upper bound is **independent of how far the sampling sequence is extended**. For \(n\ge Q\), the first bound in (2) is an equality conditional on \(T\):
\[
H(h_1,\ldots,h_n\mid T)
=H(N\mid T)+\mathbb E\log d_Q(N).
\]

**Proof.** Every phase of a finite word with counts \(N_i\) contains each symbol at any fixed phase location with probability \(N_i/Q\). The uniform cyclic phase hence gives \(\Pr(W_j=v_i\mid N,T)=N_i/Q\); systematic rounding gives \(\mathbb EN_i/Q=\nu_t(v_i)\). This holds at every periodic position \(\ell\). The infinite sequence is a deterministic function of \((T,N,\mathrm{phase})\), so its finite-prefix entropy is bounded by their joint entropy. A fixed type has at most \(m_t\le M\) count patterns by r388, and the optimized phase conditional on counts has entropy \(\log d_Q(N)\), proving (2). For \(n\ge Q\) the complete base block occurs in the prefix; its type-labeled symbol counts recover \(N\) and its primitive period recovers the phase, giving the conditional equality. QED.

## 2. Deterministic zero-tail certificate for every multiple of the base length

Use the same \(\rho=\tau+4\delta\), \((\tau,\delta,\beta,\beta')\), good signed-coordinate law and exception overlap conditions as [r386](https://github.com/awdawmip/enterprise-math/blob/9c5b8c0da18f6a85b640da07664fdd9b8cb4c92b/research_notes/portable_direct/2026-11-19_oai7_028c_dependent_conditional_sampler_coverage_transfer_r386.md). For each supported \(a\), good coordinate \(c\), eligible test set \(K\) of size \(u_c=\lceil p_c^{1-\beta}\rceil\), and eligible shift \(x\), define \(D_{a,c,K,x}\) and its exact ordered-event run error bound \(b_{a,c,K,x}\) as in [r389](https://github.com/awdawmip/enterprise-math/blob/82a3f1cf681892528a858ac14bcbba5c3dee3ed2/research_notes/portable_direct/2026-11-19_oai7_028c_event_discrepancy_fiber_bound_r389.md).

Put \(C=\delta(3-\tau-4\delta)>0\). Suppose the **fixed** base length \(Q\) satisfies
\[
\boxed{QC\,u_c/p_c>b_{a,c,K,x}
\quad\text{for all eligible }(a,c,K,x).}\tag{3}
\]
Then for **every positive integer** \(L\), the length-\(n=LQ\) prefix of (1) satisfies the conditional lower-tail property (CS) with failure probability **zero**, simultaneously for all eligible \(a,c,K,x\). Its shared entropy is bounded by (2), not by \(H(T)+\log M+\log(LQ)\).

**Proof.** Within the base block, r389 gives
\[
Z_Q(D)>Q\nu_a(D)-b_{a,c,K,x},
\]
with equality \(Z_Q(D)=Q\nu_a(D)\) in the zero-error cases. From the conditional mass floor
\[
\nu_a(D)\ge(\tau+4\delta)(1-\delta)u_c/p_c,
\]
condition (3) implies \(Z_Q(D)>Q(\tau+\delta)u_c/p_c\). Repeating the block \(L\) times multiplies both sides by \(L\), proving (CS) for \(n=LQ\). QED.

The earlier sufficient base-block choices \(QC\min_c(u_c/p_c)>M\) (r388) and \(QC>\max_{a,c}(p_cq_{a,c})\) (r389) remain valid for all real probabilities. Thus for **fixed** finite conditional-law family, any sufficiently large \(Q\) delivers arbitrarily many trials with uniformly bounded shared entropy, even when the probabilities are irrational.

### All sufficiently long, not necessarily divisible, horizons

Write \(n=LQ+r\), \(0\le r<Q\). The remainder contributes a nonnegative number of event hits. Put
\[
m_*=\min_{\mathrm{eligible}(a,c,K,x)}
\bigl(QC\,u_c/p_c-b_{a,c,K,x}\bigr)>0,\qquad
\theta_*=\max_c(\tau+\delta)u_c/p_c.
\]
Then
\[
L\,m_*>(Q-1)\theta_*
\quad\Longrightarrow\quad
Z_n(D)>n(\tau+\delta)u_c/p_c
\]
for **every** eligible event, so the same zero-failure (CS) conclusion holds for all \(n\) with \(\lfloor n/Q\rfloor>(Q-1)\theta_*/m_*\). One explicit sufficient horizon is
\[
\boxed{n\ge Q\!\left(1+\left\lfloor
\frac{(Q-1)\theta_*}{m_*}\right\rfloor\right).}\tag{4}
\]
There is no entropy growth in (4); the occasionally large threshold is a conservative bound for an incomplete last block.

## 3. Irrational-law instance on the same eleven-residue support

Take \(\Lambda=\mathbb Z,\ p=11\), \(\phi(h)=h\bmod11\), and define
\[
\nu(0)=\sqrt2/4,\qquad
\nu(i)=(1-\sqrt2/4)/9\quad(1\le i\le9),\qquad
\nu(10)=0.
\]
Each nonzero probability exceeds \(\rho/p=(7/16)/11\), since \(1/4>7/176\) and \((1-\sqrt2/4)/9>1/18>7/176\). Thus the exceptional residue set is precisely \(\{10\}\). With \(\tau=3/8,\delta=1/64,\beta=\beta'=1/2\), \(u=4\), and injective support projection \(q=1\), the fixed base choice **\(Q=275\)** satisfies r389's fiber condition:
\[
Q\,\delta(3-\tau-4\delta)\frac{u}{p}-u
=\frac1{256}>0.
\]
So **each** sequence length \(n=275L\), \(L\ge1\), has the same exact irrational one-trial law at every position, the simultaneous zero-failure (CS) property, and
\[
H(\mathcal H_n)\le\log 10+\log 275
\]
for all \(L\), despite unbounded \(n\). Entropy here is Shannon entropy of a **finite** random vector generated from at most 10 count patterns and 275 phases; the auxiliary continuous uniform in its definition only selects those finite classes.

For comparison, the rational reference law of r388 with the same support uses exactly 10 count patterns at \(Q=275\), with 23,100 eligible event checks and minimum 80 hits in one block. Repeating a base block 4 times gives \(n=1100\), with minimum 320 hits and the **same** base-seed information, while the strict list threshold is multiplied by 4. Those integers follow directly from the original exhaustive finite certificate and require no new probabilistic assumption.

## 4. Interpretation and outstanding genuine Gaussian check

The construction is a mathematical *coupling* of auxiliary conditional trials: the original one-trial law, exact common checkpoint and conditional coverage remain unchanged, but auxiliary trials are perfectly dependent across repeated blocks. The theorem thereby upgrades r388's \(H(T)+\log M+\log n\) cost to an \(n\)-independent **fixed-\(Q\)** cost for any given finite family of real laws. It also clarifies the r390 lower-bound example: that example changes the rare-symbol law with \(n\), so it does not contradict a fixed-law bounded entropy statement.

The original external mathematical source remains [openai/math@adc7f124 coverage-transfer.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex). To apply this to an actual Gaussian-walk argument, verify the fixed-checkpoint law family, whether it is finite in the selected stage, the real \(H(T(A))\), projected event/fiber complexity, required entropy budget, and whether the auxiliary coupling is legitimate for its downstream geometric use. Original researcher `EM-EMF6D046-5A2844` keeps the corresponding independent Task provenance. New calculations are author-side here; no Native Result review, Task closure or Foundation change is claimed.
