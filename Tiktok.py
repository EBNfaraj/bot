def tk(link):
	import requests
	import json

	url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

	querystring = {"url":"link"}

	headers = {
		"X-RapidAPI-Key": "6423d18b88msha2723b467fec78bp165959jsne262a07329f3",
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	result = response.text
	rest = json.loads(result)
	return {"video":rest['video'][0],"music":rest['music'][0]}