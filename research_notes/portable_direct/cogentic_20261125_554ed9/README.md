# Cogentic 论文提取与进取数论接入资料包

本包围绕 Google Research 的 Cogentic 论文固定版本，提取可以用于进取数论的定理、公式、局部证明方法与可复算示例。原始版本提交日期为 **2026-11-25**，固定提交为：

`4a7bc8ab0bc770e71a259b7966c500496b99010a`

来源清单涵盖 **10 篇论文、389 页 PDF**。完整报告将原文主张、可独立使用的局部数学工具、本项目接入推导和有限计算证据分别注明。

## 阅读入口

优先阅读 [REPORT.md](REPORT.md)。它是本包的完整报告，包括十篇论文的筛选结果、重要公式、与当前研究的连接、复算结果及后续问题。

专题笔记提供更细的原文定位、假设与证明机制：

| 文件 | 内容 |
|---|---|
| [agents/factorization.md](agents/factorization.md) | 两篇整数分解论文；祖先约束保持、加权望远镜、子群指数饱和、Walsh 正性、误差与有理恢复 |
| [agents/algebra_structure.md](agents/algebra_structure.md) | 离散对数、低秩矩阵和图重构；关系采样、联合矩、代数结构与局部核对 |
| [agents/learning_games.md](agents/learning_games.md) | 学习与博弈相关五篇论文；差分与求和、压缩、近似与优化工具 |

## 来源与版本

[source_manifest.json](source_manifest.json) 逐篇记录原始仓库路径、固定提交、源 URL、Git blob SHA-1、PDF 字节数、SHA-256 和页数。

发布资料包不包含源 PDF、文本提取缓存或页面截图。需要查阅原文时，使用清单中的固定版本 URL；需要核对文件时，按清单中的哈希核验。清单的 `verified` 字段表示相应源文件已按版本和字节信息核对，不表示论文定理已经完成独立证明审查。

## 复算环境

四个核对脚本均使用 Python。实际运行环境为 **Python 3.12.14**；其中 `agents/check_learning_kernels.py` 还使用 **SymPy 1.14.0**，其余三个脚本只依赖 Python 标准库。

运行时使用 Python 3.10 或更新版本；本包的依赖文件固定本次实际使用的 SymPy 版本。以下命令在本包根目录执行：

```bash
python3 -m pip install -r requirements.txt
```

## 复算命令与结果文件

已有 JSON 保存了本次实际计算结果。以下命令会重新生成对应结果；脚本没有外部数据下载步骤，也不需要源 PDF。

```bash
python3 agents/factorization_checks.py > agents/factorization_checks.json
python3 agents/algebra_checks.py > agents/algebra_checks.json
python3 agents/check_learning_kernels.py
python3 verify_bridge_identities.py
```

| 脚本 | 输出方式 | 对应结果 |
|---|---|---|
| [agents/factorization_checks.py](agents/factorization_checks.py) | 将 JSON 写到标准输出；上面的命令将其保存 | [agents/factorization_checks.json](agents/factorization_checks.json) |
| [agents/algebra_checks.py](agents/algebra_checks.py) | 将 JSON 写到标准输出；上面的命令将其保存 | [agents/algebra_checks.json](agents/algebra_checks.json) |
| [agents/check_learning_kernels.py](agents/check_learning_kernels.py) | 自动写入脚本同目录的 JSON，同时打印结果 | [agents/check_learning_kernels.json](agents/check_learning_kernels.json) |
| [verify_bridge_identities.py](verify_bridge_identities.py) | 自动写入脚本同目录的同名 JSON，同时打印结果 | [verify_bridge_identities.json](verify_bridge_identities.json) |

各组核对的对象如下：

- **整数分解局部工具**：混合平滑权重的精确组合公式、隐藏平方根分支的 CRT 拆分比例、子群指数饱和示例、有限群上的非负 Fourier 卷积。
- **代数结构**：低阶矩相同而高阶观测不同的例子、布尔低秩结构恒等式、合数模数上的 Bezout 行变换、有限域关系采样的有限概率核对。
- **学习与博弈局部工具**：虚拟博弈论文中的平移、转置、差分与二项式求和核，使用精确有理数和符号计算。
- **本项目接入恒等式**：离散能量、Riesel 旧通道保持与布尔观测闭包的精确例子。

脚本内的断言用于核对指定的有限域、参数范围或恒等式。保持 Python 的普通执行模式即可；不要使用会跳过断言的 `python -O`。

## 数学结论的使用范围

**有限核验不等于主定理全审。** 本包保留每个结果的实际证据范围：

1. 原论文的全局复杂度或主定理，按照原文声明及其假设记录。
2. 能独立写出局部证明的公式和引理，在报告或专题笔记中说明证明与适用域。
3. 脚本给出的有限计算，只支持其实际覆盖的输入和参数。
4. 接入本项目的推导保留整数寄存器、观测映射、联合状态和误差预算；真实算术序列与待证明的统一估计仍按各自状态处理。

后续复用时，应同时阅读所用公式旁的假设与来源定位。源文件哈希、计算通过和论文主定理成立是不同的事实。

## 目录内容

`REPORT.md`、本说明、依赖文件、来源清单、三份专题笔记、四个核对脚本及其 JSON 结果构成可直接阅读和复算的完整资料包。

