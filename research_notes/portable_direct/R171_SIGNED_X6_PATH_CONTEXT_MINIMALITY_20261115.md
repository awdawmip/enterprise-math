# R171 — Signed-X6 prefix-integral cocycle, exact context quotient, and scalar-repair obstruction

Date: 2026-11-15 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED.
Research mode: independent portable research; no formal Task/CLAIM/Result/Review assertion.
Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Immediate immutable predecessor: R170 at e810cbcdb5715a1bafa927340852aec5bd26a5cc, research_notes/portable_direct/R170_UNIVERSAL_PARITY_REPAIR_AND_CONCATENATION_COCYCLE_20261115.md.
Current foundation: P000's six signed native spatial axes (affine torsor over Z^6), Heartbeat World ACTIVE, and joint-relation observer preservation. This construction concerns typed native-axis **ordered paths**, not full native BRC amplitudes, force balance, Cell-address encoding, or time evolution.

## 1. Exact population and observers

Fix a chosen native Cell as a chart anchor, only to express *relative displacement*. Let A={+E_i,-E_i : 1<=i<=6} be the 12 signed primitive directions; A* is the free monoid of all finite ordered direction words. For P=(v_1,...,v_m), write

    D_t(P)=sum_{r=1}^t v_r in Z^6, D_0=0;
    D(P)=D_m(P);
    J(P)=sum_{t=1}^m D_t(P) in Z^6.

Here J is the vector-valued **prefix-displacement integral**, a deliberately declared port/path readout. It is path sensitive even for exact endpoint returns. It is not an extra native spatial axis or a claim of physical time integration.

For a modulus q>=2, write G_q=(Z/qZ)^6 and define

    K_q(P) = (m mod q, D(P) mod q, J(P) mod q)
           in (Z/qZ) x G_q x G_q.

For the exact integer readout, K_Z(P)=(m,D(P),J(P)). The signed-axis symbols and path order remain available in the raw population; any reduction is only relative to the explicitly declared J observer and its permitted future operations.

## 2. R171A: exact composition and context law

**Theorem (all lengths, all signed-X6 paths).** For any P,Q in A*,

    D(PQ)=D(P)+D(Q),
    J(PQ)=J(P)+J(Q)+|Q|D(P).                         (1)

Consequently K_q is a monoid morphism into the multiplication

    (a,b,c) * (d,e,f)=(a+d,b+e,c+f+d*b) mod q.       (2)

This operation is associative, has identity (0,0,0), and (on the ambient finite carrier) has inverse

    (a,b,c)^(-1)=(-a,-b,-c+a*b) mod q.               (3)

Thus the ambient carrier is a finite two-step nilpotent group H_q^6 of order q^13. The coordinates retain a signed order cocycle: switching two blocks P,Q changes the J readout by |Q|D(P)-|P|D(Q), reduced modulo q as applicable. Equation (1) and its integer analogue are exact, with no probability, positive-mass collapse, or physical calibration assumptions.

**Proof.** The first |P| prefixes contribute J(P). Each of the |Q| later prefixes equals D(P) plus the corresponding prefix of Q, giving (1). Formula (2) follows by reduction; expanding the third coordinate of a triple product shows its two bracketings both equal c+f+h+d*b+g*(b+e). Direct multiplication verifies (3). The commutator is central and determined by d*b-a*e, establishing nilpotency class at most two. QED.

## 3. R171B: minimal quotient for arbitrary left/right path contexts

Define for arbitrary P,Q in A*:

    P equivalent_q Q  iff
    J(XPY)=J(XQY) mod q for every X,Y in A*.

**Theorem (exact if-and-only-if).** For every q>=2,

    P equivalent_q Q  iff  K_q(P)=K_q(Q).            (4)

The three contexts (X,Y)=(empty,empty), ((+E_1),empty), and (empty,(+E_1)) suffice to decide equivalence, for any six-axis paths. Consequently the image K_q(A*) is the *minimal deterministic two-sided context-safe quotient* for the declared mod-q vector-J observer; the image size, rather than the ambient group order, is the correct minimal state count if the generator image is proper.

**Proof.** Twice applying (1) and subtracting gives

    J(XPY)-J(XQY)
      = J(P)-J(Q) + (|P|-|Q|)D(X)
        + |Y|(D(P)-D(Q)) mod q.                      (5)

Equal K_q makes this identically zero. Conversely, empty contexts force equal J modulo q. Left context (+E_1) forces (|P|-|Q|)E_1=0 in G_q, hence equality of lengths modulo q. Right context (+E_1) forces equality of displacement vectors modulo q. Thus (4). Any quotient preserving all such contexts must separate each inequivalent image state, and K_q itself is such a quotient. QED.

