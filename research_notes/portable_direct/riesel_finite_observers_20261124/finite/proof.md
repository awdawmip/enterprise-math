# Every finite congruence observer has a fixed trajectory with cofinite exact costs

Status: author mathematical derivation with complete finite checks of small members of a proved refinement family. This is a continuation of Researcher `EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`; no independent project Review or Foundation promotion is asserted.

## 1. Statement and precise observer scope

Retain the established square-Riesel family

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1,
\]

with old root

\[
a_*=690786768637635218740714348513373826260012289,
\]

old dictionary

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,
1321,14449,29191,65537,6700417\},
\]

and

\[
M=\prod_{p\in P}p
=1397394912916194098609132326092145093313722687204526281.
\]

Let \(\delta_P(a)\) be the minimum number of primes outside P in a proper-prime cover of every positive-index term, and let \(\tau(a^2)\) be the minimum total number of covering primes. Both minima are infinity if no finite cover exists.

The previously fixed 29-channel fiber is

\[
R_1=\{a>0:a\equiv a_*\pmod{6M},\quad
a\equiv12926327728523\pmod{80754838636615}\}.
\tag{1}
\]

Its additional root residues are

\[
\begin{array}{c|rrrrrrrrr}
q&5&13&11&61&331&19&37&73&109\\\hline
a\bmod q&3&1&0&0&0&6&0&37&0.
\end{array}
\]

For a positive integer N put

\[
B_N=\max\bigl(\{1\}\cup
\{\operatorname{ord}_q2:q\text{ is an odd prime dividing }N\}\bigr),
\]

\[
k_N=\min\{k\ge2:216\cdot2^k>B_N\},
\qquad s_N=k_N+12.
\tag{2}
\]

**Theorem.** For every positive integer N there is a residue \(r_N\pmod N\) such that, for every integer \(s\ge s_N\), there are infinitely many ordinary positive integer roots satisfying

\[
\boxed{
a\in R_1,\qquad a\equiv r_N\pmod N,\qquad
\delta_P(a)=s,\qquad\tau(a^2)=20+s.
}
\tag{3}
\]

For each s, such roots contain an arithmetic progression after deletion of finitely many initial terms. The residue \(r_N\) is chosen once, before s varies. The threshold (2) is a constructive sufficient bound, not an optimality assertion.

Consequently, all roots in (3) have exactly the same complete residue-value trajectories

\[
[F_n(a)]_m\quad(n\ge0)
\]

for every divisor m of N, as well as the previously fixed 29 trajectories in (1). Taking N to be the least common multiple handles any prescribed finite collection of integer moduli, including arbitrary finite prime powers.

The result strengthens the general pigeonhole consequence of the earlier all-cost theorem: one fixed observation now realizes **every sufficiently large finite cost**, not merely an unspecified unbounded subsequence of costs.

## 2. Reused construction and a refinement of every size at least five

The four-seed construction is published at commit
`af9e1a5e49386a28283781876e10742a71991036`, path
`research_notes/portable_direct/riesel_spectrum_20261121/spectrum/proof.md`.
Its extension to the fixed 29-channel fiber is published at commit
`b1de1acbdc97b5e51d486127abd1fadd24babd99`, path
`research_notes/portable_direct/riesel_five_cover_20261123/fiber/proof.md`, Section 5.

The six-prime seed has the following even-index phases, where n=2u and a row is written \((q,d,c)\) for \(u\equiv c\pmod d\):

\[
(5,2,1),\ (73,9,1),\ (13,6,0),\ (19,9,4),\
(433,36,16),\ (38737,36,34).
\tag{4}
\]

Its largest even period is d=36. All extra periods divide d, and its common period with the old holes is 35d. All rows have private old-hole witnesses. The twenty old private odd indices remain

\[
37,3,89,5,293,117,413,113,41,33,87,233,773,207,237,257,53,593,63,111.
\tag{5}
\]

For an integer k at least two, put

\[
a_k=2^k-1,\qquad H_k=3\cdot2^{k-1},\qquad G_k=3\cdot2^k.
\]

Define a system \(\mathcal C_k\) of k+3 classes in the auxiliary integer v. First use the k dyadic rows

\[
v\equiv2^{j-1}-1\pmod{2^j},\qquad 1\le j\le k,
\tag{6}
\]

then the class \(v\equiv0\pmod3\), and two final rows as follows:

| Parity of k | Phase modulo \(H_k\) | Phase modulo \(G_k\) |
|---|---:|---:|
| even | \(H_k-1\) | \(2^{k+1}-1\) |
| odd | \(a_k\) | \(G_k-1\) |

All k+3 moduli are distinct, divide \(G_k\), and have least common multiple \(G_k\). The dyadic rows are disjoint; they classify the conditions that the two-adic valuation of v+1 is respectively 0 through k-1. Their complement is the single progression

