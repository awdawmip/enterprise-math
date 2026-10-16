# R82 — Two disjoint four-step probes (author-side, 2026-10-16)

Status: LOCAL EXACT CHECK PASS; UNREVIEWED; NOT_ADMITTED. Frozen GlobalKnowledge main a7316c6ee0b9dc21f6b672009235c496ec73095a; Enterprise Math main 5714fd478faa9fce000bd255bdb37bcfa7b05242. Predecessor: R81 (author-side, unreviewed).

In the ordered integer observer R=Z<X1,...,X6>/(Xi^2), set S(w)=product(1+epsilon_i X_axis), T_d=homogeneous degree d. Choose four mutually distinct native axes a,b,c,e. Define appended loops g_ab=(a,b,-a,-b) and g_ce=(c,e,-c,-e), and Delta=T_(d+2)(w g_ab)-T_(d+2)(w g_ce). For every legal length-d word u, d>=1, let x=last(u). Then

[u]T_d(w)=[uab]Delta if x is outside {a,b}; otherwise [u]T_d(w)=-[uce]Delta.

Proof: S(g_ab)=1+(XaXb-XbXa)+(-XaXbXa+XbXaXb)+XaXbXaXb. Subtract the analogous ce expression; the unknown baseline T_(d+2)(w) cancels. The selected two-letter suffix has no contribution from either probe's cubic/fourth degree terms, since x lies outside the selected axis pair. Distinct probe suffixes cannot interfere. Every legal u is recovered as an integer coefficient, with no baseline or lower-degree observations.

For CYCL zero-displacement native X6 words, choose four probe axes outside the two boundary axis supports; at least four remain. Both extensions stay CYCL. This reduces R81's four baseline-free probes to TWO (sufficient; optimality unproved). Branch-resolved ordered integer observations are assumed. Different probe axis pairs generally have different strictly positive rational BRC mass factors; normalize known weights separately, not by signed branch-mass cancellation.

Local verification: 24 distinct CYCL paths, degrees 1..5; three extended instances degrees 1..8; 27 path/pair runs; independent 2,808 coefficient DP checks; native BRC bridge counts 1,12,396; ZIP coldstart and 10-file hash checks pass. Evidence bundle SHA-256: 5e02250830d1418fe4852b5f1e0bb1a5c6bbf24983435afc8e4b77ca94787f48.

Formal native session registration denied (STATIC_READONLY_SCOPE_DENIED), active-owner state unreadable (CONTROL_QUOTA). This branch is not a Task/CLAIM/Result or Driver-reviewed admission. Next: settle whether a single post-probe degree d+2 observation suffices on the actual native path image, by true CYCL collision or exact recovery.
