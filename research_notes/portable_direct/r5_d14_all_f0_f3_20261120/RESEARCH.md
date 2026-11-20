# R5 D14 — universal pair-augmentation plateau through f=3

Date: 2026-11-20 (Asia/Shanghai). Scientific state: AUTHOR_EXACT_FINITE_CHECKED / PARTIAL_INDEPENDENT_CROSSCHECK / NOT_REVIEWED. Finite scalar observer claim, no native X6/BRC transfer. Historical researcher provenance: EM-DIRECT-4C3E47.

## Frozen model and theorem

Frozen science: awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551; input EXACT_R5_ALL_101_BUDGETS.json SHA256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. There are 101 physical queries with costs k=214..314, original 256 named hypotheses, tau=58182461585441404127941754879, and unflagged adversarial errors.

Define W=(0,16,32,48,1,64,17,80,18,24,34,82). For every distinct u,v outside W and every f=0,1,2,3:

    V_f(W union {u,v}) = 735 + 950*f.

Every one of the C(244,2)=29,646 original labelled pairs was rebuilt in the complete fourteen-name joint model, yielding exactly 1,906 distinct price-aware maximal-support signatures; all 7,624 representative class/budget Bellman roots were solved. The four universal costs are 735, 1685, 2635, and 3585.

## Finite proof and reproducibility

For each price k, the doubled left endpoint 2*N_i(k)-tau witnesses S_i(k)={j:0<=N_j(k)-N_i(k)<=tau}. Because observation intervals are closed, inclusion-maximal joint response supports occur among these endpoints. Properly contained supports do not affect the worst-case Bellman recurrence. If two actions have the same complete maximal-support family, use the one with smaller cost; full-live masks stall and are excluded in a finite worst-case-cost strategy.

For e_i in {0,...,f+1}, a state terminates at at most one live hypothesis (e_i<=f). Otherwise the exact recurrence is V(e)=min_k [k+max_{S in F_k} V(min(f+1,e_i+1_{i not in S})_i)]. Each nonstalling action increases some live counter on every branch, yielding a finite acyclic recursion. The 1,906 price-aware classes come from entire 14-label support families, retaining membership of all 29,646 original pairs; no marginal or unproved native quotient is used.

The C++ source R5_D14_ALL_F0_F3.cpp independently rebuilds all original pair signatures from frozen integer adjacency. A second C++ dynamic program, driven by the predecessor's classes_1906.tsv, computed 7,624 roots with full CSV SHA256 ca98db96823e3d217bc751821fb67c6161521ebce8b0350067b7ba702dc7a019. The standalone rerun's 7,053 completed prefix rows and a 572-row suffix after an interrupted run matched the full independent-class CSV (with one overlap row).

Nonterminal state counts across all classes: f0=75,243, f1=1,204,558, f2=8,378,296, f3=40,918,646, total=50,576,743. Independent Python code constructed doubled-endpoint supports and tuple-state DP, verifying 71 class/budget roots over 22 different classes, including 7-, 8-, and 9-action signatures. These are author-controlled computations, NOT_REVIEWED by an independent mathematical reviewer.

## Additional calculations and next question

In separate bounded experiments, 121 out of 278 previously unresolved maximal preorder classes returned exact f4=4535 and f5=5485. The next run was interrupted, so this proves no corresponding claim for the other 157 maximal representatives. All completed rows are preserved in the reproduction bundle.

The universal fourteen-label plateau through f3 means that any strengthening inside this double-augmentation family must first emerge at f>=4. At f8 the predecessor's 1,265 certified signature classes/26,388 named pairs remain at V8=8335; the remaining 641 classes/3,258 pairs await resolution. The full 256-name eight-error range remains [8335,8343]. Continue with restartable 278-maximal-class f4/f8 analysis and strategy-level simulation, particularly (128,144) and (128,160). No formal CLAIM/RUN or native BRC result is asserted.

The locally verified 16-file reproduction bundle includes frozen source input, full 7,624-row results, C++ and Python programs, bounded f4/f5 results and per-file SHA256 manifest.
