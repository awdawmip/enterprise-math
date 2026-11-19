# EC49FTZ — Sharp parameter monotonicity, a two-coordinate stochastic order, and a uniform large-negative-parameter limit

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED.

## Provenance and precise research scope

- Native BRC16943 scientific freeze: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab (unchanged).
- Inherited native Bellman result: EC49FTH PR #2774, commit 999bf1069403306b3813e0e390dae4435d7b4b8c, AUTHOR_PROVED / NOT_REVIEWED.
- Direct parent: EC49FTY PR #2811, commit f82eb6b57cb05443564f3bc588a2953ac7651007, with its exact all-real-epsilon, high-gap stochastic-order proof.
- The present proposition concerns **external price-prior conditional probability** over the fixed inherited Bellman optimizer; it is not a native X6, BRC/heartbeat or new Bellman theorem. In particular two price parameters do not constitute a native two-dimensional plane or slice.

## Fixed model and inherited external pricing chart

Let R=[3/4,49/64] x [7/16,57/128]. Define

    M_*(a,b)=(525/8)a-(231/4)b-9/8,
    Z_*(a,b)=(35/32)a-b/16-5/96,
    P(a,b)=M_*(a,b) Z_*(a,b),
    h_epsilon(a,b)=1-epsilon P(a,b).

The exact range in which h_epsilon is globally nonnegative on R is

    epsilon in (-infinity,E], E=1048576/18958647.

The density normalizer cancels when conditioning. On the inherited high-gap branch, let

    1469/64 < m < 187/8,
    U=3/4,
    L(m)=(8m+173)/480,
    b(m)=(47-m)/54,
    x(m)=(740-m)/945,
    d(m)=49/64-x(m)>0,
    c=16/945.

The continuous conditional density **before normalization** is

    K_epsilon(m,z)=c[1-epsilon m z], L(m)<z<U.

The clipped stratum is the *single* observed atom Z=U, whose unnormalized mass is

    B_epsilon(m)=(1/54) integral_{x(m)}^{49/64}
                     [1-epsilon P(a,b(m))] da.

Its base mass is B0=d/54. The continuous base mass is A0=c[U-L(m)].

At the clipping boundary, exact substitution proves

    M_*(x(m),b(m))=m, Z_*(x(m),b(m))=U.

Along its clipped a-fiber, writing r=a-x(m), 0<=r<=d, gives

    M_*(a,b(m))=m+alpha r, Z_*(a,b(m))=U+beta r,
    alpha=525/8, beta=35/32.

Thus the **average latent P at the atom** and the average P in the continuous part are

    p_atom(m)=m U + (m beta+U alpha)d/2 +alpha beta d^2/3,
    p_cont(m)=m [L(m)+U]/2.

For all interior m,

    p_atom(m)>mU>p_cont(m)>0.

The inequality retains the latent clipped a-information: the observed top atom is not assigned the boundary value mU.

## Theorem 1: strict monotone-likelihood-ratio ordering in epsilon at each fixed m

For every fixed interior m and all real epsilon_1<epsilon_2<=E,

    Law(Z | M=m;epsilon_2) <=_st Law(Z | M=m;epsilon_1).

More precisely, for every L(m)<z<U,

    F_epsilon_1(z|m) < F_epsilon_2(z|m),

and the probability of the upper atom is strictly larger at epsilon_1.

**Proof.** The epsilon=0 conditional base measure has constant positive continuous density c on [L,U) and a positive atom B0 at U. The epsilon-dependent multiplier is 1-epsilon p_eff(z), with

    p_eff(z)=m z,  L<z<U,
    p_eff(U)=p_atom(m).

It is strictly increasing on the support, including the jump from the continuous part to the atom, since p_atom>mU. For epsilon_1<epsilon_2 the likelihood ratio, ignoring its positive m-dependent normalizing constant, is

    R(z)=[1-epsilon_1 p_eff(z)]/[1-epsilon_2 p_eff(z)].

It is strictly increasing in p_eff because

    dR/dp_eff=(epsilon_2-epsilon_1)/(1-epsilon_2 p_eff)^2>0.

The denominators are positive for the given open m interval, including at epsilon_2=E. Therefore the conditional family is strictly monotone-likelihood-ratio ordered, implying the stated strict interior CDF order. The top-atom probability is also strictly ordered since it is the maximal-support event and both the atom and the continuous mass are positive. QED.

