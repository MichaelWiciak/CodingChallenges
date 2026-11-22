For encrypting strings this region of chars is given (in this order!):

    all letters (ascending, first all UpperCase, then all LowerCase)
    all digits (ascending)
    the following chars: .,:;-?! '()$%&"

These are 77 chars! (This region is zero-based.)

Write two methods:

std::string encrypt(std::string text)
std::string decrypt(std::string text)

Prechecks:

    If the input-string has chars, that are not in the region, throw an Exception(C#, Python) or Error(JavaScript).
    If the input-string is null or empty return exactly this value!

For building the encrypted string:

    For every second char do a switch of the case.
    For every char take the index from the region. Take the difference from the region-index of the char before (from the input text! Not from the fresh encrypted char before!). (Char2 = Char1-Char2)
    Replace the original char by the char of the difference-value from the region. In this step the first letter of the text is unchanged.
    Replace the first char by the mirror in the given region. ('A' -> '"', 'B' -> '&', ...)

Simple example:

    Input: "Business"
    Step 1: "BUsInEsS"
    Step 2: "B61kujla"
        B -> U
            B (1) - U (20) = -19
            -19 + 77 = 58
            Region[58] = "6"
        U -> s
            U (20) - s (44) = -24
            -24 + 77 = 53
            Region[53] = "1"
    Step 3: "&61kujla"


Run: clang++ -Wall -std=c++26 main.cpp -o test.bin