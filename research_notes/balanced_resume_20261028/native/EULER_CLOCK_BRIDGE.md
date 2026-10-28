# Euler edge-index response under an explicitly supplied waiting clock

Author: EM-NATIVE-A8C19E. Activity: RA-BALANCE-NATIVE-20261028-A8C19E.
Date: 2026-10-28 (Asia/Shanghai).
Status: CONDITIONAL_INTERFACE_PROOF / NONBLIND / independent review pending. Native clock provenance remains UNKNOWN.

## Source and gap

The current full source `research_notes/chatgpt_direct/20261008_EULER_LOCAL_FIRST_RETURN_CLOCK.md` was read at immutable commit `1a553d4d28a105230ecebd5a555dc8adbab8ee28`, blob `6d0717195b3173fdf72a0cefcaafb0b2460b8a07`. Its K4 comparison grammar, fresh uniform neighbor choices, contact convention and positive path carrier remain unchanged. These are conditional model inputs, not a new native plane or primitive physical law. The full native spatial basis is X6; added clock indices below are separately typed external ordered labels.

That source distinguishes completed-contact count from comparison-edge count and already proves that return length and parity must be retained jointly. It gives, in the all-negative class,

    R_0(s)=3s^2/(9-4s^2),    R_1(s)=2s^3/(9-4s^2),
    P(edge length L even)=3/5,  E L=4,
    E[L|even]=18/5,            E[L|odd]=23/5.

For the fixed channel triple and initially independent fair sign, its normalized edge-index response c_n has

    C(s)=sum_{n>=0}c_n s^n
        =(18-9s-11s^2-8s^3)/(18-2s^2+2s^4),
    (c_0,c_1,c_2,c_3)=(1,-1/2,-1/2,-1/2),
    9c_(n+4)=c_(n+2)-c_n.

The open bridge is how a supplied clock changes these edge-index observations. No native clock law is supplied by the old source or by this note. We state an exact interface conditional on a fully declared waiting mechanism and exhibit a same-mean ambiguity that this interface detects.

## Declared waiting mechanism

Let W_1,W_2,... be iid positive-integer waits with pgf F(u)=E[u^W], independent of the complete underlying edge/channel/sign/path process. Let

    T_0=0, T_n=W_1+...+W_n,
    N(t)=max{n:T_n<=t},   t=0,1,2,... .

No comparison-edge operation occurs while waiting, and the observed edge state is held constant. At T_n the nth edge operation has completed. This specifies the left/right endpoint convention. The counter t is a separately typed clock, not another spatial axis and not a physical calibration.

The independence assumption is with the entire joint process; independence from only a current marginal or equal mean waits is insufficient. If contact, incoming direction, source history, signs or packet state affect waiting, the following scalar substitution is not automatically valid.

## Proposition 1: exact held-state transform

For any bounded scalar edge-index observable with expectation c_n, let a_t=E[c_{N(t)}]. Under the declared independent clock,

    A(u)=sum_{t>=0} a_t u^t
        = (1-F(u))/(1-u) * C(F(u)).                       (1)

This also holds coefficientwise for vector/complex observables. It is a response formula, not a conversion of signed phase coefficients into positive mass.

Proof. For each n, independence and the holding convention give

    sum_{t>=0} P(T_n<=t<T_(n+1))u^t
      = E[u^(T_n)(1-u^(W_(n+1)))/(1-u)]
      = F(u)^n (1-F(u))/(1-u).

Multiply by c_n and sum. For real 0<=u<1 the absolute total is at most sup|c_n|/(1-u), so regrouping is justified. Equivalently, since F(0)=0, every formal coefficient receives only finitely many n-contributions. The same identity extends analytically to |u|<1 by absolute convergence. Substituting the inherited C yields an exact rational/function interface for any declared F; no new path grammar is invented.

The bound from the old source, |c_n|<=(2/9)^floor(n/4), becomes

    |a_t| <= E[(2/9)^floor(N(t)/4)].                       (2)

It does not become the same exponential bound with n replaced by t. A decay rate in clock t requires information about the lower tail of N(t).

