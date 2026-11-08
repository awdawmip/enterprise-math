# PREFIX-583-R2 — Quartic gate-observer symmetry versus original native symmetry

Date: 2026-11-08 Asia/Shanghai. Status: AUTHOR-SIDE EXACT ALGEBRA / EXHAUSTIVE FINITE NATIVE EDGE CHECK / UNREVIEWED.

Frozen original science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Original 48 phases, 96 phase/branch ports, six labeled actions per port, and all three original gate transitions. No changes to P000 or native scientific input. Dependency: exact 126-coefficient quartic certificate PREFIX581_R2_exact_monomial_certificate.json on this branch.

## Observer and precise theorem statements

Let R1,...,R6 be original six unit-axis cumulative rewards and K the original native gate count. Let F4(a1,...,a6,b) be the limiting fourth cumulant per original action of a1*R1+...+a6*R6+b*K. PREFIX-581 expresses F4 as a rational homogeneous quartic P(y1,...,y5,b), where yi=ai-a6, and supplies all 126 monomial coefficients.

A quartic axis symmetry is a permutation of the six axis coefficients fixing the gate coefficient b and preserving F4 identically. A marked native axis symmetry is an axis permutation induced by a bijection on all 96 original ports taking each original labeled directed action bijectively to an original labeled directed action, with the permuted source-axis reward, original gate indicator and original branch-state semantics preserved.

**Theorem 583.1.** The exact quartic axis stabilizer is the order-four Klein group:

    G4 = { identity, (5 6), (1 3)(2 4), (1 3)(2 4)(5 6) }.

**Proof (necessary).** The coefficients of a_i^3*b in the exact single-axis quartic divide the axes into three pair classes with distinct coefficients:

    i=1,3: -659/746496
    i=2,4: 85/186624
    i=5,6: 319/746496.

Thus every symmetry must preserve each pair setwise, leaving only 2^3=8 candidates. The mixed quartic coefficient M_ij=lim Cum(Ri,Rj,K,K)/d satisfies

    M12=246755/3057647616
    M32=M14=-756902/3057647616.

Consequently the swaps (1 3) and (2 4) must occur together: the four candidates with exactly one of them change M12. At most the displayed four remain.

**Proof (sufficient).** Perform simultaneous substitution yi -> a_{sigma(i)}-a_{sigma(6)}, with a6=0 and b unchanged, into the exact 126-term rational polynomial. All 126 coefficients agree for each of the displayed four permutations. The accompanying Python standard-library script checks this as exact polynomial coefficient equality, not polynomial sampling. Hence all four and only four are symmetries. The group is C2 x C2.

**Theorem 583.2.** The group of axis permutations admitting a provenance- and gate-preserving original 96-port native action bijection is exactly

    G_native = { identity, (5 6) }, order 2.

**Upper bound.** A native marked symmetry induces a quartic symmetry, hence lies in G4. The three original marked gate transitions all depart from source-axis 1; there are no marked gate transitions departing from another source axis. Every native marked symmetry must therefore fix axis 1. The two quartic elements containing (1 3)(2 4) are ruled out. Only identity and (5 6) remain.

**Constructive lift of (5 6).** Let the four native STARs be (1,3,6), (1,4,5), (2,3,5), (2,4,6). Each original phase is a triple (star_id,p,c), with signed and opposite-sign axes p,c. Apply sigma=(5 6) to their absolute axis labels, preserving signs. There is exactly one STAR containing both transformed absolute labels; call its index a'. Define phi(star_id,p,c)=(a',sigma(p),sigma(c)). This is an involutive bijection on all 48 phases and fixes the original gate target phase (0,1,-3). On ports set Phi(2q+bit)=2phi(q)+bit.

For each of all 576 original actions, the image of its source and destination under Phi is an original action (with a possible permutation of the three successor slots), with the source-axis label exchanged 5/6, the same new branch bit and the same gate indicator. The companion checker verifies these 576 exact finite cases. Thus the lift exists, and by path concatenation it preserves full finite-length native path generating functions under matching initial-port relabeling; uniform initial ports are preserved too. This completes the native group classification.

The extra quartic symmetry (1 3)(2 4) is therefore a genuine identity of a fourth-order *observer* but not of the provenance-retaining marked native edge system. This exhibits an exact distinction between low-order observable symmetry and original carrier symmetry.


## Theorem 583.3 — First separating *reduced* cumulant occurs at order two, depth one

Fix the native uniform distribution on all 96 initial ports, and choose one of the six equally weighted labeled actions. Let Ri(1) and K(1) be their original axis reward and gate indicator. Exactly 96 of the 576 labeled edges have source reward on each axis, while exactly three gate edges have source axis 1. Consequently

    E[Ri(1)] = 1/6 for all i,
    E[K(1)] = 3/576 = 1/192,
    E[R1(1) K(1)] = 1/192,
    E[R3(1) K(1)] = 0.

Therefore the exact one-step covariances are

    Cov(R1(1),K(1)) = 5/1152,
    Cov(R3(1),K(1)) = -1/1152.

The observable permutation (1 3)(2 4), although a symmetry of the *asymptotic fourth cumulant*, fails already at the finite-depth **second** joint cumulant. For the declared uniform starting ensemble and length 1, all first moments of (R1,...,R6,K) are symmetric in the six axes, so order two is the least cumulant order distinguishing this candidate at depth 1. This is an exact BRC branch-counting identity, with no analytic limit or approximations.

## Evidence and continuation

The companion PREFIX583_R2_symmetry_certificate.py reads the exact 126-monomial PREFIX-581 rational certificate, checks eight invariant-compatible candidates, confirms the quartic stabilizer, reconstructs the original 48-phase/96-port/576-action BRC graph, proves the gate-edge source-axis invariant, and verifies all 576 edges of the explicit (5 6) native lift. All computations use exact fractions; result JSON is PREFIX583_R2_symmetry_certificate_results.json.

BRC reuse: REUSE_EXECUTED; exact scientific pin and labeled branch/gate provenance retained. Independent Driver mathematical review, original Source Researcher-ID, CLAIM, activity and Result remain pending because the native backend was unavailable. This is author-side reproducible evidence.

Next: characterize which gate-marked axis permutations preserve asymptotic cumulant generating functions of all orders, distinguishing exact finite-depth symmetry from asymptotic spectral symmetry. At uniform depth one the smallest distinguishing reduced joint cumulant is now proved to be order two.
