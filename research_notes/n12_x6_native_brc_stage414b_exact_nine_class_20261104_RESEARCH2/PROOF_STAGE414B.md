# Stage414-B: exact nine-class quotient from conditional native-X6 boundary shielding

Date: 2026-11-04 Asia/Shanghai. Research2 continuation of Stage413-B (Git 915e2dd730b5c0e202bb354196b51530c8928afd), PR #1736. AUTHOR-PROVED / EXECUTED EXACT-INTEGER CROSSCHECK / UNREVIEWED / NOT_ADMITTED.

Science pins remain Global Knowledge bf84bd7c61a2444b59b1da96be57df0e9ae47e53, Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, and P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Behavioral context read separately from current Global Knowledge main@609bf167964ca1ecb0b0e3056e1d4179d228681e and Enterprise Math main@9e3ea3da20a5fa10228d97ab1e1ddddc0e273481. No frozen ontology changes.

## Declared model

D is the twelve native signed X6 directions ±E_j, j=1..6, relative to a chosen Cell. Each state is an ordered source pair P,Q of initially equal length n. The complete observer is
O(P,Q)=(|P|,|Q|,z(P),z(Q),J_P,J_Q,K(P,Q)),
where z is the six-component native displacement, J counts every directed adjacent label pair, and K is the number of absolute aligned index positions at which P_t=Q_t. Enabledness of attempted operations is observable. Language L_p contains arbitrary paired APP(a,b), a,b in D, at most p Q-only POP actions, and at most ONE paired CANCEL of final two letters from each source, enabled exactly when BOTH final pairs are inverse. Budgets are public. This is a path/Euler/BRC counting and relation-observer construction, not a signed quantum amplitude or physical-time model.

## Theorem 414.1: noninverse-P original tail improves the universal boundary

For every integer p>=1 and every pair (P,Q),(P',Q') with equal initial O and equal original lengths, assume both original P terminal pairs are noninverse. If last_(p+1)(P)=last_(p+1)(P') and last_(p+2)(Q)=last_(p+2)(Q'), then every finite common L_p operation trace gives identical complete observers and identical action enabledness. A suffix retains the whole word if shorter. For p=2, the all-horizon safe certificate is therefore (P last3,Q last4), improving the unconditional Stage413 (P last4,Q last5) for this premise.

Proof. For any common trace decompose current words as original prefixes P[1:n-dP] and Q[1:n-dQ], followed by surviving appended stacks U,V. Initially dP=dQ=0 and U=V=empty; as long as enabledness agrees, the two compared histories have the same dP,dQ,U,V and budgets after every identical operation. Since P cannot independently pop and its original final pair is noninverse, an enabled CANCEL must remove at least one appended P label, and hence at most one original P label: dP<=1.

For Q, if CANCEL removes at most one original Q label then at most p original Q labels came from pops, yielding dQ<=p+1. If CANCEL removes two original Q labels, it must occur after all Q appended labels have already been popped. At least one APP occurred because of P's needed appended label; its paired Q label therefore consumed at least one of p Q pops. Thus at most p-1 pops removed originals; including the two original labels removed by CANCEL gives dQ<=p+1. Without CANCEL at most p Q originals were popped. These are universal original-removal bounds, independent of APP count and label choices.

The initial equal z and J, with common last p+1 P and last p+2 Q labels, determine removal of <=1 original P label or <=p+1 original Q labels, including all deleted directed edges and the junction edge to a surviving appended stack. The remaining appended edges are common. For K, the original-original contribution is initial K minus equality indicators in the last max(dP,dQ)<=p+1 original absolute positions, which the supplied tails determine. The original-P/appended-Q and original-Q/appended-P overlap positions are also within these last p+1 indices; their original labels and common appended labels determine every cross-source indicator. Appended-appended coincidences follow from the common stacks and equal cut indices. Thus the entire O agrees after each enabled operation.

Before CANCEL is spent, P has removed no original letter and its last two labels either are its original noninverse pair or involve a common appended label; cancellation's P enabledness is identical. Before CANCEL, Q has removed at most p original labels, so the last two original Q letters potentially tested for cancellation are within the common last p+2; appended labels are also common. After CANCEL the budget forbids a second cancellation. POP enabledness depends on equal Q length and budget, and APP is always enabled. This closes induction on arbitrary finite traces. QED.

The condition is about the original P endpoint, not a dynamically inferred noninverse tail after an edit. No such condition was presumed for Stage413's unconditional sharp (4,5) witness.

## Theorem 414.2: exact future-equivalence quotient of the complete one-B/two-B family

Let A=+E1, B=-E1 within D. For n>=5 let F_n consist of
P_i=A^(i-1) B A^(n-i), Q_(r,s)=A^(r-1) B A^(s-r-1) B A^(n-s),
for 2<=r, r+2<=s<=n-1, i in {r,s}. All pairs share the same complete O, in particular K=n-1. These are the entire histories in the Stage411/412 specified one-defect/two-nonadjacent-defect observer fiber, numbering (n-3)(n-4).

