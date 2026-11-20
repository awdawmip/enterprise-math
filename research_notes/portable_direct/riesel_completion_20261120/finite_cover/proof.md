# Same old observer state, unbounded exact finite covering complexity

**Status.** New author derivation in the fifth Riesel continuation, with exact
finite verification. This is not an independent project Review and no literature
priority is claimed. Reuses the fourth continuation's old-observer theorem and
the classical primitive-prime-divisor theorem stated below. The general theorem
does not assert numerical prime certificates for symbolic recursive rows.

Researcher `EM-DIRECT-970E1C`; activity `RA-D2EC212845B63844081F9A14`;
local session `LOCAL-RIESEL-a047cf12d55443c395589f6024246b16`.

## 1. Setting and the result

Keep the old twenty-prime set

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,
337,641,673,1321,14449,29191,65537,6700417\},
\]

\[
M=1397394912916194098609132326092145093313722687204526281,
\qquad
a_*=690786768637635218740714348513373826260012289.
\]

The fourth continuation proved the following for every positive odd
\(a\equiv a_*\pmod{2M}\):

* All residual trajectories of \(N_a(n)=a^2 2^n-1\) in the channels \(P\)
  coincide, including their nonzero states, for every arithmetic index \(n\).
* Those channels cover all odd positive \(n\).
* Every even term is composite by the difference-of-squares factorization.
* The old unhit set among even indices \(n=2u\) is periodic modulo \(105\) in
  \(u\), with the thirty-six residues recorded in the certificate.

Define

\[
\delta_P(a)=\min\bigl\{|C\setminus P|:
 C\text{ is a finite prime cover of }N_a(n),\ n\ge1\bigr\},
\]

with value \(\infty\) if there is no such finite cover. A prime cover means a
finite set of actual primes supplying a proper divisor of every term. Including
the old set \(P\) never changes the count \(|C\setminus P|\), so this is also the
minimum number of additional prime channels needed to complete \(P\).

**Theorem.** For every integer \(r\ge0\), there are infinitely many positive odd
roots \(a\equiv a_*\pmod{2M}\) such that

\[
\boxed{\delta_P(a)=5+5r<\infty.}
\]

Every root in these progressions can additionally be required to be divisible
by the fourth continuation's fixed \(T_{3,1}\), and hence by 3.

If \(\delta(a)\) denotes the minimum **total** number of primes in a finite
cover, the theorem gives only

\[
5+5r\le\delta(a)\le25+5r.
\]

It does not identify the exact total minimum. The theorem proves unbounded
finite minimum covering complexity, not merely lower bounds which might be
satisfied by the value infinity.

For any prescribed \(B\ge2\) and \(m\ge1\), choose \(r\) such that
\(s=5+5r\ge m+1\) and

\[
s>\#\{q\le B:q\text{ is an odd prime outside }P\}.
\]

The resulting root has a finite cover, whereas every finite full cover \(C\)
satisfies \(|C\setminus P|\ge m+1\) and \(\max C>B\). This is the finite-valued
resource statement. It does **not** say that all old-hole terms have least prime
factor greater than \(B\), nor that this root belongs to the fourth
continuation's particular \(T_{B,m}\)-divisible family.

## 2. Five initial additional channels

For even \(n=2u\), assigning

\[
a\equiv 2^{-c}\pmod q
\]

makes

\[
q\mid N_a(2u)
\quad\Longleftrightarrow\quad
u\equiv c\pmod{\operatorname{ord}_q(4)}.
\]

The following five primes are outside \(P\).

| Prime \(q\) | \(\operatorname{ord}_q(2)\) | Period in \(u\) | Phase \(c\) | Root residue \(2^{-c}\bmod q\) | Private old-hole witness \(u\) |
|---:|---:|---:|---:|---:|---:|
| 5 | 4 | 2 | 1 | 3 | 3 |
| 73 | 9 | 9 | 1 | 37 | 10 |
| 13 | 12 | 6 | 0 | 1 | 6 |
| 19 | 18 | 9 | 4 | 6 | 76 |
| 109 | 36 | 18 | 16 | 105 | 16 |

All root residues are checked by the executable certificate and are defined by
the displayed modular-inverse formula.

Write this set as \(Q_0\). It completes the old observer on the even indices.
One short coverage proof uses only the old prime 7, whose fixed old phase is
\(u\equiv2\pmod3\). Checking residues modulo 18, the union of this class and
the five classes in the table is all of \(\mathbb Z\).

The listed witnesses are more informative than mere coverage. They belong to
the **full old twenty-channel hole set**, and among \(Q_0\) each is hit only by
its own row. This is checked from the fixed old root and all twenty old channels.
The full old-hole predicate and these five classes have common period

\[
L_0=\operatorname{lcm}(105,2,6,9,18)=630=35\cdot18.
\]

Thus the five-class completion is irredundant relative to the entire old
observer, not just to the prime 7.

## 3. A recursive six-class refinement

The six congruences

