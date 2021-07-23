from pprint import pformat
import requests
import json
class Apis:
    def jokeApi(self,category=''):
        url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"
        filter = str(category)
        filter = filter.replace(" ","")
        queryString = {"format":"json","contains":filter}
        headers = {'x-rapidapi-key': "your api key",
                    'x-rapidapi-host': "jokeapi-v2.p.rapidapi.com"}
        response = requests.get(url=url,headers=headers,params=queryString)
        dat = response.text
        dat = json.loads(dat)
        dat.pop('lang')
        dat.pop('error')
        dat.pop('id')
        dat.pop('safe')
        return dat

    def searchApi(self,query):
        url='https://google-search5.p.rapidapi.com/google-serps/'
        queryString= {"q":query,"page":"1","rank":1,"hl":"en-US","autocorrect":"1"}
        headers = {
            'x-rapidapi-key': "your api key",
            'x-rapidapi-host': "google-search5.p.rapidapi.com"
                }
        response = requests.get(url=url,headers=headers,params=queryString)
        response = response.text
        response = json.loads(response)
        x = response['data']
        b = x['results']
        c=b['organic']
        d = c[0]
        e=d['snippet']
        return e
        
