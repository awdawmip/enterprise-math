# R669｜禁止连续重复闭路时，完整 D₃ 输运仍不足以决定合法未来

Date: 2026-11-09 (Asia/Shanghai). Task: RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW. Frozen science: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. Predecessors R667@06c496b74ae5027967f52b8f0119274e4be084b2 and R668@7346127d953d3bed2e53d65490dc4989055b65f8. Status: AUTHOR_SIDE_UNREVIEWED.

## Exact mathematical model

In the auxiliary V17 Johnson J(6,3) triad graph with base triad 012, take the legal three-edge closed blocks
A: 012→013→023→012 and B: 012→013→123→012.
Their slot-holonomy factors are distinct transpositions a=(0,2,1) and b=(2,1,0) in S₃. With r=(2,0,1), a=s, b=rs, ab=r²=r⁻¹, ba=r and r³=e.

Declare the following **additional schedule rule**: two consecutive *complete blocks* must have different labels. This defines a regular constrained language L_nr over {A,B}, with empty word allowed. This is a selected exact auxiliary model; the native V29 transfer-permission H and autonomous V27/V30 event scheduler have not yet been specified as this no-repeat rule. A terminal observer preserves (n_A,n_B, final active triad 012, final complete V17 slot frame h). We ask whether it suffices for deciding the legal next block.

## R669-A — exact legal language and terminal-holonomy spectrum

For all nonnegative integers m,n, let L_nr(m,n) consist of all no-repeat block words with exactly m copies of A and n copies of B.

1. If |m−n|>1, the set is empty.
2. If (m,n)=(0,0), it contains only the empty word.
3. If m=n+1, the only word is (AB)^n A. If n=m+1, the only word is (BA)^m B.
4. If m=n=q≥1, it contains exactly two words: (AB)^q and (BA)^q, whose respective complete terminal holonomies are r^(−q) and r^q. These are equal if and only if 3 divides q.

Consequently, for q≥1 the number of **distinct reachable holonomies** is 1 for q≡0 mod3 and 2 otherwise, even though there are always exactly two legal words. The result is periodic in q, and the observer's information requirement can depend non-monotonically on event counts.

Proof: A no-repeat word over a two-element alphabet must alternate, so it is determined by its first letter. Its counts are balanced, or its first letter is also its last with one extra copy. The count classification follows immediately. For balanced counts, the two words alternate in opposite orders. From ab=r⁻¹ and ba=r, their holonomies are respectively r⁻q and r^q, equal iff r^(2q)=e iff 3|q since r has exact order 3. All closed blocks return the active triad to 012. QED.

## R669-B — minimal hidden scheduler memory beyond complete holonomy

For every positive q divisible by 3, consider two permitted histories
\[
W_1=(AB)^q,\qquad W_2=(BA)^q.
\]
They have the same complete directed V17 triad-transition histogram (q traversals of the three directed edges in A and q traversals in B), the same block counts, active triad 012, and **the same entire terminal S₃ frame** h=e. However, W₁ ends in B and W₂ ends in A. Under the exact declared rule, appending A is legal only after W₁, and appending B is legal only after W₂. Thus the two histories have different sets of legal one-step futures despite identical retained terminal observer.

The shortest nonempty balanced collision in this class is q=3 (six blocks, eighteen V17 triad transitions). The required repair can be an extra last-block label \(\ell\in\{A,B,\bot\}\), where \(\bot\) denotes no preceding block. For nonempty histories with fixed q divisible by 3, one binary bit distinguishes the two possible legal next-block states, and one bit is necessary since both distinguishable classes exist.

Proof: First conclusion from R669-A. For the last-letter future test, the declared transition allows x precisely when x differs from the last label. Since both labels occur and give different permitted next sets, any state quotient predicting one-step language must distinguish them. Storing the last label is sufficient to update the schedule automaton; if N=0 retain \(\bot\) for initial-state semantics. Note that full frame h is still needed for the full frame observer, and the new bit is about *future language*, not another independent spatial axis. QED.

## R669-C — composed state and exact local update

The product automaton has state \((h,\ell)\in S_3\times\{\bot,A,B\}\), with initial (e,⊥) and the following partial transition:
\[
(h,\ell)\xrightarrow{x}(h\,g_x,x)\quad\text{iff}\quad \ell=\bot\ \text{or}\ x\ne\ell,
\]
where \(g_A=a,g_B=b\). This rule is deterministic and composition-closed on any finite legal word. It predicts both terminal frame and future legal language, whereas the quotient forgetting \(\ell\) fails at R669-B's exact collision. For a fixed nonempty legal schedule, only two values of \(\ell\) are needed.

Locality: the added label is attached to this chosen block scheduler, not inferred as a new universal Cell field. When a larger X6 network uses a different port/event license, recompute the necessary scheduling automaton rather than importing \(\ell\) as a physical primitive.

## Computation and next question

R669_VERIFY.py uses Python standard-library exact integer permutations, exhaustively checks every (m,n) with 0≤m,n≤10 against the alternating-language classification, and validates the complete holonomy and last-label witness. 121 input vectors, 41 legal words total, equal-frame cases q=3,6,9; all pass, evidence in R669_EVIDENCE.json. Scope of exhaustion: these 121 count vectors; analytic proofs cover all m,n≥0.

BRC connection: retain the ordered A/B branch provenance and complete non-Abelian frame. Even the complete group-valued terminal summary can lose a future-licensed branch; the certified sufficient carrier for the stated future observer is (h,last block label), not a total-only or frame-only BRC quotient. No signed-amplitude inference is made from these exact positive counts.

Next scientific unit: derive actual V29 port relation H and V27/V30 admissibility rules from Source, then build a product of (i) legal schedule/event machine, (ii) signed field/ledger state, and (iii) S₃ transport. Test at least one shared-Cell two-loop network for locality, continuity, rotation covariance, stable/periodic states and minimality of future-relevant memory. Preserve P000 and the frozen R462 scientific pin.