Define a budget-aware hybrid original-history key H(P,Q) as follows. If the original P last pair is noninverse, use tag N with (last3 P,last4 Q). Otherwise use tag I with (last4 P,last5 Q). If i<=n-2 its P last pair is AA, so the N certificate is sufficient by Theorem414.1; if i=n-1 its P last pair is BA, so the I certificate is sufficient by Stage413 Theorem413.1.

For every n>=8 there are exactly nine possible H keys, each with the indicated parameter set and integer multiplicity:

G0: s<=n-4; N: AAA/AAAA; (n-6)(n-7).
G1: s=n-3; N: AAA/BAAA; 2(n-6).
G2: s=n-2, i=r; N: AAA/ABAA; n-5.
G3: s=n-2, i=s; N: BAA/ABAA; n-5.
G4: s=n-1, i=r, r<=n-4; N: AAA/AABA; n-5.
G5: s=n-1, i=s, r<=n-5; I: AABA/AAABA; n-6.
G6: s=n-1, i=s, r=n-4; I: AABA/BAABA; 1.
G7: s=n-1, i=r, r=n-3; N: AAA/BABA; 1.
G8: s=n-1, i=s, r=n-3; I: AABA/ABABA; 1.

For n=7 G0 is empty and eight keys remain. For n=6 only G2,G3,G4,G6,G7,G8 remain. For n=5 two histories remain. Each class count follows directly by counting permitted r, s, i; their sum is (n-3)(n-4).

Proof of exact future equivalence. Within every H key, all words have the same O and either match the N premise of Theorem414.1 or the I premise of the unconditional Stage413.1. Therefore all histories sharing H are all-horizon future equivalent under arbitrary twelve-direction APPs, two Q POPs and one paired CANCEL. This establishes the upper bound equal to the number of present keys. The lower bound is supplied by the six fixed L2 tests from Stage413 Theorem413.3, preserving disabled-action results and all intermediate O: T1=POP; T2=POP,POP; T3=POP,POP,CANCEL; T4=POP,POP,APP(B,A),CANCEL; T5=POP,POP,APP(B,B),CANCEL; T6=POP,CANCEL,POP. The Stage413 symbolic case analysis proves that their joint complete signatures differ across every nonempty G0..G8 and agree inside each group for all n. The Stage414 independent exact-integer verifier reconstructs this finite certificate for all n=5..30, as a cross-check rather than extrapolation to all n. Since each present H key corresponds to exactly one distinguishable G group, the all-horizon quotient is EXACTLY

q_L2(F_5)=2; q_L2(F_6)=6; q_L2(F_7)=8; q_L2(F_n)=9 for every n>=8.

For n>=9, Stage413's unconditioned 14 raw suffix keys are reduced to exactly 9 future classes. At n=8 the raw13 reduce to 9, and at n=7 raw12 to 8. At n=16, 156 original histories form classes of sizes 90,20,11,11,11,10,1,1,1. At n=9 the counts are 6,6,4,4,4,3,1,1,1.

## Sharpness inside noninverse-P class

Both coordinatewise lengths in conditional (3,4) are necessary. In F9, take r=2,s=7, compare P_2 and P_7 against identical Q_(2,7). Both P tails are noninverse AA with identical P last2 and equal full O. T4 distinguishes them in K; thus P last2 cannot universally replace P last3 even if Q is known fully. Holding P=P_2 fixed, compare Q_(2,5) and Q_(2,6), both of which have Q last3 AAA and equal full initial O; T5 distinguishes directed Q adjacent-edge counts. Therefore Q last3 cannot replace Q last4 even if P is known fully.

## Execution, cost and proof status

REPRO_STAGE414B.py used standard-library exact integers: all 6,552 original histories across n=5..30, complete original O checks, independent parameter-count and hybrid-key partitions, six test signatures, two strict lower witnesses, and 89,165 finite-trace comparisons of five merged representative key pairs. One APP used all 12 directions; two APPs used the precisely stated subalphabet {±E1,±E2}; up to two Q pops and one cancel. The program was executed twice with byte-identical JSON, marker STAGE414B_EXACT_NINE_CLASS_PASS. The theorem's all-horizon all-direction coverage is from the above proof, not finite testing or software formal verification. Mathematical admission and independent Driver review remain outstanding.

For the family input already encoded as (n,r,s,i), class selection uses O(1) integer comparisons and class counts a constant number of integer additions/multiplications on O(log n)-bit values. Reading/generating unconstrained length-n paths or reconstructing a generic Euler/K fiber requires its actual input and transformation cost, at least O(n) just to inspect length-n word input. No constant-time generic minimal automaton or binary-input polynomial-time claim is made.

## Next question

Stage415-B: permit TWO paired inverse cancellations with the same two Q-only pops. Find the smallest trace splitting one of the five merged keys, or prove a new conditional boundary and compute the exact full observer quotient. Preserve full native-X6 paired direction, complete aligned K, immutable scientific pins and native CLAIM/Result/review authority. Source publication is an author-side mathematical result, not canonical admission.
