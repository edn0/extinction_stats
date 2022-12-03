import requests
import os
from time import time, sleep
from rich import print as rprint
from rich.progress import track

api_url = "https://api.gtaliferp.fr:8443/v1/extinction/profiles/discord/304629682769494026"


headers = {
    'authority': 'api.gtaliferp.fr:8443',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-none-match': 'W/"924-RsfQlc+eIHVpM+alWwa0sGX4uP8"',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}



stats_dict = {
    "zombie": 12,
    "kill":9,
    "death":11,
    "ratio":29,
    "zombie_redzone":23,
    "kill_redzone":4,
    "death_redzone":8,
    "ratio_redzone":30,
    "played_time":1
}

def time_conversion(playtime): ## askpython.com
    sec_value = playtime % (24 * 3600)
    hour_value = sec_value // 3600
    sec_value %= 3600
    minutes = sec_value // 60
    sec_value %= 60

    if minutes < 10:
        time = f"{hour_value}:0{minutes}"
    else:
        time = f"{hour_value}:{minutes}"

    rprint(f"[cyan]{time : <10}[purple] 🕒 Temps de jeu")

def main():


    response = requests.get(api_url, headers=headers)
    data = response.json()

    hour_value = 0
    minutes = 0



    zombie_kills = data["stats"][stats_dict["zombie"]]["value"]
    pvp_kills = data["stats"][stats_dict["kill"]]["value"]
    deaths = data["stats"][stats_dict["death"]]["value"]
    ratio = data["stats"][stats_dict["ratio"]]["value"]
    zombie_redzone = data["stats"][stats_dict["zombie_redzone"]]["value"]
    kills_redzone = data["stats"][stats_dict["kill_redzone"]]["value"]
    deaths_redzone = data["stats"][stats_dict["death_redzone"]]["value"]
    ratio_redzone = data["stats"][stats_dict["ratio_redzone"]]["value"]
    playtime = data["stats"][stats_dict["played_time"]]["value"]
    level = data["rank"]


    rprint(f"{zombie_kills : <10}[purple] 🧟 Zombies tués")
    rprint(f"{pvp_kills : <10}[purple] ⚔️ Opps tués")
    rprint(f"{deaths : <10}[purple] 🩸 Morts")
    rprint(f"{ratio : <10}[purple] 〽 Ratio")
    rprint(f"{zombie_redzone : <10}[purple] 🧟🔴 Zombies tués en redzone")
    rprint(f"{kills_redzone : <10}[purple] ⚔️🔴 Opps tués en redzone")
    rprint(f"{deaths_redzone : <10}[purple] 🩸🔴 Morts en redzone")
    rprint(f"{ratio_redzone : <10}[purple] 〽🔴 Ratio en redzone")
    rprint(f"{level : <10}[purple] 👾 Niveau")

    time_conversion(playtime)

while True:


    os.system('cls||clear') # Clears terminal for readability.
    main()
    rprint("")
    for _ in track(range(100), description="[purple]Délai API"):

        sleep(0.6)
    