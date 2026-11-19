# X6 three-source relation: observable event laws and reversible feedback

Date: 2026-11-19. Status: author derivation with exact finite BRC checks; portable contribution within the parent X6 continuation. This note supplies no independent Review, Task CLAIM, or primitive-event permission.

Source snapshot: `awdawmip/enterprise-math@ef720decf4a35a276e509964250571a55421b9f8`.

Sources used:

- `p000_reality_foundation.json`, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json`.
- `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`.
- `research_notes/X6_SIGNED_INTERNAL_Q_GAUGE_CORRECTION_V5_20260906.md`, particularly sections 5–7.
- `research_notes/X6_TRIADIC_ATOMIC_SCATTER_AND_BRC_CORRELATION_V1_20260906.md`, particularly sections 3–6.
- `research_notes/portable_direct/20261118_x6_gauge_covariant_followup/README.md`, Theorems 1 and 3 and Appendix A.
- `docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md` and `research_constraints/heartbeat_brc_only.json`.

## 1. Exact scope and BRC carrier

Choose one native Cell c and a cyclically oriented triple of distinct native X6 axes. Indices 0,1,2 label these selected axes; the other three native axes remain part of the ambient space. Each selected axis carries one named unit source token. Its current radial sign is s_i. The active generator has edge signs a_i with product -1 and sends e_i to a_i e_(i+1). Time indexes ordered scatter events.

The BRC carrier retains:

1. the chosen six-component Cell anchor;
2. each source name and original signed port;
3. each current signed port;
4. the active generator;
5. the ordered generator and path history;
6. the three jointly selected INNER branches per atomic scatter.

For a token on d=s_i e_i and q=a_i s_i e_(i+1), the two shortest branch words are INNER=(-d,q) and OUTER=(q,-d). The INNER midpoint is c; the OUTER midpoint is c+d+q. The three OUTER supports are different axis pairs, so the existing common-Cell argument applies to every V5 twist: among all eight joint branch choices only III has one common midpoint. The code implements this named III branch specialization. Unit branch multiplicities stay nonnegative; radial signs are attributes, never signed branch masses.

Let pi read the sign at each currently occupied selected axis. Directly from the named branch endpoint,

    pi(Apply_a(B))_i = a_(i-1) pi(B)_(i-1).

This is an exact carrier/action/readout correspondence. Concatenating branch words proves the correspondence for any finite sequence of the declared atomic III operations. The program preserves the original carrier and source history while computing this observer; it does not replace the carrier by three anonymous marginal signs. Generator feedback is an explicitly declared additional update of the retained active-twist label. No pi, trigonometric, continuum, or approximate operation is used.

This correspondence establishes the restricted BRC model and observer. Whether a particular feedback law is selected by an actual `TRIADIC_CLOSURE_E` permission predicate remains a separate source question.

## 2. The exact event-law criterion

Write b for the next generator and j for a fixed observing axis. Let

    y0=s_j,
    y1=a_(j-1)s_(j-1),
    y2=b_(j-1)a_(j-2)s_(j-2),
    r_i=s_i a_i s_(i+1),
    delta=a_(j-1)b_(j-1).

The already established identities are

    r_(j-1)=y0y1,
    r_(j-2)=delta y1y2,
    r_j=-delta y0y2.                         (1)

For any specified admissible population E of triples (s,a,b), define the observation fiber E_y by fixing the three-read word y.

**Theorem 1.** The three-read observer recovers the entire initial r on E if and only if delta is constant on each nonempty fiber E_y.

**Proof.** If delta descends to y, (1) reconstructs r. Conversely, with y fixed, the two values of delta give different r_(j-2) and r_j because all y entries are nonzero signs. Thus a fiber containing both delta values contains two different r. QED.

Consequently edge continuity (delta=+1) is sufficient, while a state-dependent event can also make delta inferable from y. The sufficient condition can be implemented by a known flip law instead of preserving the edge.

**Source-independent corollary.** If E has the form all eight s words times an allowed pair relation A of (a,b), then delta must be constant on A. Indeed every pair (a,b) realizes every y, with exactly one corresponding s. For one fixed edge there are 510 nonempty readable A among 65,535 nonempty pair relations. Requiring readability at every axis gives 60. If A is also cyclically invariant, every such readable pair obeys b=a. The finite count is optional evidence; the preceding fiber argument proves the classification criterion.

## 3. Four deterministic local laws, exactly two observable laws

Assume the next generator is a deterministic function b=F(s,a) on all 32 (s,a) states. The function uses no extra remembered state or distinguished observing port. Require covariance under independent, time-independent sign-reference changes and under cyclic axis relabeling. These are additional declared hypotheses for this finite classification.

Set D_i(s,a)=a_i F_i(s,a). Both twists change by the same endpoint gauge signs, so D is gauge invariant and product D=+1. The prior four-state orbit theorem implies D=D(r).

The r-domain has one cyclic fixed point (---) and one orbit of length three. The product-positive D-codomain has the fixed point (+++) and one orbit of length three. At r=---, equivariance forces D=+++. On the other orbit its value at one point can be any of the four D values. Thus exactly four functions exist:

| Law | D_i(r) | Relation update r'_i=D_i(r)r_(i-1) | Fixed-axis observation |
|---|---|---|---|
| Persistent generator | +1 | r_(i-1) | Complete after three reads |
| Ingress-sector feedback | -r_i | r_(i+1) | Complete after three reads |
| Egress-sector feedback | -r_(i-1) | -1 | Two initial sectors remain indistinguishable at every horizon |
| Stationary relation | -r_(i+1) | r_i | Two initial sectors remain indistinguishable at every horizon |

The second column exhausts all 4^4=256 orbit functions after cyclic equivariance is imposed. The third column uses product r=-1.

For repeated updates, one always has y_t y_(t+1)=r^t_(j-1). The first two laws rotate the relational state in opposite directions, so consecutive products reveal two different edges. The stationary law repeats one edge forever. The egress law exposes one initial edge, then the relation is --- and all later adjacent products are -1. These dynamics prove the all-horizon claims; the six-read check is a finite consistency check.

Three reads are minimal for the complete laws in the stated raw-sign observer: two reads determine only r_(j-1), and the four initial relational states split into two pairs. No calibration tag or event-side metadata is included in this read-count statement.

## 4. A changing-edge law with no calibration cost

For the ingress-sector law,

    b_i=a_i(-r_i)=-s_i s_(i+1).               (2)

The expression on the right is V5's existing alpha_state construction evaluated on the ingress sign pattern. The new conditional use is to make it the next active generator. It automatically has product -1 and the required two covariances.

On the detector predecessor edge,

    delta=-r_(j-1)=-y0y1.

Substitution in (1) gives

    r_(j-1)=y0y1,
    r_(j-2)=-y0y2,
    r_j=y1y2.                                (3)

Thus both independent relative-sign bits are read without an external calibration, even though the predecessor edge flips whenever r_(j-1)=+1. For example s=(+++), a=(-++), j=0 gives b=(---) and y=(++-). The observed edge i=2 changes from + to -, while (3) correctly recovers r=(-++). The old continuity-only formula would give the wrong relation in this example.

The timing in (2) matters. Using the output pattern s'=Q_a s instead gives b_i=-s'_i s'_(i+1), which is the egress-sector law and collapses r to ---. The existing FRAME memory can distinguish these two inputs; a source-to-event implementation must say which one it uses.

## 5. The feedback is reversible and preserves the signed six-phase law

Define the internal state update

    T(s,a)=(s',b),
    s'_i=a_(i-1)s_(i-1),
    b_i=-s_i s_(i+1).

**Theorem 2.** T^3(s,a)=(-s,a), hence T^6 is the identity on the sign/twist state. On every complete named-token FRAME, the exact period is six.

**Proof.** Put P=s0s1s2. Applying the update twice yields

    s''_i=-P a_(i+1),
    a''_(i-1)=P a_i s_i.

Therefore s'''_i=a''_(i-1)s''_(i-1)=-s_i, and

    a'''_i=-s''_i s''_(i+1)=a_i.

Three scatters return each token to its initial named axis and reverse its sign; six return both axis and sign. Any complete named FRAME return must have a step count divisible by three, and the three-step sign reversal prevents a return at three. QED.

An explicit inverse makes the information preservation transparent. Given the output (u,b), let U=u0u1u2. Then

    s_i=U b_(i+1),
    a_i=u_(i+1)s_i.

The 32 sign/twist states contain four two-cycles over r=--- and four six-cycles over the other three r values. The shorter two-cycles omit token correspondence. With all six source-to-axis assignments retained, all 192 complete FRAME/twist states have period six.

For comparison, persistent generators have the same sign/twist cycle counts. The stationary relation law is a bijection with sixteen two-cycles on sign/twist states and period six on named FRAMEs, but generally T^3 is not overall sign reversal. Egress feedback maps 32 states onto eight, with four preimages per output and a transient of length at most one.

**Finite-family equivalence.** Among the four laws of section 3, exactly two have T^3(s,a)=(-s,a) for every input. They are also exactly the two laws that permit complete three-read fixed-axis recovery. This is a classification of that declared family; it can be used as a precise discriminator for proposed native event laws.

The period concerns the internal FRAME/twist projection. The appended ordered BRC event history remains distinct after six events, as required for time-labelled provenance.

## 6. Optional extension: independently changing reference frames in time

The original V5/readout theorem uses one reference choice across events. Its gauge invariance is correct in that scope. To let the reference itself change independently at times 0,1,2, include temporal transport signs k^t_i and write

    s^(t+1)_i=k^t_i a^t_(i-1) s^t_(i-1).

Here a^t is a same-time spatial generator and k^t transports the same named axis to the next reference frame. Under local frame signs epsilon^t,

    a'^t_i=epsilon^t_i epsilon^t_(i+1) a^t_i,
    k'^t_i=epsilon^(t+1)_i k^t_i epsilon^t_i,
    y'_t=epsilon^t_j y_t.

For i=j-1 define

    Delta=a^0_i a^1_i k^0_i k^0_j,
    z01=k^0_j y0y1,
    z12=k^1_j y1y2.

All three are invariant under independently chosen temporal reference changes. The correctly transported readout is

    r^0_(j-1)=z01,
    r^0_(j-2)=Delta z12,
    r^0_j=-Delta z01 z12.                    (4)

Direct substitution proves (4). Choosing common time-independent references sets both k vectors to +1 and recovers (1). This extension adds a specified temporal-reference language; no extra calibration requirement is imposed on the earlier fixed-reference experiment.

## 7. Exact author check and next native question

Run `python check_relation_updates.py`. The checker writes `relation_update_results.json` and verifies:

- all 256 preselection joint BRC branch candidates, with unique III common-Cell selection;
- all 128 two-event named branch histories and their endpoint observer correspondence;
- all 256 gauge-orbit update functions, yielding four cyclic rules;
- all 384 unrestricted two-scattering detector cases;
- each rule on all 32 states, all eight gauges, three cyclic shifts and three detector axes;
- all 192 complete named FRAME inputs per rule for the cycle classification;
- all 24,576 transported-reference observer cases;
- all 65,535 nonempty source-independent generator-pair relations.

The arguments above prove the unrestricted finite classifications and the stated arbitrary-horizon behavior. The finite checks use the retained named BRC carrier and provide concrete reproducibility.

The strongest next source question is now: does the actual permitted event retain the generator, use the ingress alpha_state as the next generator, or follow a different explicitly specified update? Both of the first two choices realize the exact six-phase reversal and complete calibration-free three-read observation in this model. The ingress/egress distinction is the decisive new implementation obligation.
