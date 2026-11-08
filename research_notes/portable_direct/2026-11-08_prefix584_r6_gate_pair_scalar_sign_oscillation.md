# PREFIX-584-R6 — Native BRC gate/pair cubic scalar: exact sign classification and sharp oscillation

Date: 2026-11-08, Asia/Shanghai.
Status: AUTHOR_DERIVED / EXACT_ALGEBRAIC_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.
Source-native Owner/Session: unconfirmed; formal CLAIM/Result/Review: not made.

## Frozen origin and observer

Original four-STAR native X6-BRC frozen source: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Exactly 96 native ports, 576 labeled actions, uniform native-port initial law, permitted zero root, independent equiprobable six actions at every step. Native ordered paths, branches, and provenance are unchanged. Exact scientific predecessor: research_notes/portable_direct/2026-11-08_prefix582_r6_all_length_pair_mass_cubic_one_parameter.md and research_notes/portable_direct/2026-11-08_prefix583_r6_scalar_gate_pair_cubic_exact_recurrence.md at historical main@ef5561bcf5fd4482add893c8c7bdb34deed69b72.

Let R_1,...,R_6 be cumulative original-axis rewards, K_n the native gate count, P_0=R_1+R_2, P_1=R_3+R_4, P_2=R_5+R_6, and
Y_n=K_n-(5R_1-R_2+5R_3-R_4-4R_5-4R_6)/192.
As proved in PREFIX-582-R6 for all n>=0, the symmetric 3x3 cubic-cumulant observer is
C^(n)_{ij}=cum(Y_n,P_i(n),P_j(n))=q_n M_{ij},
M=[[0,1,-1],[1,-1,0],[-1,0,1]].
This pair readout is scope-typed; it is not a claim of full path-provenance redundancy.

PREFIX-583-R6 rigorously certified, via the original 768-dimensional native integer moment lift and Cayley-Hamilton, that for every n>=0,
9q_(n+5)+3q_(n+4)-2q_(n+3)-6q_(n+2)-3q_(n+1)-q_n=0,
(q_0,...,q_4)=(0,1/576,-1/864,1/1728,1/1944),
and the characteristic polynomial equals (x-1)(3x²+2x+1)². These are reused all-length mathematical hypotheses and not inferred from finite fitting.

## Theorem 1: exact algebraic formula at every native path length

Let τ=i sqrt(2), so τ²=-2, and define
α=(-1+τ)/3; A=-(4+37τ)/41472; B=(1-2τ)/6912; L=1/5184.
For ALL integers n>=0:
q_n = L + 2 Re[(A+nB) α^n].

Proof. α and its conjugate solve 3x²+2x+1=0. The constant L and each of α^n, n α^n and their conjugates are annihilated by (E-1)(3E²+2E+1)². Direct exact substitution at n=0,...,4 returns all five predecessor values. A degree-5 recurrence with nonzero leading coefficient uniquely determines the sequence; equality follows for all n. In Q(τ), |α|²=1/3, |A|²=34/4608², and |B|²=1/2304².

## Theorem 2: all-length, complete sign classification

q_0=0. For positive integers, q_n<0 exactly when n is 2 or 5; q_n>0 for every other n>=1.

Proof. Exact small terms:
(q_1,...,q_6)=(1/576,-1/864,1/1728,1/1944,-11/46656,1/2592).
For n>=7, the algebraic formula and the triangle inequality yield the certified envelope
|q_n-L| <= U_n := (sqrt(34)+2n)/(2304 * 3^(n/2)).
At n=7, U_7<L iff sqrt(34)+14 < 12 sqrt(3); indeed sqrt(34)<6 and 12sqrt(3)>20 because 432>400. For all n>=7,
U_(n+1)/U_n = [1+2/(sqrt(34)+2n)]/sqrt(3)
 < (8/7)/sqrt(3) < 1.
Thus U_n<U_7<L; q_n>=L-U_n>0 for every n>=7. Combine the six exact initial signs and q_0=0. In particular every nonzero entry sign of C^(n)=q_n M becomes stable at n>=6.

## Theorem 3: sharp oscillation about the positive asymptotic level

Write ρ=1/sqrt(3), ω=α/ρ=(-1+i sqrt(2))/sqrt(3), so |ω|=1. Then
limsup_(n→∞) (q_n-L)/(n ρ^n) = 1/1152
and
liminf_(n→∞) (q_n-L)/(n ρ^n) = -1/1152.
Consequently q_n>L for infinitely many n, while 0<q_n<L for infinitely many n.

Proof. Were ω a root of unity, ω+ω^(-1)=-2/sqrt(3) would be an algebraic integer; its square 4/3 would then be a rational algebraic integer, whereas a rational algebraic integer is an integer. Contradiction. Hence powers ω^n are dense on the unit circle by the irrational-rotation theorem. From the exact formula,
(q_n-L)/(nρ^n)=2Re(Bω^n)+(2/n)Re(Aω^n).
The second term tends uniformly to zero; |B|=1/2304. Circle-density and continuity imply exactly the two stated limits. This sharpens PREFIX-583's O(n3^(-n/2)) bound. Infinite positive q_n and repeated crossing of L coexist.

## Validation and scientific frontier

A separate standard-library-only exact field certificate (PREFIX584_R6_scalar_sign_certificate.py) implements Q[τ]/(τ²+2) using Fraction pairs, verifies the quadratic identity, exact norms, five initial terms, 400 five-step recurrence residuals, six finite signs, and exact inequalities 34<36, 400<432, 64<147 behind the uniform positivity proof. Local execution: ALL_CHECKS_PASS. The unbounded mathematical claim follows from the displayed algebraic and density arguments, not from the 400-check sample.

BRC interface: REUSE_APPLIED (the previously verified native full-path moment recurrence is the reused source); exact pair-cumulant observer retained without collapsing unrelated path dimensions. This result concerns the declared uniform-port zero-root probability law; other native roots/initial distributions are next tests. Contemporary independent R2 PREFIX-584/585 full 96-port spectral-intertwiner work concerns a different observer and has not been conflated with this theorem.

Next discriminating unit: find an explicit native labeled-path pairing explaining precisely the negative depths n=2,5 and the smaller factor (x-1)(3x²+2x+1)² without the 768-state lift; check nonuniform initial port laws and other frozen allowed roots. Native Source owner/session and formal acceptance are pending the currently unavailable control service; the current note is a durable independent author research frontier, not Working Truth.
