# X6 native-event source audit and the exact role of edge continuity

Date: 2026-11-19. Source snapshot: `awdawmip/enterprise-math@ef720decf4a35a276e509964250571a55421b9f8`.

Status: author source audit and exact restricted derivation; prepared as a delegated component of the parent continuation. No formal Task/CLAIM/Review authority is claimed.

## 1. Scope and source conclusions

The scientific objects are three distinct signed native axes embedded in Heartbeat X6, one chosen native Cell c, three named unit source tokens, and ordered SHELL/CLOSURE microevents. The remaining three spatial axes retain their ambient X6 meaning. The token histories and common Cell are retained throughout.

The current inspected sources support the following exact distinctions:

| Source | Actual content | Consequence for inter-event edge sign |
|---|---|---|
| P000 discrete-direction and triadic-balance definition, §5.3 | Primitive stable balance has exactly three nonzero force terms and TRIADIC_CLOSURE_E; legal Cell/direction incidence and dynamics may be further refined | P000 alone supplies no law comparing the sign of a named generator edge in two events |
| Atomic scatter V1, §§3–5 | Three distinct-axis equal-unit ports coalesce at one Cell; unique common-midpoint shortest branch is III | This fixes path incidence and the joint BRC branch, not the next generator |
| Signed-Q correction V5, §§4–6 | Four twists with product −1 form the signed-frame gauge-covariant completion | Gauge covariance transports a chosen operator under a coordinate change; it does not assert that nature independently reselects a physical twist every event |
| Corrected Cell internal state V1R, §§2–4 | A declared deterministic fixed-Q SHELL/CLOSURE interface has 1920 states in 160 C12 cycles | Within this interface a common reference frame has the same generator at each scatter, hence delta=+1 |
| Axis/channel V2R, §§4–7 | Bare translation-invariant, fully S6-equivariant unsigned channel transport is identity | The theorem concerns unsigned pure spatial translation; the source explicitly separates signed internal/time-dependent dynamics |
| Rotation-path groupoid V2, §8 | Path-level laws are sections/weights over provenance-preserving fibers | The carrier does not choose a next generator, branch probability, or physical time law |

Thus the fixed-Q model already provides a consistent restricted realization with the desired continuity. The weaker equal-unit closure/III conditions do not force that realization to be the only possible dynamics.

The audit is a comparison of these exact source contracts. GitHub code search returned incomplete empty results even for known existing terms, so those search results are not used as evidence that no other project artifact exists.

## 2. III uniqueness extends to every V5 twist

Fix oriented selected axes indexed i modulo 3 and signs a_i with product −1. Write

    Q_a(e_i)=a_i e_(i+1),     d_i=s_i e_i.

For one named token, the two shortest native paths between c+d_i and c+Q_a d_i are

    INNER: c+d_i -> c -> c+Q_a d_i,
    OUTER: c+d_i -> c+d_i+Q_a d_i -> c+Q_a d_i.

Every step is a primitive signed-axis X6 step. The OUTER displacement from c has support exactly {i,i+1}, with both coordinates nonzero, because a_i and s_i are ±1. Consequently no OUTER midpoint equals c. The three OUTER midpoint supports are {0,1}, {1,2}, and {2,0}; these are distinct, so the three OUTER midpoints are pairwise distinct.

It follows that all three token midpoints coincide if and only if all three tokens take INNER. This proof is independent of the signs of a and s. Therefore the source's III theorem holds for all 8 signed source words and all 4 V5 twists.

This is a native Cell/path statement inside the declared equal-unit restricted event model. It uses no Euclidean balance law and introduces no extra spatial direction. It also establishes that III alone cannot discriminate among the four allowed algebraic twists.

## 3. Explicit indistinguishable two-event histories

Use the same fixed observation axis j=0, the same oriented unsigned passage 0→1→2→0, the same chosen Cell c, and the same first generator a=(-,-,-).

Consider two model histories:

