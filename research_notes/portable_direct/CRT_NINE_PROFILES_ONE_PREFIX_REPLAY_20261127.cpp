// Exhaustive nine-profile CRT unit spectra on the span-compatible domain.
#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <utility>

constexpr int N = 9;
constexpr int RADIX = N + 1;
constexpr unsigned FULL = (1u << N) - 1;
constexpr unsigned INTERIOR = FULL ^ 1u;
using Bits = std::uint64_t;
using Cuts = std::array<int, N>;
using Shifts = std::array<unsigned, N * N>;

struct Spectrum {
    Bits low = 0;
    Bits high = 0;

    bool operator==(const Spectrum&) const = default;

    void add_shifted(Spectrum source, unsigned shift) {
        low |= source.low << shift;
        high |= source.high << shift;
        if (shift) high |= source.low >> (64 - shift);
    }

    void add_bit(int bit) {
        if (bit < 64) low |= Bits{1} << bit;
        else high |= Bits{1} << (bit - 64);
    }

    unsigned carry_layer(int carry) const {
        const int shift = RADIX * carry;
        const Bits word = shift == 0 ? low : shift >= 64 ? high >> (shift - 64)
            : (low >> shift) | (high << (64 - shift));
        return static_cast<unsigned>(word & ((Bits{1} << RADIX) - 1));
    }
};

struct Parents {
    std::array<unsigned, N> set{};
    std::array<unsigned, N> cell{};
    int count = 0;
};

const auto PARENTS = [] {
    std::array<Parents, FULL + 1> result{};
    for (unsigned used = 1; used <= FULL; ++used) {
        auto& node = result[used];
        const int start = N * (std::popcount(used) - 1);
        unsigned columns = used;
        while (columns) {
            const int col = std::countr_zero(columns);
            const unsigned bit = 1u << col;
            node.set[node.count] = used ^ bit;
            node.cell[node.count] = start + col;
            ++node.count;
            columns ^= bit;
        }
    }
    return result;
}();

Spectrum subset_spectrum(const Shifts& shifts) {
    std::array<Bits, FULL + 1> low;
    std::array<Bits, FULL + 1> high;
    low[0] = 1;
    high[0] = 0;
    for (unsigned used = 1; used <= FULL; ++used) {
        const Parents& node = PARENTS[used];
        Spectrum sum;
        if (node.count <= 5) {
            for (int j = 0; j < node.count; ++j) {
                sum.low |= low[node.set[j]] << shifts[node.cell[j]];
            }
        } else {
            for (int j = 0; j < node.count; ++j) {
                sum.add_shifted({low[node.set[j]], high[node.set[j]]}, shifts[node.cell[j]]);
            }
        }
        low[used] = sum.low;
        high[used] = sum.high;
    }
    return {low[FULL], high[FULL]};
}

Shifts make_shifts(const Cuts& a, const Cuts& b, const Cuts& d) {
    Shifts shifts{};
    for (int row = 0; row < N; ++row) {
        for (int col = 0; col < N; ++col) {
            const bool carry = col >= b[row];
            const bool prefix = col < a[row] || (carry && col < d[row]);
            shifts[N * row + col] = RADIX * carry + prefix;
        }
    }
    return shifts;
}

Spectrum literal_spectrum(const Cuts& a, const Cuts& b, const Cuts& d) {
    std::array<int, N> permutation{};
    std::iota(permutation.begin(), permutation.end(), 0);
    Spectrum result;
    do {
        int e = 0;
        int p = 0;
        for (int row = 0; row < N; ++row) {
            const int col = permutation[row];
            e += col >= b[row];
            p += 1 + (col >= b[row]) - (col >= a[row]) - (col >= d[row]);
        }
        result.add_bit(RADIX * e + p);
    } while (std::next_permutation(permutation.begin(), permutation.end()));
    return result;
}

void word_fixtures() {
    for (const auto& [e, p] : {std::pair{6, 3}, std::pair{6, 4}, std::pair{9, 9}}) {
        Shifts shifts{};
        for (int row = 0; row < N; ++row) {
            for (int col = 0; col < N; ++col) {
                shifts[N * row + col] = RADIX * (row < e) + (row < p);
            }
        }
        Spectrum expected;
        expected.add_bit(RADIX * e + p);
        const Spectrum computed = subset_spectrum(shifts);
        if (computed != expected || computed.carry_layer(e) != (1u << p)) {
            throw std::runtime_error("two-word fixtures failed");
        }
    }
}

