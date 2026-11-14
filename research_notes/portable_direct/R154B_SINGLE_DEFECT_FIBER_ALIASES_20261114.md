# R154B — Infinite unequal-denominator phase-fiber identity aliases and full single-defect classification

Date: 2026-11-14, Asia/Shanghai. Status: author-side exact proof and finite exact verification; independent review NOT_REVIEWED. Frozen scientific pin: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Scope: external S23 finite scalar mechanical-word observer with absolute R146 cuts; P000 and native-X6 assumptions unchanged.

Predecessors: R146 \`b02b0c242b274bc6a82111dbd3600126a2867319\`; R153 \`e6e436cb90f6c943b3825a4a2fe26b0500c558f8\`; R154 complete equal-denominator classification, prior branch commit \`835d68a39674d149953c58e96b49516f299b7105\`.

## R154B.1: Explicit counterexample and infinite families

R153 asked whether actual alternating equal-denominator words are the only identity aliases under complete all-coefficient phase-fiber counts. Already at m=4, two distinct words \`0010\` and \`0100\` have identical slope support (0,1/2), identical absolute intercept cuts (U,V)=(1,0), and identical counts C(K)=ceil((K-1)/2) for **all** K>=2. The two endpoint denominators are unequal (1,2). Thus the injectivity of the *cut-residue waveform* (R153.1) does not imply injectivity of the map from words to their cuts.

More generally, for every integer h>=2 define length-2h factors

\[
A_h=0^h1\,0^{h-1},\qquad B_h=0^{h-1}1\,0^h.
\]

Both have

\[
\boxed{\alpha=0,\quad\beta=1/h,\quad (U,V)=(1,0),\quad C_{A_h}(K)=C_{B_h}(K)=\lceil(K-1)/h\rceil\quad(K\ge2).}
\]

The bitwise complements \(\bar A_h=1^h0\,1^{h-1}\) and \(\bar B_h=1^{h-1}0\,1^h\) give a second infinite alias family with support (1-1/h,1) and the same counts.

**Proof.** Each A/B word has exactly one 1. Its lower endpoint is zero because every subfactor has at most one 1. The longest zero-only run has length h, giving beta<=1/h. Every factor containing the 1 has length at most 2h and hence upper-slope bound >=2/(2h)=1/h; every shorter zero-only run gives bound >=1/h. Therefore beta=1/h. With slope alpha=0, R146's cut U=min_j(s_j+1)=1. At beta=1/h, V=max_j(h s_j-j); before the unique 1 the value is -j<=0, and at/after its first prefix j=h or h+1 it equals h-j<=0. The j=0 value is zero, hence V=0. The exact phase-fiber formula

\[
C_w(K)=\left\lceil\frac{(K-1)c-V}{d}\right\rceil-\left\lfloor\frac{(K-1)a-U}{b}\right\rfloor-1
\]

reduces to ceil((K-1)/h). On generic non-boundary slopes, theta->1-theta complements the digit sequence and bijectively maps phase indices N to (K-1)-N-1, preserving counts of nonempty open phase blocks. This proves the complementary family. QED.

## R154B.2: Classification of all one-1 identity aliases at fixed length

For m>=2 let w_{p,q}=0^p1\,0^q, with p,q>=0, p+q=m-1, r=max(p,q)>0. Then the exact support and absolute cuts are

\[
\boxed{\alpha=0,\quad\beta=\min(1/r,2/m)=c/d\ \text{reduced},\quad U=1,\quad V=\max(0,d-(p+1)c).}
\]

Indeed, the most restrictive zero-only upper bound comes from length r, and the most restrictive one-containing upper bound comes from full length m. The maximum prefix cut occurs either at j=0 or at the first prefix after the 1 (j=p+1).

**Complete fixed-length theorem.** Two distinct one-1 words of the same length m have both the same support interval and the same complete phase-fiber count sequence (all K>=2) **if and only if** m=2h is even and the pair is \(A_h,B_h\). This includes h=1 and words 01,10 of length 2.

**Proof.** For m=2h+1, r>=h. The central word p=q=h has beta=2/m, strictly smaller than 1/h; all noncentral words have r>h and beta=1/r, a value which uniquely identifies r. For m=2h, r>=h and beta=1/r, so a fixed support determines r. At each r there are at most two reflected positions p,q. For r=h and m even, these are precisely the two central words, with V=0. For r>m/2, the late-one orientation has p=r and V=0, while the early-one orientation has p=m-1-r<r and V=r-p-1, an integer strictly between 0 and r. Their c=1,d=r ceiling-increment waveforms differ by R153.1 whenever r>=2 (and the count formula distinguishes them directly). The same logic treats odd m's noncentral reflected positions. Hence no other same-support complete-count alias occurs. QED.

Bit complement gives the corresponding full classification of one-0 words. These are **distinct-denominator aliases**: preserving (alpha,beta,U,V) and even the entire future integer count series can still lose word provenance.

## Exact checks and next question

Companion \`R154B_check.py\` checks every one-1 position at m=2..32 (527 words) against the exact support and cut formulas and finds precisely 16 alias pairs, one for each even length. It independently checks A_h/B_h and their complements for h=2..200 at a selection of L values including 10^12+17 (1,393 exact large-integer count comparisons). Data: \`R154B_verification.json\`; marker \`R154B_SINGLE_DEFECT_ALIAS_PASS\`. The all-length theorem rests on the proof.

Next research: classify the fibers of w -> (alpha,beta,U,V) among multiple-defect words; find the minimal word/provenance repair coordinate needed for the declared future observer. In parallel use the R152B first-period certificate and authentic cuts to tackle the still-open full-length saturation threshold T(m)=(m-2)floor((m-1)/2)+1 for m>=5.
