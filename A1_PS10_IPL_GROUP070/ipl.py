class IPL:
    PlayerTeam = [] # list containing players and teams.
    edges = [[],[]] # matrix of edges or associations

    def readInputfile(self, inputfile):
        """
        This function reads the input file containing the name of the franchises
        and associated players in one line.

        The name of the player and franchises should be separated by a slash.

        Input file format, RR, KXIP, KKR are franchinses separated by players like Franchise/Player/Player/Player/Player/Player

        RR / Ben Stokes / Jaydev Unadkat / Sanju Samson / Jofra Archer / G Krishnappa
        KXIP / KL Rahul / R Ashwin / Andrew Tye / Marcus Stoinis / Glenn Maxwell
        KKR / Chris Lynn / Mitchell Starc / Dinesh Karthik / Robin Uthappa / Manish Pandey / Chris
        Woakes
        SRH / Manish Pandey / Rashid Khan / Shikhar Dhawan
        MI / Krunal Pandya / Ishan Kishan / G Krishnappa / Kieron Pollard
        CSK / Kedar Jadhav / Dwayne Bravo / Karn Sharma
        RCB / Chris Woakes / Yuzvendra Chahal / Umesh Yadav / KL Rahul / Mitchell Starc
        DD / Glenn Maxwell / Sanju Samson / Kedar Jadhav / Karun Nair
        GL / Dinesh Karthik / Andrew Tye / Dwayne Bravo / Ishan Kishan
        RPS / Ben Stokes / Jaydev Unadkat

        The function creates relevant vertices for the players and franchises
        and relevant edges to indicate the connection of a franchise and its players.
        And ensures that none of the players or franchises get repeated
        while creating the vertices of the graph.

        """
        teamplayers = set()
        self.edges.clear()
        with open(inputfile) as file:
            for line in file:
                itemNo = 0
                itemValueAtZero = ''
                for item in line.strip().split('/'):
                    item = item.strip()
                    teamplayers.add(item)
                    if itemNo == 0:
                        teamplayers.add(item)
                        itemValueAtZero = item
                    else:
                        self.edges.append([itemValueAtZero, item])
                    itemNo += 1
        self.PlayerTeam = list(teamplayers)

    def displayAll(self):
        """
        This function displays the total number (count) of unique players and franchises entered through the input file.

        It also list out the unique players and franchises.

        The output of this function pushed into outputPS10.txt file.

        The output format should be as mentioned below.

        --------Function displayAll--------
        Total no. of franchises: 10
        Total no. of players: 28
        List of franchises:
        RR
        KXIP
        KKR
        SRH
        MI
        CSK
        RCB
        DD
        GL
        RPS

        List of players:
        Ben Stokes
        Jaydev Unadkat

        """
        teams=set()
        players=set()

        for edge in self.edges:
            teams.add(edge[0])
            players.add(edge[1])

        with open('outputPS10.txt', 'w') as file:
            file.write("--------Function displayAll--------\n")
            file.write("Total no. of franchises: %i\n" %len(teams))
            file.write("Total no. of players: %i\n" %len(players))
            file.write("List of franchises:\n")
            for team in teams:
                file.write(team)
                file.write("\n")
            file.write("\n")
            file.write("List of players:\n")
            for player in players:
                file.write(player)
                file.write("\n")
            file.write("-----------------------------------------\n")

    def displayFranchises(self, player=None):
        """
        This function displays all the franchises a particular player is associated with.
        The function reads the input franchise name from the file promptsPS10.txt

        where the search id is mentioned with the tag as shown below.
        findFranchise: Ben Stokes
        findFranchise: Robin Uthappa

        The output of this function should be appended into outputPS10.txt file.
        If a franchise is not found, an appropriate message should be output to the file.
        The output format should be as mentioned below.

        --------Function displayFranchises --------
        Player name: Ben Stokes
        List of Franchises:
        RR
        RPS (if franchise is not found display appropriate message)
        -----------------------------------------
        """
        playerFranchices = []
        with open('promptsPS10.txt') as file:
            for line in file:
                data = line.split(":")
                if data[0].strip() == "findFranchise":
                    player = data[1].strip()
                    franchices = []
                    for edge in self.edges :
                        if edge[1]==player :
                            franchices.append(edge[0])
                    playerFranchices.append([player, franchices])


        with open('outputPS10.txt', 'a') as file:
            file.write("--------Function displayFranchises --------\n")
            for playerFranchice in playerFranchices :
                file.write("Player name: "+playerFranchice[0]+"\n")
                file.write("List of Franchises:\n")
                if len(playerFranchice[1])==0:
                    file.write("No franchise found\n")
                else:
                    for franchise in playerFranchice[1] :
                        file.write(franchise+"\n")
                file.write("\n")
            file.write("-----------------------------------------\n")

    def displayPlayers(self, franchise=None):
        """
        This function displays all the players associated with a franchise.
        The function reads the input franchise name from the file promptsPS10.txt

        where the search id is mentioned with the tag as shown below.
        listPlayers: RR
        listPlayers: SRH

        The output of this function should be appended into outputPS10.txt file.
        If a player is not found, an appropriate message should be output to the file.

        The output format should be asmentioned below.
        --------Function displayPlayers --------
        Franchise name: RR
        List of Players:
        Ben Stokes
        Jaydev Unadkat
        Sanju Samson

        Jofra Archer
        G Krishnappa (if player is not found, display appropriate message)
        -----------------------------------------
        """
        franchisePlayers = []
        with open('promptsPS10.txt') as file:
            for line in file:
                data = line.split(":")
                if data[0].strip() == "listPlayers":
                    franchise = data[1].strip()
                    players = []
                    for edge in self.edges :
                        if edge[0]==franchise :
                            players.append(edge[1])
                    franchisePlayers.append([franchise, players])


        with open('outputPS10.txt', 'a') as file:
            file.write("--------Function displayPlayers --------\n")
            for franchisePlayer in franchisePlayers :
                file.write("Franchise name: "+franchisePlayer[0]+"\n")
                file.write("List of Players:\n")
                if len(franchisePlayer[1])==0:
                    file.write("No Players found\n")
                else:
                    for player in franchisePlayer[1] :
                        file.write(player+"\n")
                file.write("\n")
            file.write("-----------------------------------------\n")

    def franchiseBuddies(self, playerA=None, playerB=None):
        """
        Uses one of the traversal techniques to find out if two players are related to each other through one common franchise.
        The function reads the input player names from the file promptsPS10.txt

        where the search id is mentioned with the tag as shown below.
        franchiseBuddies: Krunal Pandya : Kieron Pollard

        The output of this function should be appended into outputPS10.txt file.
        If a relation is not found, an appropriate message should be output to the file.

        The output format should be as mentioned below.
        --------Function franchiseBuddies --------
        Player A: Krunal Pandya
        Player B: Kieron Pollard
        Franchise Buddies: Yes, MI (if no, display appropriate message)
        ------------------------------------------
        """
        if (playerA == None) or (playerB == None):
            with open('promptsPS10.txt') as file:
                for line in file:
                    data = line.split(":")
                    if data[0].strip() == "franchiseBuddies":
                        self.franchiseBuddies(data[1], data[2])
        else:
            playerAFranchise=set()
            playerBFranchise=set()
            commonFranchise=set()
            for edge in self.edges:
                if(edge[1]==playerA.strip()):
                    playerAFranchise.add(edge[0])
                if(edge[1]==playerB.strip()):
                    playerBFranchise.add(edge[0])
                commonFranchise=playerAFranchise.intersection(playerBFranchise)
                if len(commonFranchise)>0:
                    break
            with open('outputPS10.txt', 'a+') as file:
                file.write("\n--------Function franchiseBuddies--------\n")
                file.write("Player A: %s\n" %playerA)
                file.write("Player B: %s\n" %playerB)

                if bool(commonFranchise):
                    file.write("Franchise Buddies: Yes, ")
                    file.write("%s\n" %commonFranchise.pop())
                else:
                    file.write("Franchise Buddies: No, ")
                    file.write("No common Franchise")

    def bfs(self, playerA=None,playerB=None):
        adjList={}
        for edge in self.edges:
            adjList.setdefault(edge[0],[]).append(edge[1])
            adjList.setdefault(edge[1],[]).append(edge[0])

        #BFS
        queue=[(playerA,[playerA])]
        while queue:
            (vertex,path)= queue.pop(0)
            for next in set(adjList[vertex]) - set(path):
                if next == playerB:
                    return path+[next]
                else:
                    queue.append((next,path+[next]))

    def findPlayerConnect(self, playerA=None, playerB=None):
        """
        Uses BFS traversal techniques to find out if two players A and B are related to each other
        through a common franchise member C as defined in the question above.

        The function reads the input player names from the file promptsPS10.txt

        where the search id is mentioned with the tag as shown below.
        playerConnect: Kedar Jadhav : Ishan Kishan

        Display the entire relation that links player A and player B.
        The output of this function should be appended into outputPS10.txt file.

        If a relation is not found, an appropriate message should be output to the file.

        The output format should be as mentioned below.
        --------Function findPlayerConnect --------
        Player A: Kedar Jadhav
        Player B: Ishan Kishan
        Related: Yes, Kedar Jadhav > MI > Dwayne Bravo > GL > Ishan Kishan

        (if no, display appropriate message)
        """
        with open('promptsPS10.txt') as file:
            for line in file:
                data = line.split(":")
                if data[0].strip() == "playerConnect":
                    playerA=data[1].strip()
                    playerB=data[2].strip()
                    finalPath=self.bfs(playerA,playerB)
                    with open('outputPS10.txt', 'a+') as file:
                        file.write("\n--------Function findPlayerConnect--------\n")
                        file.write("Player A: %s\n" %playerA)
                        file.write("Player B: %s\n" %playerB)

                        if bool(finalPath):
                            file.write("Yes, ")
                            file.write(" > ".join(finalPath))
                        else:
                            file.write("No, Unable to connect players")