import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file: typing.IO[str] | None = None

    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(sys.argv[1])
        content = file.read()
        print("---\n")
        print(content)
        print("\n---")
        for char in content:
            new_content = char
            if char == '\n':
                new_content = '#'

    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    finally:
        if file is not None:
            file.close()
            print(f"File '{sys.argv[1]}' closed.")

    print("\nTransform data:")
    new_content = ""
    for char in content:
        if (char == '\n'):
            new_content += '#'
        new_content += char
    if len(new_content) > 0 and new_content[-1] != '#':
        new_content += '#'

    print("---\n")
    print(new_content)
    print("\n---")

    new_name = input("Enter new file name (or empty): ")

    if new_name == "":
        print("Not saving data.")
    else:
        new_file: typing.IO[str] | None = None
        try:
            print(f"Saving data to '{new_name}'")
            new_file = open(new_name, "w")
            new_file.write(new_content)
            print(f"Data saved in file '{new_name}'\n")
        except OSError as e:
            print(f"Error saving file '{new_name}': {e}")
        finally:
            if new_file is not None:
                new_file.close()


if __name__ == "__main__":
    main()
