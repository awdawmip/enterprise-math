// Pure uint64 numerical sorting: residual-aware square anchors and strong baselines.
// Build: g++ -std=c++20 -O3 -DNDEBUG -Wall -Wextra pure_bench.cpp -o pure_bench
// Every algorithm accepts only the array: family parameters are generation metadata.
// The benchmark includes input copy, all per-call allocations, full n-value output,
// and destruction. Generation, validation, and diagnostics are outside timing.
#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

using u32 = std::uint32_t;
using u64 = std::uint64_t;
using u128 = __uint128_t;
constexpr u64 MAX_VALUE = std::numeric_limits<u64>::max();
constexpr std::size_t COUNTER_CAP = 4 * 1024 * 1024;
constexpr std::size_t BUCKET_CAP = 65536;
constexpr unsigned RADIX_BITS = 10;
constexpr std::size_t RADIX_SIZE = 1u << RADIX_BITS;

void require(bool condition, const char* message) {
    if (!condition) throw std::runtime_error(message);
}

// Restoring integer square root, exact over the entire uint64 domain.
u64 exact_root(u64 x) {
    u64 result = 0, bit = u64(1) << 62;
    while (bit > x) bit >>= 2;
    while (bit) {
        if (x >= result + bit) {
            x -= result + bit;
            result = (result >> 1) + bit;
        } else result >>= 1;
        bit >>= 2;
    }
    return result;
}

// Independent root oracle for validation only.
u64 root_oracle(u64 x) {
    u64 low = 0, high = u64(1) << 32;
    while (low + 1 < high) {
        const u64 middle = low + (high - low) / 2;
        if (u128(middle) * middle <= x) low = middle;
        else high = middle;
    }
    return low;
}

// floor(2^64/d) gives a quotient underestimate of at most one for uint64 x.
// One exact remainder check repairs it. d==1 is handled without a reciprocal.
struct ExactDivider {
    u64 denominator, inverse;
    explicit ExactDivider(u64 d)
        : denominator(d), inverse(d > 1 ? u64((u128(1) << 64) / d) : 0) {}
    u64 operator()(u64 x) const {
        if (denominator == 1) return x;
        const u64 q = u64((u128(x) * inverse) >> 64);
        return q + (x - q * denominator >= denominator);
    }
};

enum Path : unsigned { TRIVIAL, STD_SORT, VALUE_RADIX, RANGE_COUNT, FREQUENCY,
    AFFINE_COUNT, AFFINE_RADIX, BRC_GRID, BRC_KEY_RADIX, BRC_VALUE_RADIX };
const char* path_name(Path p) {
    constexpr const char* names[] = {"trivial", "std_sort", "value_radix",
        "range_count", "frequency", "affine_count", "affine_radix", "brc_grid",
        "brc_key_radix", "brc_value_radix"};
    return names[p];
}
struct Stats {
    u64 roots = 0, predictions = 0, direct = 0, up = 0, down = 0;
    u64 fallback_elements = 0, failed_predictions = 0, quotient_calls = 0;
    u64 kspan = 0, rspan = 0, counter_cells = 0, auxiliary_vector_bytes = 0;
    u64 buckets = 0, radix_passes = 0;
    bool pilot_disabled = false, same_basin = false;
    Path path = TRIVIAL;
};

template<bool Collect>
void offset_radix_impl(std::vector<u64>& a, Stats* stats) {
    if (a.size() < 2) return;
    const auto bounds = std::minmax_element(a.begin(), a.end());
    const u64 low = *bounds.first, high = *bounds.second;
    if (low == high) return;
    const unsigned bits = std::bit_width(high - low);
    std::vector<u64> tmp(a.size());
    std::array<std::size_t, RADIX_SIZE> counts{};
    if constexpr (Collect) {
        stats->counter_cells = std::max<u64>(stats->counter_cells, RADIX_SIZE);
        stats->auxiliary_vector_bytes += tmp.capacity() * sizeof(u64);
        stats->radix_passes += (bits + RADIX_BITS - 1) / RADIX_BITS;
    }
    for (unsigned shift = 0; shift < bits; shift += RADIX_BITS) {
        counts.fill(0);
        for (u64 x : a) ++counts[((x - low) >> shift) & (RADIX_SIZE - 1)];
        std::size_t total = 0;
        for (auto& c : counts) { const auto n = c; c = total; total += n; }
        for (u64 x : a) tmp[counts[((x - low) >> shift) & (RADIX_SIZE - 1)]++] = x;
        a.swap(tmp);
    }
}
void offset_radix(std::vector<u64>& a, Stats* stats) {
    if (stats) { stats->path = VALUE_RADIX; offset_radix_impl<true>(a, stats); }
    else offset_radix_impl<false>(a, nullptr);
}
void standard_sort(std::vector<u64>& a, Stats* stats) {
    if (stats) stats->path = STD_SORT;
    std::sort(a.begin(), a.end());
}

