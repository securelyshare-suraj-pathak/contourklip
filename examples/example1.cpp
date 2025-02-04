#include <iostream>
#include "contourklip.hpp"
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <iostream>
#include <cassert>
#include <sstream>
using namespace std;

std::vector<float> string_to_float (string Numbers) {

  std::vector<float> v;

  // Build an istream that holds the input string
  std::istringstream iss(Numbers);

  // Iterate over the istream, using >> to grab floats
  // and push_back to store them in the vector
  std::copy(std::istream_iterator<float>(iss),
        std::istream_iterator<float>(),
        std::back_inserter(v));
  return v;
}

contourklip::Contour load_contour(std::vector<float> coord_arr){
    contourklip::Contour contour_i{{coord_arr[0], coord_arr[1]}};
    for (int i = 2; i < coord_arr.size(); i++){
        if(coord_arr[i] == 1){
            contour_i.push_back({coord_arr[i + 1], coord_arr[i + 2]});
            i += 2;
        }
        else if (coord_arr[i] == 3){
            contour_i.push_back(
                {coord_arr[i + 1], coord_arr[i + 2]}, 
                {coord_arr[i + 3], coord_arr[i + 4]}, 
                {coord_arr[i + 5], coord_arr[i + 6]}
                );
            i += 6;
        }
    }
    contour_i.close();
    return contour_i;
}

int main(int argc, char** argv) {

    if (argc != 3){
        cout << "INVALID NUMBER OF ARGUMENTS -> " << argc << '\n';
        return 0;
    }

    // contourklip::Contour contour1 = load_contour(string_to_float("0 100 1 50 100 3 77.5 100 100 77.5 100 50 3 100 22.5 77.5 0 50 0 1 0 0"));
    // contourklip::Contour contour2 = load_contour(string_to_float("150 25 1 100 25 3 72.3 25 50 47.3 50 75 3 50 102.5 72.3 125 100 125 1 150"));
    
    contourklip::Contour contour1 = load_contour(string_to_float(argv[1]));
    contourklip::Contour contour2 = load_contour(string_to_float(argv[2]));

    std::vector<contourklip::Contour> shape1{contour1};
    std::vector<contourklip::Contour> shape2{contour2};
    std::vector<contourklip::Contour> result{};

    if(contourklip::clip(shape1, shape2, result, contourklip::INTERSECTION)){
        std::cout << "SUCCESS\n";
    }

    for (const auto &contour: result) {
        std::cout << "contour:\n";
        std::cout << contour;
    }
    return 0;
}