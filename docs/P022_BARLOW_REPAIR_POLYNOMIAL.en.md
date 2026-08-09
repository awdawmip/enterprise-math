# P022 — Repair Polynomial of the Two-Sided Coordination-History Quotient

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE WEIGHTED WALK / PRIOR-ART MAPPED`  
Owner: `program/p022-geometry-v2`  
Depends on: two-sided event-driven repair; P011 fiber/collision spectrum  
Prior-art boundary: unweighted chamber/image counts are classical Catalan/Narayana/Weyl-chamber walk enumerations; the repair-bit weighting is the project-specific specialization studied here

## 1. Repair dimension as the fiber coordinate

For a length-`N` two-sided microscopic Barlow window, coordination history forgets:

- one orientation bit for each zero-departure excursion across the two absolute channels;
- one side-label bit for each diagonal split of the unordered absolute pair.

For one coordination history `h`, let

\[
r(h)=E(h)+B(h).
\]

The exact microscopic fiber theorem gives

\[
\boxed{|O_N^{-1}(h)|=2^{r(h)}.}
\]

So every fiber size is a power of two.

## 2. P022-RP01 — repair polynomial

Define

\[
a_{N,r}=\#\{h:r(h)=r\}
\]

and

\[
\boxed{
R_N(z)=\sum_r a_{N,r}z^r.
}
\]

This polynomial is an exact re-indexing of the complete fiber-size profile:

\[
\boxed{c_{2^r}=a_{N,r},}
\]

with `c_s=0` for non-powers of two.

Therefore `R_N` and the P011 fiber profile contain exactly the same information for this quotient.

## 3. P022-RP02 — finite weighted chamber recursion

Represent a coordination state by the sorted absolute pair

\[
0\le a\le b.
\]

One step independently changes each absolute coordinate by one, reflecting `0` to `1`, and then sorts the pair.

For a transition `p->q`, define the repair cost

\[
w(p,q)
=
\#\{\text{zero entries of }p\}
+
\mathbf 1_{\{p=(d,d),\ q\text{ unequal}\}}.
\]

Let

\[
F_n(a,b;z)
\]

be the repair polynomial of chamber histories of length `n` ending at `(a,b)`.  Then

\[
F_0(0,0;z)=1
\]

and

\[
\boxed{
F_{n+1}(q;z)
=
\sum_{p\to q}
 z^{w(p,q)}F_n(p;z).
}
\]

Finally

\[
\boxed{
R_N(z)=\sum_qF_N(q;z).
}
\]

At fixed `N` the reachable chamber is finite, so this is an exact finite integer recursion.

Initial polynomials are

\[
R_0(z)=1,
\]

\[
R_1(z)=z^2,
\]

\[
R_2(z)=2z^2+z^3,
\]

\[
R_3(z)=2z^2+z^3+3z^4,
\]

\[
R_4(z)=4z^2+6z^3+8z^4+2z^5.
\]

## 4. P022-RP03 — three exact evaluations

### Quotient image

Setting `z=1` forgets fiber size and counts represented histories:

\[
\boxed{R_N(1)=|\operatorname{im}O_N|.}
\]

### Microscopic domain

Setting `z=2` weights each quotient state by its exact fiber size:

\[
\boxed{R_N(2)=4^N.}
\]

This simply reconstructs all ordered pairs of length-`N` microscopic stacking words.

### Total repair-bit load

Differentiate:

\[
R_N'(2)
=
\sum_r r a_{N,r}2^{r-1}.
\]

Therefore

\[
\boxed{
2R_N'(2)
=
\sum_{\text{microscopic windows}}r(O_N(window)).
}
\]

So the derivative at the microscopic weighting point exactly equals the aggregate number of repair bits across the microscopic domain.

## 5. P022-RP04 — P011 collision polynomial from `R_N`

A repair-`r` quotient state is a fiber of size `2^r`.  Hence its contribution to P011 collision order `k` is

\[
\binom{2^r}{k}.
\]

Thus

\[
\boxed{
J_k(N)
=
\sum_r a_{N,r}\binom{2^r}{k}
}
\]

and

\[
\boxed{
K_N(t)
=
\sum_r a_{N,r}\left((1+t)^{2^r}-1\right).
}
\]

The repair polynomial is therefore a bit-dimension coordinate system for the complete P011 collision state.

## 6. Classical unweighted chamber count

The unweighted image count `R_N(1)` has established prior art.

A chamber state

\[
0\le a\le b
\]

maps under

\[
(a,b)\mapsto(a+1,b+3)
\]

to a lock-step nearest-neighbor walk in the strict rank-two chamber

\[
0<x_1<x_2
\]

starting at `(1,3)`.  The corresponding free-endpoint counts are classical Catalan/Narayana/Weyl-chamber sequences.

Let

\[
C_m=\frac1{m+1}\binom{2m}{m}.
\]

For even length `N=2m`,

\[
\boxed{
R_{2m}(1)
=(2m+1)C_m^2.
}
\]

For odd length `N=2m+1`,

\[
\boxed{
R_{2m+1}(1)
=
\frac{m+2}{2}C_{m+1}^2.
}
\]

The initial image sequence is

\[
1,1,3,6,20,50,175,490,1764,5292,19404,\ldots
\]

with even and odd subsequences appearing in established integer-sequence literature.  These formulas are treated as prior art, not as Enterprise Math novelty.

## 7. P022-RP05 — quotient-state average and worst fiber diverge strongly

The microscopic domain has size

\[
4^N.
\]

Therefore the arithmetic mean fiber size over quotient states is

\[
\boxed{
\overline f_N
=
\frac{4^N}{R_N(1)}.
}
\]

Using the standard Catalan asymptotic gives

\[
\boxed{
R_N(1)
\sim
\frac{8}{\pi N^2}4^N
}
\]

and therefore

\[
\boxed{
\overline f_N
\sim
\frac{\pi N^2}{8}.
}
\]

By contrast, the sharp maximum repair theorem gives maximum fiber

\[
\boxed{
f_{\max}(N)=2^{N+1}}
\]

for `N>=1`.

So quotient-state mean ambiguity is polynomial in horizon while worst ambiguity is exponential.

This is another concrete warning against replacing a full fiber profile by either an average or a maximum.

## 8. Sharp repair range

For every nonempty horizon,

\[
\boxed{2\le r(h)\le N+1.}
\]

The lower bound is attained by histories that make only the two initial orientation choices and never create another boundary event.

The upper bound is attained by alternating equal/split pair histories.  A one-step repair cost can equal two only on departure from `(0,0)`; every later such departure is preceded by a zero-cost return step, leaving only the first step's extra bit uncompensated.

Thus the repair polynomial is supported inside

\[
\{2,3,\ldots,N+1\}
\]

for `N>=1`.

## 9. Prior-art discipline

The chamber count at `z=1`, Catalan numbers, Narayana numbers, reflection/Weyl-chamber walk techniques, and their asymptotics are established mathematics.

The current Enterprise Math research claim is narrower: the two-sided Barlow coordination quotient has a fiber dimension generated by zero-excursion and diagonal-split events, and the resulting weighted polynomial simultaneously coordinates exact repair, P011 fibers, collision statistics and quotient-size observables.

Historical novelty of this packaging remains `NOVELTY_UNVERIFIED`.

## 10. Executable assets

Added:

- `src/enterprise_math/p022_barlow_repair_polynomial.py`;
- `tests/test_p022_barlow_repair_polynomial.py`;
- the two-sided repair module and tests.

The weighted recursion is independently checked against direct microscopic grouping through length six, while the closed chamber count is checked against the recursion through a larger finite range.
