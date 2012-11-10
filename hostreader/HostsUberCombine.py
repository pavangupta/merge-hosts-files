import os
import glob


# Let me open the uber hosts file first...
newHostsFile = open('dc1hosts_final.txt')
# I'll store all of my hosts information in a list of dicts where the first variable (the IP) is the key
# key and the host names are all the values.  Comments will be ignored.
originalList = []
# Ignore lines that start with #, and split away the comments and ensure the line is not empty before moving
for columns in (line.strip().split("#")[0].split() for line in newHostsFile if not line.startswith('#') and line.strip()):
    originalList.append({columns[0]:set(columns[1:])})
    #print [{columns[0]:set(columns[1:])}]
    
# Let me run through the hosts files I have by looking in the old directory for files
path = 'old/'
for infile in glob.glob(os.path.join(path,'*')):
    print "current file is:" + infile
    f = open(infile)
    # Ignore lines that start with #, and split away the comments and ensure the line is not empty before moving
    for columns in (line.strip().split("#")[0].split() for line in f if not line.startswith('#') and line.strip()):
        #print {columns[0]:set(columns[1:])}
        matches = [i for i,x in enumerate(originalList) if x.keys()[0] == columns[0]]
        # if I have a new IP address in one of the hosts files I'm checking, let me append it to my original list
        if not matches:
            originalList.append({columns[0]:set(columns[1:])})
            matches = [len(originalList)-1]
            #print "new match!"
            #print {columns[0]:set(columns[1:])}
            #print originalList[matches[0]]
        #print "----- matches for "+ columns[0] + " ------"
        for match in matches:
            # the next line just makes my printing a lot less stupid -- i'm able to compare what I had before with
            # what I changed and when it's different I print something.
            oldOriginalForPrintSpeed = originalList[match][columns[0]]
            # lets update our list when there's new stuff I'm seeing in a hosts file I'm checking
            originalList[match][columns[0]] = originalList[match].values()[0] | set(columns[1:])
            # uncomment the lines below to see the script run through and make updates to stuff
            #if originalList[match][columns[0]] != oldOriginalForPrintSpeed:
                #print originalList[match][columns[0]]

for i,x in enumerate(originalList):
    print x.keys()[0] + "\t" + '%s' % '\t'.join(map(str, list(x.values()[0])))