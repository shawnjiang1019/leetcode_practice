class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # store file names and the smallest possible duplicate value
        folders = {}
        result = []
        for name in names:
            if name not in folders:
                result.append(name)
                folders[name] = 1
            else:
                k = folders[name]
                new_name = f"{name}({k})"
                while new_name in folders:
                    k += 1
                    new_name = f"{name}({k})"
                result.append(new_name)
                folders[name] = k + 1
                folders[new_name] = 1
        return result

