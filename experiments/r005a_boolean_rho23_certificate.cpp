#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <tuple>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

using i64 = std::int64_t;
using u64 = std::uint64_t;

static constexpr std::array<int, 9> P = {2, 3, 5, 7, 11, 13, 17, 19, 23};
static constexpr i64 Q = 223092870; // 23#
static constexpr i64 FORCED_BASE = 30030; // 2*3*5*7*11*13
static constexpr i64 RESIDUAL = 7429; // 17*19*23
static constexpr i64 CANDIDATE_GAP = 536;
static constexpr i64 CANDIDATE_SHIFT = 19399380; // 2*(Q/23)

static i64 cyclic_unit_gap(i64 modulus, const std::vector<int>& factors) {
    std::vector<unsigned char> unit(static_cast<std::size_t>(modulus), 1);
    for (int p : factors) {
        for (i64 n = 0; n < modulus; n += p) {
            unit[static_cast<std::size_t>(n)] = 0;
        }
    }
    i64 first = -1, prev = -1, best = 0;
    for (i64 n = 0; n < modulus; ++n) {
        if (!unit[static_cast<std::size_t>(n)]) continue;
        if (first < 0) first = n;
        if (prev >= 0) best = std::max(best, n - prev);
        prev = n;
    }
    assert(first >= 0);
    return std::max(best, modulus + first - prev);
}

struct UnitWheel {
    std::vector<u64> words;
    int last_bits;

    UnitWheel() {
        const std::size_t count = static_cast<std::size_t>((Q + 63) / 64);
        words.assign(count, ~u64{0});
        last_bits = static_cast<int>(Q - static_cast<i64>(count - 1) * 64);
        if (last_bits < 64) words.back() &= ((u64{1} << last_bits) - 1);
        words[0] &= ~u64{1};
        for (int p : P) {
            for (i64 n = 0; n < Q; n += p) {
                words[static_cast<std::size_t>(n >> 6)] &= ~(u64{1} << (n & 63));
            }
        }
    }

    inline u64 linear64(i64 pos) const {
        const std::size_t i = static_cast<std::size_t>(pos >> 6);
        const int off = static_cast<int>(pos & 63);
        if (off == 0) return words[i];
        return (words[i] >> off) | (words[i + 1] << (64 - off));
    }

    inline u64 cyclic64(i64 pos) const {
        if (pos + 64 <= Q) return linear64(pos);
        const int tail = static_cast<int>(Q - pos);
        const std::size_t i = static_cast<std::size_t>(pos >> 6);
        const int off = static_cast<int>(pos & 63);
        u64 lo = words[i] >> off;
        if (off + tail > 64 && i + 1 < words.size()) lo |= words[i + 1] << (64 - off);
        if (tail < 64) lo &= ((u64{1} << tail) - 1);
        const int need = 64 - tail;
        u64 hi = words[0];
        if (need < 64) hi &= ((u64{1} << need) - 1);
        return lo | (hi << tail);
    }

    // Exact for every cyclic separator gap >64. This is enough for the global
    // certificate because a witnessed gap of 536 is checked separately and any
    // challenger must exceed 536.
    i64 max_long_separator_gap(i64 d) const {
        d %= Q;
        if (d < 0) d += Q;
        assert(d != 0);

        bool seen_separator = false;
        i64 prefix_zeros = 0;
        i64 trailing_zeros = 0;
        i64 best_gap = 0;
        i64 shifted = d;

        for (std::size_t wi = 0; wi < words.size(); ++wi) {
            const int bits = (wi + 1 == words.size()) ? last_bits : 64;
            u64 a = words[wi];
            if (bits < 64) a &= ((u64{1} << bits) - 1);
            u64 b = cyclic64(shifted);
            if (bits < 64) b &= ((u64{1} << bits) - 1);
            const u64 separator = a ^ b;

            if (separator == 0) {
                trailing_zeros += bits;
                if (!seen_separator) prefix_zeros += bits;
            } else {
                const int lead = __builtin_ctzll(separator);
                const int high = 63 - __builtin_clzll(separator);
                const int suffix = bits - 1 - high;
                if (!seen_separator) {
                    prefix_zeros += lead;
                    seen_separator = true;
                } else {
                    best_gap = std::max(best_gap, trailing_zeros + lead + 1);
                }
                trailing_zeros = suffix;
            }
            shifted += 64;
            if (shifted >= Q) shifted %= Q;
        }

        assert(seen_separator);
        best_gap = std::max(best_gap, trailing_zeros + prefix_zeros + 1);
        return best_gap;
    }
};

static bool is_prime_small(int n) {
    if (n < 2) return false;
    for (int p : P) {
        if (p * p > n) break;
        if (n % p == 0) return n == p;
    }
    return true;
}

static bool steady_unit(i64 n) {
    for (int p : P) if (n % p == 0) return false;
    return true;
}

static bool steady_strike(i64 n) { return !steady_unit(n); }

static bool activation_defect(int n) {
    return n == 0 || is_prime_small(n);
}

static bool actual_strike(i64 n) {
    bool value = steady_strike(n);
    if (0 <= n && n <= 23 && activation_defect(static_cast<int>(n))) value = !value;
    return value;
}

