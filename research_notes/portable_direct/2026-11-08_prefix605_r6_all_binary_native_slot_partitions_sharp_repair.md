# PREFIX-605-R6 — All native BRC binary slot partitions sharply repair singular phase observation

Date: 2026-11-08 Asia/Shanghai. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Original native BRC source blob: `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41` (PREFIX565). Depends on PREFIX-600 through PREFIX-604. Status: **AUTHOR_PROVED / EXACT_SYMBOLIC_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Model and question

The exact frozen BRC phase graph has 48 phases, 96 branch ports, three action slots 0,1,2, and nine allowed reward roots. We retain the previously declared twelve-incidence weighted family: at source phase p of incidence e, slot 0 has probability `1/(1+2t_e)`, and each of slots 1 and 2 has probability `t_e/(1+2t_e)`, with finite `t_e >= 0`. At t_e=1 the original frozen phase dynamics is recovered. This is an observer theorem inside that declared weighted extension.

Let P be the 48x48 **untagged** next-phase probability matrix, and C_j the **joint** probability matrix `C_j(p,q)=Pr(slot=j, final_phase=q | start_phase=p)`, j=0,1,2; hence `P=C_0+C_1+C_2`. A Boolean bit indicating whether the slot equals a fixed j, jointly with the endpoint phase, reveals precisely the two histograms `πP` and `πC_j` for any initial phase law π. The three choices of j enumerate all nonconstant binary partitions of the original three native slots.

PREFIX-601/602 proved `rank P=48-2k`, where k is the number of original six paired incidences `{e,f}` with `4t_e t_f=1`, and gave an exact 2k-dimensional left nullspace basis. Every critical pair has positive factors.

## Theorem — three sufficient Boolean labels, sharp nonnegative scalar repairs

**For every 12-tuple of finite nonnegative weights t, arbitrary initial probability distribution π on the 48 native phases, and each j=0,1,2, the map `π -> (πP,πC_j)` is injective. Furthermore, after πP is known, exactly 2k *individual nonnegative joint histogram probabilities* of the form `Pr(slot=j, final_phase=q)` suffice for recovery of π, and 2k is the sharp worst-case number of additional real linear scalar readings.** The result is independent of the nine allowed roots, which affect rewards but not this phase graph.

### Proof in the original native graph

Use the signed two-block phase order and incidence matrices W,U,V of PREFIX-600. Each critical pair e,f has `x=t_e>0`, `t_f=1/(4x)`. Write `s_i=1+2t_{e(i)}`. PREFIX-602's exact left-null generator in each signed 24-phase block is `ell_i=s_i*w_i`, where

`w=-x(V W^{-1})_e+(1/2)(V W^{-1})_f`.

The original native graph gives exactly four nonzero coefficients of w: two `+1/2` and two `-x`; their source incidences lie in the critical pair. In `ell*C_j`, the row normalizer s cancels, so the symbolic terms are exact Laurent polynomials in x.

The attached executable certificate exhaustively evaluates all **six actual critical pairs, both signed blocks, and all three singleton slot tags** over `Q[x,x^{-1}]`, yielding 36 exact symbolic identities:

* For j=0, each `ell*C_0` has four supported endpoint phases, with coefficients `1/2,1/2,-x,-x`.
* For j=1 or 2, each `ell*C_j` has two supported endpoints with coefficients `-1/2,x`.
* For a **fixed j**, the supports for the full twelve potential left-null generators are pairwise disjoint; their total supports have sizes 48 for j=0 and 24 for either j=1 or j=2.

All assertions are exact symbolic identities for arbitrary x>0. For each of the active 2k null generators, select one endpoint q with coefficient `+1/2` when j=0, or `-1/2` when j=1,2. Disjoint supports make the matrix of evaluations of these selected tagged-endpoint columns on the 2k null generators diagonal and invertible. Thus adjoining those **2k ordinary nonnegative endpoint-slot probabilities** raises the row rank of P from `48-2k` to 48.

For minimality, any fewer than 2k additional linear scalar functionals leave a nonzero vector in the intersection with the 2k-dimensional left nullspace of P. Every such vector has sum zero because P is stochastic. Small positive and negative perturbations of a strictly positive input distribution along it produce two valid, different phase laws with identical old and extra observations. QED.

## Actual validation, scope and incremental value

The standard-library `PREFIX605_R6_binary_tag_certificate.py` imports the frozen native source and preceding structural certificate modules, verifies its original Git blob SHA1 and the frozen science pin, performs **36** exact Laurent-polynomial checks, derives a complete table of selected endpoint probabilities, and independently tests exact rational ranks for `k=0,1,2,6`. The latter tests give untagged ranks 48,46,44,36 and repaired rank **48 for all three tags**, respectively. Run `python PREFIX605_R6_binary_tag_certificate.py`; actual result was `ALL_CHECKS_PASS`. The program emits `PREFIX605_R6_RESULTS.json` with all symbolic endpoint coordinates and the rank evidence.

PREFIX-603 exhibited the sufficient tag `slot=0` and 2k signed linear repair measurements. Here **all three** singleton Boolean partitions are classified and each has an optimal repair using **directly observable nonnegative individual histogram entries**, instead of signed projections.

The theorem reconstructs the **initial 48-phase marginal**, not the entire initial 96-port branch-bit joint law. The original all-one model has k=0; the rank loss occurs on explicitly declared weighted critical surfaces. One bit per action and 2k scalar histogram entries are different resource measures.

Next: derive finite-sample error amplification/conditioning comparisons across the three Boolean tags near critical incidence surfaces, and determine how much information remains when the terminal phase itself is coarsened.
