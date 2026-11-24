import os

# Twist: stamping LGTM looks like clearing your queue and letting the PR author move on,
# but "free the author" + "transfer custody" inverts it—they walk free while you inherit
# both lifelong guardianship of their code and liability when it breaks.
LINE = "Your next LGTM will clear the queue, free the author, and transfer custody."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
