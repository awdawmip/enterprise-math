# Exponential observation horizon for a finite prime-channel budget

Status: author application and exact certificates in the sixth Riesel continuation;
not an independent project Review. The covering-interval theorem used below is
classical, not a new result or a claim of priority.

Researcher `EM-DIRECT-970E1C`; Activity `RA-D2EC212845B63844081F9A14`.

## 1. Typed setting

Keep the native fixed-X6 anchor and the integer register
\(x_n=k2^n-1\), with one positive BRC effect \(x\mapsto2x+1\), weight 1,
multiplicity 1. Here \(n\) is an arithmetic index, not physical time. Prime
channels are projections of that integer register, not extra spatial axes or
additional BRC branches. Throughout, \(k\ge3\) is odd.

Let \(\tau^{\rm div}(k)\) be the least number of primes dividing every positive
term, and \(\tau^{\rm pr}(k)\) the analogous minimum requiring a proper prime
divisor at every term. Use infinity when no finite cover exists. Prefix minima
carry a subscript \(L\). The proper version is the one used for Riesel covers.

## 2. Classical finite-interval theorem

Crittenden and Vanden Eynden proved: if at most \(t\) residue classes cover
\(2^t\) consecutive integers, they cover all integers. Repeated moduli are
allowed. The original paper is *Any n arithmetic progressions covering the first
2^n integers cover all integers*, Proc. Amer. Math. Soc. 24 (1970), 475–481,
DOI `10.1090/S0002-9939-1970-0258719-2`. A modern short proof is Balister,
Bollobás, Morris, Sahasrabudhe and Tiba, *Covering intervals with arithmetic
progressions*, Acta Math. Hungar. 161 (2020), 197–200,
DOI `10.1007/s10474-019-00980-z`. The theorem and its role are also explicitly
stated in Klein–Koukoulopoulos–Lemieux (2023), Introduction and Claim 2.1:
https://dms.umontreal.ca/~koukoulo/documents/publications/covering-systems.pdf .

One algebraic explanation is useful here. For classes \(r_i\bmod d_i\), choose
primitive \(d_i\)-th roots of unity \(z_i\), and form
\(f(n)=\prod_i(1-z_i^{n-r_i})\). It vanishes exactly on the covered integers.
Expanding the product and combining equal frequencies writes it as
\(\sum_{j=1}^{u}c_j\lambda_j^n\), where \(u\le2^t\) and the nonzero
\(\lambda_j\) are distinct. Vanishing at \(u\) consecutive integers makes a
Vandermonde system with nonzero determinant, so all \(c_j=0\). Thus \(f\)
vanishes everywhere. Roots of unity here are exact algebraic proof objects;
they are not being added to the native state space. This explanation supplies
the bridge rather than interpreting complex amplitudes as positive BRC mass.

The general bound cannot be replaced by \(2^t-1\): the classes
\(2^{i-1}\bmod2^i\), \(1\le i\le t\), cover the first \(2^t-1\) positive
integers but miss \(2^t\). This sharpness statement concerns arbitrary residue
class systems, not necessarily the constrained prime channels of one fixed k.

## 3. Budget theorem for Riesel-type sequences

**Theorem.** For every integer \(t\ge0\),

\[
 \tau^{\rm div}(k)\le t
 \iff \tau^{\rm div}_{2^t}(k)\le t,
 \qquad
 \tau^{\rm pr}(k)\le t
 \iff \tau^{\rm pr}_{2^t}(k)\le t.
\]

For an odd prime \(q\nmid k\), the set
\(\{n\in\mathbb Z:k2^n\equiv1\pmod q\}\) is empty or one residue class
modulo \(\operatorname{ord}_q(2)\). Indeed, two solutions differ by a multiple
of that order, and any such shift preserves a solution. Primes dividing k and
the prime 2 have empty zero sets. Therefore a set of at most t active prime
channels corresponds to at most t residue classes. A prefix divisibility cover
of length \(2^t\) is a global one by Section 2. The reverse implication is
restriction.

