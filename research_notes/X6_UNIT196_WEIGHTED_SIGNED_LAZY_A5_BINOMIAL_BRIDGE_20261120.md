# X6 Unit196 — Positive-weight signed-X6 / lazy-A5 / nonlazy-A5 exact bridge

Status: AUTHOR_PROVED / EXACT_PINNED_PYTHON_EXECUTED / UNREVIEWED / NOT_ADMITTED. Task RS-X6-LEGACY-PLANE-RECONCILIATION; publication TP2-B4A441B23DA3159232C2; parent PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Historical author lane chatgpt-research-onhour-enterprise-math-20260923 is provenance, not current owner authorization. Maintenance lane chatgpt-hourly-enterprise-math-20260921 excluded.

Scientific input pin 59538f585d037d09ef687b28715c4bc1a3f9fe03. Frozen comparison fd2bcff10ca6e147348b6c1236027fc0d2877df3. Exact frozen executable experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py, Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176, function endpoint_weight. Positive rational independent sign-axis weights u_i,v_i are allowed by this producer. P000 raw six signed coordinates are chart-relative displacements, not final Cell addresses or new spatial axes.

## New theorem: factorized weighted all-walk path bridge

Take u_i,v_i in positive rationals, i=1,...,6. A native signed-X6 word of length 2n has weight the product of u_i for each +e_i step and v_j for each -e_j step. Let E_{2n}^{u,v}(z) be its total weight among words reaching balanced z in Z^6 (sum z_i=0). Define lazy A5 composite letters (i,j), 1<=i,j<=6, moving e_i-e_j and carrying **the labeled product weight** u_i v_j; i=j are six distinct labeled zero-displacement pairs. Let L_n^{u,v}(z) sum the weights of n-letter lazy words. Let A_n^{u,v}(z) use only i!=j. Define the exact scalar c=sum_i u_i v_i. For every n>=0 and every balanced z,

    E_{2n}^{u,v}(z) = C(2n,n) L_n^{u,v}(z)

    L_n^{u,v}(z) = sum_{k=0}^n C(n,k) c^(n-k) A_k^{u,v}(z)

    A_n^{u,v}(z) = sum_{k=0}^n C(n,k) (-c)^(n-k) E_{2k}^{u,v}(z)/C(2k,k).

Proof: balanced endpoints force exactly n plus and n minus signed native events. Extract their ordered positive labels and ordered negative labels, pair in that order, and retain one of C(2n,n) sign-slot shuffles. Each shuffled preimage has precisely the same product of all individual u_i and v_j, so the first identity holds weight by weight. In the Laurent polynomial ring, define U=sum_i u_i x_i and V=sum_j v_j x_j^{-1}. Lazy pairs have polynomial P=UV=Q+c, with Q=sum_{i!=j}u_i v_j x_i/x_j. Coefficient extraction of P^n and Q^n yields the second identity and the binomial inverse. All computations are rational and exact; n=0 and unreachable endpoints hold with the usual zero coefficient convention. Positive weights make this a weighted BRC count, not signed-amplitude cancellation.

This extends Unit195 (unit weights c=6). For unequal weights, substituting 6 for c is false. A5 letters are composite two-event readouts, not P000 native primitive directions. Endpoint mass identities are observer-level; for future predicates depending on interleaving, pair label or time order, retain the ordered native source and the sign-slot pattern. The theorem applies to factorized pair weights u_i v_j, not an arbitrary nonfactorizable A5 edge-weight matrix.

## Executed tests and concrete certificate

The complete frozen source was reconstructed byte-for-byte and checked against Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176 (SHA-256 6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4). The original endpoint_weight was imported and called. Independent exact Fraction DP enumerated 36 labeled lazy and 30 nonlazy root letters. A third native signed-axis DP independently checked a selected subset.

Three source-independent weight profiles: distinct positive integers u=(2,3,5,7,11,13), v=(17,19,23,29,31,37), c=1231 with n=0..4; positive rational profile u=(1/2,2/3,3/4,4/5,5/6,6/7), v=(7/6,6/5,5/4,4/3,3/2,2), c=3557/560 with n=0..3; unit weights c=6 with n=0..3. All balanced endpoints of each n were examined: 9,003 endpoint-length comparisons against both identities; 1,887 of these also have independently enumerated native signed DP; zero disagreements. The complete result JSON has SHA-256 42e4db2be86eae56cd8bd39aef425421fd45cbd877f5acb41ee276131bfc8bc0. Python normal, -O and -OO runs produced the same certificate bytes. No original R063 native six-file benchmark was rerun.

Exact witness for integer weights at z=0 and n=2: E_4=15,745,446; L_2=2,624,241; A_2=1,108,880; c=1231. Indeed E_4=6 L_2 and A_2=L_2 - 2c L_1 + c² L_0, where L_1(0)=c. For unit weights the witness is 396, 66, 30. The weight-dependent zero-pair mass is the obstruction to assuming the unweighted six-color correction universally.

## Actual frozen consumer scope and original error provenance

Directly inspected frozen check_signed_brc.py (blob eadc2640e190165020a60a707ac5a14c497036a0), check_x6_signed.py (blob 275f327b603a9b07f8f6c0948347e75028d3a38a), and tests/test_p022_geodesic_multiplicity.py (blob ef3da1a789186867c538b604da1b642bf6039591). The first directly tests signed_brc endpoint_multiplicity/endpoint_weight; the second imports x6_signed positive/relative observer; the last invokes P022 shortest A_p graph functions. In **these exact frozen consumers**, no direct cross-module call mixing frozen P022 shortest A5 and signed-X6 all-walk count is present. This is a bounded typed-source finding, not an all-repository negative assertion.

LP011 alleged original signed-argmax error and LP019 alleged invalid positive-N-BRC subtraction still lack a verified historical offending commit:path:line; the new mathematical bridge is not evidence that such a production call existed. The typed weight bridge should be applied only after locating a real consumer. Unit195 completed results, earlier native R063 17/17 and 512/512 evidence remain reused.

## Control / continuation

Author evidence is UNREVIEWED / NOT_ADMITTED, not a Result, Foundation update or Native semantic PROGRESS. Last previously authenticated Native author front is Unit174; the pending own-lane semantic linkage is Units175–196 and older Units149–152, conditional on current same-lane ownership. Original read-only request onhour-20261120-2055-x6-unit195-postscience-current-cont-read-v1 has been independently reconciled: SUCCEEDED, error=null; it must not be resent. The historical failed prepare onhour-20261120-1524-x6-own-unit187-native-continuation-prepare-v1 remains FAILED/NATIVE_INPUT_SCOPE_METADATA_BUDGET_EXCEEDED, not replayed.

Next exact action: locate a frozen real state- or time-dependent consumer of endpoint_weight or A5 counts, test whether a factorized pair mass and interleaving provenance suffice for its future operation, and identify an actual original LP011/LP019 offending commit:path:line if it exists. For native association, first authenticate the same Research lane's live winning claim/run and current operation contract; Source recovery metadata alone is not authority.
