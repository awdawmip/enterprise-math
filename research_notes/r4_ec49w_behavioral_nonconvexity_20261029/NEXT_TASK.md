# EC49X — exact full behavioral fixed-cost optimization

Parent: EC49W (this author-side portable proof), preceding immutable EC49V commit 1b6afb0b3d015c383812de56378e834ea8742006.

**Known exact frontier.** At eta=1/200, C1=43/48, C2=7/8 and no retained shared seed, 59/576≤δ*<11/96; the always-buy-S subclass has exact maximum 59/576, while the 11/96 convex-hull bound is behaviorally unattainable. The precise full δ* and complete (alpha,beta) section are open.

**Next discriminating unit.** Include randomized decisions not to buy S after U and each retained code. Let prefix x_wc≥0 sum_c x_wc≤1 and conditional purchase rate s_{c,u}∈[0,1]. Retain rank/factorization y_{w,c,u}=x_{w,c}s_{c,u}, i.e. source-blind information-set consistency, rather than allowing each history's S rate or a shared ex-ante seed. For t_w(u)=1/2+(2u-1)eta sigma_w and Δ_w(u,z)=t_w(u)(3I[w=z]-1)/36, require:

C1=(1/3)Σ_wc (1+I[c starts B])x_wc=43/48,
C2=Σ_wcu x_wc t_w(u) s_{c,u}/3=7/8,
δ=Σ_cuz [s_{c,u}Σ_w x_wc Δ_w(u,z)]_+.

Prove all-S dominance at these exact costs, or produce an exact rational no-S policy with δ>59/576, or give a certified semialgebraic/interval upper bound with complete cover. Ordinary floating numerical optimization is exploratory only. Compute the full fixed-cost (alpha,beta) region after this frontier.

Preserve auxiliary positive-weight BRC type and P000/ACTIVE worldview. Verify true native owner and independent Driver permissions before Source Task/Result/acceptance, and request independent replication/prior-art review.