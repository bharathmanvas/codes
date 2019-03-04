def common(s1, s2):
        out = ''
        for i, j in zip(s1, s2):
            if i != j:
                break
            out += i
        return out
s1=input("enter")
s2=input("enter")
common(s1,s2)
print(common)
