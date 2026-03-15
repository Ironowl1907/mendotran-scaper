# Mendotran requester
import stops as stops


def main():
    r = stops.mendotran_request_stop_info(25600)
    if (r.status_code == 200):
        print(r.text)
    else:
        print(f"Failed with exit code: {r.status_code}")


if __name__ == "__main__":
    main()
