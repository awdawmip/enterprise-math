# R154 — Exact full-count aliases at equal rational slope denominators

Date: 2026-11-14 (Asia/Shanghai). Status: AUTHOR-SIDE THEOREM + EXACT FINITE VERIFICATION; independent review NOT_REVIEWED. Research pin remains \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\` (no science rebase).

**Scope.** This is the external tied-phase finite Sturmian S23 scalar observer, *not* a bridge to native X6, P000, or Heartbeat–BRC physical arithmetic. Predecessors: R146 (phase-fiber formula), R152 (finite-period absences), R153 (unequal denominators injectivity and alternating aliases); verified R153 artifact: \`enterprise-math@e6e436cb90f6c943b3825a4a2fe26b0500c558f8:research_notes/portable_direct/R153_DISTINCT_DENOMINATOR_RESONANCE_20261114.md\`.

## Definitions and objective

Fix integers \(b\ge3,\ 0<a<c<b\) with \(\gcd(a,b)=\gcd(c,b)=1\). For *arbitrary integer* cuts \(U,V\), and any integer \(L\), put

\[
C_{U,V}(L)=\left\lceil\frac{cL-V}{b}\right\rceil-
 \left\lfloor\frac{aL-U}{b}\right\rfloor-1. \tag{1}
\]

For genuine finite words the same formula counts integer-phase fibers at \(K=L+1\) with their word-derived cuts; arbitrary cuts need not be nonnegative or word-realizable. The question is when two cut pairs produce **the same entire sequence of values**, not merely the same increments or a single mean.

## Theorem R154.1 — Exact alias certificate for any equal denominator

Let \(U',V'\) be other arbitrary integers and \(r=U'-U,\ s=V'-V\). Then

\[
\boxed{C_{U',V'}(L)=C_{U,V}(L)\ \ \forall L\in\mathbb Z}
\]

holds **if and only if** \(r=s\) and the following two finite subsets of \(\mathbb Z/b\mathbb Z\) coincide. Reduce \(r\) modulo \(b\) to its representative \(t\in\{0,\ldots,b-1\}\); define

\[
S_a(U,t)=\{a^{-1}(U+j)\bmod b:0\le j<t\},\qquad
S_c(V,t)=\{c^{-1}(V+1+j)\bmod b:0\le j<t\}. \tag{2}
\]

The empty sets for \(t=0\) are equal. Thus comparing the two progressions (of at most \(b-1\) residues) is a **complete, finite, exact all-coefficient count-equivalence test**.

**Proof.** Over a full period \(L=0,\ldots,b-1\), multiplication by \(a\) and \(c\) permutes the residue classes. For arbitrary integers \(r,s\),

\[
\sum_{L=0}^{b-1}\big(C_{U+r,V+s}(L)-C_{U,V}(L)\big)=r-s. \tag{3}
\]

One way to check this without analytic averaging is to telescope the floor/ceiling change as the cut is moved by one: the floor term decreases at exactly one residue, and the ceiling term decreases at exactly one residue. Equation (3) follows for positive and negative shifts. If the count sequences coincide, (3) forces \(r=s\).

For a simultaneous shift by \(qb\), each ceiling and floor drops by the same \(q\), hence (1) is unchanged; reduce the common shift to \(0\le t<b\). The exact integer identities, with residues taken modulo \(b\), are

\[
\left\lfloor\frac{x-t}{b}\right\rfloor-\left\lfloor\frac{x}{b}\right\rfloor
=-\sum_{j=0}^{t-1}\mathbf1_{x\equiv j\bmod b},
\]

\[
\left\lceil\frac{y-t}{b}\right\rceil-\left\lceil\frac{y}{b}\right\rceil
=-\sum_{j=1}^{t}\mathbf1_{y\equiv j\bmod b}.
\]

Substitute \(x=aL-U,\ y=cL-V\) into (1). Because \(a,c\) are units modulo \(b\),

\[
C_{U+t,V+t}(L)-C_{U,V}(L)
=\mathbf1_{L\bmod b\in S_a(U,t)}
-\mathbf1_{L\bmod b\in S_c(V,t)}. \tag{4}
\]

Equality for every integer \(L\) is equivalent to equality of the sets. Combining (3), simultaneous-shift invariance and (4) proves both directions. QED.

**Universal nontrivial one-step aliases.** Take \(t=1\). Equation (2) becomes

\[
\boxed{cU\equiv a(V+1)\pmod b.} \tag{5}
\]

Every \(U\bmod b\) has exactly one associated \(V\bmod b\) satisfying (5), so for **every** admissible equal-denominator endpoint pair there are \(b\) distinct modular starting pairs for which

\[
\boxed{C_{U+1,V+1}(L)\equiv C_{U,V}(L)\quad\text{for all }L.} \tag{6}
\]

This extends R153: equal endpoint denominators are not merely a *possible* increment resonance—they **always** cause genuine all-coefficient count non-identifiability in the unrestricted-cut observer. This does not claim that each such arbitrary cut pair is attained by a Sturmian word.

Example: \(a/b=1/5,\ c/b=2/5,\ U=0,\ V=4\) satisfies (5), so \((0,4)\) and \((1,5)\) have identical \(C(L)\) for every integer \(L\). Counts for these unrestricted cuts may be negative.

## Theorem R154.2 — Complete complementary-slope resonance

If \(c=b-a\), define

\[
A_U(L)=\left\lfloor\frac{a(L+1)-U}{b}\right\rfloor-
       \left\lfloor\frac{aL-U}{b}\right\rfloor.
\]

Then, with \(D_{U,V}(L)=C_{U,V}(L+1)-C_{U,V}(L)\),

\[
\boxed{D_{U,V}(L)=1-A_U(L)-A_{-V}(L).} \tag{7}
\]

The complete period-\(b\) increment waveforms satisfy

\[
\boxed{D_{U,V}=D_{U',V'}
\iff \{U,-V\}=\{U',-V'\}\quad\text{as unordered multisets modulo }b.} \tag{8}
\]

Consequently **exactly \(b(b+1)/2\)** different full increment waveforms occur among all \(b^2\) cut-residue pairs: there are \(b\) singleton equivalence classes and \(b(b-1)/2\) size-two classes. This covers every coprime complementary pair \(a+(b-a)=b\), not only R153.2's special \((1,b-1)\).

Furthermore, the complete **count** sequences have the exact classification

\[
\boxed{C_{U,V}\equiv C_{U',V'}
\iff U'-U=V'-V\quad\text{and}\quad
\{U,-V\}\equiv\{U',-V'\}\pmod b.} \tag{9}
\]

**Proof.** Using \(c=b-a\) and the integer \(L\),

\[
\left\lceil\frac{(b-a)L-V}{b}\right\rceil
=L-\left\lfloor\frac{aL+V}{b}\right\rfloor,
\]

which gives (7). For injectivity of unordered marks in (8), note \(A_U(L)=A_0(L-a^{-1}U)\) on \(\mathbb Z/b\mathbb Z\). The nonzero discrete Fourier coefficients of \(A_0\) are all nonzero: in the residue \(aL\), its support is the proper consecutive block \(\{b-a,\ldots,b-1\}\); for frequency \(1\le k<b\), the geometric-series numerator is \(1-\exp(-2\pi i k a a^{-1}/b)=1-\exp(-2\pi i k/b)\ne0\), and the denominator is also nonzero. Therefore equality of two sums of translates of \(A_0\) determines all Fourier coefficients of the sums of two point masses, including frequency zero (both totals 2). Fourier inversion uniquely determines their unordered two-mark multisets. Conversely an unordered swap leaves (7) unchanged, giving (8) and the class count.

If the full count sequences agree, their increments agree, so (8) holds; equation (3) imposes equal cut changes. Conversely, (8) gives equal increments, so their count difference is constant in \(L\). The full-period sum identity (3) says that constant times \(b\) equals zero whenever the two cut changes agree. Thus the constant is zero, proving (9). QED.

**Actual-word connection.** R153 established that the genuinely realizable alternating pair \((01)^h,(10)^h\) (length \(2h\ge4\)) has complementary support endpoints \((h-1)/(2h-1),h/(2h-1)\), equal all-coefficient counts, and distinct words. Theorem (9) identifies the precise algebraic mechanism for this preserved alias, without asserting that every unrestricted alias is an actual word.

## Computation, limits, and next discrimination

Companion \`R154_check.py\` uses only exact Python integers, floor division, modular inverses and exhaustive finite scans:
- \(b=3,\ldots,16\): 239 distinct reduced ordered endpoint pairs, 37,016 cut states, **491,822** full-count shift/set comparisons and 2,894 verified one-step aliases; an additional 74,032 checks cover negative and unequal shifts.
- Complementary endpoints through \(b=22\): 18,447 residue-cut states, 9,777 distinct waveforms and 8,670 paired aliases, all matching (8).
- Independent all-binary-word sweep through length 16: 2,404 admissible words. Interior equal-endpoint-denominator words appear only as the two alternating words at even lengths 4,6,...,16; this is **finite evidence only**, not a proof of the all-length classification.

The exact counters and per-length rows are in \`R154_verification.json\`. These are *author-side* checks; the propositions' unrestricted-cut all-length statements follow from the proofs, not the finite bounds. Independent mathematical review remains NOT_REVIEWED.

**Next scientific question.** Prove or disprove for all lengths the observed restriction that genuine finite Sturmian words with equal nontrivial endpoint denominators are exactly the two even-length alternating words. If confirmed, combine (9) with the actual-word cut constraints to finish classification of real word-identity aliases. Separately use R152B's finite last-absence window to approach the all-length permanent-saturation threshold; that remains open. No formal TASK CLAIM, Result/Review admission, native X6 attribution or P000 change is claimed.

**Control provenance.** Prior validated identity: \`EM-DIRECT-DAF2F3\`, session \`MCP-fa6cae44b88546f9a2079bdd4adcad23\`, Activity \`RA-3E75AE7BD8828F9D79A8BE96\`. During this work the backend control requests were not sent because \`BACKEND_IDENTITY_CHECK_UNAVAILABLE\`; this author-side branch publication is independent of an unverified active CLAIM and does not update a protected execution binding. GitHub persistence and canonical Activity association are separate.