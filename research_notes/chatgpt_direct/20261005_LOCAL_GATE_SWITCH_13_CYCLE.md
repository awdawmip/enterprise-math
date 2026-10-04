# Local gate-mode switching: thirteen-step return and permanent phase invisibility

Status: PROVISIONAL MODEL PROOFS AND EXACT FINITE CERTIFICATES / NOT FORMALLY ADMITTED.
This is continued work by the same logical conversation, not independent replication.
Global read snapshot: awdawmip/chatgpt-global-knowledge@f7abd42860a51586b9a7a9207e623d7dd651b0d6.
Current Source read snapshot: awdawmip/enterprise-math@06754542f6e552c705958dee9987096066414a84.
Prior scientific frontier: c75ce13d2cc46b810a61fb6c2351dbe306626123, research_notes/chatgpt_direct/20261004_AUTONOMOUS_TWO_MODE_ECHO.md, blob 01a32f67de2f0c3d988cd247f731e83cdfc8be4d.
Logical conversation: chatgpt-heartbeat-euler-20261004-layer-01; not a platform-attested identity.
Registration request: private bridge issue 2738, session-20261005-euler-local-switch-12. Actual inner receipt FAILED with SOURCE_DOWNLOAD_TOO_LARGE. REGISTER_PENDING; no new Researcher-ID, active session, CLAIM, formal run or independent authority is asserted. Former identities remain contribution provenance only.

## 1. Typed BRC scope and reuse

Ports n in Z/12 are the existing first-level Cell/gate incidence labels: even n are Cell, odd n are gate. Ports are not raw X6 spatial coordinates. The binary mode b is internal state, not a new spatial dimension. P000, six native spatial axes, separate time and the three-dimensional slice constraint are unchanged.

The declared input domain is all 24 (port,mode) states, with positive rational path weights. This extends the prior selected 20-state preparation domain; the baseline rank comparison below uses the same full 24-state domain for both rules. We retain root source, choice identity, positive CWM and operation history on every explicit path. History-sensitive actions are outside the reduced observer contract.

The exact previous conversation archive was recovered: euler_autonomous_echo_evidence.zip, SHA256 869b77a2f317463795fe4cdbe0aac9cb1f25dcd05f7562c22015f12d57c9ee3c. Its brc_autonomous.py SHA256 d8268e8723cd314ad28df1af51d0014ff48db7329035f4632b8867f8da421224 and dependency bytes were reused unchanged. They execute the existing positive CWM core, src/enterprise_math/brc_weighted.py blob 3f205696709e847909958a153f8fe10d3f6b70f0, and the exact finite incidence functions from euler_rotation_refinement.py blob 55e12f7ffb68a5b241f5d6323f5fde118de2716a. The new extension composes a mode-changing BRC edge with the actual previous advance function. REUSE_EXECUTED / EXTEND_EXISTING_TOOL; no new accepted tool family is claimed.

Scientific transport does not use pi, trigonometry, numerical roots, matrix exponentials, Taylor/Padé/Cayley or a classical reference propagator. Exact rational row operations and integer determinants below audit BRC-generated observer certificates; they are not alternative state evolution and never reinterpret signed observations as positive mass.

The new static gate mask is an explicit model assumption, not a derived native field, primitive force balance, physical clock or calibrated interaction. Holding at a gate is part of the newly declared finite program, not a theorem that an actual native gate admits this dwell law. Collision followed by streaming is the chosen update ordering.

## 2. Local reversible mode change

Choose M contained in {1,3,5,7,9,11}. At the current port set c=b XOR 1_M(n), then stream:

F_M(n,b)=(n+c mod12,c).

The collision changes only the mode at the current gate, while streaming holds or uses one existing incidence edge. Its inverse on port/mode is explicit: given (m,c), set n=m-c mod12 and b=c XOR 1_M(n). Thus the port/mode carrier is a permutation. Positive path weights are unchanged. Audit histories append and do not return when port/mode returns.

For m=|M|, there is exactly one cycle of length L=12+m containing all twelve moving states and the m idle states at active gates. Each moving state reaches the next port directly, except at an active gate it first becomes idle for one update and then leaves. The remaining 12-m inactive idle states are fixed. This proves F_M^L=I on the declared port/mode carrier. It does not identify updates with physical time.

For a single gate M={1}, L=13. A cycle beginning at (0,1) has port list

0,1,1,2,3,4,5,6,7,8,9,10,11.

The spatial phase alphabet has not been enlarged. With alpha^4-alpha^2+1=0, the twelve forward incidence transitions contribute alpha^12=1, and the one dwell contributes 1. The number of updates in a return is thirteen, while the geometric phase remains the original twelve-position observer. Temporal return and geometric phase-step count are distinct.

## 3. Exact local-flux correction to the earlier Euler law