Cuts transpose(const Cuts& cut) {
    Cuts out{};
    for (int col = 0; col < N; ++col) {
        for (int row = 0; row < N; ++row) out[col] += cut[row] > col;
    }
    return out;
}

Cuts reverse_complement(const Cuts& cut) {
    Cuts out{};
    for (int row = 0; row < N; ++row) out[row] = N - cut[N - 1 - row];
    return out;
}

std::pair<int, int> hall_bounds(const Cuts& b) {
    int lower = 2 * N;
    int upper = 0;
    for (int row = 0; row < N; ++row) {
        const int value = row + 1 + b[row];
        lower = std::min(lower, value);
        upper = std::max(upper, value);
    }
    return {N + 1 - lower, 2 * N - upper};
}

struct Counts {
    std::uint64_t outer_pairs = 0;
    std::uint64_t outer_orbits = 0;
    std::uint64_t outer_orbits_in_shard = 0;
    std::uint64_t distinct_triples = 0;
    std::uint64_t triple_orbits = 0;
    std::uint64_t layer_checks = 0;
    std::uint64_t chord_checks = 0;
    std::uint64_t literal_checks = 0;
};

void check_spectrum(Spectrum result, const Cuts& middle, Counts& counts) {
    const auto [from, to] = hall_bounds(middle);
    std::array<int, N + 1> low{}, high{};
    for (int e = 0; e <= N; ++e) {
        const unsigned layer = result.carry_layer(e);
        if ((layer != 0) != (e >= from && e <= to)) {
            throw std::runtime_error("integer carry layers differ from Hall bounds");
        }
        if (!layer) continue;
        low[e] = std::countr_zero(layer);
        high[e] = std::bit_width(layer) - 1;
        if (std::popcount(layer) != high[e] - low[e] + 1) {
            throw std::runtime_error("prefix gap on carry layer " + std::to_string(e));
        }
        ++counts.layer_checks;
    }
    for (int a = from; a <= to; ++a) {
        for (int b = a + 2; b <= to; ++b) {
            for (int e = a + 1; e < b; ++e) {
                const int d = b - a;
                const int lower = (b - e) * low[a] + (e - a) * low[b];
                const int upper = (b - e) * high[a] + (e - a) * high[b];
                if (lower <= d * (low[e] - 1) || upper >= d * (high[e] + 1)) {
                    throw std::runtime_error("gap on chord from " + std::to_string(a)
                        + " to " + std::to_string(b) + " at " + std::to_string(e));
                }
                ++counts.chord_checks;
            }
        }
    }
}

void dump(const char* name, const Cuts& cuts) {
    std::cerr << name;
    for (int cut : cuts) std::cerr << ' ' << cut;
    std::cerr << '\n';
}

void dump(const char* name, Spectrum spectrum) {
    std::cerr << name << '\n';
    for (int e = 0; e <= N; ++e) {
        std::cerr << e << ':';
        const unsigned layer = spectrum.carry_layer(e);
        for (int p = 0; p <= N; ++p) if (layer & (1u << p)) std::cerr << ' ' << p;
        std::cerr << '\n';
    }
}

struct Scan {
    int shard;
    int shards;
    Counts counts;
    Cuts a{}, b{}, d{};

    void check_middle(unsigned stabilizers) {
        unsigned fixed = 1;
        if (stabilizers & 1u) {
            const Cuts image = transpose(b);
            if (b > image) return;
            fixed += b == image;
        }
        if (stabilizers & 2u) {
            const Cuts image = reverse_complement(b);
            if (b > image) return;
            fixed += b == image;
        }
        if (stabilizers & 4u) {
            const Cuts image = transpose(reverse_complement(b));
            if (b > image) return;
            fixed += b == image;
        }

        const Spectrum spectrum = subset_spectrum(make_shifts(a, b, d));
        try {
            if (counts.triple_orbits % 262144 == 0) {
                if (spectrum != literal_spectrum(a, b, d)) {
                    throw std::runtime_error("subset and literal spectra differ");
                }
                ++counts.literal_checks;
            }
            check_spectrum(spectrum, b, counts);
        } catch (const std::runtime_error& error) {
            std::cerr << "shard " << shard << ", orbit " << counts.triple_orbits
                      << ": " << error.what() << '\n';
            dump("A:", a);
            dump("B:", b);
            dump("D:", d);
            dump("subset", spectrum);
            dump("literal", literal_spectrum(a, b, d));
            throw;
        }
        ++counts.triple_orbits;
        counts.distinct_triples += 4 / fixed;
        if (counts.triple_orbits % 2000000 == 0) {
            std::cerr << "shard " << shard << ": " << counts.triple_orbits
                      << " orbits verified\n";
        }
    }

