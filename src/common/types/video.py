class Video:
    """Video wrapper."""

    def __init__(self, v_id: int, name: str, desc: str = ""):
        """Constructor.

        Args:
            v_id (int): video id
            name (str): video name
            desc (str, optional): video description. Defaults to empty string.
        """
        self.id = v_id
        self.name = name
        self.description = desc

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Video):
            return (
                self.description == __o.description
                and self.name == __o.name
                and self.id == __o.id
            )
        return False
