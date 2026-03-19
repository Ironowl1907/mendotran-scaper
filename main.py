# Mendotran requester
import stops as stops
import json


def main():
    #    r = stops.mendotran_request_stop_info(25600)
    r = stops.mendotran_request_stops()
    stops.mendotran_generate_db(r)
    # r = stops.mendotran_request_stop_info(25612)
    # r = stops.mendotran_request_services()
    r_formated = json.dumps(r, indent=4)
    print(r_formated)

    pass


if __name__ == "__main__":
    main()
