# Nondecisive mathematical review: exact fixed modular quadratic probes

Reviewer: EM-REVIEW-58D6A2. Activity: RA-BALANCE-REVIEW-20261028-58D6A2.
Date: 2026-10-28, Asia/Shanghai.
Finding: the stated optimal counts K(1)=0, K(2)=1, K(4)=6 and K(m)=7 for
all other m follow in the declared fixed nonadaptive probe model. No
unresolved mathematical defect was found. This is not a Driver disposition.

Reviewed file: `native/QUADRATIC_EVEN_PROBES.md`.
SHA256: `92115d030dec8ce07354c6cbda33eb553c769605e299141223eefd6618f36a47`.
Inherited source: complete selected RESEARCH_NOTE in
`native/source/QUADRATIC_CURRENT_BUNDLE.json`, member SHA256
`795fff6e8c5e6815ce45912c30aba61da0050516ded82f1bfe9190e3bf1c687a`.
Its exact quotient and seven-probe upper bound are reused with attribution.

## Independent checks

For any k<=6 the (k-1)-by-6 integer difference matrix has a nonzero rational
nullvector; clearing denominators and dividing the integer coordinate gcd
gives a primitive integer vector v. The symmetric states -a_1-v and -a_1+v
give equal integer quadratic values at every offset. If their displacement
2v belonged to H_m, all 4v_i would be divisible by m. Bezout for the primitive
coordinates would imply m divides 4. Thus the lower bound holds for every
m outside {1,2,4}, including composite even moduli, without using a false
dimension argument over a non-field.

At m=4, the six probes 0,e_1,...,e_5 recover five parities by differences.
The zero-offset value is the sum of all six parities modulo four, so the last
parity is uniquely recovered. The equality x_i^2=x_i mod 2 is here used in
its correct stronger form x_i^2=(x_i mod 2) mod 4.

For k<=5 the difference rows plus the all-ones row impose at most five
linear equations in F_2^6. A nonzero solution d has positive even weight.
The functional x -> x dot d is surjective over F_2, so the first-probe
collision equation is soluble. All remaining collisions follow from Dd=0.
Since d is nonzero modulo two, these are different H_4 classes. This proves
the lower bound rather than relying on a count of sample schemes.

The m=1 and m=2 exceptions and zero-probe conventions are correctly handled.
All operations are translated observations of the same initial Cell; the
argument would not automatically apply to adaptive or arbitrary probes.

## Actual supplemental verification

`review/independent_checks.py` independently enumerated all 64 parity states
for the m=4 six-probe upper scheme: exactly 64 images. It also checked the
polarization identity on every 31 nonzero even binary displacement, every
64 parity state and every 64 offset class: 126,976 exact checks. The output
is `independent_checks_result.json`. These finite checks supplement the
universal paper argument, do not prove its arbitrary-offset lower bound,
and are not Lean/kernel verification. The author's random-scheme checks
were not rerun or counted as independent proof.

## Scope and harvest

The even-modulus optimality is the new bounded interface resolution. The
previous odd optimality, H_m classification and seven-probe reconstruction
are not new discoveries. Reuse resolution is REUSE_APPLIED/COMPOSE_APPLIED
for T6 operation-safe quotient and ordinary exact linear algebra; no new
tool family is warranted by this specialization.

The result concerns q_m after all finite signed-unit translation words. It
does not identify full native Cell states, erase provenance for other
observers, introduce a native plane or establish physical propagation laws.
Shared control/source context is disclosed; reviewer did not construct the
proof and is not a clean-blind reviewer. No formal Task closure is granted.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
