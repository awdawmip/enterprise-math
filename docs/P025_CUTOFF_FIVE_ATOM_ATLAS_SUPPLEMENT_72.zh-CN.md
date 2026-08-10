# P025 补充 72 —— Cutoff-Five Prime-Power Atom Atlas 与其负边界

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
依赖：P025 补充 51、69、71  
Hard block：`NONE`

## 1. cutoff-five hard slice 只有十种无序 exponent types

Stage 71 证明：若某个 threshold-active cyclic orientation 满足

\[
H_i<5,
\]

则其两个 complementary blocks 必为

\[
\boxed{p^e,\quad q^f,\qquad e,f\in\{1,2,3,4\}.}
\]

由于 abc components 两两互素，两个 primes 不同。

若 active component 为 `c`，则

\[
N=p^e+q^f.
\]

若某个 side component active，则两个 complements 中包含另一 side 与 `c`，此时

\[
N=|p^e-q^f|.
\]

两种情形的 exact projective denominator 都是

\[
\boxed{K=eq+fp.}
\]

因此该 atom 在 threshold `T` 上激活恰好等价于

\[
\boxed{m(N)\ge T(eq+fp),}
\]

或

\[
\boxed{
\operatorname{rad}(N)\le\frac{N}{T(eq+fp)}.
}
\]

剩余难度已经全部集中到低指数 prime-power binomial sum/difference 的 radical 结构。

## 2. P025-T141 —— prime-prime shell 永远不能在 threshold 1 激活

取

\[
e=f=1.
\]

则 denominator 为

\[
K=p+q.
\]

对 sum orientation，

\[
N=p+q=K,
\]

但每个 `N>1` 都满足

\[
m(N)<N,
\]

所以

\[
m(N)<K.
\]

对 difference orientation，

\[
N=|p-q|<p+q=K,
\]

且

\[
m(N)\le N<K.
\]

因此

\[
\boxed{
(e,f)=(1,1)
\Longrightarrow
\text{threshold-one projective activation 不可能。}
}
\]

这也与 Stage 69 一致：两个 prime complements 保留了过多 squarefree structure，无法进入 activation layer。

## 3. P025-NB15 —— 其余每一个 exponent shell 都真实存在

Prime-prime shell 是**唯一**可以只凭 exponent data 全局删掉的无序 exponent pair。

对所有其它

\[
1\le e\le f\le4,
\qquad(e,f)\ne(1,1),
\]

都存在 primitive threshold-one activated triple。

精确 fixtures：

| exponent shell | primitive activated triple |
|---|---|
| `(1,2)` | `2 + 5^2 = 27` |
| `(1,3)` | `3 + 5^3 = 128` |
| `(1,4)` | `23 + 5^4 = 648` |
| `(2,2)` | `3^2 + 79^2 = 6250` |
| `(2,3)` | `5^3 + 19^2 = 486` |
| `(2,4)` | `7^2 + 576 = 5^4` |
| `(3,3)` | `2^3 + 1323 = 11^3` |
| `(3,4)` | `3^4 + 1250 = 11^3` |
| `(4,4)` | `2^4 + 14625 = 11^4` |

在 difference-mode 行中，两端显示的 prime powers 是 complements，中间整数是 active component。

每个 fixture 都满足

\[
m(N)\ge eq+fp.
\]

因此任何只读取 `(e,f)` 的 theorem 都无法继续排除这 9 个 shells 中的任何一个。

## 4. 同一个 exponent shell 内同时存在 activated 与 subunit states

甚至 surviving shell 本身也不能决定 activation。

比较两个 `(1,2)` sum atoms：

\[
2+5^2=27
\]

与

\[
2+3^2=11.
\]

前者有

\[
K=2\cdot2+5=9,
\qquad
m(27)=9,
\]

所以 c-oriented term 恰好到达 threshold one。

后者有

\[
K=2\cdot2+3=7,
\qquad
m(11)=1,
\]

仍处于 subunit。

因此

\[
\boxed{
(e,f)+\text{sum/difference mode}
\text{ 对 activation query 仍然不充分。}
}
\]

下一步必须引入 prime bases，或者任何足以决定 `p^e +/- q^f` radical 的信息。

## 5. 精度停止规则

Stage 72 给出一个非常具体的 **coordinate saturation** 样本。

从 low-capacity state 出发，补充 exponent precision 一直有用，直到 exact shell

\[
(e,f)\in\{1,2,3,4\}^2
\]

被知道。

但此时：

- `(1,1)` 已完全判定为 safe；
- 其它所有 shells 仍然是真正 mixed。

继续“提高 exponent 精度”已经不可能再帮助，因为 exponent coordinate 已经 exact。

下一种有用精度必须换坐标族：prime base、congruence class、binomial factorization 或直接 radical information。

因此不能把“任务仍未解决”自动等同于“沿当前坐标继续加精度”。

## 6. 与经典 Diophantine families 的关系

hard atom layer 归结为

\[
p^e+q^f=N
\]

或

\[
|p^e-q^f|=N,
\qquad e,f\le4,
\]

并附带 `N` 的 radical 相对于 linear cross-capacity `eq+fp` 异常小这一条件。

Prime-power Diophantine equations、binomial factorization、Catalan/Pillai-type problems、Zsigmondy phenomena 等均属于成熟前人数学。P025 后续应选择性导入这些工具，而不是把 atom family 本身宣称为新对象。

项目侧贡献只是从 projective activation 精确路由到这个有限 exponent atlas，并证明 exponent-only refinement 已经在此耗尽。

## 7. 可执行资产

新增：

- `src/enterprise_math/abc_projective_low_capacity_atoms.py`；
- `tests/test_abc_projective_low_capacity_atoms.py`。

可执行 atlas 核验 prime-prime impossibility，并为其它 9 个无序 shells 各保存一个 exact primitive activated fixture。

## 8. 下一前沿

Hard block 不存在。继续：

1. 对每个 shell 判断哪一种 prime-base congruence/factorization information 是最便宜的下一坐标；
2. 优先研究能由经典 binomial identities 或 Zsigmondy-type primitive-divisor results 给出 exact radical lower bound 的 shells；
3. 保留“exponent precision 已耗尽”的负结果，不再用更大的 prime-base 枚举冒充理论推进；
4. 把 `precision coordinate saturation -> switch coordinate family` 模式回流 A2/P023。
