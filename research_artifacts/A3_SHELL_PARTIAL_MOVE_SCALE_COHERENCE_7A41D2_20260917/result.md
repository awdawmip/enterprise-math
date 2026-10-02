# A3 Partial Shell-Move Scale Coherence — Exact Revision Result

Task: `RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION`  
Publication: `TP2-D2D715EB36415B0CA0C5`  
Researcher: `EM-A3SCR-7A41D2`  
Claim: `claim-A3SCR-autoA-20260917-064030-7a41d2`  
Status: `EXACT_STATE_LEVEL_CLASSIFICATION / FRAME_ONLY_H4_REPLACED / DRIVER_REVIEW_REQUIRED`

## 1. Frozen carrier and BRC gate

Keep the parent carrier
\[
\Lambda_3=\{x\in\mathbb Z^4:\sum_i x_i=0\},\quad r(x)=\max_i|x_i|,
\quad B_n=\{r\le n\},\quad S_n=B_n\setminus B_{n-1},
\]
and the faithful radius-preserving action
\[
R_g=\operatorname{sgn}(g)P_g,\qquad G=S_4.
\]
For a finite label alphabet use `X_n=A^{B_n}` and literal restriction
\(\rho_{n+1,n}:X_{n+1}\to X_n\). The pointer-target stabilizer remains
\[
H=\{e,(12)\}.
\]

BRC retention used in this revision:

- population: the two actual adjacent-scale state paths, not only frame labels;
- branch identity: the scale pair, depth, support masks, and aligner cosets;
- observed output: the exact radial carrier operator (or its relation over aligner choices);
- future operation: restriction, composition, and optional residual-\(H\) quotient;
- precision: exact finite permutations and shells. No floating or scalar compression is used.

The smallest adequate exact carrier is a shell-labeled radial operator; the old single double coset is only a projection of it.

## 2. Scale-indexed partial actions

For \(1\le d\le n\), define the prefix action on carrier points by
\[
D_{n,d}(g)x=
\begin{cases}
R_gx,&r(x)\ge n-d+1,\\
x,&r(x)\le n-d.
\end{cases}
\]
It acts on labeled states by push-forward.

Compare adjacent scales \(n+1\to n\). Write \(g_+=g_{n+1}\), \(g_-=g_n\), and
\[
q=n-d+1.
\]
Because every \(R_g\) preserves radius, the upper-then-restrict path on `B_n` is induced by
\[
U_{n,d}(g_+)x=
\begin{cases}
R_{g_+}x,&r(x)\ge q+1,\\
x,&r(x)\le q,
\end{cases}
\]
whereas restrict-then-lower is induced by
\[
L_{n,d}(g_-)x=
\begin{cases}
R_{g_-}x,&r(x)\ge q,\\
x,&r(x)\le q-1.
\end{cases}
\]
Thus the two paths have different support domains even when \(g_-=g_+\).

## 3. Exact radial operator defect

Define the carrier defect
\[
K_{n,d}(g_-,g_+)=L_{n,d}(g_-)\,U_{n,d}(g_+)^{-1}.
\]
Then for every state the lower path is exactly `K` after the upper path. Since the action preserves each shell, `K` is the shell-labeled operator
\[
\kappa_{n,d}(r)=
\begin{cases}
e,&1\le r<q,\\
g_-,&r=q,\\
g_-g_+^{-1},&q<r\le n.
\end{cases}
\]
This is the exact state-level classifier. It separates two defects that the parent H4 conflated:

1. **support-transition defect** on the newly exposed shell \(S_q\): \(g_-\);
2. **overlap frame-phase defect** on \(S_{q+1},\dots,S_n\): \(g_-g_+^{-1}\).

The parent double coset
\[
\Delta_n=Hg_-g_+^{-1}H
\]
is therefore only the overlap projection. It has no information about the transition shell.

### Raw operation descent

The two state paths are equal for every labeled state iff `K=id`.
Consequently:

- if \(d=1\), exact descent holds iff \(g_-=e\); \(g_+\) disappears under restriction;
- if \(d\ge2\), exact descent holds iff \(g_-=g_+=e\).

In particular, a fixed-depth family carrying the same nonidentity \(g\) at adjacent scales never descends exactly. This is an operation-level no-go, not a frame-phase statement.

## 4. Exact representative-free relation

At each scale the legal aligner is a left coset \(A_k=Hg_k\). The exact choice-safe defect is not one element of `H\G/H`; it is the finite relation
\[
\mathcal K_{n,d}(A_n,A_{n+1})
=
\{K_{n,d}(h_-g_-,h_+g_+):h_-,h_+\in H\}.
\]
This set is independent of chosen representatives and lives in the finite radial operator group obtained by assigning one `G` element to each nonzero shell. Equivalently, the exact input is the pair of aligner cosets together with the two scale-dependent support masks.

A representative-independent shellwise double-coset projection is
\[
\bar\kappa(r)=
\begin{cases}
C_0,&r<q,\\
Hg_-H,&r=q,\\
Hg_-g_+^{-1}H,&r>q.
\end{cases}
\]
It is useful as a compressed diagnostic, but it is still weaker than \(\mathcal K\): independent shell classes erase the requirement that one *global* residual \(h\in H\) act coherently on the whole restricted state.

This is the exact place for the previously verified fixed-`H` pair-groupoid/double-coset algebra: it is a projection of the radial relation, not a replacement for the radial relation.

## 5. Universal residual-H quotient criterion

