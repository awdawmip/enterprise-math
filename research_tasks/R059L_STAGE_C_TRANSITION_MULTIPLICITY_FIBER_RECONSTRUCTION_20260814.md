# RS-R059L — STAGE C TRANSITION-MULTIPLICITY FIBER RECONSTRUCTION

Task-ID: `RS-R059L-STAGE-C-TRANSITION-MULTIPLICITY-FIBER-RECONSTRUCTION`
Generation: `R059L`
Status: `DRIVER_APPROVED_TASKBOOK`
Identity-policy: `AUTO_RESOLVE_OR_ALLOCATE`
Identity-lane: `R059L`
Date: `2026-08-14`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`

## 0. Frozen parent

This Stage C starts only from the accepted R059L native packet/path foundation and the frozen Stage-A/B results.

Frozen Stage-A owner head:

`4d196b916c815f665ea725f40ee5fb48ef76b10e`

Frozen Stage-B owner head:

`aee265e65b9b1471b066cac8d43f8d929bdd67e7`

Stage-0, Stage-A, and Stage-B artifacts are immutable.

Stage B established, among other exact facts:

- the full raw ordered path history `H0` deterministically yields directed transition multiplicity `T=H1`;
- `T` does not reconstruct `H0` in general;
- readout equality never changes native raw-history equality;
- geometry, metric, line, length, path cancellation, and physical conservation interpretations remain withheld.

This Stage C studies the exact **fiber of the readout** `H0 -> T`.

It does not introduce geometry.

---

# 1. Native equality remains raw-history equality

A native path remains an ordered packet history

```text
gamma = (x_0, x_1, ..., x_n)
```

with every successive pair satisfying declared adjacency.

Native equality remains exact equality of the whole ordered history.

For a finite nonnegative-integer directed transition table `T`, and declared endpoints `s,t`, define the Stage-C diagnostic fiber

```text
F(T;s,t)
  = { gamma : x_0=s, x_n=t, T_gamma = T }.
```

`F(T;s,t)` is a set of native paths satisfying a common N2 readout constraint.

It is **not** a quotient object at N0.

Do not replace native path equality by equality of `T`.

---

# 2. Transition-table data

For finite-support `T(x,y) in N`, define only exact integer summaries:

```text
OUT_T(x) = sum_y T(x,y)
IN_T(x)  = sum_y T(y,x)
N_T      = sum_{x,y} T(x,y)
```

and the active packet set

```text
ACTIVE(T) = {x : OUT_T(x)+IN_T(x) > 0}.
```

Define the relational support of `T` using only packet identities and positive transition multiplicities.

A symmetrized support relation may be used:

```text
x ~_T y  iff  T(x,y)+T(y,x) > 0.
```

This is a relational connectivity object only.

Do not call it geometric connectedness, distance, length, or edge geometry.

---

# 3. Stage-C primary problem: realizability

Determine exact necessary and sufficient conditions for

```text
F(T;s,t) != empty.
```

The target condition family is:

## 3.1 Zero-transition case

If `N_T=0`, determine exactly when the unique zero-transition path `(s)` realizes `(T;s,t)`.

Expected candidate:

```text
T = 0
and
s=t.
```

Do not assume; prove.

## 3.2 Positive-transition balance

For `N_T>0`, prove necessity of

```text
OUT_T(x)-IN_T(x)
  = 1[x=s] - 1[x=t]
```

for every packet `x`.

This must be derived from Stage-A endpoint incidence and not given a physical interpretation.

## 3.3 Relational support condition

Determine the weakest exact connectivity/support condition required in addition to the integer balance law.

Candidate target:

all packets in `ACTIVE(T)` lie in one connected component of the symmetrized positive-transition support relation, with the endpoint cases typed correctly.

Do not import graph distance, geometry, or a continuum notion of connectivity.

## 3.4 Sufficiency

If the exact balance + support conditions are sufficient, provide a constructive finite proof producing one raw history realizing `T`.

If the candidate conditions require correction, freeze the corrected weakest theorem and provide exact counterexamples to any failed stronger/weaker statement.

Classical names such as Euler trail/circuit may be mentioned only after the native theorem is established, as external analogy terminology. They are not premises.

---

# 4. Collapse multiplicity

Define the diagnostic integer

```text
MU(T;s,t) = |F(T;s,t)|
```

when the fiber is finite.

This is a Stage-C N2 diagnostic readout of readout nonidentifiability.

It is not entropy, probability, distance, or geometric multiplicity.

Prove:

```text
MU(T;s,t) is finite
```

for finite-support `T` with finite `N_T`.

Use the weakest exact combinatorial bound needed; no asymptotic fitting is required.

Classify:

```text
MU=0  unrealizable table/endpoints
MU=1  history uniquely reconstructed from T plus endpoints
MU>1  information-collapse ambiguity
```

These are diagnostic classes only.

---

# 5. Preferred exact ambiguity witness

Revisit the frozen Stage-B witness:

```text
gamma = A-B-A-C-A
eta   = A-C-A-B-A
```

on declared symmetric adjacencies `{A,B}` and `{A,C}`.

The shared table is:

```text
T(A,B)=1
T(B,A)=1
T(A,C)=1
T(C,A)=1
```

all other multiplicities zero, with `s=t=A`.

Stage C must determine the **exact fiber cardinality** for this `(T;A,A)`.

High-priority target:

```text
MU(T;A,A)=2
```

with an exhaustive proof that the only raw histories are exactly `gamma` and `eta`.

Do not stop at `MU>=2` if exact enumeration is feasible.

---

# 6. Reversal acts on fibers

Let

```text
T^T(x,y)=T(y,x).
```

Prove that raw-history reversal induces a bijection

```text
rev : F(T;s,t) <-> F(T^T;t,s).
```

Therefore, if proved:

```text
MU(T;s,t)=MU(T^T;t,s).
```

This is an exact combinatorial statement only.

Do not interpret transpose/reversal as spatial opposition, displacement reversal, or vector negation.

---

# 7. Packet relabeling covariance

For any bijective packet relabeling that preserves the declared adjacency relation on the relevant support, prove the corresponding equivariance of:

- raw histories;
- transition tables;
- fibers;
- `MU`.

This is a relational invariance test, not Euclidean symmetry.

---

# 8. Optional minimal-ambiguity diagnostic

The bare Stage-0 adjacency reflexivity status is `UNSPECIFIED_STAGE0`.

Therefore do not silently assume self-adjacency is forbidden.

Optionally determine the smallest transition count `N_T` for which `MU>1` under separately declared cases:

1. `ADJACENCY_IRREFLEXIVE`;
2. `SELF_ADJACENCY_ALLOWED`.

If done, keep the two cases separate and exact.

Do not modify Stage-0 adjacency semantics to make the answer cleaner.

This lane is diagnostic, not required for Stage-C success.

---

# 9. Composition of fibers — limited exact lane

For realizable tables

```text
T1 with endpoints (s,m)
T2 with endpoints (m,t),
```

concatenation gives

```text
F(T1;s,m) x F(T2;m,t)
  -> F(T1+T2;s,t).
