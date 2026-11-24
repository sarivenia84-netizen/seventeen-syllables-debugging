from pathlib import Path


HAIKU = "Logs bloom at midnight\nThe cursor finds the fault's name\nDawn breaks the bug free"


def main():
    try:
        output_dir = Path("/output")
        output_dir.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        output_dir = Path("./output")
        output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "entry.txt").write_text(HAIKU + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
