// PREFIX-984: exact four-phase signed-source observer census, p=3..7.
// The graph uses every odd p-bit input, phase in 0..3 and named legal source port.
// Counts are exact; no BRC/native-X6 physical attribution is asserted.
#include <bits/stdc++.h>
using namespace std;
struct Port {int j, mask;};
struct Residual {int c; vector<Port> ports;};

vector<Residual> dictionary(int p) {
    map<int, map<int,int>> raw;
    for (int i=0;i<p;i++)
        for (int j=1;j<p;j++)
            for (int s : {-1,1}) {
                int c=(1<<i)-s*(1<<j);
                if (c) raw[c][j] |= (s==-1 ? 2:1);
            }
    vector<Residual> out;
    for (const auto &[c, ports] : raw) {
        Residual r; r.c=c;
        for (const auto &[j,mask] : ports) r.ports.push_back({j,mask});
        out.push_back(move(r));
    }
    return out;
}
struct Answer {bool cyclic, loop4, loop8; int longest, longest_from_phase0;};

Answer solve(const array<const Residual*,4> &word, int p) {
    const int q=1<<(p-1), n=4*q;
    int dest[1024][2], degree[1024]={}, indegree[1024]={};
    for (int phase=0;phase<4;phase++)
        for (int bits=0;bits<q;bits++) {
            int u=phase*q+bits;
            for (auto [j,mask] : word[phase]->ports) {
                if (!(mask & (1 << ((bits>>(j-1))&1)))) continue;
                int v=((phase+1)%4)*q + (bits ^ (1<<(j-1)));
                dest[u][degree[u]++]=v;
                ++indegree[v];
            }
        }

    int head=0,tail=0,queue[1024],length[1024]={},length0[1024];
    for (int i=0;i<n;i++) length0[i]=(i<q ? 0:-10000);
    for (int i=0;i<n;i++) if (!indegree[i]) queue[tail++]=i;
    int longest=0,longest0=0;
    while (head<tail) {
        int u=queue[head++];
        for (int k=0;k<degree[u];k++) {
            int v=dest[u][k];
            length[v]=max(length[v],length[u]+1);
            longest=max(longest,length[v]);
            if (length0[u]>=0) {
                length0[v]=max(length0[v],length0[u]+1);
                longest0=max(longest0,length0[v]);
            }
            if (--indegree[v]==0) queue[tail++]=v;
        }
    }
    if (head==n) return {false,false,false,longest,longest0};

    bool loop4=false,loop8=false;
    for (int x=0;x<q && !(loop4&&loop8);x++) {
        uint64_t states=uint64_t(1)<<x;
        for (int t=0;t<8;t++) {
            uint64_t next=0;
            const int phase=t%4;
            while (states) {
                int bits=__builtin_ctzll(states);
                states&=states-1;
                int u=phase*q+bits;
                for (int k=0;k<degree[u];k++)
                    next |= uint64_t(1)<<(dest[u][k]%q);
            }
            states=next;
            if (t==3 && (states&(uint64_t(1)<<x))) loop4=true;
            if (!states) break;
        }
        if (states&(uint64_t(1)<<x)) loop8=true;
    }
    return {true,loop4,loop8,-1,-1};
}

int main(int argc,char **argv) {
    if (argc!=2) throw runtime_error("usage: prefix984 <integer p, 3..7>");
    int p=stoi(argv[1]);
    if (p<3 || p>7) throw runtime_error("p must be 3..7 (64-bit state mask)");
    const auto dict=dictionary(p);
    array<const Residual*,4> w;
    long long finite=0,cycles=0,no4=0,no8=0;
    int maxfinite=-1,maxphase0=-1;
    array<int,4> maxw{},maxw0{},wno4{},wno8{};
    for (const auto &a:dict)
        for (const auto &b:dict)
            for (const auto &c:dict)
                for (const auto &e:dict) {
                    w={&a,&b,&c,&e};
                    auto z=solve(w,p);
                    array<int,4> names={a.c,b.c,c.c,e.c};
                    if (z.cyclic) {
                        ++cycles;
                        if (!z.loop4) {++no4; if (no4==1) wno4=names;}
                        if (!z.loop8) {++no8; if (no8==1) wno8=names;}
                    } else {
                        ++finite;
                        if (z.longest>maxfinite) {maxfinite=z.longest;maxw=names;}
                        if (z.longest_from_phase0>maxphase0) {
                            maxphase0=z.longest_from_phase0;maxw0=names;
                        }
                    }
                }
    auto fmt=[](array<int,4> x) {
        string s="[";
        for (int k=0;k<4;k++) s+=to_string(x[k])+(k==3?"]":",");
        return s;
    };
    cout << "{\"p\":"<<p<<",\"residuals\":"<<dict.size()
         <<",\"total\":"<<(finite+cycles)<<",\"finite\":"<<finite
         <<",\"cyclic\":"<<cycles<<",\"cyclic_without_4_loop\":"<<no4
         <<",\"cyclic_without_8_loop\":"<<no8
         <<",\"max_finite_steps_any_phase\":"<<maxfinite
         <<",\"max_finite_witness_any_phase\":"<<fmt(maxw)
         <<",\"max_finite_steps_phase0\":"<<maxphase0
         <<",\"max_finite_witness_phase0\":"<<fmt(maxw0)
         <<",\"first_no4_witness\":"<<fmt(wno4)
         <<",\"first_no8_witness\":"<<fmt(wno8)
         <<"}\n";
}