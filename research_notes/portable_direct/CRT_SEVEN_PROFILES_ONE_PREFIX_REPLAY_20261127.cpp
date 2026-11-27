// Exact bitset spectra of the reduced seven-profile threshold domain.
#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <tuple>
#include <vector>

using Bits = std::uint64_t;
constexpr int WIDTH = 7;
constexpr unsigned FULL = (1u << WIDTH) - 1;
constexpr Bits GRID = (Bits{1} << (WIDTH * WIDTH)) - 1;

struct Profile {
    Bits mask;
    int transposed;
    int reversed_complement;
    unsigned row_changes;
    unsigned col_changes;
    unsigned rows_with_zero;
    unsigned cols_with_zero;
    unsigned rows_with_one;
    unsigned cols_with_one;
};

struct Counts {
    std::uint64_t corner_pairs = 0;
    std::uint64_t nested_triples = 0;
    std::uint64_t distinct_triples = 0;
    std::uint64_t orbits = 0;
    std::uint64_t slices = 0;
    std::uint64_t chords = 0;
    std::uint64_t literal_replays = 0;
};

void generate_masks(int row, int last_start, Bits mask, std::vector<Bits>& result) {
    if (row == WIDTH) {
        result.push_back(mask);
        return;
    }
    for (int start = 0; start <= last_start; ++start) {
        const Bits tail = FULL ^ ((1u << start) - 1);
        generate_masks(row + 1, start, mask | (tail << (row * WIDTH)), result);
    }
}

std::vector<Profile> profiles() {
    std::vector<Bits> masks;
    generate_masks(0, WIDTH, 0, masks);
    std::map<Bits, int> index;
    for (int i = 0; i < static_cast<int>(masks.size()); ++i) index[masks[i]] = i;
    if (index.size() != masks.size()) throw std::runtime_error("duplicate monotone mask");

    std::vector<Profile> result;
    for (Bits mask : masks) {
        Profile p{};
        p.mask = mask;
        Bits transpose = 0;
        Bits reverse_complement = 0;
        std::array<unsigned, WIDTH> rows{}, cols{};
        for (int i = 0; i < WIDTH; ++i) {
            for (int j = 0; j < WIDTH; ++j) {
                const int cell = i * WIDTH + j;
                if (mask & (Bits{1} << cell)) {
                    rows[i] |= 1u << j;
                    cols[j] |= 1u << i;
                    transpose |= Bits{1} << (j * WIDTH + i);
                } else {
                    reverse_complement |= Bits{1} << (WIDTH * WIDTH - 1 - cell);
                }
            }
        }
        p.transposed = index.at(transpose);
        p.reversed_complement = index.at(reverse_complement);
        for (int i = 0; i < WIDTH; ++i) {
            if (rows[i]) p.rows_with_one |= 1u << i;
            if (cols[i]) p.cols_with_one |= 1u << i;
            if (rows[i] != FULL) p.rows_with_zero |= 1u << i;
            if (cols[i] != FULL) p.cols_with_zero |= 1u << i;
            if (i > 0 && rows[i] != rows[i - 1]) p.row_changes |= 1u << (i - 1);
            if (i > 0 && cols[i] != cols[i - 1]) p.col_changes |= 1u << (i - 1);
        }
        result.push_back(p);
    }
    return result;
}

bool first_in_orbit(const std::vector<Profile>& data, int ai, int bi, int di) {
    const Profile& a = data[ai];
    const Profile& b = data[bi];
    const Profile& d = data[di];
    const auto id = std::tuple(ai, bi, di);
    return id <= std::tuple(a.transposed, b.transposed, d.transposed)
        && id <= std::tuple(d.reversed_complement, b.reversed_complement,
                            a.reversed_complement)
        && id <= std::tuple(data[d.reversed_complement].transposed,
                            data[b.reversed_complement].transposed,
                            data[a.reversed_complement].transposed);
}

Bits subset_spectrum(Bits carry, Bits prefix) {
    std::array<unsigned, WIDTH * WIDTH> shifts{};
    for (int i = 0; i < WIDTH * WIDTH; ++i) {
        shifts[i] = 8 * ((carry >> i) & 1u) + ((prefix >> i) & 1u);
    }
    std::array<Bits, FULL + 1> dp{};
    dp[0] = 1;
    for (unsigned used = 0; used < FULL; ++used) {
        const int start = WIDTH * std::popcount(used);
        unsigned available = FULL ^ used;
        while (available) {
            const int col = std::countr_zero(available);
            const unsigned bit = 1u << col;
            dp[used | bit] |= dp[used] << shifts[start + col];
            available ^= bit;
        }
    }
    return dp[FULL];
}

