# Heartbeat58 — retained residual field and a reader that writes back

Progress-Event-ID: HEARTBEAT58-COUPLED-FIELD-READER-BDE0CA-20260924
Researcher-ID: EM-DIRECT-BDE0CA
Research-Activity-ID: RA-4D2482B655C2FAA41ABA0E43
Status: CONDITIONAL_MODEL / SAME_AUTHOR_BRC_EXECUTION / NOT_ADMITTED

## User correction and provenance

Current user: “我的直觉告诉我计算压在哪边都不对，既要保留住原始残差形成一个场，又要构建一套读取规则来变读取场内容边模拟坍塌。” The new target is coupled field/instrument evolution, not moving all computation to either a fixed field or a history-dependent renderer. Prior Stage56/57 no-go scopes remain unchanged; the old reader is not overwritten.

Global read db1b93aa72aad29cd4bdb057886d4fefcaff1bf4; control read621bd918cfe4eea9f0c0ae20aa82def82fbc87bc. Actual statusIssue2079 and sessionIssue2080/hb58-session-20260924-a7e3 succeeded. SessionMCP-51b7533a7d9b424ca5f85ec16af1870e, activity registration3399dc1e90a9b5c78d30bf06b33cc6021f6510cc, comment5810326715. Prior contribution IDs disclosed. No formal Task/CLAIM/run/review, new independence, P000 or worldview modification.

Continue Stage57 standalone3177357504fdd8e5e14d8fece6ae8a9960a9270f. New cumulative213cb81faa0d2228f7ca0584d4d7b880330804a7, entrySTART_HERE_STAGE58.md. Full proofstage58/PROOF.md SHA25681367e6b152329d0761d2b43faf8ce05876eec6fa69cb95064c87dbfe54650ea; resultsSHA2566fc21dead15ae480b57c3b3de321934c418697793b9002bc2cbc2e6162167221. Code stage58/coupled_reader.py and run.py; contract, metadata and manifest included.

Bundle BRC_Heartbeat_coupled_reader_stage58_20260924.bundle,37938197bytes,SHA256d73adcd944fee2bc88b8304cbc7b776e3f7fd6139047cf5c95b8c07eb8c972e7. Drive1sH7D3uEUcllb2px5-jQy4UjgH8bhq8sz uploaded/fetched and byte-identical. A fresh local bundle clone replay passed207 named checks/5 actual canonical core calls. All scientific fields and call identities match; original and replay elapsed_ns values at run and per-call levels remain separately preserved.1186 inherited files byte-identical;8 new manifest entries verified;git fsck passed, unique ancestorc8f0d39e47d57037379c5861a06078bfa70347a2 retained. This is same-author replay, not independent validation. No new live HTTP or remote server deployment.

## 1. A closed field/reader update

The link field ell and coherent field state are different objects. Full X contains material positions/ports, ell, reservoir and retained records; Psi(X) or rho assigns coherent relations to these complete configurations, not a scalar probability to ell. No negative material mass or automatic identification of residual with energy.

rho_tilde=W rho W*; J_o=M_o rho_tilde M_o*; p_o=Tr J_o; rho_next=J_o/p_o for the selected nonzero outcome. The reader stores rho_next before any later propagation, not the original rho or only a histogram. Completeness sum M_o* M_o=I preserves total unnormalized weight. A full recording isometry sum M_o tensor|o> preserves the joint state; choosing one classical outcome is an explicit quantum-instrument/Born bridge, not derived here. Settings/history may enter later W or M; only fixed settings and actual retained histories are tested in this prototype.

For a region projector P,Q=I-P, choose rational u>v>0,u²+v²=1. M+=uP+vQ,M-=vP+uQ. A real conditional pointer coupling uses F_P=[[u,v],[v,-u]],F_Q=[[v,u],[u,-v]],V=P F_P+Q F_Q, so V*=V,V²=I. The inherited BRC reflection compiler is actually used. The record is appended before selection; complete field/port/source/battery labels are never replaced by the probability summary. Raw branch amplitudes remain unnormalized, avoiding numerical square roots.

If P is diagonal on the source-compatible configurations and commutes with H, the coupling preserves Gauss and bare energy for a degenerate-energy pointer. Sharp energy support stays sharp on each branch. With energy mixtures, conditional means can change without energy creation. Switching, reset, preparation and a physical clock remain unclosed.

Inside either P or Q each selected map is scalar, so internal field distinctions and relative phases persist. Retaining original residual does not require all amplitudes to be immutable. Unread crossblock PrhoQ is multiplied by2uv; selected branches instead reweight/normalize. Pure conditioned inputs remain pure. Neither purity nor within-region coherence equals a universal absence of localization.

## 2. Exact accumulation and repeated-QND collapse

For a static region or nonmixing W, let p=Tr(P rho),a=u²,b=v²,a+b=1. P(+)=ap+b(1-p), P(-)=bp+a(1-p); posterior p+=ap/P(+),p-=bp/P(-). On the consistent outcome-history probability space, with its nested record filtration, E[p_next|history]=p.

After counts N+,N-: p_n/(1-p_n)=[p0/(1-p0)](a/b)^(N+-N-). This accumulates relative evidence of one preparation, not arbitrary absolute phases of independent particles. Contradictory later reports can reverse localization tendency.

