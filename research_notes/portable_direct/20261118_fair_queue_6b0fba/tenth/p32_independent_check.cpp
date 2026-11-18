// Exhaust the coprime corner left by the circle-gap lower bound 63*N+2.
// Build: c++ -O3 -std=c++17 p32_independent_check.cpp -o /tmp/p32_check
// The 32-bit signed labels below always retain the originally named XOR bit.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <stdexcept>

using Integer = std::int64_t;
constexpr Integer N = Integer{1} << 32;
constexpr Integer max_modulus = (Integer{1} << 19) - 1;
constexpr Integer min_product = 63 * N + 2;

struct Label {
    Integer center;
    Integer bit;
    bool upward;
};

// Input is coprime; return the residue in [0,b).
Integer inverse_modulo(Integer a, Integer b) {
    Integer old_remainder = b, remainder = a % b;
    Integer old_coefficient = 0, coefficient = 1;
    while (remainder != 0) {
        const Integer quotient = old_remainder / remainder;
        const Integer next_remainder = old_remainder - quotient * remainder;
        const Integer next_coefficient = old_coefficient - quotient * coefficient;
        old_remainder = remainder;
        remainder = next_remainder;
        old_coefficient = coefficient;
        coefficient = next_coefficient;
    }
    if (old_remainder != 1) throw std::logic_error("noninvertible modulus");
    return (old_coefficient % b + b) % b;
}

// Centers are ordered left -> right by displacement gap on the CRT circle.
// Only compare different named bits, with zero used for a stationary track.
void verify_actual_collision(Integer a, Integer b, Label left, Label right, Integer gap) {
    const Integer right_base = (gap & left.bit) ? left.bit : 0;
    const Integer left_base = right_base + gap;
    if (left.bit == right.bit || (right_base & right.bit) || (left_base & left.bit))
        throw std::logic_error("invalid named-bit construction");
    const Integer x = left_base + (left.upward ? 0 : left.bit);
    const Integer y = left_base + (left.upward ? left.bit : 0);
    const Integer u = right_base + (right.upward ? 0 : right.bit);
    const Integer v = right_base + (right.upward ? right.bit : 0);
    if (std::min({x,y,u,v}) < 0 || std::max({x,y,u,v}) >= N ||
        (x ^ left.bit) != y || (u ^ right.bit) != v ||
        (x == u && y == v) || x % a != u % a || y % b != v % b)
        throw std::logic_error("invalid collision");
}

// No need to sort centers: every pair of different named bits is tested.
// Test indices in increasing order so the reported largest required bit is reproducible.
int smallest_sufficient_max_bit(Integer a, Integer b) {
    const Integer period = a * b;
    Integer residue = inverse_modulo(a, b);
    std::array<Label, 65> earlier{};
    int count = 1;  // The zero-initialized center encodes the zero step.
    for (int i = 0; i < 32; ++i) {
        const Integer bit = Integer{1} << i;
        const Integer up = a * residue;
        const std::array<Label, 2> current{{
            {up, bit, true}, {(period + bit - up) % period, bit, false}
        }};
        for (const Label here : current) {
            for (int j = 0; j < count; ++j) {
                const Label old = earlier[j];
                const Integer forward = (here.center - old.center + period) % period;
                if (forward < N - old.bit) {
                    verify_actual_collision(a, b, old, here, forward);
                    return i;
                }
                if (period - forward < N - here.bit) {
                    verify_actual_collision(a, b, here, old, period - forward);
                    return i;
                }
            }
        }
        for (const Label here : current) earlier[count++] = here;
        residue = (2 * residue) % b;
    }
    return 32;
}

int main() {
    Integer corner = 0, coprime = 0;
    std::array<Integer, 33> first_witness{};
    for (Integer a = (Integer{1} << 18) + 1; a <= max_modulus; a += 2) {
        Integer first_b = std::max(a, (min_product + a - 1) / a);
        if (first_b % 2 == 0) ++first_b;
        for (Integer b = first_b; b <= max_modulus; b += 2) {
            ++corner;
            if (std::gcd(a, b) != 1) continue;
            ++coprime;
            ++first_witness[smallest_sufficient_max_bit(a, b)];
        }
    }
    std::cout << "unordered_corner=" << corner << "\ncoprime=" << coprime << '\n';
    for (int i = 0; i < 32; ++i)
        std::cout << "first_witness_at_max_bit_" << i << '=' << first_witness[i] << '\n';
    std::cout << "no_collision_found=" << first_witness[32] << '\n';
    if (corner != 4217381 || coprime != 3418186 || first_witness[22] != 10 ||
        std::accumulate(first_witness.begin() + 23, first_witness.end(), Integer{0}) != 0)
        return 1;
}
