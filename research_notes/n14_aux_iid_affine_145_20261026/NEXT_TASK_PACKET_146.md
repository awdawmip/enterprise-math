# Stage146 — exact dual-only candidate, original primal interval OPEN

Auxiliary **external** ternary iid N=14 model, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), arbitrary randomized full ordered-prefix stopping by depth 14. No native P000/X6 theorem, native Result, or independent Driver acceptance.

The exact Stage145 author proof ends at alpha145=61650988568176660266901/177207634216336528244736 and V145=34260854261470059183743591/2835322147461384451915776. At Stage145 endpoint R=(11,2,0) has immediate P-stop coin u=1, while T=(7,1,2) has interior immediate Q-stop coin v=245752551670737/579687950800000.

Maintain T Q-versus-continue tie along the exact dual ray

dK=-119097459, dL=-87933952;
T directional gradient (-85873/6718464, 54457/3145728);
R P-versus-continue gap derivative -175207181/432 (so R strictly becomes P-stop).

The first closure of the other initially positive action gaps occurs at lambda146=13737326062879/745578398963291701152, bringing a new critical state U=(8,6,2), decision P versus continuation.

Fresh **680-state exact Bellman** dual candidate:

K146=580442338958517/1418470016864,
L146=52669253445512/132981564081,
Hroot146=1064448260606076968085635550307/3642399692121256208464084992.

Only two ties: T=(7,1,2) Q/C, U=(8,6,2) P/C; all other 1238 gaps strictly positive, minimum 6129035788073/1378752856391808, zero negative. This is **dual-only**. Stage146 primal feasibility, full-real optimal segment and right-sharpness theorem have not been proved.

**New structural lemma.** T and U cannot lie on the same ordered path. U depth8 exceeds T depth7 by 1 but changes a (first-symbol count) from 1 to 6: +5 in only 1 symbol, impossible. Conversely depth excludes U as predecessor of T. Hence two cones are disjoint.

**Next exact independent research unit:** compute T,U literal first-hit P/Q mass (with old R forced P-stop), four ordered-history observer vectors for all deterministic coin corners using exact Fraction backward recursion AND separate integer-weight forward DFS; verify mixed term zero. Solve eP=eQ for the two coins; match Stage145 endpoint, test allowed [0,1] ranges and tP>=tQ, derive largest full-real optimal interval or exact obstruction. Then justify strict right endpoint if appropriate. Preserve the scope/observer arguments for history-dependent policies.

Frozen research input: GLOBAL_KNOWLEDGE_V1 main@eddc59ec31a539546c71e1e3aacd4ce43cc06a00; EM initial main@7830c42b911508d114c9550d05eb98c4fc649a84; Stage144 source commit bc33991a8dda3a29975c9b2e5541fed11899e657. Current work author-only; native Owner/CLAIM and independent Driver review pending.