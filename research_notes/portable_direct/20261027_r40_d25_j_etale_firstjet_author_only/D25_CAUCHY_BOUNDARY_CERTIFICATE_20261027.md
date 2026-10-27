# D25 — finite Cauchy cutoff boundary and coefficientwise p-adic certificate

2026-10-27. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT-ADMITTED / REGISTER-PENDING. Portable mathematical evidence only. Same shared D25 context as this Draft PR, not independent review and not native H0/B0 execution. Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3, Taskbook blob 53a3ef039325534e3715add837f0eee332289984.

### Exact all-N boundary theorem
Inherited earlier finite identity (not a new result here):
$$S_N=\sum_{j+k<N}(3j+3k-1)u_jc_k,$$
with $u_j=\binom{2j}{j}/8^j$ and $c_k=(3k)!(2k)!/[216^k(k!)^5]$.
Set $U_r=\sum_{j<r}u_j$ and $W_N=\sum_{k<N}(6k+1)c_k$.
For every integer $N\ge1$ the following rational identities hold:
$$\boxed{S_N=\frac12\sum_{k<N}c_k[(6k+1)U_{N-k}-3(2(N-k)-1)u_{N-k-1}].}\quad(A)$$
$$\boxed{S_N-W_N=\frac12\sum_{k<N}c_k[(6k+1)(U_{N-k}-2)-3(2(N-k)-1)u_{N-k-1}].}\quad(B)$$
Proof: from $4(j+1)u_{j+1}=(2j+1)u_j$ and $V_r=\sum_{j<r}ju_j$, summation yields $4(V_r+ru_r)=2V_r+U_r$, hence $V_r=U_r/2-2ru_r$. Also $ru_r=(2r-1)u_{r-1}/4$. Substitute in the inherited finite rearrangement $S_N=\sum_{k<N}c_k[(3k-1)U_{N-k}+3V_{N-k}]$ to derive (A), then subtract $W_N$ to get (B). No infinite series interchange, conjecture, or division by $N$. The boundary term is mathematically essential, and no $u_p$ evaluation by division by $p$ is needed.

### Exact all-prime third-digit support
For every prime $p\ge5$ and $0\le k<p$,
$$\boxed{v_p(c_k)=\lfloor3k/p\rfloor+\lfloor2k/p\rfloor.}\quad(C)$$
Indeed $p$ is a unit in the coefficient denominators and $3k<3p\le p^2$; Legendre's factorial formula has only the first floor term. Valuations across $[0,p/3),[p/3,p/2),[p/2,2p/3),[2p/3,p)$ are 0,1,2,3 respectively. Since all $u_j,U_r$ and $1/2$ are $p$-integral, deleting every $k\ge T_p=\lceil2p/3\rceil$ term in (A),(B), and $W_p$ **preserves the exact residue mod $p^3$**. The cutoff is coefficientwise sharp: the preceding band has valuation exactly 2 and cannot be discarded on valuation grounds alone. This safe compression is relative to the specified observer $p^3$, not higher precision.

### Actual author-side exact checks
Companion standard-library executable compares direct rational triangular sums for $N=1,...,13$, verifies full versus valuation-truncated formulas for p=13,19,37,43,211,373,997,1213, and independently compares triangular convolution for p<=373. All pass. The rows (p, retained k-count, W mod p^3, S mod p^3, (S-W)/p² mod p) are:
(13,9,13,13,0); (19,13,19,3268,9); (37,25,37,15096,11); (43,29,43,40721,22); (211,141,211,7657823,172); (373,249,373,8487242,61); (997,665,997,487065407,490); (1213,809,1213,191279183,130).

Finite samples do not prove universal $p^2$-divisibility of $S_p-W_p$, nor original $W_p\equiv p$ mod $p^3$. This theorem only removes the auxiliary Cauchy moment V and p³-invisible coefficient tail with exact provenance retention. In BRC language the carrier is the signed triangular $(j,k)$ source; the certified future readout is the p³ residual; the boundary $u_{r-1}$ is non-erased provenance. The auxiliary model has no proved transfer to P000 native X6/3D slice.

Native same-original-class p=373 H0/B0, semilinear Frobenius and odd Green/Hesse evidence remain pending at Issue #1559. Original UR V2 four-file 94687-byte bundle must independently match SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76; no original recovered here. Source continuation in this execution returned CONTROL_QUOTA; own checkpoint reading ACCESS_DENIED; Sites remains read-only. No winning CLAIM, OPEN or authorized Source checkpoint was established. All current portable files are staged author evidence, not predecessor completed_units; a CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS seed requires completed_units=[] and full readback of seed inputs before typed succession.

Next scientific unit: prove/disprove all-target p² divisibility of this exact boundary residual, obtain a justified closed third-digit correction, or establish the authentic H0/B0-to-original-LIFT transfer. No math acceptance is claimed.
