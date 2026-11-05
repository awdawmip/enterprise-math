# PREFIX-523 — Exact aAc–BRC gate correlations on the symbolic four-STAR X6 graph

Date: 2026-11-06 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Parent: RS-X6-NATIVE-ROTATION-DYNAMICS; Researcher-ID EM-X6-BF46CB, Activity RA-8200C6019A815A362DBBC5D1.
Frozen scientific source: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Method and current norms: docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context; P000 V5 and ACTIVE Heartbeat World; docs/PORTABLE_RESEARCH_PROTOCOL.md; research_priorities/research_method.json; native BRC constraints. Prior results used: PREFIX-518, 520, 522.

## Defined population and observables

Use the PREFIX-518 symbolic four-STAR directed graph with K4 edges L1=AB,L2=CD,L3=AC,L4=BD,L5=BC,L6=AD and STARs A={L1,L3,L6}, B={L1,L4,L5}, C={L2,L3,L5}, D={L2,L4,L6}. A phase s=(STAR,prev,current) has opposite-sign previous/current phases on different axes. There are 48 states, each with three successor phases (one non-backtracking stay, two STAR switches). For each s->t, with old=current(s), new=current(t), retain the two distinct native signed-X6 primitive microtraces INNER=(-old,new) and OUTER=(new,-old). Count all 48*6^d labeled d-macro histories, including their individual branch identities and native intermediate Cells.

For each of the 24 K4/S4 chart relabelings h, define the original signed-axis color gate aAc by positive h-L1 -> a, negative h-L1 -> A, both signs of h-L3 -> c, and all other axes to other/filler colors. H_h(w) counts all indexed completed aAc occurrences from KMP q0=0. The signed primitive counts on axis i are N_i^+ and N_i^-, with the exact BRC opposite-sign pair count

    p_i(w) = min(N_i^+,N_i^-) = (N_i^++N_i^- - |N_i^+-N_i^-|)/2.

This remains an X6 signed-path, provenance-retaining observer; no physical rotation-selection or native time law is assumed.

## Theorem 523-A: exact BRC lower bound and branch-invariant pair counts

For every admissible phase itinerary, the full six-axis pair vector p is independent of the selected INNER/OUTER labels; furthermore for every chart h and history w,

    0 <= H_h(w) <= p_(h-L1)(w).

Proof: each macro's two branch paths have identical signed primitive multisets {-old,new}, so their signed counts, displacement and pair-count vector are identical. A hit aAc contains one positive and one negative h-L1 step in adjacent macros. The literal word aAc has no nonempty proper border, hence distinct occurrences have disjoint primitive character positions. Consequently H hits require at least H distinct +h-L1 and H distinct -h-L1 steps, so p=min(N+,N-) >= H. This proves support condition [z^j u^r]sum_w z^H u^p=0 for j>r.

## Theorem 523-B: sharp exclusion and spacing

Let T_h=(S_h,+a_h,-c_h) denote the unique signed phase identified in PREFIX-522, where S_h is the unique STAR containing the h-L1 and h-L3 preimage axes. For t>=2 an aAc hit ends at macro t if and only if s_t=T_h and beta_(t-1)=beta_t=INNER.

If t<t' are any two hit indices then t'-t is even and >=4. Hence for all d>=0:

    H_h(w) <= floor((d+2)/4).

Proof: phase-current signs alternate, while a hit ends on a negative phase, forcing even separation. A length-two return from T_h is impossible: immediately after T_h the current phase cannot be +a_h. The nonbacktracking same-STAR successor excludes its previous +a_h, and a switch via c_h enters the other c_h STAR, which cannot also contain a_h since the two K4 edges share one and only one STAR. But the phase preceding T_h must have current +a_h. Four-step returns exist: the precisely specified PREFIX-520 phase graph has a_2=5 four-step closed itineraries at every state. Fixing INNER at the first and last two macros of a six-macro path with such a return gives two hits at positions 2 and 6; so the separation is sharp.

Explicit original-chart d=6 witness:
Phases [[0,3,-6],[0,-6,1],[0,1,-3],[0,-3,6],[3,6,-4],[1,-4,1],[0,1,-3]];
branch labels [0,0,1,1,0,0];
native signed word [6,1,-1,-3,6,3,-4,-6,4,1,-1,-3];
full color word "_aAc_c___aAc"; hits at macro 2 and 6; p=(2,0,1,1,0,1).
All phase transitions, signed microsteps, and both hits were checked by exact code.

## Theorem 523-C: infinite exact second factorial moment and rational series

Let a_m be the number of unbranched phase returns of length 2m to one fixed phase state (PREFIX-520). The first terms are a0=1,a1=0,a2=5,a3=28,a4=297; the exact recurrence is

    a_(m+5) = 5a_(m+4)+26a_(m+3)+78a_(m+2)+135a_(m+1)-243a_m.

For the entire population of 48*6^d labeled histories define E_d=sum_w H_h(w) and B_d=sum_w binom(H_h(w),2). Then for all d>=0:

    E_0=E_1=0; E_d=9(d-1)6^(d-2) for d>=2;

    B_d = sum_(m=2)^floor((d-2)/2) (d-2m-1)*2^(2m-4)*a_m*6^(d-2m).

