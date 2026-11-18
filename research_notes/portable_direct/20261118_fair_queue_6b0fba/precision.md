## P018 · 商根动作缺失时，最大的不可分辨区间有多长？

令整数 $r\ge2$，状态为 $0,\ldots,N$，动作读数为 $O_b(q)=\lfloor(q/b)^{1/r}\rfloor$。使用项目已经确定的唯一最小动作基，即所有不超过 $N$ 的正 $r$ 次幂自由数。写 $n=\kappa_r(n)t^r$，其中 $\kappa_r(n)$ 为幂自由核，$Q_r(x)$ 为不超过 $x$ 的幂自由正整数个数，$b_j^{(r)}$ 为第 $j$ 个。下述结果是从项目已有的相邻边界判据推出的独立研究结果。

### 纤维与极值公式

删去动作集合 $E$ 后，状态 $u<v$ 的剩余读数全部相同，当且仅当 $\{\kappa_r(n):u<n\le v\}\subset E$。各动作读数单调，而从 $n-1$ 到 $n$ 在最小基中只改变坐标 $\kappa_r(n)$。故所有纤维均为连续区间。不同剩余签名的总数恰为
$$
N+1-\sum_{b\in E}\left\lfloor(N/b)^{1/r}\right\rfloor .
$$
单删一个 $b$ 时恰有 $\lfloor(N/b)^{1/r}\rfloor$ 个二元纤维，其余均为单点，因为同核两正边界间距至少为 $b(2^r-1)$。

**平方根情形的精确最坏界（普通推导与有限穷举证书）。** 任意 $N,k\ge0$，删去至多 $k$ 个平方自由动作，最大的不可分辨纤维所含的**状态数**恰为
$$
\boxed{\min\{N+1,\ b_{k+1}^{(2)}\}}.
$$
从 0 开始的区间总能达到上界。例如 $k=6,N\ge9$ 时，擦除 $1,2,3,5,6,7$，状态 $0,\ldots,9$ 具有同一剩余签名。纤维大小可以超过 $k+1$。固定任意 $r\ge2$，同一公式对所有充分大的 $k$ 亦成立，阈值只依赖 $r$。

### 为什么初始区间给出极值

记 $D_r(u,L)=|\{\kappa_r(n):u<n\le u+L\}|$，其中 $L\ge1,u\ge0$ 为整数。初始区间有 $D_r(0,L)=Q_r(L)$。只须证明任意窗口至少出现同样多的不同核。

1. 当 $u\le L/(2^r-1)$ 时，每个幂自由 $b\le u$ 取 $t=\lfloor(u/b)^{1/r}\rfloor+1$，就有 $u<bt^r\le 2^ru\le u+L$。其余 $u<b\le u+L$ 的幂自由数自身就在窗中。因此 $D_r(u,L)=Q_r(u+L)$。
2. 固定常数 $C\ge2$，当 $L/(2^r-1)<u\le CL$ 时，取 $0<c<\min\{1/(2^r-1),((C+1)^{1/r}-C^{1/r})^r\}$。对 $b\le cL$，区间 $\big((u/b)^{1/r},((u+L)/b)^{1/r}\big]$ 长至少 1，因而每个如此小的幂自由数都另贡献一个核。加上窗口中的幂自由数，得到
$$
D_r(u,L)\ge Q_r(u+L)-Q_r(u)+Q_r(cL).
$$
由 $Q_r(x)=\sum_{d^r\le x}\mu(d)\lfloor x/d^r\rfloor=x/\zeta(r)+O_r(x^{1/r})$（截断余项按级数尾界估计），对固定 $r,C,c$，右侧比 $Q_r(L)$ 多 $cL/\zeta(r)+O_{r,C}(L^{1/r})$。
3. 当 $u>CL$ 时，同核 $b$ 的相邻正幂倍数若同时入窗，间距至少 $r b^{1/r}u^{1-1/r}$。令 $Y=L^r/(r^r u^{r-1})$。该核只有在 $b\le Y$ 时才可能重现，其超出首次的出现数至多 $(Y/b)^{1/r}$。对所有 $b\le Y$ 求和并用单调函数的积分上界估计，得到 $L-D_r(u,L)\le rY/(r-1)$。选 $C$ 使 $1-1/[r^{r-1}(r-1)C^{r-1}]>1/\zeta(r)$，对所有充分大的 $L$ 即有 $D_r(u,L)>Q_r(L)$。