## Proposition 2: retain edge parity while changing duration

Let tau=T_L be the clock duration of one first-return excursion. Keep h=L mod 2 as the original transport mark. Then its exact joint generating functions are

    E[u^tau ; h=0] = R_0(F(u)),
    E[u^tau ; h=1] = R_1(F(u)).                            (3)

Proof. Condition on each complete edge path of length l and parity h. Independent waits give E[u^(T_l)]=F(u)^l without changing that path's positive weight or transport mark; sum the same source path classes. This composes the old joint kernels with the new clock and preserves their dependence. It does not replace the joint law by the product of duration and parity marginals.

If mu=E W<infinity, positive summation gives

    E tau=4mu,
    E[tau|h=0]=(18/5)mu,
    E[tau|h=1]=(23/5)mu.                                  (4)

The probabilities of h remain 3/5 and 2/5. In general h is not tau mod 2: edge parity is a transport mark, whereas tau is the new clock's elapsed duration.

## Exact discriminating pair: same mean clock, different responses

Clock D has deterministic W=2, hence F_D(u)=u^2. Clock G has independent geometric waits on {1,2,...}, P(W=w)=2^-w, hence F_G(u)=u/(2-u). Both have mean 2 and both give mean return duration E tau=8.

For D, N(t)=floor(t/2), so a_t^D=c_floor(t/2) and

    A_D(u)=(1+u)C(u^2).

For G, N(t) is Binomial(t,1/2), equivalently from (1),

    A_G(u)= [2/(2-u)] C(u/(2-u)),
    a_t^G=2^-t sum_{n=0}^t binomial(t,n)c_n.

Consequently

    (a_0^D,a_1^D,a_2^D)=(1,1,-1/2),
    (a_0^G,a_1^G,a_2^G)=(1,1/4,-1/8).

This exact difference is not resolved by matching either the mean per-edge wait or the mean completed-return duration. It closes the narrow question of whether those mean clock summaries determine the inherited Euler readout: they do not.

There is also a direct mark-typing witness. Under D every tau=2L is even, but the probability of transport mark h=1 is still 2/5. Replacing h by tau mod 2 would erase an entire positive return class, despite preserving the actual mean time. Equation (3) keeps it.

## Deduplication and method reuse

- The old Euler source's section 6 already proves that identical *edge-return-duration* marginals and transport marginals do not determine their joint law. We reuse that conclusion. This note addresses a distinct added per-edge held-state clock and gives its explicit composition interface; it does not repeat the old joint-dependence witness as a new result.
- `BRC-R-160/161` concerns observing a fixed periodic pulse through adversarial hold/skip schedules, with sharp detection horizon (L-1)(b+1). It has no iid waiting-clock pgf or held-state response transform in its stated interface. Our random independent clock is neither that adversarial schedule nor a claimed improvement of its sharp bound.
- `BRC-R-162` counts contact proposals in a fixed 81-state rebinding model. Its waiting/self-loop first-hit law and pointed-time moments are existing positive-BRC results, not a native clock calibration. This note does not repeat that first-hit problem or transfer its n-quotient to moving materials.
- Formula (1) is the standard renewal/holding-time composition, and (3) reuses the existing positive path alternative/serial composition. Resolution: COMPOSE_APPLIED, no new general tool family or literature novelty claim. The substantive source-specific output is the complete, correctly typed Euler interface and explicit mean-clock/parity counterexamples.

`verify_euler_clock.py` checks the exact series, direct binomial held-state calculation, and joint-kernel identities through a finite declared order. It is a symbolic certificate of the interface, not a rerun of the previous 136488-check scientific suite and not a new BRC-world experiment.

## Remaining boundary

Neither D nor G is promoted to a native physical clock or claimed a lawful native completion. Their purpose is to separate a missing input from a deduction. Native clock selection, any coupling between waiting and retained fields/paths, detector timing and calibration remain open. If these couplings are supplied, replace the scalar F by the actual state/mark-conditioned joint clock transition; preserve the declared path/source relations rather than assuming independence.

Researcher-ID: EM-NATIVE-A8C19E / TASK_RESEARCH
