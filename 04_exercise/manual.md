# MongoDB and Redis
 
## Workstation

- Recommeded Ubuntu/MacOS with installed Docker
- MongoDB and [robomongo](https://robomongo.org/)([snap for ubuntu](https://snapcraft.io/install/robo3t-snap/ubuntu)) or other graphical tool for MongoDB
- redis and redis CLI

## MongoDB

MongoDB is a document-oriented (NoSQL) database with fixed schema.

0. What is the [MEAN](https://www.mongodb.com/mean-stack)/MERN stack?

1. Start a mongodb instance:

   ```bash
   docker run --publish 27017:27017 --name wsb-mgo -d mongo 
   ```

2. Connect MongoDB from [robomongo](https://robomongo.org/).

3. Check what databases, we have in the MongoDB

   ```bash
   show dbs
   ```

### First steps with MongoDB

1. Let's create our database:

   ```bash
   use myunviversity
   ```

2. Add data (notice the nested data struture):

   ```js
   db.students.insert({name: "Maria", student_id: "12",
               study_year: 1,
               student_group: {name: "Group A"}
               });

   db.students.insert({name: "Jane", student_id: "23", 
               study_year: 2,
               student_group: {name: "Group B"}
               });
   ```

3. Check whether you have two records:

   ```js
   db.students.count()

   // result
   // 2
   ```

4. Display the first item in the student **collection**:

   ```js
   db.students.findOne()

   // result
   // {
   //
   // }
   ```

   What is the *ObjectID?*?

5. Find limmited numer of results:

   ```js
   db.students.find().limit(2)
   ```

6. Query the data:


	```js
   //
   db.students.find({"name": "Jane"}).count()

   // nested structure in find
   db.students.find({"student_group.name": "Group A"}).count()

   // find bigger than
	db.students.find({study_year: {$gt: 1}})

   // sort
   db.students.find().sort({study_year: 1})
	```

7. Indices:

   ```js
   db.students.getIndexes()

   // create new one
   db.students.createIndex({"student_group.name": 1})
   ```

8. How to make joins? We need the [aggregation functions](https://docs.mongodb.com/upcoming/reference/operator/aggregation-pipeline/). In general, go for embedding unless you really really need to do joins.

   ```js
   db.grades.insert({"grade": 4.5, "student_id": "23" });

   //
   db.grades.find()

   //
   db.grades.aggregate([
   {
      "$lookup": {
         "from": "students",
         "localField": "student_id",
         "foreignField": "student_id",
         "as": "student" 
      }
   }
   ])
   ```

9. How would you model `course` in MongoDB? Please create new collection `courses` and insert the data.

10. What are advantages of MongoDB vs the SQL database?

    Other usual suspects: [PSQL](https://www.postgresql.org) with a good support for JSON operations and [AWS DynamoDB](https://aws.amazon.com/dynamodb/).

    Libraries: [python](https://docs.mongodb.com/drivers/pymongo/), [js](https://www.w3schools.com/nodejs/nodejs_mongodb_query.asp).

## Redis

Redis is an in-memory key-value data structure store that you can also use as a [NoSQL database](https://redis.com/nosql/what-is-nosql/), cache, or message broker. Redis and memcached are key elements of most of the infrastruture including, e.g., Github.

0. For caching, redis or memcached are the usual suspectes. More about differences [here](https://engineering.kablamo.com.au/posts/2021/memcached-vs-redis-whats-the-difference).

1. Start your instance:

   ```bash
   docker run --publish 6379:6379 --name wsb-redis -d redis
   ```

2. Let's see whether your instance works with `redis-cli` (more in [docs](https://redis.io/commands#generic)):

   ```bash
   docker exec -it wsb-redis /bin/bash

   root@d8a0:/data# redis-cli
   root@d8a0:/data# ping

   root@d8a0:/data# set mykey somevalue
   OK
   root@d8a0:/data# get mykey
   "somevalue"
   ```

3. Let's see how we would work with [redis-py](https://github.com/redis/redis-py) (more in [docs](https://developer.redis.com/develop/python/)):

   ```path
   python3 -m venv .venv
   source .venv/bin/activate

   pip install -r redis
   ```

   ```python
   # as key/value store
   import redis
    
   r = redis.Redis()
   # ping = r.ping()

   r.set("X2399999", "Radio")
   r.mset({"X2399128": "Dress", "Y832223": "Car"})
   v = r.get("X2399128")

   print("{}".format(v))
   ```

   ```python
   # as pubsub
   import redis
   import time

   r = redis.Redis(decode_responses=True, charset="utf-8")

   p = r.pubsub()
   p.subscribe("my-first-channel")

   r.publish("my-first-channel", "awesome data")

   msg = p.get_message()
   print(msg)

   msg = p.get_message()
   print(msg)
   ```

## Related

- [MongoDB basics](https://www.mongodb.com/basics)
- [MongoDB on w3schools](https://www.w3schools.com/nodejs/nodejs_mongodb.asp)
- [MongoDB Schema Design Best practices](https://www.mongodb.com/developer/article/mongodb-schema-design-best-practices/)
- [Redis documentation](https://redis.io/documentation)
<!-- https://betterprogramming.pub/getting-started-with-redis-a-python-tutorial-3a18531a73a6 -->
