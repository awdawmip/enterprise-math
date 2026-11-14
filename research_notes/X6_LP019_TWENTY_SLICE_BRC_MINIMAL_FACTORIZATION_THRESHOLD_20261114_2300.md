# X6 / LP019 — sharp signed-native N-BRC nonfactorization thresholds through all twenty three-axis observations

Parent: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`, original Research lane `chatgpt-research-onhour-enterprise-math-20260923`; Researcher `EM-X6-FB6990`, original SID `MCP-082892eb480e45dea6d4b9fcc0491034`, original CLAIM `MCP-30a8f5fd123215e08bd4a7cf`, original RUN `RUN-3356cbe3c2b4916d79399941`. These are provenance identifiers, **not** an independent current-write authorization.

Scientific authority: P000 V5 native signed-X6 `Z^6` Cell torsor and primitive directions `±e_i`, original immutable pin `59538f585d037d09ef687b28715c4bc1a3f9fe03:p000_reality_foundation.json`. Exact current theorem consumer V10 at `f5246fd204222d6c6903536f9336d02d367de173:research_notes/X6_20_SLICE_INVERSE_LIMIT_RECONSTRUCTION_V10_20260905.md`, blob `d956ad7eb2f181557242dca30d483c4b60952596`, establishes all-twenty-slice reconstruction **only at the derived relative-observer layer**. Current V8 S6 type correction at `3f940058620a20e4f656481af2826cec994cf25f` distinguishes observer norm from native squared norm.

Classification: **NEW EXACT ALL-INTEGER SHARP OBSTRUCTION + EXECUTED FINITE CERTIFICATE / AUTHOR-PROVED / UNREVIEWED / NOT_ADMITTED**. This is neither a claim of the historical LP019 offending signed-cancellation caller nor the R063 original native benchmark; the latter remains unexecuted under support issue #2416. Prior PR #1257 observer `q: N^6→Z²×Z/2` has a *different, coarser* fibre and prior thresholds 3/6; no reuse of that result as proof of the present stronger twenty-slice theorem.

## Typed definitions

For `z=(z_0,...,z_5)∈Z^6`, let `D=(1,1,1,1,1,1)` and for each of the 20 three-axis subsets `S⊂{0,...,5}`, `|S|=3`, let `can_3(z|S)` subtract the minimum of the three coordinates. Define the full observable family

`F(z)=(can_3(z|S))_{|S|=3}`.

Retain the actual signed-native shortest primitive-path length `L(z)=Σ_i |z_i|`, its squared component norm `G(z)=Σ_i z_i²`, and the **nonnegative integer** shortest primitive-axis ordered-path multiplicity

`B(z)=L(z)!/∏_i |z_i|!`.

In each native shortest path the sign of axis `i` is forced by `sign(z_i)`, and the order of the labeled axis steps varies; therefore `B` is a positive multinomial coefficient. No amplitude, signed character or carrier cancellation is part of `B`.

V10's exact pair-overlap theorem gives `F(z)=F(w) ⇔ w=z+kD` for some integer `k`. In particular `F` equals the full relative-minimum observer `ρ(z)=z-min_i(z_i)D` as an *information partition*, but does not identify raw native Cells.

## Theorem A — adding native shortest length does not suffice; sharp first failure L=4

For all signed `z,w∈Z^6` with `F(z)=F(w)` and `L(z)=L(w)≤3`, one has `B(z)=B(w)`.

Proof: exchange `z,w` and take `w=z+kD`, `k>0`. Coordinatewise `|z_i|+|z_i+k|≥k`, hence `2L≥6k`, so `L≥3k`. For `L≤3`, only `L=3,k=1` is possible. Every coordinate then realizes equality in the triangle inequality and is an integer in `{-1,0}`. Equality of the two lengths implies precisely three -1 and three 0 coordinates; after the shift there are three 0 and three +1 coordinates. Both multiplicities are `3!=6`. For `L<3`, there are no distinct equivalent native endpoints with equal `L`.

The first failure is the exact pair

`a=(-2,-1,-1,0,0,0)`, `b=(-1,0,0,1,1,1)=a+D`.

They share `F` and `L=4`, yet `B(a)=4!/2!=12`, `B(b)=4!=24`. Their distinct native norm squares are `G(a)=6` and `G(b)=4`, so retaining `G` separates this particular pair.

## Theorem B — even F, L, and native G together do not suffice; sharp first failure L=7

For all signed `z,w∈Z^6` with `F(z)=F(w)`, `L(z)=L(w)≤6` and `G(z)=G(w)`, one has `B(z)=B(w)`.

Proof: again write `w=z+kD`, `k>0`; `L≥3k`. For `k=1`, equal `L` means exactly three coordinates of `z` are negative and three nonnegative, since each `|z_i+1|-|z_i|` equals -1 or +1. Write the three negatives as `-1-u_1,-1-u_2,-1-u_3` and the other three as `v_1,v_2,v_3`, with all `u_j,v_j≥0`. Equal squares is equivalent to `Σ_i z_i=-3`, hence `Σu_j=Σv_j=t`, and `L=3+2t`. When `L≤6`, `t=0` or 1. The two multisets `(u_1,u_2,u_3)` and `(v_1,v_2,v_3)` are then permutations of `(0,0,0)` or `(1,0,0)`. The shifted multinomial denominators coincide, so `B(z)=B(w)`.

For `k=2`, `L≥6`, so within the range only `L=6` occurs. Equality in all six coordinate triangle inequalities gives `z_i∈{-2,-1,0}`. Equal squared norms gives `Σ z_i=-6`; writing the counts of -2, -1 and 0 as `a,b,c`, the identities `a+b+c=6`, `2a+b=6` give `a=c`. Therefore the absolute-coordinate multiset of `z` and `z+2D` is identical, so their multinomial B values coincide. For `k≥3`, `L≥9`, outside the claimed range.

The sharp `L=7` counterexample is

`c=(-3,-1,-1,1,1,0)`, `d=(-2,0,0,2,2,1)=c+D`.

Both have **identical** twenty-slice `F`, shortest length `L=7`, and native squared norm `G=13`, yet

`B(c)=7!/3!=840`, while `B(d)=7!/(2!2!2!)=630`.

Thus even `(F,L,G)` fails to determine native N-BRC multiplicity.

## Infinite exact family

For every integer `t≥2`, set

`c_t=(-t-1,-1,-1,t-1,1,0)`, `d_t=(-t,0,0,t,2,1)=c_t+D`.

Both have identical `F`, `L=2t+3` and `G=2t²+5`, but

`B(c_t)=(2t+3)!/((t+1)!(t-1)!)`,
`B(d_t)=(2t+3)!/[2(t!)²]`, hence
`B(c_t)/B(d_t)=2t/(t+1)≠1`.

This family gives arbitrarily large exact integer counterexamples without altering the frozen ontology or invoking a new non-native axiom.

## Exact finite execution and bounded interpretation

A new stdlib-only checker was **actually executed** from the exact original file bytes, with `python /mnt/data/x6_lP019_2300_checker.py`, exit 0, output `PASS_X6_LP019_TWENTY_SLICE_NBRC_NONFACTOR`. Its locally executed SHA256 is `35b3160e8fc2d2a6ac1a7f26b1ed575edd9bdd9f84c5e35f17e0f03a2c6983eb`; the connected GitHub-committed file is *byte-identical* Git blob `22851b7c3bcbc06d087da7f0c3a5113ed0f07daa` at `96802fccb5d0bdd6105a4af43167d5c7f57c9756:research_checks/X6_LP019_TWENTY_SLICE_NBRC_MINIMAL_SIGNED_OBSERVER_20261114_2300.py`, verified by same-body readback.

The checker exhausts every signed ordered `z∈Z^6` with `L(z)=n` for `0≤n≤7`. The exact shell sizes are `[1,12,72,292,912,2364,5336,10836]`. Numbers of relative `F+L` fibres with nonconstant positive B are `[0,0,0,0,120,240,1100,2460]`; for `F+L+G`, `[0,0,0,0,0,0,0,360]`. The all-twenty `F` equivalence is proven from V10; the finite checker computes its equivalent `ρ` partition for exhaustive speed and also directly checks all 20 chart readouts on each displayed witness. Exact integers/factorials are used, no floating-point rounding.

## Source typing / actual parent residue

This gives a new *sharp* observer-sufficiency failure for current V10/V8 downstream consumers, and reinforces the typed distinction `PATH_FORMAL → N_BRC → OPTIONAL OBSERVER`. Neither historical LP019 *positive mass subtraction* caller nor LP011 *native dominant-axis argmax* wrong caller has yet been located; a loss of multiplicity under an observer is **not** evidence that an unlocated executable subtracts paths. No Source formal Result/Driver review is implied.

Original R063 C3/C4 same-object benchmark with full 512 regression cases remains unexecuted in this research turn; execution support issue [#2416](https://github.com/awdawmip/enterprise-math/issues/2416) stays OPEN with no verified assigned runner. The 17:00 safety-denied prose write remains prohibited from retry/repackaging/identity or channel transfer. Preserve the existing 28-LP dependency ledger, source pin, original Research SID/CLAIM/RUN and pending semantic publish requests; continue the smallest actual unexamined native consumer / original executable or arrange the originally specified benchmark through an authorized runner. This note is independently authored, not admitted and not a frozen Result.
