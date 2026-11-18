// PREFIX-886: independent half-orbit central-fiber census for odd residue ports.
// Exact 64-bit arithmetic, p=32 and q1,q2 in the stated high strip.
// Source: 2026-11-18_r6_prefix886_half_center_orbit_bit_index.md
#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
using namespace std;

constexpr uint64_t N = 1ULL << 32;

int64_t invmod(int64_t a, int64_t m) {
    if (m == 1) return 0;
    int64_t b = m, u = 1, v = 0;
    while (b) {
        int64_t t = a / b;
        a -= t * b; swap(a, b);
        u -= t * v; swap(u, v);
    }
    if (a != 1) return -1;
    return (u % m + m) % m;
}

uint64_t posmod(int64_t a, uint64_t m) {
    int64_t x = a % int64_t(m);
    return x < 0 ? x + m : x;
}

uint64_t centered(uint64_t q) {
    return ((N - 1) % q) * ((q + 1) / 2) % q;
}

int main() {
    uint64_t total = 0, odd = 0, cop = 0, cop_odd = 0;
    uint64_t low = 0, high = 0, high_odd = 0, max_cop = 0, max_n = 0;
    uint64_t hist[10000] = {};
    pair<uint64_t,uint64_t> max_pair{0,0};
    for (uint64_t q1=523001; q1<=524287; q1+=2) {
        uint64_t r1 = centered(q1);
        for (uint64_t q2=523001; q2<=524287; q2+=2) {
            ++total;
            uint64_t g = gcd(q1,q2), c = 0;
            if (g > 1) {
                uint64_t L = q1 * (q2/g), h = (N-1)/L;
                c = 2*((h+1)/2);
                if (g <= 63) ++low;
                else {++high; if ((c/2)&1) ++high_odd;}
            } else {
                ++cop;
                uint64_t r2=centered(q2);
                int64_t inv=invmod(q1,q2);
                if(inv < 0) return 3;
                uint64_t a=0;
                for (unsigned i=0;i<32;i++) {
                    uint64_t d=posmod(int64_t(r2)-int64_t(r1)-int64_t(1ULL<<i),q2);
                    uint64_t t=(d*uint64_t(inv))%q2;
                    uint64_t x=r1+q1*t;
                    if (x<N && ((x>>i)&1ULL)==0) ++a;
                }
                c=2*a;
                if (a&1) ++cop_odd;
                if (c>max_cop) {max_cop=c;max_n=1;max_pair={q1,q2};}
                else if (c==max_cop) ++max_n;
            }
            if(c>=10000) return 2;
            ++hist[c];
            odd+=(c/2)&1;
        }
    }
    if (total!=414736 || cop!=336462 || cop_odd!=59658 || odd!=61680 ||
        low!=75616 || high!=2658 || high_odd!=2022 ||
        max_cop!=8 || max_n!=54 || max_pair!=make_pair(523007ULL,524027ULL))
        return 1;
    cout << "total="<<total<<" odd="<<odd<<" gcd1="<<cop
         <<" gcd1odd="<<cop_odd<<" other_low="<<low
         <<" other_high="<<high<<" hi_odd="<<high_odd<<'\n';
    cout << "maxcop_cstar="<<max_cop<<" maxpair="<<max_pair.first<<","
         <<max_pair.second<<" max_n="<<max_n<<'\n';
    for (unsigned i=0;i<10000;i++) if(hist[i]) cout<<i<<":"<<hist[i]<<" ";
    cout<<'\n';
    return 0;
}
