// Exact parity-cut verification. The fixed-point stage only proves lower
// bounds; every inconclusive cut is checked with exact 256-bit integers.
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;
using W = uint64_t;
constexpr W scale = W(1) << 60;
struct Integer {
    array<W,4> limb{};
    Integer& operator+=(const Integer& other) {
        W carry=0;
        for (int i=0;i<4;++i) {
            __uint128_t sum=__uint128_t(limb[i])+other.limb[i]+carry;
            limb[i]=W(sum);carry=W(sum>>64);
        }
        if (carry) throw overflow_error("integer sum exceeds certified width");
        return *this;
    }
    friend Integer operator+(Integer a,const Integer& b) {return a+=b;}
    friend bool operator<(const Integer& a,const Integer& b) {
        for (int i=3;i>=0;--i) if(a.limb[i]!=b.limb[i]) return a.limb[i]<b.limb[i];
        return false;
    }
    friend bool operator==(const Integer& a,const Integer& b) {return a.limb==b.limb;}
    friend istream& operator>>(istream& in,Integer& a) {
        for (W& v:a.limb) in>>v;
        return in;
    }
};

int main() {
    int nf, nb;
    Integer denominator;
    cin >> nf >> nb >> denominator;
    vector<int> rhs(nf), type(nb);
    for (int& r : rhs) cin >> r;
    vector<array<W, 256>> lower(nb);
    vector<array<Integer, 256>> exact(nb);
    array<W, 4> totals{};
    for (int b = 0; b < nb; ++b) {
        cin >> type[b];
        array<Integer, 8> weights;
        array<W, 8> floors;
        for (int j = 0; j < 8; ++j) {
            cin >> weights[j] >> floors[j];
            if (denominator < weights[j] || floors[j] > scale) return 3;
        }
        lower[b][0] = 0;
        exact[b][0] = Integer{};
        for (int mask = 1; mask < 256; ++mask) {
            int j = countr_zero(unsigned(mask));
            int previous = mask & (mask - 1);
            lower[b][mask] = lower[b][previous] + floors[j];
            exact[b][mask] = exact[b][previous] + weights[j];
        }
        totals[type[b]] += lower[b][255];
    }
    vector<vector<uint8_t>> feature(nf, vector<uint8_t>(nb));
    for (auto& row : feature) for (auto& x : row) {
        unsigned v; cin >> v;
        if (v > 255) return 4;
        x = v;
    }
    if (!cin) return 5;
    W subsets = 0, cuts = 0, fallback = 0, tight = 0;
    vector<uint8_t> parity(nb);
    auto check = [&](int i, int j, int k) {
        array<W, 4> odd{};
        for (int b = 0; b < nb; ++b) {
            parity[b] = feature[i][b] ^ feature[j][b] ^ feature[k][b];
            odd[type[b]] += lower[b][parity[b]];
        }
        int need = 1 ^ rhs[i] ^ rhs[j] ^ rhs[k];
        ++subsets;
        // Prescribed type counts are (2,5,2,1).
        for (unsigned a = 0; a < 16; ++a) {
            if ((((a >> 1) ^ (a >> 3)) & 1) != unsigned(need)) continue;
            ++cuts;
            W bound = 0;
            for (int t = 0; t < 4; ++t)
                bound += ((a >> t) & 1) ? totals[t] - odd[t] : odd[t];
            if (bound >= scale) continue;
            ++fallback;
            Integer sum;
            for (int b = 0; b < nb; ++b) {
                int mask = parity[b] ^ (((a >> type[b]) & 1) ? 255 : 0);
                sum += exact[b][mask];
            }
            if (sum < denominator) {
                cout << "{\"verified\":false,\"features\":[" << i << ',' << j << ',' << k
                     << "],\"type_mask\":" << a << "}\n";
                return false;
            }
            tight += sum == denominator;
        }
        return true;
    };
    for (int i = 1; i < nf; ++i) if (!check(0, 0, i)) return 1;
    for (int i = 1; i < nf; ++i) for (int j = i + 1; j < nf; ++j)
        if (!check(0, i, j)) return 1;
    for (int i = 1; i < nf; ++i) for (int j = i + 1; j < nf; ++j)
        for (int k = j + 1; k < nf; ++k) if (!check(i, j, k)) return 1;
    // The empty point subset is included separately; all type assignments
    // with odd right side are also checked by this call.
    if (!check(0, 0, 0)) return 1;
    cout << "{\"verified\":true,\"indexed_subsets\":" << subsets
         << ",\"indexed_cuts\":" << cuts << ",\"exact_fallbacks\":" << fallback
         << ",\"tight_fallbacks\":" << tight << ",\"fixed_point_scale\":\""
         << scale << "\"}\n";
}
