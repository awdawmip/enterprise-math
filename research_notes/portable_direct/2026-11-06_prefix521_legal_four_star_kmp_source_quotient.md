# PREFIX-521 — Exact future-safe KMP/source quotient on legal four-STAR BRC paths

Date: 2026-11-06 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Parent task: RS-X6-NATIVE-ROTATION-DYNAMICS, independent author-side result (no formal CLAIM).
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Immediate published predecessors: PREFIX-518 a51bb9bf8071f90d95e0e0ffa956dde8f27901fa; PREFIX-519 bfadaef7382c782f04638930b2ccd7e8c3e1516c; PREFIX-520 7d8e61b5c19700bfcb522f64d0f6bc59db5ebd72.

## 1. Exact BRC history population and declared readout

Work in the full six-native-axis signed-X6 Cell torsor, relative to a chosen Cell anchor. The frozen FCC/K4 atlas has L1=AB, L2=CD, L3=AC, L4=BD, L5=BC, L6=AD. Each STAR is the triple of edges incident to one K4 vertex. PREFIX-518 defines a symbolic candidate switch relation on 48 directed phase states (STAR, previous signed phase, current signed phase), with three next phase exits each. Each macroedge a->b has a and b on distinct axes in one common STAR and opposite signs; its two exact shortest native BRC microtraces are (−a,b) [INNER/pivot] and (b,−a) [OUTER/a+b intermediate Cell]. Macroedge branch labels are retained by the original history for indexed Cell queries. This symbolic relation does not select a physical native rotation law.

The PREFIX-519 observer in chart h in S4 maps positive L1 to color a, positive L2 to b, both signs of L3 to c, and other signed letters to their declared filler colors. Either sign of L2 is source B; either sign of L3 is C; the other axes are N. In every chart, the gates are aab and aba with four-state KMP machines. For this theorem the KMP machine begins at q0=0. We query the final q and the first/last non-N B/C source after any finite legal future macroedge continuation and any one of the 24 chart relabelings.

## 2. Exact restricted KMP theorem

**Theorem A.** Let w be any history from zero or more compatible candidate macroedges, with arbitrary choices among their two native BRC microtraces. For every h in S4 and both gates g∈{aab,aba}, KMP from q0=0 satisfies:

  q_g(R_h w)=1 if the final signed primitive letter of w is positive and its unsigned axis is carried to L1 by h, and q_g(R_h w)=0 otherwise.

At every primitive prefix of every such history, q is in {0,1}. In particular the full-match state 3 is not reached by either gate at any legal history length.

**Proof.** Both primitive letters in one macroedge have the same sign, since the phase signs of a and b are opposite. Adjacent macroedges have opposite signs because the next macroedge starts from b and its next phase has sign −sign(b). Each positive two-letter block uses two distinct axes incident to the same STAR, so contains neither aa nor ab: aa would repeat an axis, and ab would require disjoint K4 edges L1=AB and L2=CD to share a STAR. Each negative block contains neither a nor b. Across neighboring blocks the signs differ, so their two-letter boundary also cannot be aa or ab. Every S4 vertex permutation preserves signs, STAR incidence and disjointness of L1/L2. Thus each relabeled word avoids both length-two gate prefixes aa (for aab) and ab (for aba), including at all primitive prefixes. The longest gate-prefix suffix can only be the one-letter prefix a, attained exactly when the final letter is positive chart-L1; otherwise it is the empty prefix. QED.

Example of reachable q=1: a candidate outer microtrace (L6,L1) colors as (filler,a) in the identity chart. Counter-scope example: the unrestricted native signed word (L1,L1) has aab KMP q=2; this theorem concerns the legal four-STAR macrotrace language.

## 3. All 24 frame source readouts from two six-axis orders

For any signed primitive word w (not necessarily legal), define F(w) as the distinct unsigned native axis IDs in order of first occurrence; define L(w) as the distinct unsigned native axis IDs in order of last occurrence when scanning from right to left. Each list has length ≤6. Signs can be erased **for this source-order readout alone**, because source B/C ignores direction sign.

For a given chart h, let b_h and c_h be the respective preimage axes of L2 and L3. Let select(E,b,c) read the earliest member of {b,c} appearing in list E, output B when it is b, C when it is c, N if neither appears.

