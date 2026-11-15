# R170 — A universal one-bit phase-signature repair and exact concatenation cocycle

Date: 2026-11-15 (Asia/Shanghai). Research status: AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED.
Source: independent portable research; frozen scientific input pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Scope: the external finite-binary-Sturmian tied-phase observer, *not* a native BRC signed-amplitude/port or X6 observer. This extends the exact two-to-one/chord theorem R162 (immutable `f451da2665923179eed166c488a1e8063222ca29`) and the collision examples R169 (immutable `1a5bcc8d759bffd68acbd0e5568d704ba96f35fb`).

## 1. Exact problem and universal repair

Fix any integer m>=1. For an admitted binary word w=w_1...w_m, let p_0=0, p_i=sum_{k=1}^i w_k, and let S_m(w)=(alpha,beta,U,V) be the exact phase signature from R162, equivalently the unscaled version (alpha,beta,1+A,B) of R169.

Define the **single parity repair bit**

    H_m(w) = (sum_{i=1}^m p_i) mod 2
           = (sum_{k=1}^m (m-k+1)w_k) mod 2.

**Theorem R170A (global injectivity).** For every m>=1, the map

    w |-> (S_m(w), H_m(w))

is injective on *all admitted finite binary Sturmian words of length m*. Thus a uniform one-bit positional checksum, defined without first decoding S_m or identifying the ambiguous index, repairs every exact signature fiber of every length. The same bit works simultaneously for all possible phases and both terminal and internal collision cases.

**Proof.** By the full-length chord theorem R162A, if admitted distinct words u,v share S_m, their prefix-sum vectors differ by exactly +1 or -1 at one unique index j and coincide at all other indices. Consequently

    H_m(u)-H_m(v) = p_j(u)-p_j(v) = +/-1 (mod 2),

so their parity bits differ. The proof includes the R162 j=m terminal case, which is handled by the same sum. Therefore no two distinct words can share the augmented signature. QED.

R162 already implies the *existence* of a one-bit index-dependent recovery coordinate w_j. R170A supplies the additional uniform, decoder-independent, linear parity formula.

**Sharpness as an information bound.** The unaugmented observer has an actual two-word fiber: for m=1, the admitted words 0 and 1 share S_1, while H_1(0)=0 and H_1(1)=1. Further nontrivial fibers exist at infinitely many m by R169 (m=2k+3, k>=2). Any exact identity-repair alphabet for a given two-word fiber must have at least two values; the parity bit meets this lower bound. This is an exact one-bit minimum relative to this declared fixed-length identity observer, not a compression claim for unrelated future native observers.

## 2. Exact concatenation law: a finite noncommutative monoid

For *any* binary words u and v (admissibility not needed for this algebra), let
m(w)=|w|, N(w)=sum_i w_i and H(w)=sum_i p_i(w) mod 2.
Directly enumerating prefixes of uv gives

    H(uv) = H(u) + H(v) + |v| N(u)      (mod 2).           (1)

Proof: prefixes within u contribute H(u). Each prefix of v after u has the form N(u)+p_i(v). Summing these |v| terms contributes |v|N(u)+H(v). QED.

Thus the three parity coordinates

    K(w)=(m(w) mod 2, N(w) mod 2, H(w))

obey the closed, exact multiplication

    (a,b,c) * (d,e,f) = (a+d, b+e, c+f+d*b)   (mod 2).    (2)

**Theorem R170B.** The eight-element carrier (Z/2)^3 with (2) is an associative monoid, identity (0,0,0), and K(uv)=K(u)*K(v). Associativity follows because the third coordinate of (x*y)*z is c+f+i+d*b+g*(b+e), which equals the third coordinate of x*(y*z), namely c+f+i+g*e+(d+g)*b. All arithmetic is modulo 2.

**Order-sensitive residual.** In particular,

    H(uv)-H(vu) = |v|N(u)-|u|N(v)  (mod 2).               (3)

