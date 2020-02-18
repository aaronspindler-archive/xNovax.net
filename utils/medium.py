import requests


def get_posts(user, num_posts):
	url = "https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@{}?format=json".format(user)
	response = requests.get(url)
	json = response.json()
	return json['items'][0:num_posts]