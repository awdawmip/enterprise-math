# Fermat residual lift: exact local precision-preservation lemma (2026-11-20)

Scope: odd prime p, unit residue r in F_p, quadratic iteration x_{j+1}=x_j^2. This is a conditional, classical p-adic observation; it is not a new factor-finding algorithm or an accepted Enterprise Math result.

## Exact statement

Let x_0,y_0 be integers with x_0 congruent to y_0 congruent to r (mod p), where p is an odd prime and r is nonzero mod p. For all j >= 0,

  v_p(x_j-y_j) = v_p(x_0-y_0),

with v_p(0)=infinity and x_{j+1}=x_j^2, y_{j+1}=y_j^2.

Proof. The iterates x_j,y_j are congruent to r^{2^j} (mod p), which is a unit. Thus x_j+y_j congruent to 2 r^{2^j} (mod p), also a unit because p is odd. The factorization x_{j+1}-y_{j+1}=(x_j-y_j)(x_j+y_j) therefore preserves p-adic valuation exactly. Induct.

Consequences for every k >= 1:
(1) On each fixed nonzero residue class mod p, the map x mod p^k -> x^{2^j} mod p^k is injective, and hence bijective on that class's p^{k-1} possible lifts onto its image residue class. The number of possible states remains exactly p^{k-1}.
(2) A full terminal residue x_j mod p^k requires discrimination among p^{k-1} lifts of an initially unspecified unit input in that residue class. A representation of all such residues therefore needs at least (k-1)log2(p) bits of information (or ceil((k-1)log2 p) bits for fixed-length binary coding). This is a *full-residue reconstruction* lower bound for this input class, not a general lower bound for every divisibility decision or for the fixed starting value x_0=2.
(3) With any fixed residue section s_j congruent to x_j mod p and x_j=s_j+p A_j, the quotient A_j mod p^{k-1} is a sufficient and, for complete reconstruction of the family, cardinality-optimal coordinate. Under changing section s_j'=s_j+p t_j, A_j'=A_j-t_j, preserving the represented x_j exactly.
(4) At a terminal index n with x_n congruent to -1 (mod p), choose s_n=-1. Then p^k divides F_n=x_n+1 precisely when A_n is zero mod p^{k-1}; this is an exact readout identity under the stated chosen section.

Boundary: if the common residue is 0 mod p, x+y is divisible by p, and the isometry claim fails; valuations can increase. If p=2, 2r is not a unit, so the proof does not apply.

Provenance/novelty: elementary factorization and local p-adic unit calculus. Useful as a precision_cost scope certificate for RS-FERMAT-RESIDUAL-LIFT-20261004. Does not establish global primality properties or whether the Fermat number has a repeated prime factor.
