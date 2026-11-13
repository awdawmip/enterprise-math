# BRC N=4: time-visible observer invariance by causal stopping-time shattering

**2026-10-31 / AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.** This is an independent portable continuation of PR #1757 at immutable parent dbe12d2403b9b40216b0ee001465be82f6fae270. The result is a theorem about a stipulated positive-rational BRC observation game, not a P000 physical Heartbeat evolution or an admitted project theorem.

## Precise carrier, observer and policy semantics

The frozen P/Q experiment has sixteen strictly positive leaves per law, with source S in {AU,AV,BU,BV}, J and independent fair K in {0,1}. Per-K raw P numerators are AU=(9,11), AV=(5,5), BU=(3,27), BV=(30,30), and Q numerators AU=(10,10), AV=(20,20), BU=(15,15), BV=(15,15); each complete law totals 240. Eight prepared (S,P/Q) inputs are scored. The six distinct conditional future rows, ordered AU_Q, AU_P, AV, BU_Q, BU_P, BV, on LR-class columns AU0,AU1,AV,BU0,BU1,BV are

    M=(1/20)*[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
              [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]].

The original full public record is O=(T,Decision,Z_BU). A BU-only sensor is emitted when BU reaches stage 3 and stops there, with Z=J XOR Bernoulli(epsilon), real epsilon in [0,1/2]; outside BU its value is bottom. All early-stop/late-stop sensor semantics remain the frozen lawful model's semantics; the general time-only argument never reads the sensor. T is the terminal stage. In the lawful S23/S2 policy language a policy may continue at stage two and, at stage three, choose stop or continue by the contemporaneously observable LR class; surviving paths terminate at stage four. S2 additionally ties AU/BU actions at stage two, and S23 requires equal LR histories at stage three to take equal action. Both witnesses obey these requirements and do not read future K.

A single stochastic encoder E with k symbols is selected before the lawful policy H; each H may have its own stochastic decoder D_H. For any public observer Y define the inf_E sup_H inf_(D_H) max_(eight preparations) total-variation reconstruction radius R_k(Y,F;epsilon). Y is a source-independent possibly randomized postprocessing of full O. The theorem uses only Y for which T can be recovered deterministically. The decoder never sees the true S,J,K or the prepared law.

## Theorem A: stopping time alone retains the sharp k>=2 staircase

For every source-independent observer O -> Y -> T, with T recoverable without error from Y, both complete lawful families F=S23 and F=S2, every real epsilon in [0,1/2], and unrestricted stochastic encoders and policy-dependent decoders:

    R_2(Y)=R_3(Y)=1/2,
    R_4(Y)=1/5,
    R_5(Y)=1/40,
    R_k(Y)=0 for all k>=6.

In particular **Y=T alone** already attains these exact minimax radii. This is a worst-policy distribution-reconstruction assertion, not pointwise or native-state sufficiency.

### Legal time-bit shattering family

For every b in {0,1}^6 define H_b^T: continue at stage one and stage two on every source; at stage three STOP iff the observed LR class j has b_j=1, otherwise CONTINUE to stage four and then terminate. The terminal Decision can be constant P everywhere. The six LR classes are distinct except within the combined AV and BV classes already represented by one column each, so the decisions to stop/continue are lawful in S23; stage-two AU/BU actions are both CONTINUE so S2 is also satisfied. No future bit K or private source label is queried.

The visible time event {T=3} has six-row probability exactly M b. Therefore the 64 H_b^T encode precisely the same 64 binary rows used by the predecessor's Decision-only dual theorem, while the public Decision itself is not observed.

Fix any row-stochastic six-by-k E with k<=5. Choose any nonzero w in its left kernel. E times the all-one code vector is the all-one preparation vector, hence sum(w)=0. For each b, if the Y-reconstruction error is at most delta, the time marginal error is at most delta. Writing d_b in [0,1]^k for the decoded probability of {T=3}, one obtains

    |w^T M b|=|w^T(Mb-E d_b)| <= delta ||w||_1.

Because r=w^T M has zero coordinate sum, max_{b in {0,1}^6}|r b|=||r||_1/2. Thus, for any such w,

    delta >= ||w^T M||_1/(2||w||_1).                         (1)

This calculation permits a different decoder for each H_b^T, so no unjustified common-decoder premise enters the lower bound.

For k=2 or 3, restrict w to the four rows AU_Q,AV,BU_Q,BV, which have mutually disjoint LR-class supports. Their four-by-k E submatrix has nonzero left kernel. On this support ||w^T M||_1=||w||_1, yielding delta>=1/2.

For k=4, a nonzero left-null w=(a,a,b,c,d,e) exists: w1=w2 is one additional homogeneous constraint on six unknowns in four encoder equations. Since sum(w)=0, write B=2|a|+|b|+|e|, s=c+d, and B>=|s|. Direct multiplication yields

    ||w^T M||_1
     =B+|c/2+d/10|+|c/2+9d/10|
     =B+max(|s|,4|d|/5)
     >=B+4|d|/5.

