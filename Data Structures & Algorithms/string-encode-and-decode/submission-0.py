class Solution:

    def encode(self, strs: List[str]) -> str:
        resu = ""
        for x in strs:
           resu += str(len(x))+ "#" + str(x) 
        return resu

    def decode(self, s: str) -> List[str]:
        i = 0
        deco = []
        while ( i < len(s)):
            j = i
            while(s[j] != "#"):
                j +=1
            lenth = int(s[i:j])
            word = s[j+1:j+1+ lenth]

            i = j+lenth+1
            deco.append(word)
        return deco
