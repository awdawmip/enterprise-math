# Legendre Pressure Test — Supplement 15

Status: `ACTIVE RESEARCH NOTE`  
Scope: cross-shell packing of P018-T110 target roots in the lower least-factor band  
Depends on: P017 L001 root-factor horizon, canonical P018-T110–T112  
Discipline: this note does **not** prove Legendre's conjecture. It uses only elementary integer inequalities, prime parity/spacing, and the already-canonical quotient-root transport. No prime-distribution estimate is invoked.

## 1. Why lower-band descent still needs a cross-shell theorem

P018-T110–T112 changed the lower-band problem qualitatively.

If

\[
n=pq,
\qquad k^2<n<(k+1)^2,
\]

and `p` is the least prime factor, then after extracting `p` the cofactor root lies at a strictly lower square-root scale.

For one lower-band prime

\[
p^2<2k,
\]

define

\[
\boxed{
j_p
=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right).}
\]

T110 says the cofactor root can only lie in

\[
\boxed{C_p(k)=\{j_p,j_p+1\}.}
\]

A remaining danger is cross-shell accumulation: many different least-prime shells might descend to the same lower root scale, so a recursive argument could still pay a large multiplicity.

The next theorem shows that this does not happen.

---

## 2. L051 — Lower-band root-target overlap is at most two

Status: `PROVED`.

Let

\[
\mathcal P_L(k)
=\{p\le k:p\text{ prime and }p^2<2k\}.
\]

For each `p in P_L(k)` define `j_p` and `C_p(k)` as above.

Then every integer root index `t` belongs to at most two candidate pairs:

\[
\boxed{
\#\{p\in\mathcal P_L(k):t\in C_p(k)\}
\le2.
}
\]

The bound is sharp: at `k=5`, the target root `3` lies in the candidate pairs for `p=2` and `p=3`.

We prove a stronger endpoint-separation statement first.

---

## 3. Stronger form: every third shell is separated by two root levels

Take three distinct lower-band primes

\[
p<q<r.
\]

Then

\[
\boxed{j_p\ge j_r+2.}
\]

This is the real packing theorem. L051 follows immediately from it.

Let

\[
u=j_r.
\]

By definition,

\[
u^2
\le
\left\lfloor\frac{k^2}{r}\right\rfloor,
\]

so

\[
\boxed{ru^2\le k^2.}
\]

The key is to show that `u` is already at least `r`.

---

## 4. Lower-band self-amplification: u >= r

Because there are three distinct primes ending at `r`, one has

\[
r\ge5.
\]

The lower-band condition gives

\[
r^2<2k.
\]

Squaring,

\[
r^4<4k^2.
\]

Since `r>=5`,

\[
4r^3<r^4.
\]

Therefore

\[
4r^3<4k^2,
\]

hence

\[
r^3<k^2.
\]

In particular,

\[
r^2
\le
\left\lfloor\frac{k^2}{r}\right\rfloor.
\]

Taking integer square roots gives

\[
\boxed{u=j_r\ge r.}
\]

This elementary inequality is what lets prime spacing become root-scale spacing.

---

## 5. General prime-spacing case

Except for the prime triple

\[
(p,q,r)=(2,3,5),
\]

we have

\[
\boxed{r-p\ge4.}
\]

Indeed:

- if `p>=3`, all three primes are odd, so each successive gap is at least `2`;
- if `p=2` and the triple is not `(2,3,5)`, then `r>=7`.

Since `u>=r`, this gives

\[
p\le r-4\le u-4.
\]

Now compare the two relevant square thresholds:

\[
\begin{aligned}
ru^2-p(u+2)^2
&=(r-p)u^2-4pu-4p\\
&\ge4u^2-4p(u+1).
\end{aligned}
\]

Using `p<=u-4`,

\[
p(u+1)
\le
(u-4)(u+1)
=u^2-3u-4.
\]

Hence

\[
ru^2-p(u+2)^2
\ge12u+16>0.
\]

Therefore

\[
\boxed{p(u+2)^2<ru^2\le k^2.}
\]

Thus

\[
(u+2)^2
\le
\left\lfloor\frac{k^2}{p}\right\rfloor,
\]

which implies

\[
\boxed{j_p\ge u+2=j_r+2.}
\]

---

## 6. The special triple (2,3,5)

It remains to handle

\[
p=2,
\qquad r=5.
\]

The argument of Section 4 gives

