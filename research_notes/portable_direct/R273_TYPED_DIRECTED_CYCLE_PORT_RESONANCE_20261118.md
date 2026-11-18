# R273 — Directed-cycle joint-Port resonance and mode-selective p-adic precision

Date: 2026-11-18.
Status: AUTHOR_PROVED / EXACT_RATIONAL_FINITE_CHECK / NOT_REVIEWED.
Mode: independent portable research; no formal CLAIM.
Frozen science pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Previous frontier: R271/R272 at bafca0cfdb4a7814cc5d74534ff9ade753029b4a.
Typed source: definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md, blob e7823e69fe8112663af2feeb3fc3207b73b2fabe, WBRC-T30/T31/T32.

## Question, exact domain and operator

Do a set of individually permitted, nonnegative, labeled Port edges exhibit a new p-adic resonance when connected into a directed cycle? Determine the sharp retained precision of the full Port star and a regular-mode observer.

Fix an odd prime p, L >= 2 with p not dividing L, N >= 1, and q=p^N. Let P be the L-by-L cyclic permutation matrix with entry (i,i+1 mod L) equal to one. Fix any positive p-unit integer c, set a_c=(1+cq)^{-1} and W_c=a_c P. Ports retain their original labels, and the hidden set is empty. Each edge is independently permitted by WBRC-T31. Every proper subset and the complete network are strictly stable nonnegative rational Port models because 0<a_c<1. Let S_c=(I-W_c)^{-1} be the visible star.

Modular observations take place over the localization Z_(p) after displaying the appropriate normalization. These are Port arithmetic claims and carry no automatic assertion about the six-axis Cell or a map from R269's auxiliary 63 sources.

## Theorem R273-A: a joint closed path creates arbitrarily deep resonance

For all p,L,N,c as above,

\[
S_c=\frac{\sum_{j=0}^{L-1}a_c^jP^j}{1-a_c^L},
\qquad v_p(1-a_c^L)=N,
\qquad p^N S_c\equiv (Lc)^{-1}J\pmod p,
\]

where J is the all-ones matrix. Every labeled entry of S_c has valuation exactly -N.

For any proper subset of the L labeled cycle edges, its adjacency matrix W is nilpotent (W^L=0); therefore its star is the finite polynomial I+W+...+W^(L-1), which is entrywise p-integral. Resonance of arbitrarily large depth can thus be a genuinely joint edge effect, absent from every proper edge subset.

Proof: P^L=I yields the geometric inverse. Factor 1-a^L=(1-a)(1+a+...+a^(L-1)). The first factor has valuation N. The second is congruent to L modulo p, hence a unit. The numerator has precisely one p-unit a^j in each position. With U(z)=((1+z)^L-1)/z and U(0)=L, p^N/(1-a^L)=(1+cq)^L/[c U(cq)] reduces to (Lc)^{-1}; the sum of all P^j is J. A proper edge subset is a directed acyclic graph, hence its adjacency is nilpotent. QED.

For L=2, two separate edges 1-to-2 and 2-to-1, both of weight a, have S11=1 when used separately, whereas S11=1/(1-a^2) when used together. Their exact mixed difference is

\[
\Delta_{12} S_{11}=\frac{a^2}{1-a^2},\quad
v_p(\Delta_{12}S_{11})=-N,\quad
p^N\Delta_{12}S_{11}\equiv(2c)^{-1}\pmod p.
\]

Thus an additive combination of the one-edge observations misses an arbitrarily deep cycle residual.

## Theorem R273-B: sharp N+m digits for the full normalized star

For any positive p-units c,d and every labeled entry, using v_p(0)=+infinity,

\[
v_p\bigl(p^N(S_c-S_d)_{ij}\bigr)
=v_p(c-d)=v_p(a_c-a_d)-N.
\]

Consequently N+m digits of the common edge weight determine the p^N-normalized full visible Port star modulo p^m within this family, and N+m-1 digits cannot suffice uniformly, for every m>=1.

Proof: each entry corresponds to one j in {0,...,L-1} and equals

\[
G_j(c)=p^N\frac{a_c^j}{1-a_c^L}
=\frac{(1+cq)^{L-j}}{c\,U(cq)}=\frac{h_j(cq)}{c},
\quad h_j(z)=\frac{(1+z)^{L-j}}{U(z)}.
\]

