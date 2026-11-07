# EC49E — equal marginal LR spectra, but strict two-step causal loss

2026-10-28 Asia/Shanghai. AUTHOR_PROVED / EXACT_FRACTION_ENUMERATION_PASS / UNREVIEWED / NOT_ADMITTED. Author-side continuation of EC49D Draft PR #1628, immutable prior commit f5076cb3cff1581dd7885e19dc58b086de76a74a. Auxiliary finite positive-rational weighted-BRC observer; not native signed BRC or X6. This is a different 8-leaf binary full-support witness from the earlier EC48W 16-leaf two-stage counterexample. No minimum-size claim.

## Precise finite model, observation language and clock

There are two strictly positive source laws P,Q on 8 labeled atoms (W,Y1,Y2) in {0,1}^3. The following integers are *unconditional* masses multiplied by 40:

| W | Y1 | Y2 | 40P | 40Q | exact full P/Q LR |
|---|---|---|---:|---:|---:|
| 0 | 1 | 1 | 14 | 4 | 7/2 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 0 | 0 | 4 | 14 | 2/7 |
| 1 | 1 | 1 | 11 | 1 | 11 |
| 1 | 1 | 0 | 4 | 4 | 1 |
| 1 | 0 | 1 | 4 | 4 | 1 |
| 1 | 0 | 0 | 1 | 11 | 1/11 |

In each source, the weights sum to 40/40. W is source-ancillary: P(W=w)=Q(W=w)=1/2.

At T=1 choose reject, accept, or continue to observe Y1 at T=2. At T=2 choose reject, accept, or continue to observe Y2 at T=3. At T=3 accept or reject. Direct acquisition of Y2 without Y1 is not permitted. Both continuation decisions are genuine options; T is an auxiliary time-step counter, not physical heartbeat time. Policies must be source-neutral and may use arbitrary real behavioral probabilities, but have no hidden writable register or retained random seed. T=1,2,3 is always available to select the stage.

Coarse stage readouts: T1 constant; T2 exact *complete prefix* LR L1=P(Y1)/Q(Y1), equal to 3 for Y1=1 and 1/3 for Y1=0; T3 exact *full hidden-joint* LR L2=P(W,Y1,Y2)/Q(W,Y1,Y2) in {1/11,2/7,1,7/2,11}. The latter readout is a declared auxiliary oracle even when W itself is hidden. Fine readouts add W at each stage, including T1. Fine T3 (W,L2) has six distinguishable values. A policy decision uses the current stage readout only.

Define the **raw** achievable four-vector region S as O=(α,β,E_PT,E_QT), with α=P(accept), β=Q(accept). Fine may ignore W, hence S_coarse ⊆ S_fine.

## Exact marginal-spectral equality and nontrivial relational residual

For every w and each i=1,2:
P(Yi=1|w)=3/4, Q(Yi=1|w)=1/4;
P(Yi=0|w)=1/4, Q(Yi=0|w)=3/4.

Thus both Y1 and Y2 are *informative* about P versus Q, but every W-conditional individual-signal Q-LR spectrum is exactly ν=(3/4)δ_{1/3}+(1/4)δ_3. Every individual marginal LR threshold/call functional, not merely one selected scalar score, is therefore independent of W.

The *joint* prediction is not W-invariant. Conditional on Y1=1:
P(Y2=1|w=0,Y1=1)=14/15 versus P(Y2=1|w=1,Y1=1)=11/15;
Q gives 4/5 versus 1/5.
This lost W-dependent correlation is the structural residual. In particular the Y1-conditioned next-step spectra do differ. We do NOT claim that the full causal predictive kernels or *conditionally updated* next-step LR laws coincide.

## Exact global theorem for every real nonnegative cost

Let [x]_+=max(0,x), c≥0, and define the linear four-vector functional
F_c(O)=α−2β−c(E_PT+E_QT−2).
The +2c term just normalizes the compulsory first clock state.

The maxima over ALL source-neutral behavioral policies in the declared two observer languages are

V_coarse(c)=[1/4−2c+(1/8−c)_+]_+;

V_fine(c)=(1/2){[1/4−2c+(1/20−c)_+]_+
                    +[1/4−2c+(1/5−c)_+]_+}.

