# X6 coherent serial phase observations: sharp multi-stage depth-alias criterion

Status: DRIVER_MATHEMATICAL_AUDIT / UNIVERSAL EXACT PROOF IN DECLARED CANDIDATE MODEL / NOT_NATIVE_RESULT_ADMISSION
Date: 2026-11-12 (+08)
Line: signed X6 native Cell, phase registration, ordered-positive microstep observation and BRC fibers
Parent scientific questions: RS-X6-NATIVE-TIME-DYNAMICS; RS-X6-NATIVE-ROTATION-DYNAMICS (historical Source tasks; no new CLAIM asserted)

## Contribution, provenance and question

This result extends the already saved Driver theorem in research_notes/driver/2026-11-12_x6_unregistered_positive_microsteps_sharp_depth_alias_threshold.md. That theorem treats phase readouts with independently chosen positive-word displacements applied to the SAME initial hidden depth. Here the process is serial: each subsequent registered signed rotation acts on the ACTUAL preceding state after its unknown positive word. Every intermediate min-zero readout is retained. The question is exactly when these observations recover the common initial depth and EVERY segment's positive-axis occurrence vector.

The underlying native signed Cell torsor, primitive axis steps and path/branch provenance come from definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md. The distinct time coordinate and Heartbeat interpretation come from definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json. The common-diagonal quotient is a declared observer. The dynamics below are an explicit candidate model, not a claim that every Heartbeat force/phase law permits these trajectories. Preserve the initial Source authors, native six-dimensional spatial meaning and P000 triadic-closure conditions. This Driver deduction is not an independent reviewer pass over its own preceding note.

## 1. Serial model and exact theorem

Fix n >= 2, D=(1,...,1) in Z^n, and q(z)=z-(min_i z_i)D. Fix a known initial q-chart r and an unrestricted integer depth h. Set z_0=r+hD. For stages i=1,...,m (m>=1), fix a known signed coordinate permutation g_i whose signed vector epsilon_i=g_i D has exactly k_i negative entries (0<=k_i<=n). Choose an unknown positive-axis occurrence vector b_i in B_{M_i}={b in Z_{\ge0}^n: sum b_j=M_i}, for fixed registered integer M_i>=0, and update

    z_i = g_i z_{i-1} + b_i,       y_i=q(z_i).

The observer receives the entire registered sequence (y_1,...,y_m). Ordered word identity, branch choices and source-level force state are additional data not claimed to be recovered by observing occurrence vectors alone.

Write

    s_i=(n-2k_i)/n,
    a_i=2k_i(n-k_i)/n,
    u_0=1,  u_i=prod_{j=1}^i s_j.

Let den(x) be the positive denominator of rational x in lowest terms, with den(0)=1. Define

    L=lcm_{1<=i<=m} den( (2k_i/n)*u_{i-1} ),
    T_i=L*a_i*|u_{i-1}|.

Each T_i is a NONNEGATIVE INTEGER by the recurrence and the definition of L.

**Sharp serial-observation theorem.** The map

    (h,b_1,...,b_m) |-> (y_1,...,y_m)

is injective for all initial r and all h in Z if and only if there exists at least one i with M_i<T_i. If M_i>=T_i for EVERY i, two distinct complete histories exist and agree at EVERY intermediate observed min-zero endpoint. Their smallest nonzero initial depth gap is precisely L. The criterion and exact threshold box depend only on n, the signed-permutation sign counts k_i, and the registered lengths M_i, not on r or the unsigned permutation parts of g_i.

If the starting depth is restricted to a nonempty H subset Z, replace the threshold-box assertion by: an ambiguity exists exactly when there is some nonzero d in H-H satisfying, for EVERY i,

    (2k_i/n)*u_{i-1}*d is integral,
    M_i >= a_i*|u_{i-1}*d|.

Equivalently, d must be a nonzero multiple of L and satisfy the length bounds. This also covers a stage k_i=n/2 where the post-stage difference coalesces to zero.

### Proof (necessity)

