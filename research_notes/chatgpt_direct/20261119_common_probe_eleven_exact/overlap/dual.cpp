// Verify a rowwise integer bound on maximum retained histories, with optional fixed matches.
#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
using Word=uint64_t;
using Mask=__uint128_t;
using Bounds=array<int,14>;
int count_bits(Mask a){return popcount(Word(a))+popcount(Word(a>>64));}
int first(Mask a){return Word(a)?countr_zero(Word(a)):64+countr_zero(Word(a>>64));}
vector<Mask> load_masks(const string& filename){
    vector<Mask> rows;
    Word lo,hi;
    ifstream f(filename);
    while(f>>lo>>hi)rows.push_back(Mask(hi)<<64|lo);
    return rows;
}
struct Row{Mask mask;array<int,9> points;Bounds overlap;};
struct Pair { Mask cells; int label; int loss; };
const Mask domain=(Mask(1)<<126)-1;
long long nodes=0, limit=0;
int search(Mask todo, int labels, int budget, const vector<Pair>& options){
    if(++nodes>limit)return -1;
    if(!labels)return 1;
    array<int,14> least;least.fill(10000000);
    vector<Pair> available;
    for(auto p:options)if((labels>>p.label&1)&&p.loss<=budget&&!(p.cells&~todo)){
        available.push_back(p);
        least[p.label]=min(least[p.label],p.loss);
    }
    int minimum=0;
    for(int i=0;i<14;i++)if(labels>>i&1)minimum+=least[i];
    if(minimum>budget)return 0;
    array<int,140> degrees{};
    available.erase(remove_if(available.begin(),available.end(),[&](const Pair& p){
        return minimum-least[p.label]+p.loss>budget;
    }),available.end());
    for(auto p:available){
        degrees[126+p.label]++;
        for(auto m=p.cells;m;m&=m-1)degrees[first(m)]++;
    }
    int target=126+countr_zero(unsigned(labels));
    for(auto m=todo;m;m&=m-1)if(degrees[first(m)]<degrees[target])target=first(m);
    for(int i=0;i<14;i++)if((labels>>i&1)&&degrees[126+i]<degrees[target])target=126+i;
    for(auto p:available){
        if(target>=126?p.label!=target-126:!(p.cells>>target&1))continue;
        int value=search(todo^p.cells,labels^(1<<p.label),budget-p.loss,available);
        if(value)return value;
    }
    return 0;
}
int main(int argc,char** argv){
    string d=argv[1];
    vector<Mask> old=load_masks(d+"/old");old.push_back(0);
    if(old.size()!=14)throw runtime_error("old labels");
    vector<Row> rows;
    for(int size:{8,9})for(auto mask:load_masks(d+"/full"+to_string(size))){
        Row row;row.mask=mask;int point=0;
        for(auto scan=mask;scan;scan&=scan-1)row.points[point++]=first(scan);
        if(size==8)row.points[point++]=125;
        if(point!=9)throw runtime_error("row");
        for(int i=0;i<14;i++)row.overlap[i]=count_bits(mask&old[i]);
        rows.push_back(row);
    }
    int fixed=0;
    while(cin>>fixed){
        Mask occupied=0;
        for(int i=0;i<14;i++)if(fixed>>i&1)occupied|=old[i];
        // The dummy point is present in exactly one selected row, the eight-point class.
        array<int,126> weights{};
        int objective=1000*count_bits(occupied);
        for(int x=0;x<126;x++)if(!(occupied>>x&1)){
            if(!(cin>>weights[x]))throw runtime_error("weights");
            objective+=weights[x];
        }
        Bounds caps;caps.fill(-1000000);
        for(const auto& row:rows)if(!(row.mask&occupied)){
            int sum=0;
            for(int p:row.points)sum+=weights[p];
            for(int i=0;i<14;i++)if(!(fixed>>i&1)&&old[i]!=row.mask)
                caps[i]=max(caps[i],1000*row.overlap[i]-sum);
        }
        for(int i=0;i<14;i++)if(!(fixed>>i&1))objective+=caps[i];
        cout<<fixed<<" "<<objective;
        if(argc>2){
            int budget=objective-1000*stoi(argv[2]);
            limit=stoll(argv[3]); nodes=0;int value=0;
            if(budget>=0){
                vector<Pair> options;
                for(const auto&row:rows)if(!(row.mask&occupied)){
                    int sum=0;
                    for(int p:row.points)sum+=weights[p];
                    Mask all=row.mask|(row.points[8]==125?Mask(1)<<125:0);
                    for(int i=0;i<14;i++)if(!(fixed>>i&1)&&old[i]!=row.mask){
                        int loss=caps[i]+sum-1000*row.overlap[i];
                        if(loss<=budget)options.push_back({all,i,loss});
                    }
                }
                value=search(domain^occupied,16383^fixed,budget,options);
            }
            cout<<" "<<value<<" "<<nodes;
        }
        cout<<endl;
    }
}
