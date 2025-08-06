import json

from lib.cmdline import cmdLineParser
from lib.constants import MAIN_DIR
from lib.loader import load_plugin


def main():
    args = cmdLineParser()
    url = args.target
    port = args.port
    OUTPUT_JSON = MAIN_DIR / args.output


    if not url:
        raise Exception("No one target to scan")

    results = load_plugin(url=url, port=port)

    url_result = {
        "target": url,
        "results": results,
    }
    with OUTPUT_JSON.open('w') as jf:
        json.dump(url_result, jf, indent=2)