```

Determine exactly whether this map is injective under frozen raw-history semantics.

If injective, prove it using the frozen split transition count

```text
N_{T1}=sum T1.
```

Do **not** assume surjectivity.

If a simple exact counterexample shows that `F(T1+T2)` contains histories not arising from this fixed split, record it.

Do not derive probability/entropy/product formulas in this stage.

---

# 10. C6 firewall remains frozen

Do not repair or extend Stage-B C6 passage composition in this stage.

Freeze:

```text
C6_PASSAGE_COMPOSITION_NOT_YET_WELL_TYPED
```

unless Driver separately authorizes a channel-event semantics task.

No ordered per-transition channel annotation may be invented merely to close a formula.

---

# 11. Forbidden work

Stage C forbids:

- line;
- straightness;
- distance;
- length;
- shortest path;
- geodesic;
- path ranking;
- metric or `Q(a,b)`;
- angle / slope / curvature / direction vector;
- edge / boundary / perimeter / chord;
- area / volume;
- Euclidean/Voronoi geometry;
- physical flux/divergence/current/conservation interpretation;
- raw-history cancellation;
- quotienting a path by reversal or loop deletion;
- promoting `T`-equality or fiber membership to native path equality;
- probability/entropy/statistical fitting;
- R057/R058S fitted geometry.

---

# 12. Required Stage-C artifacts

Freeze at least:

1. `R059L_TRANSITION_TABLE_REALIZABILITY_PROTOCOL.json`
2. `R059L_TRANSITION_TABLE_SUPPORT_CONDITION.json`
3. `R059L_TRANSITION_FIBER_DEFINITION.json`
4. `R059L_COLLAPSE_MULTIPLICITY_MU.json`
5. `R059L_TRANSITION_FIBER_REVERSAL_BIJECTION.json`
6. `R059L_TRANSITION_FIBER_RELABELING_EQUIVARIANCE.json`
7. `R059L_PREFERRED_FIBER_CARDINALITY_EXACT.json`
8. `R059L_FIBER_COMPOSITION_MAP.json`
9. `R059L_STAGE_C_THEOREM_LEDGER.json`
10. `R059L_STAGE_C_REGRESSION_RESULTS.json`
11. `R059L_STAGE_C_CHECKER_OUTPUT.json`
12. `R059L_STAGE_C_TRANSITION_FIBER_CHECKPOINT.json`

Optional:

- `R059L_MINIMAL_AMBIGUITY_BY_REFLEXIVITY.json`

---

# 13. Required checker gates

The deterministic Stage-C checker must independently verify at least:

- Stage-B exact parent head;
- Stage-0/A/B frozen write-set immutability;
- every frozen realizability example reconstructs exactly its claimed `T`;
- every unrealizable negative example is rejected for the claimed structural reason;
- endpoint balance law;
- positive-support condition on all registry cases;
- preferred witness has exact claimed `MU`;
- reversal maps every enumerated fiber bijectively to the transposed endpoint-swapped fiber;
- relabeling preserves fiber cardinality on deterministic test cases;
- fiber membership never changes native path equality;
- C6 composition remains unmodified/not-yet-well-typed;
- no forbidden geometry/metric/cancellation/physical semantics entered.

Hard negative self-tests must reject at least:

- `T_EQUAL_IMPLIES_NATIVE_PATH_EQUAL`;
- `MU_AS_NATIVE_PATH_WEIGHT`;
- `PATH_CANCELLATION_QUOTIENT`;
- `PATH_COUNT_AS_LENGTH`;
- geometric support/connectivity interpretation;
- physical flow/divergence interpretation;
- untyped C6 composition repair;
- R057/R058S geometry leakage.

---

# 14. Completion gate

Stage C succeeds if it establishes a rigorous native/readout separation and at minimum resolves:

1. exact realizability conditions for finite `T` with endpoints, or the strongest corrected theorem supported by exact counterexamples;
2. exact definition and finiteness of `MU(T;s,t)`;
3. exact preferred fiber cardinality;
4. reversal fiber bijection;
5. no promotion of readout equivalence to native path equality.

Freeze the Stage-C checkpoint and stop for Driver review.

Do not enter a Stage D.