Taking u=1 and v=0 gives H(10)=0 and H(01)=1, proving noncommutativity of K's image. This is a finite, explicit, compositional joint/order residual, without identifying it with signed BRC amplitude or native X6 path semantics.

## 3. Strong preservation along shared suffixes

**Theorem R170C (collision-pair suffix persistence).** Let m>=2 and let distinct admitted u,v of length m share the same phase signature. Their prefix defect is at an internal j<m, with equal total counts N(u)=N(v). For *any* common appended binary suffix z, of any finite length, equation (1) yields

    H(uz)-H(vz) = H(u)-H(v) = 1  (mod 2).

This identity remains true regardless of whether uz and vz remain Sturmian-admitted or have equal/unequal scalar signatures after appending. It is a statement about the retained parity residual on raw words, and does not rely on the scalar phase signature remaining defined. It distinguishes precisely the internal-exchange pairs considered in R166–R169.

Proof: R162A says a unique internal prefix differs by 1, hence N(u)=N(v). Subtract (1) for uz and vz; the suffix H(z) and length-count cross term cancel. By R170A their initial parity difference is 1. QED.

The j=m terminal case of R162 is already covered by R170A for its original length; the stated suffix-invariance theorem is deliberately restricted to pairs with equal final counts.

## 4. Recoverability and computational cost

The parity bit H can be accumulated in O(m) bit or integer operations from the original binary word using a running prefix count. For streaming append of e at current length m, with current count N,

    N' = N+e,    H' = H + N+e (mod 2),    m'=m+1.

All three parity sketch coordinates update in O(1) bit operations per appended symbol; two stored parity bits N mod 2 and H plus m mod 2 suffice for the sketch. To update the entire exact rational phase signature S_m requires separately maintaining/deriving its own exact data; R170 makes no constant-time claim for this more expensive component. Existing R164 supplies a constructive decoder for valid (S_m,H_m) by testing the at-most-two reconstructed candidates against H.

Arithmetic complexity for the full observer includes constructing S_m and any needed candidate reconstruction; the one-bit repair itself is linear-time from the word and constant-time per append with its small sketch.

## 5. Independent exact verification

Executable file `R170_parity_repair_check.py` uses Python integer arithmetic and `fractions.Fraction` (no floating point) to enumerate *every* binary word at lengths 1..15, compute the exact all-factor slope support and endpoint signature, and group all admitted words by unaugmented signature. For each of 1,760 signature classes it checks no more than two preimages and distinct H for any doubleton, comparing H with an independent prefix-count implementation. It independently checks the one-index defect of doubletons, plus the composition law on 4,464 doubleton-with-short-suffix cases and 960 three-block associativity instances. Result: 65,534 candidate words, 1,906 admitted words, 146 two-word fibers, zero repair collisions, and only one observed terminal alias (m=1). Result marker: `R170_UNIVERSAL_PARITY_REPAIR_EXACT_PASS` and dataset `R170_parity_verification.json`.

The exhaustive checks establish the finite range; the unlimited-length claims follow from R162A and the direct algebraic proof above. R162's underlying author proof is an explicit mathematical dependency, not independent review. Formal checker and independent mathematical reviewer: NOT_REVIEWED / NOT_RUN.

## 6. BRC and P000 meaning; next question

For the declared external binary-word observer, (S_m,H_m) is exactly lossless for word identity and K preserves order under concatenation with an explicit cocycle. These findings instantiate the residual-fidelity method without promoting an external scalar toy model into native BRC or the locked P000 ontology. A native signed-port transfer would require an explicit population/port observer and proof of preservation under its admissible branch/path updates, including multiplicity and provenance.

Next scientific unit: determine whether a truly reduced *native typed signed-port/path observer* admits this 1-bit cocycle as a complete residual under explicitly chosen operations, or provide a counterexample showing a second provenance coordinate is required; separately investigate sharper lifetime extremals of R169 at fixed length/weight.

Publication/status: independent non-overwriting portable research; neither a formal CLAIM nor a Result, Review or Foundation promotion. Activity association requires a currently authenticated own session/author record and an exact observed source readback.
