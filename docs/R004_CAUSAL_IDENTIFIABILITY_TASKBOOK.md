# R004 / FQ-20260810-007 — Causal Identifiability Research Taskbook

Status: `READY_FOR_CLAIM`  
Owner: `research/r004-causal-identifiability-v1`  
Foundation question: `FQ-20260810-007`  
Scheduler task: `RS-R004-CAUSAL-IDENTIFIABILITY`  
Layer: `L1/L2 research owner; NOT canonical Foundation`  
Hard block: `NONE`

## 1. 研究目标

本任务只研究一个问题：

> 是否存在一个比“直接假定 Bell locality + measurement independence”更弱、且能够自然写入进取数论有限状态/关系语言的 causal / intervention primitive，使“在线生成新的可区分性”与“从一开始就存在的有限 latent / pre-sampled completion”在操作上可区分？

若不存在，则目标不是继续加更强假设，而是证明一个精确的 **identifiability impossibility boundary**：说明当前 Foundation 在什么假设范围内原则上无法区分二者，并指出最少还需要增加哪一类物理/因果公理。

本任务不负责证明量子力学、宇宙起源、Big Bang、隐藏变量理论或 Bell 定理本身。

## 2. 必须继承、不得重证的 canonical 边界

### FQ-004

保持以下三层不同：

`exact state equality != current observational equality != declared-future-safe equality`

除非存在显式 factorization / sufficiency theorem，否则不得把压缩坐标当成完整未来状态。

### FQ-006

对确定性部分操作 `F_a:D_a->X`：

- enabledness / domain membership 属于 future behavior；
- enabled target quotient class 必须可下沉；
- legality-sensitive refinement 给出有限最粗兼容细化；
- 全定义时精确退化到 P023 total-operation closure；
- absorbing `UNDEFINED` 只允许作为显式区分的验证表示，不是 ontic state。

FQ-006 **不**回答“future alternatives 是 latent 还是 generated”。

### A4

multivalued correspondence / support 继续属于 A4。不要把它改写成一个 hidden-variable completion，也不要重新拥有 A4 mother theory。

## 3. 三份冻结压力测试输入

历史 R004 PR #302 只作为 evidence/provenance，不作为新 owner 的代码基底。

### E1 — arbitrary finite pre-sampling survives

来源：`src/enterprise_math/precision_genesis_intervention.py`

已知边界：

- finite deterministic compatible tower 可由有限 latent master / compatible path completion 表示；
- finite rational stochastic response family 可清分母后由有限 uniform seed completion 表示；
- finite adaptive intervention syntax 仍可被一个有限 counterfactual response table 预采样，只要允许任意全局表。

因此“多分支”“随机”“自适应”本身都不足以证明 ontic generation。

### E2 — finite latent capacity has an exact price

来源：`src/enterprise_math/precision_latent_capacity.py`

对 `m` 步、每步 `r` 个 full-support outcomes 的完整 deterministic pre-sampling：

`|U| >= r^m`。

这是资源下界，不自动成为物理公理。研究必须明确区分：

`latent completion exists`

与

`declared initial ontology has enough latent capacity to host that completion`。

### E3 — a testable structural restriction can obstruct pre-sampling

来源：`src/enterprise_math/precision_locality_obstruction.py`

在 setting-local deterministic response + setting-independent hidden sampling 下，有限混合满足 CHSH bound；R004 exact rational target

`(-3/5,-3/5,-4/5,+4/5)`

满足 `|S|=14/5>2`，并有 exact unbiased 20-atom joint tables 与 exact no-signalling marginals。

若只放松 measurement independence，保留 locality，则该目标在当前 TV normalization 下有 sharp cost

`M_min = 2/15`。

这只证明“加入独立可检验的结构约束后，pre-sampling 可以变得可证伪”。Bell locality / measurement independence 是 prior-art causal commitments，不得直接写成 Foundation primitive。

## 4. 第一优先研究动作

不要先设计新宇宙模型，也不要先搜索更多 Bell 例子。

第一步是定义一个候选的有限 causal-accessibility / intervention-context 结构 `C`，要求：

