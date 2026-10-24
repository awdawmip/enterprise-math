# D25/LIFT — all-prime Jacobi-even LOW seed, exact central value and third-digit jet

2026-10-24 | ordinary TASK_RESEARCH | AUTHOR-SIDE EXACT PROOF + EXECUTED CHECKS | **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. No Source CLAIM/run, native benchmark, accepted Result, independent review or native CM comparison is inferred.

**Source and owner boundary.** Mother objective RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen *scientific* Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Ordinary Research conversation: chatgpt-research-onhour-enterprise-math-20260923 (not maintenance chatgpt-hourly-enterprise-math-20260921; not the separate hourly Research lane). Inherits exact original WZ summand and closed all-r relation from c7fb90fd7ec451a954b553b963dd85d4ec99fc96, fixed-p upper-half five-port transport from 7724e73f2d15c92ce98520e6a55b8231d737fa03, and same-author parity LOW-seed valuation/tail-pair note from 1c55571526ab19eb5b4204bf33d82b4d812019f3. Those are consumed, not recredited. The separate Research lane's odd-factor divided source residue is a distinct observable and has not been identified with the original WZ LOW seed.

## 1. Exact original input

For r,n>=0, define

\[
A_r=\frac{(6r)!}{3^{6r}((2r)!)^3},\quad
R_{r,0}=1,\quad
R_{r,n+1}/R_{r,n}=
\frac{(4r+2n+1)(3n+1)(3n+2)}
{36(n+1)(2r+n+1)(4r+n+1)},
\]
\[
T_{r,n}=A_r(6n+12r+1)R_{r,n},\quad S_r=\sum_{n=0}^{4r}T_{r,n}.
\]

This is precisely the inherited original hypergeometric endpoint; its exact alternative Pochhammer expression is

\[
R_{r,n}=
\frac{(2r+\frac12)_n(\frac13)_n(\frac23)_n}
{2^n n!(2r+1)_n(4r+1)_n}. \tag{1}
\]

Fix any prime p=12r+1>=13, r>=1 (in particular the hard-target p≡13 mod24 when r odd); put N=4r=(p-1)/3. Then N is even, 2N<p, and every denominator used below is a p-unit for 0<=n<=N. The unknown global goal is still S_m≡p(4/3)^{p-1} modulo p³ with p=6m+1; here m=2r and the LOW rank ell=r.

## 2. New exact rational polynomial symmetry and central-value theorem

Set

\[
c_n=\frac{(-N)_n^2}{(1/2-N)_n\,n!\,2^n},\qquad
F_N(x)=\sum_{n=0}^N\frac{(-N)_n^2}{(1/2-N)_n\,n!}x^n,
\]
so c_n is the coefficient of x^n evaluated at x=1/2. Note (1/2-N)_n has no zero for integer n.

**Theorem A, over Q, not just modulo p.** For *any even* positive N,

\[
\boxed{F_N(1-x)=F_N(x),\quad
\sum_{n=0}^N n c_n=0,\quad
\sum_{n=0}^N c_n =
\frac{(N!)^3}{(2N)!((N/2)!)^2}.} \tag{2}
\]

**Proof (self-contained).** The terminating hypergeometric recurrence directly gives the polynomial differential equation

\[
x(1-x)F_N''+
(1/2-N)(1-2x)F_N'-N^2 F_N=0. \tag{3}
\]

