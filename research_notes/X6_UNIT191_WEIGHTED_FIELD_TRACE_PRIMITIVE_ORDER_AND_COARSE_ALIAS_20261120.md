# X6 Unit191 - exact primitive step recovery from time-indexed frozen A3 relation fields

Date: 2026-11-20. Parent PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905; exact published Task RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. Author Research lane: chatgpt-research-onhour-enterprise-math-20260923, not maintenance. Status: AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED. Native semantic PROGRESS NOT SUBMITTED.

## Frozen source and scientific boundary

The six signed primitive axis steps are from definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md at awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03. The actual historical A3 producer is src/enterprise_math/weighted_relation_field.py at @fd2bcff10ca6e147348b6c1236027fc0d2877df3. Its functions weighted_relation_field and coarsen_weighted_relation_field implement Z_ij=m_j*z_i-m_i*z_j and W_AB=sum_{i in A,j in B}Z_ij. Its actual test consumer is tests/test_weighted_relation_field.py at the same frozen commit. The signed X6 endpoint z is an explicitly typed integer adapter into A3 totals, NOT a claim of an existing native production wire between these source domains.

Unit190 already reconstructed the fine Z_t from the coarse W_t and fixed internal spanning-forest edge readings E_t at each observation time. Unit183 previously recovered signed steps from a full relative min-zero trajectory; the present result concerns a distinct genuine weighted producer, arbitrary positive unequal capacities, and a sharp classification of coarsened-trace aliases. This work does not rediscover or execute the original R063 benchmark and does not claim to have found an actual ordered X6 production consumer.

## Exact theorem 1: fine relation-field time trace recovers every primitive event

Let m=(m_1,...,m_6) be any positive integer capacity vector, z_0 any signed integer endpoint, z_{t+1}=z_t+epsilon_t*e_{i_t}, where epsilon_t in {+1,-1}. Record the entire fine weighted field Z_t=Phi_m(z_t) after every event, including time zero.

For any integer v, Phi_m(v)=0 exactly when v belongs to Q*m (the positive-capacity gauge line). The difference of two distinct signed primitive unit vectors has at most two nonzero coordinates, so it cannot be a nonzero multiple of m, which has all six coordinates nonzero. Thus the 12 primitive increments Phi_m(+/-e_i) are pairwise distinct. Each delta Z_t=Z_{t+1}-Z_t uniquely determines the signed direction and the event index. An initial absolute z_0 or equivalent gauge repair is still needed for absolute spatial positions, but NOT for the ordered primitive event word.

Consequently, when each time slice supplies (W_t, E_t) of Unit190's legitimate spanning-forest repair interface, its reconstructed Z_t sequence uniquely determines the entire signed primitive word. This is exact at every finite horizon without a positivity approximation or an unproved interpolation.

## Exact theorem 2: complete classification of the one-step coarse alias

Let P=(A_1,...,A_k) partition the six named axes and M_A=sum_{i in A}m_i>0. For a signed event epsilon*e_i in group A, the genuine frozen coarse producer gives

    delta W_BC = epsilon * (1_{B=A} M_C - 1_{C=A} M_B).

For k>=3, two signed primitive events have the same coarse increment iff they have the same group A and the same sign. For k=2 with M_1!=M_2 the same condition holds. For k=2 with M_1=M_2 there are exactly two additional group-sign alias families: (+,A_1) is indistinguishable from (-,A_2), and (-,A_1) from (+,A_2). For k=1 all 12 signed events give the zero coarse increment.

Proof: for k>=3, compare the coordinate involving one candidate group and a third, distinct group: a step at the first group yields +/-M_C while a step at the second yields zero. For k=2, the sole upper-triangular scalar is +M_2,-M_2,-M_1,+M_1 for (+A_1,-A_1,+A_2,-A_2) respectively; equality is precisely the stated balanced exception. The k=1 field has no off-diagonal entry. Same-group axis labels are always forgotten by coarse increments.

At a single time step, without a terminal-state side channel, an exact coarse-increment decoder therefore requires a side label among |A| axes in the ordinary group-sign-resolved case, 6 possibilities for a balanced two-group increment, and 12 possibilities in the one-group case. This is an immediate one-step fiber-cardinality bound, NOT a universal compressed bit-rate bound for an entire word with terminal constraints.

## Sharp two-step obstruction even after final forest repair

Let m=(1,1,1,1,1,1). Partition A_1={1,2}, remaining axes singleton. The two signed-native words (+e_1,+e_2) and (+e_2,+e_1) produce identical coarse fields at t=0,1,2 and exactly the same final fine field Phi_m(e_1+e_2), although their first fine fields and ordered Path-formal histories differ. Their common terminal shortest-path BRC count is 2. Thus preserving the coarse trace and only repairing the terminal fine field does not in general reconstruct order.

For the exceptional balanced two-block partition {1,2,3}|{4,5,6}, the words (+e_1,-e_4) and (-e_4,+e_1) also have identical coarse traces and terminal fine field: each first event contributes +3 to the sole coarse scalar. This is an independent sign/group alias beyond within-block axis ambiguity.

For an order-sensitive future operation or provenance question, retain the full repaired time trace, or explicit event labels, or another proved context-specific sufficient carrier. Forest repair only at the final endpoint is insufficient. A source-specific downstream consumer and the historic LP011/LP019 offending commit:path:line remain unresolved.

## Executed exact finite check (not the R063 native benchmark)

The independent JavaScript integer checker computes signed primitive field increments by both the actual frozen producer sum expression and the independent grouped-capacity formula. It enumerated all Bell(6)=203 partitions and 3 positive capacity vectors, for 609 partition-capacity cases. It checked 7,308 direct producer-increment identities, 87,696 ordered primitive-pair alias classifications, 87,696 full-field injectivity pair comparisons, and 87,696 two-event words. Among the last it found 8,237 additional same-coarse-trace/same-fine-terminal word instances beyond the first observed representative per output key, with zero mathematical inconsistencies. The test enumerated 10 balanced two-group cases and 606 cases exhibiting at least one order alias. These counts are finite diagnostics, not an infinite-horizon theorem.

Actual executed checker: research_checks/X6_UNIT191_WEIGHTED_FIELD_TRACE_CLASSIFIER_CHECK_20261120.js at commit 7b362a34d180e5b465368820293729049dff3e3f. Exact results: research_checks/X6_UNIT191_WEIGHTED_FIELD_TRACE_CLASSIFIER_RESULTS_20261120.json at commit d6deb5a98d1088ce1c5d31388641b2f31d665752. These source-equivalent checks do not import the historical production module; source equations were read independently. Unit190's 203-partition forest inverse and R063's 17/17 original six-file acceptance and 512/512 regression were consumed, not rerun.

## Unfinished parent obligations

Native authenticated last authored Source frontiers had been verified through Unit174. Author Units175-191 and older Units149-152 require fresh same-lane protected writer authorization and semantic linkage; mere recovery pointers are not authority. Previous takeover_prepare onhour-20261120-1524-x6-own-unit187-native-continuation-prepare-v1 conclusively FAILED/NATIVE_INPUT_SCOPE_METADATA_BUDGET_EXCEEDED: no replay. LP011 native signed argmax and LP019 positive-N-BRC subtraction suspected historical offending source calls still lack exact commit:path:line and a typed consumer. Independent Driver review is UNREVIEWED/NOT_ADMITTED. The next discriminating scientific step is to read a genuine frozen order-sensitive X6 consumer and show the precise typed interface, or find the actual LP011/LP019 offending source with immutable line evidence. Do not convert these unresolved obligations into proof of failure or task completion.
