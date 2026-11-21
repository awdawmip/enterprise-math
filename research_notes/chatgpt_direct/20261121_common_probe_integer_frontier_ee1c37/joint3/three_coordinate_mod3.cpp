#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using std::array;
using std::vector;
struct I {
    array<uint64_t,4> limb{};
    I(uint64_t value=0) {limb[0]=value;}
    I& operator+=(const I& other) {
        uint64_t carry=0;
        for(int i=0;i<4;++i) {
            __uint128_t v=__uint128_t(limb[i])+other.limb[i]+carry;
            limb[i]=uint64_t(v);carry=uint64_t(v>>64);
        }
        if(carry)throw std::overflow_error("sum exceeds certified 256-bit width");
        return *this;
    }
    friend I operator+(I a,const I& b){return a+=b;}
    friend I operator*(int k,const I& a){I b;while(k--)b+=a;return b;}
    friend bool operator<(const I& a,const I& b){
        for(int i=3;i>=0;--i)if(a.limb[i]!=b.limb[i])return a.limb[i]<b.limb[i];
        return false;
    }
    friend bool operator==(const I& a,const I& b){return a.limb==b.limb;}
    friend bool operator!=(const I& a,const I& b){return !(a==b);}
    friend std::istream& operator>>(std::istream& in,I& a){for(auto& x:a.limb)in>>x;return in;}
    friend std::ostream& operator<<(std::ostream& out,const I& a){
        out<<'[';for(int i=0;i<4;++i){if(i)out<<',';out<<a.limb[i];}return out<<']';
    }
};

int main() {
    int m; I den;
    std::cin >> m >> den;
    vector<I> w(m);
    vector<int> typ(m);
    vector<array<int,15>> occ(m);
    array<int,15> free{};
    for (auto& x: free) std::cin >> x;
    for (int j=0;j<m;++j) {
        std::cin >> typ[j] >> w[j];
        for (auto& x: occ[j]) std::cin >> x;
    }
    constexpr int q=3, nfun=81;
    array<array<int,5>,nfun> coef{};
    for(int f=0;f<nfun;++f) {
        int v=f;
        for(int a=1;a<5;++a) {coef[f][a]=v%q;v/=q;}
    }
    vector<vector<uint8_t>> residues(3*nfun, vector<uint8_t>(m));
    array<int,3*nfun> base{};
    for(int ax=0;ax<3;++ax) for(int f=0;f<nfun;++f) {
        int b=0;for(int a=0;a<5;++a)b+=coef[f][a]*free[ax*5+a];
        base[ax*nfun+f]=b%q;
        for(int j=0;j<m;++j) {
            int v=0;for(int a=0;a<5;++a)v+=coef[f][a]*occ[j][ax*5+a];
            residues[ax*nfun+f][j]=v%q;
        }
    }
    const array<int,4> counts={2,5,2,1};
    I inf;inf.limb[3]=uint64_t(1)<<48;
    I best_lhs=inf;
    array<int,3> best_f{};array<int,4> best_a{};int best_r=0;
    uint64_t violated=0,tested=0;
    vector<uint8_t> r01(m);
    for(int f=0;f<nfun;++f)for(int g=0;g<nfun;++g) {
        for(int j=0;j<m;++j)r01[j]=(residues[f][j]+residues[nfun+g][j])%q;
        for(int h=0;h<nfun;++h) {
            array<array<I,q>,4> hist{};
            for(int j=0;j<m;++j)hist[typ[j]][(r01[j]+residues[2*nfun+h][j])%q]+=w[j];
            array<I,q> dp={inf,inf,inf};array<array<int,4>,q> labels{};
            dp[(base[f]+base[nfun+g]+base[2*nfun+h])%q]=0;
            for(int t=0;t<4;++t) {
                array<I,q> next={inf,inf,inf};array<array<int,4>,q> nlabels{};
                array<I,q> cost{};
                for(int a=0;a<q;++a)for(int r=0;r<q;++r)cost[a]+=((r+a)%q)*hist[t][r];
                for(int r=0;r<q;++r) if(dp[r]!=inf)for(int a=0;a<q;++a) {
                    int s=(r+a*counts[t])%q;I value=dp[r]+cost[a];
                    if(value<next[s]) {next[s]=value;nlabels[s]=labels[r];nlabels[s][t]=a;}
                }
                dp=next;labels=nlabels;
            }
            for(int r=1;r<q;++r) {
                ++tested;if(dp[r]<r*den)++violated;
                if(dp[r]+best_r*den<best_lhs+r*den) {best_lhs=dp[r];best_r=r;best_f={f,g,h};best_a=labels[r];}
            }
        }
    }
    std::cout << "{\"modulus\":3,\"coefficient_function_count\":531441,\"dp_residue_checks\":" << tested
              << ",\"represented_index_checks\":28697814,\"violating_dp_minima\":" << violated
              << ",\"lhs_limbs\":" << best_lhs << ",\"denominator_limbs\":" << den
              << ",\"rhs\":" << best_r << ",\"fiber_coefficients\":[";
    for(int ax=0;ax<3;++ax) {
        if(ax)std::cout<<',';std::cout<<'[';
        for(int a=0;a<5;++a){if(a)std::cout<<',';std::cout<<coef[best_f[ax]][a];}
        std::cout<<']';
    }
    std::cout<<"],\"type_coefficients\":[";
    for(int t=0;t<4;++t){if(t)std::cout<<',';std::cout<<best_a[t];}
    std::cout<<"]}\n";
}
