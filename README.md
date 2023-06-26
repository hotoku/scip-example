# SCIPで2次計画を解いてみる

次のような最適化問題を考える。

変数は、 $$x[0], x[1], \ldots, x[n-1]$$

目標は、 $$x[0], x[1], \ldots, x[n-1]$$ の平均と分散の和を最小化すること、つまり、

$$
\mathrm{minimize}\ \frac{1}{n} \sum_{i=0}^{n-1}x[i]
+ \frac{1}{n} \sum_{i=0}^{n-1}x[i]^2
- \left( \frac{1}{n} \sum_{i=0}^{n-1}x[i] \right)^2
$$

別途与えられた定数の配列$$d[0], d[1], \ldots, d[n-1]$$に対して、次を満たす必要がある

$$
\sum_{i=1}^t x[i] \leq \sum_{i=1}^t d[i], t=0, 1, \ldots, n-1
$$
