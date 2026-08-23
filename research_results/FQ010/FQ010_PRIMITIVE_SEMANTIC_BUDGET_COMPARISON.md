# FQ010 — Primitive and Semantic Budget Comparison

Researcher-ID: `EM-FQ010-CA2555`

## Common substrate excluded from comparative cost

Both interfaces use the already-supplied sector/component substrate:

- three abstract component types up to the allowed relabelings;
- sector-supported nonnegative multiplicities;
- typed finite token content;
- componentwise content composition.

These are common inputs and are not counted as advantages for either interface.

## Interface F dependency DAG

`typed sector content`

`-> declare scalar field Q on sector content`

`-> [F1] axis square calibration Q(n,0)=Q(0,n)=n^2`

`-> [F2] local transverse independence Delta_a Delta_b Q=0`

`-> theorem: Q(a,b)=a^2+b^2`

`-> [F3] semantic identification Q = squared native line scale`.

Typed classification:

- scalar object `Q`: N2 readout target/carrier declaration;
- F1: independent scalar calibration condition;
- F2: independent scalar interaction/separability condition;
- sum-of-squares: derived theorem;
- F3: semantic role assignment.

The exact FQ008 source is an integration candidate at `b6ec6eb...`; its theorem content is evaluated independently of that source-integration status.

## Interface K dependency DAG

`typed content (U,tau)`

`-> theorem: R_type=ker(tau)`

`-> theorem: R_type is unique greatest component-preserving equivalence`

`-> [K1] choose component-preserving relation as the scale observation resolution`

`-> [K2] choose finite cardinality of the ordered-pair relation carrier`

`-> theorem: Q_K=sum n_c^2`

`-> theorem: axis square + transverse independence`

`-> [K3] semantic identification Q_K = squared native line scale`.

Typed classification:

- `R_type`: N0-definable derived, therefore not a new primitive assumption;
- relation maximality: theorem;
- K1: semantic/observation-resolution choice for the scale role, even though the relation itself is canonical relative to `tau`;
- K2: N2 readout choice; ordinary finite cardinality is exact once this carrier is selected;
- formula and FQ008 scalar conditions: theorems;
- K3: semantic role assignment.

## Does K genuinely reduce assumptions?

### Mathematical/structural assumptions

Yes, K removes the need to posit a free scalar field and then constrain its values pointwise. The numerical law follows from a relation independently definable before any scale semantics.

This is genuine **ontological compression**: a relational mechanism explains the scalar field rather than merely restating its values.

### Semantic assumptions

Not completely.

R065 proved that the primitive substrate does not uniquely select a scalar. FQ010 further shows that N0 admits finer and coarser observation resolutions as well as multiple scalar valuations of the same component relation.

Therefore K does not eliminate the need for semantic selection. In particular:

- choosing component resolution as the scale-relevant observation is not forced merely by the existence of `tau`;
- choosing relation-pair cardinality among other scalar readouts is not forced by relation canonicity;
- assigning squared-line-scale meaning remains a semantic declaration/calibration.

Consequently, counting “one K formula versus two F axioms” would overstate the compression.

## Comparative assumption table

| Item | F | K |
|---|---|---|
| Component substrate | common | common |
| Free scalar object | declared | not needed before readout |
| Relation object | absent | derived, no new assumption |
| Axis-square law | semantic scalar condition | derived after K2 |
| Transverse independence | semantic scalar condition | derived after K2 |
| Observation resolution for scale | implicit in sector scalar interface | explicit K1 |
| Scalar valuation/readout | implicit in `Q` | explicit K2 = relation cardinality |
| Squared-scale identification | explicit F3 | explicit K3 |
| Relation/provenance information | not encoded by scalar | retained before scalarization |

## Explanatory compression classification

K is stronger than mere notational packaging because:

1. `R_type` exists and is maximal before any scalar is introduced;
2. its cardinality simultaneously yields axis square and transverse independence;
3. the relation retains component provenance that the scalar interface cannot reconstruct;
4. the same mechanism distinguishes occurrence-count and fully-coarse alternatives.

But K does **not** prove that its cardinality is the uniquely correct squared-scale semantics from N0 alone.

The correct budget classification is therefore:

`ONTOLOGICAL_COMPRESSION_WITH_THEOREM_EQUIVALENT_SCALAR_CONTENT_BUT_RESIDUAL_N2_SEMANTIC_SELECTION`.

This is stronger than “mere notational packaging” and weaker than “primitive semantics uniquely reduced to N0”.

## Foundation implication

The assumption comparison does not justify silently deleting the FQ008 semantic/calibration interface. The strongest clean disposition is to use K as the structural refoundation and F-type scalar conditions as an exact characterization/calibration boundary unless and until the squared-scale role of relation cardinality is separately declared.

`PRIMITIVE_AND_SEMANTIC_BUDGET_COMPARED = PASS`.
