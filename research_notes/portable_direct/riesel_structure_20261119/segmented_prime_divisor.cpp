#include <algorithm>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

// Read an exact positive integer N from stdin and exhaust all primes up to B.
// The search stops at the first prime divisor, proving its minimality.
// The declared bound fits uint32; all arithmetic is exact integer arithmetic.
int main(int argc, char** argv) {
    if (argc != 2) return 2;
    const uint64_t bound = std::stoull(argv[1]);
    if (bound < 2 || bound > std::numeric_limits<uint32_t>::max()) return 2;
    std::string decimal;
    if (!(std::cin >> decimal)) return 2;
    std::vector<uint32_t> limbs(1, 0);
    for (char c : decimal) {
        if (c < '0' || c > '9') return 2;
        uint64_t carry = c - '0';
        for (uint32_t& limb : limbs) {
            const uint64_t value = static_cast<uint64_t>(limb) * 10 + carry;
            limb = static_cast<uint32_t>(value);
            carry = value >> 32;
        }
        if (carry) limbs.push_back(static_cast<uint32_t>(carry));
    }
    if (limbs.size() == 1 && limbs[0] < 2) return 2;
    auto remainder = [&](uint64_t p) {
        uint64_t r = 0;
        for (auto it = limbs.rbegin(); it != limbs.rend(); ++it)
            r = ((r << 32) | *it) % p;
        return r;
    };
    uint64_t root = 0;
    while ((root + 1) * (root + 1) <= bound) ++root;
    std::vector<uint8_t> small(root + 1, 1);
    small[0] = small[1] = 0;
    for (uint64_t p = 2; p <= root / p; ++p) {
        if (small[p]) for (uint64_t j = p * p; j <= root; j += p) small[j] = 0;
    }
    std::vector<uint32_t> base;
    for (uint64_t p = 2; p <= root; ++p) if (small[p]) base.push_back(p);
    constexpr uint64_t segment_size = 1000000;
    uint64_t count = 0, least = 0;
    const auto start = std::chrono::steady_clock::now();
    for (uint64_t lo = 2; lo <= bound && least == 0; lo += segment_size) {
        const uint64_t hi = std::min(bound + 1, lo + segment_size);
        std::vector<uint8_t> mark(hi - lo, 1);
        for (uint64_t p : base) {
            if (p * p >= hi) break;
            const uint64_t first = std::max(p * p, ((lo + p - 1) / p) * p);
            for (uint64_t j = first; j < hi; j += p) mark[j - lo] = 0;
        }
        for (uint64_t i = 0; i < mark.size(); ++i) {
            if (!mark[i]) continue;
            const uint64_t p = lo + i;
            ++count;
            if (remainder(p) == 0) { least = p; break; }
        }
    }
    const double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    std::cout << "{\"bound\":" << bound << ",\"primes_checked\":" << count
              << ",\"least_prime_divisor\":";
    if (least) std::cout << least; else std::cout << "null";
    std::cout << ",\"exhausted_bound\":" << (least ? "false" : "true")
              << ",\"seconds\":" << seconds << "}\n";
}
