def secure_archive(file_name: str, action: str, content: str
                   ) -> tuple[bool, str]:

    try:
        if action == "read":
            with open(file_name, "r") as file:
                data = file.read()
                return True, data

        if action == "write":
            with open(file_name, "w") as file:
                file.write(content)
                return True, "Content successfully written to file"

        return False, "Invalid action"
    except OSError as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    success, result = secure_archive("/not/existing/file", "read", "")
    print(f"{success}, {result}\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    success, result = secure_archive("/etc/master.passwd", "read", "")
    print(f"{success}, {result}\n")

    print("Using 'secure_archive' to read from a regular file:")
    success, result = secure_archive("ex3/ancient_fragment.txt", "read", "")
    print(f"{success}, {result}\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    success, result = secure_archive("ex3/ancient_fragment.txt", "write",
                                     "Hello World")
    print(f"{success}, {result}\n")


if __name__ == "__main__":
    main()
