# 心跳世界：相位协变乘法与非线性 BRC 验证

Researcher-ID: `EM-DIRECT-AD0416`
Research-Activity-ID: `RA-37C0A30C7B1F5A338F03D186`
Progress-Event-ID: `heartbeat-phase-algebra-resume-20260919-AD0416`
Session: `chat-local-reciprocal-ceec8bd1559acdf8c10ebc9b` (existing local identifier; not a platform-authenticated ID).
Status: `RESEARCH_DOMAIN_ADAPTER / SCOPED_PROOFS / EXECUTED_CHECKS / NOT_FOUNDATION`.
Read snapshots: EM `a9e632e1d929ac77ffb433f2469bce4dc27b12fc`; GLOBAL_KNOWLEDGE `d6a541e8ed8949dfc4f24809b3ce00fe695b5368`.

## 1. Interrupted-turn recovery

The missing chat response did not mean the preceding work was absent. The immutable naming transaction `a06a465e3bd932981794feb60c8a7aa937ca72f6` already created `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.md` and `.json` and bound them through P000. The algebra/checkpoint transaction `e02b464e158923ee94a7d5d0e0aa1dd843090ad3` already preserved the 15-group ring/carry/time-port verification. Current main contains both and their activity entry. Those results were consumed, not restarted or counted as new execution. This continuation executes the next explicitly recorded unfinished mathematical unit: transport the product with the frame and check a nonlinear update.

The name 心跳世界 / HEARTBEAT_WORLD denotes ALL native X6 space plus one time dimension, not just b=2 or twelve ticks. The seven event coordinates do not include every branch decoration. Raw signed relative displacements and registered final nonnegative Cell addresses remain different interfaces. This note does not change any native axis, P000 premise, full-rotation law or physical clock calibration.

## 2. Algebra transported with the readout

Fix the existing research ring R_b=Z[lambda]/(lambda^6-b), a chart anchor, cyclic axis order and b>=2. Let A multiply by lambda, so A^6=bI. Choose depth j>=0 and a positive-axis permutation P; set F=P A^j. Its exact readout domain is I_F=F(Z^6). F is an additive bijection from Z^6 onto I_F even for composite b with zero divisors in R_b: the integer matrix A has nonzero determinant.

Define on I_F:

    u *_F v = F(F^-1(u) * F^-1(v)).

Every inverse here is restricted to I_F. The implementation checks each Euclidean residue and rejects any nonzero residue; it never creates a fractional native Cell. The unit is F(1), not generally e1.

For u=F(x), v=F(y), w=F(z), both associations reduce to F((x*y)*z)=F(x*(y*z)); commutativity and distributivity follow the same substitution. Thus F is a ring isomorphism onto this transported ring. No metric or extra geometry theorem is required.

For P=I a second route is

    u *_j v = A^(-j)(u*v),  u,v in A^j R_b.

Indeed raw u*v=A^(2j)(x*y), and exactly one frame factor must be removed. With general P, unpermute before the raw product and permute back afterwards. Both computation routes were compared on 600 signed random triples, b in {2,3,4,5,7}, depths 0..12. All 720 positive-axis permutations were checked in the transported interface. This does not claim that all 720 preserve one frozen raw product: the earlier fixed-product symmetry obstruction remains valid.

Minimal false-dynamics witness: material 1 has phase-one readout lambda. The correct same-phase product of its two readouts is lambda, because 1*1=1; the untransported formula yields lambda^2. An apparent coordinate-axis change was manufactured by using the wrong multiplication law. This is a coordinate/modeling fault, not a new physical phenomenon.

## 3. Lossless coarse representation

Reuse the earlier repeated analyze/synthesize maps. At depth j a material x has a unique coarse coordinate q and chronological j-digit residue tuple r. Reconstructing x, applying the existing product, and reanalyzing gives a lossless transported product on (q,r). This is a reference correctness adapter, not a claim of compressed arithmetic or bounded-bit storage. 500 signed pairs at depths up to12 match full-coordinate products. All zero and negative-coordinate carries are retained.

## 4. Time and nonlinear update