template<bool Collect>
void dense_range_impl(std::vector<u64>& a, Stats* stats) {
    if (a.size() < 2) return;
    const auto bounds = std::minmax_element(a.begin(), a.end());
    const u64 low = *bounds.first, high = *bounds.second;
    if (low == high) return;
    const u128 span = u128(high) - low + 1;
    if (span > COUNTER_CAP) {
        if constexpr (Collect) stats->path = VALUE_RADIX;
        offset_radix_impl<Collect>(a, stats);
        return;
    }
    std::vector<std::size_t> counts(std::size_t(span), 0);
    if constexpr (Collect) {
        stats->path = RANGE_COUNT;
        stats->counter_cells = counts.size();
    }
    for (u64 x : a) ++counts[std::size_t(x - low)];
    auto out = a.begin();
    for (std::size_t i = 0; i < counts.size(); ++i)
        out = std::fill_n(out, counts[i], low + i);
}
void dense_range(std::vector<u64>& a, Stats* stats) {
    if (stats) dense_range_impl<true>(a, stats);
    else dense_range_impl<false>(a, nullptr);
}

void frequency_sort(std::vector<u64>& a, Stats* stats) {
    if (a.size() < 2) return;
    std::unordered_map<u64, std::size_t> counts;
    counts.reserve(std::min<std::size_t>(a.size(), 4096));
    for (u64 x : a) ++counts[x];
    std::vector<std::pair<u64, std::size_t>> keys(counts.begin(), counts.end());
    std::sort(keys.begin(), keys.end());
    auto out = a.begin();
    for (const auto& [x, n] : keys) out = std::fill_n(out, n, x);
    if (stats) {
        stats->path = FREQUENCY;
        stats->counter_cells = counts.size();
        stats->auxiliary_vector_bytes = keys.capacity() * sizeof(keys[0]);
        // Hash nodes/bucket allocation overhead is deliberately not called peak memory.
    }
}

// Both affine baselines learn per-bucket minima/maxima from the actual array.
// SquareScale=false: equal-width buckets derived solely from observed range and n.
// SquareScale=true: internally compute K=floor_sqrt(min), width=2K, centered bins.
// Neither gets the generating K/B/D or an external cluster map.
template<bool SquareScale, bool Collect>
void affine_impl(std::vector<u64>& a, Stats* stats) {
    if (a.size() < 2) return;
    const auto bounds = std::minmax_element(a.begin(), a.end());
    const u64 low = *bounds.first, high = *bounds.second;
    if (low == high) return;
    const u128 span = u128(high) - low + 1;
    u64 width = 0, center = 0;
    if constexpr (SquareScale) {
        const u64 k = exact_root(low);
        if constexpr (Collect) ++stats->roots;
        if (k) { width = 2 * k; center = k; }
    }
    if (!width) {
        const std::size_t desired = std::clamp<std::size_t>(a.size() / 32, 16, 4096);
        width = u64((span + desired - 1) / desired);
    }
    const u128 maximum_numerator = u128(high) - low + center;
    const u128 bucket_count = maximum_numerator / width + 1;
    if (bucket_count > BUCKET_CAP || maximum_numerator > MAX_VALUE) {
        if constexpr (Collect) stats->path = AFFINE_RADIX;
        offset_radix_impl<Collect>(a, stats);
        return;
    }
    const std::size_t qcount = std::size_t(bucket_count);
    const ExactDivider divide(width);
    std::vector<u64> minima(qcount, MAX_VALUE), maxima(qcount, 0);
    std::vector<std::size_t> offsets(qcount + 1, 0);
    for (u64 x : a) {
        const auto q = std::size_t(divide(x - low + center));
        minima[q] = std::min(minima[q], x);
        maxima[q] = std::max(maxima[q], x);
    }
    u128 cells = 0;
    for (std::size_t q = 0; q < qcount; ++q) {
        offsets[q] = std::size_t(cells);
        if (minima[q] != MAX_VALUE || maxima[q] == MAX_VALUE)
            cells += u128(maxima[q]) - minima[q] + 1;
        if (cells > COUNTER_CAP) break;
    }
    if constexpr (Collect) {
        stats->buckets = qcount;
        stats->quotient_calls += a.size();
        stats->auxiliary_vector_bytes = (minima.capacity() + maxima.capacity()) * sizeof(u64)
            + offsets.capacity() * sizeof(std::size_t);
    }
    const u128 density_budget = std::max<u128>(4096, u128(a.size()) * 8);
    if (cells > COUNTER_CAP || cells > density_budget) {
        if constexpr (Collect) stats->path = AFFINE_RADIX;
        offset_radix_impl<Collect>(a, stats);
        return;
    }
    offsets[qcount] = std::size_t(cells);
    std::vector<std::size_t> counts(std::size_t(cells), 0);
    for (u64 x : a) {
        const auto q = std::size_t(divide(x - low + center));
        ++counts[offsets[q] + std::size_t(x - minima[q])];
    }
    auto out = a.begin();
    for (std::size_t q = 0; q < qcount; ++q)
        for (std::size_t i = offsets[q]; i < offsets[q + 1]; ++i)
            out = std::fill_n(out, counts[i], minima[q] + (i - offsets[q]));
    if constexpr (Collect) {
        stats->path = AFFINE_COUNT;
        stats->counter_cells = counts.size();
        stats->quotient_calls += a.size();
    }
}
template<bool SquareScale>
void affine_sort(std::vector<u64>& a, Stats* stats) {
    if (stats) affine_impl<SquareScale, true>(a, stats);
    else affine_impl<SquareScale, false>(a, nullptr);
}