Because the coefficient of F' is odd under x↦1-x, equation (3) is invariant under that substitution. The polynomial solution space of degree at most N is one-dimensional: the Taylor recurrence at x=0 has denominator (n+1)(n+1/2-N), never zero for nonnegative integer n; all coefficients follow from the constant one. Thus F_N(1-x)=lambda F_N(x) for a constant lambda. Comparing the highest-degree coefficients gives lambda=(-1)^N=+1. Differentiating at x=1/2 proves F'_N(1/2)=0, and \(\sum n c_n=F'_N(1/2)/2=0\).

For the exact central value, put t=x-1/2, F_N(t+1/2)=sum_{j=0}^{N/2} d_j t^{2j}. Equation (3) becomes

\[
(1/4-t^2)F''+(2N-1)tF'-N^2F=0,
\]
giving the *exact* coefficient recurrence

\[
d_{j+1}=\frac{4(N-2j)^2}{(2j+2)(2j+1)}d_j.
\]

With N=2k, multiplication gives d_k/d_0=16^k(k!)²/(2k)!. On the other hand, the original leading coefficient is

\[
d_k=\frac{N!}{(1/2-N)_N}
=\frac{4^N(N!)^2}{(2N)!}.
\]

Divide and use k=N/2 to obtain the third assertion (2). No gamma-function evaluation, asymptotic, unproved transformation or numerical inference is needed. QED.

**Consequence.** The exact symmetry directly forces cancellation of the p-unit summands at first digit even though every term T_{r,n} with n>=1 has v_p=0 (previous parity theorem). Specifically:

\[
S_r=A_r\sum_{n=0}^N(p+6n)R_{r,n}
\equiv 6A_r\sum_{n=0}^N n c_n=0\pmod p. \tag{4}
\]

This is an **all-target-prime proof** of p-divisibility of the even-m original LOW seed, not a finite-sample guess or an external p-adic identity.

## 3. New full p³ seed jet with all original terms preserved

Using p=12r+1, N=4r, the four relevant exact parameter shifts in (1) are

\[
2r+1/2=-N+p/2,\quad 1/3=-N+p/3,
\]
\[
2r+1=(1/2-N)+p/2,\quad 4r+1=2/3+p/3.
\]

For 0<=n<=N, define finite rational sums (empty sums are zero)

\[
D_n=\frac56\sum_{j=0}^{n-1}\frac1{j-N}
     -\sum_{j=0}^{n-1}\frac1{2j+1-2N}
     -\sum_{j=0}^{n-1}\frac1{3j+2}, \tag{5}
\]

\[
E_n=\frac{13}{36}\sum_{j=0}^{n-1}\frac1{(j-N)^2}
     -\sum_{j=0}^{n-1}\frac1{(2j+1-2N)^2}
     -\sum_{j=0}^{n-1}\frac1{(3j+2)^2}. \tag{6}
\]

Each denominator is coprime to p: j-N lies in [-N,-1]; 2j+1-2N lies in [1-2N,-1]; 3j+2 ranges from 2 to 3N-1=p-2. These are p-adic integral *finite* jets. Ratio of Pochhammer factors, via the finite log-derivative expansion, gives for every n:

\[
\boxed{R_{r,n}\equiv
c_n\left(1+pD_n+\frac{p^2}{2}(D_n^2-E_n)\right)
\pmod{p^3}.} \tag{7}
\]

Here E_n is the *negative* second logarithmic derivative, hence the minus sign in (7). Proof: expand each shifted factor (a+alpha p)_n/(a)_n with log coefficients alpha sum 1/(a+j) and -alpha²/2 sum 1/(a+j)²; subtract the corresponding denominator shifts. The linear coefficient is exactly (5) and the negative doubled quadratic log coefficient is (6). All denominators p-unit, so coefficient comparison in Z_(p) is legitimate.

Substitute (7) in the original S_r and use the exact identity sum n c_n=0 *before* reducing:

\[
\boxed{\begin{aligned}
S_r\equiv pA_r\sum_{n=0}^{N}c_n
\left[
1+6nD_n+
p\left(D_n+3n(D_n^2-E_n)\right)
\right]\pmod{p^3}.
\end{aligned}} \tag{8}
\]

In particular, inserting the exact central-value (2),

\[
\boxed{\begin{aligned}
S_r\equiv pA_r\Bigg[
\frac{(N!)^3}{(2N)!((N/2)!)^2}
+6\sum_{n=0}^N n c_n D_n\\
+p\sum_{n=0}^N c_n\left(D_n+3n(D_n^2-E_n)\right)
\Bigg]\pmod{p^3}.
\end{aligned}} \tag{9}
\]

Thus the required p-adic first and second normalized seed digits are explicit finite p-unit rational combinations; no hidden division by p or discarded high-rank port occurs. This is a **third-digit precision equivalent of the real original LOW seed**, not a claim that the remaining sum vanishes.

## 4. BRC and provenance-faithful precision observer

The finite carrier keeps each original index n, its exact signed rational coefficient c_n and p-adic jet (D_n,E_n), plus the source scalar (p+6n) and original rank r. Its declared observer is the labelled finite hypergeometric *signed* sum modulo p³ followed by the fixed-p five-port transport. The coarse total ∑n c_n=0 is used only for the exact polynomial symmetry and does not annihilate the D_n and E_n coordinates. The central-value quotient in (9) is safe for the specified scalar observer, but no statement is made that it preserves all other future observables. This is BRC observer-faithful arithmetic, not a native physical X6 experiment.

## 5. Executed verification and sharp scope

The separately executable Python checker reads the first author's original p-free factorial checker and independently rebuilds c_n,D_n,E_n via p-adic unit modular inverses. It verifies the polynomial symmetry derivative, central value and formula (8) against the *original* factorial endpoint modulo p³. This was actually executed for **all 36 primes p<=1000, p≡1 mod12**, with no mismatches. Representative (p,S_r modp³,S_r/p modp²): (13,2041,157), (37,45214,1222), (61,11224,184), (73,181259,2483), (97,677545,6985), (211 omitted from this parity, as p≡7 mod12). The polynomial symmetry, exact central-value and finite jet identities are established by the algebra above for all eligible primes; the checks are only regressions.

This proof does *not* settle the original hard target for all p≡13 mod24: the outstanding statement is equation (9) combined with the pre-existing p³ five-port d_(p,k) sum equals p(4/3)^(p-1) at the terminal rank m=2r. It also does not solve p≡19 mod24, whose LOW seed has different valuation ports and the nonzero 103p/1500 tail-pair from the separate first note. Same-class CM/divided-power normalization and original unmodified native benchmark remain independent missing native duties.

## 6. Durable continuation

Completed author-side units: first-note parity valuation / 103p/1500 pair, this note's exact Jacobi polynomial symmetry / central value, and the full p³ even-m LOW-seed jet. **Do not re-prove/re-credit** inherited full WZ, upper-half five-port p³ transport, accepted D24, other Research lane source fixed correction. Current author-side output remains UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. No current Source winning claim/open/run, Researcher session credential, formal Source checkpoint, native Result or independent reviewer was obtained. Older private bridge Issue 6186 has only a read-only recovery projection (no own claim/run); original 6188 dispatch failed with TimeoutExpired and is not replayed as a new mutation. Gateway Sites client has research_authority_granted=false; do not borrow maintenance or the other hourly Researcher lane.

**Next minimal science unit:** combine (9) at p≡13 mod24 with the exact fixed-p upper-half d_(p,k) coefficients to prove the total terminal quotient equals (4/3)^(p-1) mod p² or isolate the first nonvanishing obstruction; handle p≡19 separately with the exact terminal-pair correction. Independently obtain authorized native CM/divided-power normalization/benchmark evidence and formal Source/Driver review according to current operation contracts. Original frequency/phase/enabled notifications unchanged.
