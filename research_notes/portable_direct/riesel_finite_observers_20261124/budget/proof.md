# Sharp exponential order scale for finite exact budget observers

Status: author mathematical synthesis of the new fixed-observation construction and the already published finite-budget theorem. Researcher `EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`. No independent project Review, Foundation promotion, formal verification, or priority claim is asserted.

## 1. The observable and the quantity being minimized

Retain the square-Riesel sequence

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1,
\]

the old twenty-prime dictionary P, its product M, and the fixed 29-channel root fiber R1 defined in the companion `../finite/proof.md`. Let \(\delta_P(a)\) be the minimum number of primes outside P in a proper-prime cover; its value is infinity when no finite cover exists.

For an integer N at least one, set

\[
B(N)=\max\bigl(\{1\}\cup\{\operatorname{ord}_q(2):
q\text{ is an odd prime dividing }N\}\bigr).
\tag{1}
\]

An N-observer is **budget-b sufficient on R1** when the truth value of

\[
\delta_P(a)\le b
\tag{2}
\]

is constant on every intersection of R1 with a root congruence class modulo N. Define

\[
\Omega_b=\min\{B(N):N\ge1\text{ is budget-b sufficient on R1}\}.
\tag{3}
\]

Section 3 supplies such an N, so this minimum exists. The quantity is the largest base-2 multiplicative order among the observed odd primes. It is not the number of primes, the size or bit length of N, the full orbit period modulo N, a numerical factorization cost, or an execution-time bound. Repeated prime powers affect the residue precision but do not change (1).

**Theorem.** For every integer b at least 14,

\[
\boxed{\frac{27}{512}\,2^b\ \le\ \Omega_b\ \le\ 105\,2^b.}
\tag{4}
\]

Thus

\[
\Omega_b=\Theta(2^b),\qquad \log_2\Omega_b=b+O(1).
\tag{5}
\]

The exponential rate is sharp in this precise sense. Neither multiplicative constant in (4) is claimed optimal.

## 2. Lower bound: opposite budget outcomes in one observation

The companion fixed-observation theorem proves that, for every N, there is one root class modulo N inside R1 containing infinitely many roots of each exact additional cost

\[
s\ge s_N=k_N+12,
\quad
k_N=\min\{k\ge2:216\,2^k>B(N)\}.
\tag{6}
\]

All these roots also have exact total covering cost \(20+s\). The root class in this statement is chosen before s varies.

Suppose b is at least 14 and an N-observer is budget-b sufficient. If

\[
B(N)<216\,2^{b-12},
\]

then the admissible choice \(k=b-12\ge2\) gives \(k_N\le b-12\) and \(s_N\le b\). The single class supplied by (6) therefore contains a root with \(\delta_P=b\) and another with \(\delta_P=b+1\). Their observations agree and their truth values in (2) differ, a contradiction. It follows that

\[
B(N)\ge216\,2^{b-12}=\frac{27}{512}\,2^b
\]

for every admissible N, proving the lower bound in (4).

This proof does not require a root of infinite cost. It uses two ordinary integer roots, both with finite exact covers and coprimality certificates supplied by the constructive theorem.

## 3. Upper bound: the existing finite candidate dictionary

The already published sixth continuation, commit
`2feef401388e6e81a35dd8b0e66383f43561ad12`,
`research_notes/portable_direct/riesel_budget_20261120/budget/proof.md`, Sections 2 and 7, proves a finite sufficient observer for every declared additional budget. Its input is the Crittenden–Vanden Eynden theorem: a family of at most t residue classes covering \(2^t\) consecutive integers covers all integers. Repeated moduli are allowed. The published note contains the exact roots-of-unity/Vandermonde proof and the proper-divisor boundary argument; they are reused here.

For clarity, the order consequence needed for (4) can be stated directly. The old holes lie in 36 exponent progressions

\[
n=2h+210v,
\]

where h runs through the established 36-element hole set modulo 105, and only positive n are used. Let Q be an inclusion-minimal complete supplement of size \(s\le b\). Every q in Q has a private old-hole index in one of these progressions. On that progression its nonempty zero set is one v-class of period

\[
e_q=\operatorname{ord}_q(2^{210}).
\]

If \(e_q>2^{s-1}\), then q misses the next \(2^{s-1}\) v-positions after its private index. The other at most s-1 prime classes cover that interval, hence cover the whole progression by the interval theorem. This contradicts the private index. Therefore

\[
e_q\le2^{s-1}\le2^{b-1}.
\tag{7}
\]

Take the finite prime set

\[
\mathcal Q_b=\{q\notin P:q\text{ odd prime},\
\operatorname{ord}_q(2^{210})\le2^{b-1}\}
\]

and its squarefree product

\[
N_b=\prod_{q\in\mathcal Q_b}q.
\tag{8}
\]

Finiteness follows because this is exactly the set of prime divisors outside P of

\[
\prod_{d=1}^{2^{b-1}}(2^{210d}-1).
\]

