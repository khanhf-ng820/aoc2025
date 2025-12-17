#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#define ll long long int



int main(){
	std::ifstream fin("input.txt");
	std::string line;

	if (!fin.is_open()) {
		std::cout << "Error: Cannot open file!" << std::endl;
		return 1;
	}

	// pair of id and whether it is the left side of range
	std::vector<std::pair<ll, bool>> points;
	ll count = 0;

	while (std::getline(fin, line)) {
		if (line.length() == 0) {
			break;
		}

		size_t hyphenPos = line.find('-');
		ll leftRange = std::stoll(line.substr(0, hyphenPos));
		ll rightRange = std::stoll(line.substr(hyphenPos+1));
		
		points.push_back(std::make_pair(leftRange, true));
		points.push_back(std::make_pair(rightRange, false));
	}

	std::sort(points.begin(), points.end(), [](const std::pair<ll, bool>& a, const std::pair<ll, bool>& b) {
		if (a.first != b.first) return a.first < b.first;
		else return a.second > b.second;
	});
	points.insert(points.begin(), points[0]);


	int inRange = 0;
	for (std::vector<std::pair<ll, bool>>::iterator i = points.begin() + 1; i != points.end(); ++i) {
		if (inRange == 0) {
			if (i->second) {
				inRange++;
			} else {
				inRange--;
			}
			count++;
			continue;
		}
		if (i->second) {
			inRange++;
		} else {
			inRange--;
		}

		count += i->first - (i-1)->first;
	}



	fin.close();

	std::cout << "The answer is: " << count << std::endl;

	return 0;
}
