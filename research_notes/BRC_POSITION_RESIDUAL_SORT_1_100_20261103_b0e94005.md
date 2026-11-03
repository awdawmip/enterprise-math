# 1～100 乱序排列的 BRC 保序残差与归位实现

Progress-Event-ID: brc-sort-20261103-b0e94005
At: 2026-11-03T07:56:48.824Z
Question: 一个打乱的 1 到 100 的数组，BRC 残差排序有没有实现方法？
Status: AUTHOR_DERIVATION_AND_EXECUTED_FINITE_CHECKS
Scope: 元素恰为 1..n、每值一次、允许任意两个数组位置交换；本例 n=100。
Research-Activity-ID: pending at capture; ordinary material preservation.
Registration request: https://github.com/awdawmip/kimi-query-bridge/issues/6649
Source snapshot: awdawmip/enterprise-math@01d7a2c0982291f7efec74931449e1ae0ac5e650
Global rules snapshot: awdawmip/chatgpt-global-knowledge@72721dbf9b9d9680ccac0b8cd268b023d1b54fbe
Contribution: current ChatGPT conversation plus a shared-context mathematical subagent; no independent-review claim.

## 1. 已有 BRC 接口及本轮应用

现有正权 BRC 载体为 (C,W,M)：支路数、总正质量、最大单支路质量。
支路归并为 (C+C', W+W', max(M,M'))，串联为分量相乘。
E=W/M，Delta=ln(E)；对 k 条单位权支路，(C,W,M)=(k,k,1)，E=k，Delta=ln(k)。

来源：
- [Weighted/Log Foundation](https://github.com/awdawmip/enterprise-math/blob/01d7a2c0982291f7efec74931449e1ae0ac5e650/definitions/ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md), sections 2, 5, 6.
- [Executable CWM module](https://github.com/awdawmip/enterprise-math/blob/01d7a2c0982291f7efec74931449e1ae0ac5e650/src/enterprise_math/brc_weighted.py).

本轮构造的对象是一个有限有向无环正权图：
源 S 向 v_1,...,v_n 各连一条权 1 的边；
再添加 v_1 -> v_2 -> ... -> v_n 的权 1 链。
共有 n+1 个顶点和 2n-1 条边。

到 v_k 的路径恰为 S -> v_j -> ... -> v_k，1<=j<=k。
它们按起始边区分，允许不同路径长度，每条路径质量 1。
故 C_k=W_k=k，M_k=1，E_k=k，Delta_k=ln k。
由 ln 的严格单调性，x<y 当且仅当 Delta_x<Delta_y。

输入数值 x 映射到 v_x；保序残差的精确读出 E_x=x 就是最终的 1-based 排名。
全部结点状态可用
S_0=(0,0,0),
S_k=edge(1) boxplus (S_(k-1) boxtimes edge(1))
递推，O(n) 次 CWM 运算，无需展开 n(n+1)/2 条路径。

这是现有 BRC 法则在已知连续整数域上的排序编码应用。
它把题设已知的整数次序编码到图中；全流程成本包含建图/聚合和数组归位。
本轮没有提出通用排序方法的新颖性或实际运行时间优于直接寻址的主张。

## 2. 位置残差及终止性

数组位置先按 1 起算。定义新的位置残差
r_i=E_(a_i)-i=a_i-i。
此 r_i 是本轮排序应用的错位坐标，Delta_k 则是前述 BRC 对数读出。

若 r_i!=0，令 j=i+r_i=a_i，交换 a_i 和 a_j。
交换后位置 j 的值为 j。
由于所有值唯一，j 原来若已经正确，就会与位置 i 上的 j 重复；
因此这次操作不会破坏原有正确位置，并至少新增一个正确位置。

F(a)=#{i:a_i!=i} 每次严格下降，算法必停，停时为 1..n。
若初始置换有 c 个循环（包括固定点），上述交换每次将一个非平凡循环拆出一个固定点；
循环数每次增加 1，终止时为 n，故交换次数恰为 n-c。
任意一次位置交换最多增加一个置换循环，因此这个交换数在允许任意位置交换的模型中也是最少的。
n=100 时最多 99 次。

保留的计算状态是带位置标签的排列，或等价的完整位置残差向量；
因为 a_i=i+r_i，该向量精确保留后续归位需要的信息。
F 只是进度观察量，不能单独生成下一步位置。
BRC 图的终点标签也始终保留；把所有数的状态汇总为一个标量会丢失排序地址。

残差指标检查：
对任何 1..n 的排列，sum_i r_i=0，不能用它判断归位完成。
[2,3,1] -> [3,2,1] 是合法交换；
两边 L1 残差均为 4，平方和为 6 -> 8。
因此本实现用错位数 F 的严格下降证明终止。

## 3. 直接执行项目现有 BRC 函数

以下函数原样来自上述固定源码版本，实际运行时使用它们构造 100 个 BRC 状态：
cwm_edge, cwm_propagate, cwm_recoalesce, effective_multiplicity。
为执行这几个函数，本次仅下载原样的 brc_weighted.py、brc_logarithm.py、
exact_arithmetic.py、core.py、division.py，并通过 Python namespace package 加载；
没有加载整库 __init__ 的无关导出。函数正文未改动。

```python
from enterprise_math.brc_weighted import (
    CWM_ZERO, cwm_edge, cwm_propagate, cwm_recoalesce,
    effective_multiplicity,
)

def brc_ranks(n):
    ranks = [0] * (n + 1)
    state = CWM_ZERO
    edge = cwm_edge(1)
    for k in range(1, n + 1):
        state = cwm_recoalesce(edge, cwm_propagate(state, edge))
        ratio = effective_multiplicity(state)
        # 本构造在每个 k 上都给出整数 E=k。
        ranks[k] = ratio.numerator
    return ranks

def brc_residual_sort(a, ranks):
    swaps = 0
    for i in range(len(a)):
        while ranks[a[i]] != i + 1:
            r = ranks[a[i]] - (i + 1)
            j = i + r
            a[i], a[j] = a[j], a[i]
            swaps += 1
    return swaps
```

实际验证对 k=1..100 逐个断言 count=k、total=k、dominant=1、
ratio.denominator=1。随后用 Python Random(20261103).shuffle 生成一份
1..100 排列，前十项为 [76,1,48,93,45,94,46,71,8,53]。
BRC 读出驱动的排序实际交换 95 次，完整输出等于 list(range(1,101))。

Reuse resolution: REUSE_EXECUTED.
Reused laws: WBRC-T01-CWM-SEMIRING, WBRC-T04-MULTIPLICITY-SURPLUS.
Type/observer scope: finite positive paths, endpoint-labeled CWM states, fixed unit-weight graph,
exact rational E readout; desired observations are ranks, sorted original array and swap trace.
Future operations are the declared array swaps; path-length/provenance-sensitive graph changes are not part of this input.

## 4. 消去已知建表结果后的实现

因为已经证明 E_x=x，可直接消去 ranks 表：

```python
def brc_residual_sort_inplace(a):
    """a 恰为 1..len(a) 的一个排列；原地升序，返回交换次数。"""
    swaps = 0
    for i in range(len(a)):
        while a[i] != i + 1:
            residual = a[i] - (i + 1)
            target = i + residual
            a[i], a[target] = a[target], a[i]
            swaps += 1
    return swaps
```

该等价 Python 实现实际运行了 [4,1,3,2]（2 次）及上述百元素样本（95 次）。
它直接移动原数组元素，不通过重新生成 1..n 代替排序。

在索引和数值以机器字表示的模型下：
- 显式 BRC ranks 版本：O(n) 建表、O(n) 归位，额外 O(n) 空间。
- 消去已知 E_x=x 的版本：O(n) 时间、O(1) 额外空间。
- 若另存结果数组，亦可 out[E_x-1]=x，O(n) 时间、O(n) 额外空间。
保留完整历史 trace 是另外的输出需求，计入其存储成本。

适用域来自题设：每个整数 1..n 恰好一次。
重复/缺失/一般键值的推广，需要给出相应目标秩或计数规则，并计入构造成本。

## 5. 已执行有限验证

由同上下文子代理在 functions.exec 中运行纯 JavaScript：
- 1..8 的全部 8!=40320 个排列：全部正确；每步 F 严格下降；交换数=8-c；最大交换数 7。
- 1000 个 1..100 排列：Fisher–Yates，xorshift32 seed=20261103，单一连续随机流。
  全部正确；每步 F 严格下降；交换数=100-c。
  交换次数最小 89、最大 99、平均 94.758。
- 特例：已排序 0；逆序 50；单 100 循环 [2,3,...,100,1] 为 99。
这些是执行证据；对全部 n 的结论由第 2 节的论证支持。

8 元素轨迹：
[4,1,7,3,8,2,6,5]
-> [3,1,7,4,8,2,6,5]
-> [7,1,3,4,8,2,6,5]
-> [6,1,3,4,8,2,7,5]
-> [2,1,3,4,8,6,7,5]
-> [1,2,3,4,8,6,7,5]
-> [1,2,3,4,5,6,7,8]。
1-based 交换依次为 (1,4),(1,3),(1,7),(1,6),(1,2),(5,8)；
F 为 8,7,6,5,4,2,0。

### 实验代码

以下保留实际 JavaScript 检查逻辑；functions.exec 中 text 为内置输出函数，
在 Node.js 中可设 const text=console.log。穷举和随机试验分次执行。

```javascript
function cycles(a) {
  let seen=new Set(), c=0;
  for(let i=0;i<a.length;i++){
    if(seen.has(i)) continue;
    c++; let j=i;
    while(!seen.has(j)){seen.add(j);j=a[j]-1;}
  }
  return c;
}
function sortChecked(input) {
  const a=input.slice();
  let swaps=0, oldF=a.reduce((s,x,i)=>s+Number(x!==i+1),0);
  for(let i=0;i<a.length;i++){
    while(a[i]!==i+1){
      const j=a[i]-1;
      [a[i],a[j]]=[a[j],a[i]];
      swaps++;
      const f=a.reduce((s,x,k)=>s+Number(x!==k+1),0);
      if(f>=oldF) throw Error("misplaced count did not decrease");
      oldF=f;
    }
  }
  if(a.some((x,i)=>x!==i+1)) throw Error("not sorted");
  if(swaps!==a.length-cycles(input)) throw Error("cycle count");
  return swaps;
}
let checked=0, maxSwaps=0;
function perms(a,k=0) {
  if(k===a.length){
    const s=sortChecked(a);
    checked++; maxSwaps=Math.max(maxSwaps,s);
    return;
  }
  for(let i=k;i<a.length;i++){
    [a[i],a[k]]=[a[k],a[i]];
    perms(a,k+1);
    [a[i],a[k]]=[a[k],a[i]];
  }
}
perms([1,2,3,4,5,6,7,8]);
text({checked,maxSwaps});
```

```javascript
// 与上段同一 sortChecked/cycles 检查逻辑。
let state=20261103;
function rnd(){
  state^=state<<13;
  state^=state>>>17;
  state^=state<<5;
  return (state>>>0)/4294967296;
}
const counts=[];
for(let t=0;t<1000;t++){
  const a=Array.from({length:100},(_,i)=>i+1);
  for(let i=99;i>0;i--){
    const j=Math.floor(rnd()*(i+1));
    [a[i],a[j]]=[a[j],a[i]];
  }
  counts.push(sortChecked(a));
}
const ordered=Array.from({length:100},(_,i)=>i+1);
text({
  passed:counts.length,
  minSwaps:Math.min(...counts),
  maxSwaps:Math.max(...counts),
  meanSwaps:counts.reduce((a,b)=>a+b,0)/counts.length,
  special:{
    already_sorted:sortChecked(ordered),
    reverse:sortChecked(ordered.slice().reverse()),
    single_100_cycle:sortChecked([...ordered.slice(1),1])
  }
});
```

## 6. 后续可检验问题

对未知非连续整数集合，如何从输入构造 BRC 保序读出，并将建秩、残差传播、
排序与恢复输出的总成本一起核算？
在已知有限值域但允许重复时，可先研究带多重性的目标区间和稳定归位规则。
本次用户问题的排列情形已给出具体实现、终止论证及执行证据；
这里的后续问题是可选研究方向，没有发布新任务或领取共享任务。
