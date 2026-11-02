# R5 — Exact four-source K2 answer-coin classification in the genuine two-law stopped tree

Date: 2026-11-03 (Asia/Shanghai). Research status: **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**.

## Frozen input, predecessor, and scope

Scientific frontier: `awdawmip/enterprise-math@b0c63e26d94308a23232b7778fb8b520c96e8c70:research_notes/brc_r5_k2_single_source_answer_fiber_20261103_t0055/RESEARCH.md`; the fixed-source predecessor is the genuine two-law serial stopped tree of `b25947a3c94313c3ccf993e70de1f87af8a833f0`. Its frozen scientific input pins are **global `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`**; these are *scientific* pins, not the current operational-rule snapshot. This result changes only the specified terminal answer kernels and does not alter P000, ACTIVE worldview or the time/likelihood-ratio collision structure.

Mother objective: find a legitimate finite two-law stopped-tree model for which `conv O(FULL)=conv O(LR)` but the actual images `O(FULL)` and `O(LR)` differ, with `O=(e_P,e_Q,T_P,T_Q)`. This note provides a **complete classification of a four-parameter subfamily**; the mother objective remains open. The theorem concerns a classical auxiliary finite probability tree with source-preserving positive BRC probability flows, not an established native-X6 correspondence.

## Model and statement

Use the fixed tree `X -> J -> K1 -> K2` with sources `s=(C,I,BJ,IJ)`, P/Q source masses `(1/4,1/4,1/8,1/8)` plus D of mass `1/4`. A flag `X=1` (probability `x`) prevents I/IJ from reaching K1. Sources BJ/IJ have J stop/continue decisions at time 2. A K1 continuation is followed by source-specific P success probability `alpha=(1/2,2/3,1/2,3/4)` and Q success probability `alpha/2`; a K2 continuation has P success `c=2/3`, Q success `c/2=1/3`. The two seedless LR decision keys at `(time,likelihood ratio)` remain K1 `(3,1)` and K2 `(4,2)` (and J `(2,1)`); LR uses common J, K1, K2 continuation controls `y,z,t`. FULL may condition on hidden source and available history. At earlier stopping sites use the exact baseline terminal labels and J answer kernels of the predecessor.

**New parameter family.** After *each* source's K2 success, independently generate a Q-label answer nature coin with P-law probability `eta_s/8` and Q-law probability `eta_s`, where **every real `eta_s` lies strictly between 0 and 1**. All natural Bernoulli probabilities in the tree are strictly between 0 and 1. The behavior policy probabilities may include endpoints. Define the fixed source-success weights

    q*=(1/8, 1/6, 1/16, 3/32),  A*=sum(q*)=43/96,
    d*=5/32,  mu=(sum_s q*_s eta_s)/A*.

Let `n_mu=(-2/3,-7/3,-1+mu,4-2mu)` and let `h` be the support function over **all real history-dependent behavioral policies**. Then

    h_FULL(n_mu)-h_LR(n_mu)
      = (1/3) sum_s q*_s (mu-eta_s)_+
      = (1/6) sum_s q*_s |eta_s-mu|.                (THEOREM)

In particular, throughout the continuous strictly positive parameter family:

    conv O(FULL)=conv O(LR)  iff  eta_C=eta_I=eta_BJ=eta_IJ.

When all `eta_s` are equal, **the actual real observer images coincide** `O(FULL)=O(LR)` and the LR image has full four-dimensional local rank. For nonconstant `eta`, the stated single explicit signed normal strictly separates the convex hulls. Consequently this whole four-parameter answer-coin family has no equal-hull/different-image solution, although useful source/time couplings outside this family remain open.

## Exact positive source-flow calculation

Write `b` for eight times the BJ mass that continues from J, and `i` for eight times the IJ mass that continues; these are independently selectable by FULL with `0<=b<=1`, `0<=i<=1-x`. Set

    w=(1/4,(1-x)/4,b/8,i/8),
    d=b/16+3i/32, H(x)=1/8+(1-x)/6,
    q_s=w_s alpha_s z_s,
    r1=sum_s q_s,  s_s=c q_s t_s,
    r2=sum_s s_s, S_eta=sum_s eta_s s_s.

The effective FULL controls `z_s,t_s in [0,1]` represent conditional source-wise mass averages, including root-history adaptation. By exact P/Q terminal-path summation,

    eP = 107/128-21x/128+d/4-S_eta/8,
    eQ = 13/64+3x/64-d/2+S_eta/4,
    TP = 3+r1+r2,  TQ = 3+r1/2+r2/4.       (1)

Use the fixed invertible affine observer coordinates of the predecessor:

    vP=eP-107/128, vQ=eQ-13/64,
    x'=(-vP/2-vQ/4)/(9/128),
    d'=(-3vP/64-21vQ/128)/(9/128),
    r1'=4(TQ-3)-(TP-3), r2'=2(TP-3)-4(TQ-3).

Exact substitution yields `(x',d',r1',r2')=(x,d-S_eta/2,r1,r2)`. Thus the physical normal `n_mu` is, up to an additive scalar common to both policy classes, the functional

    Psi = r1+d'+(mu/2)r2
        = d + sum_s q_s z_s [1+(c/2)t_s(mu-eta_s)].  (2)

All four q values and all transition kernels are positive, with no cancellations in the probability flows; the signed coefficients in `Psi` are observer costs, not negative path probabilities.

## All-real FULL optimization

For each `s`, `1+(c/2)t_s(mu-eta_s) >= 2/3 >0` because `c/2=1/3` and `0<eta_s,mu<1`. Therefore optimize over `z_s` by setting all equal to 1; optimize over `t_s` by choosing `t_s=1` exactly where `eta_s<mu`, otherwise 0. Equation (2) reduces to

    d + sum_s w_s alpha_s [1+(1/3)(mu-eta_s)_+].

