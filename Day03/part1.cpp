#include <iostream>
#include <fstream>
#include <string>



int charToInt(char c) { return static_cast<int>(c - '0');}

int main(){
	std::ifstream fin("input.txt");
	std::string line;

	if (!fin.is_open()) {
		std::cout << "Error: Cannot open file!" << std::endl;
		return 1;
	}

	long long int totalJoltage = 0;

	while (std::getline(fin, line)) {
		const size_t len = line.length();
		char suffixMax[len];

		suffixMax[len-1] = line[len-1];
		for (int i = len-2; i >= 0; i--) {
			suffixMax[i] = std::max(suffixMax[i+1], line[i]);
		}

		int maxJoltage = 0;
		for (int i = 0; i < len-1; i++) {
			maxJoltage = std::max(maxJoltage, charToInt(line[i]) * 10 + charToInt(suffixMax[i+1]));
		}

		totalJoltage += maxJoltage;
	}

	fin.close();

	std::cout << "The answer is: " << totalJoltage << std::endl;

	return 0;
}
