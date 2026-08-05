class Solution:
    primary_delimiter = '.'
    secondary_delimiter = '/'

    def encode(self, strs: List[str]) -> str:
        decoder = ""
        encoded = ""
        for st in strs:
            decoder += str(len(st))+self.primary_delimiter
            encoded+=st
        decoder+=self.secondary_delimiter
        print(decoder+encoded)
        return decoder+encoded

    def decode(self, s: str) -> List[str]:
        message_start = s.find(self.secondary_delimiter)
        lengths = s[:message_start].split(self.primary_delimiter) 
        message_start+=1
        decoded = []
        for length in lengths:
            if length != '':
                decoded.append(s[message_start:message_start+int(length)])
                message_start += int(length)
        print(decoded)
        return decoded

    def encode2(self, strs: List[str]) -> str:
        encoded="º"
        for st in strs:
            encoded+=st+'º'
        return encoded

    def decode2(self, s: str) -> List[str]:
        return s.split("º")[1:-1]