Since U(0)=L is a p-unit, h_j is p-integral near zero with h_j(0)=1/L. Expand the exact difference as

\[
G_j(c)-G_j(d)=
(d-c)\frac{h_j(cq)}{cd}
+\frac{h_j(cq)-h_j(dq)}d.
\]

The second term is divisible by q(c-d), while the coefficient of d-c in the first term is a p-unit with residue (Lcd)^(-1). Thus the valuation of the difference is exactly v_p(c-d). Direct subtraction gives a_c-a_d=(d-c)q/[(1+cq)(1+dq)]. Set c=1 and d=1+p^(m-1) for a witness at the lower precision boundary. QED.

## Theorem R273-C: a regular observer has no resonance-depth precision penalty

Put Pi=J/L and Q=I-Pi in M_L(Z_(p)), both commuting with P. Then

\[
S_c=\frac{\Pi}{1-a_c}+R_c,\qquad
R_c=(I-a_cP)^{-1}Q.
\]

The regular operator R_c is entrywise p-integral. For any p-integral weights a,b congruent to 1 modulo p (with rational inverses defined), the regular operators obey

\[
R(a)-R(b)=(a-b)R(a)P R(b).
\]

The right product is integral and invertible on the zero-sum Port submodule modulo p. Therefore every entry of R(a)-R(b) has valuation at least v_p(a-b), and at least one entry has valuation exactly v_p(a-b) when a!=b. The regular-mode operator is exactly locally 1-Lipschitz. Its m output digits require no N-digit penalty.

Proof: p does not divide L, so the Port module splits integrally into constant-line image(Pi) and zero-sum V=image(Q). On V, I-P is invertible over Z_(p), since its determinant is L up to sign. Therefore (I-aP)^(-1) on V is integral and invertible modulo p whenever a=1 (mod p). The resolvent identity supplies the displayed difference. Since the factor R(a)P R(b) is an automorphism of V modulo p, it is nonzero mod p in the labeled matrix and yields sharpness. QED.

For L=2, the regular labeled observable is S11-S12=1/(1+a). Its difference under a-to-b has valuation v_p(a-b), whereas the normalized full-star difference has valuation v_p(a-b)-N. We retain both the resonant cycle channel and the regular observer, including the original Port labels and edge provenance.

## Exact finite certificate

Accompanying pure-stdlib Fraction checker verifies (I-aP)S=I, strict positivity/stability, determinant valuation, every normalized star-entry residue, all-entry difference valuations, all single-edge-deleted nilpotent cases, the regular operator's integrality and sharpness, and the L=2 mixed residual. Exact grid: primes 5,7,11,13, port count 2..8 except p|L, N=1..3 and m=1..3 for primes 5/7/11, N=1..5 and m=1..4 for p=13.

Output: PASS 311 exact cycle cases, 47 exact two-Port cases and 96 additional 13-adic positive-unit residue cases. The full generated reproducible JSON is 85,169 UTF-8 bytes with SHA256 2f76737f8612cc0835d63e8310b8fa16ced4fbafae2dbe03cb47542c5b51d8a1. Finite checking does not substitute for the preceding universal algebraic proofs.

Classical ingredients: geometric resolvent, permutation eigenspaces, elementary p-adic valuations and Woodbury/rank-one updating. Project-specific scope: finite stable positive-rational *labeled* WBRC Port contexts with a verified joint cycle residual and observer-specific sharp precision; NOT_REVIEWED and no Foundation promotion.

## Unfinished next unit

Extend the resonance/regular-mode split to strongly connected, branched labeled Port graphs and calculate the observer-restricted Smith precision. Separately test an actual provenance-preserving candidate map from R269 auxiliary sources to WBRC Port signatures under all declared future contexts, with exact fiber-constancy or a counterexample. Associate this source with the existing genuine Research Activity only when its current record CAS/identity and a faithful readback are available.

Files: R273_TYPED_DIRECTED_CYCLE_PORT_RESONANCE_20261118.md; R273_two_edge_cycle_precision_checker.py; R273_digest.json. Full R273_verification.json reproducible from the checker and retained locally.
