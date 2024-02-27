import argparse
import urllib.request
import json
from datetime import datetime

def submit_gist(game_name, t_flag, r_flag, p_flag):
    text = game_name
    if t_flag or r_flag or p_flag:
        payload = {
            "Finish": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "T": text if t_flag else "",
            "R": text if r_flag else "",
            "P": text if p_flag else ""
        }

        try:
            gist_url = "https://gist.githubusercontent.com/superheher/3b12eb930c738291895375b4d7ca25bb/raw"
            response = urllib.request.urlopen(gist_url)
            data = json.loads(response.read())
            data.append(payload)
            data_json = json.dumps(data).encode("utf-8")
            req = urllib.request.Request(gist_url, data=data_json, method="PUT", headers={"Content-Type": "application/json"})
            response = urllib.request.urlopen(req)
            if response.getcode() == 200:
                print("Данные успешно отправлены")
            else:
                print("Не удалось отправить данные")
        except Exception as e:
            raise e
    else:
        print("Выберите хотя бы одну опцию -T, -R или -P")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Submit game statistics to gist")
    parser.add_argument("-n", "--name", type=str, help="Наименование игры")
    parser.add_argument("-T", action="store_true", help="Флаг T")
    parser.add_argument("-R", action="store_true", help="Флаг R")
    parser.add_argument("-P", action="store_true", help="Флаг P")
    args = parser.parse_args()

    submit_gist(args.name, args.T, args.R, args.P)
