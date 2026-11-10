# R700b — exact V29 matched-TRANSFER repair and a minimal native-grammar observer counterexample

Date: 2026-11-11 (Asia/Shanghai). Continuation of R700 in Draft PR #2015. Task \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, immutable science pin unchanged. Author-side research; **UNREVIEWED**.

## A. Question

R700 gives a sharp seven-state contrast-only fiber and a reconstruction inverse for positive-BRC histogram \`v=(e,t,c,z)\` encoded as V29 PASS ring at one Cell x. The actual V29 grammar also allows matched boundary TRANSFER events between Cells. Does the local \`(u_x,P_x)\` observer still suffice after such transfers?

## B. Transfer-corrected theorem

Let the source-selected path tokens emit only R700's four ring PASS types inside x. In addition, permit *any finite history* of V29 matched TRANSFER events incident to x, all recorded in its nonnegative \`Rin_x,Rout_x\`. Let \`P_x=Σ M_x[a,b]\`, and retain a separately declared baseline \`P_{x,0}\` if the ledger is not initially zero. Then the corrected local internal contrast

\`u_int := u_x−Rin_x+Rout_x = (e−z,t−e,c−t,z−c)\`

and \`s=P_x−P_{x,0}\` recover the original four source bins exactly by R700's formulas:

\`e=(s+u_int,0−2u_int,1−u_int,2)/4\`,
\`t=e+u_int,1\`, \`c=e+u_int,1+u_int,2\`, \`z=e−u_int,0\`.

**Proof.** V29 defines \`u_x=(M_x−M_xᵀ)1+Rin_x−Rout_x\`. Every matched TRANSFER preserves M and P. Removing the known signed boundary contrast leaves exactly the ring PASS differences; apply R700. This is an equality of integer event ledgers after arbitrary finite matched TRANSFER histories, independent of event serialization for final counts. ∎

## C. Exact V29-grammar counterexample: uncorrected (u,P) loses source identity

Declare a two-Cell typed skeleton x,y with allowed bidirectional same-port connections for ports 0,1,2. Compare these two **different positive BRC candidate token histories**:

History A: source histogram \`v_A=(1,0,0,0)\`. At Cell x, \`PASS(x:0→1)\`, \`TRANSFER(x:0→y:0)\`, \`TRANSFER(y:1→x:1)\`. This yields local \`u_x=(0,0,0,0)\`, \`P_x=1\`; the internal ring contrast is \`(1,−1,0,0)\`.

History B: source histogram \`v_B=(0,1,0,0)\`. At x, \`PASS(x:1→2)\`, \`TRANSFER(x:1→y:1)\`, \`TRANSFER(y:2→x:2)\`. The same local observations \`u_x=(0,0,0,0)\`, \`P_x=1\` result, but the internal ring contrast is \`(0,1,−1,0)\`.

Every PASS and TRANSFER above is an allowed **count-grammar operation on the declared network skeleton**; matched TRANSFER preserves global scalar charge. The histories differ at the full \`(M,Rin,Rout)\` ledger and are restored by \`u_int\`. Thus \`(u_x,P_x)\` *alone* is not sufficient for this enlarged V29 count-event language, even with exactly one source token. This is a scoped predictive-information counterexample, not an obstruction to the P000 X6 mother dynamics.

## D. Actual finite execution and next bridge

\`R700B_V29_NETWORK_TRANSFER_VERIFY.js\` executes the ring contrast plus every choice of one incoming and one outgoing matched transfer on the selected Cell, for **all 43,224 nonempty source histograms** and 16 port pairs, totaling **691,584 exact integer checks**. It verifies recovery via the corrected contrast and the concrete two-history collision. Execution returned \`R700B_BOUNDARY_REPAIR_EXACT_PASS\`.

The mathematical proof covers *any finite number* of matched transfers as long as no extra unencoded PASS is counted in \`P−P_0\`. For full native X6 / V39, still construct an authorized Link/Port packet with active frame, dependency order, based-loop current j and S3 holonomy h. The four-port group identification remains a declared candidate interface pending that native lift. Preserve boundary source/multiplicity and full raw Path/BRC provenance when future operations require them.
