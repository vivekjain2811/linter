"""Simple script that prints a greeting message."""


def say_hello(name: str) -> None:
    """Print a greeting message for the given name."""
    print(f"Hello, {name}")


if __name__ == "__main__":
    say_hello("World")