    void middle(int row, int ceiling, unsigned missing, unsigned stabilizers) {
        if (row == N) {
            if (!missing) check_middle(stabilizers);
            return;
        }
        int upper = std::min(ceiling, d[row]);
        if (row && a[row] == a[row - 1] && d[row] == d[row - 1]) {
            upper = std::min(upper, ceiling - 1);
        }
        const int required = missing ? static_cast<int>(std::bit_width(missing)) - 1 : 0;
        const int lower = std::max(a[row], required);
        for (int cut = lower; cut <= upper; ++cut) {
            const unsigned left = missing & ~(1u << cut);
            if (std::popcount(left) > N - 1 - row) continue;
            b[row] = cut;
            middle(row + 1, cut, left, stabilizers);
        }
    }

    void outer_pair() {
        ++counts.outer_pairs;
        const auto id = std::pair(a, d);
        const auto t = std::pair(transpose(a), transpose(d));
        const auto r = std::pair(reverse_complement(d), reverse_complement(a));
        const auto tr = std::pair(transpose(r.first), transpose(r.second));
        if (id > t || id > r || id > tr) return;
        const auto index = counts.outer_orbits++;
        if (index % static_cast<unsigned>(shards) != static_cast<unsigned>(shard)) return;
        ++counts.outer_orbits_in_shard;
        const unsigned stabilizers = (id == t) | (2u * (id == r)) | (4u * (id == tr));
        unsigned missing = INTERIOR;
        for (int row = 0; row < N; ++row) missing &= ~((1u << a[row]) | (1u << d[row]));
        middle(0, N, missing, stabilizers);
    }

    void last_outer(int row, int upper) {
        if (row == N) {
            outer_pair();
            return;
        }
        for (int cut = a[0]; cut <= upper; ++cut) {
            d[row] = cut;
            last_outer(row + 1, cut);
        }
    }

    void first_outer(int row, int upper) {
        if (row == N) {
            int first_d = 0;
            while (first_d < N && a[first_d] > 0) d[first_d++] = N;
            last_outer(first_d, N);
            return;
        }
        for (int cut = 0; cut <= upper; ++cut) {
            a[row] = cut;
            first_outer(row + 1, cut);
        }
    }
};

int main(int argc, char** argv) {
    try {
        int shard = 0;
        int shards = 1;
        if (argc == 3) {
            shard = std::stoi(argv[1]);
            shards = std::stoi(argv[2]);
        }
        if ((argc != 1 && argc != 3) || shard < 0 || shard >= shards) {
            throw std::runtime_error("usage: replay [shard-index shard-count]");
        }
        word_fixtures();
        Scan scan{shard, shards, {}};
        scan.first_outer(0, N);
        const Counts& c = scan.counts;
        std::cout << "{\"width\":" << N << ",\"shard\":" << shard << ",\"shards\":" << shards
                  << ",\"outer_pairs\":" << c.outer_pairs << ",\"outer_orbits\":" << c.outer_orbits
                  << ",\"outer_orbits_in_shard\":" << c.outer_orbits_in_shard
                  << ",\"distinct_profile_triples\":" << c.distinct_triples
                  << ",\"orbit_representatives\":" << c.triple_orbits
                  << ",\"subset_transitions\":" << c.triple_orbits * N * (1u << (N - 1))
                  << ",\"hall_bound_replays\":" << c.triple_orbits
                  << ",\"integer_layers\":" << c.layer_checks
                  << ",\"chord_checks\":" << c.chord_checks
                  << ",\"literal_spectrum_replays\":" << c.literal_checks
                  << ",\"word_fixtures\":3}\n";
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return EXIT_FAILURE;
    }
}
