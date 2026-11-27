# Riesel R₄ 三条必要素坐标阶族

2026-11-27 · 知情作者构造与整数校验 · 待项目独立评审

固定原 \(R_4\)、辞典 \(P\) 和严格真素因子覆盖。设 \(t=b-11\)。预算 \(b=11\) 取 \(j=0\)，预算 \(b\ge12\) 取任一个 \(1\le j\le t\)。则所有满足
\[
\operatorname{ord}_q(2)\in\{560\cdot2^j,\ 1680\cdot2^j,\ 5040\cdot2^j\}
\]
的奇素数 \(q\)，对根余数和未来轨迹判定均逐素数必要。可对任一漏掉 \(q\) 的模数构造余数相同、补全成本分别为 \(b,b+1\) 的两个正根。即使知道最高必要阶，逐素数支持仍保留了更低阶的信息。 [原十锚与任意预算二进细分](https://github.com/awdawmip/enterprise-math/blob/2ae5de00bf7e8f1e2571ef5666e95f82a25dc429/research_notes/portable_direct/riesel_r4_twelve_observer_lower_20261125/REPORT.md)

## 可选阶和二进叶

原十锚与 \(P\) 留下唯一孔 \(n=3488+5040z\)。每枚锚的私有指数在允许固定辅助类 246241 和整条 \(n\equiv3488\bmod560\) 后仍然私有。对于深度 \(j\) 的二进叶 \(z\equiv z_0\bmod 2^j\)，上述三种原阶都能用根余数 \(2^{-(3488+5040z_0)/2}\bmod q\) 实现。因为 \(\gcd(5040,\operatorname{ord}_q(2))\) 在 \(j\ge1\) 时恰留下相对期 \(2^j\)，在 \(j=0\) 时三者均整除 5040。全局命中仍在 \(n\equiv3488\bmod560\) 内。原固定坐标和十锚中没有素数占据这些阶，见下方复算。每一阶至少有一枚素数由 Bang–Zsigmondy 定理保证。

选择有 \(t+1\) 个叶的完整二叉分割，并把指定 \(q\) 放在深度 \(j\) 的一叶。另选两枚素数作为该叶两个深度 \(j+1\) 子叶的维修坐标，其相位放在两个根中。通常使用深度 \(t\) 的梳状树，深度 \(1,\ldots,t-1\) 各一叶，深度 \(t\) 两叶。在修补层已经有一叶或没有叶时，一阶一枚即可分配。细节如下。

- \(j\ne t-1\) 时，含维修坐标的每层最多三枚，直接用各层的三种阶。\(t=0\) 时只有根叶和两枚深度一的维修坐标。
- \(j=t-1\)、\(t\ge4\) 时，取深度 \(t-1\) 的梳状树并分裂其深度一的叶，得到 \(t+1\) 个叶。深度二恰有三叶，深度 \(t\) 只有维修坐标。
- \(t=2,j=1\) 时，梳状树在深度二有两叶，加入两枚维修坐标共需四枚。原阶 6720 有至少两枚可用素数。
- \(t=3,j=2\) 时，取全深度二的四叶树，维修坐标放到深度三。原阶 1120 有至少两枚可用素数。

各层的阶彼此不重合，分配时总可保留指定的 \(q\)，包括它位于同阶中有两枚的情形。

## 成本与必要性

开根激活 \(q\)，关根只把该坐标置零。锚仍各自被强制使用。二进叶或子叶上的算术级数都含有避开固定辅助类 246241 的指数，故每条未维修叶都必须使用其指定类。目标叶开时可用一枚、关时必须用两枚，成本分别为 \(10+(t+1)\) 和 \(10+t+2\)。精确排除其它竞争素数和同余拼接沿用原任意预算证明的有限目标阶界 \(6720\cdot2^{b-1}\)，在界内对所有其它自由素数共同置零。任意漏掉 \(q\) 的观察模数都能添加相同 CRT 余数，未来项也随之同余。

## 有限库存复算

把[预算 19 的归档复算包](https://github.com/awdawmip/enterprise-math/blob/660f791ed86d245524e32610ee73bbb65db38085/research_notes/portable_direct/riesel_r4_nineteen_sharp_20261125/reproduction.json)存为 \(\texttt{budget19.json}\)。固定旧坐标只需检查哪些候选阶整除 \(q-1\)。有 78 个不同的旧坐标和锚，15 个可整除的阶候选，零碰撞。阶 1120 在去掉 16824641 后的原始部分仍有 360 位，阶 6720 在去掉 16141441 后仍有 1513 位，故两阶各有第二枚可用素数。

~~~python
import json
from math import gcd, isqrt, prod
from pathlib import Path
import re

basis = json.loads(Path('budget19.json').read_text())['files']['basic-omission-high-bound.js']
fixed = list(map(int, re.findall(r'"(\d+)"', basis.splitlines()[1])))
anchors = [5,13,19,73,38737,487824887233,1009,21169,4278255361,394783681,246241]
old = set(fixed + anchors)

def exact_order(q, d):
    return pow(2,d,q) == 1 and all(
        pow(2,d//p,q) != 1 for p in (2,3,5,7) if d%p == 0
    )

checks = 0
for q in old:
    for multiplier in (1,3,9):
        d = 560*multiplier
        while (q-1)%d == 0:
            assert not exact_order(q,d)
            checks += 1
            d *= 2
assert (len(old), checks) == (78,15)

for d,q,bits in ((1120,16824641,360),(6720,16141441,1513)):
    assert all(q%k for k in range(2,isqrt(q)+1)) and exact_order(q,d)
    n = 2**d-1
    excluded = prod(2**(d//p)-1 for p in (2,3,5,7) if d%p == 0)*q
    while (factor := gcd(n,excluded)) > 1:
        n //= factor
    assert n > 1 and n.bit_length() == bits
~~~

这些阶族与统一最高阶相容。下一步可改变原锚留下的唯一孔，检验三族之外的坐标能否同样被强制。