For a positive path population let A and B be the phase sums over idle and moving paths. Write Z=A+B. Define the signed observer

J=sum_(n in M) (idle_mass(n)-moving_mass(n))*alpha^n.

Collision sends (A,B) to (A-J,B+J); streaming then gives

Z_next=A+alpha*B+(alpha-1)*J.

This identity follows by serial/alternative BRC composition; J is not negative positive mass. It identifies the exact closure term missing from the earlier constant-mode formula. Unless J is determined by A and B, those two phase components are not a sufficient predictive state. The term is a model/representation closure correction, not an established physical energy or force residual.

## 4. Six zero samples followed by an echo

Take two moving paths at ports 2 and 8, each weight 1/2, and M={1}. With no gate switch they remain antipodal and have zero phase forever. Under F_M they still have Z_k=0 for k=0,...,5. At k=5 the paths occupy ports 7 and 1. The next update moves the first to 8 but changes the second to idle at 1:

Z_6=(alpha^8+alpha)/2=(alpha-alpha^2)/2 != 0.

The four coefficient output is (0,1/2,-1/2,0). CWM stays (2,1,1/2), all weights remain positive, and no new path is added. The output has period thirteen. The old implication 'two adjacent zero samples imply all future phase zero' was correct for the constant-mode model, but is false under this changed action.

For any population on the active single-gate cycle, its temporal average phase is alpha*W_active/13. Add the fixed-state phase A_fixed for the full average. More generally the average for mask M is

A_fixed + W_active/(12+|M|) * sum_(g in M) alpha^g.

Each active state visits every port once plus each active gate once, so the formula is immediate. This is a time-indexed algebraic observer average, not additional positive mass.

## 5. Complete single-gate permanent-invisibility theorem

Work over rational path weights and the exact four-coefficient alpha observer. Enumerate the thirteen active cycle states in the order above; their weights are r_0,...,r_12. Let A_fixed be the phase sum of the eleven fixed idle states. Then

Z_k=0 for every k >= 0

if and only if there is a rational u such that

r_0=...=r_12=u, and A_fixed=-u*alpha.

Necessity: extract the coefficient of alpha from the active orbit outputs. Its cyclic sequence is

g=(0,1,1,0,0,0,-1,0,-1,0,0,0,1).

The corresponding polynomial is q(t)=t+t^2-t^6-t^8+t^12. It satisfies q(1)=1 and is not a scalar multiple of Phi_13(t)=1+t+...+t^12. Since Phi_13 is irreducible over Q, gcd(q,t^13-1)=1. Therefore cyclic convolution by g is invertible on rational thirteen-tuples. A constant output of this coordinate forces constant active weights. Summing the full alpha-valued cycle gives alpha, forcing the displayed fixed compensation. Sufficiency follows directly by cycling the uniform weights.

The irreducibility used here is the standard prime cyclotomic result, not a novelty claim: Phi_13(t+1) is Eisenstein at 13. Primary background: Tom Moshaiov, An alternative proof for the irreducibility of the p-th cyclotomic polynomial, arXiv:2210.15467. This external result is used for algebraic proof, not as native dynamics input or a numerical fallback.

The inactive eleven-port phase map has rational rank four (ports 0,2,3,11 already span 1,alpha^2,alpha^3,alpha-alpha^3). It has a seven-dimensional kernel. Adding u gives permanent-invisibility dimension eight on the full 24-weight space. The all-future phase-observation rank is therefore sixteen. The constant-mode baseline on the same full domain has rank eight and kernel dimension sixteen. The new kernel is contained in the old one, but nonzero positive permanently invisible populations still exist. These are dimensions of rational distribution/observer spaces, not physical spatial dimensions.

## 6. Exactly ten adjacent phase samples are sufficient, and nine are not

Let O_h be the 4h by 24 rational array obtained by evolving each unit-weight atomic BRC input and recording its four output coefficients at k=0,...,h-1. All its entries are exact integers. For h=1,...,13 the ranks are

4,8,9,10,11,12,13,14,15,16,16,16,16.

The lower bounds are certified by explicit nonzero integer minors, evaluated with a separate Bareiss determinant checker. Kernel basis vectors give independently checked upper bounds. For h=10, a 16 by 16 minor with determinant -1 uses zero-based row indices

0,1,2,3,4,5,6,7,9,13,17,21,25,29,33,37

and column indices in order STATES=((n,b): n=0..11,b=0,1)

0,1,2,3,4,5,6,7,9,10,11,13,15,17,19,21.

Its rank reaches the all-future rank sixteen from section 5, so ten consecutive exact samples determine every future phase output. They do not reconstruct the entire population. If those ten samples are zero, all later phase outputs are zero under this fixed model.

