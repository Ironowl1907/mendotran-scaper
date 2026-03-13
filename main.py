# Mendotran requester
import requests

url = "https://mendotran.oba.visionblo.com/oba_api/api/where/stops-for-location.json"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://mendotran.oba.visionblo.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}

# HACK: lat, lon, latSpan and lonSpan should change dynamically
mendotran_request_stops_params = {
    "platform": "web",
    "v": "",
    "lat": "-32.74167391740799",
    "lon": "-68.70059967041017",
    "latSpan": "0.3742517721891758",
    "lonSpan": "1.2805938720703125",
    "version": "1.0",
}

def main():
    mendotran_request_stops(mendotran_request_stops_params)

def mendotran_request_stops(params):
    r = requests.get(url, params=params, headers=headers)
    print(r.status_code)
    print(r.json())
    return r

if __name__ == "__main__":
    main()
