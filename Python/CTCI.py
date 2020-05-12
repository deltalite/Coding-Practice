## Chapter 1
# 1.1
def all_unique(s):
    letters = set()
    for c in s:
        if c in letters:
            return False
        else:
            letters.add(c)
    return True

print('1.1')
assert all_unique('asdfqwer ')
assert not all_unique('2344')

# 1.2
def is_permutation(s1,s2):
    if len(s1) != len(s2):
        return False
    l = {}
    for c in s1:
        if c not in l:
            l[c] = 1
        else:
            l[c]+=1
    for c in s2:
        if c not in l:
            return False
        elif l[c] == 1:
            l.pop(c)
        else:
            l[c] -= 1
    return True

print('1.2')
assert is_permutation('asdf','fdas')
assert not is_permutation('afe','sdf')
    

# 1.6
def str_comp(s):
    if s=='':
        return ''
    i=1
    newstr=s[0]
    num=1
    while i<len(s):
        if s[i]==s[i-1]:
            num+=1
        else:
            newstr += str(num)+s[i]
            num=1
        i+=1
    newstr += str(num)
    return newstr

print('1.6')
assert str_comp('aabcccccaaa')=='a2b1c5a3'

## Chapter 2

# 2.1
def remove_dups1(ll):
    if ll.next == None:
        return ll
    cur = ll
    seen = set(cur.val)
    while cur.next is not None:
        if cur.next.val not in seen:
            seen.add(cur.next.val)
            cur = cur.next
        else:
            cur.next = cur.next.next
    return ll

