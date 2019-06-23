import time
import threading
import cognitive_face as CF
import csv

KEY = ''  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

interval = 80
count =-17
white_actors=[]
white_actors_api_age=[]

f = open('caucasian_celebs2.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

for line in rdr:
    print(line)
    if (len(line)!= 0): #exclude empty elements
        if(line[0]!=''):
            white_actors.append(line)
print(white_actors)
def add_count():
    global count
    count=count+17
    print(count)
    return count

def doit(args):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        threading.Timer(interval, startTimer).start() #start
        index = add_count()
        print("count:"+ str(index))
        if(index<len(white_actors)):
            if(index==len(white_actors)-1):
                iterator = white_actors[index:]
                myPeriodicFunction(iterator)
            else:
                iterator = white_actors[index:index+17]
                print(iterator)
                myPeriodicFunction(iterator)
        else:
            write_csv()
        print("sleeping 100 secs")
        time.sleep(100)

def myPeriodicFunction(iterator):
    print("This loops on a timer every %d seconds" % interval)
    for item in iterator:
        print(item[0])
        img_url = item[1]
        faces = CF.face.detect(img_url, attributes='age')
        for attr in faces:
            print(attr['faceAttributes']['age'])
            api_age=[]
            api_age.append(item[0])
            api_age.append(attr['faceAttributes']['age'])
            print(api_age)
            white_actors_api_age.append(api_age)

def write_csv():
    with open("caucasian_celebs2_face_api.csv", 'w', encoding='utf-8') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(white_actors_api_age)
    print(white_actors_api_age)
    print("finished!")
    exit()

def startTimer():
    t = threading.Thread(target=doit, args=("task",))
    t.start()
    print("blah")
    time.sleep(100)
    t.do_run = False
    t.join()

startTimer()