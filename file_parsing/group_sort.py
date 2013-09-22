#!/usr/bin/python

DEFAULT_FILENAME = '/etc/passwd'
MIN_USERS = 5

def count_groups(filename=None):
    
   grplist = []
   if not filename:
       filename = DEFAULT_FILENAME
   f = open(filename, "r")
   stopped = None
   while not stopped:
       line = f.readline()
       stopped = not line
       linelst = line.split(':')
       if len(linelst) < 4:
           continue
       groupno = linelst[3]
       if not groupno in grplist:
           grplist.append(groupno)
   f.close()
   print "total unique groups: %d" % len(grplist)
   return grplist
       

def histogram_groups(filename=None):

   hist_grplist = {}
   if not filename:
       filename = DEFAULT_FILENAME
   grplist = count_groups(filename)
   f = open(filename, "r")
   stopped = None
   while not stopped:
       line = f.readline()
       stopped = not line
       linelst = line.split(':')
       if len(linelst) < 4 :
           continue
       groupno = linelst[3]
       uid = linelst[2]
       username = linelst[0]
       if not hist_grplist.get(groupno, None):
           hist_grplist[groupno] = []
       hist_grplist[groupno].append((username, uid))
   #print "Groups: %s" % hist_grplist
   return hist_grplist


def popular_groups(filename=None, min_users=None):

    if not min_users:
        min_users = MIN_USERS
    histogram = histogram_groups()
    for gid in histogram:
        tup = histogram[gid]
        if len(tup) > min_users:
            print "gid: %s, users: %d, %s" % (gid, len(tup), tup)

#count_groups()
#popular_groups(min_users=2)
