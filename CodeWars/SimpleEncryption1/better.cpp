#include <string>
#include <utility>
#include <iostream>

std::string encrypt(std::string text, int n)
{
    if (text.empty() || n <= 0)
    {
        return text;
    }

    const std::size_t len = text.size();
    std::string current = std::move(text);

    for (int step = 0; step < n; ++step)
    {
        std::string next;
        next.reserve(len);

        for (std::size_t i = 1; i < len; i += 2)
        {
            next.push_back(current[i]);
        }
        for (std::size_t i = 0; i < len; i += 2)
        {
            next.push_back(current[i]);
        }

        current = std::move(next);
    }

    return current;
}

std::string decrypt(std::string encryptedText, int n)
{
    if (encryptedText.empty() || n <= 0)
    {
        return encryptedText;
    }

    const std::size_t len = encryptedText.size();
    const std::size_t mid = len / 2;
    std::string current = std::move(encryptedText);

    for (int step = 0; step < n; ++step)
    {
        std::string next;
        next.reserve(len);

        std::size_t odd_idx = 0;
        std::size_t even_idx = mid;

        for (std::size_t i = 0; i < len; ++i)
        {
            if (i % 2 == 0)
            {
                next.push_back(current[even_idx++]);
            }
            else
            {
                next.push_back(current[odd_idx++]);
            }
        }

        current = std::move(next);
    }

    return current;
}

int main(int argc, char const *argv[])
{
    std::cout << "Initial: 012345" << std::endl;
    int n = 2;
    std::string encryptedText = encrypt("012345", n);
    std::cout << encryptedText << std::endl;
    std::string decryptedText = decrypt(encryptedText, n);
    std::cout << decryptedText << std::endl;
    return 0;
}