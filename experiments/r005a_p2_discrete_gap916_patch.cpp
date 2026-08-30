// R005-A p=2 discrete one-unit gap-916 seam verifier.
//
// This is a finite exact regression for the first prime-only seams beyond the
// continuous multiscale frontier.  It uses the standard deterministic
// Miller-Rabin base set for uint64_t inputs; all cofactor floor values here
// are < 2^64.
//
// Usage:
//   ./r005a_p2_discrete_gap916_patch <q> [j0] [j1]
//
// Large seams may be split into disjoint inclusive j-ranges.  Counts from
// those ranges add exactly.  The symbolic companion note explains why only
// floor-width 915 events need inspection in this phase.

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <vector>

#ifdef _OPENMP
#include <omp.h>
#endif

using u64 = std::uint64_t;
using u128 = __uint128_t;

static u64 mod_mul(u64 a, u64 b, u64 m) {
    return static_cast<u64>((u128)a * b % m);
}

static u64 mod_pow(u64 a, u64 d, u64 m) {
    u64 r = 1;
    while (d) {
        if (d & 1) r = mod_mul(r, a, m);
        a = mod_mul(a, a, m);
        d >>= 1;
    }
    return r;
}

static bool is_prime_u64(u64 n) {
    if (n < 2) return false;
    for (u64 p : {2ULL, 3ULL, 5ULL, 7ULL, 11ULL, 13ULL,
                  17ULL, 19ULL, 23ULL, 29ULL, 31ULL, 37ULL}) {
        if (n % p == 0) return n == p;
    }

    u64 d = n - 1;
    u64 s = 0;
    while ((d & 1) == 0) {
        d >>= 1;
        ++s;
    }

    // Deterministic for n < 2^64.
    for (u64 a : {2ULL, 325ULL, 9375ULL, 28178ULL,
                  450775ULL, 9780504ULL, 1795265022ULL}) {
        if (a % n == 0) continue;
        u64 x = mod_pow(a % n, d, n);
        if (x == 1 || x == n - 1) continue;
        bool composite = true;
        for (u64 r = 1; r < s; ++r) {
            x = mod_mul(x, x, n);
            if (x == n - 1) {
                composite = false;
                break;
            }
        }
        if (composite) return false;
    }
    return true;
}

static u64 isqrt_u128(u128 n) {
    long double approx = std::sqrt(static_cast<long double>(n));
    u64 x = static_cast<u64>(approx);
    while ((u128)x * x > n) --x;
    while ((u128)(x + 1) * (x + 1) <= n) ++x;
    return x;
}

static u64 ceil_sqrt_u128(u128 n) {
    u64 r = isqrt_u128(n);
    return (u128)r * r == n ? r : r + 1;
}

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "usage: " << argv[0] << " <q> [j0] [j1]\n";
        return 2;
    }

    const u64 q = std::strtoull(argv[1], nullptr, 10);
    const u128 P85 = (u128)10141231999636330906ULL * 10 + 9;
    const u64 GAP = 916;
    const u64 H = GAP / 2;  // 458
    const u64 Q = q * q;

    // First integer k at which the global e=1 resource x<P85 can fail.
    const u64 k_global_fail = ceil_sqrt_u128(P85 * q);

    // First integer k at which the q^2 interval has real width >= 916.
    const u64 k_q2_width = H * Q;

    if (k_global_fail >= k_q2_width) {
        std::cerr << "no seam for q=" << q << "\n";
        return 3;
    }

    // In the one-unit-deficit phase k=(H-1)Q+r = H Q-s.
    const u64 m = H - 1;
    const u64 r0 = k_global_fail - m * Q;
    if (r0 >= Q) {
        std::cerr << "q is outside the 915/916 one-unit seam regime\n";
        return 4;
    }
    const u64 s_max = Q - r0;
    const u64 j_max = static_cast<u64>((u128)s_max * s_max / Q);

    u64 j0 = argc > 2 ? std::strtoull(argv[2], nullptr, 10) : 0;
    u64 j1 = argc > 3 ? std::strtoull(argv[3], nullptr, 10) : j_max;
    if (j0 > j_max) {
        std::cerr << "j0 beyond j_max\n";
        return 5;
    }
    if (j1 > j_max) j1 = j_max;
    if (j1 < j0) {
        std::cerr << "empty j range\n";
        return 6;
    }

    unsigned long long events = 0;
    unsigned long long prime_floor_starts = 0;
    unsigned long long endpoint_pairs = 0;
    unsigned long long gap916_failures = 0;
    u64 first_bad_k = 0;
    u64 first_bad_floor = 0;

    #pragma omp parallel for schedule(dynamic, 20000) \
        reduction(+:events, prime_floor_starts, endpoint_pairs, gap916_failures)
    for (long long jj = static_cast<long long>(j0);
         jj <= static_cast<long long>(j1); ++jj) {
        const u64 j = static_cast<u64>(jj);
        const u128 multiple = (u128)j * Q;
        const u64 root = isqrt_u128(multiple);

        // At most root/root+1 can satisfy
        //   jQ <= s^2 < (j+1)Q,  s^2-jQ < 2s.
        for (u64 s : {root, root + 1}) {
            if (s < 1 || s > s_max) continue;
            const u128 ss = (u128)s * s;
            if (!(multiple <= ss && ss < (u128)(j + 1) * Q)) continue;
            if (ss - multiple >= (u128)2 * s) continue;

            const u64 k = H * Q - s;
            if (k < k_global_fail || k >= k_q2_width) continue;

            const u128 A = (u128)k * k;
            const u128 U = A + (u128)2 * k;
            const u64 floor_A = static_cast<u64>(A / Q);
            const u64 floor_U = static_cast<u64>(U / Q);

            // These are exactly the one-unit floor-deficit events.
            if (floor_U - floor_A != GAP - 1) {
                std::cerr << "internal floor-width mismatch\n";
                std::abort();
            }
            ++events;

            // If floor_A is composite, a previous prime lies <=floor_A-1,
            // and max gap 916 already puts the next prime inside floor_U.
            if (!is_prime_u64(floor_A)) continue;
            ++prime_floor_starts;

            // A failure is now possible only if floor_A starts an exact
            // consecutive-prime gap of length 916.
            if (!is_prime_u64(floor_A + GAP)) continue;
            ++endpoint_pairs;

            bool has_interior_prime = false;
            for (u64 n = floor_A + 2; n < floor_A + GAP; n += 2) {
                if (is_prime_u64(n)) {
                    has_interior_prime = true;
                    break;
                }
            }

            if (!has_interior_prime) {
                ++gap916_failures;
                #pragma omp critical
                {
                    if (first_bad_k == 0 || k < first_bad_k) {
                        first_bad_k = k;
                        first_bad_floor = floor_A;
                    }
                }
            }
        }
    }

    std::cout
        << "q=" << q
        << " k_global_fail=" << k_global_fail
        << " k_q2_width=" << k_q2_width
        << " j_max=" << j_max
        << " j0=" << j0
        << " j1=" << j1
        << " events_D915=" << events
        << " prime_floor_starts=" << prime_floor_starts
        << " endpoint_pairs_916=" << endpoint_pairs
        << " gap916_failures=" << gap916_failures
        << " first_bad_k=" << first_bad_k
        << " first_bad_floor=" << first_bad_floor
        << "\n";

    return gap916_failures == 0 ? 0 : 1;
}
