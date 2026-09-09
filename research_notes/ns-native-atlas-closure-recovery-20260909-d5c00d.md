# Recovered atlas-closure and finite-moment frontier (distinct event12)

Event: `NS-NATIVE-ATLAS-CLOSURE-20260909-D5C00D-12`  
Researcher: `EM-DIRECT-D5C00D`; activity `RA-D5C00DF7D77F4AA2ACE0`.  
Status: **RECOVERED_PRIOR_EXECUTED_RESULT_CONDENSED_SOURCE_NOT_REEXECUTED**.

This event is NOT `NS-NATIVE-INCIDENCE-FAMILY-20260909-D5C00D-12`, which already has a separate source and activity entry. The full event ID, not the suffix12, is its identity. The MICRO-CLOSURE event11 has already been recovered remotely and is not copied again.

The supplied original atlas package was inspected and its 14 extracted manifest-listed text/code/JSON files passed exact SHA256 and Git-blob SHA1 checks. Original detailed note SHA256: `1b0936b31d2cc8676b8c085a2238e95b1b402d2bc3d34f7e96e84b60c605abf3`; original checker SHA256: `0418849626be43c8929c5db56c1b2626be069e27b92e7fcd4d73a3c41804565b`; original result SHA256: `89ec43efc4acb403f9d95ae8432868ff3a4734bfc7af0fa81dadf5c95093b4fe`. The original executable/dependencies remain in the downloadable recovery bundle, not claimed re-executed by this recovery entry.

## Exact coordinate and signed-relation results

For z in Z6, the fixed FCC readout is

    Bz=(z1+z2+z3+z4, z1-z2+z5+z6, z3-z4+z5-z6).

Its image is L={(x,y,w) in Z3:x+y+w even}. With h=(z4,z5,z6), the map z -> (Bz,h) is a bijection onto L x Z3. The inverse is

    z1=(x+y-w)/2-h4-h6;
    z2=(x-y-w)/2-h4+h5;
    z3=w+h4-h5+h6;
    (z4,z5,z6)=(h4,h5,h6).

Substitution proves both directions, including integrality. At least three additional additive integer coordinates are needed for an injective additive supplement, by rank of the resulting integer matrix. This is not an arbitrary-encoding lower bound or three global numbers repairing a particle field.

The signed path vectors

    rA=e1-e3-e6, rB=e1-e4-e5,
    rC=e2-e3+e5, rD=e2-e4+e6

are individually in ker B but nonzero natively. Component elimination gives

    qA*rA+qB*rB+qC*rC+qD*rD=0
    iff (qA,qB,qC,qD)=lambda*(1,-1,-1,1).

For example, -qB-qD=0 in component4, -qA+qD=0 in component6, and qA+qB=0 in component1 determine this form; substitution checks the others. The first three r's are an integer kernel basis, as their coefficients can be recovered integrally from (z4,z5,z6). A,D,-B,-C is a twelve-primitive-step return. Twelve is minimal only for a nonzero net signed relation among these four types, not all closed paths. Native return is not equated with primitive force balance.

## No marginal or fixed finite-moment closure for the frozen count rule

The rule is X6-DENSITY-PORT-1 from source `6f119ea99021f83141321a5241dcb33b70f5af44`, not a new fitted rule. It moves a neutral pair in an eligible triple only toward a unique maximizing unused-axis neighbor-count score, then streams all channels once.

Put the common core {+e1,+e2,-e2} at0. Compare one +e1 marker at e3 with one at e3+4rA. Their entire B-position/channel counts are identical. Only the first marker is a native neighbor of the core. The first system changes the core pair axis to3, the second does not; markers themselves are ineligible. Their next B-position/channel count difference is exactly4. Hence this marginal cannot determine its own next update on all finite states.

For each fixed p>=0 use markers at e3+4a*rA, 0<=a<2^(p+1). Put even binary-digit-parity a's in one system, odd-parity a's in the other. Both retain the common core, so each has3+2^p particles, and every native slot has occupancy at most1. All markers have the same B readout and hidden coordinates affine in a. The alternating sum of every polynomial of degree<=p is zero, by the product of p+1 finite-difference operators with steps1,2,4,...,2^p. Thus all hidden-coordinate moments of total degree<=p agree at every B-position and channel. Only a=0 is adjacent to the core, so the next B marginal difference remains4.

Consequently no single fixed finite moment order closes this update on the entire family of finite particle states with growing support. This is not impossibility of reconstruction for a known fixed support/population or of an approximate/statistical closure under additional assumptions.

Retaining the full joint coordinate (r,h) is an exact conjugacy: if Psi is the bijection above, define the coordinate-transformed update by applying the unchanged rule at the exact inverse positions. Then Ftilde*Psi_*=Psi_*F, and induction gives all integer iterates. Summing out h yields an exact marginal balance only with the ACTUAL event rates; the counterexample shows those rates do not follow from the collapsed data.

## Prior execution and limits

The original recorded checks included15,625 coordinate inversions,31,104 ordered twelve-step paths,728 nonzero quotient directions, moment orders0 through8, and30 finite input fields over120 steps. Those are prior executions, not rerun counts for the current recovery. No primitive-force legality, viscosity, physical f=0 or NS result, Lean verification, independent review, or Foundation admission is asserted.