Let `H` act globally on `X_n` by the same carrier rotation on all shells. For a rigidly labeled state (hence for universal operator descent), the two paths are equal in `X_n/H` iff
\[
K_{n,d}(g_-,g_+)=R_h|_{B_n}
\quad\text{for one single }h\in H.
\]
The checker exhaustively verifies the following closed form for all `G x G`, all `1<=d<=n<=4`:

- `n=1,d=1`: quotient descent iff \(g_-\in H\); \(g_+\) is removed by restriction;
- if \(q\ge2\) and `d=1`: iff \(g_-=e\);
- if \(q\ge2\) and `d>=2`: iff \(g_-=g_+=e\);
- if \(q=1\), `n>=2` (equivalently `d=n`): iff \(g_-\in H\) and \(g_+=e\).

Reason: for every `r>=1`, the induced action on `S_r` is faithful. If a nonzero inner shell is fixed by `K`, any global `H` witness is forced to be `e`. When `q=1`, `S_1` fixes the global witness to `g_-`, and the overlap shells then force `g_+=e`.

Hence even shellwise identity double-coset tests are not, by themselves, a complete global-quotient classifier; the common global-`H` witness must be retained.

## 6. Frozen Driver counterexample replay

Take `n=2`, `d=2`, `g_-=g_+=(23)`, and
\[
p=(1,-1,0,0)\in S_1.
\]
Then

- scale 3 depth-2 support is `S3 union S2`, so upper-then-restrict fixes `p`;
- scale 2 depth-2 support is `S2 union S1`, so restrict-then-lower sends
  \[
  p\mapsto(-1,0,1,0).
  \]

The `H` orbit of `p` is the singleton `{p}`, so the paths disagree even modulo `H`.

The exact radial profile is
\[
S_1:C_2,\qquad S_2:C_0,
\]
while the old frame-only defect reports only `C0`. The positive control `g_-=g_+=e` also has frame-only defect `C0` and does commute. Therefore no invariant depending only on the old adjacent frame double coset can classify the state-level square.

## 7. General support-mask naturality theorem

The failure is not specific to `S4`. Let a radial action at scale `n` be specified by an exact shell-label function
\[
\alpha_n:\{1,\dots,n\}\to G.
\]
Because `G` preserves shells, adjacent-scale restriction commutes exactly iff
\[
\alpha_{n+1}(r)=\alpha_n(r)\quad\text{for every }1\le r\le n.
\]
Thus a support defined by a fixed **absolute radial cutoff** is restriction-natural, while a support defined by fixed **depth from the moving boundary** shifts by one shell at every scale and is non-natural unless its newly exposed action is trivial.

This gives the requested structural repair: support masks are part of the morphism data.

## 8. Re-audit of H5/H6 observables

The parent three-radius frame algebra remains valid only at its stated compressed strength:

- `C2*C2={C0,C2}` remains an exact fixed-`H` relation-valued multiplication fact;
- the old sequence `Delta_n` is a `FRAME_PHASE_ONLY` observable and cannot certify state-level scale commutation;
- `DEFECT_BIRTH_RADIUS`, `STABILIZATION_RADIUS`, and any boundary-to-bulk signature must use the radial relation `K`/`mathcal K` (or an explicitly proven operation-safe projection), not only `Delta_n`.

For the alternating family `g_n=e` on odd radii and `(23)` on even radii, every old overlap defect is `C2`, but the depth-2 radial double-coset profiles for eligible transitions are
\[
(C_2,C_2),(C_0,C_2),(C_2,C_2),(C_0,C_2),\ldots
\]
where the first entry is the transition shell and the second the overlap. The support-aware observer therefore recovers parity that the old all-`C2` sequence erased.

The A2 orientation-leakage result is preserved. For orientation-sensitive slice data, the residual `H` quotient is not operation-safe; the raw radial relation and orientation/slice/layer tags must be retained.

## 9. Reproducible verification

Checker: `research_checks/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_7A41D2_20260917.py`.

Local exact run:

```text
A3_PARTIAL_MOVE_SCALE_COHERENCE_CHECK=PASS
RAW_PATH_CASES=5760
GLOBAL_H_QUOTIENT_CASES=5760
FROZEN_REGRESSION=PASS;N=2;D=2;G=(23);PATH_A=p;PATH_B=(-1,0,1,0)
FROZEN_RADIAL_PROFILE=S1:C2,S2:C0
FRAME_ONLY_NO_GO=PASS;C0_HAS_BOTH_COMMUTING_AND_NONCOMMUTING_STATE_SQUARES
ALTERNATING_D2_PROFILES=n2:(C2,C2),n3:(C0,C2),n4:(C2,C2),n5:(C0,C2),n6:(C2,C2)
ABSOLUTE_CUTOFF_NATURALITY=PASS
UNIVERSAL_GLOBAL_H_CRITERION=PASS_EXHAUSTIVE_N_LE_4
```

Checker SHA-256: `d9b9f6002aca78157a3548d7a2b78a44a05a0952e69ab4ff0abfdbdec8ab4a9c`.

The exhaustive finite validation is a regression/certificate for the exact formulas; the general support-mask theorem is proved directly from shell preservation and does not extrapolate numerically from `n<=4`.

## 10. Disposition

Hard target achieved at researcher strength:

`A3_PARTIAL_MOVE_SCALE_COMMUTATION_AND_RADIAL_DEFECT_EXACTLY_CLASSIFIED`.

The false parent H4 iff statement is replaced by an exact radial operator/relation theorem and a no-go for frame-only classification. No Foundation/Working-Truth promotion is asserted. Independent Driver review remains required.
