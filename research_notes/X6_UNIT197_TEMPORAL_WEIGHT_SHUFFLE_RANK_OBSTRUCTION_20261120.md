# X6 Unit197 — Exact temporal sign-shuffle bridge and the first rank-two source obstruction

Status: **AUTHOR_PROVED / EXACT_INTEGER_FINITE_EXECUTED / SOURCE_PIN_ALIGNED / UNREVIEWED / NOT_ADMITTED**.
Mother objective: \`PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905\`; task \`RS-X6-LEGACY-PLANE-RECONCILIATION\`; publication \`TP2-B4A441B23DA3159232C2\`.
Author research lane: \`chatgpt-research-onhour-enterprise-math-20260923\` (historical lane reference only, not a newly authenticated native claim).
Frozen scientific pin: \`59538f585d037d09ef687b28715c4bc1a3f9fe03\`. Frozen comparison: \`fd2bcff10ca6e147348b6c1236027fc0d2877df3\`.
Existing source interface: \`experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py::endpoint_weight\` at frozen blob \`300a96e3dc24bf6fff73743037a0347a8bc83176\`; the producer uses fixed per-axis positive/negative weights. The **time-dependent extension below is a mathematical model extension**, not a claim that the pinned producer already takes time arrays. Unit196 is reused at its exact scope.

## 1. Exact time-slot result

In P000 native signed six-coordinate displacement chart \(\mathbb Z^6\), let a path of exactly \(2n\) primitive events have one separately typed event time \(t=1,\ldots,2n\). Let \(u_i,v_i\in\mathbb Q_{>0}\) be fixed axis/sign weights and \(a_t,b_t\in\mathbb Q_{>0}\) be time-slot multipliers. An event \(+e_i\) at slot \(t\) has weight \(a_tu_i\); an event \(-e_j\) there has weight \(b_tv_j\). Products retain the order-dependent slot assignment; the observer below aggregates endpoint weights only.

For balanced endpoint \(z\in\mathbb Z^6\), \(\sum_i z_i=0\), let \(E^{\mathrm{time}}_{2n}(z)\) be the exact sum over all signed native words of length \(2n\) ending at \(z\). Let \(L_n^{u,v}(z)\) be the **labeled** lazy A5 paired-word weight with 36 possible letters \((i,j)\), each of weight \(u_iv_j\), including six distinct zero-displacement pairs. Define
\[
H_n(a,b)=\sum_{\substack{S\subseteq\{1,\dots,2n\}\\|S|=n}}
 \prod_{t\in S} a_t\prod_{t\notin S} b_t,\qquad H_0=1.
\]
Then for every \(n\geq0\), every balanced \(z\), and all positive rational inputs,
\[
\boxed{E^{\mathrm{time}}_{2n}(z)=H_n(a,b)\,L_n^{u,v}(z).}
\]
In particular, if \(E^{\mathrm{static}}_{2n}(z)\) is the pinned fixed-axis-weight value, Unit196 gives
\[
\boxed{\binom{2n}{n}E^{\mathrm{time}}_{2n}(z)=H_n(a,b)E^{\mathrm{static}}_{2n}(z).}
\]

**Proof.** A balanced endpoint after \(2n\) unit signed-axis steps forces exactly \(n\) positive and \(n\) negative events because their total coordinate sum is zero. Fix their separately ordered positive labels \(i_1,\ldots,i_n\) and negative labels \(j_1,\ldots,j_n\). Choose the set \(S\) of the \(n\) positive time slots. The path weight factors as
\[
\bigl(\prod_{r=1}^n u_{i_r}v_{j_r}\bigr)
\bigl(\prod_{t\in S}a_t\prod_{t\notin S}b_t\bigr).
\]
Pair the \(r\)-th positive and \(r\)-th negative label into an ordered lazy letter; retain \(S\) separately. This is a bijection including \(i_r=j_r\), and summing over \(S\) yields \(H_n\). The empty word satisfies both sides for \(n=0\). This is an exact BRC provenance-preserving derivation; projecting away \(S\) is valid only for the declared endpoint-weight observer.

Let \(c=\sum_i u_iv_i\). If \(\widetilde E_{2k}=E^{\mathrm{time}}_{2k}/H_k\) uses the corresponding \(2k\)-slot profile, Unit196's labeled-zero-pair inversion gives
\[
\boxed{A_n^{u,v}(z)=\sum_{k=0}^n\binom nk(-c)^{n-k}\widetilde E_{2k}(z),}
\]
where \(A_n\) has only the 30 nonzero A5 root letters. Positivity ensures all \(H_k>0\).

## 2. Precisely when two time slots generate a rank-two obstruction

For **arbitrary** slot-dependent positive axis vectors \(u^{(1)},u^{(2)},v^{(1)},v^{(2)}\) (not presumed proportional), the two-event balanced readout has the labeled pair matrix
\[
M_{ij}=u^{(1)}_i v^{(2)}_j+u^{(2)}_i v^{(1)}_j.
\]
As a \(6\times6\) rational matrix, \(\operatorname{rank}M\le 2\). Moreover,
\[
\boxed{\operatorname{rank}M=1\iff
u^{(1)}\parallel u^{(2)}\ \text{or}\ v^{(1)}\parallel v^{(2)}.}
\]
The equivalence follows from the exact minor factorization
\[
M_{ij}M_{k\ell}-M_{i\ell}M_{kj}
=(u^{(1)}_iu^{(2)}_k-u^{(2)}_iu^{(1)}_k)
(v^{(2)}_jv^{(1)}_\ell-v^{(1)}_jv^{(2)}_\ell).
\]
All vectors here are strictly positive, so a zero minor for every pair enforces proportionality of one of the two vector pairs, and either proportionality makes \(M\) rank one.

Concrete all-positive integer counterexample, indices \(1,\ldots,6\):
\[
u^{(1)}=(1,2,1,1,1,1),\quad u^{(2)}=(2,1,1,1,1,1),
\]
\[
v^{(1)}=(1,1,1,1,1,1),\quad v^{(2)}=(1,1,1,2,1,1).
\]
For the four **off-diagonal endpoints** \(e_1-e_3,e_1-e_4,e_2-e_3,e_2-e_4\), their observed two-event masses form
\[
\begin{pmatrix}3&4\\3&5\end{pmatrix},\qquad \det=3.
\]
Therefore even these four endpoint masses cannot be explained by **one** fixed-axis factorized pair profile times any common shuffle scalar. For \(e_1-e_3\), the two distinct native event orders contribute \(1\) and \(2\), respectively; the endpoint mass \(3\) has hidden the actual event-time source.

The rank-one iff above is a statement about the **complete labeled-pair matrix**. Its off-diagonal counterexample is sufficient to disprove the proposed endpoint-level rank-one collapse; it makes no assertion about arbitrary abstract quotient observers.

## 3. Exact execution certificate

An independent Python integer dynamic program executed the full twelve-direction time-dependent recursion. For each of two static axis-weight profiles (unit and six nonuniform positive integers), the time multipliers were \(a=(2,3,5,7,11,13)\), \(b=(17,19,23,29,31,37)\), truncated to the first \(2n\) slots. For each \(n=0,1,2,3\), all balanced attainable endpoints were checked against the independent factorial/weak-composition formula corresponding to pinned \`endpoint_weight\`. There were **3,168 distinct profile/length/endpoint comparisons** (one profile contributes \(1+31+271+1281=1584\)), all exact integers, with **zero violations**. The sign-subset coefficients were \(H_0=1\), \(H_1=89\), \(H_2=42,541\), \(H_3=62,759,750\). The rank-two four-endpoint counterexample was independently checked against two-step native dynamic recurrence, yielding determinant \(3\). A reproducible script and JSON result are separate source artifacts.

The frozen producer was **not re-imported in this unit**; the source-aligned factorial formula was independently implemented. This extends Unit196; the R063 six-file native benchmark was not rerun.

## 4. Source/observer boundary and next executable action

The new result isolates the missing type of temporal provenance: a **sign-slot subset** \(S\) suffices for exact native-word reconstruction from positive/negative ordered labels, while the endpoint-weight scalar \(H_n\) suffices for the precisely declared factorized time-slot family. Nonfactorized temporal axis profiles can require a matrix-valued/multi-rank carrier; the rank-two witness prohibits reducing the corresponding four endpoint masses to one scalar product.

The named pinned producer uses time-independent axis weights. The verified historical \`check_signed_brc.py\`, \`check_x6_signed.py\` and \`tests/test_p022_geodesic_multiplicity.py\` are standalone validation consumers, without a direct cross-call between shortest A5 and all-walk signed X6 in those exact files. Original LP011/LP019 offending \`commit:path:line\` remains unlocated; a bounded negative search does not establish global absence.

Next useful research action: locate the actual frozen state/time-sensitive consumer, if any, or inspect existing real temporal carrier interfaces; compare its precise ordered-data demand with the sign-slot/repaired matrix witness. Retain latest Native authenticated frontier Unit174, pending semantic association Units175–197, historical Units149–152 and original read/failed-prepare receipts. Native execution authorization and independent Driver review remain separate from this author proof and exact test.