**Theorem B.** For every finite primitive word, first and last source selectors in each frame obey

  f_h(w)=select(F(w),b_h,c_h),  ell_h(w)=select(L(w),b_h,c_h).

For all words u,v, with ⊙ denoting order-preserving concatenation followed by removal of later duplicate axes,

  F(uv)=F(u) ⊙ F(v),  L(uv)=L(v) ⊙ L(u).

**Proof.** An axis first occurs in uv at its first occurrence in u if present there, otherwise at its first occurrence in v. This gives the first formula. Its last occurrence is in v if present there, otherwise in u, giving the second. Comparing the two selected axis arrival orders is exactly the earliest/last B/C definition. QED.

## 4. Unbounded-horizon observer-safe factorization

For macroedge-aligned legal paths retain (initial phase, final phase), full six-axis displacement y, full six-axis BRC pair vector p, antisymmetric area A where needed, the two occurrence orders F,L, and first/last signed primitive letters (or empty sentinel). Then Theorem A recovers all 24 gate terminal states from the last signed letter. Theorem B recovers all 24 first/last B/C sources. Under a compatible future macroedge continuation, F and L update by ⊙, and the signed endpoint letters are inherited from the corresponding first/last nonempty part. Chart relabelings simply permute the axis IDs. Consequently these outputs factor through the reduced carrier for *every finite legal continuation*, a future-operation-safe right congruence with the exact phase-boundary typing.

The independent native BRC data compose by the previously proved identities:

  y(uv)=y(u)+y(v);
  p_i(uv)=p_i(u)+p_i(v)+(|y_i(u)|+|y_i(v)|−|y_i(u)+y_i(v)|)/2;
  A(uv)=A(u)+A(v)+y(u)∧y(v).

The quotient replaces 24 complete KMP transition-function records and 24 raw source selectors by two lists of at most six native axis IDs and the signed boundary letters for this declared observer. It is also exact under chart relabeling. Finite list updates take bounded operations; integer bit lengths for y,p,A increase with history size.

This proof covers output after KMP initialization at q0 and all compatible future macroedge continuations. Arbitrary-initial-state transition functions, free insertion of arbitrary native letters, and indexed historic intermediate Cell queries require their stronger original records. The original native BRC branch provenance remains available for those queries; the present reduction does not identify distinct native paths.

## 5. Executed exact integer checks

Certificate: research_notes/portable_direct/prefix521_four_star_legal_kmp_certificate.py.
Capture: research_notes/portable_direct/PREFIX521_EXACT_EXECUTION.json.
Runtime: Python 3 standard library, signed integer axes, exact symbolic native two-step branches; no floating point.

The executed program constructs all 48 directed phase states from K4 incidence, all 288 outgoing branch-labeled microtraces, all 24 S4 relabelings, and both literal four-state KMP machines. It exhaustively traverses macroedge depths 0,1,2,3 from every starting phase: respectively 48,288,1728,10368 histories (total 12,432). Results: ALL_CHECKS_PASS; 596,736 direct KMP comparisons, 298,368 frame source comparisons, 12,384 incremental order merges and 288 two-step native BRC branch assertions.

Theorem A and B are algebraic/word-structural for all finite lengths. The bounded exhaustive certificate checks the actual implementation and small legal histories; it is not used to extrapolate unbounded validity.

## 6. Next executable scientific question

The two inherited KMP gates are never triggered on the legal PREFIX-518 candidate language. Next select a *reachable* chart-covariant short gate (for example a gate incorporating a sign-sensitive negative-native-axis letter) and explicitly construct a legal occurrence. Then ask for the minimal sufficient phase-aware KMP/BRC future transducer, test Myhill–Nerode distinguishability of states and retain original indexed branch history for stronger observers. Separately continue the parent task's arbitrary-triad signed C6 generators and physical rotation-selection law.

Provenance: frozen P000 and VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md; current docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context, docs/PORTABLE_RESEARCH_PROTOCOL.md, research_priorities/research_method.json, active Heartbeat World / observation-preservation contract, and PREFIX-518/519/520. The actual gateway identity status returned BACKEND_IDENTITY_CHECK_UNAVAILABLE while the native task control query succeeded and reported READY / NEEDS_DISPATCH, owner taskbook/unassigned (observed 2026-11-05T18:48:05Z). A session-start request was queued; authenticated activity completion is not asserted by this author-side paper.
