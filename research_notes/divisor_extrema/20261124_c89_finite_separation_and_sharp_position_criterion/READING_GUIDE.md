# C89 阅读、复核与接续路线

## 首读

1. `C89_RESEARCH_NOTE.md`：原问题、全部新结论及精确适用范围。
2. `root/SHARP_MOVING_POSITION_CRITERION.md`：三库存移动位置充要判据。
3. `joint/PAIR_LATTICE_LIMIT.md`：双支联合整数格、成对唯一公式和有限分离真实损失。

## 两条辅助证明链

- 相位链：`phase/PHASE_CONDITIONED_BOUND.md` →
  `root/LOW_PRECISION_SEPARATION_TRANSITION.md`。
- 谱几何链：`spectral/CURVATURE_AND_ALGEBRAIC_TAIL.md` →
  `spectral/THREE_JET_EXCEPTION_ARC.md` → 联合格稿第 8 节的真实管状损失。

谱曲率公式本身来自 C84 `BRANCH_TRANSITION.md` §3；本轮新证明和继承输入
已在每篇的来源部分区分。完整冻结输入在复算包的 `inputs/` 中；远程项目
主目录只保存本轮新源文件，避免复制历史源。

## 准确算术的唯一必需复算

`joint/DOUBLE_SLOPE_CERTIFICATE.md` 解释两个导数非零证书。
在 `joint` 目录执行：

```bash
python certify_double_slope.py
```

脚本只依赖 Python 标准库，生成 `double_slope_certificate.json`。
最终接受区间是准确有理比较；显示浮点值仅便于阅读。
该复算核验横截性输入，不替代联合格定理的文字证明。

## 项目内交叉核查

本轮不同协作研究分工进行了互查；输入共享，记录不称外部独立同行审查。

- `reviews/ROOT_REVIEW_PHASE_AND_SPECTRAL.md`：根代理对相位强化和谱几何的核查。
- `phase/REVIEW_OF_LOW_PRECISION.md`：低精度分离过渡的交叉核查。
- `phase/REVIEW_OF_THREE_JET_EXCEPTION_ARC.md`：三谱真配对弧及有限连续延拓。
- `spectral/REVIEW_OF_PHASE_CONDITIONED_BOUND.md`：相位条件强化的交叉核查。
- `reviews/ROOT_REVIEW_JOINT_AND_CRITERION.md`：根代理对联合格、证书与锐判据的核查。
- `phase/REVIEW_OF_PAIR_LATTICE_LIMIT.md`：双支完整联合极限与真实损失。
- `phase/REVIEW_OF_SHARP_MOVING_POSITION_CRITERION.md`：全移动位置充要判据。
- `spectral/REVIEW_OF_TRUE_LOSS_SYNTHESIS.md`：正规三谱弧与整数格的真实损失合成。

## 参数极限的顺序

原库存定理先固定正的临界倍率极限 \(L\) 与有限分离极限 \(\tau\)，再令
\(c\to\infty\)。低精度 \(L\to0\) 或大分离 \(\tau\to\infty\) 的展开随后
作用于已证明的函数或库存极限夹逼。固定正紧倍率窗口的子列追踪结论已另行证明。

三谱例外弧与 Gamma 准确碰撞推论中的落点是实变量；整数落点问题继续使用
原整数目录。三库存锐判据的 \(B\gg c^{1/3}\) 范围与立方根过渡区也分别保留。

## 直接下一步

全六支有限分离联合极限，以及真实大分离损失的准确主项。
已有双支理论、谱例外弧、相位条件下界和源文件均可直接复用。
多分支 joining 的具体负载义务和条件候选公式见
`joint/MULTIBRANCH_JOINING_FRONTIER.md`。
