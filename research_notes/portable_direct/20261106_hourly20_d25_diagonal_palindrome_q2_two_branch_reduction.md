# D25: prime-square diagonal palindrome and one-scalar second-digit factor

Date: 2026-11-06. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; exact publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific input `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Author-side portable research, **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**. Original p=373 H0/B0, Frobenius and eta/kappa remain separate Source obligations.

## Previously established input

[
C_n=sum_{k=0}^{2n}(6k+1)(-1)^k2^{2n-k}inom{2n}{k}inom{3n}{k}inom{4n}{k}.
]
For any prime q>=5, write n=qN+r (0<=r<q), s_i=ir mod q and M_i=iN+floor(ir/q), i=2,3,4; a=-1/2 modulo q^2. The previously published, author-derived signed two-digit Lucas theorem (research_notes/portable_direct/20261106_hourly20_d25_lucas_q2_two_moments.md) gives
[
C_nequiv 2^{2(N+r)}[LT+q(AT+BT_1)]pmod{q^2},
]
with u_j=a^j prod_i binom(s_i,j), v_l=a^l prod_i binom(M_i,l), L=sum_j(6j+1)u_j mod q², T=sum_l v_l mod q², T1=sum_l l v_l mod q, and the explicit harmonic/carry/Fermat coefficients A,B in that cited theorem. Its proof and status are inherited, not recredited.

## New theorem: diagonal digit palindrome

Take **n0=(q²-1)/6** (integer for every prime q>=5), and define U=sum_j u_j mod q², D=sum_j j*u_j mod q, Z=U mod q. The high and low **multisets** (M2,M3,M4) and (s2,s3,s4) are identical:
- q=6b+1: N=r=b and both multisets equal {2b,3b,4b}.
- q=6b+5: N=b,r=5b+4; high {2b+1,3b+2,4b+3}; low {4b+3,3b+2,2b+1}.

Consequently v_j=u_j term by term (including its signed power) modulo q², hence T=U (mod q²), T1=D (mod q) and **L=U+6D** (mod q), where the last congruence is enough. Suppose the exact first-digit premise **L=0 mod q**, and write lambda=L/q (mod q) using the representative L mod q². Then D=-Z/6 (mod q), and direct substitution into the earlier q² theorem proves
[
oxed{ C_{n0}/qequiv 2^{2(N+r)}, Z,(lambda+A-B/6)pmod q. }	ag{DP}
]
All divisions by 6 are valid because q>=5 is prime. Therefore, **under L=0 mod q**,
[
oxed{q^2mid C_{n0}iff Z(lambda+A-B/6)=0pmod q.}	ag{DP2}
]
In particular, Z=0 implies q²|C_n0 without needing to determine A or B. The second-digit two-high-moment criterion has become a one-scalar **two-branch** problem, preserving the signed low digit, unique carry origin and high/low observer identity.

## Additional Clausen-square specialization, q=6b+1

Let H(z)=sum_{j=0}^{2b}(-1)^j binom(2b,j)binom(3b,j)binom(4b,j)z^j. Define
[
G(z)={}_2F_1(-b,-2b;	frac12-3b;z).
]
Clausen's terminating square identity with a=-b, b'=-2b gives
G(z)^2={}_3F_2(-2b,-3b,-4b;-6b,	frac12-3b;z).
For q=6b+1, each lower parameter equals 1 mod q; all relevant denominators up to degree 2b are q-units. Thus **coefficientwise in F_q[z]**,
[
H(z)=G(z)^2,quad
G(z)equivsum_{j=0}^binom bjinom{2b}jz^j.
]
At z=1/2, Z=H(1/2)=G(1/2)^2 and D=(zH'(z))_{z=1/2}=G(1/2)G'(1/2), so L=G(1/2)[G(1/2)+6G'(1/2)] mod q. In this prime class the **Z=0 branch is exactly the G=0 branch**. This is a reuse of the earlier Clausen identity with a new diagonal-prime-square consequence; no claim of first discovering Clausen's identity.

## New finite evidence and next proof obligations

An independently executed standard-library exact-integer verifier checked all **166 primes 5<=q<=1000** by evaluating L,Z,D,A,B from the published two-digit formula, the palindrome and DP. For every one, L=0 and
[
lambda+Aequivepsilon_q,qquad Bequiv6epsilon_qpmod q,qquad
epsilon_q=+1;(q=1mod6),;-1;(q=5mod6).
	ag{E-observed}
]
These are **new conjectural universal identities**, not yet generally proved. They imply DP2 for all q if proved. The 166 primes split into **90** cases Z=0 and **76** cases Z!=0. In the tested range, Z=0 exactly for q mod24 in {13,17,19,23}, consistent with (-6/q)=-1; this residue-class characterization is also conjectural beyond the finite test.

The verifier separately computed the original integer-binomial C_n0 (not merely the two-moment formula) for all 12 primes 5<=q<=43 and matched zero mod q², and checked the full two-moment/DP congruences for all 166 primes. Exact modular inverses, integer binomials, source-specific carry K_i and Fermat/harmonic terms were retained. These counts are finite evidence only.

**Next smallest independent proof task:** derive the two low-digit finite-sum identities (E-observed), using contiguity/WZ certificates or reflection of the unique carry channel. Alternatively prove the Z=0 condition for (-6/q)=-1. Either would advance the universal q² base, which together with the previously proved prime-square transport supplies infinite families. A connection back to the frozen D25 original F,H second-digit ports needs a separate source-preserving derivation, not just this integer-shadow congruence.

Control: historical old-session staging and service identity remain protected/unverified; this artifact is author-side durable evidence, not a native execution or mathematical admission. No old claim/session/run or Source checkpoint is updated by the artifact.
