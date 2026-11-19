// Exact 192-bit meet-in-the-middle and stable parity partition.
// g++ -O3 -std=c++17 v4_phase_work/minimize_family.cpp -o v4_phase_work/minimize_family
// v4_phase_work/minimize_family v4_phase_work/family_M.bin 240 > v4_phase_work/minimum_M.json
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

struct U192 {
    uint64_t x=0, y=0, z=0;
    friend bool operator<(U192 a,U192 b) { return a.z!=b.z ? a.z<b.z : a.y!=b.y ? a.y<b.y : a.x<b.x; }
    friend bool operator==(U192 a,U192 b) { return a.x==b.x && a.y==b.y && a.z==b.z; }
    friend U192 operator+(U192 a,U192 b) {
        unsigned __int128 t=(unsigned __int128)a.x+b.x;
        U192 c; c.x=t;
        t=(unsigned __int128)a.y+b.y+(t>>64); c.y=t;
        t=(unsigned __int128)a.z+b.z+(t>>64); c.z=t;
        assert(!(t>>64)); return c;
    }
    friend U192 operator-(U192 a,U192 b) {
        assert(!(a<b)); U192 c;
        c.x=a.x-b.x; uint64_t borrow=a.x<b.x;
        unsigned __int128 middle=(unsigned __int128)b.y+borrow;
        c.y=a.y-(uint64_t)middle;
        borrow=((unsigned __int128)a.y < middle);
        c.z=a.z-b.z-borrow; return c;
    }
    U192 half() const { return {x/2+(y<<63), y/2+(z<<63), z/2}; }
    std::string decimal() const {
        U192 v=*this; std::string result;
        do {
            unsigned __int128 r=v.z; v.z=r/10; r=(r%10<<64)+v.y;
            v.y=r/10; r=(r%10<<64)+v.x; v.x=r/10;
            result.push_back('0'+int(r%10));
        } while(v.x || v.y || v.z);
        std::reverse(result.begin(), result.end()); return result;
    }
};
struct Node { U192 value; uint64_t code; };
static_assert(sizeof(Node)==32);

struct Winner { U192 value; uint64_t left=0,right=0; int translation=0; bool present=false; };

void consider(Winner &best,U192 value,uint64_t a,uint64_t b,int translation) {
    assert(value.x&1);
    if(!best.present || value<best.value) best={value,a,b,translation,true};
}

Winner minimize(const std::vector<Node>& a,const std::vector<Node>& b,U192 modulus,int translation) {
    Winner best;
    std::array<size_t,2> minimum_a={a.size(),a.size()}, minimum_b={b.size(),b.size()};
    for(size_t i=0;i<a.size() && (minimum_a[0]==a.size() || minimum_a[1]==a.size());++i)
        if(minimum_a[a[i].value.x&1]==a.size()) minimum_a[a[i].value.x&1]=i;
    for(size_t i=0;i<b.size() && (minimum_b[0]==b.size() || minimum_b[1]==b.size());++i)
        if(minimum_b[b[i].value.x&1]==b.size()) minimum_b[b[i].value.x&1]=i;
    for(int parity=0;parity<2;++parity) {
        size_t i=minimum_a[parity], j=minimum_b[1-parity];
        if(i<a.size() && j<b.size()) {
            U192 s=a[i].value+b[j].value;
            if(s<modulus) consider(best,s,a[i].code,b[j].code,translation);
        }
    }
    for(unsigned parity=0;parity<2;++parity) {
        size_t i=0, j=b.size(); // j is one beyond the descending candidate
        while(true) {
            while(i<a.size() && (a[i].value.x&1)!=parity) ++i;
            while(j>0 && (b[j-1].value.x&1)!=parity) --j;
            if(i==a.size() || j==0) break;
            U192 s=a[i].value+b[j-1].value;
            if(!(s<modulus)) {
                consider(best,s-modulus,a[i].code,b[j-1].code,translation);
                --j;
            } else ++i;
        }
    }
    if(!best.present) throw std::runtime_error("No odd candidate; sign symmetry invariant failed");
    return best;
}

void advance(std::vector<Node>& values,std::vector<Node>& buffer,U192 modulus) {
    size_t even=0,odd=values.size()/2;
    for(const Node &node: values) {
        if(node.value.x&1) buffer[odd++]={(node.value+modulus).half(),node.code};
        else buffer[even++]={node.value.half(),node.code};
    }
    assert(even==values.size()/2 && odd==values.size());
    values.swap(buffer);
}

void print_winner(const Winner& w) {
    std::cout << "{\"root\":\""<<w.value.decimal()<<"\",\"a_code\":"<<w.left
              <<",\"b_code\":"<<w.right<<",\"translation\":"<<w.translation<<"}";
}

int main(int argc,char** argv) {
    if(argc!=3) throw std::runtime_error("usage: minimize_family binary_input number_of_shifts");
    auto start=std::chrono::steady_clock::now();
    std::ifstream input(argv[1],std::ios::binary);
    if(!input) throw std::runtime_error("cannot open input");
    char magic[8]; input.read(magic,8);
    if(std::string(magic,8)!="RIESELV4") throw std::runtime_error("bad input magic");
    U192 modulus; input.read(reinterpret_cast<char*>(&modulus),sizeof(modulus));
    uint64_t count_a,count_b; input.read(reinterpret_cast<char*>(&count_a),8); input.read(reinterpret_cast<char*>(&count_b),8);
    assert(modulus.x&1); assert(modulus.z<(1ULL<<62));
    std::vector<Node> a(count_a),b(count_b),temp_a(count_a),temp_b(count_b);
    input.read(reinterpret_cast<char*>(a.data()),count_a*sizeof(Node));
    input.read(reinterpret_cast<char*>(b.data()),count_b*sizeof(Node));
    if(!input) throw std::runtime_error("truncated input");
    for(const auto *values: {&a,&b}) for(const Node& n:*values) assert(n.value<modulus);
    const auto cmp=[](const Node& a,const Node& b){return a.value<b.value;};
    std::sort(a.begin(),a.end(),cmp); std::sort(b.begin(),b.end(),cmp);
    Winner global;
    int shifts=std::stoi(argv[2]);
    std::cout << "{\"modulus\":\""<<modulus.decimal()<<"\",\"left_count\":"<<count_a
              <<",\"right_count\":"<<count_b<<",\"shift_count\":"<<shifts<<",\"minima\":[";
    for(int t=0;t<shifts;++t) {
        Winner current=minimize(a,b,modulus,t);
        if(t) std::cout << ',';
        print_winner(current);
        consider(global,current.value,current.left,current.right,t);
        if((t+1)%20==0) std::cerr << "completed shifts "<<(t+1)<<'/'<<shifts<<'\n';
        if(t+1<shifts) { advance(a,temp_a,modulus); advance(b,temp_b,modulus); }
    }
    std::cout << "],\"minimum\":"; print_winner(global);
    double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    std::cout << ",\"seconds\":"<<seconds<<"}\n";
}
