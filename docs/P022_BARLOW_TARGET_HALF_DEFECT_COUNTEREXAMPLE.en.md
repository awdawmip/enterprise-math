# P022 — Target-Family Half-Defect Valuation Reversal at `p=369581`

Status: `ACTIVE RESEARCH NOTE / EXACT COUNTEREXAMPLE / NEGATIVE BOUNDARY`  
Owner: `program/p022-geometry-v2`  
Depends on: half-index Franel divisor; canonical A-elimination; midpoint transversality; companion/support routing  
Cross-route relevance: P018 defect sign/cancellation; P023 quotient-stable witnesses and minimal repair

## 1. The conjecture being tested

For primes

\[
p>5,
\qquad
p\equiv5\text{ or }23\pmod{24},
\]

put

\[
m=\frac{p-1}{2}.
\]

The half-index theorem gives

\[
p\mid F_m
\]

and the A-boundary

\[
2m-1=p-2
\]

is composite.

Earlier finite pressure suggested two stronger statements:

1. the canonical A-elimination support might always avoid earlier Franel zero digits in this residue family;
2. consequently the pure defect might satisfy
   \[
   v_p(D_m)=1.
   \]

Both statements are false.

---

## 2. P022-LI38 — exact target-family counterexample

Take

\[
\boxed{p=369581.}
\]

It is prime and

\[
369581\equiv5\pmod{24}.
\]

Therefore

\[
\boxed{m=184790}
\]

belongs to the declared target family.

The midpoint Franel value is a forced zero modulo `p`.  Independent recurrence modulo `p^2` gives

\[
\boxed{
\frac{F_m}{p}
\equiv153310\pmod p,
}
\]

which is nonzero. Hence

\[
\boxed{v_p(F_m)=1.}
\]

So the midpoint transversality/simple-lift mechanism behaves exactly as the earlier conjectural picture expected.

The failure occurs in the support correction.

---

## 3. An earlier Franel zero is exceptionally explicit

The eighth Franel number is

\[
F_8
=\sum_{k=0}^8\binom8k^3
=739162.
\]

But

\[
\boxed{
739162=2\cdot369581.}
\]

Therefore

\[
\boxed{v_p(F_8)=1.}
\]

This is not a numerical near-hit: the earlier Franel term is exactly twice the target prime.

---

## 4. The canonical A-elimination uses the earlier zero with exponent two

The exact canonical central-binomial relation at `m=184790` is

\[
\boxed{
\begin{aligned}
A_m={}&
A_1^3A_2^{-2}A_4A_5^{-1}A_6
A_8^2A_9^{-2}\\
&\cdot A_{543}A_{544}^{-1}
A_{8799}^{-1}A_{8800}A_{184789}.
\end{aligned}}
\]

Thus

\[
\boxed{\alpha_{m,8}=2.}
\]

A direct recurrence scan modulo `p` across the complete canonical support shows that `j=8` is the **only** support index at which the Franel value vanishes modulo `p`.

Hence the p-adic correction contributed by the eliminated coordinates is exactly

\[
\boxed{
\sum_{j<m}\alpha_{m,j}v_p(F_j)
=2.}
\]

---

## 5. P022-LI39 — the defect valuation changes sign

By definition,

\[
D_m
=
\frac{F_m}{\prod_{j<m}F_j^{\alpha_{m,j}}}.
\]

Therefore

\[
\begin{aligned}
v_p(D_m)
&=v_p(F_m)
-
\sum_{j<m}\alpha_{m,j}v_p(F_j)\\
&=1-2.
\end{aligned}
\]

Thus

\[
\boxed{
v_{369581}(D_{184790})=-1.}
\]

The forced midpoint prime does **not** disappear.  It survives the canonical quotient/elimination with the opposite valuation sign:

\[
\boxed{
\text{local numerator witness}
\longrightarrow
\text{defect denominator witness}.}
\]

This falsifies the stronger conjecture

\[
\boxed{v_p(D_{(p-1)/2})=+1}
\]

inside the very residue family for which it had been proposed.

It also falsifies global support avoidance in that family.

---

## 6. Why earlier pressure tests missed it

Earlier direct prime scans stopped below

\[
p=50000.
\]

The first counterexample found by the reverse Franel/support search is much larger:

\[
p=369581.
\]

The productive reversal was to fix a small earlier Franel index `j`, factor `F_j`, and ask whether one of its large prime divisors makes `j` appear in **that prime's own** canonical A-support.

Here

\[
2j+1=17
\]

is prime, and

\[
17\mid m.
\]

So `j=8` lies directly in the first prime-halving ancestry layer of `m`.  The actual canonical coefficient turns out to be `+2` after all representation paths are combined.

This demonstrates why increasing the old prime cutoff was a weak strategy: the dangerous Franel index can be tiny while the target prime is very large.

---

## 7. Relation to the universal companion

The midpoint offset of the earlier zero is

\[
d=m-8=184782.
\]

The universal integer companion therefore satisfies

\[
\boxed{369581\mid K_{184782}.}
\]

This offset lies in the far region permitted by the support-localization theorem.

So the counterexample is fully consistent with all previous exact reductions:

\[
\text{Franel zero}
\leftrightarrow
p\mid K_d
\leftrightarrow
\text{companion hit},
\]

and in this case the terminal prime

\[
2j+1=17
\]

is genuinely present in the prime-halving ancestry of `m`.

---

## 8. What remains viable after the counterexample

Several weaker statements survive.

### 8.1 Forced midpoint divisibility remains exact

Nothing changes in

\[
p\mid F_m.
\]

### 8.2 Midpoint simple lifting remains viable

This counterexample still has

\[
v_p(F_m)=1.
\]

So it does not falsify the transversality/non-Wieferich conjecture for the midpoint itself.

### 8.3 The prime remains a nonzero defect witness

Although the sign reverses,

\[
v_p(D_m)=-1\ne0.
\]

Thus a weaker possible target is

\[
\boxed{v_p(D_m)\ne0}
\]

rather than `+1`.  This is **not** promoted to a conjecture here without further pressure testing, because the earlier broader forced family already contains the exact cancellation example `p=157` with defect valuation zero.

Whether zero can occur inside the narrower `5,23 mod24` target family is now the correct next counterexample question.

---

## 9. Precision / quotient lesson

The negative result is stronger than ordinary information loss.

A coordinate change can alter not merely the presence/absence of a local witness but its **signed valuation orientation**:

\[
\boxed{
\text{visible numerator information}
\not\Rightarrow
\text{same-sign quotient information}.}
\]

The canonical operation algebra must therefore retain enough state to compute the entire valuation correction, not just a bit recording whether the prime was locally visible before elimination.

This is a sharp P022 specialization of the A2/P023 rule that future-safe precision is operation-relative.

---

## 10. Status corrections

Any older P022 note saying that the target `5,23 mod24` family had shown no support hit in finite pressure tests must now be read as superseded finite evidence.

The current exact state is:

- target support avoidance: **REJECTED**;
- universal `v_p(D_m)=+1`: **REJECTED**;
- midpoint `v_p(F_m)=1`: still open globally and survives this example;
- target-family nonzero defect valuation: open;
- full pure-defect multiplicative independence: open.

---

## 11. Executable assets

Added:

- `src/enterprise_math/p022_barlow_target_half_defect_counterexample.py`;
- `tests/test_p022_barlow_target_half_defect_counterexample.py`.

The certificate reconstructs the canonical A-relation, the identity `F_8=2p`, the unique support zero, the nonzero midpoint lift modulo `p^2`, and the exact resulting defect valuation `-1` without ever constructing the gigantic integer `F_184790`.
