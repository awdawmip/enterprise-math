// R257 independent exact C++17 verifier; positive path counts only.
// Formal BRC selector model; not native heartbeat or R193 semantics.
#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <vector>
using boost::multiprecision::cpp_int;
using State=std::tuple<int,int,int,int>; // control, sign, shift, balance counter
using Edge=std::tuple<int,int,int>;
using Histogram=std::map<State,cpp_int>;

const std::array<std::array<Edge,2>,3> edges = {{
  {Edge{2,-1,-1},Edge{2,+1,-1}},
  {Edge{0,-1,-1},Edge{0,+1,-1}},
  {Edge{1,+1,+1},Edge{2,+1,-1}}
}};
State brc_step(const State& s,int a){
    const auto [q,eps,k,d]=s;
    const auto [target,eta,b]=edges.at(q).at(a);
    return State{target,eta*eps,eta*k+b,d+(a==0?1:-1)};
}
State evaluate(const std::string& word){
    State s{0,1,0,0};
    for(char ch:word){ assert(ch=='0'||ch=='1');s=brc_step(s,ch-'0'); }
    return s;
}
void check_fiber(int m){
    const int h=m/3, r=m%3;
    const auto common=std::make_tuple(r==0?0:2,1,-h-r);
    std::set<int> distinct;
    std::vector<std::pair<std::string,int>> witnesses;
    for(int j=0;j<=h;j++){
        std::string word;
        for(int i=0;i<j;i++) word += "000";
        for(int i=0;i<h-j;i++) word += "101";
        word+=std::string(r,'1');
        auto [q,eps,k,d]=evaluate(word);
        assert(std::make_tuple(q,eps,k)==common);
        assert(d==4*j-h-r);
        assert(distinct.insert(d).second);
        witnesses.emplace_back(word,d);
    }
    for(auto const& [word,d]:witnesses){
        std::string suffix=d>=0?std::string(d,'1'):std::string(-d,'0');
        auto intended=evaluate(word+suffix);
        assert(std::get<3>(intended)==0);
        for(auto const& [other,d2]:witnesses){
            auto actual=evaluate(other+suffix);
            assert(std::make_tuple(std::get<0>(intended),std::get<1>(intended),std::get<2>(intended))
                ==std::make_tuple(std::get<0>(actual),std::get<1>(actual),std::get<2>(actual)));
            assert(std::get<3>(actual)==d2-d);
        }
    }
}
int main(){
    Histogram layer{{State{0,1,0,0},cpp_int(1)}};
    cpp_int mass=1;
    int enumerated=0;
    for(int m=0;m<=48;m++){
        cpp_int sum=0;
        for(auto const& [s,n]:layer){
            sum+=n;
            assert(n>0);
            assert(std::abs(std::get<2>(s))<=m);
            assert(std::abs(std::get<3>(s))<=m);
        }
        assert(sum==mass);
        if(m<=12){
            Histogram direct;
            const int end=1<<m;
            for(int k=0;k<end;k++){
                std::string w;
                for(int b=m-1;b>=0;b--)w.push_back((k>>b)&1?'1':'0');
                direct[evaluate(w)]+=1;
                enumerated++;
            }
            assert(direct==layer);
        }
        if(m==3||m==6||m==12||m==24||m==48) check_fiber(m);
        if(m==48){
            std::cout<<"{\"validation\":\"PASS\",\"depth\":48,\"total_paths\":\""<<sum
                <<"\",\"joint_atoms\":"<<layer.size()<<",\"enumerated_words\":"<<enumerated<<"}\n";
            break;
        }
        Histogram next;
        for(auto const& [s,n]:layer){
            next[brc_step(s,0)]+=n;
            next[brc_step(s,1)]+=n;
        }
        layer.swap(next);
        mass*=2;
    }
    return 0;
}
