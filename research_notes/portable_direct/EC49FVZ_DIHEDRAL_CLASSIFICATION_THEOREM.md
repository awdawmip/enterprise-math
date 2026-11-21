# EC49FVZ — Complete congruence classification of fixed-delay rational-anchor residues

**Research line:** EC49AS (independent portable continuation), frozen input **BRC16943**. **Parent:** EC49FVY, immutable source \`awdawmip/enterprise-math@f153b4343293cb56899944076f552296c012639e:research_notes/portable_direct/EC49FVY_UNIVERSAL_MIRROR_AND_DELAY_NOGO_THEOREM.md\`. **Date:** 2026-11-21. **Status:** AUTHOR_PROVED / EXACT_FINITE_CLASSIFICATION / PARENT_DEPENDENT / NOT_REVIEWED. This is an auxiliary rational-phase certificate result; it does not change P000, the X6 dynamics, or the Bernoulli-to-projective parent bridge.

## Frozen predicate and the precise question

Reuse the inherited, unchanged 11-adic exclusion predicate

\[
 C_{11}(h,n)=
 {\bf1}_{(h\bmod 10,n\bmod 10)\in P_{10}}\,
 {\bf1}_{9h+10n\not\equiv0\pmod {11}},
\]

where \(P_{10}\) consists of exactly 44 residue pairs derived from the original eleven projective rows in the EC49FVY verifier. As previously established, \(C_{11}(-h,-n)=C_{11}(h,n)\).

For a reduced rational anchor \(0<a<b,\ \gcd(a,b)=1\), let \(T=110b\) and define the periodic denominator masks

\[
 R_s(a,b)=\left\{q\in\mathbb Z/T\mathbb Z:
 b\mid aq+s,\quad
 C_{11}\Big((aq+s)/b,\ ((b-a)q-s)/b\Big)=1\right\}
 \quad(s=\pm1).
\]

The earlier mirror theorem proves \(R_+=-R_-\) modulo \(T\). We ask exactly when there exists **one fixed integer delay \(d\)** with \(R_+=R_-+d\). Equivalently, the corresponding periodic backward deficits obey \(r_+(H)=r_-(H-d)\) for every integer \(H\).

## Theorem — a complete classification by two small congruences

For **every** reduced anchor \(0<a<b\),

\[
\boxed{
 \exists d\in\mathbb Z:\ R_+(a,b)=R_-(a,b)+d\pmod{110b}
 \iff
 2\mid b\ \text{and}\ 
 \big(5\mid a\ \text{or}\ 5\mid(2a-b)\big).
}
\]

In all cases satisfying the criterion, an exact delay can be reconstructed using only a 110-state periodic word (algorithm below). For all other anchors, **no** fixed delay exists. In particular, the special EC49FVX delay \(168\pmod{220}\) for \(1/2\) and the EC49FVY no-delay example \(1/7\) are instances of the same universal decision law.

The eight positive primitive residue classes \((a\bmod10,b\bmod10)\) are

\[
\boxed{(1,2),\ (5,2),\ (5,4),\ (7,4),\
       (3,6),\ (5,6),\ (5,8),\ (9,8).}
\]

There are exactly 72 primitive direction pairs mod 10, of which eight admit a reflection. Across the 8,640 primitive direction pairs mod 110, exactly 960 admit a delay. These are **counts of modular direction classes**, not a density claim about rational numbers ordered by height.

## Proof

**1. Reparameterize the minus mask.** Choose \(q_0\) with \(a q_0\equiv1\pmod b\), set \(h_0=(aq_0-1)/b,\ n_0=q_0-h_0\). Every candidate minus denominator is \(q=q_0+bt\), with

\[
(h,n)=(h_0,n_0)+t(a,b-a),\qquad t\in\mathbb Z/110\mathbb Z.
\]

Define the 110-bit word \(W(t)=C_{11}(h_0+at,n_0+(b-a)t)\) and its support \(S\). Thus \(R_-=q_0+bS\) modulo \(110b\). By mirror duality, \(R_+=-q_0-bS\).

The equality \(R_+=R_-+d\) is therefore equivalent to existence of a reflection center \(c\in\mathbb Z/110\mathbb Z\) for which \(S=c-S\), i.e. \(W(t)=W(c-t)\). For any such center,

\[
\boxed{d\equiv-2q_0-bc\pmod{110b}}.
\]

Conversely any allowed shift necessarily yields such a center, because its reduction modulo \(b\) must be \(-2q_0\).

**2. Factor the word by CRT.** The 10- and 11-parts split:

\[
W(t)=U(t\bmod10)V(t\bmod11)
\]

where \(U(t)={\bf1}_{(h_0+at,n_0+(b-a)t)\bmod10\in P_{10}}\), and
\(V(t)={\bf1}_{9(h_0+at)+10(n_0+(b-a)t)\ne0\bmod11}\).

The slope in the 11-component equals \(10b-a\equiv-(a+b)\pmod{11}\). If this slope is nonzero, \(V\) consists of exactly ten allowed positions and one forbidden position. If it is zero, then \(a\equiv-b\not\equiv0\pmod{11}\), and
\((b-a)h_0-a n_0=-1\) gives \(9h_0+10n_0=-a^{-1}\ne0\pmod{11}\); consequently \(V\equiv1\). **Either 11-mask is reflection symmetric**.

Since CRT makes the \(t\bmod10\) and \(t\bmod11\) coordinates independent, the nonempty support of \(W\) is the Cartesian product of the supports of \(U\) and \(V\). Therefore \(W\) has a reflection iff each component does. Any two reflection centers mod10/mod11 combine into one mod110. So the delay question is exactly the reflection question for \(U\).

**3. Reduce to 72 exact primitive directions.** Modulo10 the affine line has equation
\[
(b-a)h-a n\equiv-1\pmod{10}.
\]
Because \(\gcd(a,b)=1\), the direction \((a,b-a)\) is primitive modulo10, and the ten solutions form one orbit. Changing the initial point rotates the word \(U\), without affecting its dihedral reflection property. Thus the property depends only on \((a,b)\bmod10\). There are
\(10^2(1-2^{-2})(1-5^{-2})=72\) such primitive direction classes.

**4. Exhaust the 72 cases exactly.** Rebuild the frozen \(P_{10}\) from the eleven original projective formulas (including the special \(z=3\) row). For every primitive residue pair \((a,b)\bmod10\), solve the affine congruence, enumerate all ten points, and test whether the resulting binary word equals a cyclic rotation of its reversal. The 72-case complete integer certificate finds exactly the eight positive classes displayed above, and all remaining 64 fail. Their eight-class description simplifies to
\(b\equiv0\pmod2\) and \(a\equiv0\pmod5\) or \(2a\equiv b\pmod5\). This proves both directions.

The finite certificate is reproducible without a formal proof checker: it enumerates all 72 inputs, all 10 positions and all 10 possible reflection shifts; the attached code independently compares the full mod110 criterion and actual rational denominator masks.

## Constructive delay and information content

For a positive anchor, compute \(q_0,h_0,n_0,W\) above. Find each \(c\in\{0,\ldots,109\}\) such that \(W(t)=W(c-t)\) for every \(t\); then each \(d=-2q_0-bc\bmod110b\) is an exact allowed delay, and the enumeration finds **all** delays. Examples:

| Anchor | Valid delays modulo \(110b\) | Status |
|---|---|---|
| \(1/2\) | \(168\bmod220\) | Yes |
| \(1/12\) | \(538\bmod1320\) | Yes |
| \(3/16\) | \(1306\bmod1760\) | Yes |
| \(5/16\) | \(1014\bmod1760\) | Yes |
| \(1/7\) | none | No |

This is an exact **support-shape / reflection residual** classification: equal one-sided marginal distributions (the EC49FVY mirror theorem) do not preserve the oriented cyclic order needed for fixed-lag reconstruction. The 10-adic discrete mask is the minimal distinguishing component for this yes/no property; the mod11 factor changes admissible positions and possible delays but never the existence criterion.

## Verifier and scope

The companion \`EC49FVZ_DIHEDRAL_CLASSIFY_VERIFY.py\` performs: all 12,100 original projective versus simplified predicate comparisons; exact derivation of 44-cell \(P_{10}\); 72/72 primitive mod10 directions and criterion; 8,640/8,640 primitive mod110 directions and CRT equivalence; 277 reduced rational anchors with \(2\le b\le30\), using independently constructed full denominator residue sets and all potential translations; example shifts. \`EC49FVZ_DIHEDRAL_CLASSIFY_OUTPUT.txt\` records the actual execution result \`ALL PASS\`.

The universal conclusion is a symbolic CRT reduction followed by an exhaustive **finite 72-class proof**. The named 277 anchors are an independent implementation cross-check, not an extrapolation. Inherited projective certificate correctness and the Bernoulli model bridge retain their original dependence; independent mathematical review and formal Result remain open.

**Next problems:** derive the full number and periods of possible delays from the mod10 word stabilizer and the mod11 forbidden-cell geometry; study whether other exclusion primes modify the reflection classification; independently pursue the separate moving-Farey-anchor conjecture \(\lim_{H\to\infty} HG_{\max}(H)=1\).