An independent differentiation identity makes the last claim explicit. Writing A_e=A0-e A1, B_e=B0-e B1 where

    A1=A0 p_cont, B1=B0 p_atom,

the top-atom probability q_e=B_e/(A_e+B_e) satisfies

    dq_e/de=(B0 A1-B1 A0)/(A_e+B_e)^2
           =A0 B0(p_cont-p_atom)/(A_e+B_e)^2 < 0.

The proof works for arbitrarily negative finite epsilon.

## Theorem 2: joint two-parameter partial stochastic order

Let m_1,m_2 lie in (1469/64,187/8) and epsilon_1,epsilon_2 in (-infinity,E], with

    m_1<=m_2, epsilon_1>=epsilon_2.

Then

    Law(Z|m_1;epsilon_1) <=_st Law(Z|m_2;epsilon_2).

**Proof.** Apply Theorem 1 at m_1 when epsilon_1>epsilon_2 (equality if equal), then apply the EC49FTY theorem at the fixed epsilon_2 as m increases from m_1 to m_2. First-order stochastic dominance is transitive. QED.

This is a genuinely two-coordinate comparison: M and the prior tilt epsilon can change **simultaneously in opposite directions**. It supplements, rather than reproduces, EC49FTY's fixed-epsilon order.

## Theorem 3: pure-P boundary law and a uniform total-variation bound

Let s>=0 and epsilon=-s. At each interior m define two conditional laws with the *same inherited optimizer*:

- mu_0: conditional law for constant prior h=1;
- mu_infinity: conditional law for the positive prior h=P=M_* Z_*.

Put C0=A0+B0 and C1=A1+B1. Since the unnormalized prior is 1+sP, a direct measure decomposition gives the **exact mixture identity**

    mu_{-s}=[C0/(C0+s C1)] mu_0
           +[s C1/(C0+s C1)] mu_infinity.

The minimum and maximum of P on the original full rectangle are exactly

    P_min=17372631/1048576 >0, attained at (3/4,57/128),
    P_max=18958647/1048576, attained at (49/64,7/16).

Indeed M_* and Z_* are positive and both strictly increase in a and decrease in b, so their product has the same coordinate monotonicity.

Consequently C1/C0>=P_min on **every** conditional fiber, and

    sup_{m in (1469/64,187/8)}
       ||mu_{-s}(m)-mu_infinity(m)||_TV
         <= 1/(1+s*17372631/1048576).

Hence convergence to the pure-P conditional law is uniform in m, with an explicit O(1/s) bound. For L(m)<z<U its exact CDF is

    F_infinity(z|m)=
       [(c m/2)(z^2-L(m)^2)]/
       [(c m/2)(U^2-L(m)^2)+(d(m)/54)p_atom(m)].

The limiting pure-P law remains stochastically increasing in m: take the limit in the already-proved EC49FTY order for any fixed m_1<m_2. By Theorem 1 it is also the maximal right-shifted member in the closure of this epsilon family. QED.

## Evidence, invariants, and next research

- Exact rational implementation: EC49FTZ_PARAMETER_ORDER_VERIFY.py. Its JSON certificate and counts are generated by running the script with the Python standard library Fraction type.
- Checks include the original-chart clipping identity; exact clipped P antiderivative; exact conditional mixture identity for selected rational samples; exact P extrema; and finite rational tests of both stochastic-order directions. These checks are regressions; the universal epsilon and m quantifiers rest on the analytic arguments and inherited parent, not finite sampling.
- No original source pin, P000/ACTIVE world premise, native Bellman branch or mathematical admission is changed. Contributor provenance remains EC49FTY -> EC49FTZ; the parent remains NOT_REVIEWED, and this theorem is likewise NOT_REVIEWED.

**Next unresolved scientific problem.** Determine actual branchwise conditional fibers for the lower Bellman phase m<=1469/64 and match their boundary measures to the high-gap formula. Only after reconstructing that branch can cross-phase stochastic order be asserted or refuted. The pure-P law derived here is a convenient explicit limiting test case for this comparison.

**Control scope.** RS-EC49AS has previously been observed as UNPUBLISHED_TOPIC_METADATA_ONLY; this research note grants no formal CLAIM, Result, Review or task owner. Its Source publication and the own Researcher Activity checkpoint are distinct operations.
