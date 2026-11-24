# 本轮单侧 Mellin 接口

研究身份：EM-DIRECT-E7808F / TASK_RESEARCH。活动：RA-0B92AAF774CA466C1C1BC38B。

## 文件

- PROOF.md：完整定义、量词、自足 Landau 引理、整数到连续的曲率桥、平滑显式公式、正负两侧各自的能量指数、真实骨架与匹配迁移边界。
- verify_mellin_interface.py：六项精确符号代数及 518 项向外区间曲率核验。
- mellin_interface_certificate.json：完整固定参数、所有曲率区间、验证结论与依赖散列。
- AUTHOR_CROSSCHECK.md：本轮共同作者的交叉核对记录；不是独立 Review。

## 复算

从包含 `replay.py`、`one_sided_mellin/` 与 `prior/` 的本包根目录执行：

~~~sh
python3 replay.py --branch one_sided_mellin --output /tmp/riemann-one-sided-mellin
~~~

证书写入 `/tmp/riemann-one-sided-mellin/next/one_sided_mellin/mellin_interface_certificate.json`。统一入口的 `--prior` 默认指向本包的 `prior/riemann_directed_local_20261124/`；依赖外置时可传入 `--prior /path/to/riemann_directed_local_20261124`。完整参数说明见本包根目录的 `REPLAY.md`。

程序使用 Python 标准库、SymPy，及前轮保留的纯向外整数区间模块，默认来源为 `prior/riemann_directed_local_20261124/prior/riemann_cumulative_haar_20261123/dependencies/certify_fast_harmonic_energy.py`。原分支脚本没有命令行参数，并依赖原研究目录关系；统一入口会把脚本、同版 `PROOF.md` 和区间模块按该关系复制到指定输出目录，再运行副本。

脚本没有网络访问，不生成或读取完整高精度 \(D,c,q\) 缓存，不调用零点表。其有限核验不能证明 RH，也不能代替 PROOF.md 的无界解析论证。

## 结果边界

证明的是条件等价与精确增长指数，并未证明 RH 或所需的单侧无界上界。辅助 \(Q\) 保留同一背景、Euler 常数和完整前缀；实际匹配道路须另外支付误差，固定 \(m=11\) 输入不能直接外推。全部整数窗口骨架已有指数证明，固定二进端点的骨架版本在本稿中不作声明。