For h=p(1-p),kappa=a-b: E[h_next|p]=ab h/(ab+kappa²h), and h-E[h_next|p]=kappa²h²/(ab+kappa²h)>=4kappa²h². Telescoping gives sum E[h_n²]<infinity. Markov+Borel–Cantelli implies h_n->0 almost surely; bounded-martingale convergence gives p_infinity in{0,1}, and bounded convergence yields P(p_infinity=1)=p0. This is a concrete standard repeated-QND collapse proof, not new universal physics. For u,v>0 and0<p0<1, no finite nonzero-weight history forces exact zero. A finite-resolution stopping threshold must be stated. The native moving field below mixes regions, so this convergence theorem is NOT transferred to arbitrary driven motion.

u4/5,v3/5 gives coherence multiplier24/25 and measurement bias7/25. For p0=1/2, n favorable reports yield p_n=16^n/(16^n+9^n), with history probability[u^(2n)+v^(2n)]/2. At n1/2/4/8 the probabilities are16/25,256/337,65536/72097,4294967296/4338014017. These are conditional paths, not an unconditional deterministic drift to one side. All outcomes are retained. Unread mean coherence decays as(24/25)^n while each ideal selected pure trajectory stays pure.

## 3. No-click also writes back; avoid counting one particle repeatedly

K0=Q+uP,K1=vP is a complete one-region click instrument. Equal two-mode input with u4/5,v3/5 gives P(no)=41/50,P(click)=9/50,p(region|no)=16/41,p(region|click)=1. Thus a no-click result changes the surviving field. In the nonmixing case P(first click at n)=p0 v² u^(2n-2),survival_n=(1-p0)+p0 u^(2n). The unobserved complement need not eventually click.

Prototype first-click latching closes this preparation's record stream after one click. This is an observation protocol, NOT physical absorption; real absorption needs source/energy transfer to the detector and is not implemented by deleting field identities. Repeated weak-meter outputs remain tagged meter_report, not independent particle detections. Deterministic counting debt may render scores, but cannot silently replace stochastic instrument sampling in the above martingale/collapse proof.

Actual feedback witness: start|+>,read M+,apply inherited rational R=[[3/5,-4/5],[4/5,3/5]],read again. Correct updated-field P(next+)=9/25; evolving stale original field gives457/1250, difference7/1250. Both use the same actual BRC compiler; the stale calculation is a deliberately faulty comparator.

## 4. Real twelve-neighbour field integration

Reuse Stage55: both identified sources mobile,Dell=delta_xplus-delta_xminus,H0/epsilon=sum ell²+B=1,full twelve-port coins,W=Sminus Cminus Splus Cplus. P tests xplus=e1; after the first W its probability is1/36. Execute W,V,W,V. The four record histories each retain3456 nonzero complete endpoints. All outcome weights sum to1; every endpoint preserves Gauss,energy1 and source separation<=1. Conditional battery means vary without changing total energy.

The union of full tagged conditional branches equals the unselected coherent-record calculation exactly. On that WHOLE joint state the actual reverse order V2,W^-1,V1,W^-1 restores the original full input and both ready pointers. This is not a deterministic inverse of one selected branch and does not establish objective global collapse. A developing dense-density comparison timed out without producing finalized evidence; the final sparse complete-amplitude equality avoids needless quadratic-size expansion and passed. No old result was overwritten or counted as new.

## 5. Evidence, literature and limits

207 named assertions include126 per-history likelihood checks; these are not207 experiments.5 real cached canonical BRC core calls per fresh execution: unchanged bc7babbb9e890f6d5a7094430a5fbdccf66c77ad:src/enterprise_math/brc_weighted_recurrent.py,blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb,SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26. Actual reuse Stage45/50/53/55. No pi,trigonometry,ordinary propagator or eigensolver. Four64-report pseudorandom traces are illustrative synthetic data. Outcome-ID retry is idempotent; closed first-click streams reject a new mark.

Primary abstracts/metadata read: Jacobs/Steck quant-ph/0611067; Bauer/Bernard1106.4953; Murch etal1305.7270/Nature502,211–214(2013). Instrument back-action, repeated-QND collapse and measured quantum trajectories are prior art. No full-text novelty audit or empirical raw-data fit.

Dedicated Issue2081/batch7da45813-a866-4740-96e2-28c0e947ea31/comment5810349635,requestSHA2053f352aa19aec8af0591e71a3d3cbe7c741979755ee19a3e03c5e923185342: outerFAILED,two childPARTIAL, target metadata quant-ph/0611067v1 and1106.4953v2,2provider calls,0bridge-model calls. Original full response remains in Issue; selected exact metadata/status in stage58/QUERY_OUTCOME.json, not a full-paper cache.

Still unproved: native amplitude/phase and Born origin; autonomous detector source/energy/control transfer; calibrated heartbeat duration; actual experimental likelihood fit; fundamental irreversible-collapse uniqueness or instantaneous signal. This is a new conditional field-reader interface and checked model, not mathematical admission or completion of the broader physics objective. Next: model independently calibrated detector inefficiency/unobserved records in this SAME full-field trajectory, rather than another passive histogram.
