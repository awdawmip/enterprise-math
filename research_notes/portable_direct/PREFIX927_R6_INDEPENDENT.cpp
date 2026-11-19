// PREFIX-927 independent C++17 exact enumeration; loop over (b,a), not Python's (b,k).
// Build: g++ -O3 -std=c++17 PREFIX927_R6_INDEPENDENT.cpp -o check
// Run: ./check sorted_ids.bin && sha256sum sorted_ids.bin
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <numeric>
#include <vector>
using namespace std;
static constexpr uint64_t N = 1ULL << 32;
static constexpr int QMIN = 262145, QMAX = 524287, M = 131072;

int64_t egcd(int64_t a, int64_t b, int64_t &x, int64_t &y) {
    if (!b) { x = 1; y = 0; return a; }
    int64_t u, v;
    int64_t g = egcd(b, a % b, u, v);
    x = v;
    y = u - (a / b) * v;
    return g;
}
int mod_inverse(int a, int b) {
    int64_t x, y;
    assert(egcd(a,b,x,y)==1);
    return int((x % b + b) % b);
}
int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "usage: %s sorted_ids.bin\n", argv[0]);
        return 1;
    }
    vector<int> special(QMAX + 1, 0);
    for (int b = QMIN; b <= QMAX; b += 2) {
        int64_t r = 2 % b;
        for (int d = 1; d < 32; ++d) {
            if (r == 1 || r == b-1) { special[b] = 1; break; }
            r = 2*r % b;
        }
    }
    auto outside = [&](int a, int b) {
        if (uint64_t(b) < 33*((N+a-1)/a) || uint64_t(a) < 33*((N+b-1)/b)) return false;
        if (uint64_t(a / gcd(a,b)) * b < N) return false;
        return !special[b];
    };
    auto code = [](int a, int b) -> uint64_t {
        return uint64_t((a-QMIN)/2)*M + (b-QMIN)/2;
    };
    array<vector<uint64_t>,4> by_bit;
    array<uint64_t,4> witnesses = {0,0,0,0};
    for (int b = 400001; b <= 400127; b += 2) {
        for (int a = QMIN; a <= QMAX; a += 2) {
            if (gcd(a,b) != 1) continue;
            int ia = mod_inverse(a,b);
            uint64_t cap = (N-1)/a;
            for (int i = 0; i < 4; ++i) {
                uint64_t h = 1ULL << i;
                for (int sign : {-1, 1}) {
                    uint64_t k = (sign == -1 ? (h*ia)%b : (b-(h*ia)%b)%b);
                    if (k == 0 || k > cap) continue;
                    uint64_t A = k*a;
                    if (A + (sign == 1 ? h : 0) >= N) continue;
                    assert((int64_t(A)+sign*int64_t(h)) % b == 0);
                    uint64_t x = sign == 1 ? h : 0, y = A+x;
                    assert(y < N && (y-x)%a == 0 && (y-(x^h))%b == 0);
                    ++witnesses[i];
                    if (outside(a,b)) by_bit[i].push_back(code(a,b));
                    if (outside(b,a)) by_bit[i].push_back(code(b,a));
                }
            }
        }
    }
    vector<uint64_t> combined;
    for (int i = 0; i < 4; ++i) {
        auto &v = by_bit[i];
        sort(v.begin(),v.end());
        v.erase(unique(v.begin(),v.end()),v.end());
        printf("bit%d witnesses=%llu outside=%zu\n",i,(unsigned long long)witnesses[i],v.size());
        combined.insert(combined.end(),v.begin(),v.end());
        sort(combined.begin(),combined.end());
        combined.erase(unique(combined.begin(),combined.end()),combined.end());
        printf("through_bit%d=%zu\n",i,combined.size());
    }
    FILE *f = fopen(argv[1],"wb");
    assert(f);
    for (uint64_t key : combined) {
        // Explicit little-endian output regardless of host byte order.
        unsigned char bytes[8];
        for (int i=0; i<8; ++i) bytes[i] = (key >> (8*i)) & 255;
        assert(fwrite(bytes,1,8,f)==8);
    }
    assert(fclose(f)==0);
    return 0;
}
