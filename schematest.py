import warlock

schema = {
"definitions": {
  "company" : {
    "type" : "object",
      "propherties" : {
                "Name" : { "type" : "string"},
                "ZipCode" : {"type" : "string"},
                "Ph1" : {"type" : "string"},
                "Ph2" : {"type" : "string"},
                "Address1": {"type" : "string"},
                "Address2": {"type" : "string"},
                "Fax": {"type" : "string"},
                "WebAddress" : {"type" : "string"},
                "SrcURL" : {"type" : "string"},
                "FacebookUrl": {"type" : "string"},
                "TwitterUrl": {"type" : "string"},
                "LinkedinUrl": {"type" : "string"},
                "InstagramURI": {"type" : "string"},
                "GooglePlusUrl": {"type" : "string"},
                "DNBCode": {"type" : "string"},
                "ParentBranch": {"type" : "number"},
                "Logo": {"type" : "string"},
                "SEOKeyword": {"type" : "string"},
                "IntentKeyword": {"type" : "string"},
                "Company_Type_Id": {"type" : "number"},
                "City_Id": {"type" : "number"},
                "Employee_Range_Id": {"type" : "number"},
                "Revenue_Range_Id": {"type" : "number"},
                "Employee_Range": {"type" : "string"},
                "Revenue_Range": {"type" : "string"},
                "Entity_Type_Id": {"type" : "number"},
                "BritishDoNotCallList": {"type" : "number"},
                "AssetUsd": {"type" : "string"},
                "State_Id": {"type" : "number"},
                "Country_Id": {"type" : "number"},
                "PreTaxProfitUsd": {"type" : "string"},
                "SalesUsd": {"type" : "string"},
                "TotalLiabilitiesUsd": {"type" : "string"},
                "type": ["array", "null"],
                "Technology" : {
                  "type" : "object",
                  "properties": {
                    "Technology_Category_Id" : { "type" : "string"},
                    "Technology_Name" : { "type" : "string"},
                    "Time_Period" : { "type" : "string"},
                    "Key_Person" : { "type" : "string"},
                    "Affiliated_Techs" : {
                      "type" : ["array", "null"],
                      "items" : {
                        "properties" : {
                        "Affiliated_TechName" :  { "type" :"string"}
                        }
                      }
                    },
                    "Products_Used" : { 
                      "type" : ["array", "null"],
                      "items" : {
                        "properties" : {
                          "Product_Id" : { "type" : "string"},
                          "Product_Name" : { "type" : "string"}
                      }
                    }
                  }
                    
                }
              }
                
            }
              
        }
    }
}

Company = warlock.model_factory(schema)

cisco = Company(Name="Cisco", ZipCode="12345", WebAddress="http://www.cisco.com")

print(cisco)

