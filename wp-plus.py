"""
      _______ _      __________________       _______ _______ _______ _______
     (  ___  | \     \__   __|__   __( \     (  ___  |  ____ |  ____ |  ___  )
     | (   ) | (        ) (     ) (  | (     | (   ) | (    )| (    )| (   ) |
     | (___) | |        | |     | |  | |     | (___) | (____)| (____)| |   | |
     |  ___  | |        | |     | |  | |     |  ___  |  _____)     __) |   | |
     | (   ) | |        | |     | |  | |     | (   ) | (     | (\ (  | |   | |
     | )   ( | (____/\__) (_____) (__| (____/\ )   ( | )     | ) \ \_| (___) |
     |/     \(_______|_______|_______(_______//     \|/      |/   \__(_______)

[+] ABOUT SCRIPT:
[-] With this script, you can get unlimited GB on Warp+.
[-] Version: 4.0.0
--------
[+] THIS SCRIPT CODED BY ALIILAPRO
[+] CONTRIBUTORS: JOGERJ
[-] SITE: aliilapro.github.io
[-] TELEGRAM: aliilapro
--------
"""

import urllib.request
import urllib.error
import json
import datetime
import random
import string
import time
import os
import sys
import argparse
import configparser


def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')


def gen_string(string_length):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(string_length))
    except Exception as error:
        print(error)


def digit_string(string_length):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for _ in range(string_length)))
    except Exception as error:
        print(error)


def run(referral_id):
    try:
        install_id = gen_string(22)
        body = {"key": "{}=".format(gen_string(43)),
                "install_id": install_id,
                "fcm_token": "{}:APA91b{}".format(install_id, gen_string(134)),
                "referrer": referral_id,
                "warp_enabled": False,
                "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                "type": "Android",
                "locale": "es_ES"}
        data = json.dumps(body).encode('utf8')
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                   'Host': 'api.cloudflareclient.com',
                   'Connection': 'Keep-Alive',
                   'Accept-Encoding': 'gzip',
                   'User-Agent': 'okhttp/3.12.1'
                   }
        req = urllib.request.Request(URL, data, headers)
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        response_msg = response.msg
    except urllib.error.HTTPError as error:
        status_code = error.code
        response_msg = error.reason
    except Exception as error:
        status_code = "UnknownError"
        response_msg = str(error)
    finally:
        return status_code, response_msg


def cmdline_args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("referral id", nargs='*', help="(Optional) Device id(s)")
    default_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    p.add_argument('-c', '--config', dest='config_file', default=default_path, type=str,
                              help="Specify path to config file. If referral id arguments are used,"
                                   + " it will combine both ids found in config file and positional arguments."
                                   + " If unused, will read 'config.ini' file if it exists.")
    p.add_argument('-i', '--ignore', dest='ignore_config', action="store_true",
                              help="Ignore existing config files. When used with '-c', may overwrite specified file")
    p.add_argument('-d', '--delay', dest='delay', default=18, type=int,
                   help="Specify custom delay (in seconds) between requests. Default is 18 seconds."
                        + " WARNING: Too short delay may lead to errors!")

    return p.parse_args()


def validate_id(device_id: str):
    return [len(x) for x in device_id.split('-')] == [8, 4, 4, 4, 12]


def read_config(parsed_args: argparse.Namespace, path: str):
    config = configparser.ConfigParser()
    try:
        if os.path.exists(path):
            config.read(path)
            if 'CONFIG' in config:
                if 'device_ids' in config['CONFIG']:
                    device_ids = [device_id.strip() for device_id in config['CONFIG']['device_ids'].split(';')]
                    args_ids = getattr(parsed_args, 'referral id')
                    args_ids += device_ids
                    setattr(parsed_args, 'referral id', list(filter(validate_id, args_ids)))
        else:
            print(f"Config file '{path}' not found! Skipping...")
    except IOError as e:
        print(e)
    finally:
        return config


ANIMATION = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%",
             "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]
URL = f'https://api.cloudflareclient.com/v0a{digit_string(3)}/reg'

if __name__ == "__main__":
    os.system("title WARP-PLUS-CLOUDFLARE By ALIILAPRO")
    clrscr()
    args = cmdline_args()
    read_config(args, args.config_file)
    referral_ids = getattr(args, 'referral id')
    if not referral_ids:
        input_id = input("[#] Enter the WARP+ Device ID: ")
        if not input_id:
            print("WARP+ Device ID cannot be empty!\nExiting...")
            exit(0)
        if not validate_id(input_id):
            print("WARP+ Device ID is not valid (incorrect length)!\nExiting...")
            exit(0)
        save_id = input("Save this ID? [Y/n] ")
        if not save_id.lower().startswith('n'):
            try:
                new_config = configparser.ConfigParser()
                new_config.read(args.config_file)
                new_config['CONFIG'] = {'device_ids': input_id}
                with open(args.config_file, 'w') as configfile:
                    new_config.write(configfile)
            except IOError as error:
                print(error)
        referral_ids.append(input_id)

    sum_g = 0
    sum_b = 0
    g = dict((i, 0) for i in referral_ids)
    while True:
        for referrer in referral_ids:
            response_code, msg = run(referrer)
            if response_code == 200:
                sum_g += 1
                g[referrer] += 1
                clrscr()
                print("\n                  WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO\n")
                for i in range(len(ANIMATION)):
                    time.sleep(0.5)
                    sys.stdout.write("\r[+] Preparing... " + ANIMATION[i % len(ANIMATION)])
                    sys.stdout.flush()
                print(f"\n[-] WORKING ON ID: '{referrer}'")
                print(f"[✓] HTTP {response_code}: {msg}")
            else:
                sum_b += 1
                clrscr()
                print("\n                  WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO\n")
                print(f"\n[-] WORKING ON ID: '{referrer}'")
                print(f"[✗] Error when connecting to server. HTTP {response_code}: {msg}")
            print(f"[#] {g[referrer]} GB has been successfully added to this account.")
            print(f"[#] Total: {sum_g} Good {sum_b} Bad")
            for timer in range(args.delay, 0, -1):
                sys.stdout.write(f"\r[*] After {timer} seconds, a new request will be sent.")
                sys.stdout.flush()
                time.sleep(1)