The same argument with Z^6 instead of G_q proves the unmodded exact statement P equivalent_Z Q iff K_Z(P)=K_Z(Q), now with an infinite countable state space. It provides a minimal sufficient observable state, not the full raw ordered-path identity.

## 4. R171C: sharp odd-modulus state count; q=3 signed distinction

**Theorem.** For every odd q>=3, the path-generated image K_q(A*) is the entire ambient H_q^6, so the exact minimal number of context states is

    |K_q(A*)|=q^13.                                 (6)

In particular q=3 distinguishes +E_i from -E_i and has exactly

    3^13 = 1,594,323

context-distinct reachable states.

**Proof.** Work in the finite group (2). Let A_i=K_q(+E_i)=(1,E_i,E_i) and B_i=K_q(-E_i)=(1,-E_i,-E_i). Their products are

    A_i B_i=(2,0,E_i),  B_i A_i=(2,0,-E_i).

Therefore the subgroup generated by signed primitive steps contains every central element (0,0,2E_i), by multiplying the first product by the inverse of the second. Since 2 is invertible modulo odd q, it contains (0,0,E_i) for all i. Removing the central E_i from A_i B_i supplies (2,0,0), whose suitable power supplies (1,0,0). Multiplying A_i by the inverse of this pure-length element on the right supplies (0,E_i,0). The pure-length, all pure-displacement, and all central generators generate all q^13 triples.

Finally, the subgroup generated by A_i,B_i equals the **positive-word** image: each generator lies in a finite group, so its inverse is a positive power of that generator. Thus no inverse direction unavailable in A* was used in the reachability conclusion. QED.

For even moduli, the image may be proper; (4) remains exact. The code checks selected even-q cases without asserting an unsupported all-even formula.

## 5. R171D: a native-path counterexample to exporting R170's single bit

Declare the lossy binary sign projection b(+E_i)=1, b(-E_i)=0 for every i. Take two legal two-step paths from the same chosen Cell anchor:

    P=(+E_1,-E_1),   Q=(+E_2,-E_2).

Both binary projections are 10 and hence have the same scalar Sturmian phase signature S_2 and the same R170 parity repair H_2 (indeed all R170 K coordinates match). Both have |P|=|Q|=2 and D(P)=D(Q)=0 in native Z^6. But

    J(P)=E_1,   J(Q)=E_2.                            (7)

Thus (b-word scalar S, R170 H, native endpoint) is not sufficient for the declared port-resolved J observer, even at a single present observation. This is an exact witness for retaining a joint signed-axis/path residual when transferring scalar repair schemes into P000. It does not assert a failure of R170's proved scope on its own binary-Sturmian word identity domain.

No primitive two-force equilibrium or full internal-time return is inferred from the two-step spatial loops.

## 6. Exact computation, cost, and status

Companion executable: research_notes/portable_direct/R171_signed_path_cocycle_check.py.
Companion output: research_notes/portable_direct/R171_signed_path_verification.json.

Independent pure-integer checker validates (1)/(2) on 116,281 concatenation pairs for signed two-axis subalphabet, (4) via the three separating contexts on 7,225 pairs of words length <=3, and generator reachability for q=3 with 1,2,3 signed axes (27,243,2187 states) and q=2 with 1,2,3 axes (4,16,64 states). It also checks the full six-axis integer counterexample (7). All tests passed. These finite tests audit the implementation; full six-axis and arbitrary odd-modulus results follow from the algebraic proofs.

Computing full integer D,J requires one prefix scan of m steps, with O(6m) arithmetic operations and values bounded in magnitude by O(m^2). The q-residue sketch updates in O(6) modular operations per appended signed step. The bit cost depends on q and the encoded integer sizes. These statements cover construction and reading of K, not BRC amplitude computation or recovery of raw path identities.

Source status: author's complete symbolic proofs; exact program checks performed; independent proof review and formal checker not run. No Result, Review, Working Truth, or Foundation admission claimed.

## 7. Research continuation

1. Develop and validate the *actual* native BRC signed-port/branch observer, including weights, labels, multiplicity and allowed updates. Use the precise population/operation map to test whether vector-J plus endpoint suffices, or construct a second independent provenance-residual witness.
2. Characterize the image and minimal state count of K_q(A*) for even q (the present checker documents q=2 small-d data), and study finite-window versus unbounded-context observer requirements.
3. Compare q=3 six-axis context quotient with original R170's eight-state binary identity repair only after fixing a common observer and representation map; state compression benefits within their actual observer scopes.

No source-input pins were rebased. The original R170 proof and status remain unchanged.