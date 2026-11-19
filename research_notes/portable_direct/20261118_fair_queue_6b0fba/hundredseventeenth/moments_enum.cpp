// Certified enumeration of the weighted kernel. The Python driver checks the basis
// and rounds exact rational projections outwards before supplying the integer data.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>

using Z = std::int64_t;
constexpr int capacity = 60;
constexpr Z shift_scale = 1 << 20, star_scale = 4096;
constexpr Z field_scale = 32, projector_scale = 16384;
using Field = std::array<Z,capacity>;

int rank_, cols;
Z budget, window[capacity], star_peak[capacity], denom[capacity], digit[capacity];
Z row[capacity][capacity], mu[capacity][capacity], star[capacity][capacity];
int projector[capacity][capacity][capacity];
Z nodes[capacity+1], rejected[capacity+1], max_digit_sum, max_error;
bool tighten;

Z floor_div(Z x, Z y) {
    return x >= 0 ? x/y : -((-x+y-1)/y);
}
Z ceil_div(Z x, Z y) {
    return -floor_div(-x,y);
}
Z read_number(Z bound) {
    Z x;
    if (!(std::cin >> x) || x < -bound || x > bound) std::exit(2);
    return x;
}

// Each step proposes a separating functional from the endpoints of the
// interval of possible readings. Only its certified dot-product test cuts.
bool separates(int level, Z error, const Field& value) {
    if (!tighten || level < 2) return false;
    Field trial = value;
    Z trial_error = error, value_l1 = 0;
    for (int k=0; k<cols; ++k) value_l1 += std::abs(value[k]);
    for (int step=0; step<8; ++step) {
        Z top=0, bottom=0;
        int plus=-1, minus=-1;
        for (int k=0; k<cols; ++k) {
            if (trial[k]>top) { top=trial[k]; plus=k; }
            if (trial[k]<bottom) { bottom=trial[k]; minus=k; }
        }
        Z divisor=step<3 ? 4 : 8;
        for (int k=0; k<cols; ++k) {
            Z contrast=(plus<0 ? 0 : projector[level][plus][k])
                      -(minus<0 ? 0 : projector[level][minus][k]);
            trial[k]=((divisor-1)*trial[k]+value[k]
                      -budget*field_scale*contrast/projector_scale)/divisor;
        }
        trial_error=ceil_div((divisor-1)*trial_error+error
                             +ceil_div(2*budget*field_scale,projector_scale)+1,divisor)+1;
        Z dot=0, trial_l1=0;
        top=bottom=0;
        for (int k=0; k<cols; ++k) {
            assert(std::abs(trial[k])<10000000);
            dot+=trial[k]*value[k];
            trial_l1+=std::abs(trial[k]);
            top=std::max(top,trial[k]); bottom=std::min(bottom,trial[k]);
        }
        Z lower=dot-error*trial_l1-trial_error*value_l1-cols*error*trial_error;
        if (lower>budget*field_scale*(top-bottom+2*trial_error)) return true;
    }
    return false;
}

void search(int level, Z digit_sum, Z error, const Field& value) {
    assert(digit_sum<=10000 && error<=10000);
    max_digit_sum=std::max(max_digit_sum,digit_sum);
    max_error=std::max(max_error,error);
    ++nodes[level+1];
    if (level<0) {
        Z positive=0,negative=0;
        Field signed_counts{};
        for (int k=0; k<cols; ++k) {
            Z weight=0;
            for (int j=0; j<rank_; ++j) weight+=digit[j]*row[j][k];
            assert(weight%(denom[k]-1)==0);
            signed_counts[k]=weight/(denom[k]-1);
            if (weight>0) positive+=weight; else negative-=weight;
        }
        if (positive+negative && std::max(positive,negative)<=budget) {
            std::cout<<"HIT "<<positive<<" "<<negative;
            for (int k=0;k<cols;++k) std::cout<<" "<<signed_counts[k];
            std::cout<<'\n';
        }
        return;
    }
    Z shift=0;
    for (int j=level+1; j<rank_; ++j) shift+=mu[j][level]*digit[j];
    Z first=ceil_div(-window[level]-digit_sum-shift,shift_scale);
    Z last=floor_div(window[level]+digit_sum-shift,shift_scale);
    for (Z n=first; n<=last; ++n) {
        digit[level]=n;
        Z a=shift+n*shift_scale;
        assert(std::abs(a)<=7000000);
        Z next_error=error+ceil_div(field_scale*digit_sum*star_peak[level],shift_scale)
            +ceil_div(field_scale*std::abs(a),shift_scale*star_scale)+1;
        Field next{};
        Z lo=0,hi=0,squared=0;
        for (int k=0; k<cols; ++k) {
            next[k]=value[k]+a*star[level][k]*field_scale/(shift_scale*star_scale);
            assert(std::abs(next[k])<10000000 && next_error<=10000);
            lo=std::min(lo,next[k]); hi=std::max(hi,next[k]);
            Z low=std::max(Z(0),std::abs(next[k])-next_error);
            squared+=low*low;
        }
        if (squared>2*(budget*field_scale)*(budget*field_scale)
                || squared>budget*field_scale*(hi-lo+2*next_error)
                || separates(level,next_error,next)) {
            ++rejected[level];
        } else {
            search(level-1,digit_sum+std::abs(n),next_error,next);
        }
    }
}

int main(int argc,char** argv) {
    tighten=argc==2 && std::string(argv[1])=="tight";
    rank_=read_number(capacity-1); cols=read_number(capacity); budget=read_number(2332);
    assert(rank_==50 && cols==57 && budget==2332);
    for (int k=0;k<cols;k++) denom[k]=read_number(2333);
    for (int i=0;i<rank_;i++) {
        for (int j=0;j<cols;j++) row[i][j]=read_number(10000);
        for (int j=0;j<i;j++) mu[i][j]=read_number(shift_scale);
        for (int j=0;j<cols;j++) star[i][j]=read_number(30000000);
        window[i]=read_number(6500000);
        star_peak[i]=read_number(10000);
    }
    if (tighten)
        for (int i=0;i<rank_;i++) for (int j=0;j<cols;j++) for (int k=0;k<cols;k++)
            projector[i][j][k]=read_number(projector_scale+1);
    search(rank_-1,0,0,Field{});
    std::cout<<"NODES"; for (int i=0;i<=rank_;i++) std::cout<<" "<<nodes[i];
    std::cout<<"\nCUTS"; for (int i=0;i<=rank_;i++) std::cout<<" "<<rejected[i];
    std::cout<<"\nBOUNDS "<<max_digit_sum<<" "<<max_error<<"\n";
}
