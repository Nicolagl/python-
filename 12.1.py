def main():

    import os.path
    if os.path.isfile("wht.txt"):
        print("ecists")
    
    outfile=open("wht.txt","w")

    outfile.write("wstsdsb\n")
    outfile.write("wstmyxjj\n")
    outfile.close()
main()
