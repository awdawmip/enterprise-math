# A3 all-scale orbit naturality and intrinsic quotient-square classification

**Date:** 2026-11-13. **Status:** mathematical Driver audit / exact all-radius proof; no Native Review or frozen-Result replacement.

**Provenance.** Original task RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION, publication TP2-D2D715EB36415B0CA0C5, frozen Result RR-9FF7F84F01C577774649, researcher EM-A3SCR-7A41D2. The original author's shellwise radial-defect formula and finite classification are preserved. This note proves the quotient-path classification at *all* radii and distinguishes it from the more restrictive intrinsic quotient-square condition. The [single fixed binary probe theorem](2026-11-13_a3_single_binary_probe_centralizer_theorem.md) comes from the same Driver context; the present note is **not** an independent second reviewer.

## 1. Exact carrier and distinct questions

Work within the restricted A3 carrier

\[
B_n=\{x\in\mathbb Z^4:\ \sum_{i=1}^4x_i=0,\ \|x\|_\infty\le n\},
\qquad S_r=B_r\setminus B_{r-1}.
\]

The signed \(S_4\) action is \(\rho_g=\operatorname{sgn}(g)P_g\). Put \(h=(12)\), \(H=\{e,h\}\), and \(X_n=A^{B_n}\) for any alphabet with **\(|A|\ge2\)**. Carrier permutations act by pushforward \(T_*f=f\circ T^{-1}\). Let \(\pi_n:X_n\to X_n/H\) be the orbit projection. The depth-\(d\) radial action \(D_{n,d}(g)\) is \(\rho_g\) on shells \(r\ge n-d+1\) and identity below. Restriction \(J_n:X_{n+1}\to X_n\) is \(H\)-equivariant.

Fix \(n\ge d\ge1\), lower aligner \(g_-\), upper aligner \(g_+\), and \(q=n-d+1\). Two different assertions are relevant:

**(O) Output-orbit equality, after both complete paths:**

\[
\pi_n(J_nD_{n+1,d}(g_+)_*f)
=\pi_n(D_{n,d}(g_-)_*J_nf)
\quad\text{for every }f\in X_{n+1}.
\]

Here the upper and lower radial actions need not individually induce quotient-space operators; only the output comparison is made after restricting and projecting.

**(Q) Intrinsic quotient-state commuting square:** each of \(D_{n+1,d}(g_+)\) and \(D_{n,d}(g_-)\) must itself descend to the corresponding \(X_m/H\), and the resulting two quotient operators must commute with restriction on the quotients.

## 2. Orbit-rigidity lemma for a global involution

**Lemma.** Let \(Y\) be a finite carrier, \(h:Y\to Y\) an involution, and \(K\in\operatorname{Sym}(Y)\). For \(|A|\ge2\),

\[
(\forall f\in A^Y)\quad K_*f\in\{f,h_*f\}
\quad\Longleftrightarrow\quad
K\in\{\operatorname{id},h\}.
\]

**Proof.** Mark one site \(x\) by a second label, leaving all other sites at the first label. The orbit condition forces \(Kx\in\{x,hx\}\). On each two-element \(h\)-orbit, bijectivity forces \(K\) to act either as identity or as the exchange of the pair; \(h\)-fixed sites remain fixed. If two distinct two-element orbits had different choices, a state marking one site in each orbit would be sent to neither itself nor its image under the **single global** \(h\). Thus all exchanged-or-not decisions agree. For zero or one two-element orbit the same conclusion is immediate. Hence \(K=\operatorname{id}\) or \(K=h\) everywhere. The converse is immediate. QED.

This lemma is an exact certification of the **declared full labeling observer and global-\(H\) orbit**. It does not authorize dropping signed, phase, branch, or path information from a richer observer.

## 3. Faithfulness on every positive shell

For each \(r\ge1\), the sites \(r(e_i-e_4)\), \(i=1,2,3\), belong to \(S_r\) and span the three-dimensional sum-zero representation. The signed permutation action is faithful there: for an even \(g\), \(\rho_g=I\) forces \(g=e\); for an odd \(g\), \(\rho_g=I\) would require \(P_g=-I\) on that space, contradicting

\[
\operatorname{tr}(P_g|_{\sum x_i=0})
=\#\operatorname{Fix}(g)-1\ge-1>-3.
\]

Moreover, \(\rho_h\) is nonidentity on each \(S_r\), because \(\rho_h(r(e_3-e_4))=-r(e_3-e_4)\). Every \(\rho_g\) preserves the shell decomposition and fixes the zero site.

## 4. Universal output-orbit classification (O)

Let \(U\) denote the upper-then-restrict carrier permutation on \(B_n\) and \(L\) the restrict-then-lower one. The original A3 calculation gives \(K=LU^{-1}\), with the exact shell profile

