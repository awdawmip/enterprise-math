# R627｜signed BRC 多来源加性叠加：共同背景消去与轴相关背景的精确阈值

Date: 2026-11-08. Status: AUTHOR_SIDE_EXACT_PROOF / UNREVIEWED / NOT_ADMITTED.
Parent: R626@b05b5755ccd152a8b03802980856824f0dd76a9c; frozen scientific input R462@18783e01e3646c72b7aab3b16d3f565e83e6446f (θ=0); signed-K source blob 7fa7a762f758b30c6090468ac43487daa34abad8.

## 1. Exact mathematical model

Set P_j(t)=K_(2j−1)(t)∈Z[t], 1≤j≤6. Frozen kernels give ν_t(P_j)=e_j=2(j−1), with signed first coefficients c_j=(2,−8,6,106,83,9). Let ρ_d be reduction mod t^(d+1), with ν_t(0)=∞. An unknown orientation π∈S₆ assigns basic label π⁻¹(x) to independently addressable six-axis output x. The common nonzero unknown gain A∈Z[[t]] has r=ν_t(A)≥0. Identifiability asks whether equal observed six-axis d-jets of two parameter explanations, whose nuisance series may differ, forces equal π.

Addition in this model is signed formal-series addition, not a positive-mass operation. The actual source history, branch-grade, multiplicity and native X6 joint-state remain separately typed; the two theorems concern this explicitly declared coefficient-only observer.

## 2. Theorem A — arbitrary common additive background

**Theorem.** If Y_x=A P_(π⁻¹(x))+H with one arbitrary unknown H∈Z[[t]] shared across all six axes, then for every fixed r, the orientation is uniformly recoverable from the six d-jets **if and only if d≥r+8**. Even if r is not supplied, it can be determined from the data when this depth condition holds.

**Proof.** For distinct basic indices i<j the orders e_i<e_j imply ν_t(P_i−P_j)=e_i. As H cancels, for x≠y:

ν_t(Y_x−Y_y)=r+2 min(π⁻¹(x)−1,π⁻¹(y)−1).

At d≥r+8 all 15 pairwise differences remain nonzero modulo t^(d+1), and their minimal order is r. Among the six axes, basic j=1 is the unique axis for which all five pairwise difference orders equal r. Remove it; basic j=2 becomes the unique axis for which all differences to the remaining four axes have order r+2. Repeat to identify basic j=3 and j=4. The unclassified pair has labels {5,6}.

For the identified x₁ and x₂, ρ_d(Y_(x₁)−Y_(x₂))=ρ_d(A(P₁−P₂)). The constant coefficient of P₁−P₂ is 2. It is a unit in Q[[t]], so exact rational-series division reconstructs the unique ρ_d A, and the input ensures this reconstruction has integer coefficients. For each remaining axis x, evaluate ρ_d(Y_x−Y_(x₁)+AP₁)=ρ_d(AP_(π⁻¹(x))). The j=5 case has nonzero first coefficient at order r+8, namely 83·[t^r]A; the j=6 case has valuation r+10, hence is zero at d=r+8. This separates the last pair and recovers π.

For d≤r+7, exchange just basic axes 5 and 6, keeping A,H fixed. The affected outputs differ first at order ν_t(A(P₅−P₆))=r+8 and therefore have identical six-axis d-jets. This is the sharp lower bound. QED.

## 3. Theorem B — independent additive histories

**Theorem.** Suppose Y_x=A P_(π⁻¹(x))+H_x, with the six unknown independent additive backgrounds satisfying ν_t(H_x)≥r+q, for a fixed integer q≥0. There exists a finite universal observation depth identifying every π **if and only if q≥9**. In that range the optimal depth is d_min=r+8. For 0≤q≤8, two different orientations can yield identical full infinite series, using only two genuine frozen positive-axis K branch terms per ambiguous output.

**Proof when q≥9.** For basic j=1,…,5 the respective nonzero leading orders r,r+2,r+4,r+6,r+8 are strictly smaller than r+9, so the independent backgrounds cannot change them. At d=r+8 exactly five axes exhibit these distinct leading orders and the sixth label is determined by exclusion. This construction works for all A and all allowed H_x. For d≤r+7 take H_x=0 and swap j=5,6 as before: identical d-jets. Thus the depth is optimal.

**Proof when q≤8.** Keep basic labels 1,…,4 fixed, and swap only 5 and 6 in two candidate orientations. For either of the last two spatial axes, require the same complete output A(P₅+P₆). In explanation I, an axis carrying P₅ has background AP₆, while an axis carrying P₆ has background AP₅. In explanation II swap basic assignments and correspondingly exchange the backgrounds. The two background valuations r+10 and r+8 both satisfy the lower bound r+q. All six complete output series agree exactly, although π differs. The two source multiplicities in the ambiguous sum are +1; the signed K polynomial coefficients retain their signs. QED.

## 4. Explicit frozen collision and verification

At A=1, the two signed frozen polynomial contributions are:

P₅=K₉=83t⁸+497t⁹+1239t¹⁰+1645t¹¹+1225t¹²+483t¹³+77t¹⁴−t¹⁵;

P₆=K₁₁=9t¹⁰+72t¹¹+252t¹²+504t¹³+630t¹⁴+504t¹⁵+252t¹⁶+72t¹⁷+9t¹⁸.

The common scalar packet P₅+P₆ has two distinct signal/background assignments, even when every coefficient is observed. Native branch-grade or selectable future-source operations can distinguish those explanations; the exact collision applies to the stated coefficient-only reading.

Reproduce with Python 3 standard library: python R627_VERIFY.py. The verifier reconstructs all twelve K via the frozen integer-binomial formula, works in exact Z[t] and Q[[t]]/(t^(d+1)), and enumerates 720 orientations. Executed checks: 11,520 common-background decodes (4 gains×4 backgrounds×720 orientations), 4 sharp finite-depth collisions, 2,880 high-order independent-background decodes, 36 full-series low-noise-floor collisions, and 4 source-term checks, for a total of 14,444 specific cases. Marker: R627_ADDITIVE_HISTORY_OBSERVABILITY_EXACT_PASS. Universal statements follow the proofs above; finite code verifies the frozen instances and decoder implementation.

## 5. Research continuation

Identify an actual registered native X6 joint-field operator whose input/output realizes a six-axis signed response. If additive background is shared, test exact difference/ratio reconstruction (Theorem A). If backgrounds are independent, seek and verify a grade/observer-specific q≥9 bound or preserve the provenance necessary to resolve the explicit q≤8 collision. The current Source definition of Heartbeat World records fixed_heartbeat_program=null. Neither the auxiliary series grade nor its formal update is declared a physical heartbeat time operation.

Native Researcher-ID/Owner/CLAIM and independent Driver admission are governed by Source. This result is author-side, unreviewed and unadmitted.
