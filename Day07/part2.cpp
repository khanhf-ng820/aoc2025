#include <iostream>
#include <fstream>
#include <string>
#include <vector>



int main() {
	std::ifstream fin("input.txt");
	std::string line;

	if (!fin.is_open()) {
		std::cout << "Error: Cannot open file!" << std::endl;
		return 1;
	}

	std::vector<std::string> lines;
	while (std::getline(fin, line)) {
		lines.push_back(line);
	}

	const size_t rows = lines.size();
	const size_t cols = lines[0].length();

	std::vector<long long int> tachyon(cols, 0);
	int countSplit = 0;

	tachyon[lines[0].find('S')] = 1;

	for (int i = 1; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			if (lines[i][j] == '^' && tachyon[j]) {
				if (j > 0) tachyon[j-1] += tachyon[j];
				if (j < cols-1) tachyon[j+1] += tachyon[j];
				tachyon[j] = 0;
				countSplit++;
			}
		}
	}

	long long int result = 0;
	for (const long long int& t : tachyon) {
		result += (long long int)t;
	}



	fin.close();

	std::cout << "The answer is: " << result << std::endl;

	return 0;
}