Every minimum supplement of size at most b is contained in this dictionary by (7). Conversely, a subdictionary of size at most b covering all old holes supplies the desired supplement. Its zero phases are completely determined by \(a^2\bmod N_b\). Consequently the predicate (2) factors through that residue, and therefore also through \(a\bmod N_b\).

Properness introduces no additional unobserved exception on the old root class, hence on R1. Odd-index terms already have the old proper cover, while even-index terms factor as

\[
F_{2u}(a)=(a2^u-1)(a2^u+1),\qquad u\ge1.
\]

All roots in the stated class are at least the fixed positive root \(a_*\), so both factors exceed one. Every term is composite independently of the new dictionary. Any prime dividing such a term is a proper divisor.

Finally, write \(o_q=\operatorname{ord}_q(2)\). The elementary order identity gives

\[
e_q=\frac{o_q}{\gcd(o_q,210)},
\qquad
o_q=e_q\gcd(o_q,210)\le210\,2^{b-1}=105\,2^b.
\tag{9}
\]

Thus \(B(N_b)\le105\,2^b\). The admissible observer (8) proves the upper bound and existence of the minimum (3). No full factorization of the enormous product (8) is needed for this mathematical existence proof. Its practical enumeration efficiency is not asserted.

## 4. The same scale for complete finite residue trajectories

Consider the stronger-looking task of observing the entire sequence

\[
\bigl([F_n(a)]_N\bigr)_{n\ge1}
\]

at one fixed modulus N. For the lower bound, equal roots modulo N give equal complete trajectories, so the two roots in Section 2 are still indistinguishable. Observing more future indices at that same modulus cannot resolve them.

For the upper bound, N_b in (8) is odd. Its very first residual value recovers

\[
a^2\equiv 2^{-1}(F_1(a)+1)\pmod{N_b}.
\]

That is exactly the data used in Section 3. Hence, if \(\widehat\Omega_b\) is defined like (3) but requires the whole residual trajectory modulo N to determine (2), the same bounds hold:

\[
\frac{27}{512}\,2^b
\le\widehat\Omega_b\le105\,2^b,
\qquad b\ge14.
\tag{10}
\]

Any finite collection of prescribed moduli is equivalent, for these congruence data, to its least common multiple. Arbitrarily high but finite powers of a fixed finite set of primes cannot evade the lower bound, since (1) stays fixed. This does not address an oracle returning an entire infinite prime-adic integer, or an adaptive procedure allowed to add unbounded new moduli.

## 5. Native interpretation and limits

The native update is still the fixed-X6, typed integer, positive singleton BRC update

\[
x\longmapsto2x+1.
\]

For every finite N the readout \(O_N(x)=[x]_N\) commutes exactly with this update. Exact commutation guarantees the residue dynamics and all future queries in that observation. It does not imply that the global covering-cost functional factors through the same observation.

Equations (4) and (10) give a quantitative separation: each finite budget admits a finite sufficient prime dictionary, while the largest observed prime order needed for a dictionary valid throughout R1 grows exponentially with the budget. These are statements about task-specific congruence sufficiency, not a reduction of the full native integer state or of joint cofactor relations to a finite state model.

The result supplies no proof that any specified root has infinite covering cost. In particular, the original fixed root a* retains its earlier status: the computed finite obstruction window gives a lower bound, and existence or nonexistence of an unrestricted finite cover remains unresolved in this research record. The construction also does not classify all cost-seven supplements or identify a global cost-seven minimum.

## 6. Sources and verification boundary

The new result is the synthesis of two stated mathematical inputs: the companion all-cost fixed-observation construction, and the already published finite-budget order bound. The constants in (4) follow from \(216/2^{12}=27/512\) and \(210/2=105\). No additional large numerical search or benchmark is required to prove the synthesis.

External mathematical inputs, checked at their author or publisher sources:

1. R. B. Crittenden and C. L. Vanden Eynden, *Any n arithmetic progressions covering the first 2^n integers cover all integers*, Proceedings of the American Mathematical Society 24 (1970), 475–481, DOI [10.1090/S0002-9939-1970-0258719-2](https://doi.org/10.1090/S0002-9939-1970-0258719-2). The theorem and a short algebraic proof are retained in the pinned sixth-continuation note. An accessible author manuscript explicitly states the theorem and applies it in Claim 2.1: J. Klein, D. Koukoulopoulos and S. Lemieux, [*On the j-th smallest modulus of a covering system with distinct moduli*](https://dms.umontreal.ca/~koukoulo/documents/publications/covering-systems.pdf), June 26, 2023.
2. The companion refinement uses the primitive-prime existence input already used in the seventh continuation: every base-2 order greater than six is attained by a prime. It is stated as Lemma 2, citing Bang, in M. Filaseta, C. Finch and M. Kozek, [*On powers associated with Sierpinski numbers, Riesel numbers and Polignac's conjecture*](https://people.math.sc.edu/filaseta/papers/SierpinskiEtCoPap5.pdf).

The external inputs are credited as existing mathematics. The project-specific observer theorem and this sharp-rate consequence are author derivations with their scopes and dependencies exposed; no claim of literature-wide novelty is made.