// Mode 0 = each exact root; Mode 1 = old square anchor + one correction;
// Mode 2 = residual-aware anchor with hardware integer division;
// Mode 3 = residual-aware anchor with exact reciprocal division.
// The first 16 predictions keep the anchor if >=12 succeed after <=1 correction.
// Every accepted candidate is exact; failure invokes exact integer root recovery.
template<int Mode, bool Collect>
void brc_impl(std::vector<u64>& a, Stats* stats) {
    if (a.size() < 2) return;
    u64 minimum = 0, maximum = 0, K = 0, origin = 0, denominator = 1;
    bool use_anchor = false, single = false;
    if constexpr (Mode > 0) {
        const auto bounds = std::minmax_element(a.begin(), a.end());
        minimum = *bounds.first; maximum = *bounds.second;
        if (minimum == maximum) {
            if constexpr (Collect) stats->direct = a.size();
            return;
        }
        K = exact_root(minimum);
        origin = Mode == 1 ? K * K : minimum;
        denominator = K ? 2 * K : 1;
        use_anchor = K != 0;
        single = u128(maximum) < u128(K + 1) * (K + 1);
        if constexpr (Collect) { ++stats->roots; stats->same_basin = single; }
    }
    const ExactDivider divide(denominator);
    std::vector<u32> roots(a.size());
    u64 kmin = MAX_VALUE, kmax = 0, rmin = MAX_VALUE, rmax = 0;
    unsigned probes = 0, successes = 0;
    for (std::size_t i = 0; i < a.size(); ++i) {
        const u64 x = a[i];
        u64 k = 0;
        if constexpr (Mode == 0) {
            k = exact_root(x);
            if constexpr (Collect) { ++stats->roots; ++stats->fallback_elements; }
        } else if (single || x == minimum) {
            k = K;
            if constexpr (Collect) ++stats->direct;
        } else if (use_anchor) {
            const u64 quotient = Mode == 3 ? divide(x - origin) : (x - origin) / denominator;
            const u64 candidate = K + quotient;
            const u128 square = u128(candidate) * candidate;
            bool accepted = true;
            if constexpr (Collect) { ++stats->predictions; ++stats->quotient_calls; }
            if (square <= x) {
                k = candidate;
                // For the residual-aware formula p >= true_root-1 globally.
                // For the old formula p >= true_root globally.
                if constexpr (Mode >= 2) {
                    if (x - u64(square) >= 2 * candidate + 1) {
                        ++k;
                        if constexpr (Collect) ++stats->up;
                    } else if constexpr (Collect) ++stats->direct;
                } else if constexpr (Collect) ++stats->direct;
            } else if (square - (u128(2) * candidate - 1) <= x) {
                k = candidate - 1;
                if constexpr (Collect) ++stats->down;
            } else {
                accepted = false;
                k = exact_root(x);
                if constexpr (Collect) {
                    ++stats->roots; ++stats->fallback_elements; ++stats->failed_predictions;
                }
            }
            if (probes < 16) {
                ++probes; successes += accepted;
                if (probes == 16 && successes < 12) {
                    use_anchor = false;
                    if constexpr (Collect) stats->pilot_disabled = true;
                }
            }
        } else {
            k = exact_root(x);
            if constexpr (Collect) { ++stats->roots; ++stats->fallback_elements; }
        }
        roots[i] = u32(k);
        const u64 residue = x - k * k;
        kmin = std::min(kmin, k); kmax = std::max(kmax, k);
        rmin = std::min(rmin, residue); rmax = std::max(rmax, residue);
    }
    const u64 B = kmax - kmin + 1, D = rmax - rmin + 1;
    const u128 cells = u128(B) * D;
    if constexpr (Collect) {
        stats->kspan = B; stats->rspan = D;
        stats->auxiliary_vector_bytes = roots.capacity() * sizeof(u32);
    }
    const u128 density_budget = std::max<u128>(4096, u128(a.size()) * 4);
    if (cells <= COUNTER_CAP && cells <= density_budget) {
        std::vector<std::size_t> counts(std::size_t(cells), 0);
        for (std::size_t i = 0; i < a.size(); ++i) {
            const u64 k = roots[i], r = a[i] - k * k;
            ++counts[std::size_t((k - kmin) * D + r - rmin)];
        }
        auto out = a.begin();
        for (u64 ki = 0; ki < B; ++ki) {
            const u64 k = kmin + ki;
            for (u64 ri = 0; ri < D; ++ri) {
                const auto count = counts[std::size_t(ki * D + ri)];
                // Empty grid cells need no reconstructed number; this also avoids
                // overflow for mathematically impossible (k,r) combinations.
                if (count) out = std::fill_n(out, count, k * k + rmin + ri);
            }
        }
        if constexpr (Collect) { stats->path = BRC_GRID; stats->counter_cells = u64(cells); }
        return;
    }
    const unsigned rbits = std::bit_width(D - 1), kbits = std::bit_width(B - 1);
    if (rbits + kbits > 64) {
        if constexpr (Collect) stats->path = BRC_VALUE_RADIX;
        offset_radix_impl<Collect>(a, stats);
        return;
    }
    const u64 rmask = rbits ? (u64(1) << rbits) - 1 : 0;
    for (std::size_t i = 0; i < a.size(); ++i) {
        const u64 k = roots[i], r = a[i] - k * k;
        a[i] = ((k - kmin) << rbits) | (r - rmin);
    }
    if constexpr (Collect) stats->path = BRC_KEY_RADIX;
    offset_radix_impl<Collect>(a, stats);
    for (auto& x : a) {
        const u64 k = (x >> rbits) + kmin;
        x = k * k + (x & rmask) + rmin;
    }
}
template<int Mode>
void brc_sort(std::vector<u64>& a, Stats* stats) {
    if (stats) brc_impl<Mode, true>(a, stats);
    else brc_impl<Mode, false>(a, nullptr);
}

