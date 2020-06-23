# Chapter.7
##No.8 Name search for popular name between 2000 and 2009.

def readGirlNames(fileName):
    girlsNamesFile = open(fileName, "r")
    girlsNamesList = []

    girlName = girlsNamesFile.readline()
   
    while girlName != "":
        girlName = girlName.rstrip('\n')
        girlsNamesList.append(girlName)
        girlName = girlsNamesFile.readline()
    

    return girlsNamesList

def readBoysNames(fileName):
    boysNamesFile = open(fileName, "r")
    boysNamesList = []

    boyName = boysNamesFile.readline()

    while boyName != "":
        boyName = boyName.rstrip('\n')
        boysNamesList.append(boyName)
        boyName = boysNamesFile.readline()
    

    return boysNamesList

def getusersearchnames():
    usersearchname = input('Please enter the first name to search for:')
    usersearchnamelist = []

    while usersearchname != "-1":
        usersearchnamelist.append(usersearchname)
        usersearchname = input('Please enter next name to' +\
                               'search for or -1 to continue:')
    return usersearchnamelist

def searchForName(usersearchnamelist, allNamesList):

    foundnames =[]

    for usersearchnamelistIndex in range(len(usersearchnamelist)):
        if usersearchnamelist[usersearchnamelistIndex] in allNamesList:
            foundnames.append(usersearchnamelist[usersearchnamelistIndex])

    return foundnames


def printserachresults(usersearchnamelist, foundnames):
    for usersearchnamelistIndex in range(len(usersearchnamelist)):
        if usersearchnamelist[usersearchnamelistIndex] in foundnames:
            print(usersearchnamelist[usersearchnamelistIndex], 'was a popular name '\
                  'between 2000 and 2009')
        else:
            print(usersearchnamelist[usersearchnamelistIndex], 'was not popular name '\
                  'between 2000 and 2009')
            

def main():
    girlsFileName = "GirlNames.txt"
    boysFileName = "BoyNames.txt"

    girlsNamesList = readGirlNames(girlsFileName)
    boysNamesList = readBoysNames(boysFileName)
    AllNamesList = girlsNamesList + boysNamesList
    userSearchNamesList = getusersearchnames()
    foundnamesList = searchForName(userSearchNamesList, AllNamesList)
    printserachresults(userSearchNamesList, foundnamesList)
main()