\[
v=a_k+2^k t.
\tag{7}
\]

On this complement, the three extra rows cover the three t-classes modulo three exactly once. For even k, their t-phases in the order 3,\(H_k\),\(G_k\) are 0,2,1. For odd k they are 1,0,2. This follows directly by reducing \(a_k+2^k t\) modulo the indicated moduli. Consequently \(\mathcal C_k\) covers every integer.

It is irredundant. The two final rows lie in \(v\equiv-1\pmod{2^{k-1}}\), so they miss every dyadic row with j<k. On each such row, the class modulo three covers only one third, leaving private points. On the last dyadic row j=k, the class modulo three and the class modulo \(H_k\) cover at most two thirds together; the final \(G_k\)-row misses it. Thus that dyadic row also has private points. Finally, on the complement (7), each of the three extra rows has its own t-class modulo three and therefore private points.

Private witnesses can also be specified without a search. For the j-th dyadic row choose

\[
w_j=\begin{cases}
2^{j-1}-1,&j\text{ even},\\
3\cdot2^{j-1}-1,&j\text{ odd}.
\end{cases}
\]

For the three extra rows, in the order \(3,H_k,G_k\), choose

\[
\begin{cases}
(a_k,G_k-1,2^{k+1}-1),&k\text{ even},\\
(2^{k+1}-1,a_k,G_k-1),&k\text{ odd}.
\end{cases}
\]

All these numbers lie in the full period \(0\le v<G_k\). Each \(w_j+1\) has two-adic valuation j-1 and \(w_j\not\equiv0\pmod3\); for j=k direct reduction modulo \(H_k\) excludes its extra row as well. The last three witnesses respectively represent the three private classes in (7). Thus each displayed witness belongs to precisely its assigned row.

The case k=2 is the inherited five-child cover

\[
(m,b)=(2,0),(3,0),(4,1),(6,5),(12,7).
\]

The case k=3 gives the new six-child cover

\[
(m,b)=(2,0),(3,0),(4,1),(8,3),(12,7),(24,23).
\]

Its respective private residues modulo 24 can be chosen as 2,15,1,11,7,23. The companion calculator checks complete periods for k=2 through 6; universal coverage and irredundancy follow from the argument just given.

For a current parent class \(u\equiv c\pmod d\), replace it by

\[
u\equiv c+db\pmod{dm}
\qquad((m,b)\in\mathcal C_k).
\tag{8}
\]

For each child choose a prime of exact base-2 order 2dm and impose

\[
a\equiv2^{-(c+db)}\pmod q.
\]

The inherited primitive-prime theorem supplies such a prime for every requested order, which here is greater than six. This is the same mathematical existence input already used in the published five-child construction; no stronger assertion about the number of primitive prime factors is needed.

All requested orders within each pattern are distinct. Every retained extra order is at most 2d, while every child order is at least 4d. Therefore the children are fresh relative to all current extra primes. Starting at d=36, every child order is at least 144, greater than every old-prime order in the verified P dictionary. Freshness from P follows as well.

The maximum child period is \(G_kd=3\cdot2^k d\). All periods continue to divide the maximum, and the maximum has only prime factors two and three. The common hole period remains 35 times that maximum.

Privacy is preserved by the same explicit argument as in the inherited construction. If the parent has a private witness \(w=c+dv_0\), then all \(w+35dt\) remain private against unaffected rows and remain old holes. Their parent coordinate is \(v_0+35t\). Since \(\gcd(35,G_k)=1\), this coordinate reaches every private residue of the child cover. Thus every child has a private old-hole witness. Unaffected rows keep their old private witnesses because those lie outside the parent class.

Every new child has even exponent phase and even base-2 order, so it misses all odd indices. The old private odd witnesses (5) survive. The only extra odd-order channel remains the unchanged prime 73, already checked to avoid these old witnesses.

We have therefore proved an indefinitely reusable largest-parent refinement with

\[
\boxed{
\text{number of children}=k+3,\quad
\text{extra-cost increment}=k+2,\quad
\text{largest-period factor}=3\cdot2^k.
}
\tag{9}
\]

In particular, **every integer cost increment at least four is available in one refinement**.

## 3. Move all future refinements beyond the observed prime orders

Begin at the six-prime seed (4), choose its largest-period 433 row, and refine it once using \(\mathcal C_k\) with \(k=k_N\). Let the resulting finite dictionary be

\[
S_0=P\sqcup Q_0.
\]

It has

\[
|Q_0|=c_0=k+8,
\qquad d_0=108\cdot2^k,
\qquad 2d_0=216\cdot2^k>B_N.
\tag{10}
\]

