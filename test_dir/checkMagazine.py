def checkMagazine(magazine, note):
    mag_hash={}
    for w in magazine:
        if w not in mag_hash:
            mag_hash[w]=1
        else:
            mag_hash[w]+=1

    print("dict = {}".format(mag_hash))
    for w in note:
        print("Note word={}".format(w))
        if w in mag_hash and mag_hash[w]!=0 :
            mag_hash[w]-=1
        else:
            print("No")
            return

    print("Yes")

if __name__ == '__main__':
    m="o l x imjaw bee khmla v o v o imjaw l khmla imjaw x".split()
    n="imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o".split()
    checkMagazine(m,n)