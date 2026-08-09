# Legendre Pressure Test — Supplement 19

Status: `PROVED RESEARCH NOTE`  
Scope: actual lower-band root-image separation while retaining exact cofactor windows  
Depends on: P017 L051–L054, P007 quotient-window transport Supplement 01, P023 image-separation Supplement 08, and P018 T113  
Discipline: finite integer inequalities only; no prime-distribution estimate and no claim of a Legendre proof.

## 1. Why L052 should be re-examined

For a lower-band prime `p`, L052 defines

\[
j_p=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right)
\]

and enlarges the possible root output to the candidate pair

\[
C_p(k)=\{j_p,j_p+1\}.
\]

It proves that these candidate pairs are pairwise disjoint from `k>=15`, and at `k=14` both `C_2(14)` and `C_3(14)` contain root 9.

L054 later proves that the exact cofactor windows themselves are strictly separated. That forces a sharper question:

> is candidate root 9 at `k=14` actually realized by both exact windows?

No:

\[
W_2(14)=[99,112]
\quad\Longrightarrow\quad
R_2(W_2)=\{9,10\},
\]

whereas

\[
W_3(14)=[66,74]
\quad\Longrightarrow\quad
R_2(W_3)=\{8\}.
\]

The candidate pairs overlap while the realized images do not.

This calls for the P023-S8 actual-image separation test rather than collision counting on enlarged candidate supersets.

## 2. Actual root image

For a prime `p<=k`, retain the exact cofactor window

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
\]

Define its **actual square-root image** by

\[
\boxed{
G_p(k)=\{R_2(q):q\in W_p(k)\}.
}
\]

Because `R_2` is monotone, `G_p(k)` is a consecutive integer root interval; under the present square-basin geometry T113 bounds it by at most two adjacent roots.

## 3. L055 — Actual lower-band root images are pairwise disjoint from k=9

Status: `PROVED`.

Let

\[
k\ge9
\]

and let `p<r` be distinct lower-band primes:

\[
p^2<2k,
\qquad
r^2<2k.
\]

Then

\[
\boxed{
G_p(k)\cap G_r(k)=\varnothing.
}
\]

Thus, from `k>=9`, an actually realized descended root index can come from at most one lower-band least-prime shell.

The uniform stable threshold for **realized shell channels** therefore improves from the L052 candidate-pair threshold `15` to

\[
\boxed{9}.
\]

## 4. Three necessary integer conditions for a common root

Assume for contradiction that a common root `s` exists. Then there are

\[
q_p\in W_p(k),
\qquad
q_r\in W_r(k)
\]

with

\[
R_2(q_p)=R_2(q_r)=s.
\]

The root basin is

\[
s^2\le q\le(s+1)^2-1=s^2+2s.
\]

This yields three necessary conditions.

### 4.1 From the left boundary of the p-shell

Since `q_p in W_p(k)`,

\[
pq_p>k^2.
\]

Since `q_p<=s^2+2s`,

\[
\boxed{k^2<p\,s(s+2).}
\tag{A}
\]

### 4.2 From the right boundary of the r-shell

Since `q_r>=s^2` and

\[
rq_r\le k(k+2),
\]

we have

\[
\boxed{rs^2\le k^2+2k.}
\tag{B}
\]

### 4.3 From the left boundary of the r-shell

Also `rq_r>k^2`, while `q_r<(s+1)^2`, so

\[
\boxed{k^2<r(s+1)^2.}
\tag{C}
\]

Subtracting the `p s^2` part of (A) from (B) gives

\[
\boxed{(r-p)s^2<2ps+2k.}
\tag{D}
\]

These are the complete pressure inequalities used below.

## 5. Uniform compression for every r>=5

If `r>=5`, then `r` is odd and every smaller prime satisfies

\[
p\le r-2.
\]

The elementary square identity

\[
(r+1)^2-4r=(r-1)^2\ge0
\]

combined with (C) gives

\[
4k^2<4r(s+1)^2\le(r+1)^2(s+1)^2.
\]

Hence, for positive integers,

\[
\boxed{2k<(r+1)(s+1).}
\tag{E}
\]

Now combine `r-p>=2`, `p<=r-2`, (D), and (E):

\[
\begin{aligned}
2s^2
&\le(r-p)s^2\\
&<2ps+2k\\
&\le2(r-2)s+2k\\
&<(3r-3)s+r+1.
\end{aligned}
\]

Thus every common root would have to satisfy

\[
\boxed{2s^2<(3r-3)s+r+1.}
\tag{F}
\]

## 6. r>=11: the lower-band condition makes s too large

The lower-band condition gives

\[
r^2<2k
\quad\Longrightarrow\quad
r^4<4k^2.
\]

Using (C),

\[
r^4<4r(s+1)^2,
\]

hence

\[
\boxed{r^3<4(s+1)^2.}
\tag{G}
\]

For `r>=11`, if

\[
2(s+1)\le3r,
\]

then

\[
4(s+1)^2\le9r^2<r^3,
\]

contradicting (G). Therefore

\[
2(s+1)>3r,
\]

so integrality gives

\[
\boxed{2s\ge3r-1.}
\tag{H}
\]

But then

\[
\begin{aligned}
&2s^2-(3r-3)s-(r+1)\\
&=s(2s-3r+3)-(r+1)\\
&\ge2s-r-1\\
&\ge2r-2>0,
\end{aligned}
\]

contradicting (F).

Thus no realized common root exists for `r>=11`.

