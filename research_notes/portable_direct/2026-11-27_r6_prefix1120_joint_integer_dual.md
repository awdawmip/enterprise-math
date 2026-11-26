# PREFIX-1120 — joint integer-dual exclusion of pair and triple near hits

2026-11-27. Own EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322, original registration r6-20261123-2358-session-start-own-v1 verified SUCCEEDED. LEASED read r6-20261127-0648-leased-read SUCCEEDED, error=null, snapshot as of 2026-11-26T22:49:43.430597Z, tasks=[]; no new CLAIM, no shared task mutation. Author proof, NOT_REVIEWED. Continuing the independent directed Stage46 frontier.

Frozen inputs: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d, joint observer and X6/time companions. Same signed BRC carrier as PREFIX-1119 (chart O, incoming -e1, signed reversal -5 with phase cover 5q, other weights 1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives). Retain cell, port, sign/phase, branch order and multiplicity. The present calculation is auxiliary arithmetic on the inherited BRC boundary certificate, not a new native propagation, native plane, or classical physical comparison. The 8400/8800 anchor process exits remain unconfirmed. Parameter box is conditional on inherited certificates. No new anchor or CT evaluation.

Parent: 26bb7627e794f4081e3b4002ce78cb1743581224:research_notes/portable_direct/2026-11-27_r6_prefix1119_cubic_cluster_lacunarity.md. Curvature and signed two-hit identity: PREFIX-1117/1118 as pinned by that parent. Exact parameter input: 897771dcc60212121f1e222bf139da189cce0078:research_notes/portable_direct/2026-11-27_r6_prefix1117_root_8800_result.json, Git blob e03d50ec3c79588577e8aaef7e194adf7562f2c8, SHA256 367ed5c982ef92405623cfe6633aa29ce1449bfa2e1cb2e355fd8692d84355a9. All seven entries of the prior PREFIX-1119 evidence manifest verified locally. The exact input is unchanged. The inherited finite sweep gives at most one true near hit on [10^8,M), M=16225927682921336339157801028812800000000; it is not rerun in this unit.

## 1. Pair relation and all-future small denominator exclusion

Write f(m)=rho*m+c+d/m, d>0, and e_m=f(m)-j_m with |e_m|<=E/m^2, E=400000. For two distinct true near hits a<b in [L,2L), let their primitive integer line be q*j-p*m=h, gcd(p,q)=1, q>0. Thus b-a>=q and all signs and the intercept h are retained. Set delta=rho-p/q and gamma=c-h/q. Direct elimination yields
delta=d/(ab)+(e_b-e_a)/(b-a),
gamma=-d*(1/a+1/b)+(b*e_a-a*e_b)/(b-a).
Consequently q*|delta|<=(d_u*q+2E)/L^2.

Let R=[rho_l,rho_u], C=[c_l,c_u], T=[d_l,d_u] be the exact frozen intervals. Take P=72486411641368782354423090020719211170157, Qw=3380890274893182433251695995418378677023, Q0=544447235321021556325566186117974922692. The fraction P/Qw is reduced and Qw>Q0. Put eta=max_{r in R}|r-P/Qw|. For any reduced p/q with q<=Q0, rational separation gives q*|rho-p/q|>=1/Qw-Q0*eta. The verifier proves the exact strict inequality
1/Qw-Q0*eta-(d_u*Q0+2E)/M^2>0
(approximate margin 2.874838878174103e-79).
Thus every pair in every window with L>=M has q>=qmin=Q0+1. On the fixed doubling grid starting at 10^8, no pair exists in windows before M by the inherited finite sweep. This raises the global future minimum primitive pair denominator from the earlier small-q certificate. It is not a claim of complete separation.

For q>=qmin>16E/d_l, define K=9*d_u/8, J=16E/d_l, H=2*d_u+4E/qmin. The signed pair identities give 0<delta<K/L^2 and |gamma|<=H/L. Indeed the slope residual is at most 2E/(q L^2)<d/(8L^2), and the intercept residual at most 4E/(q L). For any triple window the inherited collinearity and curvature inequalities imply q^2<=J L. The determinant hypotheses at L0=10^8 are verified again by the exact script.

## 2. General integer-dual certificate

Let x=(rho_l+rho_u)/2, y=(c_l+c_u)/2 and wr,wc their half widths. Suppose a class of integer relation triples (q,p,h), with 0<q<=Q, obeys
|p-x*q|<=ep, |h-y*q|<=eh.
For any three independent integer linear forms with rows (A_i,B_i,C_i), define
T_i=Q*|A_i+B_i*x+C_i*y|+|B_i|*ep+|C_i|*eh.
If all T_i<1, the class is empty. Proof: A_i*q+B_i*p+C_i*h is an integer with absolute value <=T_i<1, so each is zero. Independence forces (q,p,h)=(0,0,0), contrary to q>0. This is an exact obstruction certificate; finding the forms and verifying them are separate. No approximation of signs, collapse of intercept, or assertion about native coordinates is needed. The strict inequality is essential.

