# Next R1/N14 research unit — non-IID two-law compression

Status: continuation question only, not a canonical V2 task, native CLAIM or transfer of Stage171 ownership.

Given strictly positive but history-dependent measures P,Q on a finite observed-path tree and a deterministic monitor x=(t,k,s), find necessary and sufficient flow feasibility conditions for ONE law-independent randomized policy on x to match the joint terminal (T,x,D) distributions of an arbitrary complete-history policy simultaneously under both laws.

Smallest test: two ordered paths 01 and 10 with identical counts and merged monitor, but with unequal likelihood ratios Q(01)/P(01) and Q(10)/P(10). Define a positive rational two-law path model and a decision rule selecting P only on 01, requiring stop at t=2. Prove or refute the existence of a common compressed randomized action matching both decisions under P and Q. Then formulate a minimal ratio-aware repair, declaring what prefix information must be retained and proving future update compatibility.

Success: exact fractions; complete argument or minimal counterexample; independent arithmetic checker; prior-art/novelty status kept separate; author persistence with GitHub readback. Do not repeat the already completed N=4 IID finite monitor classification. No six-dimensional P000 correspondence or mathematical promotion may be inferred from this external auxiliary result.