这证明固定 $r$ 的长窗极值。取最大满足 $Q_r(L)\le k$ 的长度，即 $b_{k+1}^{(r)}-1$，再加上区间左端点并按 $N+1$ 截断，得到大 $k$ 结论。

### 平方根怎样覆盖全部窗口长度

在 $r=2$ 时，取 $C=2,c=1/10$，满足上式。远端 $u>2L$ 有 $D_2(u,L)>3L/4$，而 $Q_2(L)\le L-\lfloor L/4\rfloor=\lceil3L/4\rceil$，故所有长度均已覆盖。仅需检查 $L/3<u\le2L$ 的中段。

对整数 $x\ge1$ 有 $|Q_2(x)-x/\zeta(2)|\le2\sqrt{x}+1$：置 $m=\lfloor\sqrt{x}\rfloor$，舍入和级数尾项误差之和至多 $m+x/m\le2\sqrt{x}+1$。由于 $1/\zeta(2)>1/2$，第 2 步的下界减 $Q_2(L)$ 至少为 $L/20-9\sqrt L-5$，故 $L\ge40000$ 时成立。

有限证书有两项。令 $A(x)=10000Q_2(x)-6079x$。整数筛在 $0\le x\le120000$ 给出最小值 $-118324$（$x=80156$）、最大值 $157683$（$x=47523$）。于是 $920\le L\le40000$ 时，$10000[Q_2(u+L)-Q_2(u)+Q_2(\lfloor L/10\rfloor)-Q_2(L)]\ge6079\lfloor L/10\rfloor-552014>0$。最后 $1\le L\le919$ 的 704873 对中段 $(u,L)$ 逐个计算不同核数，最小余量 $D_2(u,L)-Q_2(L)=0$，负值数为 0。

以下是两项有限证书的复算代码如下。
```python
from math import isqrt

bound = 120000
kernel = [0] * (bound + 1)
counts = [0] * (bound + 1)
for b in range(1, bound + 1):
    if kernel[b] == 0:
        for t in range(1, isqrt(bound // b) + 1):
            kernel[b * t * t] = b
    counts[b] = counts[b - 1] + (kernel[b] == b)
diff = [10000 * counts[x] - 6079 * x for x in range(bound + 1)]
assert (min(diff), max(diff)) == (-118324, 157683)
checked = 0
for u in range(2 * 919 + 1):
    seen = set()
    for length in range(1, 920):
        seen.add(kernel[u + length])
        if length < 3 * u and u <= 2 * length:
            assert len(seen) >= counts[length]
            checked += 1
assert checked == 704873
```

另以直接求 $O_b$ 的整数定义独立核验 $r=2,3,4,5$、$N=64$ 的全部 8320 对 $u<v$，每对的签名汉明距离均等于窗口的不同核数。所有阶数的全长度极值是否同样由初始区间达到，仍留作 $r\ge3$ 的问题。以上适用完整最小基、失效动作标签已知的擦除模型。

项目依赖为指定快照的[相邻边界与最小动作基](https://github.com/awdawmip/enterprise-math/blob/7b32ae2ad9d1c13a13ff4668d1d218adda99390d/src/enterprise_math/p018_p023_power_free_action_basis.py)和[既有谱系说明](https://github.com/awdawmip/enterprise-math/blob/7b32ae2ad9d1c13a13ff4668d1d218adda99390d/docs/PRIOR_ART_P018_P023_POWER_FREE_ACTION_BASIS.zh-CN.md)。幂自由计数与 Möbius 反演沿用经典算术。
