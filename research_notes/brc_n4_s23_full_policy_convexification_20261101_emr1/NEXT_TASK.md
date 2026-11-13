# Next exact research unit: stochastic five-state storage

Preserve full-policy convexification theorem PROOF.md: a common stochastic 6xk encoder E supports full behavioral 11-parameter S23 error <=epsilon with fully policy-dependent decoders iff ALL 2048 deterministic causal strategies have policy-dependent decoders for the SAME E with that bound. No continuous family of policies needs enumerating for this full-policy question.

**Open discriminating question:** Is there a stochastic 6x5 source encoder and 2048 policy-specific 5x4 decoders attaining a **strict rational error smaller than 1/40**? Alternatively show a universal exact >=1/40 obstruction. Previous authors proved 1/47 <= unrestricted stochastic five-state floor <= 1/40, while deterministic five-state floor is exactly 1/40.

For every s in {0,1}^11, use the exact source matrix M and time kernel F_s in PROOF.md. Unknown common E[x,z]>=0 with row sums 1; unknown D_s[z,t]>=0 with decoder row sums 1. Introduce u_s[i,t]>=0, require

    -u_s[i,t] <= sum_x M[i,x] (F_s[x,t]-sum_z E[x,z]D_s[z,t]) <= u_s[i,t],
    sum_t u_s[i,t] <= 2 epsilon for every prepared row i and table s.

For fixed E, each table is a rational linear feasibility problem. Joint E,D_s feasibility is bilinear: numerical optimizers can suggest candidates but cannot certify a global bound. A proposed rational improvement must verify ALL 2048 tables exactly, after which the theorem automatically covers all behavioral strategies. A lower bound must quantify over all stochastic E. Do not substitute the six terminal-source indicator policies for the entire 2048 set without proving that reduction.

Full-policy continuous decoder availability is different from m=10 precommitted policy tags; that finite-label problem remains distinct. P000 native six-axis Cell/time readout and S2 causal embedding are separate bridge obligations. Author-side research is UNREVIEWED / NOT_ADMITTED; native service research authority/Owner/CLAIM remains to be verified independently.

Input sources: GLOBAL_KNOWLEDGE_V1 main@9ced971d8b4a0352707cfb25bcb17977a494feb4; Enterprise Math main@993a408982a302265cb3c31f93e69e4751299500; predecessor c22282ef2deea811f7e300c76c7282deefb39f89; PR #1762.