class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + "#" + string 
        return encodedString

    def decode(self, s: str) -> List[str]:
        array_of_strings = []
        length_of_string = 0
        i = 0
        while i < len(s):
            5#Hello5#World
            j = i
            while s[j] != "#":
                j += 1
            length_of_string = int(s[i:j])
            array_of_strings.append(s[j+1:j+1+length_of_string])
            i = j+1+length_of_string
        return array_of_strings
