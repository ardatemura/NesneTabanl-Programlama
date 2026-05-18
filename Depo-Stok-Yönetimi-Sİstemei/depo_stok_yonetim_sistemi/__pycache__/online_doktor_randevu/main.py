if __name__ == "__main__":
    # Allow running from any working directory.
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from app import run

    run()
