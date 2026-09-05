# Orientation-resolved Ramanujan traces for odd primitive denominators

Status: `FREE_RESEARCH / EXACT FINITE-TRACE THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- primitive phase-multiplication polynomials `R_n`;
- complement involution on primitive finite roots;
- odd-denominator reflection factors `Psi_d^E,Psi_d^O`;
- Ramanujan trace dictionary.

## 1. Full primitive trace for arbitrary phase multiplier

For `d>2`, define

\[
\mathcal T_d(n)
:=\sum_{\Psi_d(\alpha)=0}R_n(\alpha).
\]

Primitive roots occur in complement pairs `alpha,4-alpha`.

Phase multiplication satisfies

\[
\boxed{
R_n(4-u)=
\begin{cases}
4-R_n(u),&n\text{ odd},\\
R_n(u),&n\text{ even}.
\end{cases}}
\tag{ORT-1}

This follows internally from `C(n(tau-theta))=(-1)^n C(ntheta)`.

### odd n

Every complement pair contributes exactly four.  Since there are `phi(d)/2` pairs,

\[
\boxed{\mathcal T_d(n)=2\varphi(d),\qquad n\text{ odd}.}
\tag{ORT-2}

### even n=2q

The previously derived primitive Ramanujan trace gives

\[
\boxed{\mathcal T_d(2q)=2(\varphi(d)-c_d(q)).}
\tag{ORT-3}

Combining,

\[
\boxed{
\mathcal T_d(n)=
\begin{cases}
2\varphi(d),&n\text{ odd},\\
2(\varphi(d)-c_d(n/2)),&n\text{ even}.
\end{cases}}
\tag{ORT-4}

Thus the unsigned/full primitive `u`-trace is arithmetically blind to every odd phase multiplier.

## 2. Odd denominator orientation channels

Now let `d>1` be odd and split

\[
\Psi_d=\Psi_d^E\Psi_d^O,
\]

where `E` contains primitive even mode indices and `O` primitive odd mode indices in `1,...,d-1`.

Define orientation-resolved traces

\[
\mathcal T_d^E(n)
:=\sum_{\Psi_d^E(\alpha)=0}R_n(\alpha),
\]

\[
\mathcal T_d^O(n)
:=\sum_{\Psi_d^O(\alpha)=0}R_n(\alpha).
\]

Then

\[
\mathcal T_d=\mathcal T_d^E+\mathcal T_d^O.
\]

## 3. Even multiplier: two orientations recoalesce exactly

If `n=2q`, complement partners have equal images under `R_n`.  Complement exchanges `E` and `O`, so

\[
\boxed{
\mathcal T_d^E(2q)=\mathcal T_d^O(2q).
}
\tag{ORT-5}

Using (ORT-3),

\[
\boxed{
\mathcal T_d^E(2q)
=\mathcal T_d^O(2q)
=\varphi(d)-c_d(q).
}
\tag{ORT-6}

Thus even phase multiplication is orientation-insensitive at the trace level.

## 4. Odd multiplier: orientation difference restores Ramanujan information

Let `n` be odd.  For a primitive residue representative `1<=r<d`, define orientation sign

\[
\sigma(r)=(-1)^r,
\]

so `sigma=+1` on the even/E channel and `-1` on the odd/O channel.

The constant term `2` in `R_n=2-2C(n theta)` cancels in the signed sum because the two channels have equal cardinality.  Hence

\[
\mathcal T_d^E(n)-\mathcal T_d^O(n)
=-2\sum_{(r,d)=1}(-1)^r
C\left(\frac{nr\tau}{d}\right).
\tag{ORT-7}

Since `d,n` are odd, `n+d` is even and

\[
(-1)^r C\left(\frac{nr\tau}{d}\right)
=
C\left(\frac{(n+d)r\tau}{d}\right).
\]

Writing

\[
q=\frac{n+d}{2},
\]

the right side is the standard primitive even-phase sum.  Therefore

\[
\boxed{
\mathcal T_d^E(n)-\mathcal T_d^O(n)
=-2c_d\left(\frac{n+d}{2}\right),
\qquad n\text{ odd}.
}
\tag{ORT-8}

Together with the full trace (ORT-2),

\[
\boxed{
\mathcal T_d^E(n)
=\varphi(d)-c_d\left(\frac{n+d}{2}\right),
}
\tag{ORT-9}

\[
\boxed{
\mathcal T_d^O(n)
=\varphi(d)+c_d\left(\frac{n+d}{2}\right),
}
\tag{ORT-10}

for odd `n`.

## 5. Example d=3,n=1

The primitive roots are

\[
u_{1,3}=1\quad(O),
\qquad
u_{2,3}=3\quad(E).
\]

Thus

\[
\mathcal T_3^E(1)=3,
\qquad
\mathcal T_3^O(1)=1.
\]

Since

\[
c_3((1+3)/2)=c_3(2)=-1,
\]

(ORT-9)--(ORT-10) give exactly

\[
2-(-1)=3,
\qquad
2+(-1)=1.
\]

The full trace is four and by itself contains no sign of the Ramanujan value.

## 6. Information-loss theorem for orientation recoalescence

For odd multiplier `n`, the full trace is always

\[
2\varphi(d),
\]

independent of the arithmetic phase class.  Yet the orientation difference is

\[
-2c_d((n+d)/2),
\]

which varies nontrivially with `n`.

Therefore

\[
\boxed{
\text{FULL POSITIVE TRACE}
\text{ does not determine }
\text{ORIENTATION-RESOLVED TRACE}.
}
\tag{ORT-11}

The loss is not philosophical: explicit Ramanujan arithmetic disappears under orientation recoalescence for every odd phase multiplier.

## 7. Two complementary arithmetic channels

For odd primitive denominator `d`, the complete trace response can be read as:

```text
even phase multiplier n=2q:
    common E/O trace
    -> c_d(q)

odd phase multiplier n:
    E-O trace difference
    -> c_d((n+d)/2)
```

Thus the parity of the phase multiplier decides which finite observable carries the arithmetic information:

`EVEN_MULTIPLIER -> ORIENTATION-SYMMETRIC TRACE`.

`ODD_MULTIPLIER -> ORIENTATION-ANTISYMMETRIC TRACE`.

Freeze:

`ODD_PHASE_ARITHMETIC_IS_LOST_BY_ORIENTATION_RECOALESCENCE`.

`ORIENTATION_RESOLVED_TRACE_RESTORES_RAMANUJAN_INFORMATION`.

`PHASE_PARITY_SELECTS_SYMMETRIC_VS_ANTISYMMETRIC_ARITHMETIC_CHANNEL`.
