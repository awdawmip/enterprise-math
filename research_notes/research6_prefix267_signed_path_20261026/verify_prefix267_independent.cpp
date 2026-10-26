// Independent X6 lattice signed-walk dynamic-programming checker.
// This checks exact reachable endpoint counts and multiplicities, not physics.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_map>
using Position = std::array<int,6>;
struct Hash {
    std::size_t operator()(const Position& a) const {
        std::uint64_t h=1469598103934665603ULL;
        for (int x:a) { h^=static_cast<std::uint32_t>(x+100000); h*=1099511628211ULL; }
        return static_cast<std::size_t>(h);
    }
};
int main() {
    for (int m=1;m<=6;++m) {
        std::unordered_map<Position,std::uint64_t,Hash> dp;
        dp[Position{}]=1;
        std::uint64_t expected=1;
        for(int k=0;k<=10;++k){
            std::uint64_t total=0;
            for (auto const& [z,c]:dp){
                int norm=0;
                for(int i=0;i<m;++i) norm+=(z[i]<0?-z[i]:z[i]);
                assert(norm<=k && (k-norm)%2==0);
                for(int i=m;i<6;++i) assert(z[i]==0);
                total+=c;
            }
            assert(total==expected);
            if(m==6 && k==10){
                Position zero{};
                Position maximal{}; maximal[0]=10;
                assert(dp[zero]>0 && dp[maximal]==1);
                std::cout<<"X6 k=10 endpoints="<<dp.size()<<" mass(0)="<<dp[zero]<<" total="<<total<<"\n";
                assert(dp.size()==85305);
            }
            if(k==10) break;
            std::unordered_map<Position,std::uint64_t,Hash> next;
            next.reserve(dp.size()*4);
            for(auto const& [z,c]:dp){
                for(int i=0;i<m;++i){
                    Position plus=z; ++plus[i]; next[plus]+=c;
                    Position minus=z; --minus[i]; next[minus]+=c;
                }
            }
            expected*=static_cast<std::uint64_t>(2*m);
            dp.swap(next);
        }
    }
    std::cout<<"INDEPENDENT_CPP_DP_PASS\n";
}