For properness, start with a prefix proper cover and discard every prime that
does not provide a proper divisor of any prefix term. Every remaining prime is
strictly smaller than at least one prefix term, hence smaller than
\(k2^{2^t}-1\). It still covers the prefix by divisibility, so it covers all
indices by Section 2. At indices beyond the prefix every selected prime is
strictly smaller than the term; properness is automatic there. Inside the
prefix it was given. This proves the second equivalence as well. At t=0 both
sides are false since the first term is greater than 1.

This replaces the fifth continuation's valid but much larger k-dependent
recursive bound \(U_t\) by an observation horizon depending only on the
prime-channel budget. It does not turn existence of some finite cover into a
decision procedure with an unspecified budget.

## 4. Bounds independent of k on necessary periods and prime sizes

If Q is an inclusion-minimal **divisibility** cover of size s, a selected
prime q has a private positive index n0. Put \(D=2^{s-1}\) and
\(d=\operatorname{ord}_q(2)\). If d>D, q misses all of the next D indices
n0+1 through n0+D. The other s−1 channels cover those consecutive indices,
so Section 2 would make them a full cover, contradicting minimality. Thus

\[
 \operatorname{ord}_q(2)\le2^{s-1},\qquad
 q\le2^{2^{s-1}}-1.
\]

For a proper cover all terms are composite. Any prime divisor of a composite
term is proper, so inclusion-minimality in this case is also minimality as a
divisibility cover. The same bounds therefore hold. Separately, removing q
and applying Section 2 to the remaining s−1 classes gives a private positive
index at most \(2^{s-1}\), which also yields the weaker bound
\(q\le k2^{2^{s-1}}-1\). The order bound is stronger and does not depend on k.

Since an existing proper cover implies all terms composite, the bound applies
to every inclusion-minimal proper Riesel cover. It need not bound primes in an
arbitrarily redundant cover.

Consequently, for a positive budget t, every minimum cover of size at most t
uses only primes in the finite dictionary

\[
 \mathcal P_t=\{q\text{ odd prime}:\operatorname{ord}_q(2)\le2^{t-1}\}.
\]

This dictionary is exactly the set of prime factors of
\(\prod_{d=1}^{2^{t-1}}(2^d-1)\), with the empty factor 1 harmless.
The predicate \(\tau^{\rm div}(k)\le t\) therefore depends only on
\(k\bmod\prod_{q\in\mathcal P_t}q\). The proper predicate has the same
property once \(2k-1>\max(\mathcal P_t\cup\{1\})\); below that threshold properness is
checked separately. A fixed finite-budget question thus has a finite sufficient
residue dictionary, despite the lack of such sufficiency for an unrestricted
cost observable.

## 5. A terminating search using short prefix observations

At a search node with j selected primes, check only the first \(2^j\) terms.
If they are all covered, the set is a global divisibility cover. In proper mode,
require proper coverage in this check; the same Section 3 argument applies.
Otherwise take a missing index n, where \(n\le2^j\), and branch on all prime
divisors of \(k2^n-1\) not already selected (in proper mode retain only proper
divisors). Any successful extension must use one of those primes. Stop a failed
branch at depth t. Complete deterministic factorization makes every branching
set finite and complete, so the search decides the fixed-budget question.

In proper mode, if a node fails only because a selected prime equals the whole
term, that term is prime and has no proper divisor; no successful extension
exists. Otherwise the missing index is missing by divisibility and all added
prime factors are genuinely new. This handles the boundary case rather than
silently allowing a prime term as a composite certificate.

The numbers factored at internal nodes have index at most \(2^{t-1}\).
This is a termination and witness-size statement, not a practical efficiency
guarantee. No claim of polynomial time or a finite unbudgeted rejection bound
is made.

## 6. A smaller joint sample for the old twenty-channel observer