For triple windows with L>=M and qmin<=q<=Q, curvature gives L>=q^2/J. The pair identities then yield
|p-x*q|<=Q*wr+K*J^2/qmin^3 = ep,
|h-y*q|<=Q*wc+H*J/qmin = eh.
The bound is simultaneous: the same q appears in both coordinates. This retains information that separate rational approximation tests discard.

## 3. Explicit unimodular witness and Stage46 consequences

Set Q=18*10^50. Three rows were found by weighted exact rational lattice reduction on the joint rho,c midpoint lattice. The following independently checkable integer rows, rather than the correctness or exit status of any reduction library, are the proof certificate:
(13241695572016246280452795405,-614903515325433031059117378,-586453816401334287434546)
(1182616791650392258028253444,-74796824988556406807726418,4246778208283374384362279)
(-7752265403315380654172299023,382363756442351370763912993,-4494886358260478563501531)

The exact integer determinant is +1. The three exact Fraction bounds T_i are strictly less than 1; decimal displays only:
0.6932114563241172, 0.8111320093434606, 0.9838996543787506.
Therefore no triple window with L>=M has q<=Q. Combining with q^2<=J L gives the exact necessary lower bound L >= (Q+1)^2/J, approximately 4.905999221443534e96. The first admissible start on the fixed doubling grid at or above this bound is approximately 6.365737426045269e96 (exact integer in verifier output). Applying PREFIX-1119 to that start, the second DISTINCT triple slope has start at least Ldy^3/(18E)^2, approximately 4.976009144118182e276. These are lower bounds on hypothetical occurrences, not records of actual hits. The previous first possible triple start on this grid was M and the previous second-distinct-slope lower bound was approximately 8.24e106.

For all pair windows with L>=10^80 (without a triple/curvature premise), instead take ep=Q*(wr+K/10^160), eh=Q*(wc+H/10^80). The SAME three forms have exact bounds <1, displayed as 0.6934160392986138, 0.8126134874983977, 0.9854676844528663. Thus every such pair has q>Q, hence b-a>Q. This excludes short-gap pairs on the unbounded tail, not arbitrary pairs. In general, for any pair the integer-dual criterion gives a scale-dependent necessary condition with ep=q*(wr+K/L^2), eh=q*(wc+H/L); at least one form must reach absolute bound 1. This is a joint arithmetic observer on the signed BRC spectral parameters and not a new BRC computation.

## 4. Actual exact verification and remaining work

Executed Python Fraction verifier, input bytes matched the pinned Git blob; all assertions passed. The weighted reduction was used only to discover the integer witness; the fixed-row verifier uses only Python standard library and no LLL dependency. The first trial using a library reduction raised AssertionError; a small exact rational reduction supplied the rows, which were then verified independently as integer forms. No claim about that library's general correctness.

Exact verifier source: 61a09069e50b1ebded9e1d94c9a4db66d132ff98:research_notes/portable_direct/2026-11-27_r6_prefix1120_joint_dual_verify.py, Git blob ae7fb4b226050fd21fbe44b86886e9267b1b6d59, SHA256 cb78bea9e44d4ec3be69dd45d1df982ab0f6d9e0d4e1f0a412906bd3eccb3369. Put the pinned parameter JSON beside it as root_8800_result.json and run python <verifier>. It writes complete rational endpoints, rows and bounds to prefix1120_result.json; SHA256 of actual result d07ecef97cb0974f6ec6810115899f7e18cfbbcbbf115aaf041f253ed983997d. Actual log:
qmin 544447235321021556325566186117974922693 small q margin 2.874838878174103e-79 det 1
triple bounds 0.6932114563241172 0.8111320093434606 0.9838996543787506
pair bounds 0.6934160392986138 0.8126134874983977 0.9854676844528663
first triple L 4.905999221443534e+96 first dyadic 6.365737426045269e+96 second distinct dyadic 4.976009144118182e+276

Next: exploit parameter correlation rather than axis-aligned intervals in the dual bound; derive a sharper pair-gap profile, and refine rho-only precision by factor >=24209 to resolve the 122 pending candidate signs. The current continuous integer endpoint formula remains certified only up to 4265326180744162387203315935318273935179 exclusive, conditionally as before. All-scale eventual separation, isolated hits, exact-zero classification, remaining spectrum and mother B_fix,odd(32) open. Independent review, inherited anchor exit confirmation, and Activity observation audit pending. No new claim or mathematical acceptance.
