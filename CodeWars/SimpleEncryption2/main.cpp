#include <string>
#include <iostream>

class Kata
{
public:
    static std::string encrypt(const std::string &text)
    {
        return "";
    }

    static std::string decrypt(const std::string &encryptedText)
    {
        return "";
    }
};

int main(int argc, char const *argv[])
{
    Kata kata;

    std::string expected = "5MyQa9p0riYplZc";
    std::string actual = kata.encrypt("This is a test!");

    std::cout << expected << " ==? " << actual << std::endl;

    expected = "$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV9VuhO Iz3dqb.U0w";
    actual = kata.encrypt("Do the kata \"Kobayashi-Maru-Test!\" Endless fun and excitement when finding a solution!");
    std::cout << expected << " ==? " << actual << std::endl;

    expected = "5MyQa79H'ijQaw!Ns6jVtpmnlZ.V6p";
    actual = kata.encrypt("This kata is very interesting!");
    std::cout << expected << " ==? " << actual << std::endl;

    return 0;
}
