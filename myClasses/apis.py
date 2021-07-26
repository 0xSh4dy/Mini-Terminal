from pprint import pformat
import requests
import json
class Apis:
    def jokeApi(self,category=''):
        url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"
        filter = str(category)
        filter = filter.replace(" ","")
        queryString = {"format":"json","contains":filter}
        headers = {'x-rapidapi-key': "b7d43b6896mshf7112da639a3c2dp145b9ajsn394528a6394f",
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
            'x-rapidapi-key': "b7d43b6896mshf7112da639a3c2dp145b9ajsn394528a6394f",
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
    
    def weatherApi(self,city):
        key = "7b7e2d38973b2d857874398ea4af4d5c"
        url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
        response = requests.get(url=url)
        response = response.text
        response = pformat(json.loads(response))
        return response

    def movieApi(self,movie):
        key = "931573fc170c73de9b62e451e44f666b"
        url = f"https://api.themoviedb.org/3/search/movie?api_key={key}&query={movie}"
        response = requests.get(url=url).text
        response = json.loads(response)
        response = response['results']
        response = response[0]
        title = response['original_title']
        overview = response['overview']
        popularity = response['popularity']
        release_date = response['release_date']
        vote_average = response['vote_average']
        result = {'title':title,'overview':overview,'popularity':popularity,'release_date':release_date
                ,'vote_average':vote_average}
        result = json.dumps(result)
        return result        

    def imageApi(self,image='random'):
        client_id = "jc49qWiXIEV3_dp8wcWqyDQGactRlbv2_kvWpLt6zuA"
        url = f"https://api.unsplash.com/search/photos/?client_id={client_id}&query={image}"
        response = requests.get(url=url).text
        response = json.loads(response)
        try:
            response = response['results']
            response = response[0]['urls']
            response = response['small']
        except(IndexError):
            response = "No"
        return response
        