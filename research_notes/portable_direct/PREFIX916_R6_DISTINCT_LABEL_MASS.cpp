#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
using U = std::uint64_t;
using I = std::int64_t;
using U128 = unsigned __int128;

static U bit_ones_below(U z, unsigned j) {
    const U h = U(1) << j, t = h << 1;
    return (z / t) * h + std::max<U>(0, z % t > h ? z % t - h : 0);
}
static U witness_count(unsigned p, U A, unsigned i, unsigned j, int eps, int eta) {
    assert(p >= 2 && p <= 32 && j < i && i < p && A > 0 && A < (U(1) << p));
    const U H = U(1) << i, T = H << 1, length = (U(1) << p) - A;
    const U q = length / T, rem = length % T;
    const U offset = (eps == -1 ? H : 0);
    const U u = rem <= offset ? 0 : std::min(H, rem - offset);
    const U d = bit_ones_below(A + u, j) - bit_ones_below(A, j);
    return q * (H / 2) + (eta == -1 ? d : u - d);
}
static std::string decimal(U128 v) {
    if (!v) return "0";
    std::string s;
    while (v > 0) {s.push_back(char('0' + v % 10));v /= 10;}
    std::reverse(s.begin(),s.end());return s;
}
struct Result { U128 mass = 0; U identities = 0, positive_identites = 0, max_witness_count = 0; };
static Result exact_family(unsigned p, U a, U b) {
    const U N = U(1) << p;
    Result r;
    for (U k = 1; k * a < N; ++k) {
        const U A = k * a;
        for (unsigned i = 1; i < p; ++i) {
            for (unsigned j = 0; j < i; ++j) {
                for (int eps : {-1,+1}) for (int eta : {-1,+1}) {
                    const I t = I(A) - I(eps) * I(U(1)<<i) + I(eta) * I(U(1)<<j);
                    if (t <= 0 || (U(t) % b != 0)) continue;
                    ++r.identities;
                    const U m = witness_count(p,A,i,j,eps,eta);
                    if (m) {
                        ++r.positive_identites;
                        r.mass += U128(m);
                        r.max_witness_count = std::max(r.max_witness_count,m);
                    }
                }
            }
        }
    }
    return r;
}

// Independent parameter traversal: terminal gap ell*b first, then solve A=k*a.
// Only positive-multiplicity families matter; valid final endpoint separation < N.
static Result exact_family_terminal_first(unsigned p,U a,U b) {
    const U N=U(1)<<p;
    Result r;
    for(U ell=1;ell*b<N;++ell) {
        const U B=ell*b;
        for(unsigned i=1;i<p;++i)for(unsigned j=0;j<i;++j) {
            for(int eps : {-1,+1})for(int eta : {-1,+1}) {
                const I A0=I(B) + I(eps)*I(U(1)<<i) - I(eta)*I(U(1)<<j);
                if(A0<=0 || U(A0)>=N || (U(A0)%a!=0)) continue;
                const U m=witness_count(p,U(A0),i,j,eps,eta);
                ++r.identities;
                if(m) {
                    ++r.positive_identites;
                    r.mass+=U128(m);
                    r.max_witness_count=std::max(r.max_witness_count,m);
                }
            }
        }
    }
    return r;
}

static U brute_mass(unsigned p,U a,U b) {
    const U N=U(1)<<p;
    U ans=0;
    for(U x=0;x<N;++x)for(U y=x+1;y<N;++y) {
        if ((y-x)%a) continue;
        for(unsigned i=1;i<p;++i)for(unsigned j=0;j<i;++j) {
            const U u=x^(U(1)<<i), v=y^(U(1)<<j);
            if (v>u && ((v-u)%b==0)) ++ans;
        }
    }
    return ans;
}
int main(){
    U small_tests=0;
    for(unsigned p=2;p<=7;++p) {
        const U N=U(1)<<p;
        for(U a=1;a<N&&a<=15;a+=2)for(U b=1;b<N&&b<=15;b+=2) {
            const Result r=exact_family(p,a,b);
            const U direct=brute_mass(p,a,b);
            assert(r.mass==direct);
            ++small_tests;
        }
    }
    const Result r=exact_family(32,321651,440665);
    const Result r2=exact_family_terminal_first(32,321651,440665);
    assert(r2.mass==r.mass && r2.positive_identites==r.positive_identites);
    std::cout << "small_p_2_to_7_observer_tests=" << small_tests << "\n"
              << "small_p_mismatches=0\n"
              << "pair_a=321651 pair_b=440665\n"
              << "all_signed_index_role_identity_count=" << r.identities << "\n"
              << "identity_with_positive_witness_count=" << r.positive_identites << "\n"
              << "max_per_identity=" << r.max_witness_count << "\n"
              << "exact_distinct_labeled_pair_mass=" << decimal(r.mass) << "\n"
              << "independent_terminal_first_mass=" << decimal(r2.mass) << "\n"
              << "independent_terminal_first_positive_identities=" << r2.positive_identites << "\n";
    assert(r.mass >= U128(1)<<30);
}