struct Algorithm { const char* name; void (*run)(std::vector<u64>&, Stats*); };
const std::array<Algorithm, 10> algorithms{{
    {"std_sort", standard_sort}, {"offset_radix", offset_radix},
    {"range_count_or_radix", dense_range}, {"frequency_sort", frequency_sort},
    {"affine_range_local", affine_sort<false>}, {"affine_square_local", affine_sort<true>},
    {"brc_fullroot", brc_sort<0>}, {"brc_old_onecorrect", brc_sort<1>},
    {"brc_residual_div", brc_sort<2>}, {"brc_residual_recip", brc_sort<3>}
}};

u64 bounded(std::mt19937_64& rng, u64 bound) {
    if (!bound) return rng(); // Represents the full 2^64 domain.
    const u64 threshold = (u64(0) - bound) % bound;
    u64 x;
    do { x = rng(); } while (x < threshold);
    return x % bound;
}
enum FamilyKind { UNIFORM, SQUARE, JITTERED, UNIQUE_SQUARE, RESIDUE_ANCHOR7 };
struct Condition {
    std::string name;
    std::size_t n;
    FamilyKind kind;
    u64 K = 0, B = 0, D = 0, shift = 0, uniform_max = 0;
};
std::vector<Condition> conditions() {
    std::vector<Condition> out;
    auto uniform = [&](const char* name, u64 high, std::initializer_list<std::size_t> ns) {
        for (auto n : ns) out.push_back({name, n, UNIFORM, 0, 0, 0, 0, high});
    };
    auto square = [&](std::string name, u64 K, u64 B, u64 D, u64 shift,
                      FamilyKind kind, std::initializer_list<std::size_t> ns) {
        for (auto n : ns) out.push_back({name, n, kind, K, B, D, shift, 0});
    };
    uniform("uniform_1e6", 1000000, {100, 1000, 10000, 100000, 1000000});
    for (u64 shift : {0ull, 900ull, 1790ull})
        square("square900_s" + std::to_string(shift), 900, 20, 8, shift, SQUARE,
               {100, 10000, 100000});
    for (u64 shift : {0ull, 1999990ull})
        square("square1e6_s" + std::to_string(shift), 1000000, 20, 8, shift, SQUARE,
               {10000, 100000, 1000000});
    for (const auto& [B, D] : std::array<std::pair<u64, u64>, 5>{{
             {64, 8}, {256, 8}, {20, 64}, {64, 512}, {256, 512}}})
        square("square1e6_B" + std::to_string(B) + "_D" + std::to_string(D),
               1000000, B, D, 0, SQUARE, {100000});
    square("unique1e6_B256_D512", 1000000, 256, 512, 0, UNIQUE_SQUARE,
           {10000, 100000});
    square("jitter900_B20_D8", 900, 20, 8, 0, JITTERED, {10000, 100000});
    square("jitter1e6_B20_D8", 1000000, 20, 8, 0, JITTERED,
           {10000, 100000, 1000000});
    uniform("uniform_1e12", 1000000000000ull, {100, 10000, 100000});
    square("square3e9_B20_D8", 3000000000ull, 20, 8, 0, SQUARE, {100000});
    square("square900_B60_D8", 900, 60, 8, 0, SQUARE, {100000});
    square("square900_B20_D1801", 900, 20, 1801, 0, SQUARE, {100000});
    square("square900_anchor7", 900, 20, 8, 0, RESIDUE_ANCHOR7, {100000});
    return out;
}

