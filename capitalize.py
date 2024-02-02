def solve(s):
    ans = s.split(" ")
    ans1 = (i.capitalize() for i in ans)
    return " ".join(ans1)


# passes all test cases that s.title doesn't