\[
K|_{S_r}=
\begin{cases}
\rho_e,&r<q,\\
\rho_{g_-},&r=q,\\
\rho_{g_-g_+^{-1}},&q<r\le n.
\end{cases}
\]

Since \(J_n\) is surjective on all labelings of \(B_n\), (O) is equivalent to \((\forall u\in X_n)\ K_*u\in H_*u\). The lemma makes this equivalent to **one global** \(K=\rho_e\) or \(K=\rho_h\).

If \(q\ge2\), the fixed inner shell \(S_1\) rules out global \(\rho_h\). Hence \(K=\rho_e\); faithfulness of \(S_q\) gives \(g_-=e\), and any overlap shell \(S_{q+1}\) (present when \(d\ge2\)) then gives \(g_+=e\).

If \(q=1\), the first shell requires \(g_-\in H\). If \(n\ge2\), the second shell must implement that *same* \(H\) element, forcing \(g_+=e\). At \(n=d=1\), the upper aligner acts only on sites dropped by restriction, so it is unrestricted.

The **complete all-radius theorem** is therefore:

| Regime | Necessary and sufficient conditions for (O) |
|---|---|
| \(q\ge2,\ d=1\) | \(g_-=e;\ g_+\in S_4\) arbitrary |
| \(q\ge2,\ d\ge2\) | \(g_-=g_+=e\) |
| \(q=1,\ n\ge2\) | \(g_-\in H;\ g_+=e\) |
| \(n=d=1\) | \(g_-\in H;\ g_+\in S_4\) arbitrary |

This proves the frozen researcher's formerly finite-tested output-orbit criterion for every \(n\ge d\ge1\) in the declared A3 model, without using the insufficient frame-only double coset \(Hg_-g_+^{-1}H\).

## 5. Intrinsic quotient-square classification (Q)

The previous exact single-probe descent theorem establishes, for every nonempty active shell,

\[
D_{m,d}(g)\text{ descends to }X_m/H
\quad\Longleftrightarrow\quad
g\in C_{S_4}(h)
=\{e,(12),(34),(12)(34)\}.
\]

Thus (Q) holds precisely when (O) holds **and** both aligners lie in that centralizer. Explicitly:

| Regime | Necessary and sufficient conditions for (Q) |
|---|---|
| \(q\ge2,\ d=1\) | \(g_-=e;\ g_+\in C_{S_4}(h)\) |
| \(q\ge2,\ d\ge2\) | \(g_-=g_+=e\) |
| \(q=1,\ n\ge2\) | \(g_-\in H;\ g_+=e\) |
| \(n=d=1\) | \(g_-\in H;\ g_+\in C_{S_4}(h)\) |

**Sharp distinction.** At \(n=d=1\), choose \(g_-=e,\ g_+=(23)\). Condition (O) holds because the upper nonidentity shell is discarded. But \(g_+\) does not commute with \(h\), so it has no induced operator on the upper quotient \(X_2/H\); (Q) fails. Any claim about an intrinsic quotient diagram must state and check its map-existence condition.

## 6. Exact finite regression

An additional locally run integer permutation enumeration independently computed \(K\) on every site of every shell, for all \(24^2=576\) choices of \((g_-,g_+)\) in each regime \(1\le d\le n\le4\), then checked the full-carrier equality \(K=\rho_e\) or \(K=\rho_h\). It used signed coordinate permutations, no floating point arithmetic, and compared every outcome to the formula in §4. The counts of valid (O) pairs, each out of 576, were:

| \((n,d)\) | (1,1) | (2,1) | (2,2) | (3,1) | (3,2) | (3,3) | (4,1) | (4,2) | (4,3) | (4,4) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| (O) | 48 | 24 | 2 | 24 | 1 | 2 | 24 | 1 | 1 | 2 |
| (Q) | 8 | 4 | 2 | 4 | 1 | 2 | 4 | 1 | 1 | 2 |

All **5,760** pair/regime checks agreed. For (Q), the counts result from the additional exact centralizer test on both aligners. The finite check is a regression; the all-radius claim is proved in §§2–5.

## 7. Scientific and operational scope

The exact theorem uses the restricted A3 \(B_n\) shell carrier, the *global* residual involution, and full binary-capable state labelings. It is not an assertion that a four-coordinate shell is an independent native spatial world. The Enterprise Math native basis is HEARTBEAT_WORLD X6; any transfer requires an explicit X6 embedding/readout and the associated observer-and-future-operation certificate.

The original researcher, frozen Result bytes and exact radial-defect theorem remain intact. This note adds a rigorous universal proof of the original finite quotient criterion and a typed quotient-operator correction. It is eligible as additional mathematical material for the real Driver review, with shared-context provenance disclosed; it is **not** an immutable Native Review, Result acceptance, Task DONE, or mother Objective closure. Existing terminal failed flow requests remain terminal and are not replayed.