Also ||w||_1=B+|s-d|+|d|<=2B+2|d|. Hence ||w^T M||_1>=(2/5)||w||_1, so (1) gives delta>=1/5 for every stochastic E.

For k=5, M is invertible. The six inverse columns mapping r=w^T M to w are

    (11,-10,0,0,0,0), (-9,10,0,0,0,0), (0,0,1,0,0,0),
    (0,0,0,9/4,-5/4,0), (0,0,0,-1/4,5/4,0), (0,0,0,0,0,1).

Their maximal pairwise L1 distance is exactly 40. Any zero-sum r has r=t(p-q) with t=||r||_1/2 and probability vectors p,q; their inverse images lie in the convex hull of these six columns, so

    ||w||_1 <=40t=20||w^T M||_1.

Equation (1) gives delta>=1/40. All these lower bounds also apply to a richer observer Y whenever T is recoverable.

### Constructive upper bounds for the full O and all its postprocessings

On the full six-class future, the following unconditional reconstruction kernels have rowwise exact total-variation radii, in order k=1,2,4,5:

    D1=(5,5,10,2,8,10)/40, one constant code: max error 3/4;
    D2L=(10,10,20,0,0,0)/40 for AU/AV, and
    D2R=(0,0,0,4,16,20)/40 for BU/BV: max error 1/2;
    D4 uses one source code for AU,AV,BU,BV, with AU J1=21/40
       and BU J1=28/40: max error 1/5;
    D5 merges only AU_Q and AU_P at J1=21/40, retains all
       four other distinct preparations: max error 1/40;
    D6 exactly retains all six distinct conditional rows: error 0.

Attach fair K and the same BU sensor kernel, then execute any lawful H. Total-variation contraction under this common Markov postprocessing gives the displayed upper bounds simultaneously for every H and every epsilon. The same bounds carry to any postprocessed Y, giving Theorem A. For k=3 reuse the two-code construction; for k>6 ignore excess codes.

## Theorem B: deleting Decision and sensor BIT retains the entire low-code staircase

Let Y1=(T,Z_BU), with bottom as an observable absence indicator, and Y2=(T,I[Z_BU is present]). These are source-independent postprocessings of O and retain T. For every real epsilon in [0,1/2] and either lawful family:

    R_1(Y1)=R_1(Y2)=3/4,
    R_2(Y1)=R_2(Y2)=R_3(Y1)=R_3(Y2)=1/2,
    R_4(Y1)=R_4(Y2)=1/5,
    R_5(Y1)=R_5(Y2)=1/40,
    R_{k>=6}(Y1)=R_{k>=6}(Y2)=0.

Only k=1 remains to prove beyond Theorem A. Define a *single* legal policy H_dagger: stage one continues; at stage two stop AV, continue AU/BU/BV; at stage three stop AU and BU, continue BV; at stage four stop BV. Give every terminal leaf the same Decision=P. S2 ties the AU/BU stage-two CONTINUE actions; S23 has identical stage-three action for equal-LR-class histories (notably both BV J values continue). All BU paths stop at stage three and emit the BU-only tag. Its public Y2 supports are exactly four disjoint atoms:

    AV -> (2,absent), AU -> (3,absent),
    BV -> (4,absent), BU -> (3,present).

Under Y1 the BU atom splits into (3,0)/(3,1), still disjoint from the other three supports for every epsilon. Take one preparation from each group. For any one-code decoder distribution d, the four disjoint-support masses sum at most one, so one true input has overlap at most 1/4 and total variation at least 3/4. Conversely D1 above has full-carrier error <=3/4 for all H, hence Y1 and Y2 have exact R1=3/4.

This explicitly preserves original source, joint branch identities, timing and the BU tag on the scientific carrier. The fact that Decision and sensor BIT do not affect these worst-policy radii does not give a fiberwise factorization for every fixed H or future operation.

## Additional finite fixed-policy distinction

For H_dagger and Y1, the observed output matrix has three separate non-BU pure-atom columns plus a BU two-bit block. BU_Q=(1/2,1/2) and BU_P=(1/10+(4/5)epsilon,9/10-(4/5)epsilon), with determinant (2/5)(1-2epsilon). Thus the exact rank, and the minimum exact stochastic code count for this *fixed policy*, are 5 when epsilon<1/2 and 4 at epsilon=1/2. For Y2 the four source-prototype atoms have rank 4 for all epsilon and four codes attain zero fixed-policy error. This rank statement is not an all-policy zero-loss claim.

## Validation and scientific boundaries

The actually executed exact-integer VERIFY.js reconstructs all P/Q leaf normalizations, 64 legal time-bit policies on all eight preparations (512 checks), H_dagger observed distributions on eight preparations and four rational epsilon values (32), four full-carrier upper references on six distinct rows (24), and all fifteen inverse-column pairs; see RUN_EVIDENCE.txt. Universal stochastic E, all lawful randomized/adaptive H, and all real epsilon follow from the analytic inequalities, not from finite epsilon samples or grid search. The physical P000 native six-axis Cell torsor, separate time and native joint path/provenance require a separately proved observer-and-future-operation-preserving map into this finite carrier. No external physical inference or mathematical admission follows from this finite theorem.
