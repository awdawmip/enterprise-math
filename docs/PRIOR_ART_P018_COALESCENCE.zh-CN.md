# 前人工作 —— P018 合流时间与 Ultrametric 结构

状态：`ACTIVE PRIOR-ART NOTE`  
范围：P018 Supplement 14  
主要来源 ID：`[SRC-MURTAGH-CONTRERAS-2010-HIERARCHY-ULTRAMETRIC]`、`[SRC-FOUTEL-RODIER-2018-COALESCENT-ULTRAMETRIC]`

## 1. 必须保留的边界

层级合并结构与 ultrametric 描述属于成熟数学。Murtagh 与 Contreras 明确把 hierarchy 与 ultrametric topology 放在同一结构框架中讨论；Foutel-Rodier、Lambert 与 Schertzer 则通过 ultrametric spaces 和 nested partitions 研究 coalescent processes。

因此进取数论**不**主张以下内容为原创：

- dendrogram 或 hierarchy 到 ultrametric 的一般构造；
- coalescence / genealogy merging 与 ultrametric spaces 的一般关联；
- strong triangle inequality 作为 ultrametric 的特征规律。

## 2. 进取数论特有的研究接口

P018 研究的是更窄的 deterministic finite-state 接口：

1. 在选择任何 metric 之前，State Pair / kernel logic 已经存在；
2. 对单个确定性 endomap，首次共同迭代时间完全由 pair 首次进入 diagonal 定义；
3. P020 在良基、单调、向下动力学上给出有限 stabilization；
4. 因而 eventual coalescence 可与 canonical stabilized state 相等精确等价，并由 stabilization steps 给出显式有限上界；
5. 进一步可以证明 P011 collision spectra 在有限 observation set 上经过有限时间后饱和。

这一整合接口的创新性状态为 `NOVELTY_UNVERIFIED`。除非专门历史检索证明，否则只能视为项目特有综合，不得主张历史首创。

## 3. 来源用途

`[SRC-MURTAGH-CONTRERAS-2010-HIERARCHY-ULTRAMETRIC]` 只用于标记 hierarchy/ultrametric 结构属于前人工作。

`[SRC-FOUTEL-RODIER-2018-COALESCENT-ULTRAMETRIC]` 只用于标记更广义 coalescent/ultrametric 联系属于前人工作。

两者都不是本仓库 P020 stabilization theorem 或确定性 kernel 恒等式的证明依据。
