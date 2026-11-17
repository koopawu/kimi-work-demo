"""Greeting generation logic."""


def build_greeting(name: str = "World") -> str:
    """Return a friendly greeting for a non-empty name.

    Args:
        name: The person or group to greet.

    Raises:
        ValueError: If the name is empty or contains only whitespace.
    """
    normalized_name = name.strip()
    if not normalized_name:
        raise ValueError("name must not be empty")
    return f"Hello, {normalized_name}!"
