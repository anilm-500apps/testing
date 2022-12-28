from sheets import Sheets
import json
import os
import time

google_sheets = {"P0":"P0 Keywords" ,"P1" : "P1 Keywords" ,"Competitors" : "Competitor Keywords"}

def append_to_json_file(app_name,search_key, search_value, dic):
    if not os.path.exists("/root/infinity-seo/test.json"):
        open("/root/infinity-seo/test.json", "x")
        f = open("/root/infinity-seo/test.json", "a")
        f.write("{ }")
        f.close()
    with open("/root/infinity-seo/test.json","r+") as fil :
        data = json.load(fil)
        try:
            data[app_name][search_key][search_value] = dic
        except:
            try:
                data[app_name][search_key]={}
                data[app_name][search_key][search_value] = dic
            except:
                data[app_name]={}
                data[app_name][search_key]={}
                data[app_name][search_key][search_value] = dic

        fil.truncate(0)
        fil.seek(0)
        json.dump(data, fil, indent=4)
        fil.close()

def run_code():
    for sheet in google_sheets:
        gc = Sheets('1OszpoNl15T-U5UtIqhkhLsge2XM31FiWQrtEOjYjK1o',sheet)
        all_profiles = gc.get_all_records()
        for i in all_profiles:
            # print(i)
            app_name = i["App"]
            search_key = google_sheets[sheet]
            search_value = i[search_key]
            dic = {
                'Rank':i["Rank"],
                'Link':i["Link"],
                'Date':i["Date"]
            }
            # print(app_name,search_key,search_value,dic)
            append_to_json_file(app_name,search_key, search_value, dic)


condition = True
while condition:
    try:
        run_code()
        validate_output = open("/root/infinity-seo/test.json" , "r")
        json.load(validate_output)
        condition = False
    except:
        if os.path.exists("/root/infinity-seo/test.json"):
            os.remove("/root/infinity-seo/test.json")


time.sleep(20)
old_file = open("/root/infinity-seo/test.json" , "r")
old_data=json.load(old_file)
with open("/root/infinity-seo/test-dummy.json","w") as new_file:
    json.dump(old_data,new_file)