Proof: mark hits at t and t+g, g=2m>=4. Because each phase has three incoming ports and every initial phase is counted, there are 3^t phase prefixes ending at T_h. The first hit fixes two branch labels, leaving 2^(t-2) choices. Between the two targets, the phase itinerary has exactly a_m possibilities. The second hit fixes the last two branch labels of these g macrosteps, leaving 2^(g-2) interior labels. Subsequent suffixes have 6^(d-t-g) independent labeled continuations. Their product simplifies to 2^(g-4)*a_m*6^(d-g), independent of the first hit index t. There are d-g-1 possible first indices t in [2,d-g]. Sum over all even g>=4. Extra hits are allowed: binom(H,2) counts each marked pair exactly once. E_d is the independent single-window formula of PREFIX-522.

Writing A(x)=sum_(m>=0)a_m*x^m, the exact PREFIX-520 formula is

    A(x)=(1-5x-21x^2-75x^3-108x^4)/
         (1-5x-26x^2-78x^3-135x^4+243x^5).

Thus both factorial moments have explicitly rational ordinary generating functions:

    sum_(d>=0) E_d t^d = 9t^2/(1-6t)^2;

    sum_(d>=0) B_d t^d = [9t^2/(4(1-6t)^2)]*[A(4t^2)-1].

The second denominator has degree at most 12, yielding an exact recurrence of order at most 12. This is not a minimal-order claim. In particular B6=180. As d=6 permits at most two hits, exactly 180 of 2,239,488 labeled d=6 histories have H=2.

## Theorem 523-D: operation-safe exact gate/BRC coefficient transfer

Let u,v mark the *separate positive and negative signed* primitive counts on the h-L1 axis. On every phase edge s->t define the branch-independent monomial

    m_h(s,t)=u^[number of +a_h steps in (-cur(s),cur(t))]
             * v^[number of -a_h steps in (-cur(s),cur(t))].

Use 96 persistent macro-boundary states (s,beta) plus an initial sentinel label. For transition (s,b)->(t,c), multiply by

    m_h(s,t)*z^[b=0 and c=0 and t=T_h],

with the exponent set to zero on the first macro. Sum all paths from the 48 initial phase states, and sum all final states. The resulting polynomial equals

    G_d(u,v,z)=sum_(all labeled histories w) u^{N_a^+(w)}v^{N_a^-(w)}z^{H_h(w)}.

This follows bijectively: each history uniquely determines its phase/branch transitions; monomial products add the true signed X6 primitive counts, and the gate exponent is precisely the PREFIX-522 local indicator. The final exact BRC joint readout is

    F_d(z,r)=sum_(i,j>=0:min(i,j)=r) [u^i v^j]G_d(u,v,z).

The min-readout must occur after the product; applying it to edges would miss cross-boundary BRC cancellation. Twelve signed-count variables on the same 96-state transfer retain the full six-axis BRC pair vector. For a fixed single-axis joint histogram, each macro visits that axis at most once, so N+ + N-<=d; a depth-d coefficient DP has O(d^3) integer counter entries and computing all depths through d uses O(d^4) integer additions, versus 48*6^d explicit labeled paths. Integer bit lengths remain part of actual cost. The phase/branch source path and indexed Cell histories remain available for stronger declared observers.

## Executed verification and handoff

The independently run Python exact-native certificate and its complete stdout (including all (H,p) histograms) are in the accompanying local evidence archive PREFIX523_COMPLETE_EVIDENCE.tar.xz; the repository also contains an independently executed small JavaScript exact-integer certificate and complete JSON stdout, named prefix523_compact_certificate.js and PREFIX523_COMPACT_EXECUTION.json. Verification scopes:
- All 48 directed states, 24 charts and 41,472 two-macro histories checked for the local hit criterion and signed-pair branch invariance.
- All native signed primitive histories d=0..4 compared with the weighted 96-state exact BRC transfer by independent enumeration (Python); all 24 frames agree on their d=4 joint event/BRC histogram.
- PREFIX-520 phase returns a0..a8 and the finite recurrence checks; second-factorial formula versus exact coefficient DP for d=2..10.
- Every chart's phase return T->T is 0 at two macros, 5 at four macros. An explicit two-hit native signed word is checked.
- Output: ALL_CHECKS_PASS. For d=2,4,6,8,10 respectively, (sum H, sum binom(H,2)) equals (9,0),(972,0),(58320,180),(2939328,23472),(136048896,1772928).
- Any independently reviewed theorem admission or verified physical rotation law remains a separate task.

Next PREFIX-524: derive a minimal recurrence or state-space factorization for the rational pair-correlation generating series and the full higher-event distribution; search for two phase histories with identical six-axis signed BRC counts but distinguishable future gate/source behavior. Continue the mother objective of arbitrary triad C6 and physical native X6 rotation-selection dynamics under its separate frozen proof conditions.
