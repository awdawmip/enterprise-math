# Stage409-B — Exact three-state quotient on an infinite family of native-X6 Euler/K fibers

Date: 2026-11-03 Asia/Shanghai. Research2 continuation of Stage408-B `dc63b4cd6014de44f9e20ff27d3fce9a1f63822e` in Draft PR #1736. Classification: AUTHOR_PROVED / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Scientific pins retained: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Behavioral rules separately checked on global canonical main `86d6ccfb7776eb6f8a9078680908bfd958a385a8`, EM main `263e49405ff00217fbd8948374d7e5bd32358136`. P000 and ACTIVE Heartbeat World are unchanged.

## Observer and operation model

The complete primitive direction alphabet is `D={±E_i | 1<=i<=6}` in native X6. Let A=+E1, B=-E1. Two ordered original source words P,Q have equal length n. At every intermediate step observe individual lengths, native signed six-axis endpoints, the **full labelled directed adjacency histograms** J_P,J_Q, and absolute-position coincidence K(P,Q)=sum_{i<=min(|P|,|Q|)}[P_i=Q_i]. Native endpoint-derived positive BRC counts/weights and nonzero direction-local products are included with the same inherited semantics. Operations: arbitrary paired APP(a,b) for a,b in all twelve directions, at most one Q-only POP, and at most one simultaneous CANCEL erasing the last inverse pair of *both* sources. Enabledness and every intermediate observation are visible.

## Theorem 409.1: full fiber and exact minimal quotient

For every integer n>=5, fix P=A^n, J_P(AA)=n-1, and for Q the directed-edge counts
`J_Q(AA)=n-5, J_Q(AB)=J_Q(BA)=2` (all others zero); endpoints z_P=nE1,z_Q=(n-4)E1, lengths n, and K=n-2. The **complete full-X6 observation fiber** is

`F_n={(A^n, A^u B A^v B A^w): u,v,w>=1, u+v+w=n-2}`.

Proof of completeness: all observed Q transitions use only A,B and BB never occurs. Q has n-2 letters A and two B, from the endpoint and length. Since AB and BA counts both equal two, a path that begins and ends B would contain three B visits (two B departures plus its final B), contradiction. Thus it begins and ends A, and its two B letters are separated by positive A-runs. The converse is immediate. Therefore |F_n|=binom(n-3,2).