\[
0\pmod2,\quad 0\pmod3,\quad 1\pmod4,\quad
3\pmod8,\quad 7\pmod{12},\quad23\pmod{24}
\]

cover the integers. Each has a private residue modulo 24:

| Modulus \(m\) | Phase \(b\) | Private residue \(w\) |
|---:|---:|---:|
| 2 | 0 | 2 |
| 3 | 0 | 15 |
| 4 | 1 | 1 |
| 8 | 3 | 11 |
| 12 | 7 | 7 |
| 24 | 23 | 23 |

The finite check is simply that every residue modulo 24 is covered and each
listed \(w\) satisfies precisely its own row.

Suppose a completion has a largest channel

\[
u\equiv c\pmod d.
\]

Replace it by the six channels

\[
u\equiv c+db\pmod{dm}
\]

for the six pairs \((m,b)\) above. Each new class is contained in the replaced
class, and their union is exactly that class. The covering property is therefore
preserved. The number of added channels increases by five.

### Actual prime realization

For each new modulus \(dm\), choose a primitive prime divisor \(q\) of
\(2^{2dm}-1\), so that

\[
\operatorname{ord}_q(2)=2dm,
\qquad \operatorname{ord}_q(4)=dm.
\]

The classical theorem needed here is: for every integer \(t>6\),
\(2^t-1\) has a primitive prime divisor. It is stated as Lemma 2 in Filaseta,
Finch and Kozek's author-hosted 2008 paper, which cites A. S. Bang's 1886 paper.
Source:
[On powers associated with Sierpiński numbers, Riesel numbers and Polignac's conjecture](https://people.math.sc.edu/filaseta/papers/SierpinskiEtCoPap5.pdf),
Lemma 2; reference [1] is Bang, *Taltheoretiske Undersgelser*,
Tidsskrift for Mat. 4 (1886), 70–80, 130–137.

In our first refinement \(d=18\), so the six requested exact orders of 2 are

\[
72,108,144,288,432,864.
\]

Every exponent is greater than 6. These six orders are distinct and are absent
from the old \(P\)-order list. At subsequent refinements every new order exceeds
all orders previously used. Distinct orders force distinct primes, so all new
primes are fresh and remain outside \(P\). No unproved assertion about how many
prime factors one cyclotomic value has is used: only one prime per distinct
specified order is requested.

For each new prime impose \(a\equiv2^{-(c+db)}\pmod q\). All moduli are
distinct primes, so this is compatible with all other new channels and with
\(a\equiv a_*\pmod{2M}\).

### Private witnesses survive every refinement

At depth \(r\), the largest period and its phase are

\[
d_r=18\cdot24^r,\qquad c_r=d_r-2.
\]

Every other new period divides \(d_r\), and the common period with the old-hole
predicate is

\[
L_r=\operatorname{lcm}(105,d_r)=35d_r.
\]

These assertions hold at depth zero. Refinement multiplies the largest period by
24, all other new periods divide that largest period, and the last phase becomes
\(24d_r-2\), proving the assertions inductively.

Let \(u_*\) be a private old-hole witness for the channel being replaced. All

\[
u=u_*+35d_rt
\]

are still old holes and still avoid every channel not being replaced. Write
\(u_*=c_r+d_rv_0\). Then the new within-channel index is

\[
v=v_0+35t.
\]

Because \(\gcd(35,24)=1\), for each private residue \(w\) in the six-row table
there is a nonnegative \(t<24\) such that

\[
v_0+35t\equiv w\pmod{24}.
\]

The corresponding \(u\) is a private old-hole witness for that new child. Every
unreplaced channel retains its previous private witness: it was outside the
replaced parent class, hence it is outside all the children. The completion at
depth \(r\) is therefore irredundant and has exactly \(5+5r\) members.

This also supplies a finite exact algorithm for choosing private witnesses at
every depth. No inference from a long finite prefix to all indices is involved.

## 4. Turning irredundancy into a lower bound against every possible cover

Irredundancy alone would only show that none of the displayed primes can be
deleted from this particular cover. It would not rule out a completely different
smaller cover. The following CRT construction supplies that missing implication.

Fix a depth \(r\), its finite prime set \(Q_r\), and one positive private
old-hole witness \(u_i\) for each of its \(s=5+5r\) channels. Put \(n_i=2u_i\).
The \(n_i\) are distinct positive even indices. Let

\[
D=\operatorname{lcm}_{i<j}\bigl(2^{|n_i-n_j|}-1\bigr),
\qquad
S=P\cup Q_r,
\]

and remove all powers of the known primes in \(S\):

\[
E=\frac{D}{\prod_{p\in S}p^{v_p(D)}}.
\]

No factorization of the remaining part of \(D\) is necessary. Repeated exact
division by the finitely many specified primes computes \(E\). Equivalently,
one may repeatedly divide by \(\gcd(E,\prod_{p\in S}p)\) until that gcd equals 1.

Then \(\gcd(E,2\prod_{p\in S}p)=1\). Impose the simultaneous conditions

\[
a\equiv a_*\pmod{2M},\qquad
a\equiv2^{-c_i}\pmod{q_i}\quad(q_i\in Q_r),\qquad
a\equiv0\pmod E.
\]

CRT gives an infinite arithmetic progression of odd roots. Choose roots large
enough that \(2a^2-1>\max S\); every subsequent term is larger. The cover
\(P\cup Q_r\) now supplies proper divisors for every term.

There is an optional useful strengthening which we use in the certificate. Set
\(T_1\) to the integer obtained by removing all old \(P\)-prime powers from
\(2^{210}-1\). None of the orders \(4,9,12,18,36\) of the initial new primes
divides 210. Every recursively supplied order is divisible by 4, so it too fails
to divide 210. Thus \(\gcd(T_1,\prod Q_r)=1\), as well as
\(\gcd(T_1,2M)=1\). Replacing \(E\) by \(\operatorname{lcm}(E,T_1)\) preserves
CRT compatibility and proves the strengthening for every depth. Since
\(3\mid T_1\), all roots may be required to be multiples of 3. This is exactly
the fixed \(B=3,m=1\) old forcing, not arbitrary \(B,m\) forcing.

**Pairwise-coprimality claim.** The \(s\) private terms \(N_a(n_i)\) are
pairwise coprime.

If a prime \(q\) divides two terms, it does not divide \(2a\), and subtracting
the two relations gives

\[
2^{|n_i-n_j|}\equiv1\pmod q.
\]

Hence \(q\mid D\). There are only three possibilities:

1. If \(q\notin S\), then \(q\mid E\mid a\), contradicting
   \(q\mid a^2 2^{n_i}-1\).
2. If \(q\in P\), the old-hole property excludes it from either term.
3. If \(q\in Q_r\), privacy says it hits at most one of these chosen terms.

All possibilities are impossible, proving the claim.

Every complete prime cover, whether or not it contains \(P\), must supply
distinct primes outside \(P\) for these \(s\) pairwise-coprime terms. Therefore
\(\delta_P(a)\ge s\). The displayed finite cover gives \(\delta_P(a)\le s\),
proving the exact equality claimed in Section 1.

The quantifiers are

\[
\forall r\ge0\ \exists^\infty a\quad \delta_P(a)=5+5r.
\]

They do not claim a single fixed root has all these different finite values.

## 5. Numerical base certificate and native arithmetic bridge

`verify_exact_complexity.py` constructs a 225-digit root for the \(r=0\) case.
Its exact decimal root, square length, CRT modulus, all root residues, private
values and pairwise gcd certificates are in `exact_complexity_certificate.json`.

The private indices are

\[
\{6,20,12,152,32\}.
\]

The script verifies all ten pairwise gcds equal 1. It checks the full prime cover
over its complete exponent period 20160, so the coverage is global. The numerical
root additionally satisfies the fourth continuation's \(T_{3,1}\mid a\): that
integer is adjoined to the coprimality-forcing modulus after compatibility is
checked. In particular \(3\mid a\). This shows that killing the prime 3 does not
force the absence of a finite cover.

The verifier uses the project's `enterprise_math.brc_transport` from frozen
source commit `b1efc6c805661ed7b476e6e730107da6043176ee`. Before import, it
computes the actual Git blob hash of all four native source files recorded in the
prior certificate and checks equality with those frozen pins. It instantiates the
singleton positive branch

\[
x\longmapsto2x+1
\]

with weight and multiplicity 1, starts at \(a^2-1\), and obtains the exact private
terms using the native packet evaluation. Two steps are verified to give
\(x\mapsto4x+3\). The value \(-1\) is fixed under both. The old \(P\)-channel
residual states coincide because \(a\equiv a_*\pmod p\) for every old channel.

This lives at a fixed X6 anchor in internal arithmetic registers. The exponent is
an arithmetic index, not physical time; primes are observer channels, not spatial
axes. An unbounded minimal observer dictionary is not an assertion of unbounded
native BRC branch count: the native transition here always has one branch.

The script also verifies the recursive private witnesses through depth 6 and the
full symbolic covering periods through depth 2. These are finite checks of the
construction, while the proof in Section 3 establishes all depths. For depths
above zero it does not claim to have produced decimal values or primality
certificates for every symbolic primitive prime.

## 6. What remains unresolved

This theorem answers the finite-valued resource question in the same old
\(P\)-observer class. It does not prove finite cover existence for every root in
the fourth continuation's \(T_{B,m}\)-forced family, or even for one root of each
such particular family. That stronger requirement keeps every low-order channel
inactive on each hole fibre and all small primes inactive on every old hole.
The new construction instead keeps several small prime channels and makes rarer
private holes require arbitrarily many different further channels.

The exploratory MILP search in `search_compatible.py` only discovered the initial
five-channel cover. Its restricted-pool timeout or infeasibility outcomes are
not used as mathematical nonexistence claims. The exact verifier is independent
of the MILP optimizer and requires no solver.

