// Independent exact depth audit: g++ -O3 -std=c++17 collision_depth.cpp -o depth
// ./depth path/to/g15.g6   (connected, degrees 2 or 3, order 15)
#include <algorithm>
#include <array>
#include <iostream>
#include <fstream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
constexpr int N=15;
using Graph=array<int,N>;
using Colors=array<int,N>;
using Profile=array<int,N-2>;
using Signature=array<int,4>;
struct Record { Graph edges; Colors seed; string g6; };
int countbits(int x){return __builtin_popcount((unsigned)x);}
int first(int x){return __builtin_ctz((unsigned)x);}
Graph decode(const string& text){
    if(text.size()!=19 || text[0]!='N' || (text.back()-63)%8!=0)
        throw runtime_error("wrong graph6 header, size or padding");
    Graph g{};
    for(int high=1;high<N;++high){
        for(int low=0;low<high;++low){
            int k=high*(high-1)/2+low;
            int digit=text[1+k/6]-63;
            if(digit<0 || digit>=64)throw runtime_error("bad graph6 digit");
            if(digit & (32>>(k%6))){
                g[low]|=1<<high;g[high]|=1<<low;
            }
        }
    }
    int reached=1;
    for(int old=0;old!=reached;){
        old=reached;
        for(int i=0;i<N;++i)if(old&(1<<i))reached|=g[i];
    }
    if(countbits(reached)!=N)throw runtime_error("not connected");
    for(int row:g)if(countbits(row)!=2 && countbits(row)!=3)
        throw runtime_error("degree outside domain");
    return g;
}
// Enumerate each undirected simple cycle once. Its maximum vertex is top,
// and the smaller of its two top-neighbors is its designated first neighbor.
void extend(const Graph& g,array<Profile,N>& counts,int top,int head,int tip,int used){
    int length=countbits(used);
    if(tip>head && (g[tip]&(1<<top))){
        for(int x=used;x;x&=x-1)++counts[first(x)][length-3];
    }
    int next=g[tip]&~used&((1<<top)-1);
    while(next){
        int v=first(next);next&=next-1;
        extend(g,counts,top,head,v,used|(1<<v));
    }
}
array<Profile,N> profiles(const Graph& g){
    array<Profile,N> out{};
    for(int top=2;top<N;++top){
        for(int b=g[top]&((1<<top)-1);b;b&=b-1){
            int h=first(b);extend(g,out,top,h,h,(1<<top)|(1<<h));
        }
    }
    return out;
}
struct DepthRecord {
    Record input;
    Colors labels;
};
using Bucket=vector<DepthRecord>;
struct DepthStats {
    long long buckets=0, pairs=0, ambiguous=0, largest=0;
    array<long long,16> pairs_by_r{};
};
void account(const Bucket& b,DepthStats& s){
    long long n=b.size();
    ++s.buckets;
    s.largest=max(s.largest,n);
    if(n<2)return;
    s.pairs+=n*(n-1)/2;s.ambiguous+=n;
    // At depth zero an untyped cycle histogram could in principle mix different r.
    // Count same-stratum pairs explicitly rather than assuming purity.
    array<long long,16> by{};
    for(const auto& e:b){
        int rv=0;
        for(int v:e.input.edges)rv+=countbits(v)==3;
        ++by[rv];
    }
    for(int k=0;k<16;k++)s.pairs_by_r[k]+=by[k]*(by[k]-1)/2;
}
void print_depth(int d,const DepthStats& s){
    cout<<"depth "<<d<<" buckets "<<s.buckets<<" unresolved_pairs "<<s.pairs
        <<" ambiguous_graphs "<<s.ambiguous<<" largest "<<s.largest<<" pairs_by_r";
    for(int k=2;k<=14;k+=2)cout<<" "<<k<<":"<<s.pairs_by_r[k];
    cout<<"\n";
}
int main(int argc,char** argv){
    if(argc!=2)return 1;
    ifstream f(argv[1]); if(!f)return 1;
    map<Profile,int> roots;
    map<Colors,Bucket> initial;
    string line;int graphs=0,cycles=0;
    while(getline(f,line)){
        Graph g=decode(line);
        if(all_of(g.begin(),g.end(),[](int row){return countbits(row)==2;})){++cycles;continue;}
        array<Profile,N> pr=profiles(g);
        Colors labels;
        for(int i=0;i<N;i++)labels[i]=roots.try_emplace(pr[i],roots.size()).first->second;
        Colors key=labels;sort(key.begin(),key.end());
        initial[key].push_back({{g,labels,line},labels});++graphs;
    }
    cout<<"graphs "<<graphs<<" excluded_cycles "<<cycles<<"\n";
    DepthStats current;vector<Bucket> live;
    for(auto& kv:initial){
        account(kv.second,current);
        if(kv.second.size()>1)live.push_back(move(kv.second));
    }
    initial.clear();roots.clear();
    print_depth(0,current);
    for(int d=1;!live.empty() && d<=N;++d){
        DepthStats next;next.buckets=current.buckets-live.size();next.largest=1;
        vector<Bucket> next_live;
        string witnessA=live.front()[0].input.g6,witnessB=live.front()[1].input.g6;
        for(auto& group:live){
            // Ids in this dictionary are shared by every vertex in EVERY graph
            // in this bucket. Distinct parent buckets can never merge because
            // the old root color is a component of each child signature.
            map<Signature,int> dict;
            map<Colors,Bucket> children;
            for(auto& e:group){
                Colors updated;
                for(int i=0;i<N;i++){
                    Signature sig{e.labels[i],-1,-1,-1};
                    int j=1;
                    for(int bits=e.input.edges[i];bits;bits&=bits-1)
                        sig[j++]=e.labels[first(bits)];
                    sort(sig.begin()+1,sig.begin()+j);
                    updated[i]=dict.try_emplace(sig,dict.size()).first->second;
                }
                e.labels=updated;sort(updated.begin(),updated.end());
                children[updated].push_back(move(e));
            }
            for(auto& kv:children){
                account(kv.second,next);
                if(kv.second.size()>1)next_live.push_back(move(kv.second));
            }
        }
        if(next_live.empty())cout<<"last_unresolved_witness depth "<<d-1<<" "
            <<witnessA<<" "<<witnessB<<"\n";
        print_depth(d,next);current=next;live=move(next_live);
    }
    return !live.empty();
}
