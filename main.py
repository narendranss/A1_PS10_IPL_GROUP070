from A1_PS10_IPL_GROUP070.ipl import IPL

def main():
    print("Executing main program")
    ipl = IPL()
    output = ipl.readInputfile("inputPS10.txt")
    ipl.displayAll()
    ipl.displayFranchises('')
    ipl.displayPlayers('')
    ipl.franchiseBuddies(None, None)
    ipl.findPlayerConnect(None, None)
    print("Done!!!")

if __name__ == '__main__':
    main()