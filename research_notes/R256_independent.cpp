// Independent finite-control positive-BRC branch recurrence and substring query verifier.
// Formal mathematical carrier; NOT a physical heartbeat solver.
#include <array>
#include <map>
#include <string>
#include <iostream>
#include <cassert>
#include <boost/multiprecision/cpp_int.hpp>
using Z = boost::multiprecision::cpp_int;
using Key = std::array<int,4>; // q, sign, offset, query_state
struct Edge { int target, eta, offset; };
const Edge EDGE[3][2] = {
    {{2,-1,-1},{2,+1,-1}},
    {{0,-1,-1},{0,+1,-1}},
    {{1,+1,+1},{2,+1,-1}}
};
const int DELTA[3][2] = {{1,0},{2,0},{2,2}};
Key next(Key s, int symbol){
    const auto &e=EDGE[s[0]][symbol];
    return {e.target,e.eta*s[1],e.eta*s[2]+e.offset,DELTA[s[3]][symbol]};
}
Key word(const std::string &s) {
    Key z={0,1,0,0};
    for(char c:s) z=next(z,int(c-'0'));
    return z;
}
int main(){
    std::map<Key,Z> cur;cur[{0,1,0,0}]=1;
    Z fib0=0, fib1=1; // F_0 and F_1
    unsigned long long exhaustive=0;
    for(int depth=0;depth<=96;depth++){
        Z total=0, no=0, query=0;
        for(const auto &[st,c]:cur){ total+=c; if(st[3]==2)query+=c; else no+=c; }
        Z f0=0,f1=1;
        for(int i=0;i<depth+2;i++){Z t=f0+f1;f0=f1;f1=t;}
        assert(no==f0);
        assert(total==(Z(1)<<depth));
        assert(query==total-no);
        if(depth<=12){
           std::map<Key,Z> direct;
           for(int num=0;num<(1<<depth);num++){
             std::string s(depth,'0');
             for(int j=0;j<depth;j++)s[j]=((num>>(depth-j-1))&1)?'1':'0';
             direct[word(s)]++;
             exhaustive++;
           }
           assert(direct==cur);
        }
        if(depth==3){
            auto a=word("000"),b=word("101");
            assert(a[0]==b[0]&&a[1]==b[1]&&a[2]==b[2]);
            assert(a[3]==2 && b[3]==0);
        }
        if(depth==7){
            auto a=word("1110101"),b=word("1011010"),c=word("0000000");
            assert(a[0]==b[0]&&a[0]==c[0]&&a[1]==b[1]&&a[1]==c[1]&&a[2]==b[2]&&a[2]==c[2]);
            assert(a[3]==0&&b[3]==1&&c[3]==2);
            assert(a[0]==2&&a[1]==-1&&a[2]==1);
        }
        if(depth==3||depth==7||depth==12||depth==24||depth==48||depth==96){
            std::cout << "m=" << depth << " total="<<total<<" no00="<<no<<" contains00="<<query<<" product_atoms="<<cur.size()<<"\n";
        }
        std::map<Key,Z> nxt;
        for(const auto &[st,c]:cur){nxt[next(st,0)]+=c;nxt[next(st,1)]+=c;}
        cur.swap(nxt);
    }
    assert(exhaustive==8191);
    std::cout<<"CXX_PASS all_word_checks="<<exhaustive<<" exact_96_steps=yes\n";
}
