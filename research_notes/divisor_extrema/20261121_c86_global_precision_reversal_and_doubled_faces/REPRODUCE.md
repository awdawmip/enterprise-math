# C86 复算入口

本包证明全库存高精度比较 \(I_{1/4}<I_{1/2}\)，并给出
\(1.7101<\kappa_3<1.7960\) 及三角窗 \(A<8/3\) 的准确概率公式。

## 阅读顺序

1. C86_RESEARCH_NOTE.md：结果、原库存含义、精度反转和剩余问题。
2. smallarea/ALL_AREA_FAREY_MELLIN.md：完整全面积归约。
3. CERTIFIED_HIGH_PRECISION_COMPARISON.md：二维积分误差与原模型推论。
4. phase/KERNEL_REGULARITY.md：独立连续性和积分审计。
5. triangle/CHORDAL_CORRECTION.md、DOUBLED_FACE_INTEGRAL.md、QT_SUPPORT.md：三角分支完整证明。
6. smallarea/DOUBLED_FACE_INDEPENDENT_REVIEW.md：三角分支的独立内部复核。
7. phase/EXACT_PHASE_ELIMINATION.md：准确固定有理格算法及朝向反例。

## 环境与路径

准确积分程序使用 Python 3 的标准库。两个符号核对脚本额外使用 SymPy；
NumPy 只用于明确标为探索性的 Gaussian 脚本，不是证明运行依赖。
所有程序按自身所在目录寻找数据，解压位置不限。
以下命令均从包根目录执行。

## 默认准确核对

    python verify_bundle.py

本轮实际运行结果：7 组检查全部 PASS，失败 0，见 checks.json。
这些组分别检查完整有限归约、整区间连续性、小区域分析常数、有理格相位算法、
三角构型及角积分、独立三角复核、主证书的准确算术绑定。
组数与各组内部的子项计数是不同口径。

默认核对重跑有限有理和符号检查，验证已保存积分证书的源绑定、算术关系及严格端点；
它不冒称重新运行全部积分网格。本轮两个完整积分本身已经实际执行，
结果分别保存在 mellin_integral_certificate.json 与 triangle/doubled_face_certificate.json。

## 从头重新计算两份完整积分

    python verify_bundle.py --full

完整模式先重算二维主积分和三角常数，再执行七组核对。在本次运行环境中，
主积分约 13 秒，三角积分约 81 秒；不同机器时间会不同。
准确端点应相同，JSON 中运行时间等观测字段可以不同。

也可单独运行：

    python certify_mellin_integral.py --n 96
    python triangle/certify_doubled_face.py

主积分：96×96 单元，112 位向外区间，48 位整数验证二十次根，
40 位有理节点，跨区单元单独使用分片梯度误差。

三角积分：外层每单位面积 1024 单元，短方向网格 512，
Π 的方向网格 256，面积缓存网格 64，QP 在两个 u 区间各用 64 个单元。
支持交叉、二阶导数余项及原有尾界均包含在证书中。

## 准确分类的再生成

    python smallarea/enumerate_width_kernels.py
    python smallarea/symbolic_mellin_chambers.py
    python smallarea/verify_finite_reduction.py
    python phase/verify_mellin_regularities.py

独立有限验证器不导入分类生成器；它检查每个整数仿射变换见证、
全部参数区域的线性不等式、完整宽度推前分布及各区间系数。
因此生成与验证并非同一代码路径的自我比较。

## 固定有理格的准确计算

    python phase/exact_phase_moment.py --basis 3 -4 4 3 --denominator 5
    python phase/verify_exact_phase_moment.py

后者核对五个完整方格位置公式、40 次不剪枝的端点相位积分、
四个严格例子及两次幺模基重标记。

## 文件完整性

SHA256SUMS 列出所有打包科学文件的字节散列。可在运行会覆盖 JSON 的复算命令之前执行：

    sha256sum -c SHA256SUMS

运行时间等字段重新生成后可能使 JSON 散列改变；这不等于数学端点发生变化。
精确依赖代码的独立散列仍会由各证书验证。

## 已有结果与探索性文件

triangle/ 下四个既有区间程序原样来自 C85 的不可变源码；
SOURCE_REFS.json 给出完整出处。C85 报告和证明仍是原库存桥接、旧三角积分、
密度函数及尾界的前件，本包不冒称重新证明全部先前基础。

smallarea/mellin_exploratory.json 及 explore_mellin_kernel.py 仅是路线探索，
未用于任何严格符号结论。早期 chordal_lower_certificate.json 是本轮中间进展，
最终应引用 doubled_face_certificate.json。

triangle/QT_CONTINUATION_CANDIDATE.md 若在包中，明确标为未纳入 C86 证书的续研候选。
当前完整常数证书仍对 \(8/3<A<4\) 使用 \(0\le Q_T\le\tau\)。

项目内交叉核对已经进行，外部同行复核尚未进行。研究保存与活动登记不自动授予正式定理接受或基础晋升。