std::vector<u64> make_data(const Condition& c, unsigned bank) {
    // No family name/offset in the seed: translation/jitter controls share labels.
    const u64 seed = 0xB0E9400520261107ull + u64(c.n) * 0x9e3779b97f4a7c15ull
        + u64(bank) * 0xD1B54A32D192ED03ull;
    std::mt19937_64 rng(seed);
    std::vector<u64> a(c.n);
    if (c.kind == UNIFORM) {
        for (auto& x : a) x = bounded(rng, c.uniform_max + 1);
        return a;
    }
    const u64 population = c.B * c.D;
    std::vector<u64> labels(c.n);
    if (c.kind == UNIQUE_SQUARE) {
        require(c.n <= population && std::has_single_bit(population), "unique family capacity");
        const u64 multiplier = bounded(rng, population) | 1;
        const u64 offset = bounded(rng, population);
        std::size_t used = 0;
        if (c.n) labels[used++] = 0;
        if (c.n > 1) labels[used++] = population - 1;
        for (u64 i = 0; used < c.n; ++i) {
            const u64 label = (multiplier * i + offset) & (population - 1);
            if (label && label != population - 1) labels[used++] = label;
        }
        std::shuffle(labels.begin(), labels.end(), rng);
    } else {
        for (auto& label : labels) {
            if (c.kind == RESIDUE_ANCHOR7) {
                const u64 q = bounded(rng, population - 7);
                label = q == 0 ? 7 : q + 7;
            } else label = bounded(rng, population);
        }
        // Fix observed endpoints in every paired bank, not only support endpoints.
        if (c.n) labels.front() = c.kind == RESIDUE_ANCHOR7 ? 7 : 0;
        if (c.n > 1) labels.back() = population - 1;
        if (c.kind == RESIDUE_ANCHOR7 && c.n > 2) labels[1] = c.D;
    }
    std::vector<std::int64_t> jitter(c.B, 0);
    if (c.kind == JITTERED) {
        std::mt19937_64 offsets(0x4A177E2ull);
        const u64 amplitude = c.K / 4;
        for (u64 j = 1; j + 1 < c.B; ++j)
            jitter[j] = std::int64_t(bounded(offsets, 2 * amplitude + 1))
                - std::int64_t(amplitude);
    }
    for (std::size_t i = 0; i < a.size(); ++i) {
        const u64 j = labels[i] / c.D, r = labels[i] % c.D, k = c.K + j;
        const __int128 value = __int128(k) * k + r + c.shift + jitter[j];
        require(value >= 0 && u128(value) <= MAX_VALUE, "generated value overflow");
        a[i] = u64(value);
    }
    return a;
}

