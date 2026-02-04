class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        for s in strs:
            length = len(s)
            result += str(length) + "/" + s
        return result

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        # find the first index of delimiter: "/"
        cur_string = s
        while cur_string:
            idx = cur_string.index("/")
            length = int(cur_string[:idx])
            cur_string = cur_string[idx + 1:]
            content = cur_string[:length]
            result.append(content)
            cur_string = cur_string[length:]
        return result
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))