# R161 — Global Sturmian saturation threshold and unique extremisers

Date: 2026-11-15, Asia/Shanghai. Status: **AUTHOR_PROVED (all m ≥ 5); NOT_REVIEWED**. Observer: the external finite-Sturmian tied-phase integer-intercept scalar model, not a native X6 or BRC realization. Scientific input remains frozen at 43ec6098b1330ae86d0a7863be336c5d97f6ef34.

Predecessors: R157 exact extremal absence family at faaf0e42eac30d3a2cafdbefe967a0785c560b2d; R158 exact residue certificates at c96a9e24905566bba302ed82b45590f3c3812668; R159 reversal and prefix cuts at 014bc02903e83d7aad4b4bc18713afeee1c1ad96; R160 Farey minimum gap at c47e00fd99dc77fa33d75242d79d8eec9ae83def.

## 1. Definitions and global theorems

For an admitted binary word \(w=w_1\cdots w_m\), put \(p_0=0\), \(p_j=\sum_{i=1}^{j}w_i\). The open slope support \(I_w=(\alpha,\beta)\subseteq(0,1)\) is the intersection of the strict inequalities \((q-1)/k<\theta<(q+1)/k\), over every length-\(k\) contiguous factor having \(q\) ones. Define

\[
 A=\min_{0\le j\le m}(p_j-j\alpha),\quad B=\max_{0\le j\le m}(p_j-j\beta),\quad
 \Delta=\beta-\alpha,\quad W_w=(B-A)/\Delta.
\]

The exact integer-phase count for integer \(L\ge1\) is

\[
 C_w(L+1)=\#\{z\in\mathbb Z:L\alpha-(1+A)<z<L\beta-B\}.
\]

