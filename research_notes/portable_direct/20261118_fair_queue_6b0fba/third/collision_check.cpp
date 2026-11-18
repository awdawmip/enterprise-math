// Exact Q30 replay on a graph6 stream of 15-vertex graphs. C++17, one argument: input .g6 file.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
constexpr int N=15, FULL=(1<<N)-1;
using Graph=array<int,N>;
using Profile=array<int,N-2>;
using Colors=array<int,N>;
using Signature=array<int,4>; // old color, then up to three sorted neighbors; missing = -1.
using Packet=vector<int>;
struct Record {Graph edges; Colors seed; string g6;};
int countbits(int x){return __builtin_popcount((unsigned)x);}
int first(int x){return __builtin_ctz((unsigned)x);}
Graph decode(const string& line){
    if(line.size()!=19 || line[0]!='N')throw runtime_error("invalid graph6 length or order");
    Graph g{};int bit=0;
    for(int j=1;j<N;++j)for(int i=0;i<j;++i,++bit){
        int c=(unsigned char)line[1+bit/6]-63;
        if(c<0||c>=64)throw runtime_error("invalid graph6 digit");
        if((c>>(5-bit%6))&1){g[i]|=1<<j;g[j]|=1<<i;}
    }
    if(((line.back()-63)&7)!=0)throw runtime_error("nonzero graph6 padding");
    int seen=1,queue=1;
    while(queue){int v=first(queue);queue&=queue-1;int add=g[v]&~seen;queue|=add;seen|=add;}
    if(seen!=FULL)throw runtime_error("disconnected graph");
    for(int row:g)if(countbits(row)<2||countbits(row)>3)throw runtime_error("degree outside domain");
    return g;
}
void paths(const Graph& g,array<Profile,N>& out,int start,int second,int last,int used,int length){
    if(length>=3 && second<last && (g[last]&(1<<start))){
        for(int bits=used;bits;bits&=bits-1)++out[first(bits)][length-3];
    }
    int higher=FULL^((1<<(start+1))-1);
    for(int bits=g[last]&higher&~used;bits;bits&=bits-1){
        int next=first(bits);paths(g,out,start,second,next,used|(1<<next),length+1);
    }
}
array<Profile,N> profiles(const Graph& g){
    array<Profile,N> out{};
    for(int i=0;i<N;++i)for(int bits=g[i]&~((1<<(i+1))-1);bits;bits&=bits-1){
        int j=first(bits);paths(g,out,i,j,j,(1<<i)|(1<<j),2);
    }
    return out;
}
// This search checks the exact adjacency relation. Seed labels only prune necessary equalities.
int matching(const Graph& left,const Graph& right,const Graph& candidates,int freeL,int freeR){
    if(!freeL)return 1;
    int chosen=-1,best=0,bestSize=N+1;
    for(int bits=freeL;bits;bits&=bits-1){
        int i=first(bits), allowed=candidates[i]&freeR, size=countbits(allowed);
        if(!size)return 0;
        if(size<bestSize){chosen=i;best=allowed;bestSize=size;}
    }
    int sum=0;
    for(int choices=best;choices;choices&=choices-1){
        int v=first(choices),rest=freeL^(1<<chosen); Graph next=candidates;
        for(int b=rest;b;b&=b-1){
            int i=first(b);
            next[i]&=((left[chosen]&(1<<i)) ? right[v] : FULL^right[v]);
        }
        sum+=matching(left,right,next,rest,freeR^(1<<v));
    }
    return sum;
}
int isomorphisms(const Record& a,const Record& b){
    Graph candidates{};
    for(int i=0;i<N;++i)for(int j=0;j<N;++j)
        if(a.seed[i]==b.seed[j] && countbits(a.edges[i])==countbits(b.edges[j]))
            candidates[i]|=1<<j;
    return matching(a.edges,b.edges,candidates,FULL,FULL);
}
// Called after fixing the complete seed histogram. Restore lexicographic ordering of
// the actual root profiles, then use the frozen local ranking in every layer.
Packet packet(const Record& r,const vector<int>& lexRank){
    Colors colors=r.seed;
    for(int& c:colors)c=lexRank[c];
    Colors legend=colors;
    sort(legend.begin(),legend.end());
    auto last=unique(legend.begin(),legend.end());
    for(int& c:colors)c=lower_bound(legend.begin(),last,c)-legend.begin();
    Packet out;
    for(int step=0;step<N;++step){
        array<Signature,N> all, sorted;
        for(int i=0;i<N;++i){
            Signature sig{colors[i],-1,-1,-1};int pos=1;
            for(int bits=r.edges[i];bits;bits&=bits-1)sig[pos++]=colors[first(bits)];
            sort(sig.begin()+1,sig.begin()+pos);
            all[i]=sig;
        }
        sorted=all;sort(sorted.begin(),sorted.end());
        auto end=unique(sorted.begin(),sorted.end());
        out.push_back(end-sorted.begin());
        for(auto it=sorted.begin();it!=end;++it)out.insert(out.end(),it->begin(),it->end());
        for(int i=0;i<N;++i)colors[i]=lower_bound(sorted.begin(),end,all[i])-sorted.begin();
    }
    sort(colors.begin(),colors.end());out.insert(out.end(),colors.begin(),colors.end());
    return out;
}
struct Stats {int reps=0, ambiguous=0, equal=0;long long orbit=0;map<int,int> autos;};
int main(int argc,char**argv){
    if(argc!=2)return 1;
    ifstream in(argv[1]);if(!in)return 1;
    map<Profile,int> dictionary;
    map<Colors,vector<Record>> blocks;
    map<int,Stats> stats;
    long long fact[N+1]{1};for(int i=1;i<=N;++i)fact[i]=fact[i-1]*i;
    int cycles=0;string line;
    while(getline(in,line)){
        Graph g=decode(line);int r=0;for(int row:g)r+=countbits(row)==3;
        if(!r){++cycles;continue;}
        auto roots=profiles(g);Record current{g,{},line};
        for(int i=0;i<N;++i){
            auto [it,inserted]=dictionary.try_emplace(roots[i],dictionary.size());
            current.seed[i]=it->second;
        }
        int aut=isomorphisms(current,current);
        auto& s=stats[r];++s.reps;++s.autos[aut];
        if(aut<=0 || fact[r]*fact[N-r]%aut)throw runtime_error("automorphism order");
        s.orbit+=fact[r]*fact[N-r]/aut;
        auto key=current.seed;sort(key.begin(),key.end());
        blocks[key].push_back(move(current));
    }
    vector<int> lexRank(dictionary.size());
    int index=0;
    for(const auto& entry:dictionary)lexRank[entry.second]=index++;
    for(const auto& [key,group]:blocks){
        if(group.size()<2)continue;
        map<Packet,const Record*> packets;
        for(const Record& item:group){
            int r=0;for(int row:item.edges)r+=countbits(row)==3;
            auto& s=stats[r];++s.ambiguous;
            auto [it,inserted]=packets.emplace(packet(item,lexRank),&item);
            if(!inserted){
                int iso=isomorphisms(*it->second,item);
                if(iso)throw runtime_error("duplicate isomorphic representatives");
                ++s.equal;cout<<"collision "<<it->second->g6<<" "<<item.g6<<" iso "<<iso<<"\n";
            }
        }
    }
    cout<<"cycle_excluded "<<cycles<<" seed_histograms "<<blocks.size()<<"\n";
    for(const auto& [r,s]:stats){
        cout<<"r="<<r<<" reps="<<s.reps<<" in_nonunique_seed_buckets="<<s.ambiguous
            <<" repeats="<<s.equal<<" orbit="<<s.orbit<<" aut:";
        for(auto [a,c]:s.autos)cout<<" "<<a<<":"<<c;
        cout<<"\n";
    }
}
