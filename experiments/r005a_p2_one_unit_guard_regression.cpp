#include <cassert>
#include <cstdint>
#include <iostream>
using u64 = std::uint64_t;
using u128 = __uint128_t;

static bool one_unit_whole_seam(u64 q, u64 k_global_fail) {
    const u64 G = 916;
    const u64 H = G / 2;
    const u64 Q = q * q;
    const u64 lower_band = (H - 1) * Q;
    const u64 upper_band = H * Q;
    if (k_global_fail < lower_band || k_global_fail >= upper_band) return false;
    const u64 r0 = k_global_fail - lower_band;
    const u64 s_max = Q - r0;
    return r0 < Q && (u128)2 * s_max <= Q;
}

int main() {
    assert(one_unit_whole_seam(78541ULL, 2822237591848ULL));
    assert(!one_unit_whole_seam(78553ULL, 2822453183434ULL));
    std::cout << "R005A one-unit guard regression passed\n";
}
