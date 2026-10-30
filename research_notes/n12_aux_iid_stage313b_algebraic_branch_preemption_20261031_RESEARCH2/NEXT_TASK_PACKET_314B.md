# Stage314-B — locate the first full-eight-rate Pareto departure from the local polynomial

Parent and frozen input: Stage312-B at research commit `2b33ac263fe327436da5a5bbf982deef89ba65ce`, followed by Stage313-B algebraic/rational preemption proof in the adjacent file. Recheck current global and EM control snapshots before subsequent execution; the current run fixed `GLOBAL_KNOWLEDGE_V1 main@ffc97b2f` and `Enterprise Math main@673a838d`.

The model is unchanged: `S` fair with Bernoulli future rates 1/4,3/4; `P(J=S|S)=7/8`, `P(W=S|S)=3/4`, Y~Bern(p_S), h=(J,W,Y), source weights `/256` `(63,1),(21,3),(21,3),(7,9),(9,7),(3,21),(3,21),(1,63)`, G=(W,Y), three locked-rate future F visits, independent fair H bits. Full eight-rate cube, with all-F public `P` and source-tagged `T` total variations. MAP `P0=11/256`, `T0=77/1024`.

Proved frontier through `E=18117/4000000`: `F_P(P0-eps)=T0+g(q^{-1}(eps))` with `q=9u/128+3u^2/32-u^3/8`, `g=117u/4096-123u^2/1024+23u^3/256`.

Stage313-B shows a strict **later** failure: choose `t_100=(7-sqrt(13))/8` and all others at MAP. Then `P=(-1/32+9sqrt(13)/512)` and `T=(319-sqrt(13))/4096`. Let u_c be the unique root of `g(u)=(11-sqrt(13))/4096` in `(109/1000,11/100)`, `eps_c=q(u_c)≈0.00865532323`. For every `eps_c<eps<=q(3/25)=0.0095715` the old polynomial is strictly above a feasible tagged cost. Exact rational corroboration at u_small=11/100, u_large=87/500. **This is a formula/solution-branch preemption; no global active-set switch has been established.**

Smallest next work: derive an exact lower envelope for each source-fiber sign chamber and compare the small-u candidate against all one-, two-, and eight-fiber competitors on `(E,eps_c]`. Either prove `eps_first=eps_c` and classify whether the one-fiber jump is globally optimal, or construct a rigorous earlier competitor and narrow the bracket. Maintain separation of first formula failure, first active-set change and first observation-sign flip. Provide exact algebraic or rational/interval certificates plus actual executable output, and retain the native X6 correspondence obligation.

Delivery state: portable author source, `UNREVIEWED / NOT_ADMITTED`. No formal native CLAIM, Source Result, reviewer or Driver acceptance inferred from this handoff.