u64 checked_arrays = 0;
void check_case(const std::vector<u64>& input) {
    auto expected = input;
    std::sort(expected.begin(), expected.end());
    for (const auto& algorithm : algorithms) {
        auto actual = input;
        Stats stats;
        algorithm.run(actual, &stats);
        if (actual != expected) throw std::runtime_error(std::string("instrumented mismatch: ") + algorithm.name);
        actual = input;
        algorithm.run(actual, nullptr);
        if (actual != expected) throw std::runtime_error(std::string("timed implementation mismatch: ") + algorithm.name);
    }
    ++checked_arrays;
}

void verify() {
    u64 root_points = 0, divider_points = 0;
    for (u64 x = 0; x <= 1000000; ++x) {
        require(exact_root(x) == root_oracle(x), "small root mismatch");
        ++root_points;
    }
    std::mt19937_64 rng(20261107);
    for (u64 k : {0ull, 1ull, 2ull, 900ull, 1000000ull, 2147483647ull,
                  3037000499ull, 4294967295ull}) {
        const u64 s = k * k;
        for (u64 x : {s, s ? s - 1 : 0, s + (s != MAX_VALUE)}) {
            require(exact_root(x) == root_oracle(x), "root boundary mismatch");
            ++root_points;
        }
    }
    for (unsigned i = 0; i < 10000; ++i) {
        const u64 x = rng();
        require(exact_root(x) == root_oracle(x), "wide root mismatch");
        ++root_points;
    }
    for (u64 d : std::array<u64, 10>{1, 2, 3, 6, 1800, 2000000,
                  6000000000ull, 8589934590ull, 9223372036854775808ull, MAX_VALUE}) {
        const ExactDivider divide(d);
        for (u64 x : std::array<u64, 5>{0, 1, d - 1, d, MAX_VALUE}) {
            require(divide(x) == x / d, "divider boundary mismatch");
            ++divider_points;
        }
        for (unsigned i = 0; i < 10000; ++i) {
            const u64 x = rng();
            require(divide(x) == x / d, "divider random mismatch");
            ++divider_points;
        }
    }
    for (unsigned len = 0; len <= 5; ++len) {
        const u64 number = u64(1) << (2 * len);
        for (u64 code = 0; code < number; ++code) {
            u64 q = code;
            std::vector<u64> a(len);
            for (auto& x : a) { constexpr u64 alphabet[] = {0, 1, 3, 4}; x = alphabet[q % 4]; q /= 4; }
            check_case(a);
        }
    }
    for (const auto& a : std::vector<std::vector<u64>>{
            {}, {MAX_VALUE}, {0, MAX_VALUE}, {1, MAX_VALUE}, {3, 4},
            {810007, 811801}, {0, 1, 4, 9, 16, 25},
            {MAX_VALUE, MAX_VALUE - 1, 18446744065119617025ull, 0, 1},
            {9223372036854775807ull, 9223372036854775808ull, 9223372036854775809ull},
            std::vector<u64>(100, 0), std::vector<u64>(100, MAX_VALUE)}) check_case(a);
    for (unsigned trial = 0; trial < 160; ++trial) {
        std::vector<u64> a(bounded(rng, 300));
        for (auto& x : a) x = trial % 3 == 0 ? bounded(rng, 1000001) : rng();
        check_case(a);
    }
    for (auto c : conditions()) {
        c.n = std::min<std::size_t>(c.n, 10000);
        check_case(make_data(c, 0));
    }
    for (unsigned bank = 0; bank < 8; ++bank) {
        const Condition base{"pair", 10000, SQUARE, 900, 20, 8, 0, 0};
        auto shifted = base, jittered = base;
        shifted.shift = 1790; jittered.kind = JITTERED;
        const auto a = make_data(base, bank), b = make_data(shifted, bank), j = make_data(jittered, bank);
        for (std::size_t i = 0; i < a.size(); ++i) require(b[i] - a[i] == 1790, "translation pairing");
        auto av = a, jv = j;
        std::sort(av.begin(), av.end()); std::sort(jv.begin(), jv.end());
        require(av.front() == jv.front() && av.back() == jv.back(), "jitter observed span");
        for (std::size_t i = 1; i < av.size(); ++i)
            require((av[i] == av[i - 1]) == (jv[i] == jv[i - 1]), "jitter multiplicities");
        for (std::size_t i = 0; i < a.size(); ++i) {
            const auto rank_a = std::lower_bound(av.begin(), av.end(), a[i]) - av.begin();
            const auto rank_j = std::lower_bound(jv.begin(), jv.end(), j[i]) - jv.begin();
            require(rank_a == rank_j, "jitter rank pairing");
        }
    }
    {
        std::vector<u64> a{810007, 811801}; Stats s;
        brc_sort<3>(a, &s); require(s.up == 1 && s.roots == 1, "upward witness route");
    }
    {
        Condition c{"unique", 100000, UNIQUE_SQUARE, 1000000, 256, 512, 0, 0};
        auto a = make_data(c, 0); std::sort(a.begin(), a.end());
        require(std::adjacent_find(a.begin(), a.end()) == a.end(), "unique generator duplicated a value");
        check_case(make_data(c, 0));
    }
    std::cout << "{\"result\":\"PASS\",\"domain\":\"full uint64\",\"value_bytes\":" << sizeof(u64)
              << ",\"root_points\":" << root_points << ",\"divider_points\":" << divider_points
              << ",\"verified_arrays\":" << checked_arrays << ",\"algorithms\":" << algorithms.size()
              << ",\"instrumented_and_timed_implementations_checked\":true"
              << ",\"paired_translation_and_jitter_banks_checked\":8,\"unique_100000_checked\":true}\n";
}