Suppose two histories agree at all observations. By q-fiber equality, their raw states obey z_i-z'_i=d_i D for some integers d_i, with d_0=h-h'. Since g_i D=epsilon_i, the two update equations imply

    d_{i-1} epsilon_i + (b_i-b'_i) = d_i D.       (1)

Summing the n components and using sum b_i=sum b'_i=M_i gives

    d_i=s_i d_{i-1}; hence d_{i-1}=u_{i-1} d_0.  (2)

Equation (1) then imposes the unique difference vector

    b_i-b'_i=d_{i-1}(s_i D-epsilon_i).            (3)

At each of the k_i negative-sign positions the difference is 2(n-k_i)d_{i-1}/n; at each of the n-k_i positive-sign positions it is -2k_i d_{i-1}/n. For integral d_{i-1}, (3) has integer entries exactly when (2k_i/n)d_{i-1} is an integer. It has a positive and negative part of equal total mass a_i|d_{i-1}|. Thus two nonnegative vectors with the same sum M_i can realize (3) exactly when M_i >= a_i|d_{i-1}|. The integer condition at all stages is equivalent to d_0 being a multiple of L (inductively (2) then has integral d_i).

For a nonzero gap d_0, necessarily |d_0|>=L, so all its length requirements are at least T_i. If at least one stage length lies below T_i, no nonzero d_0 is possible. With d_0=0, (2)-(3) force b_i=b'_i at every stage. Therefore the entire parameter sequence is unique.

### Proof (sufficiency and sharpness)

Suppose all M_i>=T_i. Take d_0=L and set d_{i-1}=L u_{i-1}. At each stage the vector w_i=d_{i-1}(s_i D-epsilon_i) is integral, sums to zero and has positive and negative parts of equal size T_i. Choose any common v_i>=0 with sum M_i-T_i, and set

    b_i=(w_i)_+ + v_i,   b'_i=(w_i)_- + v_i.

Then b_i,b'_i are admissible at the given exact length and satisfy (1), with d_i=s_i d_{i-1}. Start from z_0=r+LD and z'_0=r; induction gives identical y_i at every stage. The two histories differ at initial depth by L, the smallest allowed gap. For arbitrary H, the same construction works iff an admissible nonzero d belongs to H-H and meets all bounds. QED.

The k_i=0 or n cases have a_i=0, preserve |d_i| and add no depth discrimination. At k_i=n/2, s_i=0 and d_i=0: once distinct histories have merged into the SAME raw state, all later observations remain equal by choosing the same future b_i. Thus a later phase cannot undo this particular early coalescence.

## 2. Sharp X6 two-stage results

Use the previously published signed triad candidate R(z_1,...,z_6)=(-z_3,z_1,z_2,z_4,z_5,z_6). At each stage apply R to the preceding raw state, then append a separately unknown positive-only native word. As g_1=g_2=R, both stages have k_1=k_2=1. The scalar depth-gap propagation is 1 -> 2/3 -> 4/9. The arithmetic gives

    L=lcm(den(1/3),den(2/9))=9,
    (T_1,T_2)=(15,10).

Therefore both registered intermediate min-zero readouts recover the entire initial depth and both segment occurrence vectors whenever M_1<15 OR M_2<10, regardless of the other registered word length. The first serial ambiguity appears at M_1=15 AND M_2=10. In particular, a first-stage ambiguity possible at M_1=5 cannot survive the second registered R observation at ANY M_2: its initial depth gap 3 produces intermediate gap 2, which cannot satisfy 6|2*2.

Exact sharp witness (initial r=0, lengths 15 and 10):

    history A: h=9, b_1=(15,0,0,0,0,0), b_2=(10,0,0,0,0,0)
    history B: h=0, b'_1=(0,3,3,3,3,3), b'_2=(0,2,2,2,2,2).

Both yield y_1=(0,3,3,3,3,3) and y_2=(0,5,8,8,8,8), despite differing initial depth and per-segment path counts. Raw states after stage one differ by 6D; after stage two they differ by 4D. Adding shared admissible vector padding at each segment extends this collision to all larger M_1 and M_2.

Other exact sign-count choices for n=6:

| k_1,k_2 | least gap L | first-stage T_1 | second-stage T_2 |
|---|---:|---:|---:|
| 1, 1 | 9 | 15 | 10 |
| 1, 2 | 9 | 15 | 16 |
| 1, 3 | 3 | 5 | 6 |
| 2, 1 | 9 | 24 | 5 |
| 2, 2 | 9 | 24 | 8 |
| 3, 1 | 1 | 3 | 0 |

For (k_1,k_2)=(3,1), the initial phase has exactly half negative signs and collapses the raw common-depth difference to zero. A first-stage collision at M_1=3 therefore remains possible even if M_2=0.

## 3. Independent exact checks

Exact rational arithmetic computed the L and threshold pairs displayed above. The explicit n=6 history was checked by direct integer vector updates for both stages; all twelve observed coordinates match pairwise after q.

As an independent exhaustive small-rank check, n=4, k_1=k_2=1 gives L=4 and (T_1,T_2)=(6,3). For initial depths h=0,...,4 and ALL n=4 nonnegative occurrence vectors at each fixed length, the map was verified to have no duplicate complete history at (M_1,M_2)=(5,3), across 5,600 enumerated histories, or (6,2), across 4,200 histories. At (6,3), the exact exhaustive enumerator finds a collision within 8,400 histories, between h=0 and h=4. Another independent case n=4,(k_1,k_2)=(2,1) gives L=1,(T_1,T_2)=(2,0) and a collision already when (M_1,M_2)=(2,0).

The enumeration tests finite families; the preceding integer argument proves the universal candidate-model statement for arbitrary n,m and all nonnegative word lengths.

## 4. Consequence for actual Heartbeat / Source-pinned triadic models

This theorem distinguishes **independent probes from successive states of one coherent native path**: the intermediate hidden depth is transformed before the next unknown displacement, so the second observation supplies an arithmetic divisibility test absent from the independent-probe model. It also supplies an exact method to test future specific registered phase/triadic-force rules: extract their actual allowed segment occurrence sets and the signed action on the depth direction, then check whether (3) can be realized by TWO allowed coherent histories. The unrestricted B_M assumption here is an upper envelope of positive-axis segment possibilities; further physical coherence or triadic-force constraints can be represented as restrictions on the admissible histories, without changing this proof.

Keep ordered word/branch identity and BRC multiplicity outside the recovered occurrence-vector assertion. Keep real Heartbeat time, global self-consistent instantaneous state, and primitive triadic-force closure distinct from this affine candidate. The next decisive Source-typed question is whether the present native rotation-plus-positive-path operator is a permitted state transition for the current triadic-force update, and, if not, which exact allowed transitions supply a corresponding difference-set test.

Source lineage: research_notes/driver/2026-11-12_x6_unregistered_positive_microsteps_sharp_depth_alias_threshold.md; research_notes/driver/2026-11-12_x6_time_ordered_signed_rotation_depth_observability.md; definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json; definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md; definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json. This is an authored Driver mathematical audit saved on canonical Source, not an admitted Native Result, independent reference review, official Task closure or parent Objective closure.
