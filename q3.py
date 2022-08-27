from timer import timeit

@timeit(loops = 10000)
def lengthOfLongestSubstring_1(s: str) -> int:  
    if len(s) == 0:
        return 0
    sub_str_set = set()
    sub_str = ""
    max_sub_str = 1
    for c in s:
        update = True
        if c not in sub_str_set:
            sub_str_set.add(c)
        else:
            if c in sub_str:
                update = False
                while c in sub_str and len(sub_str) != 0:
                    sub_str = sub_str[1:len(sub_str)]
        sub_str += c
        if sub_str not in sub_str_set:
            sub_str_set.add(sub_str)
            if update and len(sub_str) > max_sub_str:
                max_sub_str = len(sub_str)
    return max_sub_str


print(lengthOfLongestSubstring_1("mtmzuxtm"))