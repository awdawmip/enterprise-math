# Stage411-B — Uniform five-class exact future quotient for the one-defect / two-defect X6 path family

Date: 2026-11-04 Asia/Shanghai. Parent: Stage410-B at f55991be3bfe3b11d2abbfb89a2b522eb9dcf9d6, Draft PR #1736. Classification: AUTHOR_PROVED / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Frozen inputs and observer

Frozen science: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral rules read separately at global main 4faf0ff9fdfba409587fef20511e42a8b477b581 and Enterprise Math main d19932605e091c56d379b1a9461047e229fce62a. The native direction set is D={+E_j,-E_j:1<=j<=6}; set A=+E_1 and B=-E_1 for this fiber only. A and B are native directions embedded in all six native spatial axes, not a separate native plane. This theorem concerns a path-formal observer, without a claim of calibrated physical dynamics.

Every intermediate observation includes the two lengths, both labelled X6 endpoints, the complete directed labelled-adjacency histograms J_P and J_Q and absolute-position match count K(P,Q)=sum_{t<=min(|P|,|Q|)}[P_t=Q_t], together with operation enabledness. All future operations are arbitrary paired APP(a,b) for any (a,b) in D^2; at most one Q-only POP; at most one simultaneous CANCEL, removing the final two inverse-adjacent original or appended directions from EACH source, enabled only if both have such pairs. Operations and remaining budgets are known. Positive path BRC counts and independent commutative per-direction products are derived observers when defined; no signed-amplitude cancellation is inferred from positive mass.

## Theorem 411.1: exact complete fibers and all-horizon minimal quotient

Fix an integer n>=5 and the observation for length-n histories P,Q with P endpoint (n-2)E_1, Q endpoint (n-4)E_1, J_P(AA)=n-3, J_P(AB)=J_P(BA)=1, J_Q(AA)=n-5, J_Q(AB)=J_Q(BA)=2, every other directed J entry zero, and K=n-1.

Write P with its unique B at 1-indexed position i; write Q with Bs at r<s. The full observation fiber is precisely

F_n = { (P_i,Q_{r,s}): 2<=r, r+2<=s<=n-1, i in {r,s} },

where P_i=A^(i-1) B A^(n-i), Q_{r,s}=A^(r-1) B A^(s-r-1) B A^(n-s). There are (n-3)(n-4) source pairs.

The exact equivalence classes under ALL finite legal future action traces are the following NONEMPTY sets:

C0: s=n-1, i=s, r=n-3. Size 1.
C1: s=n-1, i=s, 2<=r<=n-4. Size n-5.
C2: s=n-2, i in {r,s}, 2<=r<=n-4. Size 2(n-5).
C3: s=n-1, i=r, 2<=r<=n-3. Size n-4.
C4: 4<=s<=n-3, 2<=r<=s-2, i in {r,s}. Size (n-5)(n-6).

Consequently q(F_5)=2; q(F_6)=4; for every integer n>=7, q(F_n)=5. For n=7 the 12 histories split [1,2,4,3,2]. The original (suffix_3(P),suffix_4(Q)) sufficient representation has seven keys on F_7, while the true quotient has five. The fixed-width bits are ceil(log2 7)=ceil(log2 5)=3 at n=7. Relative to retaining the full distinguishable-history labels, q(F_n) is eventually constant while |F_n| grows quadratically.

## Proof of fiber completeness

J_P has one AB, one BA, no BB, and n-3 AA edges. Because both first and last labels are A (the only Euler trail compatible with those positive edges and the 1-B endpoint), P has exactly one interior B. J_Q has two AB and two BA, no BB, and n-5 AA edges; Q starts and ends in A and has exactly two nonadjacent interior Bs. Hence P_i and Q_{r,s} are all possible full-X6 words satisfying the labelled J constraints; any other native direction would require a nonzero forbidden J entry. P has one B and Q two, so K=n-1 exactly when the unique P-B coincides with one of Q's Bs. Number of admissible (r,s) pairs equals choose(n-3,2), with two choices of i per pair.

## Observer-safe lemma A: raw suffix criterion

For arbitrary initially equally observed length-n native path pairs, if both P histories have the same last THREE original labels and both Q histories have the same last FOUR, they are equivalent under the declared future language.

Proof: In any trace the surviving state can be written P[1:n-d_P]U, Q[1:n-d_Q]V, where U,V are surviving appended stacks. One CANCEL deletes at most two original P labels and two original Q labels; one Q-POP deletes at most one additional original Q label, so d_P<=2, d_Q<=3. Once P has lost two originals, CANCEL is spent; once Q has lost three originals, both erasers are spent. For any d_P,d_Q, the directed histograms and endpoints of the truncated originals are reconstructed by subtracting the exact removed suffix edges and directions from the original equal observation. Original-original K is initial K minus the equality indicators among the last max(d_P,d_Q)<=3 aligned original positions; these are known from the shared P-three/Q-four suffixes. The overlap of a longer original prefix and the other appended stack needs at most max(d_P,d_Q)<=3 of the final P labels or <=2 of the final Q labels; the shared suffixes supply them. Appended-appended observation is identical for common surviving U,V. Terminal one or two required labels of truncated originals also agree: if a source has lost so many originals that only the last one is certified, the operation needing two original labels has already been consumed. Therefore each common future action has equal enabledness, produces equal next observation and preserves this decomposition with identical appended stacks. Induction on action-trace length proves the lemma for all twelve directions and arbitrary finite horizons.