| Quantity | History H+ | History H− |
|---|---|---|
| Initial signed shell s | (+,+,−) | (+,−,−) |
| First generator a | (−,−,−) | (−,−,−) |
| Intermediate shell s'=Q_a s | (+,−,−) | (+,−,+) |
| Second generator b | (−,−,−) | (−,+,+) |
| Final shell s''=Q_b s' | (+,−,+) | (+,−,−) |
| Fixed-axis readout (s_0,s'_0,s''_0) | (+,+,+) | (+,+,+) |
| delta=a_2 b_2 | +1 | −1 |
| Initial invariant relation r_i=s_i a_i s_(i+1) | (−,+,+) | (+,−,+) |

Every source at every scatter has a valid two-step INNER path through c. Each event has three named unit source tokens, three distinct underlying axes, the same unsigned cycle, and the same III branch choice. The two initial r states are distinct, so this is not merely a common signed-frame relabeling.

In the model class that permits both displayed second generators, the fixed-port shell reads and the unsigned passage/branch data fail to distinguish the histories. This is an explicit failure of the implication

    equal-unit common-Cell closure + V5 twist constraint + III
        => named edge continuity.

The statement does not assert that the currently unspecified physical scheduler permits both histories. Rather, it identifies the exact extra decision that a scheduler must make to exclude the ambiguity. It also shows that restoring unsigned branch provenance alone cannot repair the missing signed inter-event relation.

## 4. A positive fixed-generator bridge already present

V1R's deterministic local transition is

    (F,SHELL) -> (F,CLOSURE) -> (Q_a F,SHELL)

for one fixed generator a in a consistent named frame. For the canonical gauge a=(-,-,-), this is exactly the corrected source interface; V5 transports the same interface to any one of the other three gauges.

Repeat the same transition twice. The two occurrences use the same a, so delta=a_(j−1)^2=+1. The three shell-boundary observations determine

    r_(j−1)=y0 y1,
    r_(j−2)=y1 y2,
    r_j=−y0 y2.

All three scattering paths at every closure can be selected as III by §2. Therefore the fixed-generator no-external-sign-calibration reader has a complete restricted native Cell/path realization within the already declared deterministic interface.

Its physical scope remains exactly that interface: the source has not specified that every TRIADIC_CLOSURE_E occurrence follows a fixed-generator scheduler.

## 5. Where the adaptive candidate can live

The parent continuation is investigating the gauge-covariant candidate next-generator policy

    b_i=−s_i s_(i+1),

where s is the signed shell immediately before the current scatter and a is the generator used for that scatter.

The source's SHELL→CLOSURE transition preserves the whole named signed frame F. Hence the candidate can be implemented without unbounded historical memory by augmenting the local state with an active twist:

    (F,a,SHELL)
        -> (F,a,CLOSURE)
        -> (Q_a F, b(F), SHELL).

The three incoming source signs are available in the CLOSURE internal frame; the candidate computes the next active twist before replacing the frame by the outgoing one. It does not substitute a two-force balance event: all three sources meet at the same atomic Cell throughout the underlying event.

An equivalent implementation after release may reconstruct the previous signs from current s' and a:

    s_i=a_i s'_(i+1),

then use b_i=−s_i s_(i+1). Thus it needs the current full signed frame and active twist, not a new history register or an additional spatial axis.

V1R's internal-fiber typing permits these variables as a finite model extension. Its existing fixed-Q transition does not itself supply the feedback law's native permission. The proposed scheduler must therefore be presented as a specific constructible candidate with independently checkable dynamical properties.

A useful exact observation is that this feedback map is invertible on the 32 (s,a) states. Given output (s',b), the equations b_i=−s_i s_(i+1) determine s up to simultaneous sign reversal. The V5 product condition applied to a_i=s'_(i+1)s_i requires

    product(s)=−product(s').

Because simultaneous reversal changes the product of three signs, exactly one candidate s meets the condition, after which every a_i is determined. This is an author proof of bijectivity; the parent checker may verify its cycle structure.

## 6. Minimal open bridge

The actionable next native-event question is a signed inter-event scheduler, stated at the retained named Cell/Port/source interface. Two concrete candidates now exist:

1. retain active Q over the two-scatter observation window, as in the existing deterministic interface;
2. use the explicit adaptive next-twist policy and prove its observer recovery properties.

The most general readout criterion is that the relevant inter-event delta be constant on each admitted fixed-axis observation fiber; the parent's algebraic continuation develops that condition and its classification.

Current input definitions suffice to locate the candidate state variables and realize their primitive paths. The remaining license question is which signed scheduler belongs to the intended physical TRIADIC_CLOSURE_E law. Neither source covariance nor the unsigned channel flatness theorem resolves it.

## Exact source references

All references below are read at the snapshot in the header.

- `p000_reality_foundation.json`.
- `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`, §5.3.
- `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`.
- `definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json`.
- `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`.
- `research_notes/X6_TRIADIC_ATOMIC_SCATTER_AND_BRC_CORRELATION_V1_20260906.md`, §§2–6 and §12.
- `research_notes/X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md`, §§2–4.
- `research_notes/X6_SIGNED_INTERNAL_Q_GAUGE_CORRECTION_V5_20260906.md`, §§4–6.
- `research_notes/X6_AXIS_CHANNEL_FRAME_GAUGE_AND_FLAT_TRANSPORT_V2_20260906.md`, §§4–7.
- `research_notes/X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md`, §§2–3 and §7.
- `research_notes/X6_ROTATION_PATH_GROUPOID_V2_20260906.md`, §8.
- `research_notes/portable_direct/20261118_x6_gauge_covariant_followup/README.md`, Appendix A.