\[
u=j_5\ge5.
\]

For `u>=5`,

\[
5u^2-2(u+2)^2
=3u^2-8u-8.
\]

Since `u>=5`,

\[
3u^2\ge15u,
\]

so

\[
3u^2-8u-8
\ge7u-8>0.
\]

Thus again

\[
2(u+2)^2<5u^2\le k^2,
\]

and therefore

\[
\boxed{j_2\ge j_5+2.}
\]

So the stronger three-shell separation holds in every case.

---

## 7. Deduction of the multiplicity bound

Suppose, for contradiction, that one root index `t` belonged to three candidate pairs associated with

\[
p<q<r.
\]

Then

\[
t\in\{j_p,j_p+1\}
\quad\text{and}\quad
 t\in\{j_r,j_r+1\}.
\]

Therefore both `j_p` and `j_r` belong to

\[
\{t-1,t\},
\]

so

\[
j_p-j_r\le1.
\]

But Sections 3–6 prove

\[
j_p\ge j_r+2,
\]

a contradiction.

Hence

\[
\boxed{
\#\{p\in\mathcal P_L(k):t\in\{j_p,j_p+1\}\}
\le2.
}
\]

∎

---

## 8. What L051 changes in the lower-band recursion

T110–T112 provide **vertical** structure inside one shell:

\[
\text{factor extraction}
\longrightarrow
\text{strictly smaller root scale}.
\]

L051 adds the missing **horizontal** structure across shells:

\[
\boxed{
\text{one lower target root scale}
\longleftarrow
\text{at most two lower-band least-prime shells}.
}
\]

This is qualitatively different from summing one recursion independently over every small prime.

It suggests that lower-band recursion should be reindexed by the descended root scale rather than by the original least prime.

However, L051 alone is not yet a useful mass bound. Replacing every exact cofactor subwindow by an entire target square basin is far too coarse and can exceed the original `2k` basin size by a large factor. The exact quotient subwindows and roughness/least-factor constraints must be retained.

---

## 9. Relation to T113 threshold coherence

P018-T113 sharpens each shell's candidate pair into one exact threshold response.

For a basin offset

\[
n=k^2+s,
\]

one has

\[
R_2\!\left(\left\lfloor\frac np\right\rfloor\right)
=j_p+\mathbf1[s\ge\tau_p].
\]

L051 says that even before using this threshold bit, a target root has at most two possible lower-band shell channels.

T113 can therefore only reduce the actual channel count further, state by state.

This is the right order of use:

1. L051 gives a uniform cross-shell packing bound;
2. T113 selects the actual branch by one basin-offset threshold;
3. the descended root bounds the next least factor by L001.

---

## 10. Relation to the mirror certificate

For mirror radius `rho` around `M=k(k+1)`, the two basin offsets are

\[
s_-=k-\rho,
\qquad
s_+=k+\rho.
\]

T113 turns each least-factor root branch into a radius half-interval condition, while the existing mirror route supplies CRT progressions and transverse-support separation.

L051 adds a further global restriction: for any descended root cutoff, there are at most two lower-band least-prime shell channels that can feed it.

This combination is a natural candidate for **least-factor-gated mirror capacity**. It should be tested before introducing any further unstructured mirror moments.

---

## 11. Executable validation

`src/enterprise_math/p017_lower_band.py` provides:

- `lower_band_primes`;
- `lower_band_base_root`;
- `lower_band_candidate_roots`;
- `lower_band_root_channels`;
- `lower_band_root_overlap_bound`.

`tests/test_p017_lower_band.py` checks:

- the lower-band definition and candidate roots;
- the multiplicity-two theorem over a dense bounded range;
- the stronger three-shell endpoint separation at larger roots through `k=200000`;
- the sharp first double-overlap witness `k=5`, target root `3`, shells `2` and `3`.

Finite tests audit the implementation. The proof is the integer argument above.

---

## 12. Next target

The next step must preserve **exact subwindow geometry**.

A useful recursive inequality should combine:

- T110/T112 strict root descent;
- T113 exact branch thresholds;
- L051 at-most-two cross-shell target multiplicity;
- exact cofactor-window endpoints and p-rough constraints;
- where useful, mirror CRT/least-factor gating.

If the resulting inequality reduces to ordinary Buchstab bookkeeping after a change of coordinates, it should be demoted. The goal is a genuinely smaller lower-band composite-capacity bound, not another exact reindexing.
