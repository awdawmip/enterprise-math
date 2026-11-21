// Exhaust every two-template repair of a fixed, disjoint 124-orbit cover.
// Input: eleven lines; each lists one template's four-coordinate base-5 point indices.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <sstream>
#include <vector>

using Point = std::array<int,4>;
std::array<Point,625> points;
int projection[625], lift[125][5];
static std::uint8_t forbidden[625][625][125];
struct Domain { int orbit; std::array<int,2> options; };

void initialize() {
    for (int n=0;n<625;n++) {
        int v=n;
        for (int j=3;j>=0;j--) {points[n][j]=v%5; v/=5;}
        auto p=points[n];
        int s=0;
        for(int j=0;j<3;j++) s=5*s+(5+p[j]-p[3])%5;
        projection[n]=s;
        lift[s][p[3]]=n;
    }
    for(int a=0;a<625;a++) for(int b=a+1;b<625;b++) for(int c=b+1;c<625;c++) {
        if(projection[a]==projection[b] || projection[a]==projection[c] || projection[b]==projection[c]) continue;
        int types=0;
        for(int j=0;j<4;j++){
            int x=points[a][j],y=points[b][j],z=points[c][j];
            if(x==y && y!=z) types|=1;
            if(y==z && z!=x) types|=2;
            if(z==x && x!=y) types|=4;
        }
        if(!(types & (types-1))) continue;
        auto add=[](int p,int q,int r){
            forbidden[p][q][projection[r]] |= 1<<points[r][3];
            forbidden[q][p][projection[r]] |= 1<<points[r][3];
        };
        add(a,b,c);add(a,c,b);add(b,c,a);
    }
}

using Chosen=std::array<std::vector<int>,2>;
bool complete(const std::vector<Domain>& remaining, Chosen& selected, std::uint64_t& calls) {
    ++calls;
    if(remaining.empty()) return true;
    auto options=[&](const Domain &d,int color) {
        const auto &s=selected[color];
        if(s.size()>=12) return 0;
        if(s.empty()){
            if(color==1 && selected[0].empty()) return 0;
            return 1; // independent diagonal translation normalizes this group's first lift
        }
        return d.options[color];
    };
    size_t pivot=0;
    int best=11;
    for(size_t j=0;j<remaining.size();j++){
        int n=__builtin_popcount(options(remaining[j],0))+__builtin_popcount(options(remaining[j],1));
        if(!n)return false;
        if(n<best){best=n;pivot=j;}
    }
    auto current=remaining[pivot];
    for(int color=0;color<2;color++){
        for(int m=options(current,color);m;m&=m-1){
            int p=lift[current.orbit][__builtin_ctz(m)];
            auto next=remaining;
            next.erase(next.begin()+pivot);
            for(auto &d:next){
                for(int q:selected[color]){
                    d.options[color] &= ~forbidden[p][q][d.orbit];
                }
            }
            selected[color].push_back(p);
            if(complete(next,selected,calls))return true;
            selected[color].pop_back();
        }
    }
    return false;
}

int main() {
    initialize();
    std::vector<std::vector<int>> groups;
    std::array<int,125> memberships{};
    std::string line;
    while(std::getline(std::cin,line)){
        std::istringstream in(line);
        std::vector<int> orbit;
        int i;
        while(in>>i){int s=projection[i];++memberships[s];orbit.push_back(s);}
        groups.push_back(orbit);
    }
    assert(groups.size()==11 && std::count(memberships.begin(),memberships.end(),1)==124);
    std::uint64_t calls=0;
    int capacity=0, tested=0, solved=0;
    for(int a=0;a<11;a++)for(int b=a+1;b<11;b++){
        auto used=memberships;
        for(int s:groups[a])--used[s];
        for(int s:groups[b])--used[s];
        std::vector<Domain> remaining;
        for(int s=0;s<125;s++)if(!used[s]) remaining.push_back({s,{31,31}});
        if(remaining.size()>24){++capacity;continue;}
        Chosen sel;
        ++tested;
        if(complete(remaining,sel,calls))++solved;
    }
    std::cout<<"{\n  \"template_pairs\": 55,\n  \"capacity_exclusions\": "<<capacity
             <<",\n  \"exhausted_pairs\": "<<tested<<",\n  \"nodes\": "<<calls
             <<",\n  \"complete_55_label_replacements\": "<<solved<<"\n}\n";
}
