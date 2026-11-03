# Stage396-B — sharp bounded pair-cancellation memory window

Date: 2026-11-03 (Asia/Shanghai). Research2; author-side exact mathematical theorem, UNREVIEWED / NOT_ADMITTED. Parent Stage395-B Research2 PR #1736 commit 57d32fabad19adf3a08e9ebfaad99f43d627ad92.

Scientific pins unchanged: EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; global science bf84bd7c61a2444b59b1da96be57df0e9ae47e53; original P000 project blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. New behavioral instructions read independently from the canonical 2026-11-03 global main. Exact native input: research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md and definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json at the frozen EM commit.

## Model and complete observer

Let A={+E_i,-E_i:1<=i<=6} be the native signed direction alphabet; a history w is an ordered finite word of length m. z(w) in Z^6 is its native endpoint and tau(w) counts adjacent unequal labels. An independent source label is retained. O(w) contains: source; all 20 three-component min-zero axis-triple observations R_S(z); global common depth h(z)=min_i z_i; length m; the native full-length endpoint count N_m(z); its fixed positive-rational weighted endpoint mass B_m^p(z) for p_d>0; tau(w); and a separate individual-history signed nonzero-rational product Omega(w)=product omega_d. All triple components, including the third, are retained, and R_S plus h reconstructs z. N and B use the frozen native signed-X6 multinomial/opposite-pair kernel, not a signed-amplitude model.

APPEND(d) pushes any native signed direction. POP_D deletes the terminal letter when it belongs to D subset A; at most H POPs are allowed in total. New pair-cancellation operation CANCEL deletes terminal (d,-d) on one native axis regardless of D; at most C such operations are allowed. H,C are nonnegative integers. Definedness and O are observed after every operation, and future APPEND sequences may have arbitrary finite length. CANCEL is syntactic/provenance-typed path rewriting, not a declared physical Cell inverse or time reversal.

## Theorem 396.1: sufficient uniform suffix and arbitrary-future fidelity

For any D,H,C, if O(w)=O(v) and the last min(m,H+2C+1) labels of w,v coincide, then every finite common sequence of APPEND, POP_D and CANCEL operations has identical definedness and identical intermediate O observations. Thus O, the budgets and the suffix of length min(m,H+2C+1) are a constructive sufficient memory state.

Proof. POP deletes at most one original input symbol; CANCEL deletes at most two. Across the entire future at most H+2C original labels can be lost. If m<=H+2C+1 the original word is fully stored. Otherwise the common initial suffix of length H+2C+1 always retains at least one original symbol above the potentially different hidden prefixes. Every appended surviving symbol is shared by the coupled paths. Therefore all accessible top labels agree at every step. APPEND updates tau with the previous last label; POP and CANCEL subtract exactly the old adjacency contributions determined by the removed 1 or 2 symbols and their known predecessor. Endpoint z, length m, and source evolve identically and determine all R_S,h,N,B. Omega updates exactly by multiplication/division by the nonzero factors for inserted/removed labels. The deletion preconditions inspect only common accessible top labels. Induction on future operations gives equal readouts and equal successor accessible stacks at every step. QED.

This bound is sufficient uniformly; a fixed O-fiber may have a smaller exact quotient.

## Theorem 396.2: sharp universal lookback for any D containing +E1

For every H,C>=0, on the class of all observation fibers with +E1 in D, no uniform suffix of length H+2C suffices. Hence the minimum universally sufficient suffix length is exactly H+2C+1.

Proof. Set u=(-E1,+E2,-E2) and v=(-E1,+E3,-E3). Let tail=(+E4,-E4)^C (+E1)^H and compare w=u tail, w'=v tail. Both have the same endpoint, length, turn count, source, all twenty triple readouts and common depth. Choose omega_(+Ei)=i+1, omega_(-Ei)=-1/(i+1); the product of either opposite-sign pair equals -1, hence Omega(w)=Omega(w'). The native N and positive weighted B depend on endpoint and length and are equal for every fixed p. The two paths have identical H+2C-symbol suffix tail, but their preceding labels differ.

Perform H legal POPs of the terminal +E1 symbols and then C terminal CANCEL operations, successively deleting each (+E4,-E4) pair. Both observations still agree and the remaining paths are u and v. APPEND(-E2) changes tau by 0 for u and 1 for v. Their future observations diverge using exactly H POPs and C CANCELs. Thus a smaller uniform window fails. QED.

At H=1,C=1, this is a concrete counterexample to reusing the selective-POP Stage395-B barrier signature after extending the operation language: POP removes +E1, CANCEL crosses the -E4 barrier by deleting (+E4,-E4), and APPEND(-E2) reveals the previously hidden distinction. The same works within the previous H=3 limit.

## Added joint-history observation

On the six-letter H=C=1 witness the directed adjacent-label histogram J(d,e)=#{j:(d_j,d_(j+1))=(d,e)} distinguishes the histories immediately: one has (+E2,-E2), the other (+E3,-E3). This individual-history joint histogram refines current observer fibers. It is distinct from the positive endpoint mass B and from the signed product Omega. The exact minimal quotient when J is included is the next question.

## Exact executed checks and method reuse

REPRO_STAGE396B_PAIR_CANCEL.py uses only integer and Fraction arithmetic. Its native BRC formula is checked against an independent full-12-direction recurrence on 1,375 endpoint/length cases through m=4 for count and positive weights. Sixteen parameter families H,C=0..3 verify equal current and intermediate O readouts, equality of H+2C suffixes and distinct future turn increments. An exhaustive four-letter finite crosscheck covers input words of length<=4, H,C<=1 and future operation sequences length<=4: 384 same-(O,suffix) pairs, 133,904 visited paired states and 140,240 attempted operations. An independent full replay produces byte-identical stdout. Infinite-future scope follows from the proofs, not the finite checker.

BRC reuse: REUSE_APPLIED to the pinned full-length native signed-X6 N and positive rational endpoint-B formulas; COMPOSE_APPLIED to the typed Stage395 observer, signed individual-history trace and new pair deletion. Status: PORTABLE_AUTHOR_PROOF / EXACT_FRACTION_EXECUTED / GITHUB_SAVED (after verified write) / UNREVIEWED / NOT_ADMITTED. GitHub publication is not a native Source CLAIM, Result, Driver review or Foundation change.

Next Stage397-B: compute the exact fiberwise minimal future-equivalence quotient under bounded POP and CANCEL, potentially smaller than the sharp uniform window. With the individual-history joint adjacency histogram added, check its correct update laws and the boundary memory necessary for arbitrary future APPEND/POP/CANCEL operations. Preserve frozen science pins, source, full X6, third components and typed positive mass versus signed traces.