A FrameProgram explicitly supplies j(t), b and P. Same-time binary arithmetic requires identical time and program ports. Equal phase modulo a period does not make time0 and time12 the same event. FramedEvent.advance moves from t to t+1 and applies a declared material update U; a readout-only change uses U=id and therefore is NOT an identity arrow in time.

For y_t=F_t(x_t), the correct nonlinear evolution is

    y_(t+1) = F_(t+1)(U(F_t^-1(y_t))).

For the declared diagnostic U(x)=x*x+1, a no-pulse program and the twelve-depth breathing program recover exactly the same material trajectory. This is proved by substitution, and checked for three signed initial conditions over eight updates each. It does not prove that every physical pulse is only a readout. It separates pure reframing from an interaction that actually changes with the physical scale or phase. A pulse-specific benefit must be sought in such an explicitly different U_t, not by changing coordinates and retaining a stale operation formula.

## 5. New BRC boundary: quadratic observations and joint pairing

The affine degree-two moment lease is unchanged. But U(x)=x*x is quadratic in the six integer coefficients. Take material measures along e1:

    mu=(delta_-1+delta_1)/2,
    nu=delta_-2/8+3delta_0/4+delta_2/8.

All input moments of degree<=2 agree. After squaring, both first moments are1, but their second moments are1 and4. Existing exact BRC histogram/moment code verifies this. A one-step quadratic polynomial output of degree<=2 is determined by input moments through degree4; after K quadratic updates degree2^(K+1) is a general sufficient bound, not a minimality claim and not a practical universal compression method. Special supports/invariants can lower the requirement.

A second, distinct obstruction concerns multiplying two fields. Let X,Y each have marginal distribution {-1,+1} with equal positive weights. If Y=X, E[XY]=1; if independently paired, E[XY]=0. The marginal histograms are exactly equal, yet the product distributions differ. The missing object is the joint branch pairing, not a higher marginal moment. Positive branch mass remains1 in both experiments; signed algebraic coefficients are not negative BRC weights. A binary product must carry its declared joint law/time ports or an independence certificate. Cartesian branch composition without such a premise changes the problem.

## 6. Execution and exact sources

Executed unchanged `research/heartbeat_algebra.py` (Git blob c8d0b73a805740075e9b485d53e3b9ab71636490), existing brc_transport and brc_histogram. The existing contract-check function was reused as a verbatim excerpt from `tests/verify_heartbeat_world.py`; this is not a claim to execute that entire prior test suite. Five complete local files, including the naming JSON and cached predictive module, were checked against observed Git blobs. The cached predictive module was not newly invoked for a new result. The vendor prime-valuation dependency remains an explicitly labeled minimal excerpt from the earlier package.

T0 affine/histogram reuse: REUSE_EXECUTED. Existing radix analysis/synthesis: REUSE_EXECUTED. Frame transport, image-domain guards, and explicit same-time binary interface: EXTEND_EXISTING_TOOL / RESEARCH_DOMAIN_ADAPTER. No new top-level BRC family and no automatic source or Foundation admission.

10 new check groups PASS:5 byte identities; naming contract with7 invalid mutations;600 transported-ring triples;720 axis relabelings;500 residue pairs;3x8 nonlinear trajectory comparisons;static-product failure witness;quadratic-moment witness;joint-pairing witness;8 invalid time/domain rejections. Compilation passed. Seeds and full outputs are in PHASE_RESULTS.json. This is local execution and a second algebraic computation path, not independent mathematical peer review or whole-project integration tests.

Primary literature comparison inspected only at abstract/metadata level: Garcia Garcia et al., arXiv:1603.03330 (polyphase and perfect reconstruction); Garcia et al., arXiv:1804.04974 (semi-direct products, filter banks and sampling). These situate known mathematics; the proofs above stand on explicit substitutions. No priority/novelty claim.

## 7. Remaining exact question

A coordinate-only heartbeat has now been separated from material evolution at both linear and quadratic levels. The next meaningful research variable is ONE declared geometry-dependent U_t or joint branch coupling that changes with scale/phase, tested against this conjugate baseline at equal actual work. This note does not add such an interaction, claim semantic recall improvement, or change production Nollm.
