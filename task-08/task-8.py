import json, os

organization = "amfoss"

org_url = "https://api.github.com/orgs/" + organization + "/repos"
curl_request = "curl -s " + org_url + " >> repo_list.json"
os.system(curl_request)
os.system("touch task-8.json")
i = open('repo_list.json')
data = json.load(i)
i.close()
os.system("rm repo_list.json")
key = "name"
res = [ sub['name'] for sub in data ]
os.system("touch sirPercevalsJourney.sh")
tPJ = open("sirPercevalsJourney.sh", 'a')
for x in res:
    perceval_request = "perceval git --json-line https://github.com/" + organization + "/" + x + " >> commits.json"
    tPJ.write(perceval_request)
    tPJ.write("\n")
    tPJ.write("cat task-8.json")
    tPJ.write("\n")
tPJ.close()
os.system("chmod +x sirPercevalsJourney.sh")
os.system("./sirPercevalsJourney.sh")
os.system("rm sirPercevalsJourney.sh")
os.system("rm task-8.json")
