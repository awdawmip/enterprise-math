# D25/LIFT — exact even-Frobenius / odd-second-digit fiber obstruction (2026-10-28)

Status: AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. Existing shared D25 author context, not independent reviewer. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Exact typed model and observer
For any prime p≡13 or 19 (mod24), Legendre (2/p)=-1. Work only in the **auxiliary** unramified quadratic ring R₂=(Z/p²Z)[T]/(T²-2), with involution σ(T)=-T, pinned ordered basis (1,T) and pinned vector e=1. Set, for a,b∈F_p,

η_(a,b)=1+p(a+bT),   F_(a,b)(x)=η_(a,b) σ(x).

η is a unit and F is σ-semilinear. These objects are **not** the original H0/B0 or any already-authenticated native crystalline/Frobenius module. The even observer is F² modulo p², optionally its trace/determinant and F mod p. The declared future operation is the **pinned** odd p-second-digit coefficient χ(F)=[T](F(e)-e)/p mod p; it is *not* gauge invariant without a fixed generator/normalization.

## Universal theorem and proof
For every target prime p and all a,b,

F_(a,b) mod p = σ,
F_(a,b)² = (1+2pa)·id mod p²,
χ(F_(a,b)) = b mod p.

Indeed F²(x)=ησ(η)x, with ησ(η)=(1+pa)²-2p²b² ≡1+2pa (mod p²), while F(1)=1+p(a+bT). In the pinned (1,T) basis,

[F]=[[1+pa,-2pb],[pb,-1-pa]] (mod p²),

with trace 0 and determinant -(1+2pa), independent of b. Consequently each fixed tuple (F mod p,F² mod p²,tr,det) within this declared (a,b)-family has **exactly p distinct pinned odd-jet outputs**, one for each b∈F_p. Conversely a is uniquely recovered from the even normalized jet ((N(η)-1)/p)·2^{-1} mod p, and b is χ. Thus one extra F_p-valued odd repair coordinate is both sufficient and necessary to distinguish all p source states under this declared observer/future-operation lease. The even observer alone does **not** factor χ.

Explicit witness: η+=1+pT and η-=1-pT have the same F mod p, F²=id mod p², trace=0, determinant=-1, yet χ+=1 and χ-=-1 mod p. At p=373 (p²=139129), χ are 1 and 372 mod373. This is a rigorous model-fiber counterexample to any *unqualified universal* odd-jet decoder from those even data alone; it neither proves nor refutes the original LIFT/JT2 assertion.

## BRC preservation, exclusions and native acceptance gate
Population: labeled pairs (a,b) with operation F and basis e; even quotient forgets b; nonconstancy of the future signed observer χ across its fiber is an exact BRC non-descent witness. Relative to this observer a one-field-element repair suffices; it does not imply universal irreducibility, geometry of native six-dimensional Heartbeat X6, or physical validity. In particular, equal-norm operators may be gauge-equivalent: χ depends on the pinned generator, hence native gauge/η and signed odd Hesse/Green observer require separate verification.

**Not demonstrated:** native H0/B0 rank one, original CM class, its semilinear direction/η, an η-to-W_p map, original Δ_p−R_p or p373 [X]U modulo p². These remain responsible-owner/native experimental gates in existing issue #1559 (PENDING_OWNER / NOT_RUN), not this auxiliary calculation. A true original-class rigidity rule could determine b from additional source structure; no negative conclusion about such a rule is drawn.

Exact standard-library checker d25_frobenius_even_odd_jet_fiber_checker_20261028.py and author-side PASS JSON cover 6520 typed cases over p=13,19,37,43,109,211,373. The proof above covers all target p independently of finite tests. No native CLAIM, OPEN, checkpoint or independent mathematical review is asserted.

UR V2 original remains a separate hash/provenance debt: 94687 bytes; expected SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76. On a CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS Source seed, predecessor completed_units=[] and all input artifacts require full readback before typed continuation_prepare.

**Next discriminating action:** obtain actual authorized original H0/B0 p373 normalized Frobenius and signed odd observer under #1559; then test whether original-class constraints bind the odd second digit b to even data or demand a separate signed port. Do not replace a native result with this ring witness, a scalar W_p regression or a provisional author PR.


## Exact gauge-orbit corollary (second verified unit)

Fix a,b,c in F_p and let u_c=1+pcT. In R₂, σ(u_c)^{-1}=u_c modulo p². Conjugating the **semilinear** operator with this unit gives

u_c F_(a,b) u_c^{-1}(x)
 = u_c η_(a,b) σ(u_c)^{-1} σ(x)
 = η_(a,b+2c) σ(x)
 = F_(a,b+2c)(x)  (mod p²).

Since 2 is invertible modulo p, these changes act **transitively** on all p distinct pinned b labels with fixed a/norm. Thus the b-coordinate is not gauge-invariant for an *unmarked* semilinear module. The previous exact non-descent theorem is deliberately for the **pinned generator/odd readout**; treating its b labels as p physically distinct Frobenius modules without an anchor would be invalid.

Native implication: the original H0/B0 task must provide an actual basis/marked-section normalization and a corresponding signed Green/Hesse observer (or a separately proved genuinely gauge-invariant odd quantity). Merely supplying a rank-one norm/F² scalar cannot justify a pinned odd second-digit output. Conversely, this toy gauge equivalence does NOT prove that the authentic native odd source channel is pure gauge or zero.

The standalone checker also directly verifies this conjugation formula for all 6520 tested (p,a,b) pairs by selecting c=a+b+1 modulo p. These are author-side exact checks; the displayed algebra proves the full target-prime statement.
