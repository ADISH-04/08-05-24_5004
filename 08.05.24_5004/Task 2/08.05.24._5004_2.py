def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while prefix:
            if s.startswith(prefix):
                break
            prefix = prefix[:-1]
        else:
            return ""
    return prefix

example1 = ["flower", "flow", "flight"]
print("Use Case 1")
print(longest_common_prefix(example1))

example2 = ["dog", "racecar", "car"]
print("Use Case 2")
print(longest_common_prefix(example2))