**Exact equivalence theorem.** Two histories in F_n are future equivalent under *every finite legal full-12-direction action trace* if and only if their trailing A-run lengths w,w' satisfy `min(w,3)=min(w',3)`. Consequently the exact minimum number of extra memory states is

`q_n = min(3,n-4)`.

For n>=7 the class multiplicities are `n-4, n-5, (n-6)(n-5)/2`, for the classes w=1,w=2,w>=3 respectively. n=5 has one class, n=6 two.

### Proof: equivalence within each class

Each source after any operation is a prefix of its original word followed by a stack of common appended letters. The original P letters are all A, so a single CANCEL can remove at most **one** original P letter: the original AA pair cannot be an inverse pair. With one POP and one CANCEL, at most two original Q letters can be removed. To remove two Q originals requires having consumed *both* destructive operations: a P-enabling APP also appends to Q; for CANCEL to erase two Q originals, Q's appended boundary must first be removed by POP. If Q has lost exactly two original letters, no destructive operation is left; the next step can inspect only its current *terminal*, never its penultimate original letter.

Let r be the number (0,1,2) of deleted original Q letters, and g=min(w,3). All relevant original-prefix edge and tail data are functions of (r,g):

|g|r=0 original Q last pair|r=1 removed edge; new last pair|r=2 removed original edges; remaining last letter|
|---|---|---|---|
|1|BA|BA; AB|BA and AB; A|
|2|AA|AA; BA|AA and BA; B|
|3|AA|AA; AA|AA and AA; A|

The full original J_Q after deletion is the fixed initial J_Q minus the indicated removed edges; its endpoint and A/B counts follow exactly from the same deletions. For r=0,1 any still-available deletion needs only the listed last pair (or current appended suffix); when r=2 only APP remains and its needed old boundary is the listed last letter. Original P is A^n or A^(n-1), so its prefix J, endpoint and suffix are uniquely determined.

It remains to preserve the **joint** observer K. On every original-original overlap position, P carries A. Accordingly the number of matches in the first min(n-r_P,n-r) Q positions is the original Q prefix's A count, with r_P in {0,1}; when r_P=1,r=0 the only excluded last original Q letter is A in *every* member of F_n. When an appended letter overlaps an original P letter, that P letter is A; an appended P letter can overlap an original Q letter only at Q's last original position n, which is likewise A in every member. All appended-appended matches use the identical chronological APP letters and their surviving stacks. Hence K matches after all common enabled actions. All directions outside ±E1 are treated as arbitrary typed APP labels, and do not change this argument. Native endpoint-dependent BRC readouts and direction-local multiplicative outputs also agree since the endpoints, direction counts and appended streams agree. Finally, legality of POP/CANCEL follows from the same current suffix pairs. These identical update rules supply a bisimulation of every pair of histories with the same g. Thus equality extends to *all* finite full-X6 future traces.

### Proof: distinct classes cannot merge

A Q-only POP erases BA for w=1 and AA for w>=2; therefore g=1 differs immediately from the other classes. To separate w=2 from w>=3, use `POP_Q; APP(B,B); CANCEL`. After POP both Q sources end A and P ends A. APP(B,B) creates an inverse AB terminal pair in both sources, so CANCEL is legal and deletes the appended B plus the old final A of each. For g=2 the two removed Q original edges are AA,BA; for g=3 they are AA,AA. The resulting labelled J_Q differ. All three classes, when present, are necessary. This proves the theorem. □

## Stage409-B n=8 executable numerical certificate

For n=8 the complete fiber has ten paths. A residual-Euler directed-edge plus joint-K DP retains only remaining labelled edge counts, last Q letter, last-four suffix, signed endpoint and K, **not complete Q paths**. Its exact output is `AAAA:1, AABA:3, ABAA:3, BAAA:2, BABA:1`, independently checked by direct enumeration of all 2^8 two-label words. The Stage406 safe raw (P3,Q4) representation has five states; the exact quotient has three classes of multiplicities **[4,3,3]**. Fixed coding reduces from ceil(log2 5)=3 to ceil(log2 3)=2 bits.

The actual checker also confirms the two distinguishing operation traces and twelve within-class pair comparisons over APP directions {+E1,-E1,+E3} to operation depth four (10,068 visited paired states; 13,704 transition attempts). The full-X6, unbounded-future claim is established by the bisimulation proof above, not this finite check.

Native all-twelve-direction integer BRC recurrence `N_(t+1)(z)=sum_(d in D)N_t(z-d)`, `W_(t+1)(z)=sum_(d in D)w(d)W_t(z-d)` using w(A)=2,w(B)=3, all others 1 gives: `N8(8E1)=1, W8(8E1)=256; N8(4E1)=20608, W8(4E1)=479808`. These count *all* native endpoint words and are distinct from the ten-path directed-edge observation fiber. No signed/phase cancellation conclusion is drawn from positive weights.

Actual local Python standard-library runs were performed twice with byte-identical stdout. Checker result: `STAGE409B_EULER_K_THREE_CLASS_PASS`. Peak distinct residual-DP states: 16. General DP resource cost is measured in numerical edge counts; no binary-encoding polynomial-time claim. This family additionally has the exact closed combinatorial formulas above.

Reuse: Stage402/404 Euler/K residual transfer COMPOSE_APPLIED; Stage406 tail sufficiency REUSE_APPLIED; Stage408 reduced-APP scope REUSE_APPLIED in finite cross-check; native signed-X6 positive BRC integer recurrence REUSE_EXECUTED.

Native service check in this run: research_authority_granted=false, owner listing CONTROL_QUOTA, session creation STATIC_READONLY_SCOPE_DENIED (operation_sent=false). No source-native CLAIM, Result or independent Driver admission.

## Next unit

Stage410-B: change P from A^n to a path with one isolated B and require complete joint K; search for a full fiber with q>=4, or prove an exact bound in that explicit family. Preserve native X6 provenance and examine POP/CANCEL order interactions.
