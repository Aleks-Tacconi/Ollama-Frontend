import sys

from website import Website


def main() -> None:
    if len(sys.argv) < 1:
        raise ValueError("Missing model name")

    website = Website(sys.argv[1])
    website.main()


if __name__ == "__main__":
    main()
