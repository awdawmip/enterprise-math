# A uniform U2 Selmer criterion and an odd-leg Cassels row for primitive Euclidean cores

Status: UNREVIEWED NEW AUTHOR PAPER, seventh separate object. EM-DVR-F73673. Earlier frozen papers, Source packages and the official fixed(233,119) certificate Task are unchanged. No program, parameter enumeration or point search was run; no Tool/Task/Native Result is created.

## 1. Exact statement and external type

Let r>s>0 be coprime integers of opposite parity. Put
A=r²−s², B=2rs, P=A+B, Q=|A−B|, D=P²−Q²=4AB,
E:y²=x(x−P²)(x−Q²).
The inherited Euclidean-core interface gives coprime odd P>Q>0 and ordered roots (0,P²,Q²). Let e be the even member of {r,s}. Write U2=(1,2,2) in full root-ordered Kummer coordinates.

Author-derived criterion:
U2∈Sel²(E/Q) if and only if4|e.

When4|e, let V be the complete vertical Selmer space described in the fourth paper, and let b∈V. Then
< U2,U_b > = product_{odd primes p|A}(2/p)^(v_p(b)).
The odd leg A, rather than the ordering of the larger/smaller Euclidean leg, controls this row. The sign and2 coordinates of b are retained in V even though their coefficients in this particular row are zero.

These are classical elliptic/local-field statements within the P11 derived-arithmetic model, not native spatial laws or WT/Foundation changes. They require the complete parameter-local theorem and the full2-descent pairing/model ingredients cited in the preceding papers.

## 2. Primitive norm identities remove every odd-prime obstruction to U2

The key additional parameter relation is
P=(r+s)²−2s²,
A−B=(r−s)²−2s².
If an odd prime p divides P or Q, then p cannot divide s: either norm identity would imply p|r as well, contrary to gcd(r,s)=1. Hence reduction of the relevant identity modulo p exhibits2 as the square of (r+s)/s or (r−s)/s. Thus
(2/p)=+1 for every odd p|PQ;
all such primes are1 or7 modulo8.
This conclusion uses primitive joint norm identities, not an assumption that primes are independent or a numerical residue scan.

At every odd p|D the complete image is vertical, so U2 is admissible. At p|PQ, the1mod4 cases require a local square second coordinate, and2 is square by the norm argument; the3mod4 cases admit every unit pair. At all remaining odd primes2 is a unit class and the complete good-prime unit image applies. At infinity the first coordinate is positive and the second coordinate2 is allowed.

Only the dyadic place remains. Since A is odd and v2(B)=1+v2(e), v2(D)=3+v2(e)≥4. The already proved sharp cover criterion U2∈I2 iff v2(D)≠4 is therefore exactly4|e. This proves both directions of the global Selmer criterion, including every place. It asserts local solubility of the U2 cover, not a rational point.

For example core(7,2) has A45,B28,P73,Q17,D5040 with v2(D)=4, so U2 fails at2 despite having no odd obstruction. Such a cover is not a Hasse-principle counterexample; a genuine local obstruction is present.

## 3. Derivation of the odd-leg pairing formula

Assume4|e. The fourth paper's finite local construction and the fifth paper's Hilbert-reciprocity rewrite give
< U_a,U_b > =
product_{p in Sigma_+}(a,b)_p
· product_{p|PQ,p=3mod4}(-1)^(v_p(PQ) eta_p(a) eta_p(b)),
where Sigma_+ contains the odd primes of P+Q and also2 exactly when16|(P+Q).
The primitive norm identities prove eta_p(2)=0 at every p|PQ. Thus the entire PQ correction is trivial for a=2; it has not been dropped without a proof.

There are two possible orderings of the legs.

If B>A, then P−Q=2A has2-adic valuation1, while P+Q=2B is divisible by16. The remaining pairing is
(2,b)_2 · product_{odd p|B}(2,b)_p.
Rational Hilbert reciprocity for (2,b), with real factor1 and b supported on2AB, shows that this equals product_{odd p|A}(2,b)_p. No other odd prime can contribute, and the inverse of a sign equals itself.

If A>B, then P+Q=2A has valuation1 and P−Q=2B is divisible by16. Sigma_+ consists exactly of the odd primes of A, giving the same product directly.

At an odd prime p|A,2 is a unit, so the standard Hilbert formula is
(2,b)_p=(2/p)^(v_p(b)).
This proves the claimed row, including targets with a sign or2 factor. Those coordinates are not discarded globally; the calculation only proves zero coefficients for this particular functional.