## 7. r=7

Condition (F) becomes

\[
2s^2<18s+8.
\]

At `s=10` the left side already exceeds the right by 12, and the difference increases thereafter, so

\[
s\le9.
\]

Since `p<=5`, (A) gives

\[
k^2<5\cdot9\cdot11=495,
\]

hence `k<=22`.

But `r=7` is lower-band only when

\[
49<2k,
\]

which forces `k>=25`, a contradiction.

## 8. r=5

Condition (F) becomes

\[
2s^2<12s+6.
\]

At `s=7` the left side already exceeds the right by 8 and the gap increases thereafter, so

\[
s\le6.
\]

Since `p<=3`, (A) gives

\[
k^2<3\cdot6\cdot8=144,
\]

so `k<=11`.

But the lower-band condition for `r=5` is

\[
25<2k,
\]

forcing `k>=13`, again impossible.

## 9. The final small-prime pair r=3, p=2

Only

\[
(p,r)=(2,3)
\]

remains. Conditions (A) and (B) become

\[
\boxed{k^2<2s(s+2),}
\tag{I}
\]

\[
\boxed{3s^2\le k^2+2k.}
\tag{J}
\]

### 9.1 Exclude s>=8

From (I),

\[
k^2<2(s+1)^2.
\]

Since

\[
49\cdot2=98<100,
\]

we get

\[
49k^2<100(s+1)^2,
\]

and therefore

\[
7k<10(s+1).
\]

Hence

\[
49(k^2+2k)
<100(s+1)^2+140(s+1).
\]

Together with (J),

\[
147s^2
<100(s+1)^2+140(s+1),
\]

which simplifies to

\[
47s^2<340s+240.
\]

At `s=8`, however,

\[
47s^2-(340s+240)=48>0,
\]

and the difference increases for every `s>=8`. Contradiction.

Thus

\[
s\le7.
\]

### 9.2 Only k=9,10,11 remain

Using (I) and `s<=7`,

\[
k^2<2\cdot7\cdot9=126.
\]

Under the theorem hypothesis `k>=9`, only

\[
k=9,10,11
\]

remain.

- `k=9`: (J) gives `s<=5`, but the right side of (I) is then at most `70<81`;
- `k=10`: (J) gives `s<=6`, but the right side of (I) is at most `96<100`;
- `k=11`: (J) again gives `s<=6`, but `96<121`.

All cases contradict (I). Therefore `(2,3)` also cannot collide for `k>=9`, completing L055. ∎

## 10. Sharpness: k=8 has a realized collision

At `k=8`, both 2 and 3 are lower-band primes and

\[
W_2(8)=[33,40],
\qquad
R_2(W_2)=\{5,6\},
\]

while

\[
W_3(8)=[22,26],
\qquad
R_2(W_3)=\{4,5\}.
\]

Therefore

\[
5\in G_2(8)\cap G_3(8).
\]

So the uniform eventual threshold `k>=9` is sharp.

A bounded audit further finds realized lower-band cross-shell root collisions only at

\[
k=5,6,8,
\]

all from `(p,r)=(2,3)`. That enumeration supports the implementation but is not part of the proof.

## 11. Exact relation to L052

L052 is not discarded.

It proves the coarser candidate-pair statement: even without knowing which branch inside the exact window is realized, the full pairs `{j_p,j_p+1}` are cross-shell disjoint from `k>=15`.

L055 uses more retained information — the L054 exact windows — and therefore advances separation of the **realized images** to `k>=9`.

The two results form a clear precision hierarchy:

\[
\boxed{
\text{candidate-superset precision}:15
\quad\longrightarrow\quad
\text{actual-window precision}:9.
}
\]

This is a strict number-theoretic example of higher structural precision eliminating false collisions.

## 12. A2 meaning: the root coordinate already recovers the shell label

By P023-S8-T02, L055 is equivalent to the statement that for the lower band at `k>=9`, after exact factor stripping and square-root projection, the least-prime shell label `p` remains a function of the retained root coordinate.

But `R_2` can still be many-to-one inside one window, so this does **not** recover the original cofactor or composite state.

Hence

\[
\boxed{
\text{shell identity retained}
\neq
\text{full state retained}.
}
\]

## 13. Consequences for the next P017 step

From `k>=9`, there is no realized competition among lower-band least-prime shells at the root scale.

The next recursion should therefore stop paying a uniform multiplicity-two cost for that false competition. The actual remaining problems are:

1. composite capacity inside each unique exact p-rough subwindow;
2. within-shell many-to-one merging under the root coordinate;
3. further compression of realized subwindows by the L053 multiplicity-sensitive mirror CRT state;
4. the hard core consisting of singleton small-prime support plus a large-prime tail.

In particular, exact windows must not be re-expanded to complete target root basins, or the false collisions eliminated by L055 will be reintroduced.

## 14. Executable audit

- `src/enterprise_math/p017_actual_root_separation.py`
- `tests/test_p017_actual_root_separation.py`
- `experiments/p017_actual_root_separation_probe.py`

Regression pins the sharp `k=8,p=2,r=3,root=5` witness and checks pairwise actual-image separation for every `9<=k<2000`; an independent probe extends the scan below `k=5000` and records all small collisions.

Historical novelty remains `NOVELTY_UNVERIFIED`. The proof itself is elementary integer arithmetic; the project-specific value is that exact-window and image-separation tools expose a stronger P017 structure than the earlier enlarged-candidate analysis.
