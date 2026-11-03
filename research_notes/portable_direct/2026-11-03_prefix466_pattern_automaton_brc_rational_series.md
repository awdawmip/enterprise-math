# PREFIX-466 — Exact pattern-gated X6 BRC automata, minimal history repair and rational weighted generating series

Date: 2026-11-03 (Asia/Shanghai). Claim type: **author-side analytic proof with executable exact-integer regression**. Review/admission: pending. Continuation: PREFIX-465 at \`3da723e83f38863417e3ce0a2a9f76ff9e6d6ee1\`. Frozen scientific pin retained: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.

## Scientific object and observer

Retain P000's native signed X6 path steps and the P000/ACTIVE joint-provenance discipline. This independent positive-BRC source model has eleven permitted step *symbols* \`x=+e1, ±e2,...,±e6\`; it is a typed path-language restriction over those native directions. For each ordered word retain its endpoint (in a chosen affine chart), exact positive rational multiplicative weight, and integer path multiplicity. The modeled future operation is append a legal step; the readout is the exact endpoint/product-weight/multiplicity histogram over declared extensions. Full native path order remains available in the source ensemble; the quotient below is certified only for this observer and this extension language.

Choose the gate word \`w=a b\` with \`a=+e2\` and \`b=+e3\`. The first step has no gate (in particular initial x is allowed). At every later step, \`x\` is legal precisely when the immediately preceding two steps are \`a,b\` in order. All ten non-x directions remain legal. Unlike PREFIX-465's last-a permission, this gate tests a *two-step* ordered suffix. This is a new future language with a separate observer certificate.

## Theorem A: exact rational generating function, arbitrary pattern length

Let B be any finite non-x alphabet (not necessarily distinct native directions), let x be a special letter, let \(w=w_1\cdots w_k\in B^k\) with \(k\ge1\), and assign each symbol a commuting weight in a commutative characteristic-zero ring (or positive rationals). Put \(S=\sum_{b\in B}\omega_b\), \(\chi=\omega_x\), and \(c=\chi\prod_{j=1}^{k}\omega_{w_j}\). The first letter x is unrestricted; each later x requires the immediately preceding k symbols to equal w. For all lengths, the exact weighted-word generating series equals

\[
\boxed{F_w(z)=\sum_{n\ge0}\Big(\sum_{u\ {\rm legal},\,|u|=n}\omega(u)\Big)z^n
=\frac{1+\chi z}{1-Sz-cz^{k+1}}.}
\]

**Proof.** First require x to obey the suffix gate even at the beginning. Every such word has a unique decomposition into a sequence of blocks \(v_1w x,\ldots,v_tw x\) followed by an unrestricted final \(v\in B^*\), because cutting immediately after each x is unique and w is exactly the last k non-x letters before it. The generating weight of a block ending in x is \(c z^{k+1}/(1-Sz)\), and the final B-only tail contributes \(1/(1-Sz)\). The geometric series is exactly \(1/(1-Sz-cz^{k+1})\). The actual first-letter exception adds the disjoint family \`x\` followed by a suffix-gated word, contributing \(\chi z/(1-Sz-cz^{k+1})\). Summing proves the identity as a formal power-series relation. The argument does not require w to be unbordered. QED.

For unweighted eleven-direction paths, \(S=10,\chi=c=1\). Thus **for every fixed gate pattern of length k** the legal ordered-path counts satisfy
\[
F_w^{\rm count}(z)=(1+z)/(1-10z-z^{k+1}).
\]
For the explicit native X6 \`ab\` example, assign positive-direction weights (6,12,18,24,36) to \`(+e2,+e3,+e4,+e5,+e6)\`, all other directions weight one. Then \(S=101,\chi=1,c=72\), so
\[
F_{ab}^{\rm weighted}(z)=\frac{1+z}{1-101z-72z^3}.
\]
The coefficient recursion is \(T_0=1\), \(T_n=S T_{n-1}+c T_{n-k-1}+\chi[n=1]\), with \(T_j=0\) for \(j<0\). This is a **mass/word-count observer**; it is not substituted for the full endpoint-weight histogram.

## Theorem B: minimal automaton and suffix-provenance repair

For the post-initial gate on an arbitrary word \(w\in B^k\), define q to be the maximal length \(i\in\{0,\ldots,k\}\) such that the length-i prefix of w is a suffix of the current word. Reading each non-x symbol updates q by exact prefix/suffix matching (the KMP prefix automaton); x is eligible exactly in state k and, when taken, resets q to zero because x is absent from w. This \(k+1\)-state carrier suffices for *all future horizons*. All \(k+1\) states are pairwise distinct as future-eligibility languages: for \(i<j\), append the remaining tail \(w_{j+1}\cdots w_k\) followed by x. It is legal from state j, while from state i the suffix w cannot be formed in fewer than \(k-i\) new non-x letters (otherwise the old word would have ended with a longer-than-i prefix of w). Therefore the post-initial machine has exactly \(k+1\) Myhill–Nerode classes. An exceptional first-position x may require an extra initial state for general w.

For \`w=ab\` with \(a\ne b\), the exceptional empty-prefix behavior is equivalent to matched state 2: both permit x and have the same transitions on every non-x symbol. A **three-state machine** handles the whole language, with q0=neither a suffix nor ab, q1=ends a, q2=ends ab (or the special empty start); on a set q1, on b set q2 iff previous q1 else q0, on other non-x set q0, and on x allow q2 then reset q0.

## Theorem C: exact two-bit repair is necessary in one native endpoint fiber

Take three source words \`abc\`, \`bca\`, \`cab\`, where c=+e4. Each has length 3, native endpoint \(+e2+e3+e4\), zero paired-cancellation count, identical valuation coordinates A=C=0 from PREFIX-465, and individual product weight \(6\cdot12\cdot18=1296\). Yet the suffix-automaton states are respectively q0,q1,q2.

For future readout at horizon H=0, the three histories have one class; for H=1 they have **two** classes (q2 permits x, q0/q1 do not); for any H≥2 they have **three** classes (q1 admits \`bx\`, q0 does not; q2 admits x immediately). The separation is witnessed by endpoint-typed positive-weight continuation histograms: a future \`bx\` (and, for exactly longer horizons, \`bx c^{H-2}\`) has one +e1 and no +e2, hence cannot be generated from q0 without acquiring an a-prefix. Consequently this particular native-base fiber requires 0,1,2 additional fixed-width history bits at horizons H=0, H=1 and H≥2 respectively. Two bits suffice via q∈{0,1,2}; the lower bounds follow from distinguishability. This is a genuine provenance repair on top of endpoint, exact weight signature and path length, rather than an assertion of unrestricted global state minimization.

## Certified descent and implementation

For the explicit native X6 positive-weight model, reuse PREFIX-463/465's exact pair-valuation signature:
\(p_j=\min(n_j^+,n_j^-)\) for the five *paired directions indexed j=1,...,5*, 
\(A=p_2+2p_4+p_5,\ C=p_3+p_5\), \(p=\sum_jp_j\).
For chart relative signed net vector y, x-count s and word length n, \(p=(n-s-\sum|y_j|)/2\), and
\[
W=\big(\prod_{j=1}^{5}\rho_j^{\max(y_j,0)}\big)6^p2^A3^C,
\quad\rho=(6,12,18,24,36).
\]
An appended signed native axis step updates y and adds the corresponding valuation column precisely when it closes an opposing-pair count; appending x increments s. The three-state q transition above handles ordered-source future legality. Hence state \((n,s,y,A,C,q)\) exactly propagates endpoint, each product weight and integer multiplicity by induction, for all future horizons within this language. The state is a typed observer quotient; any additional operation dependent on more of the ordered source must retain suitable further provenance.

## Exact executable verification and cost scope

Run the accompanying standard JavaScript BigInt program \`prefix466_pattern_gate_certificate.js\` with Node.js 18+. It independently compares full ordered-word enumeration with aggregated native X6 BRC histograms for all n=0..5, evaluates exact state recursions through n=8, reconstructs every state's integer product weight, and checks unweighted/weighted generating-function coefficients at each n. Four generic B-word patterns \`a\`, \`ab\`, \`aba\`, \`aa\` are exhaustively checked with independent weighted full-word enumeration for n=0..6. The same projected-base three-witness fiber is checked at n=3. Exact integer arithmetic makes each checked finite-domain equality exact; the all-k theorem follows from the preceding decomposition proof.

Computational state aggregation here preserves weighted integer multiplicity and costs O(11×number_of_reachable_aggregated_states) per step plus exact integer bit-arithmetic; these counts do not assert a native physical performance or phase-amplitude gain. Source exposure, reviewer independence, formal CLAIM/Review/Admission remain under the project's own control contracts. Native Owner was not confirmed in this run: canonical control-task list returned \`CONTROL_QUOTA\`, and authenticated researcher start returned \`STATIC_READONLY_SCOPE_DENIED\` with \`operation_sent=false\`. GitHub login \`awdawmip\` has repository admin/push but is not a native Researcher-ID.

**Next PREFIX-467:** build a joint dense bounded-horizon codec for the exactly reachable \((A,C,q)\) fibers of this two-step gate. Compare the product-bound \(|S_p|\times3\) with genuinely reachable joint states, and prove a finite-horizon minimal codec where observable continuations identify states. In parallel retain the independent all-degree X6 moment-rank theorem question from PREFIX-459/460.