The largest-period row cannot be an observed prime q dividing N: its exact order is 2d_0, which exceeds all observed odd-prime orders. Whenever any \(\mathcal C_\ell\) refinement is applied after this point, its parent again has the largest period and therefore an order greater than B_N. Its children have still larger orders. It follows inductively that, for every later sequence of refinements:

1. no observed prime dividing N is newly introduced;
2. no observed prime already in S_0 is removed;
3. every observed prime retained in the dictionary keeps its original phase.

The intersection of the evolving dictionary with the odd prime divisors of N is thus **fixed once and for all**. This stabilization holds for arbitrary later choices of refinement size, not only along one preselected infinite chain.

## 4. Every sufficiently large extra cost is available

Given any \(s\ge c_0+4=s_N\), put

\[
\ell=s-c_0-2\ge2
\tag{11}
\]

and refine a largest-period row once using \(\mathcal C_\ell\). Its cost increment is \(\ell+2=s-c_0\), so the resulting cover has exactly s extra primes. It is irredundant, preserves the twenty old private witnesses, and retains the same observed-prime subset and phases as S_0. Thus only one further refinement is needed for each requested cost, without a numerical-semigroup gap argument.

The construction at this point provides a covering dictionary and private witnesses. Exact minimum cost will follow from coprimalization, with the fixed modulus N imposed compatibly.

## 5. Choose one root residue modulo N and retain it for every cost

Factor N into prime powers. Define compatible root residues at each factor \(q^e\Vert N\) as follows:

| Observed prime power | Fixed residue modulo \(q^e\) |
|---|---|
| q=2 | \(a_*\bmod2^e\), an odd residue |
| q in P | \(a_*\bmod q^e\) |
| odd q in \(S_0\setminus P\), with its fixed phase c | \(2^{-c}\bmod q^e\) |
| odd q not in \(S_0\) | 0 |

These choices determine one residue \(r_N\pmod N\) by CRT. They depend on N and the chosen seed S_0 but not on the final cost s or the later refinement path. Prime-power precision does not cause a compatibility issue: all dictionary constraints originally fix residues only modulo their primes, and the indicated lifts respect those constraints.

For the dictionary \(S=P\sqcup Q\) at a chosen final cost s, take all of its private exponent indices \(n_q\), and define

\[
D=\operatorname{lcm}_{q\ne q'}(2^{|n_q-n_{q'}|}-1),
\qquad
E=D\Big/\prod_{p\in S}p^{v_p(D)}.
\tag{12}
\]

Retain the previous forcing factor

\[
T_{3,1}=\frac{2^{210}-1}{\prod_{p\in P}p^{v_p(2^{210}-1)}}.
\]

The root constraints are

\[
\begin{split}
a&\equiv a_*\pmod{2M},\\
a&\equiv2^{-c_q}\pmod q\qquad(q\in Q),\\
\operatorname{lcm}(E,T_{3,1})&\mid a,\\
a&\equiv r_N\pmod N.
\end{split}
\tag{13}
\]

These constraints are compatible prime by prime:

- For any dictionary prime q, every q-power has been removed from E. If q also divides N, it belongs to the stabilized subset of S_0 and the fixed prime-power lift agrees with its unchanged phase. The old P congruences agree in the same way.
- Every observed odd prime outside S is outside S_0 as well, by stabilization. Its N-residue is zero, which is compatible with any power of that prime occurring in E or in \(T_{3,1}\).
- The extra prime orders in the seed are 4,9,12,18,72; all later extra orders are divisible by 72. None divides 210. Thus no extra dictionary prime divides \(T_{3,1}\); the old dictionary factors have been removed from that forcing factor by definition.
- E and \(T_{3,1}\) are odd. The prescribed lift at a power of two is odd and agrees with the old parity condition.

General CRT therefore gives a nonempty arithmetic progression of roots for each s, always with the same residue \(r_N\pmod N\).

## 6. Exact costs and membership in R1

If a prime \(\ell\) divided two different private terms, the two defining congruences would imply

