#include <array>
#include <iostream>
#include <stdexcept>
using namespace std;
using Row = array<long long,7>;
using Seven = array<Row,7>;

// Independent word enumeration; no Python or Source implementation reused.
array<long long,6> counts(int length){
    array<long long,6> v{};
    for(int mask=0;mask<(1<<length);++mask){
        int q=0, r=0;
        for(int pos=length-1;pos>=0;--pos){
            int a=(mask>>pos)&1;
            int nr;
            if(r==0) nr=(a==0?1:0);
            else if(r==1) nr=(a==0?2:0);
            else nr=2;
            if(q==0) q=2;
            else if(q==1) q=0;
            else q=(a==0?1:2);
            r=nr;
        }
        v[2*q+(r==2?1:0)]++;
    }
    return v;
}
long long bareiss(Seven a){
    long long sign=1, den=1;
    for(int k=0;k<6;k++){
        if(a[k][k]==0){
            int t=k+1;
            while(t<7 && a[t][k]==0) ++t;
            if(t==7) return 0;
            swap(a[k],a[t]); sign=-sign;
        }
        const long long pivot=a[k][k];
        for(int i=k+1;i<7;i++){
            for(int j=k+1;j<7;j++){
                const long long n=a[i][j]*pivot-a[i][k]*a[k][j];
                if(n%den) throw runtime_error("nonexact Bareiss division");
                a[i][j]=n/den;
            }
            a[i][k]=0;
        }
        den=pivot;
    }
    return sign*a[6][6];
}
int main(){
    array<array<long long,6>,8> f{};
    for(int m=0;m<=7;++m){
        f[m]=counts(m);
        long long total=0;for(auto n:f[m]) total+=n;
        if(total!=(1LL<<m)) return 2;
    }
    Seven H{};
    for(int i=0;i<7;++i){
        for(int j=0;j<6;++j) H[i][j]=f[i][j];
        H[i][6]=f[i+1][2];
    }
    auto determinant=bareiss(H);
    if(determinant!=-880) return 3;
    cout<<"R262 C++ independent exhaustive certificate PASS: det="<<determinant<<"; all 255 words of lengths 0..7 verified.\n";
    return 0;
}
