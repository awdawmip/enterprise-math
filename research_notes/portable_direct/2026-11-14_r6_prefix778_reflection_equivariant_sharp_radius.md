# PREFIX-778 / R6 — Sharp noise radius under reflection-equivariant Gamma readout

Date: 2026-11-14 (Asia/Shanghai). Researcher: EM-DIRECT-E77192; existing SID: MCP-d9aca4ec6e00440eba66035326ea5a4e. Status: AUTHOR_EXACT_INTEGER_ALGEBRAIC_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.

**Scientific input** remains frozen at `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Direct input: PREFIX-776 reflection identity, PREFIX-777 exact mixed increments and four-cell margin. This note studies only the external 189-layer killed-Pascal first-stop model with two independent unit-rate Gamma clocks. It asserts no native X6 event or signed-port equivalence.

## Precise problem

Let `Y(p,z)=max(C_p,C_z)`, `mu=E[Y]`, `W=Var(Y)`, `V_q=q²W-q mu`, and `G={k/768:0<=k<=768}`. Put `R38=[38,39]^2/768`, `R39=[39,40]^2/768`. Their reflected cells are `R38#=[38,39]x[729,730]/768` and `R39#=[39,40]x[728,729]/768`. The rectangular mixed difference is `Delta_R F=F(b,d)-F(b,c)-F(a,d)+F(a,c)`.

Set `A_k=-Delta_Rk(mu)>0`, `B_k=-Delta_Rk(W)>0`, `r_k=A_k/B_k` for k=38,39. The inherited exact calculation gives `r38<r39`; this run additionally verifies `B38<B39`. Thus `Delta_Rk V_q=q x_k(q)`, `x_k(q)=A_k-q B_k`. Exact reflection yields the opposite difference in each reflected cell.

**Observer hypothesis:** for every relevant vertex (the seven vertices of the two adjacent base squares and their seven reflected vertices), another scalar readout `Vhat_q` obeys both (i) `Vhat_q(p,1-z)=Vhat_q(p,z)` and (ii) `|Vhat_q(p,z)-V_q(p,z)|<=q epsilon`. The fourteen vertices may carry independent errors subject to the stated reflection pairing. No native transfer is presumed.

## Theorem: exact largest guaranteed perturbation radius

Define

`D=A39 B38-A38 B39>0`,

`epsilon_star=D/[2(B38+2 B39)]`, and

`q_star=(A38+2 A39)/(B38+2 B39)`.

**For every real q>0 and every 0<=epsilon<epsilon_star, the four cells contain at least one strictly positive and one strictly negative mixed difference of Vhat_q.** This bound is *sharp for this four-cell family and this observer class*: at `epsilon=epsilon_star`, `q=q_star`, a reflection-equivariant perturbation exists which makes all four mixed differences zero.

The exact integer certificate gives

`9020758537/10^17 < epsilon_star < 9020758538/10^17`,

so `epsilon_star ~= 9.0207585373397955823864330163e-8`, `q_star ~= 0.02852242876345894395483482896`.

Compared to PREFIX-777's *sharp unrestricted-corner* sufficient radius `C_four/4`, this structural hypothesis improves the uniform guarantee by the exact factor

`epsilon_star/(C_four/4)=2(B38+B39)/(B38+2B39) ~= 1.33166105973473906`.

In particular, the fully rational sufficient bound `epsilon<=9020758537/10^17` is valid, using the strict lower certificate.

## Proof: seven-corner overlap

The two base squares share exactly the point `(39/768,39/768)`, with coefficient +1 in *both* mixed differences. Under a vertex perturbation of magnitude at most `q epsilon`, divide errors and mixed differences by `q`. Each base cell has three private vertices capable jointly of any signed adjustment in `[-3 epsilon,3 epsilon]`; the common vertex supplies an identical adjustment `t in [-epsilon,epsilon]` to both mixed differences. Therefore simultaneous cancellation of `x38` and `x39` is feasible exactly when the three closed real intervals

`[-epsilon,epsilon]`, `[-x38-3epsilon,-x38+3epsilon]`, `[-x39-3epsilon,-x39+3epsilon]`

have a common point. Since three real intervals intersect jointly iff every pair intersects, this is equivalent to

`epsilon >= M(q) := max(|x38|/4, |x39|/4, |x39-x38|/6)`.

For `q in [r38,r39]`, put `s=B38(q-r38)>=0` and `t=B39(r39-q)>=0`. Then

`M(q)=max(s/4,t/4,(s+t)/6)`.

Here `s/4` increases, and, because `B39>B38`, both `t/4` and `(s+t)/6` decrease. Their minimax crossing occurs at `s=2t`, or `q=q_star`, where `M(q_star)=epsilon_star`. On `q<r38`, `|x39|/4` is strictly greater than its value at `r38`; on `q>r39`, `|x38|/4` is strictly greater than at `r39`. Thus `inf_{q>0} M(q)=epsilon_star`.

If `epsilon<epsilon_star`, simultaneous cancellation is impossible. At least one base difference is nonzero and its reflected difference has the opposite sign, proving the claim.

**Sharpness construction:** at `q_star`, put `c=x39(q_star)>0`, so `x38(q_star)=-2c` and `epsilon_star=c/2`. At the common base vertex assign perturbation `+q epsilon_star`. Assign the three private R38 corner errors to contribute `+3q epsilon_star` to its mixed difference, and the three private R39 corner errors to contribute `-3q epsilon_star`; these choices respect the vertex error bound. The resulting base increments are `-2qc+4q epsilon_star=0` and `qc-2q epsilon_star=0`. Reflect all errors with `z -> 1-z`, canceling the two mirror increments too. The certificate is therefore sharp.

## Exact computation and verification

Reuses the frozen `W=2^18` width predicate and integer killed-Pascal recursion. Reconstructs 189 rows with 9,529 nonzero pre-terminal survivor coefficients, validates symmetry/terminal emptiness and four reflected mixed differences. If `H=768^(376) 2^377`, write `a_k=-H Delta_Rk mu`, `b_k=-H^2 Delta_Rk W`; then `J=a39 b38-a38 b39>0`, and

`epsilon_star=J/[2H(b38+2b39)]`, `q_star=H(a38+2a39)/(b38+2b39)`.

The checker uses arbitrary-precision integer cross products for `b39>b38`, ratio ordering, the strict decimal interval, the exact minimax equalities and the improved radius inequality. Local independent run of the equivalent full-kernel checker returned `ALL_CHECKS_PASS PREFIX778 EQUIVARIANT_SHARP_RADIUS`. Full local result SHA-256: `58e5616a673dce793e8c4d33fd0a157df0f19f625d1c6749c622673fceb23e5f`.

Run the committed checker with `python3 research_notes/portable_direct/PREFIX778_R6_REFLECTION_EQUIVARIANT_RADIUS_CHECK.py`. It regenerates the full rational result file in the same directory.

## Next discriminating problem

Obtain a *typed* native observation/reflection map on the original X6/BRC comparator retaining Cell/Link/Port, branch/source and event-time information; determine whether an exact reflection invariance or a verified error/defect budget holds at the fourteen corners. Alternatively treat an approximate reflection defect explicitly and derive the corresponding sharp robustness threshold. No historical original-comparator grid exclusion has been added.