C1 satisfies the lemma: every member has P suffix ABA and Q suffix AABA. (C0 is a singleton.)

## Observer-safe lemma B: P-ending-AA budget certificate

Suppose initially equal observed paths of length n have P ending AA in both histories. For all six (d_P,d_Q) with d_P in {0,1}, d_Q in {0,1,2}, suppose (i) the full truncated ORIGINAL-pair observations agree; (ii) retained P prefixes have matching last TWO labels when d_P=0 and last ONE when d_P=1; (iii) retained Q prefixes have matching last TWO labels when d_Q<=1 and last ONE when d_Q=2; (iv) the respective final TWO original labels of P and of Q match across compared histories. Then the histories are all-horizon future equivalent.

Proof: Since P originally ends AA, a CANCEL touching original P needs a prior paired APP, and can delete at most one original P label; hence d_P<=1. If two original Q labels are lost, a Q-POP and the only CANCEL have both been used (the APP needed for P's cancellability also appends to Q, so removing two original Q labels with CANCEL alone requires consuming Q-POP on that append). Thus d_Q<=2 and the d_Q=2 terminal state has no erasing action left. The six prefix certificates determine original-only observations at every possible destructive boundary. Appended suffixes U,V evolve identically under common actions. The original-appended overlap covers at most two terminal P original labels or one terminal Q original label, supplied by (ii)-(iv); all other terms are original-original (i) or appended-appended. Boundary labels also decide every remaining enabled operation identically. Induction establishes a bisimulation for arbitrary paired APP in D^2, arbitrary action order and unlimited action-trace length.

For C2, C3 and C4 this certificate holds uniformly in n. In each class P ends AA; Q's respective last three labels are BAA, ABA and AAA; hence all required boundaries are class-constant after zero, one or two deletions. J_P and the endpoints after deleting at most one final A are class-constant. J_Q and its endpoint after deleting up to two trailing labels are class-constant from the indicated Q suffix. Write L=n-max(d_P,d_Q). The truncated original match count is L-1 for C2 and C4, since both Q-B positions and exactly one P-Q mismatch remain in their common first L positions. For C3 it is L-1 when L>=n-1, and L when L=n-2, because the unique mismatch at s=n-1 has then been deleted. Thus (i) holds. The terminal AA for P and the class-constant last two Q original labels also establish (ii)-(iv). Lemma B merges each of C2, C3 and C4 over ALL its internal r,s,i choices.

## Necessity: four explicit short observer tests

Let T0=CANCEL, T1=POP_Q, T2=POP_Q then CANCEL, T3=POP_Q then APP(B,B) then CANCEL; an unavailable action is an observable disabled result.

T0 is enabled precisely for C0 and C1: both originals end BA iff i=s=n-1.
T1 removes the Q edge BA when s=n-1 (C0,C1,C3), and removes AA when s<=n-2 (C2,C4), distinguishable in the labelled Q histogram.
Among C0/C1, T2 is legal and the resulting Q truncated original ends B in C0 (r=n-3), versus A in C1 (r<=n-4), yielding different labelled Q histograms.
Among C2/C4, T3 is legal and its resulting Q ends B for C2 (s=n-2) versus A for C4 (s<=n-3), again with different Q adjacency histograms.

These four observable test responses distinguish all five nonempty classes (and the surviving classes for n=5,6). Lemmas A-B prove sufficiency within each, so the partition is the exact all-horizon quotient.

## Exact executed evidence and reuse

REPRO_STAGE411B.js enumerates F_n independently by positive A-run compositions and by directed B positions for every n=5,...,16; verifies the class formulas, initial full observations, safe suffix and all six truncated-prefix certificates. It applies the four separating tests and checks their constancy and distinctness. It also runs an independent residual-directed-Euler/K transfer at n=7 and a finite APP alphabet {+E1,-E1,+E3}, depth<=4 within-class transition comparison. The all-horizon statement is proved above, not inferred from the finite test horizon.

Native twelve-direction integer BRC uses N_(t+1)(z)=sum_{d in D}N_t(z-d) and W_(t+1)(z)=sum_{d in D}w(d)W_t(z-d), with w(A)=2, w(B)=3 and all other weights 1. At n=7, exact endpoint totals are N_7(5E1)=217, W_7(5E1)=8064; N_7(3E1)=10521, W_7(3E1)=132048. These are full native endpoint populations, separate from the 12-pair J/K fiber. Existing native BRC recurrence is REUSE_APPLIED; Stage406 raw-suffix and Stage404 residual Euler/K interfaces are COMPOSE_APPLIED, with a new family-specific exact future quotient, not a new global tool acceptance claim.

The residual-edge state count is polynomial in numeric n for fixed signed alphabet and bounded eraser budget, not claimed polynomial in binary-encoded counts. The theorem concerns exact observer-safe source-history memory in the declared action model; other path/provenance or physical observations require their own preservation certificate.

## Status and continuation

Verified author-side mathematics and exact computation; independent mathematical review and native Result/CLAIM are outstanding. GitHub actor was awdawmip; the native static read-only session creation call returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false), and current task inventory returned CONTROL_QUOTA. Do not infer active Task owner from GitHub ownership.

Stage412-B should derive the five-class quotient directly from directed J, absolute K and fixed eraser budgets without listing F_n, using a boundary automaton or generating functions; then test allowing a second Q-only POP or second simultaneous CANCEL as a falsifier of eventual q=5. Preserve the original frozen science pins, P000 and admitted-source boundaries.
