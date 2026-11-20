// R762HJ exact check; C++17: g++ -O3 -std=c++17 R762HJ_CHECK.cpp -o r762hj && ./r762hj
// All calculations are exact integers; time-labelled Port transitions stay distinct.
#include <array>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

static int port[15], nxt[15][8], supp[15][8], retained[15][8], m, word[40], keep[40];
struct Count { long long closed=0, even=0, alt=0, hi2=0, both=0, any=0, block=0; };

int support_mask(const string& s) {
    int x=0; for(char c:s) { assert(c>='0'&&c<='5'); x |= 1<<(c-'0'); }
    return x;
}
int index_port(int mask) {
    for(int i=0;i<15;i++) if(port[i]==mask) return i;
    assert(false); return -1;
}
bool one_block(const vector<int>& S) {
    const int n=(int)S.size(); vector<array<int,6>> V(n+1);
    V[0].fill(0);
    for(int t=0;t<n;t++) {
        V[t+1]=V[t];
        for(int i=0;i<6;i++) if((S[t]>>i)&1) V[t+1][i] += (t&1)?-1:+1;
    }
    for(int a=0;a<n;a++) for(int b=a+1;b<=n;b++) {
        bool ok=true;
        for(int i=0;i<6;i++) if(2*(V[b][i]-V[a][i]) != V[n][i]) ok=false;
        if(ok) return true;
    }
    return false;
}
void examine(const vector<int>& S, const vector<int>& K, Count& cnt) {
    const int n=(int)S.size();
    cnt.closed++;
    int deg[6]={}, r[6]={}, disp[6]={};
    for(int t=0;t<n;t++) {
        for(int i=0;i<6;i++) if((S[t]>>i)&1) {
            deg[i]++; disp[i] += (t&1)?-1:+1;
        }
        r[K[t]] += (t&1)?-1:+1;
    }
    for(int i=0;i<6;i++) assert(disp[i] == -r[i]); // HJ1 for the actual Port walk
    for(int i=0;i<6;i++) if(deg[i]&1) return;
    cnt.even++;
    bool alt=true;
    for(int i=0;i<6;i++) if(r[i]) alt=false;
    bool hi2=false;
    for(int c=0;c<6;c++) {
        int dl[6]={}; // type-1 layer of HI1: c is inside the support
        for(int t=0;t<n;t++) if((S[t]>>c)&1)
            for(int i=0;i<6;i++) if(i!=c && ((S[t]>>i)&1)) dl[i]++;
        bool ok=true;
        for(int i=0;i<6;i++) if(i!=c && (dl[i]&1)) ok=false;
        if(ok) hi2=true;
    }
    bool block=one_block(S);
    assert(!alt || block);
    if(alt) cnt.alt++;
    if(hi2) cnt.hi2++;
    if(alt&&hi2) cnt.both++;
    if(alt||hi2) cnt.any++;
    if(block) cnt.block++;
}
void walk(int t,int p,Count& cnt) {
    if(t==m) {
        if(p==0) {
            vector<int> S(word,word+m), K(keep,keep+m);
            examine(S,K,cnt);
        }
        return;
    }
    for(int j=0;j<8;j++) {
        word[t]=supp[p][j]; keep[t]=retained[p][j];
        walk(t+1,nxt[p][j],cnt);
    }
}
void check_witness() {
    vector<string> names={"01","15","12","25","24","14","45","04","05","03",
                          "05","03","04","24","23","25","35","05","01"};
    vector<int> S, K;
    for(int t=0;t<18;t++) {
        int p=support_mask(names[t]), q=support_mask(names[t+1]);
        int inter=p&q;
        assert(__builtin_popcount((unsigned)inter)==1);
        S.push_back(p|q);
        K.push_back(__builtin_ctz((unsigned)inter));
    }
    assert(names.front()==names.back());
    int degree[6]={};
    for(int x:S) for(int i=0;i<6;i++) if((x>>i)&1) degree[i]++;
    int expected[6]={10,6,8,8,8,14};
    for(int i=0;i<6;i++) assert(degree[i]==expected[i]);
    assert(!one_block(S));
    // Two singleton interval flips: [0,1) and [5,6)
    int sum[6]={};
    for(int t=0;t<18;t++) {
        int sign=(t&1)?-1:+1;
        if(t==0||t==5) sign=-sign;
        for(int i=0;i<6;i++) if((S[t]>>i)&1) sum[i]+=sign;
    }
    for(int i=0;i<6;i++) assert(sum[i]==0);
    long long solutions=0;
    for(int bits=0;bits<(1<<18);bits++) {
        int z[6]={};
        for(int t=0;t<18;t++) {
            int sign=(bits&(1<<t))?+1:-1;
            for(int i=0;i<6;i++) if((S[t]>>i)&1) z[i]+=sign;
        }
        bool zero=true;
        for(int i=0;i<6;i++) if(z[i]) zero=false;
        if(zero) solutions++;
    }
    assert(solutions==652);
    cout<<"witness_m18: parity_even=1, one_block=0, two_blocks=1, signed_completions="
        <<solutions<<"\\n";
}
int main() {
    int n=0;
    for(int i=0;i<6;i++) for(int j=i+1;j<6;j++) port[n++]=(1<<i)|(1<<j);
    assert(n==15 && port[0]==3); // fixed starting Port 01
    for(int p=0;p<15;p++) {
        int k=0;
        for(int q=0;q<15;q++) if(__builtin_popcount((unsigned)(port[p]&port[q]))==1) {
            nxt[p][k]=q;
            supp[p][k]=port[p]|port[q];
            retained[p][k]=__builtin_ctz((unsigned)(port[p]&port[q]));
            k++;
        }
        assert(k==8);
    }
    const long long expected[4][7]={
        {8,8,8,8,8,8,8},
        {288,168,168,168,168,168,168},
        {17536,4960,4960,4864,4864,4960,4960},
        {1118720,177536,176264,162368,161288,177344,177536}
    };
    for(int t=0;t<4;t++) {
        m=2+2*t; Count c; walk(0,0,c);
        long long x[7]={c.closed,c.even,c.alt,c.hi2,c.both,c.any,c.block};
        for(int j=0;j<7;j++) assert(x[j]==expected[t][j]);
        cout<<"m="<<m<<" closed="<<c.closed<<" parity="<<c.even
            <<" alternate="<<c.alt<<" HI2="<<c.hi2
            <<" HI2_and_alt="<<c.both<<" HI2_or_alt="<<c.any
            <<" one_block="<<c.block<<"\\n";
    }
    check_witness();
    cout<<"PASS R762HJ exact census and witness\\n";
}
