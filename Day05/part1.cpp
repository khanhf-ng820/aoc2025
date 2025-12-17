#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#define ll long long int



int main(){
	std::ifstream fin("input.txt");
	std::string line;

	if (!fin.is_open()) {
		std::cout << "Error: Cannot open file!" << std::endl;
		return 1;
	}

	std::vector<std::pair<ll, ll>> ranges;
	bool getRanges = true;
	int count = 0;

	while (std::getline(fin, line)) {
		if (line.length() == 0) {
			getRanges = false;
			continue;
		}

		if (getRanges) {
			size_t hyphenPos = line.find('-');
			ranges.push_back(std::make_pair(
				std::stoll(line.substr(0, hyphenPos)),
				std::stoll(line.substr(hyphenPos+1))
			));
		} else {
			ll id = std::stoll(line);
			for (const auto& [l, r] : ranges) {
				if (l <= id && id <= r) {
					count++;
					break;
				}
			}
		}
	}



	fin.close();

	std::cout << "The answer is: " << count << std::endl;

	return 0;
}