u64 observed = 0;
void consume(const std::vector<u64>& a) {
    asm volatile("" : : "g"(a.data()), "g"(a.size()) : "memory");
    if (!a.empty()) observed ^= a.front() + a[a.size() / 2] * 257 + a.back();
}
using Clock = std::chrono::steady_clock;
double timed(const Algorithm& algorithm, const std::vector<std::vector<u64>>& banks,
             std::size_t cycles, unsigned rotation) {
    const auto start = Clock::now();
    for (std::size_t c = 0; c < cycles; ++c)
        for (std::size_t b = 0; b < banks.size(); ++b) {
            std::vector<u64> work = banks[(b + rotation) % banks.size()];
            algorithm.run(work, nullptr);
            consume(work);
        }
    return std::chrono::duration<double>(Clock::now() - start).count();
}
double quantile(std::vector<double> x, double q) {
    std::sort(x.begin(), x.end());
    const double p = q * (x.size() - 1);
    const auto i = std::size_t(p);
    return x[i] + (x[std::min(i + 1, x.size() - 1)] - x[i]) * (p - i);
}

void benchmark(const std::string& path, std::size_t max_n, double target_seconds) {
    constexpr unsigned BANKS = 8, ROUNDS = 7;
    require(target_seconds > 0 && target_seconds <= 1, "target_seconds must be in (0,1]");
    std::ofstream file(path);
    require(bool(file), "cannot open benchmark output");
    file << "family,n,algorithm,value_bytes,banks,rounds,median_us,p10_us,p90_us,min_us,max_us,calls_per_round,"
         << "mean_distinct,mean_min,mean_max,mean_numeric_span,roots,predictions,direct_hits,up_corrections,down_corrections,"
         << "fallback_elements,failed_predictions,quotient_calls,kspan,rspan,counter_cells,auxiliary_vector_bytes,"
         << "buckets,radix_passes,pilot_disabled_fraction,same_basin_fraction,path,"
         << "round1_us,round2_us,round3_us,round4_us,round5_us,round6_us,round7_us\n";
    file << std::setprecision(12);
    u64 completed = 0, validated_banks = 0;
    for (const auto& condition : conditions()) {
        if (condition.n > max_n) continue;
        std::vector<std::vector<u64>> banks;
        for (unsigned b = 0; b < BANKS; ++b) banks.push_back(make_data(condition, b));
        std::array<std::vector<Stats>, algorithms.size()> diagnostics;
        long double distinct = 0, minima = 0, maxima = 0, spans = 0;
        for (const auto& input : banks) {
            auto expected = input; std::sort(expected.begin(), expected.end());
            minima += expected.front(); maxima += expected.back();
            spans += static_cast<long double>(u128(expected.back()) - expected.front() + 1);
            distinct += std::inner_product(expected.begin() + 1, expected.end(), expected.begin(),
                u64(1), std::plus<u64>(), std::not_equal_to<u64>());
            for (std::size_t ai = 0; ai < algorithms.size(); ++ai) {
                auto actual = input; Stats stats;
                algorithms[ai].run(actual, &stats);
                if (actual != expected) throw std::runtime_error("diagnostic mismatch " + condition.name + "/" + algorithms[ai].name);
                diagnostics[ai].push_back(stats);
                actual = input; algorithms[ai].run(actual, nullptr);
                if (actual != expected) throw std::runtime_error("timed implementation mismatch " + condition.name + "/" + algorithms[ai].name);
            }
            ++validated_banks;
        }
        std::array<std::size_t, algorithms.size()> cycles{};
        std::array<std::vector<double>, algorithms.size()> samples;
        for (std::size_t ai = 0; ai < algorithms.size(); ++ai) {
            const double one = timed(algorithms[ai], banks, 1, 0);
            cycles[ai] = std::clamp<std::size_t>(std::size_t(target_seconds / std::max(one, 1e-9) + 0.999), 1, 100000);
        }
        std::mt19937_64 order_rng(0xA164B0E94005ull + condition.n + completed * 31337);
        for (unsigned round = 0; round < ROUNDS; ++round) {
            std::array<std::size_t, algorithms.size()> order;
            std::iota(order.begin(), order.end(), 0);
            std::shuffle(order.begin(), order.end(), order_rng);
            for (auto ai : order)
                samples[ai].push_back(timed(algorithms[ai], banks, cycles[ai], round) * 1e6 / (cycles[ai] * BANKS));
        }
        for (std::size_t ai = 0; ai < algorithms.size(); ++ai) {
            const auto mean = [&](auto getter) {
                long double sum = 0;
                for (const auto& s : diagnostics[ai]) sum += getter(s);
                return sum / BANKS;
            };
            bool same_path = true;
            for (const auto& s : diagnostics[ai]) same_path &= s.path == diagnostics[ai].front().path;
            file << condition.name << ',' << condition.n << ',' << algorithms[ai].name
                 << ',' << sizeof(u64) << ',' << BANKS << ',' << ROUNDS
                 << ',' << quantile(samples[ai], .5) << ',' << quantile(samples[ai], .1)
                 << ',' << quantile(samples[ai], .9) << ',' << quantile(samples[ai], 0)
                 << ',' << quantile(samples[ai], 1) << ',' << cycles[ai] * BANKS
                 << ',' << distinct / BANKS << ',' << minima / BANKS << ',' << maxima / BANKS << ',' << spans / BANKS;
            for (auto member : {&Stats::roots, &Stats::predictions, &Stats::direct, &Stats::up, &Stats::down,
                    &Stats::fallback_elements, &Stats::failed_predictions, &Stats::quotient_calls,
                    &Stats::kspan, &Stats::rspan, &Stats::counter_cells, &Stats::auxiliary_vector_bytes,
                    &Stats::buckets, &Stats::radix_passes})
                file << ',' << mean([&](const Stats& s) { return s.*member; });
            file << ',' << mean([](const Stats& s) { return s.pilot_disabled; })
                 << ',' << mean([](const Stats& s) { return s.same_basin; })
                 << ',' << (same_path ? path_name(diagnostics[ai].front().path) : "mixed");
            for (double sample : samples[ai]) file << ',' << sample;
            file << '\n';
        }
        file.flush();
        ++completed;
        std::cerr << "completed pure " << condition.name << " n=" << condition.n << '\n';
    }
    std::cout << "{\"result\":\"PASS\",\"conditions\":" << completed
              << ",\"benchmark_rows\":" << completed * algorithms.size()
              << ",\"validated_input_banks\":" << validated_banks << ",\"banks\":" << BANKS
              << ",\"rounds\":" << ROUNDS << ",\"value_bytes\":" << sizeof(u64)
              << ",\"target_seconds\":" << target_seconds << ",\"observable_sink\":" << observed << "}\n";
}

int main(int argc, char** argv) {
    try {
        if (argc == 2 && std::string(argv[1]) == "--verify") verify();
        else if (argc >= 3 && std::string(argv[1]) == "--bench")
            benchmark(argv[2], argc > 3 ? std::stoull(argv[3]) : 1000000,
                      argc > 4 ? std::stod(argv[4]) : 0.012);
        else {
            std::cerr << "usage: pure_bench --verify | --bench output.csv [max_n=1000000] [target_seconds=0.012]\n";
            return 2;
        }
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return 1;
    }
}
