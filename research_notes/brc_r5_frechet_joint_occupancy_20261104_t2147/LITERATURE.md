# External scientific comparison: semi-algebraic memoryless-policy images

Verified online 2026-11-04 against the publisher record:

Ryan A. Anderson and Guido Montúfar, "The Value Function Semi-Algebraic Set in Partially Observable Markov Decision Processes", Proceedings of the 43rd International Conference on Machine Learning (ICML 2026), Proceedings of Machine Learning Research 306:2677–2715 (July 2026).
Publisher: https://proceedings.mlr.press/v306/anderson26a.html
ArXiv initial posting: 2026-06-02, https://arxiv.org/abs/2606.03048

Publisher abstract claim: the feasible set of value functions for infinite-horizon POMDPs under memoryless stochastic policies is semialgebraic, describable using explicit polynomial inequalities from transitions, observation kernels, and reward dynamics. This supplies published context for why memoryless/observation-key policy images may have nonlinear geometry even when full-history occupancy formulations are polyhedral.

Our R5 note concerns a finite two-action *auxiliary* occupancy map with an exact product relation z=xy and Fréchet coupling lift. Its specific theorem, four-component witness and exact distance are independently derived and checked in RESEARCH.md / VERIFY.py. The publisher paper concerns infinite-horizon value functions rather than the original R5 four-dimensional error/time observer. The literature comparison motivates an exact semialgebraic nonmembership test after the lawful BRC embedding and convex-hull test. It does not establish the original R5 mother conjecture or an independent review of this new result.