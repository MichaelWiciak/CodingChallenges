#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

std::string encrypt(std::string text, int n)
{
    if (text == "")
    {
        return text;
    }

    std::string output_string;
    std::string intial_string = text;

    std::string odd_indeces_numbers;
    std::string even_indeces_numbers;

    int len_of_string = intial_string.length();

    for (int j = 0; j < n; j++)
    {
        for (int i = 0; i < len_of_string; i++)
        {
            char tempChar = intial_string[i];
            if (i % 2 == 0)
            {
                even_indeces_numbers += tempChar;
            }
            else
            {
                odd_indeces_numbers += tempChar;
            }
        }
        intial_string.clear();
        output_string.append(odd_indeces_numbers);
        output_string.append(even_indeces_numbers);
        intial_string.append(output_string);
        output_string.clear();
        odd_indeces_numbers.clear();
        even_indeces_numbers.clear();
    }

    return intial_string;
}

std::string decrypt(std::string encryptedText, int n)
{
    if (encryptedText == "")
    {
        return encryptedText;
    }

    // split the string into middle,first half has odd and second has even indices
    // and put them back into their original position

    int midpoint_of_string = encryptedText.length() / 2;
    std::string odd_indicies_numbers;
    std::string even_indicies_numbers;

    std::string initial_working_string;
    std::string output_string;
    int total_length;
    int even_indicies_used;
    int odd_indicies_used;

    for (int j = 0; j < n; j++)
    {
        even_indicies_used = 0;
        odd_indicies_used = 0;
        odd_indicies_numbers = encryptedText.substr(0, midpoint_of_string);
        even_indicies_numbers = encryptedText.substr(midpoint_of_string);
        total_length = even_indicies_numbers.length() + odd_indicies_numbers.length();
        initial_working_string.clear();
        for (int i = 0; i < total_length; i++)
        {
            if (i % 2 == 0)
            {
                initial_working_string += even_indicies_numbers[even_indicies_used];
                even_indicies_used++;
            }
            else
            {
                initial_working_string += odd_indicies_numbers[odd_indicies_used];
                odd_indicies_used++;
            }
        }
        output_string.clear();
        output_string.append(initial_working_string);
    }
    return output_string;
}

int main(int argc, char const *argv[])
{
    std::cout << "Initial: 012345" << std::endl;
    int n = 1;
    std::string encryptedText = encrypt("012345", n);
    std::cout << encryptedText << std::endl;
    std::string decryptedText = decrypt(encryptedText, n);
    std::cout << decryptedText << std::endl;
    return 0;
}
