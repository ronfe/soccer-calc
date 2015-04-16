import os, shelve, uuid

pwd = os.path.dirname(os.path.realpath(__file__))
os.chdir(pwd)

def getTeamList(filePath):
    f = open(filePath, 'r').readlines()
    g = []
    for each in f:
        g.append(each.strip())
        
    return g

def initClub(clubName):
    f = shelve.open(pwd+'/clubs/'+clubName+'.cl')
    f['id'] = uuid.uuid4()
    f['name'] = clubName
    f['match'] = []
    f['keyMatch'] = []
    f['thetaPoint'] = 0
    f['points'] = 0
    f['goal'] = 0
    f['against'] = 0
    f.close()
    