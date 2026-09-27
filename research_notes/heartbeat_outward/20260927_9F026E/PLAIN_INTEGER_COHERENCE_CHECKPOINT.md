# 小整数多世界相干接口：执行检查点

Progress-Event-ID: hbw-plain-integer-coherence-9f026e-20260927
Status: EXECUTED_FINITE_SIGNED_BRC_CANDIDATE / NOT_ADMITTED
Researcher-ID: EM-DIRECT-9F026E
Research-Activity-ID: RA-DEF97E433B003C96F9B921F8
Session: local-chat-hbw-outward-940b2892a3a34015a3b6f1afc20f60b4 (local scope, not platform authentication)
Global-read: a2556afc4bb707a69d3b195d4fee4090cf64f8a2
EM-arithmetic-source: d37d848b5e6bf5f8835ae1ed8226b1b32e8bd4dc

用户原话：“深入试试，思想要深奥，计算要朴素。”

## Actual result and scope

One frozen candidate trial executed, with 61 predeclared assertions passing. This is a sourced positive-BRC two-sign extension, NOT raw X6 Cell/carry dynamics, a physical Bell experiment, a derived native coupling, a general efficient classical quantum simulator, or Shor closure. No pi, trigonometry, ordinary matrix propagator, high-precision reference simulation, or world-axiom change was used. Two ports are logical interfaces, not two-force primitive balance; a three-input sign rule is not automatically P000 triadic closure. Outward spatial transport itself was not executed in this trial.

Exact positive primitives actually reused: CWMState/constants, cwm_edge, cwm_recoalesce, cwm_propagate, from src/enterprise_math/brc_weighted.py at the EM pin. Whole-file Git blob 3f205696709e847909958a153f8fe10d3f6b70f0. The retrieved lines 1-110 excerpt has SHA256 6d0fdbb61e873d01edf460d0b2a40647e9325b804192e99152857974d489b7bc. Only the complete required AST definitions and imports were selected without changing bodies; excerpt hash is not full-file hash.

## Typed extension and equations

For positive CWM carriers P,N,R,S, use signed pairs A=(P,N):

    (P,N) plus (R,S) = (P plus R,N plus S)
    (P,N) times (R,S) = (P*R plus N*S,P*S plus N*R)
    sign_flip(P,N) = (N,P)
    chi(P,N) = P.total-N.total

Expansion proves chi preserves alternative sum and serial product. This familiar two-sign algebra is a candidate extension, not a new theorem of positive mass cancellation. State keys retain full joint bits and active environment labels. Same dynamic keys may interfere; distinct active labels are squared separately before marginalization. Passive audit history is preserved outside the dynamical key under the declared future-operation lease. History-sensitive future operations require rechecking that lease. Born-style squared readout is an explicit bridge assumption, not a derived physical law.

The integer two-port operation is L(a,b)(x,y)=(a*x+b*y,b*x-a*y). Its squared norm is multiplied by a^2+b^2, so common normalization can be deferred. H~=L(1,1). Starting from a basis state, H~, permutations and sign flips give integer coefficients k_z with sum(k_z^2)=2^h after h H~ gates. Probabilities are k_z^2/2^h; no numerical square root is required. This says nothing about efficient access to all k_z.

## Executed two-world outcomes

Prepare 00+11 by H~ on the first bit then controlled routing. Use A0=identity, A1=H~; B0=L(2,1), B1=L(2,-1). In 00,01,10,11 order:

|Setting|Integer amplitudes|Squared norm|E=P00+P11-P01-P10|
|---|---|---|---|
|A0B0|(2,1,1,-2)|10|3/5|
|A0B1|(2,-1,-1,-2)|10|3/5|
|A1B0|(3,-1,1,3)|20|4/5|
|A1B1|(1,-3,3,1)|20|-4/5|

S=E00+E01+E10-E11=14/5. The simulator centrally maintains a signed joint state; this is not a local-hidden-variable construction or a physical Bell violation. A reversible active marker m <- m XOR a changes reduced readout to S=6/5; repeating that joint operation before measurement restores S=14/5. Deleting a passive log is not physical uncomputation. Bell+ XX output is (1/2,0,0,1/2), Bell- is (0,1/2,1/2,0), tagged XX is uniform.

All 44 pairs a=1..8,b=0..a were executed: all 28 interior pairs had S>2 and all 16 endpoints had S=2. Direct symbolic formula:

    S(a,b)=2(a^2-b^2+2*a*b)/(a^2+b^2)
    S(a,b)-2=4*b*(a-b)/(a^2+b^2).

If each of the four final readout distributions has total-variation error <=epsilon, each correlator changes by <=2epsilon, hence S_actual>=14/5-8epsilon. Epsilon<1/10 retains S>2 in this fixed test. This is not a per-gate or Shor error bound.

