# D25 / SECOND-DIGIT-LIFT — original E3 rational 3-torsion deck involution

Date: 2026-10-27. Logical Research lane: chatgpt-research-onhour-enterprise-math-20260923 (separate from maintenance). AUTHOR-SIDE / PROVED ALGEBRAIC IDENTITY / EXACT FINITE CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_H0B0_NOT_EXECUTED. Classical elliptic-curve formulas are reused; the new task-local result is their exact original-coordinate signed observer identification.

Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged.

## Exact theorem and proof

Work on the nonsingular original curve E_c: y²+xy+cy=x³ over characteristic zero with c≠0 and 1−27c≠0. Put Q=(0,−c), t=−x/y, and omega=dx/(2y+x+c). In D25, c=(2−T)/108 and T²=2.

Q has order exactly 3: tangent at Q has slope −1 and meets E again at (0,0)=−Q, hence 2Q=−Q.

For a generic P=(x,y) let A=x+y+c. The secant through P and Q has slope (y+c)/x, and the full Weierstrass addition formulas give

    x(P+Q) = c A / x²,
    y(P+Q) = −c A² / x³.

Therefore t(P+Q)=x/A. The original group inverse is −P=(x,−y−x−c), so t(−P)=x/A. Thus the following equality holds in the rational function field of E_c, not just to finite order:

    t(P+Q) = t(−P).
    J(P)=Q−P, J²=id, and t(J(P))=t(P).

Elimination of y=−x/t gives the exact quadratic t²x²−(1−t)x+ct=0. Its two roots have product c/t. On the other hand x(J(P))=−cy/x²=c/(tx), so J exchanges the two roots and therefore the two geometric sheets of the degree-two parameter map t. The roots are

    x_O=(1−t+sqrt(D))/(2t²),
    x_Q=(1−t−sqrt(D))/(2t²),
    D=(1−t)²−4ct³, sqrt(D)(0)=1.

The first germ is the identity O, the second the rational 3-torsion point Q. They share t=0 but not their geometric basepoint. Translation preserves the invariant differential, inversion negates it, hence J*omega=−omega. This matches the exact signed local pullbacks omega_O=+dt/sqrt(D), omega_Q=−dt/sqrt(D). The full second-kind identity eta_O=t^(−2)dt−eta_Q for eta=x omega still requires its principal part in any operator comparison.

## Formal coordinate transport: exact, not a first-order sign guess

For P near O, u(t)=t(P+Q) is the coordinate near Q. As a scalar series it equals t(−P), the formal-group inverse expressed at O:

    u(t)=−2t/[1−t+sqrt((1−t)²−4ct³)].

Set H=1/sqrt(D), L(t)=integral_0^t H(v)dv with L(0)=0 and L'(0)=1. Because translation by Q preserves omega while omega_O and omega_Q have opposite local signs,

    −H(u) du = H(t) dt,

giving the exact identity

    L(u(t))=−L(t); equivalently u=L^(-1)(−L(t)).

Its initial coefficient series is

    u=−t−t²−t³−(1+c)t⁴−(1+3c)t⁵
      −(1+6c)t⁶−(1+10c+2c²)t⁷+O(t⁸).

Consequently the first-order sign −1 is insufficient to transport degree-four-and-higher data. This exact signed branch morphism is an original E3 comparator, not a statement about the original native divided-power H0/B0 operator.

A group-homomorphic semilinear comparison mapping Q_c to Q_(c^sigma), if independently established for the original fixed class, must satisfy F∘J_c=J_(c^sigma)∘F. No native Frobenius statement is inferred without that authentication.

## Executed exact p=373 certificate

Companion file: research_notes/portable_direct/d25_original_E3_torsion_deck_guard_20261027.py. The checker uses Python standard-library integer arithmetic in (Z/139129Z)[T]/(T²−2), T²=2. It independently computes sqrt(D), H, formal L and u through degree 12, and verifies coefficientwise L(u)+L=0 and u(u)=t. The run returned:

    PASS_E3_DECK_373_P2 {'ring': 139129, 'degree': 12, 'c': (105635, 16747), 'Jt_t4': (33493, 122382), 'L_inverse': True, 'involution': True}

The algebraic proof applies under the declared nonsingularity hypotheses; this finite check covers degree <=12 at p=373 and does not prove a new universal Frobenius theorem.

## BRC use and exact research continuation

BRC classification: COMPOSE_APPLIED. Carrier: geometric point/sheet O or Q, original scalar coordinate t, differential sign, and full Laurent pole of eta. Operation: involution J, translation by Q, inversion, and only conditionally an authenticated semilinear Frobenius. Observer: both original de Rham columns with signs and p-adic precision. The quotient retaining only t is not observer-safe, because J preserves t while reversing omega; retaining only the regular second-kind coefficients also deletes the pole. This is an explicit non-faithful quotient witness, not native X6/P000 physics.

Native highest priority: same-original-class p=373 H0/B0 divided-power [X]U modulo 139129, native module rank, Frobenius direction and normalization, odd signed Green/Hesse, original kappa and Delta_p−R_p. The already-existing support issue #1559 tracks this object with PENDING_OWNER / NOT_EXECUTED as observed 2026-10-27. The newly proved sheet relation supplies a conditional validation criterion only after an H0/B0-to-E3 map is demonstrated. D25/LIFT/JT2 stays OPEN. Do not repeat completed D24 UR or W/S certificates and do not treat external E3 algebra as execution of the native benchmark.

Current control observation: exact Research-lane continuation request onhour-20261027T1604-D25-continuation returned CONTROL_QUOTA. Site gateway 0.6.11 reports research_authority_granted=false. Historical recovery #6575 and dispatch #6576 grant no present claim. No own Source session/claim/run was verified; status REGISTER_PENDING. Maintenance conversation_id was not used, and this author artifact is not a canonical Source checkpoint/Result/review.

NEXT ACTION: legally authorized native H0/B0 executor accepts #1559, actually executes the frozen original p373 object with reproducible source/normalization, publishes raw [X]U and all signed ports, and only then compares the E3 deck identity if the bridge is proven. Research lane reconciles exact outstanding requests and Source ownership before any role-bound mutation. Frozen scientific Source pin and existing scheduler/notification policy remain unchanged.
