import typing
import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file: typing.IO[str] | None = None

    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(sys.argv[1])
        print("---\n")
        print(file.read())
        print("\n---")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{sys.argv[1]}' closed")


if __name__ == "__main__":
    main()