Bits literal_spectrum(Bits carry, Bits prefix) {
    std::array<int, WIDTH> column{};
    std::iota(column.begin(), column.end(), 0);
    Bits result = 0;
    do {
        Bits matching = 0;
        for (int row = 0; row < WIDTH; ++row) {
            matching |= Bits{1} << (row * WIDTH + column[row]);
        }
        const int e = std::popcount(matching & carry);
        const int p = std::popcount(matching & prefix);
        result |= Bits{1} << (8 * e + p);
    } while (std::next_permutation(column.begin(), column.end()));
    return result;
}

void check_spectrum(Bits observed, Counts& counts) {
    std::array<unsigned, WIDTH + 1> layer{};
    std::array<int, WIDTH + 1> low{}, high{};
    for (int e = 0; e <= WIDTH; ++e) {
        layer[e] = (observed >> (8 * e)) & 255;
        if (!layer[e]) continue;
        low[e] = std::countr_zero(layer[e]);
        high[e] = std::bit_width(layer[e]) - 1;
        if (std::popcount(layer[e]) != high[e] - low[e] + 1) {
            throw std::runtime_error("gap in integer carry layer");
        }
        ++counts.slices;
    }

    for (int a = 0; a <= WIDTH; ++a) {
        if (!layer[a]) continue;
        for (int b = a + 2; b <= WIDTH; ++b) {
            if (!layer[b]) continue;
            for (int e = a + 1; e < b; ++e) {
                const int denominator = b - a;
                const int lower = (b - e) * low[a] + (e - a) * low[b];
                const int upper = (b - e) * high[a] + (e - a) * high[b];
                if (!layer[e] || lower <= denominator * (low[e] - 1)
                    || upper >= denominator * (high[e] + 1)) {
                    throw std::runtime_error("a straddling chord exposes an integer gap");
                }
                ++counts.chords;
            }
        }
    }
}

int main() {
    const std::vector<Profile> data = profiles();
    const int size = static_cast<int>(data.size());
    Counts counts;
    for (int ai = 0; ai < size; ++ai) {
        const Profile& a = data[ai];
        for (int di = 0; di < size; ++di) {
            const Profile& d = data[di];
            if ((d.mask & ~a.mask) || (a.rows_with_zero & d.rows_with_one)
                || (a.cols_with_zero & d.cols_with_one)) continue;
            ++counts.corner_pairs;
            for (int bi = 0; bi < size; ++bi) {
                const Profile& b = data[bi];
                if ((d.mask & ~b.mask) || (b.mask & ~a.mask)) continue;
                ++counts.nested_triples;
                if ((a.row_changes | b.row_changes | d.row_changes) != (FULL >> 1)
                    || (a.col_changes | b.col_changes | d.col_changes) != (FULL >> 1)) continue;
                ++counts.distinct_triples;
                if (!first_in_orbit(data, ai, bi, di)) continue;
                const Bits prefix = GRID ^ a.mask ^ b.mask ^ d.mask;
                const Bits observed = subset_spectrum(b.mask, prefix);
                if (counts.orbits % 4096 == 0) {
                    if (observed != literal_spectrum(b.mask, prefix)) {
                        throw std::runtime_error("subset and literal spectra differ");
                    }
                    ++counts.literal_replays;
                }
                check_spectrum(observed, counts);
                ++counts.orbits;
            }
        }
    }
    std::cout << "{\"width\":" << WIDTH
              << ",\"monotone_masks\":" << size
              << ",\"corner_pairs\":" << counts.corner_pairs
              << ",\"span_compatible_triples\":" << counts.nested_triples
              << ",\"distinct_profile_triples\":" << counts.distinct_triples
              << ",\"orbit_representatives\":" << counts.orbits
              << ",\"subset_transitions\":" << counts.orbits * 448
              << ",\"integer_slices\":" << counts.slices
              << ",\"chord_checks\":" << counts.chords
              << ",\"literal_spectrum_replays\":" << counts.literal_replays
              << "}\n";
}