\[
\ell\mid 2^{|n_q-n_{q'}|}-1,
\]

so \(\ell\mid D\). If \(\ell\in S\), privacy excludes this. Otherwise \(\ell\mid E\mid a\), which gives \(F_n(a)\equiv-1\pmod\ell\), again a contradiction. Thus all \(20+s\) private terms are pairwise coprime.

Any complete prime cover needs at least \(20+s\) primes for these private terms, and S supplies exactly that many. The s new private terms avoid P, so at least s covering primes must be outside P. This proves

\[
\delta_P(a)=s,\qquad\tau(a^2)=20+s.
\]

All sufficiently large positive members of the CRT progression have \(2a^2-1>\max S\), making every assigned divisor proper.

The larger fixed fiber R1 is preserved. The permanent channels have residues 3,37,1,6 at the primes 5,73,13,19. None of 11,61,331,37,109 occurs among the extra primes: their orders are respectively 10,60,30,36,36, while the permanent seed orders are 4,9,12,18, the two binary-seed orders are 72, and every later order is divisible by 72. They are also outside P.

The unchanged private odd indices include 3 and 63, with difference 60, and 5 and 41, with difference 36. Therefore

\[
2^{60}-1\mid D,\qquad2^{36}-1\mid D.
\]

The five absent primes consequently divide E and hence a. The factor \(T_{3,1}\) forces \(3\mid a\). Together with the old congruence, these are precisely the residues defining R1 in (1). Adding the modulus N has not changed this conclusion. The theorem is proved.

## 7. Consequences for finite observations

### 7.1 A complete future residue trajectory can have a cofinite exact-cost spectrum

For roots with \(a\equiv r_N\pmod N\), one has

\[
F_n(a)\equiv r_N^2 2^n-1\pmod N
\qquad(n\ge0).
\tag{14}
\]

Thus one exact complete observed trajectory supports every finite additional cost s beyond the threshold (2). Each cost is realized by infinitely many ordinary roots. This is a uniform constructive statement about one residue, not an interchange of \(\forall s\exists a\) with \(\exists a\forall s\). No single root of infinite cost follows.

There is no finite-valued function of these fixed residue trajectories that equals the exact cost on the whole root family. More strongly, no finite-valued upper-bound function of this observation can bound every finite cost in the selected fiber. A uniformly bounded additive-error estimate is likewise impossible on that fiber.

### 7.2 A necessary order-growth bound for exact budget predicates

Let b be an integer at least 14. Suppose the residue a modulo N determines the Boolean predicate

\[
\delta_P(a)\le b
\]

for every root \(a\in R_1\). Then necessarily

\[
\boxed{
B_N\ge216\cdot2^{b-12}
=\frac{27}{512}\,2^b.
}
\tag{15}
\]

To prove this, put \(k=b-12\ge2\). If \(B_N<216\cdot2^k\), then \(k_N\le k\), so \(s_N=k_N+12\le b\). The theorem gives one residue class modulo N containing both a root of exact cost b and a root of exact cost b+1. Their budget predicates differ, a contradiction. Equivalently, warm up from the cost-six seed with \(\mathcal C_{b-12}\), reaching cost b-4 and maximum order \(216\cdot2^{b-12}\); a five-child or six-child final refinement gives the two opposite budget outcomes.

The bound is necessary and is not claimed sharp. It concerns sufficiency of a fixed modulus for the whole stated root family. Since \(B_N\) depends only on the odd prime divisors of N, increasing the finite powers of a fixed set of observed primes does not increase this bound. For that fixed prime set, no finite precision suffices for all sufficiently large budget predicates.

The residue in the theorem may vary when N varies. The result does not assert that one ordinary root or one fixed prime-adic point realizes all costs at all precisions. It also does not establish impossibility of arbitrary adaptive procedures with access to unbounded integer information.

### 7.3 Exact transition projection and task information are separate properties

For the native integer update \(T(x)=2x+1\), the residue observation \(O_N(x)=x\bmod N\) commutes exactly with the finite update:

\[
O_N(T(x))=2O_N(x)+1\pmod N.
\]

It therefore preserves every future residue query at that modulus. Nevertheless, (3) shows that the exact covering-cost functional does not factor through this observation, even on the R1 family of square-Riesel roots. Closure of an observation under the update does not by itself make it sufficient for every property of the underlying integer state.

The fixed X6 anchor, typed integer register, positive singleton BRC weight and multiplicity one remain unchanged. Prime-power readouts are observations, not additional axes. The full integer state and its joint cofactor relations remain available; the theorem identifies an exact limitation of any prescribed finite congruence observation for this covering-cost question.

## 8. Evidence and reuse boundary

The new finite arithmetic checks exercise \(\mathcal C_k\) for k=2 through 6, including the inherited five-child pattern and the new six-child pattern. `verify_refinement.py` checks each complete period, irredundancy, private cells, the three complementary phases and the common-period conditions. The universal family is proved by the explicit dyadic-complement argument in Section 2; the observer theorem then follows from refinement, prime-by-prime CRT compatibility and the inherited coprimalization theorem. No prime-size cutoff, sampled cost range or numerical convergence argument is used to infer a universal statement.

The primitive-prime existence statement remains the one used in the v7 source: for every base-2 order greater than six there exists a prime of that exact order, as cited there from Bang through the Filaseta et al. paper. This note does not claim a new proof of that external theorem or an exhaustive numerical construction of all high-cost roots.

The theorem does not require a new native execution: the integer update, residue readout and old family are unchanged, with their existing execution evidence retained at the pinned sources. Parent integration may supply a new concrete refined example without changing the scope of the universal proof.
