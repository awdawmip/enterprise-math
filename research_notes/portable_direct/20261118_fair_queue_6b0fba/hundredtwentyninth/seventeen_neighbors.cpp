// First certificate: sorted-denominator DFS and adjacent buckets on a three-torus.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
#include "certificate.hpp"

namespace {
using Point = std::array<int, 6>;
constexpr int bins = 240;
constexpr int number_of_bins = bins * bins * bins;
std::vector<int> tail_cost;
std::vector<Point> columns, points;
std::vector<int> start(number_of_bins + 1), position;
int generated;
long long comparisons, close_pairs;

int modular_inverse(int a) {
    int answer = 1;
    for (int e = modulus - modulus / 17 - 1; e; e /= 2) {
        if (e % 2) answer = 1LL * answer * a % modulus;
        a = 1LL * a * a % modulus;
    }
    return answer;
}

Point character(int d) {
    int x = modular_inverse(d / 17);
    Point result{};
    for (int j = 0, power = x; j < 6; ++j) {
        for (int k = 0; k < 6; ++k) {
            result[k] = (result[k] + 1LL * weights[k][j] * power) % modulus;
        }
        power = 1LL * power * x % modulus;
    }
    return result;
}

int bucket(const Point& p) {
    int result = 0;
    for (int k = 0; k < 3; ++k) {
        result = result * bins + int(1LL * bins * p[k] / modulus);
    }
    return result;
}

void generate(int first, int left, const Point& p, bool store) {
    ++generated;
    const int k = bucket(p);
    if (store) points[position[k]++] = p;
    else ++start[k + 1];
    for (int i = first; i < int(tail_cost.size()) && tail_cost[i] <= left; ++i) {
        Point next = p;
        for (int j = 0; j < 6; ++j) {
            next[j] += columns[i][j];
            if (next[j] >= modulus) next[j] -= modulus;
        }
        generate(i, left - tail_cost[i], next, store);
    }
}

void compare(const Point& a, const Point& b) {
    ++comparisons;
    for (int j = 0; j < 6; ++j) {
        int dist = std::abs(a[j] - b[j]);
        if (std::min(dist, modulus - dist) >= exclusive_bound[j]) return;
    }
    ++close_pairs;
}

int wrap(int x) {
    if (x < 0) return x + bins;
    if (x >= bins) return x - bins;
    return x;
}
}

int main() {
    for (int d = 17; d <= budget + 1; d += 17) {
        if (divisor_grid % d || std::find(pivots, pivots + 6, d) != pivots + 6) continue;
        tail_cost.push_back(d - 1);
        columns.push_back(character(d));
    }
    assert(tail_cost.size() == 53);
    assert(1LL * bins * *std::max_element(exclusive_bound, exclusive_bound + 3) < modulus);
    generate(0, budget, {}, false);
    const int tails = generated;
    for (int k = 0; k < number_of_bins; ++k) start[k + 1] += start[k];
    points.resize(tails);
    position = start;
    generated = 0;
    generate(0, budget, {}, true);
    assert(generated == tails && tails == start.back());
    std::vector<int>().swap(position);
    for (int h = 0; h < number_of_bins; ++h) {
        if (start[h] == start[h + 1]) continue;
        int x = h / (bins * bins), y = h / bins % bins, z = h % bins;
        for (int dx = -1; dx <= 1; ++dx) {
            for (int dy = -1; dy <= 1; ++dy) {
                for (int dz = -1; dz <= 1; ++dz) {
                    int k = (wrap(x + dx) * bins + wrap(y + dy)) * bins + wrap(z + dz);
                    if (k < h) continue;
                    for (int i = start[h]; i < start[h + 1]; ++i) {
                        int first = k == h ? i + 1 : start[k];
                        for (int j = first; j < start[k + 1]; ++j) compare(points[i], points[j]);
                    }
                }
            }
        }
    }
    std::cout << "{\"tails\":" << tails << ",\"pairs\":" << comparisons
              << ",\"real_hits\":" << close_pairs << "}\n";
}