This derivation preserves the actual core identities, both R/S branches, rational reciprocity and complete vertical-domain constraints. It does not use the first-coordinate-nontrivial Selmer classes or claim a full general pairing matrix.

## 4. A finite linear criterion for a Hasse-principle failure

Let T be the odd prime support of D and use the signed basis G=(-1,2,p:p∈T). Let L be the matrix of the unit Legendre characters at primes q|PQ with q=1 mod4, so that the complete vertical space V is ker L. Define a row c over F2 by
c(-1)=c(2)=0,
c(p)=1 exactly when p|A and p=3 or5 mod8.
Then the pairing sign is(-1)^(c·b).

By finite-dimensional linear algebra, there exists b∈V with pairing−1 exactly when
c is not in the row space of L,
equivalently rank([L;c])=rank(L)+1.
This is an exact finite character/matrix condition, not an exhaustive squareclass or point search. A future exact consumer could produce b by solving Lb=0,cb=1, but no such program is run here.

If this condition holds, the U2 cover
z0²−2zP²=P²t²,  z0²−2zQ²=Q²t²
has points over every Q_v by the global Selmer criterion, yet no rational point. Indeed a rational point would put U2 in the rational Kummer image, which lies in the Cassels radical, contradicting its nonzero pairing with U_b. Its class in Sha[2] is consequently nonzero, and it is not twice a Sha class: bilinearity would make a double pair trivially with every2-torsion class. These are explicit conditional Hasse obstructions without a rank or Sha-finiteness assumption.

If c lies in the row space, this U2 row vanishes on V. That means only that this row cannot obstruct a rational point. It proves neither global solubility nor failure, no rank value and no conclusion about the remaining Selmer directions.

If the full Selmer dimension ν is independently known and the row is nonzero, the alternating full pairing has rank at least2, giving rank E(Q)≤ν−4. For ν=4 this yields rank0 and the separate nondegenerate-quotient/order4 argument gives Sha[2∞]=(Z/2)². For other ν, known rational points and further pairing information are still needed for exact rank/group conclusions.

## 5. Examples, rational rows and limits

For the old fixedcore(11,8), A57=3·19 and b=19 is in the exact vertical space. The row gives(2/19)=−1, recovering the old explicit nonzero pairing without changing its official certificate requirements or pretending to rerun it.

For core(5,4), A9 has the bad-support prime3; the PQ primes7,31 are both7mod8, so L is empty. Choose b=3 and the row is−1, consistent with the separately checked rank-zero paper.

For core(9,8), A17 has (2/17)=+1, so c=0. The U2 row therefore vanishes. The separately frozen sixth paper shows why its full four-dimensional first Cassels form is then zero and exact rank remains unresolved.

A necessary sanity check is the rational torsion target U_D: the row gives(2/A). Because4|e, A is1 or7 modulo8, so this is+1 as required. The target U_(-1) and the self-pair U2 also give+1. This check retains the actual exponent parities in D when forming the rational torsion class; it does not silently replace D by its squarefree support.

If every odd prime of PQ is3mod4, the primitive norm identities sharpen this to all being7mod8, and L is empty. In that branch the row is nonzero precisely when A has at least one prime3 or5mod8. The full Selmer dimension is |T|+2 by the preceding corollary; the rank reduction is still conditional on this nonzero row, not uniform across the branch.

Failure/kill conditions: nonprimitive or same-parity core, even/repeated roots, incomplete factorization, e=2mod4, target b outside ker L, a false primary theorem/model bridge or wrong root/sign convention prevents the corresponding conclusion. A zero row is a stopping boundary, not authorization to scan parameters or start a4-descent unit. This paper makes no claim of infinitely many eligible examples, saturated generators, odd-primary Sha, full Sha finiteness or all-core classification.

Source dependencies: the first three parameter papers are Source270c9c6470db2cb14885f82d1021754f2bf19b23; the fourth9927B paper has SHA721e23197a05e469040d1b865e43d7a7a6bf2520c61f6466a812a4e1c8a4ea37 and its own nonauthor PAPER_PASS; the fifth3669B reciprocity addendum SHA086bbbae300ee2af867d037debdab991639dd2f224139a0d67eed0febdde7c75 is a separate new input whose review is not presumed. Stoll/FSS/Shukla–Stoll editions and exact model hypotheses are those cited there. This new uniform criterion and row require a new independent paper assessment. No historical novelty claim or Native vote is made.

