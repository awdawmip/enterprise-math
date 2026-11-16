# 复算 C73

在此目录下运行 `python3 reproduce.py`。实测 Python 3.12.14、SymPy 1.14.0、NumPy 2.3.5；四五块的代数主证书还提供纯 Python 版本。全部脚本都用整数、分数或有限域准确运算。运行器逐字节比对随包提供的参考输出。八块原观测的生成涉及大整数，最后一项耗时较长。

| 脚本 | 核对对象 |
|---|---|
| check_prefix.py | 8550 次中心、既约分子及最大公因数恒等式 |
| check_three_state.py | 三状态逐因子路径生成的三个尾比，逐个与整块递推对照；单独检查长隙的 2 进相合 |
| check_linear_landing.py | 两块有向端点宽度、异首落点配对必要式 |
| verify_fixed_h.py、check_fixed_h_gap.py | 原单项在三块的四个满秩证书、四个一阶系数、四种真实最短位置 |
| check_four_five.py、four_five_independent.py、audit_four_five.py | 四五块重数、模素数平方的雅可比复算，直接有理微分复核；记录更正后的库存层编号 |
| check_single.py、check_single_stock.py | 单项的行列式消元、截面代入及多库存校准恒等式 |
| radical_decoder.py | 从单项 $g$ 逐坐标比较公因数，再以准确 $g$ 回验所提安排。并列或回验失败时输出未决 |
| certify_two_single.py | 两个库存的全部原两块词，核验单项 $g$ 给定值对应的完整原像 |
| decode_two_blocks.py | 仅以库存及原两项读数求两块的全部形式中心解 |
| decode_one_preparation.py | 仅以库存和一项按库存选定的有理输入读数恢复两中心 |
| blind_center_decoder.py --full | 在一、二、三及八块用原两项读数解两中心，另以单项读数解中心比 |

每个库存均公开。验证程序中的生成器知道测试安排，反演函数只接收显式参数。形式中心检查可以在任意隙长上运行；它与观测的 2 进相合需要长隙条件。全部测试由作者运行。一般定理的背景引理及对照结果可按以下固定版本复核。

- [C63 原极小值的逐规模唯一性](https://github.com/awdawmip/enterprise-math/blob/de41b8cd9e6b0ea52345d5f669af924f9379318a/research_notes/divisor_extrema/20261111_c63_pointwise_minimum_and_fixed_inversion.md)
- [C68 固定模板的首库存分离](https://github.com/awdawmip/enterprise-math/blob/b33dad96447719460514b5f12e20f5010f6c06f6/research_notes/divisor_extrema/20261111_c68_deterministic_recovery/C68_RESEARCH_NOTE.md)
- [C69 实与 2 进读数的逼近](https://github.com/awdawmip/enterprise-math/blob/903c822b5f18c716fc2cf1fd2e0db9718ae9804b/research_notes/divisor_extrema/20261113_c69_fixed_stock_identification/arithmetic/MIXED_DENSITY.md) · [C69 同分支整数漂移计数](https://github.com/awdawmip/enterprise-math/blob/903c822b5f18c716fc2cf1fd2e0db9718ae9804b/research_notes/divisor_extrema/20261113_c69_fixed_stock_identification/arithmetic/SIXTH_DEPTH.md)
- [C70 两块原双读数的最终逐词单射](https://github.com/awdawmip/enterprise-math/blob/903c822b5f18c716fc2cf1fd2e0db9718ae9804b/research_notes/divisor_extrema/20261113_c70_fixed_stock_arithmetic/two/EVENTUAL_INJECTIVITY.md)
