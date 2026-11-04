# PREFIX-493 — Complete BRC–KMP source-mask transfer and append-closed observer

Date: 2026-11-04 (Asia/Shanghai). Stage: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.
Scientific input (frozen): awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Predecessors: PREFIX-490 (q=0 masks), PREFIX-491 (suffix polygon shift), PREFIX-492 (q=1,2 total and source distinction). The applicable global/project rules are read independently at their current canonical snapshots.

## Model and problem

Use P000 Heartbeat World native six signed spatial axes and separately typed event order. In the declared restricted observer the sixth special axis has zero occurrences. Ordinary native directions are a/A, b/B, c/C, d/D, e/E. Every ordered word is admitted; gate g in {aab,aba} is used only for terminal KMP state, including q=3 for a full terminal match. At each ordinary axis let u_i and v_i be its positive/negative counts, y_i=u_i-v_i and p_i=min(u_i,v_i). The BRC additive cancellation observer is V=p_b+2p_d+p_e and W=p_c+p_e. Length n=sum_i(u_i+v_i). First-source tag N means no b/B/c/C encountered; B means b/B appeared first; C means c/C appeared first. A fiber is (n,y_a,...,y_e,V,W,q); its **source mask** is the set of tags attainable among all ordered paths in that fiber. Count distinct fibers once, not ordered path multiplicities. P000 native ordered steps, branches, and provenance remain the precursor; this paper studies the stated Boolean readout and signed-count updates, not phase/amplitude or physics.

## Theorem 1 — Rational source-mask basis for the unrestricted prefix

Set D=1-z. For a prefix of arbitrary ordered symbols, without fixing its KMP terminal state, let G_M(z) count fibers (n,y,V,W) having exact source-support mask M in {N,B,C,NB,NC,BC,NBC}. Then:

G_N   = (1+z)(1+z²-z⁴)/D⁵;
G_B   = z²(1+z)/D⁵ + 2z(1+z)(1+2z²)/D⁶;
G_C   = z²(1+z)(1+z²)/D⁵ + 2z(1+z)(1+2z²)/D⁶;
G_NB  = z⁴(1+z)/D⁵;
G_NC  = 0;
G_BC  = z⁴(1+z²)/D⁶ + 4z³(1+2z²)/D⁷ + 4z²(1+2z²)/D⁸;
G_NBC = z⁴/D⁶.

Their sum is H(z)=(1+z)²(1+2z²)/D⁸. The formulas apply for all n>=0.

Proof. For fixed y and m=(n-sum|y_i|)/2, the image of nonnegative cancellation counts under (V,W) is the saturated integer polygon P_m={(V,W):0<=W<=m, 0<=V<=2m-W}, proved constructively in PREFIX-488/491. At any occupancy, the attainable first-source tags are N if b,c populations both vanish, B if only b occurs, C if only c occurs, and {B,C} if both occur. Taking the union over p-vectors in a polygon fiber yields the three predicates N0, B0 and C0 from PREFIX-490, with displacement flags y_b!=0 and y_c!=0. The signed-displacement series for each freely varying axis is (1+z)/D, and each cancellation pair adds z². These fixed-m polygon counts give exactly the seven formulas above. Equivalently, they are the seven q=0 formulas in PREFIX-490 with the finite suffix exclusions restored: pure a^n (n>=1) contributes z/D to G_N; all-lowercase a^k b with k>=2 for aab or k>=1 for aba contributes E_g to G_B. Summation gives H(z).

## Theorem 2 — Full terminal-state source masks, all lengths

Define the mask transfer Φ_B on the seven-basis vector: a prefix's possible N or B becomes B after appending a fixed suffix containing b/B before any c/C, while a possible C remains C. On exact masks, Φ_B maps N,B,NB to B; C to C; BC,NBC to BC; NC would map to BC (and G_NC=0). Let L(z)=Φ_B(G(z)); its only nonzero components are

L_B=G_N+G_B+G_NB,  L_C=G_C,  L_BC=G_BC+G_NBC.

For each gate g, let Q_{g,q,M}(z) count fibers (n,y,V,W,q_g=q) with exact source mask M. Every Q is determined by the following identities, interpreted componentwise:

  q=0: Q_{aab,0}=G - (z/D)e_N - (z³/D)e_B;
       Q_{aba,0}=G - (z/D)e_N - (z²/D)e_B.
  q=1: Q_{aab,1}=zG - (z²/D)e_N;
       Q_{aba,1}=zG.
  q=2: Q_{aab,2}=z²G;
       Q_{aba,2}=z²L.
  q=3: Q_{aab,3}=Q_{aba,3}=z³L.

Here e_N and e_B are unit vectors in the corresponding exact-mask components.

