# BRC fixed-word Boolean quotient: exact minimum quota and all-quota enumeration

Date: 2026-10-16 Asia/Shanghai. Status: UNREVIEWED / author symbolic proof and finite exact self-check / NOT Foundation / NO NATIVE CLAIM.
Inputs pinned: GLOBAL_KNOWLEDGE_V1 main b261ab9138dd94ce61383dac7c7521def475a07c; Enterprise Math main 1565f7c1f52441ff9088050243f873dca081db48.
Previous frontier (not independently admitted by this note): Hall/Top-t formula and homogeneous cutoff signature; preceding quota-saturation draft (2026-10-16).

## Typed observer

There are n>=2 labeled sources with d_i nonnegative integers. G_j publicly permits exactly the sources other than j. Each operation secretly resets one permitted source to zero, and every legal path has positive support. The only observable is whether ALL paths end with sum>=Q for an arbitrarily long but PRECOMMITTED word of G_j operations (including the empty word). Public feedback traces, adaptive policies, path weights, signs, and physical X6 dynamics are NOT observed. This is an auxiliary exact BRC observer under the fixed P000/X6 ontology, not a claim of a native X6 embedding.

For initially safe d let c_j be the maximum t in {0,...,n-1} with the homogeneous word G_j^t universally safe. If c_j=n-1, the homogeneous word stays safe even when repeated longer. All unsafe initial states have one signature (-1,...,-1). The inherited Hall formula proves that c is a complete invariant for ALL fixed public words: a mixed omitted-index word with length 1<=t<n is safe iff all c_j>=t; a mixed word with t>=n is unsafe. Homogeneous words saturate after n-1 operations.

## NEW THEOREM A: exact quota to realize each signature

Given a proposed c in {0,...,n-1}^n, set m=min_i c_i, k=n-m-1. A necessary condition is at least k entries equal m. If it fails c is impossible at every Q.

If it holds, sort the cutoff entries nondecreasingly and let
U={c_(i) : i=k+1,...,n and c_(i)<n-1}.
Then c is realizable at safety quota Q>=1 if and only if Q>=Q_min(c), where

  Q_min(c) = 1                         if U is empty;
  Q_min(c) = 2 + max(U) - m             otherwise.

In particular, realizability of signatures is nested as Q grows, although the safety output for any fixed state is not monotone increasing in Q.

Proof. Sort source masses a_1<=...<=a_n and put S_r=sum_{i<=r}a_i. Let k0=min{r:S_r>=Q}. The least homogeneous cutoff is m=n-k0, so k0=k+1. Its first k0-1 mass ranks all have cutoff m, proving the necessary multiplicity condition. At a larger source rank i>k, the minimum mass of a surviving set of size r+1 that contains i is a_i+S_r. For a submaximum cutoff u=c_(i)<n-1 put r=n-1-u in [1,k]. Exactness requires a_i+S_r>=Q and a_i+S_(r-1)<Q. Thus a_r>=1, whence a_r,...,a_k>=1 and S_k>=k-r+1. But S_k<Q, hence Q>=k-r+2. The strongest lower bound comes from the smallest positive r, corresponding to u=max U, giving Q>=max U-m+2.

For constructive sufficiency, if U is empty put the first k sorted masses at 0 and all later masses at Q. Otherwise let s=n-1-max U. Given ANY Q>=k-s+2, set a_i=0 for i<s, a_i=1 for s<=i<=k. For each i>k write r_i=n-1-c_(i); set a_i=Q if r_i=0, otherwise a_i=Q-(r_i-s+1). These are nonnegative nondecreasing integers, S_k=k-s+1<Q, and S_(k+1)>=Q. For i>k with r_i>0, a_i+S_(r_i)=Q while a_i+S_(r_i-1)=Q-1; sources with r_i=0 remain safe when alone. The first k have cutoff m. Thus every prescribed cutoff is realized at every Q>=Q_min. Undo the label permutation. QED.

## NEW THEOREM B: ALL quotas, labeled and unlabeled class numbers

N_n(Q) denotes the number of labeled fixed-word Boolean quotient classes; O_n(Q) counts these classes modulo a simultaneous permutation of all labels. Let b_m(Q)=min(Q-1,n-1-m). Use 0^0=1.

For every n>=2:

  N_n(1)=2^n,
  N_n(Q)=1 + sum_(m=0)^(n-1) sum_(h=0)^(m+1)
                     binom(n,h) b_m(Q)^h,   Q>=2.

  O_n(1)=n+1,
  O_n(Q)=1 + sum_(m=0)^(n-1)
                     binom(m+1+b_m(Q), m+1),   Q>=2.

Proof. Q=1 signatures arise by selecting the support set: k=n-m-1 sources have cutoff m, all m+1 remaining have cutoff n-1. Include one unsafe class. For Q>=2 and fixed minimum m, at least k=n-m-1 entries must equal m, while each of the remaining h<=m+1 entries may take exactly b_m(Q) distinct elevated values: m+1,...,min(m+Q-2,n-2), together with n-1. This is equivalent to Theorem A. Choose the h labels and their values for N. When labels are forgotten, the elevated values form a multiset of size h on b_m types; summing its binomial count over h and applying the hockey-stick identity yields O. Include one unsafe class. QED.

Specializations agree with prior Q=1,2,3 formulas, including N_n(2)=n*2^(n-1)+1, N_n(3)=(n-3)*3^(n-1)+2^(n+1). For Q>=n, the former saturation numbers and O_n(Q)=2^n follow. This theorem thus closes the entire fixed-word Boolean quota stratification, but says nothing about feedback-adaptive observation depth.

## Independent exact tests and limitation

Local C++17 full enumeration: all d_i in {0,...,Q} for n=2..7, Q=1..n+1, totaling 8,558,921 states. Exact signature-set equality, N counts and O orbit counts passed. The cutoff-state candidate search checked 873,611 candidate signatures, 54,984 constructive witnesses, and 20,000 larger-n random construction checks (n<=30). Separate Python positive-support path enumeration checked 32,914 fixed words, including homogeneous saturation beyond n-1. No floating point. Entire local evidence ZIP SHA256: 4709e4fa5f351d4977de86211291fd85181cb124a6c0b8737461ba9d90cac5e2. The executable files, complete proof and full logs are in that local ZIP; this remote note is a small portable source frontier, not proof of its own tests having run remotely.

Example: n=7, c=(1,1,1,1,1,2,4). Theorem A gives Q_min=5; witness at Q=5 is d=(0,1,1,1,1,2,4), while Q<=4 is impossible.

## Honest control/next action

A native research-session attempt returned STATIC_READONLY_SCOPE_DENIED. Native current-task listing returned CONTROL_QUOTA, so no live owner/claim roster was established; do not represent this Git branch as an authorized CLAIM, Research Activity, Result, review, or Foundation admission. Need current native authority and owner verification for formal publication, then independent Driver scrutiny.

NEXT mathematics: find a smallest feedback/source-correlation repair coordinate for the stronger feedback-adaptive observer (start with n<=4, Q=3,T=4); prove a separation counterexample and a scoped preservation law. Keep prior successful fixed-word units as completed and do not repeat the enumerations.