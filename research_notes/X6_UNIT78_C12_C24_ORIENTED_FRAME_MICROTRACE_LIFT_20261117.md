# X6 Unit78 — all-20 C12 microtrace causal horizon and exact typed C24 history lift

Date: 2026-11-17. Parent: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905; Task: RS-X6-LEGACY-PLANE-RECONCILIATION; publication: TP2-B4A441B23DA3159232C2.
Source provenance: original on-hour Research lane, EM-X6-FB6990 / MCP-082892eb480e45dea6d4b9fcc0491034; exact previous author Unit77 and independently checked Unit78. Status: AUTHOR-EXACT / FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED. Do not count as R063 or Helly benchmark, Result, Driver approval or native PROGRESS.

## Immutable premise and genuine new question

Frozen signed P000 V5 input: enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03, 6 signed Cell axes; historical plane corpus remains fd2bcff10ca6e147348b6c1236027fc0d2877df3. Original live executable conventions were read at enterprise-math@76570a3b4dd3416bd5c2a90ec4edd0d955be3175, files:
- experiments/x6_triadic_rotation_v1_20260906/check_triadic_rotation.py (blob c446d0327f9bf643d5796348ba46cafe96d2915d);
- experiments/viete_x6_all20_triadic_root_c24_20260906/check_viete_x6_all20_triadic_root_c24.py (blob aa84515187c4319a6f8a65e65d12d6edbaae67fb);
- experiments/viete_x6_prostate_memory_obstruction_20260905/check_prostate_memory_obstruction.py (blob ea3273e1b1b05b9ea16efadc6351630fedfb22dd).

Unit77 already proved that the C12 root Cell does not determine the signed q rotation without its frame. This unit closes a different operational gap: exactly when does the *actual C12 all-OUTER microstep* first distinguish the missing frame, and what is the smallest declared period-24 history cover preserving both microtrace and frame? It uses the fixed all-OUTER branch; no change to the original accepted source or new X6 primitive is proposed.

## Theorem A — one microstep descends, two microsteps do not

For each ascending triad of axis indices 0<=i<j<k<=5, define q(e_i)=-e_j, q(e_j)=-e_k, q(e_k)=-e_i; all other signed axes fixed. For eps=+ use q, eps=- use q^{-1}. Starting at a_0=e_i, put a_r=q^{eps*r}e_i, for r mod 6, and let the twelve original OUTER microstates be x_{2r}=a_r, x_{2r+1}=a_r+a_{r+1}.

The micro-root at index 3 and its next two actual microstates are:

eps=+: (x_3,x_4,x_5)=(e_k-e_j, e_k, e_k-e_i).
eps=-: (x_3,x_4,x_5)=(e_j-e_k, e_j, e_j-e_i).

Proof: substitute the explicit q-orbit phases, forward (e_i,-e_j,e_k,-e_i,e_j,-e_k) and reverse (e_i,-e_k,e_j,-e_i,e_k,-e_j). This is identity in the six signed native coordinates, not a carrier quotient.

For a fixed observed signed root, the ordered pair j,k and eps are recovered from the nonzero signed coordinates, but i ranges over 0,...,j-1. The first next microstate x_4 is therefore independent of i; x_5 varies injectively with i. Consequently root-only microtrace prediction is exact over the one-step root horizon, and ceases to be single-valued after two microsteps for exactly 12 of the 20 distinct signed roots. For the original max fiber, j=4 (0-based), four source i values are possible. This is a refined horizon statement, not a claim that every C12 microstep factors through Cell everywhere.

Concrete witness: triads (0,2,4) and (1,2,4), both forward, share x_3=e_4-e_2 and x_4=e_4, while x_5=e_4-e_0 and e_4-e_1 differ. Translating to 1-based axis names: (1,3,5) versus (2,3,5).

## Theorem B — minimal typed period-24 lift with retained frame

For each fixed triad S and orientation eps, the x_0,...,x_11 are twelve different native Cell states and x_{r+2}=q^eps(x_r). Define a separate history-state cover (k,b) in Z/12 x Z/2 with exact successor

F(k,b)=(k+1 mod 12, b xor [k=11]).

The projection to native Cell is pi(k,b)=x_k, and pi(F(k,b))=x_{k+1}. It has one 24-cycle; F^12(k,b)=(k,1-b), F^24=id. Its macro update Q=F^2 projects exactly to the named native q^eps; Q^6 toggles the sheet, Q^12=id. This is an explicit cocycle/historical 2-cover, not a seventh native spatial axis and not a derivation of the separate complex spinor or principal +/-3 scalar.

Minimality: a 12-cycle cannot map equivariantly onto the 24-cycle under a one-step successor, since equivariance of any state x gives phi(x)=phi(T^{12}x)=phi(x)+12 mod 24, impossible. At least two distinct history states over each native microcycle are required; the constructed 2-cover attains this lower bound. At a known root phase with the maximum 4 source frames, the two sheets make 8 mutually distinguishable (frame,history) continuations, so 3 extra binary bits beyond the signed root and known root phase are sufficient and necessary in the worst case for simultaneously retaining frame-specific two-step future and the declared C24 sheet.

The full all-20 oriented labeled population has 20 triads x 2 chirality branches x 12 phases x 2 sheets = 960 states. Counting only 20 root Cells or 40 frame-root observations as 960 native Cells would be a type error.

## Exact execution, limits and next action

Independent integer Python checker enumerated all 20 combinations, both original q/q^{-1} orientations, all 12 original OUTER microstates and two history sheets. It checked 480 macro-action identities, 960 sheet-state cycles, the {1:8,2:6,3:4,4:2} fiber histogram, 12 ambiguous two-step root fibers, and the period/holonomy identities. Python normal, -O and -OO returned identical JSON, SHA256 7efa8b5c8ff21ad5c5bd7d669fa40f1dc5e2c7164ea1ffc9ebea70ff02f3bd95. Exact program is research_checks/X6_UNIT78_C12_C24_FRAME_MICROTRACE_CHECK_20261117.py and output certificate is research_checks/X6_UNIT78_C12_C24_FRAME_MICROTRACE_RESULTS_20261117.json.

This unit supplies a typed adapter and original-native causal horizon test for LP023/LP028. It is NOT a complete original Viète C24 spinor dynamical identification, R063/Helly native experiment rerun, all-current-callers closure or independent acceptance. Existing unit77 evidence and historic Unit76 remain intact. The next mother-unit is to test an actual downstream consumer that identifies its C24 spinor sheet with the new history bit, or assumes a root-only two-microstep native prediction: require a specified map and source:line before claiming a defect. Separately preserve unresolved historical LP011 wrong argmax and LP019 positive-BRC signed cancellation source attribution. Current native Unit75 request onhour-20261117-0630-x6-unit75-native-semantic-progress-v1 was newly read as SUCCEEDED/SOURCE_CHECKPOINT_PUBLISHED, not repeated. Unit77/78 native linkage remains pending exact same-SID live-run authorization; neither formal checkpoint nor Driver Result is claimed.
