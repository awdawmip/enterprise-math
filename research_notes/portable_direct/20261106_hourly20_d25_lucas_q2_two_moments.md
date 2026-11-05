# D25 — Signed two-digit Lucas/carry theorem for the original-216 integer shadow

Date: 2026-11-06. Classification: AUTHOR-DERIVED ALGEBRA / FINITE-EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM.

Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`. Publication: \`TP2-B6F4FC938FF94941C1B7\`. Frozen science: \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. This is an ordinary integer/arithmetic observer; original native H0/B0 is NOT_RUN.

## Input reused without recredit

The earlier signed integer shadow is
\[
C_n=\sum_{k=0}^{2n}(6k+1)(-1)^k2^{2n-k}\binom{2n}k\binom{3n}k\binom{4n}k.
\]
The earlier mod-q Lucas decomposition for prime q dividing 6n+1 is an input. The new unit proves a genuine second-digit decomposition.

## General theorem (any n>=0 and prime q>=5)

Write n=qN+r, 0<=r<q. For i=2,3,4 define
\[
s_i=ir-q\lfloor ir/q\rfloor,\qquad M_i=iN+\lfloor ir/q\rfloor.
\]
All denominators below are units at q. Let a=-1/2 modulo q², \(\phi_q(2)=(2^{q-1}-1)/q\bmod q\), \(H_j=\sum_{t=1}^j1/t\bmod q\). Define
\[
u_j=a^j\prod_i\binom{s_i}j,\quad(0\le j\le J=\min_i s_i),\qquad
v_\ell=a^\ell\prod_i\binom{M_i}\ell,\quad(0\le\ell\le\min_i M_i).
\]
The **two high moments** and low moments are
\[
T=\sum_\ell v_\ell\bmod q^2,\quad T_1=\sum_\ell \ell v_\ell\bmod q,\quad
L=\sum_{j=0}^J(6j+1)u_j\bmod q^2,\quad Z=\sum_{j=0}^J u_j\bmod q.
\]
For each i=2,3,4 define, modulo q,
\[
U_i=\sum_{j=0}^J(6j+1)u_j(H_{s_i}-H_{s_i-j}),\qquad
V_i=\sum_{j=0}^J(6j+1)u_j(H_{s_i-j}-H_j).
\]
The separate one-carry coefficients are
\[
K_i=\sum_{s_i<j\le\min_{h\ne i}s_h}(6j+1)a^j
  \tau(s_i,j)\prod_{h\ne i}\binom{s_h}j,\quad
\tau(s,j)=(-1)^{j-s+1}s!(j-s-1)!/j!\pmod q.
\]
Empty sums vanish. Put
\[
A=2N\phi_q(2)L+\sum_i M_i(U_i+K_i),\qquad
B=6Z-\phi_q(2)L+\sum_i(V_i-K_i)\pmod q.
\]
Then the following identity is **proved for every such n,q**, without requiring q|6n+1:
\[
\boxed{C_n\equiv 2^{2(N+r)}\bigl[LT+q(AT+BT_1)\bigr]\pmod{q^2}.}\tag{1}
\]

### Proof kernel

For q>=5, the q-free factorial part obeys
\[
\frac{(qM+s)!}{q^M M!}\equiv((q-1)!)^M s!(1+qM H_s)\pmod{q^2}
\]
because \(H_{q-1}=0\bmod q\). Hence for j<=s:
\[
\binom{qM+s}{q\ell+j}\equiv \binom M\ell\binom sj
[1+q(MH_s-\ell H_j-(M-\ell)H_{s-j})]\pmod{q^2}.
\]
For j>s the base-q borrow yields
\[
\binom{qM+s}{q\ell+j}\equiv q\,\binom M\ell (M-\ell)\tau(s,j)\pmod{q^2}.
\]
The latter formula also holds when the high binomial is divisible by q; products with two carries vanish modulo q². With \(a^{q\ell+j}=a^{\ell+j}(1-q\ell\phi_q(2))\) and
\(2^{2n}=2^{2(N+r)}(1+2qN\phi_q(2))\bmod q²\), expand
\(6(q\ell+j)+1=(6j+1)+6q\ell\), collect zero-carry and one-carry terms, and separate their \(\ell\)-dependence into T and T1. This gives (1). The formula retains the signed original index k=qell+j, binomial ancestry, each borrow/carry, Fermat and harmonic corrections.

## Specialization to q|6n+1

Here the old low-digit theorem gives \(L\equiv W_q\bmod q\). Also the three residues s2,s3,s4 are distinct, with
\[
q\equiv1\bmod6:\ s_2<s_3<s_4;\qquad
q\equiv5\bmod6:\ s_4<s_3<s_2.
\]
Therefore *exactly one carry channel can potentially contribute* (K2 or K4, respectively). This is a prime-class-dependent oriented signed observer, not an assumption of cancellation.

Whenever L=0 modq (the frozen first-digit hypothesis in its applicable class), define \(\lambda=L/q\bmod q\) using the q² residue. Dividing the theorem gives the **exact reduced second-digit certificate**
\[
\boxed{q^2\mid C_n\iff(\lambda+A)(T\bmod q)+B(T_1\bmod q)=0\bmod q.}\tag{2}
\]
For q²|6n+1 this makes the prime-power conjecture a low-sum/two-high-moment condition instead of a full q-by-N digit-pair convolution. It remains open to prove (2) vanishes for all such n and q.

## Computation: exact, reproducible, independent original sum

Companion standard-library script: \`research_notes/portable_direct/d25_lucas_q2_factorization_20261106.py\`. It performs **588/588** independent direct comparisons against the original integer-binomial C_n modulo q² for q=5,7,11,13,17,19,23,29,31 and n=0,...,min(4q+5,90)-1. Additionally 11/11 targeted independent direct checks at n=(q²-1)/6 for primes q=5,...,41 yield C_n mod q²=0. On 166 primes 5<=q<=1000, the proved two-moment formula (rather than the original long sum for the larger primes) yields 166/166 zero residues at n=(q²-1)/6.

Selected exact residues: (q,n,6n+1,C_n mod q²,L,T,T1 mod q,A,B,K_single):
\[
(5,9,55,5,5,6,0,3,4,3),\quad
(13,2,13,143,104,1,0,0,6,8),
\]
\[
(13,28,169,0,104,104,0,6,6,8),\quad
(19,3,19,171,76,1,0,0,6,17),
\]
\[
(19,60,361,0,76,247,0,16,6,17),\quad
(37,80,481,296,851,554,431,5,6,26).
\]
All finite evidence is integer exact. Tests are not the universal proof.

## Source boundary / next action

The old Source native checkpoint, contributor ids, two recorded completed units, original signed odd branch and frozen input pins remain unchanged; this is an author-side portable science artifact. D25 mother goal remains \(\Delta_p-R_p=0\bmod p\) for p=13,19 mod24 (original W_p=p mod p³ target). Next non-repeating subunit: symbolically evaluate the low coefficient \(\lambda\), the unique K, and the high moments under q²|6n+1 to resolve (2), then connect only genuinely source-preserving cancellations to the signed F,H second-digit ports. Alternative: a direct finite-sum telescoper for original F,H, rather than more global prime scanning. Native p373 original-class H0/B0, [X]U mod139129, Frobenius direction/eta/kappa and independent review remain open.

Authorship: author-side exact derivation; no new service-issued Researcher, CLAIM, OPEN, Source checkpoint, Result or independent acceptance is claimed for this file.
