import MySQLdb
import sys
import os
import httplib
import json
import optparse
import datetime
import time
import calendar

url='cmsweb.cern.ch'

dbname = "relval"

while True:

    os.system("if [ -f batches.html ]; then rm batches.html; fi")
    
    sys.stdout = open('batches.html','a')

    print "<html>"
    print "<head><title>batches</title>"
    print "</head>"
    print "<body>"



    print "last update = " + str(datetime.datetime.now())
    print "<br>"

    print "<form action=\"http://localhost:50000/cgi-bin/handle_POST_2.py\" method=\"post\">"

    conn = MySQLdb.connect(host='localhost', user='relval', passwd='relval')

    curs = conn.cursor()
    
    curs.execute("use "+dbname+";")
    
    #workflow = line.rstrip('\n')
    #curs.execute("insert into workflows set hn_req=\""+hnrequest+"\", workflow_name=\""+workflow+"\";")

    curs.execute("select * from batches order by batch_id")
    batches=curs.fetchall()

    for batch in batches:
        if batch[7] != "inserted":
            continue
        print "<br>"        
        print "batch "+str(batch[0])+": "+str(batch[1])+"<br>"
        print "<input  name='batch"+str(batch[0])+"' value='approve' type='radio'/> approve <input  name='batch"+str(batch[0])+"' value='disapprove' type='radio'/> disapprove <input checked='checked' name='batch"+str(batch[0])+"' value='null' type='radio'/> do nothing<br/>"

    print "<br>"    
    print "<input type=\"submit\" value=\"Submit\"/>"

    print "</form>"
    print "</body>"
    print "</html>"
        
    sys.stdout.flush()
    
    #os.system("scp relval_monitor.txt relval@vocms174.cern.ch:~/webpage/")

    sys.exit(0)
    time.sleep(60)