Proof. The q=0 identities are the complete source-mask classification of PREFIX-490, whose exceptions come from the inability of the purely lowercase a^n and a^k b families to end in KMP 0. The q=1 identities are the pointwise source-mask equivalence of PREFIX-492: suffix a is attainable with exactly the unrestricted prefix mask, except the all-a family for aab. For q=2, the exact terminal suffix is aa in aab and ab in aba; neither can terminate in q=3. For q=3 the exact terminal suffix is aab or aba. For any fixed suffix h with signed letter-counts h_i^+,h_i^-, fixed total displacement y, define α_i=max(0,h_i^+-max(y_i,0),h_i^--max(-y_i,0)). Every occupancy admitting h has p_i=α_i+p'_i with p'_i>=0. The prefix displacement is y'_i=y_i-(h_i^+-h_i^-); the BRC pair (V,W) is translated by the constant linear image of α, and residual occupancies are in bijection with the complete nonnegative p' vectors at that y'. Thus fixed-suffix fibers are in an exact one-to-one correspondence with unrestricted prefix fibers of length n-|h|, preserving the whole set of prefix source tags. Appending suffix aa leaves the tag unchanged. Appending ab, aab or aba applies Φ_B, because their earliest b/c source is b. This proves the q=2,3 identities for every n.

## Corollary — Total KMP fiber generating functions

Sum all source-mask components and all q states. With H as above:

 T_aab(z)=(1+z+z²+z³)H(z)-(z+z²+z³)/D;
 T_aba(z)=(1+z+z²+z³)H(z)-(z+z²)/D;
 T_aba(z)-T_aab(z)=z³/D.

The gates have equal total fibers for n=0,1,2; for each n>=3, aba has exactly one more full-KMP observer fiber. At n=8 the totals are 39,886 (aab) and 39,887 (aba). The q=2 aab fibers admitting N have generating function z²/D⁶, whereas q=2 aba has no N-admitting fiber. This is a complete all-length classification for the declared observer and both gates.

## Theorem 3 — Exact one-step BRC closure and minimal finite control memory

For the permitted future operation 'append one signed primitive letter' and outputs (n,y,V,W,q,first-source tag), the observer state itself is a sufficient exact online state. Let c=(0,1,0,2,1), d=(0,0,1,0,1), and append sign ε in {+1,-1} at axis i. Define δ=1 exactly when ε y_i<0, using y_i before the append. Then

 n'=n+1,    y'_i=y_i+ε,    V'=V+c_i δ,    W'=W+d_i δ,

with unchanged other y coordinates. Independently update q by the standard KMP transition and update the first-source tag from N to B/C at the first corresponding symbol. Proof: if ε y_i<0, adding the opposite letter increases min(u_i,v_i) by one; otherwise the minimum is unchanged. The equations therefore commute exactly with the raw signed-occupancy update for any path length. Inducting over future primitive appends proves observer preservation for arbitrary finite append sequences.

The reachable (q,tag) Moore states number 11 for aab (N permits q=0,1,2; B and C each permit q=0,1,2,3), and 10 for aba (N permits q=0,1; B and C each permit q=0,1,2,3). Witnesses for aab are N:{empty,a,aa}, B:{b,ba,baa,aab}, C:{c,ca,caa,caab}; for aba they are N:{empty,a}, B:{b,ba,ab,aba}, C:{c,ca,cab,caba}. Each has a distinct current readout (q,tag), so these state counts are minimal for a machine required to return both readouts at the current step. They fit in four bits. The unbounded integer fields are n, five y_i, V and W.

For the stronger output requesting every per-axis p_i, the two sparse integer repair coordinates established in PREFIX-485 supply exact reconstruction. The present append-closed BRC observer requires zero such additional integer coordinates. This identifies two distinct, fully specified lossless observer contracts.

## Executed finite certificate and evidence

The submitted JavaScript certificate computes the exact coefficients of all seven G rational functions, transforms the predicted masks into q=0,1,2,3 for both gates, and independently enumerates every reachable raw ten-direction occupancy with its KMP and first-source states for n=0..8. For every n, q and mask it checks exact equality. Every next raw single-letter transition additionally checks the displayed BRC append formula against recomputation from the new raw counts. The same test compares total gate differences. Actual execution output ends ALL_CHECKS_PASS. Finite coverage and full-domain analytic proof are separate evidence. No physical time calibration, native phase calculation or independent review is claimed.

## Next PREFIX-494

Study the finite-state minimization when the *reported* source query is Boolean or horizon-limited, rather than the complete first-source tag. Derive the minimal future-equivalence quotient of the 11/10-state joint KMP/source machine, with exact witness words for separated states and a finite automaton certificate. Then include the resulting bit-cost and BRC integer-field bit complexity for bounded path length n, without changing the observer contract or P000.
