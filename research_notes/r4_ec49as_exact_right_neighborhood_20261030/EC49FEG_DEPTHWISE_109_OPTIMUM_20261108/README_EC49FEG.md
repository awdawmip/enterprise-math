# EC49FEG — Exact 109-edge optimum for the 108 late-three-key family

**Date:** 2026-11-08. **Status:** author-side finite combinatorial theorem and exact computation, pending independent Driver admission. **Frozen science pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Statement and precise scope

Use the original signed native six-axis path grammar and nine-state DFA/observational-signature requirements from EC49FED–EC49FEF. Window path quotas for H2–H9 are (4,2,2,4,2,4,4,2). Require final signed native displacement +2E1 for every word, signature coverage of 18,20,33,40 (rank-9 test), and at most five full positive BRC keys.

Restrict to the **108** late-three-key choices of EC49FEB: A belongs to {(3,2,1),(4,1,1)}, B to the six listed in the attached Python, and C to the nine listed there, used at H4, H5–H6 and H7–H9, respectively. H5 may **also mix B and C**, preserving signature/group constraints. H2–H3 may choose any of the **28** early legal arrangements previously enumerated by EC49FED (at most two additional BRC keys, all native/observer requirements). Other global five-key allocations are outside this theorem.

**Theorem (exact global optimum within that finite family).** Across all 108×28 configurations and all allowed 18 late paths (including all H5 mixtures), the minimum union of nonempty signed native-X6 path-prefix edges is precisely **109**.

The known 94-edge mother-problem witness remains unaffected; the original target ≤93 remains open.

## Proof — depthwise set-cover relaxation

1. Exhaustive six-operator enumeration at horizons 2 and 3, using exact signed-native paths and 9-state signatures, yields exactly 28 eligible early (H2,H3) arrangements. Their true native-prefix costs have minimum **35**. Let U be the union of every native-prefix node from all 28 arrangements. Direct enumeration gives |U|=70. For each actual early set E, E⊆U.
2. For a chosen late triple (A,B,C) and each of the 18 late horizon/signature groups g, compute the exact full set P_g of legal native-path words, using the frozen operator counts. For H5 include both B and C candidates. No continuous/numerical approximation occurs.
3. At each positive native depth d, let G_d={g : min_{p∈P_g}|p|≥d}. This retains only groups whose **every alternative reaches depth d**. Removing a group with a shorter alternative is a valid relaxation.
4. For each g∈G_d, each candidate depth-d prefix covers that group. A prefix p∈U is declared **free**, although a real early arrangement may contain only a subset; this can only lower the needed cost. Delete groups covered by free nodes. The remaining minimum number of distinct nonfree prefixes sufficient to cover the remaining groups is an exact finite **unit-cost set-cover number** m_d, solved by recursive integer bitmask dynamic programming. Consequently every legal complete system W satisfies

   **C_native(W) ≥ 35 + Σ_{d≥1} m_d(A,B,C).**

   Proof: each selected late word from a retained group has a depth-d prefix, so its selected prefix set must cover all retained groups; separately, different depths count disjoint native-prefix nodes. Replacing true E by the larger free U and replacing the exact candidate allocation by a separate optimum at each depth only relaxes constraints. Hence each m_d is a valid lower bound on new depth-d nodes, while 35 bounds early nodes.
5. The previously verified involution I=(c d)(f g) preserves signed native-prefix costs and signature coverage, transforms BRC keys via K(x,y,z)=(y+2z,x−2z,z), interchanges the two A choices and permutes B,C families; it also maps the 28 early arrangements to themselves. It suffices to compute all **54** configurations with A=(3,2,1).
6. Exact bitmask enumeration produces 54 lower bounds, all ≥109 (range **109–166**); mirrored choices inherit their bounds. The attached explicit 24-word witness has **109** distinct nonempty native prefixes, exactly **five** full BRC keys, signed endpoint +2E1 for every path, all eight window quotas and rank-9 coverage. This supplies the upper bound, completing the scoped equality.

The witness BRC keys are (2,1,1),(3,1,1),(3,2,1),(4,3,1),(6,4,1).

## Reproduction and checks

Run `python EC49FEG_CERTIFY.py > EC49FEG_CERTIFIED_OUTPUT.json` (Python standard library only). The code contains the original six signed-native operations, nine-state automaton, all 28 early arrangements, exact 54×depth set-cover computations and the full explicit witness. The JSON output retains all 54 configurations' depth-cover counts and integer lower bounds; `EC49FEG_LOWER_BOUNDS.json` provides the 54 concise configuration results.

A separately executed SciPy/HiGHS 0–1 set-cover implementation recalculated **1140** depth subproblems, all 54 lower bounds and the explicit 109-edge witness. Its independently obtained result is preserved in `EC49FEG_INDEPENDENT_AUDIT.json`. The bitmask proof kernel in the stand-alone source is exact and does not rely on floating-point solver status.

## Next research unit

The studied 108×28 late-three-key family (including H5 B/C mixing) has an exact 109-edge cost floor. Next examine the **actual late key-allocation structure of the already recorded 94-edge mother witness**, then search other global five-key arrangements and early/late key sharing outside this restricted family; use the depthwise lower bound to screen candidates before joint optimization. The 109 bound is **not** a bound on the unrestricted mother problem.

**Control:** GitHub author `awdawmip` has repository write permission. Native control reported `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE` with operation_sent=false; active Owner, CLAIM, and independent Driver admission are unconfirmed.