Let \(T_w\) be the least \(K\ge2\) such that \(C_w(K')>0\) for every \(K'\ge K\), and \(T(m)=\max_{|w|=m}T_w\).

**Theorem R161A (sharp global intercept-width envelope).** For every \(m\ge5\),

\[
\boxed{\max_w W_w=\frac{m(m-3)}2.}
\]

**Theorem R161B (exact global saturation threshold).** For every \(m\ge5\),

\[
\boxed{T(m)=(m-2)\left\lfloor\frac{m-1}{2}\right\rfloor+1.}
\]

In **both** theorems, the complete set of maximizing words consists of exactly

\[
\boxed{01^{m-2}0\quad\text{and}\quad 10^{m-2}1.}
\]

## 2. A sharp separation between the first two Farey double gaps

**Lemma.** If \(m\ge9\), among the spans of three consecutive fractions of the Farey sequence \(\mathcal F_m\), the only spans smaller than

\[
\delta_2=\frac{2}{(m-1)(m-3)}
\]

are the two endpoint triples

\[
\frac1m<\frac1{m-1}<\frac1{m-2},\qquad
1-\frac1{m-2}<1-\frac1{m-1}<1-\frac1m.
\]

Their spans equal \(\delta_1=2/[m(m-2)]\). The value \(\delta_2\) is attained by the consecutive triple \(1/(m-1)<1/(m-2)<1/(m-3)\), so it is exactly the second distinct smallest span.

*Proof.* Take consecutive reduced Farey fractions \(a/b<p/q<c/d\). The adjacent determinant identities imply

\[
 pb-aq=1,\qquad cq-pd=1,\qquad q\mid(b+d),
\]

and \(b,d,q\le m\), \(\gcd(b,q)=\gcd(d,q)=1\). Their full two-cell width is

\[
\delta=\frac1{bq}+\frac1{qd}=\frac{b+d}{bdq}.
\]

All possibilities split according to the middle denominator:

- \(q\le m-4\): \(\delta\ge2/(mq)\ge2/[m(m-4)]>\delta_2\).
- \(q=m-3\): for \(m\ge10\), \(b+d=kq\le2m\) forces \(k=1,2\). When \(m=9\), \(k=3\) would force \(b=d=9\), contrary to coprimality with \(q=6\). At \(k=1\), \(\delta=1/(bd)\ge4/q^2>\delta_2\); at \(k=2\), \(\delta=2/(bd)\ge2/q^2>\delta_2\).
- \(q=m-2\): only \(k=1,2\) are possible. The first yields \(\delta\ge4/q^2>\delta_2\). In the second, \(b+d=2q\) and \(b\ne d=q\) by coprimality. Since \(b,d\) are integers, \(bd\le q^2-1=(m-1)(m-3)\), giving \(\delta=2/(bd)\ge\delta_2\).
- \(q=m-1\): \(k=1\) gives \(\delta\ge4/(m-1)^2\ge\delta_2\). At \(k=2\), \(b+d=2m-2\) and \(b,d\le m\), hence the only pairs are \((m,m-2)\), \((m-1,m-1)\), and \((m-2,m)\). The middle is not coprime to \(q\). The other two give precisely \(\delta_1\); the determinant identities fix the displayed endpoint triples.
- \(q=m\): coprimality yields \(b,d\le m-1\) and divisibility then forces \(b+d=m\). Thus \(\delta=1/(bd)\ge4/m^2\ge\delta_2\) for \(m\ge9\).

The stated \(\delta_2\) witness has consecutive Farey terms because neighboring denominator sums exceed \(m\). QED.

**Slope gap dichotomy.** R160 proved that every nonconstant admitted word has both endpoints in \(\mathcal F_m\) and contains a Farey fraction of denominator at most \(m\) strictly inside its support. Its support therefore spans at least two Farey cells. If it consists exactly of an extremal double gap, R160's equality classification forces \(10^{m-2}1\) or its complement. Any longer support contains at least two overlapping double gaps, not both extremal. Consequently **every other** admitted word at \(m\ge9\) has

\[
\boxed{\Delta\ge\delta_2.}
\]

## 3. Sharp prefix-cut deficit

**Lemma.** Every nonconstant admitted word of length \(m\) satisfies

\[
\boxed{B-A\le \max(1-\Delta,\;1-1/m)=1-\min(\Delta,1/m).}
\]

*Proof.* Put \(X_j=p_j-j\alpha\) and \(Y_j=p_j-j\beta=X_j-j\Delta\). R159's endpoint range identity gives \(\max_j X_j=A+1\). Thus for \(j\ge1\), \(Y_j-A\le1-\Delta\). The empty prefix contributes \(Y_0-A=-A\).

The factor inequality for the prefix of length \(j\ge1\) gives \(\beta\le(p_j+1)/j\). Since \(\alpha<\beta\), \(X_j=p_j-j\alpha>-1\). Write the reduced endpoint \(\alpha=a/b\), with \(b\le m\); every \(X_j\) is an integer multiple of \(1/b\). Hence \(\min_j X_j=A\ge-1+1/b\ge-1+1/m\) (also true for the empty prefix). Thus \(-A\le1-1/m\). Taking the maximum of \(Y_j-A\) proves the bound. QED.

In particular, \(B-A\le1\); for \(\Delta\le1/m\), we have \(W_w\le1/\Delta-1\). Constant words have \(W_w=0\).

## 4. All-length proof of R161A and R161B, \(m\ge9\)

Put \(E_m=m(m-3)/2\) and \(M_m=(m-2)\lfloor(m-1)/2\rfloor-1\). The open phase interval in the definition of \(C_w(L+1)\) has width

\[
1+L\Delta-(B-A)=1+\Delta(L-W_w).
\]

Thus whenever \(L>W_w\), its width exceeds one, so it contains an integer. Therefore any final missing position satisfies \(L\le\lfloor W_w\rfloor\).

The already proved R157 exact extremal-family formulas give, for both \(01^{m-2}0\) and \(10^{m-2}1\),

\[
W_w=E_m,\qquad \text{last missing }L=M_m,\qquad T_w=M_m+2.
\]

For a nonextremal, nonconstant word the two lemmas yield

\[
W_w\le1/\Delta\le\frac{(m-1)(m-3)}2<E_m.
\]

So the extremal pair uniquely maximize \(W\), proving R161A at \(m\ge9\).

If \(m\) is **odd**, then \(M_m=E_m\) is an integer. The last inequality ensures \(\lfloor W_w\rfloor<M_m\) for every nonextremal word. Hence the extremal pair alone attain the latest missing position \(M_m\), proving R161B and uniqueness.

If \(m\) is **even**, \(m\ge10\), then

\[
\frac{(m-1)(m-3)}2=M_m+\frac12.
\]

For a nonextremal word with \(\Delta\le1/m\), the sharper deficit lemma yields \(W_w\le1/\Delta-1\le M_m-1/2\), whence \(\lfloor W_w\rfloor\le M_m-1\). If instead \(\Delta>1/m\), then \(W_w\le1/\Delta<m\le M_m\) for even \(m\ge10\), so again \(\lfloor W_w\rfloor\le M_m-1\). Thus no nonextremal word can be missing at \(L=M_m\). The extremal pair attain that last missing position by R157. R161B and uniqueness follow for all even \(m\ge10\). QED.

## 5. Complete finite exceptional lengths and executable verification

The cases \(m=5,6,7,8\) are completed exhaustively with exact fractions, scanning all \(2^m\) binary words. A word is admitted precisely when its factor-slope interval is nonempty. The script calculates all prefix cuts and checks each final missing position by **both** direct count scanning up through \(\lfloor W\rfloor\) and the independent R158 residue certificate. Results:

| m | candidates | admitted | max W | final missing L | T(m) | complete maximizer set |
|--:|--:|--:|--:|--:|--:|---|
| 5 | 32 | 24 | 5 | 5 | 7 | 01110, 10001 |
| 6 | 64 | 36 | 9 | 7 | 9 | 011110, 100001 |
| 7 | 128 | 54 | 14 | 14 | 16 | 0111110, 1000001 |
| 8 | 256 | 76 | 20 | 17 | 19 | 01111110, 10000001 |

The companion exact checker verifies the second-gap lemma over all \(9\le m\le100\) by enumerating Farey triples, and the R157 extremal formula for both words at every \(5\le m\le160\) (312 word instances). It returned **R161_EXACT_CHECKS_PASS**.

The general results rely on the symbolic argument; the finite computations close exactly four exceptional lengths and provide corroboration. All arithmetic is exact. Independent mathematical review remains NOT_REVIEWED.

## 6. Further mathematical questions and status

The previously open sharp width envelope and global saturation threshold are now closed within this scalar model, including all maximizing words. The next separate problem is to prove the all-length upper bound of two on the size of a signature fiber \(w\mapsto(\alpha,\beta,U,V)\), observed exhaustively through \(m=64\), or find a longer counterexample. Retain word/source provenance when compressing this observer for BRC; a native X6 transfer requires its own typed embedding.

Control provenance: original exact Source task lookup em-r1-20261115-0557-s23-current-task-01 returned SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY at commit 71941840047e6f1bafce016f14c3bfc866f428cc on 2026-11-15 05:58:39 Asia/Shanghai. The lookup reports publication-directory absence, not a native owner projection. This is independent portable author research, not a formal CLAIM, RR, driver review or Foundation adoption.
