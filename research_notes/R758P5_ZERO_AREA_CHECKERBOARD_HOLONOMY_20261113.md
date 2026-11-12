# R758P5 — Minimal zero-area nontrivial S3 holonomy and checkerboard BRC flux

Date: 2026-11-13 Asia/Shanghai. Status: exact author-side candidate-model theorem (not an admitted native TRIADIC_CLOSURE_E event). Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Prior verified frontier: R758P3 PR #2204 @9e010eb25d64205dfc2ea3b94e88602d53f45656 and R758P4 PR #2208 @2f18520361adc259323674007dc684d23116e045.

## 1. Declared model and exact result

Fix a root Cell in the P000 six-axis signed spatial torsor, select a three-axis research slice with axis labels a=0,1,2, and hold the other three native coordinates fixed. A rooted spatial path is a word of signed native unit moves (a_j,eps_j), eps_j=+1 or -1. A closed path has total signed displacement zero in each axis and therefore even length.

Use the *candidate* S3 connection from R758P3–P4: T_a=s r^a, with r^3=e, s^2=e, srs=r^{-1}. Positive and negative steps on the same axis share T_a, an involution. Later actions multiply on the left. For closed words define

- A_ab(w) = sum over steps j along axis b of x_a(j-1)*eps_j for a<b, with x measured from the chosen Cell. Set A=(A_01,A_02,A_12).
- q(w)= sum over j of (-1)^(j-1)*a_j modulo 3.
- H(w)=T_last ... T_first=r^{q(w)} (exact group normal form).

**Theorem A.** Among *all* rooted closed signed-unit paths in this three-axis slice, including paths with repeated Cell visits and arbitrary axis multiplicity, the minimal length with all three signed projected areas zero but final frame H(w) nonidentity is **8**.

Take

    W=(+0,+1,-0,-1, +0,-1,-0,+1)
    V=(+0,-0, +0,-0, +0,-0, +0,-0).

W is two four-edge Cell-return squares: the first contributes A_01=+1, the second A_01=-1. Thus A(W)=0 and native displacement=0. The unsigned axis sequence for each square is (0,1,0,1), so q(square)=0-1+0-1=-2=1 (mod 3), yielding q(W)=2 and H(W)=r². V also has zero displacement and A(V)=0, but q(V)=0 and H(V)=e. Both have length 8, identical Cell and area observations, and different S3 conjugacy classes.

**Theorem B (complete short-word classification).** Exhausting all distinct rooted signed-unit closed words in the fixed three-axis slice gives:

| Word length | All closed words | Area=0 and H=e | Area=0 and H=r | Area=0 and H=r² |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 | 0 |
| 2 | 6 | 6 | 0 | 0 |
| 4 | 90 | 66 | 0 | 0 |
| 6 | 1,860 | 876 | 0 | 0 |
| 8 | 44,730 | 12,882 | 48 | 48 |

All 96 length-eight flat nonidentity words use exactly two distinct axes, with each axis occurring twice positively and twice negatively. Each of the three unordered axis pairs contributes 32 such words, split 16 with H=r and 16 with H=r². The 46,686 nonempty words in lengths 2,4,6,8 were all tested by exact integer and S3 permutation operations.

**Coverage proof.** A length-2k signed unit path closes iff for each a, the number of positive a occurrences equals the number of negative a occurrences. Choose the multiset of k axis labels in {0,1,2}, add one +a and one -a for each selected occurrence, then enumerate every distinct permutation of that multiset. This yields each and every rooted closed path exactly once; no random or bounded-coordinate sampling is involved. Hence exhaustive zero-area triviality for lengths 0,2,4,6 establishes minimality of the explicit eight-step W.

**Corollary.** For each m>=1, W^m returns to the same Cell with A=0 and H=r^{2m}. For every even L>=8, append (L-8)/2 immediate backtracks (+0,-0) to both W and V: equal length, signed projected area, native displacement and endpoint remain fixed while the frames stay different.

## 2. A geometric explanation: parity-weighted face flux

Let p(x)=sum_{a=0}^2 (x_a-c_a) mod 2 be the bipartite Cell parity relative to the root. To a signed directed unit edge x -> x+eps*e_a assign the Z3 voltage

    omega(x -> x+eps*e_a) = (-1)^{p(x)} * a  (mod 3).

The reversed edge has the opposite voltage, because parity flips on every primitive unit step. On a rooted path the edge voltages add to q(w). In particular the oriented elementary ab plaquette based at its lower-left vertex x, with boundary (+a,+b,-a,-b), has circulation

    d omega(square_ab(x)) = 2 (-1)^{p(x)} (a-b)  (mod 3).

In contrast, the standard signed ab area contributes +1 on each positively oriented ab plaquette, independent of parity. For any finite oriented cubical 2-chain Sigma with boundary w, exact discrete Stokes gives

    q(w) = sum_{a<b} 2(a-b) * sum_{ab faces f in Sigma} eps_f*(-1)^{p(v_f)}  (mod 3),
    A_ab(w) = sum_{ab faces f in Sigma} eps_f.

Here v_f is the coordinate lower-left vertex of face f and eps_f its signed orientation. The combined checkerboard-weighted flux is independent of the chosen surface because it equals the boundary evaluation of omega. Individual checkerboard-separated ab-face counts need not be separately independent of the chosen 3D filling. The witness W cancels ordinary +1/-1 area while retaining a nonzero parity-weighted circulation. Thus this BRC residual is geometrically typed, not an arbitrary bit attached to a discarded path.

For any pair of closed paths u,v based at the same Cell, A(uv)=A(u)+A(v) and q(uv)=q(u)+q(v) mod 3. Consequently (A,q) is an exact sufficient state for the declared future observables (all signed projected areas and S3 final frame) under concatenation of closed loops. At length 8 the A=0 fiber contains three distinct q values, proving a three-state lower bound for any exact frame-recovery quotient on that fiber (2 bits fixed binary coding). This quotient is observer-scoped; source order and branch multiplicity remain separately available for other operations.

## 3. Evidence and next scientific action

Verification source: VERIFY_ZERO_AREA_MINIMAL.py (stdlib only), output EXACT_OUTPUT.json. The checker uses exhaustive multiset permutations for all closed words up to eight steps, integer area sums, and *independent full S3 permutation multiplication* to cross-check the r^q formula for each word. It asserts the totals, all flat-fiber counts, all three axis-pair anomaly counts and equal-length counterexamples. No approximate arithmetic is used.

The native question remains whether some *actually admitted* P000 TRIADIC_CLOSURE_E Cell/Link/Port event, V29 updates and V39 based-loop frame transport induce this or any other parity-voltage residual. The declared signed-unit spatial loop is not itself a primitive three-force balance event. Preserve frozen science, P000 and current ACTIVE worldview. Formal CLAIM/Source Result and independent Driver review are separate current-authority operations; publication of this author-side proof does not assert them.