An explicit nine-zero counterexample starts with one unit path in each of the 24 states, adds one at (1,0) and one at (5,1), and removes the one at (3,1). All remaining counts are nonnegative, totalling 25 unit paths. Divide each weight by 25 for total positive mass one. The uniform background is invariant under the permutation and has zero phase. The remaining signed observer contrast is delta_(1,0)-delta_(3,1)+delta_(5,1). Its phase is zero at k=0,...,8 but equals (alpha-alpha^2)/25 at k=9. The actual expanded 25-path realization and its CWM=(25,1,1/25) were checked. This proves nine samples cannot suffice even for positive populations.

The evidence additionally gives every output row over the full thirteen-step period as an integer combination of sixteen selected rows among the first ten samples. All 24 column identities were checked. The largest sum of absolute reconstruction coefficients is 45. Therefore if each sampled coefficient has error at most epsilon, this reconstruction has coefficient error at most 45*epsilon for every future update. This is a conservative certified bound for an algebraic coefficient interface, not an assertion about a physical sensor or an optimal noise constant. Finite-precision near-zero is not exact zero.

## 7. Arrangement, not just number of scatterers, controls invisibility

If M is invariant under n -> n+6, then the antipodal involution A(n,b)=(n+6,b) commutes with F_M. The phase observer changes sign under A. Every equal positive antipodal pair with the same mode consequently stays phase-zero for all updates. This proof applies to all such populations and every future iterate, rather than merely a tested horizon.

Thus M={1,7} protects these zero pairs, whereas M={1,3} need not. Both masks have one fourteen-cycle and ten fixed states, yet their full rational all-future observation ranks are eleven and seventeen. Cycle length and amount of interaction alone do not determine which residual information can be observed.

All 64 subsets of the six gates were checked exhaustively. Grouped by number of gates, the observation-rank distributions are:

0 gates: rank8 (1 layout).
1 gate: rank16 (6 layouts).
2 gates: rank11 (3 layouts), rank17 (12 layouts).
3 gates: rank14 (2 layouts), rank18 (18 layouts).
4 gates: rank11 (3 layouts), rank19 (12 layouts).
5 gates: rank19 (6 layouts).
6 gates: rank8 (1 layout).

Every layout includes exact cycle membership, a nonzero-minor lower bound, independent kernel vectors annihilating all period rows, and rank-nullity verification. Increasing the number of switches is not monotone in observation rank. None of these counts are native-axis dimensions, thermodynamic losses, quantum entanglement or a general scattering classification.

## 8. Verification, scope, and durable next question

The final suite passed 9,759 assertions. It covers every one of 64 gate masks on all 24 atomic states, inverse/locality/CWM/provenance and local-flux identities, all-period observer certificates, antipodal preservation, the six-zero and nine-zero positive echoes, 64 weighted populations through five updates with explicit-path/24-bin CWM comparisons, and the ten-sample reconstruction and error factor.

Actual existing-source CWM calls: cwm_edge 80,009; cwm_propagate 72,710; cwm_recoalesce 43,278. Incidence successor calls: 18,430. The mask extension recorded 35,395 collisions, 33,859 forward steps and 1,536 inverse steps. Counts are assertions/calls, not independent experiments. Earlier 9,479/9,677-check intermediate stages preceded additional rank and reconstruction certificates; they are not independent replications. Prior research suites were consumed without replaying them as new results.

New module brc_local_switch.py SHA256 dd76f8e750d6115f505ccb59b4babb87f93a908448aedf84f8e9d4639b59baf1; Git blob 89eca36e9ab0ee51309bec4770fa92da5456d77c.
New checker check_local_switch.py SHA256 3e59d0026e9204cc4369814dac515d55dc1eef0257a44d720f7b56c9d5af6bc0; Git blob 5d9733f81d3fa361029d68a6cb5b9baa8da25ebb.
Full certificate evidence/summary.json SHA256 9ffb5958b1819784e5e36e188507d5ac1820949010c93deaa4966a4e70e3e261. Run python check_local_switch.py from the conversation evidence package; Python 3.10+, standard library only.

This is a new local mode-switching result, not a retry of any previously safety-blocked incidence note or verification sidecar. Those earlier blocked payloads are neither copied here nor used to claim repaired activity linkage. Source proof storage, full execution-package availability, activity registration and formal mathematical admission are distinct. No formal task or successful final gate is asserted.

Completed unit: a specified local mode-changing BRC interaction, its exact joint transport, changed return cycle, closure correction, permanent-invisibility classification, sharp exact sampling horizon and layout dependence. The actual native-to-port bridge and the physical origin of the static mask remain unproved. The next scientific question is a dynamical local field coupled to the path/mode with an explicit conservation/interaction contract, then analysis of whether the new joint state remains finite and future-sufficient. A collision law cannot be obtained by naming this static mask a force. Spatial propagation and physical time additionally require their own calibrated bridge.
