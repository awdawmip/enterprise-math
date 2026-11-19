// Second certificate: add all multiplicities of one new part at a time, then
// independently group with eight shifted partitions. The last id is a control.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <set>
#include <utility>
#include <vector>
#include "certificate.hpp"

namespace {
using Point = std::array<int, 6>;
constexpr int side = 128;
constexpr int box_count = side * side * side;

int inverse(int n) {
    // Extended Euclid, modulus is not prime.
    long long a = n, b = modulus, u = 1, v = 0;
    while (b) {
        long long q = a / b;
        long long r = a - q * b, w = u - q * v;
        a = b; b = r; u = v; v = w;
    }
    assert(a == 1);
    return int((u % modulus + modulus) % modulus);
}

Point read_column(int denominator) {
    int x = inverse(denominator / 17);
    Point out{};
    for (int i = 0; i < 6; ++i) {
        // Evaluate row polynomial by Horner, with zero constant term.
        for (int j = 5; j >= 0; --j) {
            out[i] = (1LL * x * (out[i] + weights[i][j])) % modulus;
        }
    }
    return out;
}

int label(const Point& a, int choice) {
    int out = 0;
    for (int j = 0; j < 3; ++j) {
        long long numerator = 2LL * side * a[j] + ((choice >> j) & 1) * modulus;
        int h = int(numerator / (2LL * modulus)) % side;
        out = out * side + h;
    }
    return out;
}

bool close(const Point& a, const Point& b) {
    for (int i = 0; i < 6; ++i) {
        int delta = std::abs(a[i] - b[i]);
        if (std::min(delta, modulus - delta) >= exclusive_bound[i]) return false;
    }
    return true;
}
}

int main() {
    std::vector<int> parts;
    for (int d = 17; d <= budget + 1; d += 17) {
        if (divisor_grid % d == 0 && std::find(pivots, pivots + 6, d) == pivots + 6) {
            parts.push_back(d);
        }
    }
    std::vector<int> sizes(budget + 1);
    sizes[0] = 1;
    for (int d : parts) {
        for (int t = d - 1; t <= budget; ++t) sizes[t] += sizes[t - (d - 1)];
    }
    int total = 0;
    for (int count : sizes) total += count;
    std::vector<Point> points;
    std::vector<int16_t> costs;
    points.reserve(total + 1); costs.reserve(total);
    points.push_back({}); costs.push_back(0);
    for (int d : parts) {
        Point increment = read_column(d);
        const int old_size = int(points.size());
        for (int i = 0; i < old_size; ++i) {
            if (costs[i] + d - 1 > budget) continue;
            Point next = points[i];
            for (int t = costs[i] + d - 1; t <= budget; t += d - 1) {
                for (int j = 0; j < 6; ++j) {
                    next[j] += increment[j];
                    if (next[j] >= modulus) next[j] -= modulus;
                }
                costs.push_back(t); points.push_back(next);
            }
        }
    }
    assert(total == int(points.size()));
    std::vector<int16_t>().swap(costs);
    const int control = total;
    points.push_back(read_column(17));
    assert(2LL * side * *std::max_element(exclusive_bound, exclusive_bound + 3) < modulus);
    std::vector<int> start(box_count + 1), slot, order(total + 1);
    std::set<std::pair<int,int>> real_hits, control_hits;
    long long comparisons = 0;
    for (int choice = 0; choice < 8; ++choice) {
        std::fill(start.begin(), start.end(), 0);
        for (const Point& p : points) ++start[label(p, choice) + 1];
        for (int k = 0; k < box_count; ++k) start[k + 1] += start[k];
        slot = start;
        for (int i = 0; i <= total; ++i) order[slot[label(points[i], choice)]++] = i;
        for (int k = 0; k < box_count; ++k) {
            for (int i = start[k]; i < start[k + 1]; ++i) {
                for (int j = i + 1; j < start[k + 1]; ++j) {
                    ++comparisons;
                    int a = order[i], b = order[j];
                    if (!close(points[a], points[b])) continue;
                    if (b == control) control_hits.emplace(a, b);
                    else real_hits.emplace(a, b);
                }
            }
        }
    }
    std::cout << "{\"tails\":" << total << ",\"pairs_with_repetition_and_control\":" << comparisons
              << ",\"real_hits\":" << real_hits.size() << ",\"control_hits\":" << control_hits.size()
              << ",\"empty_vs_control\":" << control_hits.count({0,control}) << "}\n";
}
