#Anagram Checker

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    cnt1 = {}
    cnt2 = {}

   
    for char in str1:
        if char in cnt1:
            cnt1[char] += 1
        else:
            cnt1[char] = 1

    
    for char in str2:
        if char in cnt2:
            cnt2[char] += 1
        else:
            cnt2[char] = 1

    return cnt1 == cnt2

print(are_anagrams('iran', 'rain'))    
print(are_anagrams('tear', 'rate')) 
print(are_anagrams('home', 'land'))     






































# def is_anagram(str1,str2):
#     if len(str1) != len(str2):
#         return False
#     else:
#         return sorted(str1) == sorted(str2)
    