## Symbolic boundary continuation (not another run)

For normalized real environment states u,v, set gamma=<u,v> and Psi=(00*u+11*v)/sqrt(2). Future operations confined to the two worlds depend on the environment through its Gram data. The same settings give E00=E01=3/5, E10=4*gamma/5, E11=-4*gamma/5 and S=(6+8*gamma)/5. Gamma>1/2 is the positive-violation condition here. Only gamma=0 and gamma=1 endpoints were executed above. If future operations can access/uncompute the environment, gamma alone is not generally sufficient. Outward coordinate relabeling does not by itself increase overlap or useful-sample probability.

## Executed three-world extension

CCZ flips the sign only at joint bits111. All eight basis columns of H~_c CCZ H~_c=2*Toffoli passed, realizing (a,b,c)->(a,b,c XOR (a AND b)). Symbolically, if ab=0 the target sees H~H~=2I; otherwise H~ZH~=2X. This proves the stated linear identity, not native geometric implementation.

The all-plus three-bit state and its111-sign-flipped version have identical full computational-basis probabilities (therefore identical Z marginals), but applying three H~ gates to the latter gives P000=9/16 and each of the other seven outcomes1/16. This is NOT equality of all reduced density matrices. H+Toffoli computational universality is prior art, not a new result or evidence of efficient classical simulation.

## Actual costs and saved review

Production source calls: cwm_edge1720, cwm_propagate9296, cwm_recoalesce12660; signed observers4066, sign swaps401, exact probability readouts194. There were324 gate applications across the complete test suite, peak8 joint configuration keys, peak10-bit CWM integers, and peak288 positive paths per sign record. These are call counts and record sizes, not total bit operations or physical heartbeat counts.

The raw ledger has27936 arithmetic/observer records,324 gate records, and2490043 bytes. Saved-record self-review checked primitive operands/results, gate transfers,194 normalizations and48 local marginal readouts. Review calls are separately reported. No independent peer admission, source-signed causal execution proof, arbitrary-scale theorem or wall-clock speedup is claimed.

## Complete material and hashes

Google Drive upload succeeded and metadata readback matched file ID, parent, MIME and71187-byte size. No second-download remote byte check was performed.

Archive: https://drive.google.com/file/d/1I2LPlO6cK5BKa6ilLxtEqW7YoF3m0Ch4/view?usp=drivesdk
Parent: 19dd_3frjJu-MeL-eD-UKuNYdCo5cTZXP (进取数论_研究物料)
ZIP SHA256: b4e7ddee0f2ddf25d4cf4a1c25e9214e6d63666393ffd6e355f1e7785a3d3f3d
ZIP MD5 (local):132f4e518dfffce4aa8260c3f615f3e7
Full Chinese report SHA256:b6ea170a1d3e07b01217e05d7f2e7c9f232b2d7d83fe34457cff3f5ebbc41255
Frozen trial.py SHA256:56165a2c9d6d05834b5ccff6069e110c75ef7e89acf295aaf11a8bf930863388
Frozen plan SHA256:865630aebf3ae523a5cfe88040bedd148db60f54cdc3f71351372921be074f4f
Raw ledger SHA256:5c6b521d88b1ca2f160e41a16d5387933113e7d8dcc592d30cab7ba1200e773c
Compressed ledger SHA256:ab5c367e8d2f0f10fb0af2d82e57f4a768fee9ccd7bb2452b41e3443af3ea3c6

The archive contains PLAN.md,STARTED.json,trial.py,source excerpt,results.json,ledger.json.gz,verify_saved.py,saved_record_review.json,REPORT.zh-CN.md,QUERY_AUDIT.json,MANIFEST.json. This checkpoint was authored after the archive and is not inside it. Do not overwrite/restart the frozen run to package it.

## Sources and next unit

Prior art: CHSH, Phys.Rev.Lett.23,880(1969), DOI10.1103/PhysRevLett.23.880; Aharonov arXiv:quant-ph/0301040; Gottesman arXiv:quant-ph/9807006. Publisher/arXiv primary pages were checked. Dedicated query Issue2543 returned three irrelevant records and was not used as mathematical evidence; QUERY_AUDIT preserves checked receipt metadata, not a full provider archive.

Next: choose one bounded native X6 cell/triadic interface and actually derive one of H~ or the conditional111 sign operation, with original-path provenance, all-input correspondence, readout normalization and native resource receipts. Do not insert the desired logical gate into the input and call its output an emergent native law. Then investigate minimal sufficient joint-boundary state and total Shor sampling cost.

The existing own activity was read; this new event still needs its actual source-readback link in that activity. Scientific durability, activity bookkeeping and theorem admission are distinct.

Global-Knowledge-Sync: main@a2556af / GLOBAL_KNOWLEDGE_V1
