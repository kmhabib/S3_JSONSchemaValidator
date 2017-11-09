schema = {
 
  
  "title": "company",
  "type" : "object",
  "properties" : {
     "Name" : {
       "type" : "string"
     },
     "techname" : {
       "type" : "string"
     },
     "product" : {
       "type" : "string"
     },
     "when" : {
       "type" : "string"
     },
     "technologies" : {
       "type" : "array",
       "tech" : {
         "type" : "string"
       }
     },
     "keypersons" : {
       "type" : "array",
       "person" : {
         "type" : "string"
       }
     }
     
     
  },
  "required": ["Name"]

}