# PREFIX-515 — Exact signed-BRC path composition and reversal lift
Date: 2026-11-05 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.
Researcher-ID: EM-X6-AE330F; activity: RA-1BDA1295B2F2FB1D0A4AD7BB (native session registration).
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Formal task: RS-X6-NATIVE-ROTATION-DYNAMICS, publication TP2-6A1F9D8C2047E3B51C01. Author-side independent result, without formal CLAIM.

## Typed model and question
Use ordered native signed words on the restricted ten-direction X6 alphabet a,A,b,B,c,C,d,D,e,E (five embedded axes of the six-axis Heartbeat World). Native step concatenation uv follows the last cell of u. The formal operator rev(w) reverses *step order*, keeping signs and net signed displacement, without asserting physical reversibility. The c sign-reflection swaps c and C everywhere. The colors are a=0,A=4,b=1,B=2,c=C=3,d=D=e=E=4 and the two KMP gates are aab and aba. Retain exact cancellation pair numbers p_i, BRC readouts V=p_b+2p_d+p_e and W=p_c+p_e, terminal KMP prefix state q_g and first B/C-source tag t in {N,B,C}.

## Theorem A — universal exact BRC cross-boundary cancellation formula
For any two ordered signed words u,v, the number of cancellation pairs on axis i is p_i(w)=(N_i(w)-|y_i(w)|)/2, where N_i counts native axis steps and y_i is their signed sum. Define

k_i(u,v)=[|y_i(u)|+|y_i(v)|-|y_i(u)+y_i(v)|]/2.

Then k_i is a nonnegative integer and

p_i(uv)=p_i(u)+p_i(v)+k_i(u,v),
V(uv)=V(u)+V(v)+k_b+2*k_d+k_e,
W(uv)=W(u)+W(v)+k_c+k_e.

Proof: N_i(uv)=N_i(u)+N_i(v), and y_i(uv)=y_i(u)+y_i(v). Substitute the definition of p_i. The parity of N_i and y_i coincides, so k_i is integral; the integer triangle inequality makes it nonnegative. These equalities hold for every word, independently of step ordering.

## Theorem B — explicit finite transition-signature lift
For a fixed gate g, define delta_g(q,c) to be the longest prefix of g which is a suffix of the gate-prefix represented by state q followed by color c, allowing full-match state 3. Let T_g(w) be the four-entry map sending an *arbitrary* initial q in {0,1,2,3} to the final q after reading word w. Consequently q_g(w)=T_g(w)(0).

Let f(w) be the earliest b/B or c/C source tag (N if none), and let ell(w)=f(rev(w)), the latest source of w. Define

Gamma_g(w)=(n,y,V,W,T_g(w),T_g(rev(w)),f(w),ell(w)).

Gamma is an exact finite-size integer/KMP/source observer supporting the following word operations. For uv the length and displacement add; V,W use Theorem A; T(uv)=T(v) composed with T(u); T(rev(uv))=T(rev(u)) composed with T(rev(v)); f(uv) chooses the first non-N tag among f(u),f(v); ell(uv) chooses the first non-N tag among ell(v),ell(u). Reversal exchanges the two transition maps and f with ell, keeping n,y,V,W. Swapping c/C negates y_c but fixes every other field of Gamma; it commutes with reversal and concatenation.

Proof: Each signed primitive defines an exact four-state transition, so the transition maps compose in word order. The equality rev(uv)=rev(v)rev(u) supplies the reverse-map formula. The source rules are leftmost and rightmost occurrence identities. Theorem A supplies the BRC update. The c/C reflection preserves color and source category for every step, and preserves all cancellation pair counts while negating c-axis net displacement. Thus every field of all three operations is a function of Gamma. All arguments apply to words of arbitrary finite length and both gates.

The signature retains exactly the original observable O_g(w)=(n,y,V,W,q_g,f), obtained as q_g=T_g(w)(0), t=f. It is operation-safe for the declared path algebra: concatenation, formal order reversal and c-axis sign reflection. It is not used to discard native path words or original branch identity when additional future observables are requested.

## Theorem C — smallest reversal-information-loss witness and minimal repair
The original observer O_g is not sufficient for formal order reversal. For both gates,

w1=bbc, w2=bcb,
O_g(w1)=O_g(w2)=(3,(0,2,1,0,0),0,0,0,B).

After order reversal the words are cbb and bcb. They have source tags C and B respectively, hence their O_g observations differ. There is therefore no exact map on O_g alone that realizes reversal on all signed words. Complete finite enumeration of all ten-direction words of lengths 0,1,2 verifies that length 3 is the minimal counterexample for either gate.

For the operation set {identity, reversal}, the coarsest exact reversal-stable refinement of O is O_hat(w)=(O(w),O(rev(w))). Reversal exchanges the two factors. Any observer refining O on which reversal descends must determine O(rev(w)) as well, hence must determine O_hat. This proves minimality by the factorization criterion. Gamma of Theorem B is a constructive fixed-size strengthening of that minimal repair which also supports concatenation.

## Executed certificate and verification scope
The accompanying JavaScript program prefix515_path_signature_certificate.js evaluates native signed paths directly with exact integer cancellation updates and independently calculates KMP transition maps. For each of aab and aba it exhaustively checks 11,111 original words (length 0..4) for reversal and c-sign reflection, all 54,321 ordered pairs (total length 0..4) for the composition identity, all same-observer fibers of lengths 0..2 for minimality, and the explicit length-3 split witness. Executed output: PREFIX515_EXACT_EXECUTION.json, ALL_CHECKS_PASS. The unlimited-length results rest on the algebraic proofs; enumeration checks their finite implementation.

## Next
PREFIX-516: select one frozen published C6 native microtrace, define a typed action on ordered signed primitive words or branch families, and check its exact descent through Gamma. For a failed fiber-constancy test, retain both native witnesses, derive the necessary additional state and retest. The mother objective of native six-axis physical rotation generators and triadic closure remains open.

Applicable references: p000_reality_foundation.json; definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json; definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json; docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context; docs/PORTABLE_RESEARCH_PROTOCOL.md; docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md; research_constraints/heartbeat_brc_only.json; research_notes/portable_direct/2026-11-05_prefix514_signed_c_reflection_W_prefix.md.
