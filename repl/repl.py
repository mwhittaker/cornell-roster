import pymongo

LAMBDA = u'\u03BB'

def main():
    client  = pymongo.MongoClient()
    cornell = client.cornell
    roster  = cornell.roster
   
    try:
        while (True):
            # read
            print LAMBDA,
            query = raw_input()

            # eval
            cursor = roster.find({
                "title": {
                    "$regex": query, 
                    "$options": "i"
                }
            }).sort([
                ('subject', pymongo.ASCENDING),
                ('id'     , pymongo.ASCENDING)
            ])
    
            # print
            for doc in cursor:
                subject = doc["subject"]
                id      = doc["id"]
                title   = doc["title"]
                print "{:<5} {} {}".format(subject, id, title)

    except (EOFError, KeyboardInterrupt):
        pass

if __name__ == "__main__":
    main()
