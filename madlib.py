import re
def madlib():
    fresh=open("fresh.txt", 'w+') #fresh.txt is just an empty text file where the changed paragraph is written.
    story=open("story.txt", 'r')
    with open("write.txt", 'r+') as output:
        read=story.readlines()
        write=output.readlines()
#        print(read)
#        print(write)
        for iter in range(0,11):
                print(read[iter], '\n')
                choice= input("enter choice:")
                line=write[iter]
                linenew=re.sub("_", choice, line)
                fresh.write(linenew)
        print("the final story is:")
        fresh.seek(0)
        final=fresh.read()
        print(final)

#if __name__== "__main__":
madlib()
fresh=open("fresh.txt", 'r+')
fresh.truncate()
fresh.close()
    
