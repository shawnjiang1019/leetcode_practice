class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # store a filename, content pair where content is the key
        data = {}
        result = []

        for string in paths:
            files = string.split()
            root = files[0]
            for i in range(1, len(files)):
                filename, content = files[i].split('(')
                content = content[:-1]
                if content not in data:
                    data[content] = [root + "/" + filename]
                else:
                    data[content].append(root + "/" + filename)
        for key in data.keys():
            if len(data[key]) > 1:
                result.append(data[key])
        
        return result

