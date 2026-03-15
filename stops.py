import requests

stops_url = "https://owa.visionblo.com/api/mendoza/search"
stops_info_url = "https://owa.visionblo.com/api/mendoza/arrivals"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0",
    "Accept": "*/*",
    "Accept-Language": "es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "Content-Type": "application/json",
    "Origin": "https://owa.visionblo.com",
    "Referer": "https://owa.visionblo.com/web/mendoza/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}


def mendotran_request_stops():
    payload = {
        "token": "OQkGfHEQqWRO9zXRQgJb",
        "text": "",
        "xss": "86adb365fced6934d3ff6bec",
        "search": ["stops"],
        "no_favorites": True
    }
    r = requests.post(stops_url, json=payload, headers=headers)
    return r


def mendotran_request_stop_info(stop_id: str):
    payload = {
        "first_time": "true",
        "stop_id": stop_id,
        "token": "OQkGfHEQqWRO9zXRQgJb",
        "xss": "3b935fa2ffe3c87bc65363e2",
    }
    r = requests.post(stops_info_url, json=payload, headers=headers)
    return r
