// Exact R5 quotient-flat enumeration: no floating point, no random sampling.
// Build: c++ -std=c++17 -O2 VERIFY_FLATS.cpp -o verify_flats
// Run : ./verify_flats QUOTIENT_MATRIX.txt
#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
static i64 V[30][6];

i64 det5(i64 m[5][5]) {
    int p[5]={0,1,2,3,4};
    __int128 total=0;
    do {
        __int128 product=1;
        for(int i=0;i<5;i++) product*=m[i][p[i]];
        int inversions=0;
        for(int i=0;i<5;i++) for(int j=i+1;j<5;j++)
            if(p[i]>p[j]) inversions++;
        total += (inversions&1) ? -product : product;
    } while(next_permutation(p,p+5));
    if(total>LLONG_MAX || total<LLONG_MIN)
        throw runtime_error("determinant exceeds signed 64-bit output");
    return (i64)total;
}

array<i64,6> primitive_normal(const array<int,5>& ids) {
    array<i64,6> normal{};
    for(int skip=0;skip<6;skip++) {
        i64 m[5][5]{};
        for(int i=0;i<5;i++) {
            int k=0;
            for(int j=0;j<6;j++) if(j!=skip)
                m[i][k++]=V[ids[i]][j];
        }
        i64 minor=det5(m);
        normal[skip]=(skip&1) ? -minor : minor;
    }
    i64 g=0;
    for(i64 v:normal) g=std::gcd(g,std::llabs(v));
    if(g==0) return normal; // projected rank less than five
    for(i64& v:normal) v/=g;
    for(i64 v:normal) {
        if(v!=0) {
            if(v<0) for(i64& z:normal) z=-z;
            break;
        }
    }
    return normal;
}

int main(int argc,char**argv) {
    try {
        ifstream fin(argc>1?argv[1]:"QUOTIENT_MATRIX.txt");
        if(!fin) throw runtime_error("cannot open quotient matrix");
        string line;
        vector<i64> values;
        while(getline(fin,line)) {
            if(line.empty()||line[0]=='#') continue;
            istringstream row(line);
            i64 x; int k=0;
            while(row>>x){ values.push_back(x);k++; }
            if(k!=30) throw runtime_error("expected exactly thirty entries per row");
        }
        if(values.size()!=180) throw runtime_error("expected exactly six quotient rows");
        for(int row=0;row<6;row++)
            for(int j=0;j<30;j++) V[j][row]=values[30*row+j];

        map<array<i64,6>,uint32_t> flats;
        long long tested=0,rank_five=0;
        for(int a=0;a<26;a++)
        for(int b=a+1;b<27;b++)
        for(int c=b+1;c<28;c++)
        for(int d=c+1;d<29;d++)
        for(int e=d+1;e<30;e++) {
            tested++;
            auto n=primitive_normal({a,b,c,d,e});
            if(n==array<i64,6>{}) continue;
            rank_five++;
            if(flats.count(n)) continue;
            uint32_t mask=0;
            for(int j=0;j<30;j++) {
                __int128 dot=0;
                for(int k=0;k<6;k++) dot+=(__int128)n[k]*V[j][k];
                if(dot==0) mask |= (uint32_t(1)<<j);
            }
            flats[n]=mask;
        }
        map<int,int> hist;
        for(const auto& [n,mask]:flats)
            hist[__builtin_popcount(mask)]++;
        cout<<"EXACT_INTEGER_ENUM total="<<tested
            <<" rank5="<<rank_five
            <<" unique_flats="<<flats.size()<<"\n";
        for(const auto& [size,count]:hist)
            cout<<"FLAT_SUPPORT_SIZE "<<size<<" COUNT "<<count<<"\n";
        for(const auto& [n,mask]:flats) {
            int count=__builtin_popcount(mask);
            if(count<14) continue;
            cout<<"HYPERPLANE ";
            for(i64 v:n) cout<<v<<",";
            cout<<" size="<<count<<" edges=";
            for(int j=0;j<30;j++)
                if(mask&(uint32_t(1)<<j)) cout<<j<<",";
            cout<<"\n";
        }
        if(tested!=142506 || rank_five!=67728 || flats.size()!=2986
           || hist[14]!=3 || hist[24]!=4)
            throw runtime_error("flat certificate mismatch");
        cout<<"PASS_ALL_INTEGER_FLATS\n";
    } catch (const exception& ex) {
        cerr<<"FAIL: "<<ex.what()<<"\n";
        return 1;
    }
}