Every coefficient of `b` and `i` is strictly positive, and the coefficient of `(1-x)` is strictly positive. Hence its global maximum is reached at `x=0,b=i=1`, with weights `q*`; it equals

    A*+d*+(1/3)sum_s q*_s(mu-eta_s)_+.          (3)

This is valid for all real adaptive FULL strategies, not merely deterministic samples.

## All-real LR optimization

LR enforces `b=y` and `i=(1-x)y`. Put

    d=(5-3x)y/32, A=H(x)+d,
    q(x,y)=(1/8,(1-x)/6,y/16,3(1-x)y/32),
    E(x,y)=mu A-sum_s eta_s q_s(x,y).

With common `z,t` equation (2) becomes

    Psi_LR = zA+d+(c/2)zt E(x,y).                    (4)

All q_s(x,y) lie between 0 and their own `q*_s`. Let `delta=A*-A>=0`. Because `sum q*=A*` and `sum eta_s q*_s=mu A*`, both `sum eta_s (q*_s-q_s)` and `mu delta` lie in `[0,delta]`. Therefore `|E|<=delta`. Also `d<=d*` and `delta<=A*-zA=A*-r1`. Hence

    Psi_LR <= r1+d*+(1/3)(A*-r1)
            <= A*+d*.                              (5)

Equality is attained at `x=0,y=1,z=1` with any `t`, because `E=0` there. Therefore `max_LR Psi=A*+d*`. Subtracting from (3) proves the exact support-gap formula. Since `sum q*_s(mu-eta_s)=0`, the positive part equals half the weighted absolute deviation. All `q*_s>0`, so the gap vanishes iff all four eta values coincide.

## Uniform kernel: actual-image equality and full rank

If `eta_s=eta` for every source, `S_eta=eta*r2`, so the physical observation is the *same invertible affine shear* of the original auxiliary `(x,d,r1,r2)` for FULL and LR. For completeness, for an arbitrary FULL real policy set

    y=32d/(5-3x), z=r1/(H(x)+d),
    t=r2/(c*r1) if r1>0, else 0.

The constraints `0<=b<=1`, `0<=i<=1-x`, `0<=r1<=H(x)+d`, `0<=r2<=c*r1` guarantee `0<=y,z,t<=1`. This LR policy reproduces exactly `x,d,r1,r2`, and hence all four physical observer coordinates. The reverse inclusion is immediate because LR strategies are FULL strategies. Thus actual real images coincide.

At interior LR parameters, writing `A=H(x)+(5-3x)y/32`, the Jacobian of `(x,y,z,t)->(x,d,r1,r2)` is

    det J_aux = [ (5-3x)/32 ] * c*z*A^2 > 0.

The original physical observer map has determinant `-9/512`; the uniform shear has determinant 1. Thus the uniform-equality cases retain four-dimensional local rank.

## Rational example and exact validation

At `(eta_C,eta_I,eta_BJ,eta_IJ)=(1/4,1/2,3/4,1/2)`, `mu=20/43`, the normal is `(-2/3,-7/3,-23/43,132/43)`. The maximizing FULL strategy uses `x=0`, all J continue, all K1 continue and *only source C* continues at K2. Its physical observer is

    W=(335/384,25/192,113/32,623/192).

Exact support values are `h_FULL=14833/2064`, `h_LR=29629/4128`, with gap `37/4128` and the all-real distance certificate

    dist_inf(W,conv O(LR)) >= (37/4128)/(8-3*20/43)
                             = 37/27264.

`VERIFY.py` executes a standalone standard-library `fractions.Fraction` check. For each of five strictly positive rational eta vectors, it recomputes all 2048 reduced FULL deterministic observer points and 16 LR deterministic points by independent terminal-path summation and checks the exact support gap, witness, positivity, and physical-coordinate norm. The finite deterministic-policy reduction is exact for the convex hull of a finite tree with independently randomized nodes: its observer map is multi-affine in local conditional action probabilities; repeated hidden-origin histories are represented by distinct FULL decisions. A further 120 genuinely nonbinary, flag-adaptive FULL policies verify the independent source-flow formula against the terminal-path implementation, and uniform-coin cases test the explicit real-strategy aggregation. The continuous theorem comes from the algebraic optimization above, **not** from extending those finite tests by extrapolation.

Actual executed result: `PASS_EXACT_R5_FOUR_SOURCE_K2_COIN_CLASSIFICATION`, **31,733 exact assertions** (see `EXACT_OUTPUT.txt`). Numerical/theorem scope is exactly the four-parameter coin family, fixed source/time kernels and declared action structure.

## Publication and next question

Researcher conclusion pending independent review, native CLAIM and Source Result, separately from author-side GitHub preservation. On the current sites-connected native gateway, `research_authority_granted=false` and Site transport is read-only; native active-owner lookup status must be reported as actually observed, without borrowing another research session. This research note contains no secrets or delegated session keys.

**Next discriminating unit.** The positive-weight absolute-deviation invariant classifies all K2-success answer coins whose P/Q Q-label probabilities are locked in the ratio `1:8`. Relax that cross-law ratio independently for one or more sources while preserving genuine LR collision keys and strict positivity; derive the affine observer lift and test whether equal-hull candidates can remain four-dimensional without actual-image equality. A second route allows source-conditioned *time* branching at K2 or post-K2 history. For any rational candidate first certify all-signed hull equality via finite deterministic vertices and exact rational convex combinations (or find Farkas normals); only then test real-image membership. Keep the parent four-observer mother problem open until that full criterion is met.