For the old square-root class \(a\equiv a_*\pmod{2M}\), the old channels P
cover every odd index and all even indices outside the known hole set
\(H\subset\mathbb Z/105\mathbb Z\), with \(|H|=36\). Use positive
representatives \(\widetilde H\subset\{1,\ldots,105\}\), replacing the
residue 0 by 105. The hole indices are precisely

\[
 n=2h+210v,\qquad h\in\widetilde H,\quad v\ge0.
\]

For each fixed h, an added prime q has either an empty zero set on v or a
single residue class modulo \(\operatorname{ord}_q(2^{210})\). Therefore

\[
\boxed{\delta_P(a)\le t\iff
 \exists Q\subseteq\{\text{odd primes}\}\setminus P,\ |Q|\le t,
 \quad Q\text{ properly covers every }a^22^{2h+210v}-1,
 \ h\in\widetilde H,\ 0\le v<2^t.}
\]

The finite sample has exactly \(36\cdot2^t\) terms and maximum exponent
\(210\cdot2^t\). It is crucial that **one common Q** covers all 36 fibers.
Allowing a separate t-prime dictionary for each fiber would change the budget
and is not the stated equivalence.

Primes in P have no hits on these fibers and are discarded before counting Q.
To check properness on later points, separately retain, on each fiber, only
the primes that properly divide a point in that fiber's initial sample. This
subdictionary still covers its \(2^t\) initial points and has at most t
elements, so its classes cover all v. Every retained prime is below that
fiber's largest sampled term, hence below every later term of the same fiber.
The union need not be enlarged: each subdictionary is already contained in the
same Q. The old P supplies proper divisors of nonholes. Thus the same global
budget is preserved.

One may alternatively use the coarser generic full-prefix bound
\(2^{20+t}\) for the union P and Q; the 36-fiber sample is more economical
and retains the shared dictionary constraint explicitly.

## 7. A finite sufficient observer for the additional budget

For an inclusion-minimal supplement Q of size s, each q has a private old-hole
index in at least one of the 36 fibers. Restrict to such a fiber. If
\(e_q=\operatorname{ord}_q(2^{210})>2^{s-1}\), the next \(2^{s-1}\)
consecutive v positions are covered by the other s−1 channels. The interval
theorem makes those channels cover the entire fiber, contradicting the private
point. Hence

\[
 e_q\le2^{s-1},\qquad q\le2^{210\cdot2^{s-1}}-1.
\]

For a fixed budget t>0 let

\[
 \mathcal Q_t=\{q\notin P:q\text{ odd prime},\
              \operatorname{ord}_q(2^{210})\le2^{t-1}\}.
\]

It is the set of prime factors outside P of the finite product
\(\prod_{d=1}^{2^{t-1}}(2^{210d}-1)\). On the old root class the predicate
\(\delta_P(a)\le t\) factors through the residue data
\(a^2\bmod\prod_{q\in\mathcal Q_t}q\). All these roots already have
composite terms by the odd-index old cover and even-index factorization, so
there is no prime-equals-whole-term exception in this class.

This is an exact scope-typed positive compression result: the enlarged finite
observer is sufficient for a declared budget. In contrast, the companion exact
cost families prove that the old P observer alone does not determine the
unbounded cost, even if its full future is known. The dictionary is finite but
can be enormous; this result does not assert its optimality or practical size.

## 8. Exact finite verification and limits

`verify_window.py` checks native source pins before import, uses the actual
positive singleton BRC update, verifies the six-prime cover of k=509203 on the
64-term horizon and its six pairwise-coprime witnesses already within the first
32 terms, and validates complete bounded-search trees on small instances.
It checks binary residue-class examples attaining the generic horizon and the
36-fiber sample for the constructed five-extra-channel family. These finite
checks exercise the applications; Section 2 is the theorem establishing the
arbitrary-t implication.

The fixed old root's existence or nonexistence of an unrestricted finite cover
remains open in this research record. Increasing exact lower bounds is not a
proof of infinity. The theorem concerns bounded observer dictionaries and
does not assert finitely many native states, a physical time bound, or collapse
of the whole residual system to its old twenty-channel readout.
