import os

LINE = (
    "Out of office: I'm hallucinating on a beach somewhere. "
    "For urgent matters, consult my training data \u2014 "
    "it invented me, and it's improvising too."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