1. 严格弱于直接安装 Bell locality + measurement independence；
2. 能在现有 typed state / partial future-language / relation-support 语言旁边精确定义；
3. 不偷偷把完整 counterfactual table 当成 primitive state；
4. 有明确 observable equivalence：两个模型在所有声明 interventions 下何时算操作等价；
5. 可以问出“任意 finite latent master 是否仍然能 factor through C”。

然后立即做二择一压力测试：

### 路线 N — no-go 优先

尝试构造一个 universal latent-completion compiler：

`finite C-process -> finite latent master / response table`

若能构造，优先证明它，并记录让该构造成立的最弱假设。不要因为结果是否定的就继续加假设直到得到正结果。

### 路线 P — obstruction

若某个明确的 `C` 阻止 universal latent completion，则提取最小 obstruction：

- 哪条 factorization / accessibility law 失败？
- 是否存在有限 witness？
- witness 是否只依赖 project-native `C`，而不是暗中重新引入 Bell locality？
- 去掉哪一个假设后 latent completion 重新出现？

## 5. 建议的首批候选 primitive（只作为待证伪对象）

这些不是答案，也不是 Foundation 提案，只是优先级排序：

1. **intervention-local response ownership**：一次 intervention 只能访问其 declared causal neighborhood，而不是读取一个全局 counterfactual response table；
2. **state-extensional causal accessibility**：未来合法操作只依赖当前 retained state / relation state，不可直接读取被历史坍缩掉的 witness identity；
3. **bounded latent capacity**：初始 state 明确携带有限 latent-resource budget，未来完整 response language 若需要超出预算则不能由初始 deterministic seed completion 实现；
4. **composition/factorization locality**：独立 causal regions 的 joint response 必须通过某个声明的局部组合结构，而不是任意 joint table。

每一个候选都必须先问“是否只是把要证明的结论换了名字”。

## 6. 禁止越界

新研究只写入：

- `docs/R004_CAUSAL_IDENTIFIABILITY_*`；
- `src/enterprise_math/r004_causal_identifiability*`；
- `tests/test_r004_causal_identifiability*`；
- 对应 experiments / sources / lineage。

不要修改或占有：

- `src/enterprise_math/precision_*`；
- `tests/test_precision_*`；
- A1/A2/A4 generic mother theory；
- FQ-004 / FQ-006 canonical statements；
- P016 physical promotion rules。

若发现 generic theorem，应通过 Relay / Foundation Feedback Packet 路由给真实 mother owner，不在 R004 私有复制。

## 7. 交付标准

### 正结果

必须包含：

1. typed causal/intervention primitive；
2. weakest hypotheses；
3. operational equivalence definition；
4. obstruction theorem；
5. 至少一个 exact finite witness/falsifier；
6. 去掉关键假设后的 latent-completion counterexample；
7. prior-art audit；
8. 与 FQ-004/FQ-006/A4 的 reduction/boundary；
9. 明确说明哪些内容只是 physical axiom candidate。

### 负结果

必须包含：

1. 明确的 candidate class；
2. finite latent-completion theorem / compiler 或不可区分定理；
3. 最弱假设；
4. 至少一个 exact executable cross-check；
5. “还需增加什么类型的 axiom 才可能可检验”的最窄说明；
6. prior-art audit。

负结果与正结果价值相同，不允许为了得到“生成是真的”而不断增强定义。

## 8. 回流格式

达到一个可证明 checkpoint 后：

1. owner branch 内保存 theorem/tool/test/provenance；
2. Relay #82 发布可复用结果或 negative boundary；
3. 在 Issue #164 的 `FQ-20260810-007` 下 RETURN：
   - theorem/counterexample；
   - weakest hypotheses；
   - exact source commit/PR；
   - executable evidence；
   - prior-art boundary；
   - canonical change recommendation；
4. 不自行修改 Foundation；等待 steward independent verification。

Scheduler 是 best-effort coordination。无 CLAIM 也不阻止明确用户任务或 owner-local research；只有完整四字段 mathematical `HARD_BLOCK` 才能停止该路线。
