# Mendotran requester
import stops as stops
import json


def main():
    #    r = stops.mendotran_request_stop_info(25600)
    r = stops.mendotran_request_stops()
    json_formatted_str = json.dumps(r, indent=4)
    print(json_formatted_str)


if __name__ == "__main__":
    main()