**Proof, including random policies.** Fix W=w and conditionally normalize its P and Q masses to 1. At T2, Y1=0 has nonpositive immediate accept reward P−2Q and all its terminal LR values are ≤1<2, hence reject optimally. For Y1=1 the immediate accept reward is 3/4−2(1/4)=1/4. At T3, given any actually purchased branch, accept iff its complete LR exceeds 2, since its individual reward has sign P−2Q=Q(LR−2). On Y1=1 this terminal maximum equals 14/20−2(4/20)=3/10 at W=0, and 11/20−2(1/20)=9/20 at W=1; the increment above immediate acceptance is respectively g_0=1/20 and g_1=1/5. The extra T2→T3 step costs c(P(Y1=1|w)+Q(Y1=1|w))=c. Thus each conditional W fiber's T2 option value is 1/4+(g_w−c)_+. Purchasing Y1 at T1 costs c(P+Q)=2c per W-conditional normalized fiber. Rejecting at T1 has normalized value zero, and immediate accepting has negative value 1−2. The fine observer optimizes separately in the two equally weighted W fibers, yielding V_fine.

Coarse cannot condition the T1 or T2 purchases on W. The T2=Y1=1 posterior W mixture has equal 1/2 weights under both sources; terminal positive payoff is (3/10+9/20)/2=3/8 and its increase over immediate accept is 1/8. It follows that V_coarse is the single T1 max formula. The T3 optimal LR threshold rule is simultaneously admissible across any histories merged into the same terminal LR, because the sign of Q(LR−2) is consistent on that fiber. Therefore no illicit knowledge of previous Y1 is used.

Each node's behavioral random probabilities produce a multilinear expected score. Independently sampling deterministic actions for all finite observation nodes before the run expresses the score as a convex mixture of complete deterministic-policy scores, with no operational seed required in a pure deterministic maximizing policy. Consequently random behavioral strategies cannot exceed these deterministic dynamic-programming maxima. The formulas hold for every real c≥0 and every legal randomized policy. QED.

Subtracting yields the **sharp** cost profile

Δ(c)=V_fine−V_coarse =
0,                            0≤c≤1/20;
c/2−1/40,                   1/20<c≤1/8;
9/40−3c/2,                 1/8<c<3/20;
0,                            c≥3/20.

Hence Δ>0 exactly when 1/20<c<3/20. Its maximum is 3/80 at c=1/8; free acquisition c=0 has Δ=0. The defect is specifically a *history-dependent continuation option*, despite every individual marginal predictive LR spectrum being unchanged.

## Strict raw-region separation certificate

At c=1/8, coarse has V_coarse=0 and fine has V_fine=3/80.

Implement the fine deterministic witness as follows: at T1 reject if W=0, otherwise purchase Y1. At T2 reject if Y1=0, otherwise purchase Y2. At T3 accept exactly for complete LR=11 (the one atom W=Y1=Y2=1), reject otherwise.

Its explicitly computed raw observation is O*=(11/40,1/40,15/8,13/8). The P time numerator is 20+2·5+3·15=75, Q time numerator is 20+2·15+3·5=65, each over 40. Then
F_{1/8}(O*)=11/40−2/40−(1/8)(15/8+13/8−2)=3/80.

The coarse inequality F_{1/8}(O)≤0 applies to every coarse raw vector, and therefore to its convex hull. Since F_{1/8}(O*)>0, O* is not even in conv(S_coarse), proving S_coarse is a proper subset of S_fine. This strict support witness is stronger than a failure to reconstruct some selected policy.

## Reproduction, typing and next discriminating obligation

Run python VERIFY.py and compare actual stdout JSON to EXACT_REPORT.json. The executed Python Fraction verifier checks strict positive masses and normalization, both marginal spectra, exact likelihood ratios, and fully enumerates 864 coarse and 46,656 fine deterministic policies (47,520 total); each of 11 rational cost cases matches the closed support formula. It also checks the explicit witness and sharp-gap cases. The *continuous* real-cost theorem is the algebra above, not a claim of computational enumeration over reals.

Positive rational weighted branch mass and labeled (W,Y1,Y2) provenance are the actual BRC carrier. The original W fiber is a relationship coordinate, not another spatial dimension. No signed amplitude, physical experiment, native X6 coordinate, P000 rotation, three-dimensional native slice, or heartbeat time calibration has been computed. General two-stage bisimulation, P000 transfer, irrational-only rational-target feasibility and independent mathematical review remain separate proof/verification obligations.

EC49F next: determine a sufficiently fine *action-conditioned* causal predictive carrier that allows source-neutral finite-memory policy reconstruction of the entire **raw** region under two future acquisitions; either prove an exact occupancy-kernel quotient theorem or construct a distinct exact two-action rational obstruction. For current source pins, scientific literature and actual authority status see SOURCES.md; for an executable next specification see NEXT_TASK.md.