static std::array<int, 4> extension_signature(int a, int b, int p, int delta) {
    assert(p == 2 || p == 3);
    std::array<int, 4> out = {-1, -1, -1, -1};
    for (int r = 0; r < p; ++r) {
        const int left_mask = (r != 0);
        const int right_mask = ((r + delta) % p != 0);
        out[static_cast<std::size_t>(r)] = (a * left_mask) ^ (b * right_mask);
    }
    return out;
}

int main() {
    std::vector<std::pair<int, i64>> caps;
    for (int p : P) {
        std::vector<int> factors;
        for (int r : P) if (r != p) factors.push_back(r);
        const i64 j = cyclic_unit_gap(Q / p, factors);
        caps.push_back({p, p * j});
    }
    const std::vector<std::pair<int, i64>> expected = {
        {2, 40}, {3, 60}, {5, 130}, {7, 182}, {11, 308},
        {13, 390}, {17, 578}, {19, 646}, {23, 782}
    };
    assert(caps == expected);

    i64 forced = 1;
    for (auto [p, cap] : caps) if (cap <= CANDIDATE_GAP) forced *= p;
    assert(forced == FORCED_BASE);
    assert(Q / forced == RESIDUAL);

    UnitWheel wheel;
    assert(wheel.max_long_separator_gap(CANDIDATE_SHIFT) == CANDIDATE_GAP);

    i64 residual_best = 0;
    i64 residual_best_d = 0;
#ifdef _OPENMP
#pragma omp parallel
    {
        i64 local_best = 0;
        i64 local_d = 0;
#pragma omp for schedule(dynamic, 8)
        for (i64 k = 1; k < RESIDUAL; ++k) {
            const i64 d = FORCED_BASE * k;
            const i64 gap = wheel.max_long_separator_gap(d);
            if (gap > local_best) { local_best = gap; local_d = d; }
        }
#pragma omp critical
        {
            if (local_best > residual_best) { residual_best = local_best; residual_best_d = local_d; }
        }
    }
#else
    for (i64 k = 1; k < RESIDUAL; ++k) {
        const i64 d = FORCED_BASE * k;
        const i64 gap = wheel.max_long_separator_gap(d);
        if (gap > residual_best) { residual_best = gap; residual_best_d = d; }
    }
#endif
    assert(residual_best == CANDIDATE_GAP);
    assert(residual_best_d != 0);
    const i64 rho23 = residual_best - 1;
    assert(rho23 == 535);

    i64 residual_ts_best = -1;
    i64 residual_ts_d = 0;
    int residual_ts_start = -1;
    int residual_ts_next_gap = -1;
    for (i64 k = 1; k < RESIDUAL; ++k) {
        const i64 d = FORCED_BASE * k;
        int last_mask_error = -1;
        for (int n = 0; n <= 23; ++n) {
            const bool separator = steady_strike(n) ^ steady_strike(n + d);
            if (separator != activation_defect(n)) last_mask_error = n;
        }
        const int start = last_mask_error + 1;
        if (start > 23) continue;

        int g = 1;
        while (g <= CANDIDATE_GAP && !(steady_strike(23 + g) ^ steady_strike(23 + g + d))) ++g;
        assert(g <= CANDIDATE_GAP);
        const i64 depth = 23 + g - start;
        if (depth > residual_ts_best) {
            residual_ts_best = depth;
            residual_ts_d = d;
            residual_ts_start = start;
            residual_ts_next_gap = g;
        }
    }
    assert(residual_ts_best == 213);
    assert(residual_ts_d == 9 * (Q / 23));
    assert(residual_ts_start == 20);
    assert(residual_ts_next_gap == 210);
    assert(23 + 390 < rho23 + 1);

    int tt_best = -1, tt_a = -1, tt_b = -1;
    for (int a = 0; a <= 23; ++a) {
        for (int b = a + 1; b <= 23; ++b) {
            int t = 0;
            while (t <= 600 && actual_strike(a + t) == actual_strike(b + t)) ++t;
            if (t > tt_best) { tt_best = t; tt_a = a; tt_b = b; }
        }
    }
    assert(tt_best == 15);
    assert(tt_a == 4 && tt_b == 10);
    assert(tt_best < rho23);

    const i64 full_actual_horizon = rho23;
    assert(full_actual_horizon == 535);

    for (int p : {2, 3}) {
        for (int delta = 0; delta < p; ++delta) {
            std::vector<std::array<int, 4>> signatures;
            for (auto [a, b] : {std::pair{0,0}, std::pair{0,1}, std::pair{1,0}, std::pair{1,1}}) {
                signatures.push_back(extension_signature(a, b, p, delta));
            }
            int distinct = 0;
            for (int i = 0; i < 4; ++i) {
                bool first = true;
                for (int j = 0; j < i; ++j) if (signatures[i] == signatures[j]) first = false;
                distinct += first;
            }
            assert(distinct == (delta == 0 ? 2 : 4));
        }
    }

    std::cout
        << "rho23_exact gap=" << residual_best
        << " rho=" << rho23
        << " candidate_d=" << CANDIDATE_SHIFT
        << " residual_ts_best=" << residual_ts_best
        << " tt_best=" << tt_best
        << " full_actual_H=" << full_actual_horizon
        << "\n";
}
