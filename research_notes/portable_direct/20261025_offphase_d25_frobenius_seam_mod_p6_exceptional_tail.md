# D25/LIFT — sixth-digit source-faithful Frobenius seam and exceptional genuine-tail lift

2026-10-25 | TASK_RESEARCH | PORTABLE AUTHOR PROOF / EXACT AUTHOR CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT / NONBLIND.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin: **c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged)**. This is an external p-adic arithmetic observer, not a same-class H0/B0/CM/DP representative or native Heartbeat/X6 proof.

## Source consumed without re-credit

The exact original five-port factorial/WZ identity and integral source factor jet are [here](https://github.com/awdawmip/enterprise-math/blob/6a09b88e4ca545ef5400e2e80b101028cc2420d8/research_notes/portable_direct/20261025_offphase_d25_source_factor_jet_all_precision.md), the [lifted factorization](https://github.com/awdawmip/enterprise-math/blob/745e569fc6bf9ccd8803a5cc3f169d3a33d0b335/research_notes/portable_direct/20261025_offphase_d25_lifted_frobenius_p2_seam_universal_third_digit.md), and the preceding [mod-p^5 seam](https://github.com/awdawmip/enterprise-math/blob/cda9047a08910aa6463c82c827a8e93e438099f4/research_notes/portable_direct/20261025_offphase_d25_lifted_frobenius_p5_compressed_fifth_digit.md).

For prime \(p=6m+1\ge13\), put \(n=2m\), \(h_j^{(r)}=\sum_{i=1}^j i^{-r}\), \(q_c=(c^{p-1}-1)/p\). Let \(H_p(z)\) mean the compressed source generating function (not harmonic notation). The established **exact source-labeled** identities are

\[
Q_p(z)=T_p(z)^2(R_p(z)^2A_p(z)+L_p(z)),\quad H_p(z)=A_p(z)+L_p(z),
\]
\[
T_p(z)=\prod_{j=1}^{p-1}(1+z/j),\quad R_p(z)=\frac{1-z}{1+z/(p-1)},
\]
\[
A_p(z)=2mC(z)K_U(z),\quad L_p(z)=\frac{3z}{220}B(z)P_{\rm base}(z).
\]

The exact products C, B, K_U, P_base are specified by the inherited original factorial source, retaining the old edge and all four genuine tail ports; \(Q_p(p)=(S_{m+1}-S_m)/p\).

Define p-integral \(\Theta=h_{p-1}^{(2)}/p\) and \(\Omega=h_{p-1}^{(4)}/p\). For the new low-degree source coefficients set

\[
\begin{aligned}
k_1&=4-q_{108}-2h_n^{(1)}-h_{n-1}^{(1)},\\
k_2&=2+q_{108}^2/2-h_n^{(2)}+h_{n-1}^{(2)}/2,\\
k_3&=4/3-q_{108}^3/3-2h_n^{(3)}/3-h_{n-1}^{(3)}/3,\\
J_2&=k_2+k_1^2/2,\qquad J_3=k_3+k_1k_2+k_1^3/6.
\end{aligned}
\]

The old-edge \(a_i=[z^i]A_p(z)\) through the new degree three are

\[
\begin{aligned}
a_0&=-4m,\\
a_1&=2m(3/4-2k_1),\\
a_2&=2m(-393/40+3k_1/4-2J_2),\\
a_3&=2m(-10051/400-393k_1/40+3J_2/4-2J_3).
\end{aligned}
\]

The authentic tail derivative requires
\[
g=\frac{169}{440}-2q_2-3q_3-2h_{n-1}^{(1)}
+h_5^{(1)}+2h_4^{(1)}+2-2h_2^{(1)}-h_{n+4}^{(1)},
\]
\[
\ell_1=[z]L_p(z)=\frac{752427}{3942400},\quad
\boxed{\ell_2=[z^2]L_p(z)=\frac{466056841}{4691456000}+\ell_1g.}
\]
Indeed \(P_{\rm base}(0)=1\), \(P_{\rm base}'(0)=g\), \(B(0)=250809/17920\), \(B'(0)=466056841/63974400\). No actual port is dropped. All denominators are p-units for this residue class (17 is not \(1\bmod6\); \(n+4<p\)).

## Theorem — complete sixth digit

For **all** admissible primes,

\[
\boxed{\begin{aligned}
Q_p(p)-H_p(p)\equiv {}&
2a_0p^2\\
&+[2a_1+(4-2\Theta)a_0]p^3\\
&+[2a_2+(4-2\Theta)a_1+9a_0-2\Theta\ell_1]p^4\\
&+[2a_3+(4-2\Theta)a_2+9a_1+
(20-4\Theta-\Omega)a_0-2\Theta\ell_2]p^5
\pmod{p^6}.
\end{aligned}}
\]

The newly exposed correction is the last bracket, including \(-\Omega a_0\) from the complete harmonic observer and \(-2\Theta\ell_2\) from the **authentic four-tail derivative**.

**Proof.** Put \(h_r=h_{p-1}^{(r)}\). Finite-field power sums and the involution \(j\mapsto p-j\) yield \(h_2,h_4,h_5\in p\mathbf Z_{(p)}\), \(h_1,h_3\in p^2\mathbf Z_{(p)}\), and

\[
2h_1=-ph_2-p^2h_3-p^3h_4\pmod{p^5},\qquad
2h_3=-3ph_4\pmod{p^3}.
\]

The dropped \(p^4h_5\) term lies in \(p^5\). Hence the exact binomial product \(T_p(p)=\binom{2p-1}{p-1}\) has

\[
\log T_p(p)=ph_1-p^2h_2/2+p^3h_3/3-p^4h_4/4
\equiv-p^2h_2-p^4h_4/2\pmod{p^6}.
\]

Since its valuation is at least three, the square of the exponential has no nonlinear correction before \(p^6\):

\[
\boxed{T_p(p)^2\equiv1-2p^3\Theta-p^5\Omega\pmod{p^6}.}
\]

The rational identity \(R_p(p)=(1-p)^2/(1-2p)\) directly gives
\(R_p(p)^2\equiv1+2p^2+4p^3+9p^4+20p^5\pmod{p^6}\).
Thus
\[
T_p(p)^2R_p(p)^2-1\equiv
2p^2+(4-2\Theta)p^3+9p^4+(20-4\Theta-\Omega)p^5\pmod{p^6}.
\]
Now use the *exact* labeled source identity
\[
Q_p(p)-H_p(p)=(T_p(p)^2R_p(p)^2-1)A_p(p)+(T_p(p)^2-1)L_p(p).
\]
Inserting \(A_p(p)=\sum_{i=0}^3a_ip^i+O(p^4)\), \(L_p(p)=\ell_1p+\ell_2p^2+O(p^3)\) gives the theorem. The few coefficient extractions use only rational p-units and never invert a degree index divisible by p. QED.

## Exceptional genuine-tail visibility

The full authentic-tail compression discrepancy \(E_p=(T_p(p)^2-1)L_p(p)\) now satisfies
\[
\boxed{E_p\equiv -2p^4\Theta\ell_1-2p^5\Theta\ell_2\pmod{p^6}.}
\]

The prior fifth-digit calculation identified the admissible numerator-prime exceptions \(p=13,109\), for which \(\ell_1\equiv0\pmod p\). Their **sixth-digit** coefficient is \(-2\Theta(\ell_1/p+\ell_2)\bmod p\), *not* \(-2\Theta\ell_2\). Exact modular evaluation:

| p | \(\Theta\bmod p\) | \((\ell_1/p)\bmod p\) | \(\ell_2\bmod p\) | \((E_p/p^5)\bmod p\) |
|---:|---:|---:|---:|---:|
| 13 | 12 | 6 | 12 | **10** |
| 109 | 3 | 45 | 57 | **42** |

Therefore \(v_{13}(E_{13})=v_{109}(E_{109})=5\): those ports disappear at fifth-digit precision but **reappear at sixth-digit precision**. Outside the numerator-prime exceptions and with \(\Theta\not\equiv0\pmod p\), the earlier exact valuation \(v_p(E_p)=4\) remains; no classification of all Wolstenholme primes is asserted.

## Exact author-side verification

The companion standard-library Python script reconstructs the original old-edge source product \(F_U(p)\) using its full \(p-2\) factor, and independently forms the genuine tail \(P_{\rm base}(p)\) and exact four-port transfer B(p). It checks \(F_U=T^2R^2K_U\), the arithmetic source result Q, the \(A,L\)-jets, the binomial harmonic formula, and the entire sixth-digit correction using integer p-unit inverses.

**Executed 206/206 PASS**, all primes \(13\le p<3000\), \(p\equiv1\pmod6\). Examples:
- \(p=13:\ Q-H=2857790\bmod13^6,\ E_{13}=3712930=10\cdot13^5\bmod13^6\).
- \(p=19:\ Q-H=22639754\bmod19^6\).
- \(p=109:\ Q-H=515702147458\bmod109^6,\ E_{109}=646222061058=42\cdot109^5\bmod109^6\).

The author tests verify **source-factor algebra and jets**, not an independent derivation of the original uncollapsed \(W(r,t)\) sum, a native CM/DP experiment, or a Driver review. General validity rests on the displayed proof, subject to formal mathematical review.

## Control, provenance, BRC and exact next action

BRC is **COMPOSE_APPLIED** on source-labeled ports, p-valuations and coefficient jets. A compressed scalar without seam coordinates is not automatically a future-operation-safe quotient. These arithmetic labels are not assumed to be positive-mass BRC branches or native X6 states.

Native Gateway reports no Site execution write authority; the bounded task read returned CONTROL_QUOTA and own-client checkpoint listing ACCESS_DENIED. Thus this is only a neutral portable GitHub source: **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. No own Source session, CLAIM, OPEN, checkpoint, Result, freeze, review or mathematical admission is inferred. On legal recovery, read the exact own recovery_status/request receipts and Source continuation, then attach already-completed author evidence through the actual writer/provenance mechanism rather than redoing the proof or borrowing another writer's claim.

UR V2 four-file original (historical 94,687 bytes; SHA-256 **4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76**) remains unlocated with authentic bytes. Historical UR mathematics is not reproved. The precise pending action is original-byte/staging/request retrieval, hash verification and legal writer/provenance/checkpoint, without treating unpublished uploads as durable.

D25/LIFT still needs a same-prime same-original-class normalized H0/B0/CM/DP representative and its semilinear second-digit bridge. The present exact WZ observer does **not** solve it. Do not permanently constrain future canonical dispatch to this WZ topic; the next arithmetic unit, when authorized, would involve fourth old-edge and third genuine-tail derivatives or a different lawful source-assigned frontier.
