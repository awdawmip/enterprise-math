# High-prefix separation for the full-family second minimum

All quantities and cutoffs use the exact C63 model. For any k≥65, split just before the r=63 block. Write p for the number of noncanonical edges r≥64. Let R be the final TV ratio to A_k. Every schedule with p≥1 satisfies R>29.

Write s=c-r-1, Q=W(r-1,c-m)/W(r,c), and W_0 for the first internal inventory potential. From C63 each noncanonical edge contributes a factor greater than 21/10 after dividing by G_r Q, and all common-edge distortions together contribute more than 377/378. The endpoint correction W_cut D/U exceeds 99/100 for a canonical suffix, exceeds 2 for a competing suffix, and exceeds 14 for a competing suffix if its starting inventory belongs to [2,96]. Also W_0≤1.

1. If p≥5, R>(377/378)(21/10)^5(99/100)>40. If b_0≥2, then W_0≤1/16 and R>(377/378)(21/10)(99/100)16>33. It remains to consider 1≤p≤4 and b_0=0 or 1.
2. Initially s=1-b_0∈{0,1}. An edge changes s by 1-m, and every canonical edge preserves s. Thus before each noncanonical edge s≤4, and at the cut s≤5.
3. If any high edge uses m≥2, its starting c≤r+5, so c/(2r+1)≤(r+5)/(2r+1)<3/5 (since r>22). The exact likelihood formula, with the m+1 factors (1+4x)/(1+x) each at most 17/8 at x≤3/5, gives ρ≤(17/8)^(m+1)/4^m≤(17/8)^3/16<9/10. C63's inequality in the far-from-synchrony case yields L/G_r≥4r²16^(-m) and Q≤16^(2-m). Therefore L/(G_r Q)≥r²/64≥64, and R>(377/378)·64·(99/100)>63.
4. Otherwise all high edges have m∈{0,1} and s is nondecreasing. If cut s were zero, it would have stayed zero throughout, and all high edges would have m=1: this contradicts p≥1. Thus cut s∈{1,2,3,4,5}, i.e. cut c∈[65,69]. Every suffix from such a state is competing, so C63 supplies W_cut D/U>14, and R>(377/378)(21/10)14>29.

These branches exhaust all high-divergent schedules. This reuses C63's primary cut without a new large-inventory computation.

## Source relation

The inherited original is C63_RESEARCH_NOTE.md, §§2–5 and Appendix A, in the C63 research package (copied locally at inherited/C63_RESEARCH_NOTE.md). The new point is counting noncanonical edges and applying the far-from-synchrony subcase only to the bounded-imbalance prefix. The exhaustive small-rank suffix certificate is a separate step.

## First-divergence bound with arbitrary k and arbitrary positive multiplier

Let r*≥64 be the first noncanonical edge, counting from the first 23 towards the end. Write r=r*. At this edge s≤1: either s=1-b_0≤1 initially or all preceding internal edges were canonical (and so s=0). One has L/(G_r Q)>r/40 in every case.

- m≥2: as above c≤r+2 gives ρ<9/10, hence L/(G_r Q)≥r²/64>r/40.
- m=1: this edge is noncanonical so c≠r+1. The C63 single-5 lemma gives Q≤1, |ρ−1|>1/(2r) and τ/(τ+max(1,ρ))²>1/460. Hence L/(G_r Q)>100r/920>r/40.
- m=0, s≤0: C63 gives Q≤16 and L/G_r>100r/80, hence L/(G_r Q)>100r/1280>r/40.
- m=0, s=1: we have c=r+2, Q=16(3r+1), and ρ−1=3c/(K+c)>1 since 2c>K. From τ=7(D₂/D₀)(D₂−1)/(D₁−1), both ratios are in [1,3]: c/K<3/5<8/13 gives D₂/D₀<3 and c≤4r gives (D₂−1)/(D₁−1)≤3. Thus τ∈[7,63] and τ/(τ+max(1,ρ))²≥τ/(τ+4)²>1/80 (evaluate endpoints). It follows that L/(G_r Q)>100r²/[80·16(3r+1)]>r/40 since r>8.

All remaining noncanonical high factors exceed 21/10, W_0≤1, all canonical high-edge distortion costs combined exceed 377/378, and the cut correction for every suffix exceeds 99/100. Since (377/378)(99/100)>40/41, it follows that **R>r*/41**. Thus any schedule of ratio at most M can first depart only at r*<41M or inside the last 63 pairs. Fixed-rank consequences follow by choosing finitely many legal fixed suffixes of bounded derivative ratio to the canonical suffix.
