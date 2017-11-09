import warlock
import jsonify
import json
import realschema
from jsonschema import validate
import boto3
from random import randint

# create S3 boto3 resource
s3 = boto3.resource('s3')


# create the Company object. Add all the attributes according to the schema when you create the object
#Company = warlock.model_factory(testschema)
def createCompany(name,techname="",prod="",period=[],tech=[],folks=[]):

  Company = warlock.model_factory(realschema.schema)

  book = Company(technologies=tech, Name=name)
#cisco.product = "webex"
#cisco.keypersons = ["Kamran", "Karim"]
  #print(book.Name)

#Validate the schema before we write to file
  validation = validate(book, realschema.schema)
  #print(validation)
  if validation is None:
    #data = {}
    #data['Name'] = cisco.Name 
    #data['keypersons'] = cisco.keypersons
    # take the object and convert to JSON format which we will write to file
    json_data = json.dumps(book, indent=4,sort_keys=True)
    print(json_data)
    fname=name + ".json"
    with open(fname, 'w') as outfile:
      json.dump(book,outfile)
    return(fname)
filename = createCompany(name = "Cisco",tech = ["Java","Python"])
object = s3.Object('companyjsonlibrary', filename).put(Body=open(filename,'rb'))

#print(json_data)
