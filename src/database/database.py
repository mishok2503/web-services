from src.common.types.video import Video


class DataBase:
    """RAI for database."""

    def __init__(self):
        """Init database."""
        self._data = {}
        self._cur_video_id = 0

    def _set_video(self, video: Video):
        self._data[video.id] = video

    def insert_video(self, name: str, desc: str = "") -> int:
        """Insert new video to database.

        Args:
            name (str): video name
            desc (str, optional): video description. Defaults to "".

        Returns:
            int: new video id
        """
        self._cur_video_id += 1
        self._set_video(Video(self._cur_video_id, name, desc))
        return self._cur_video_id

    def update_video(self, video: Video) -> bool:
        """Update video in database if db contains it.

        Args:
            video (Video): video to update

        Returns:
            bool: true if video in db
        """
        if video.id in self._data:
            self._set_video(video)
            return True
        return False

    def delete_video(self, video_id: str) -> bool:
        """Delete video from database.

        Args:
            video_id (str): video id to delete

        Returns:
            bool: true if video in db
        """
        if video_id in self._data:
            del self._data[video_id]
            return True
        return False

    def get_video(self, video_id: str) -> Video | None:
        """Get video by id.

        Args:
            video_id (str)

        Returns:
            Video | None: video if it exists in db
        """
        if video_id in self._data:
            return self._data[video_id]
        return None

    def clear(self):
        """Clear database"""
        self._cur_video_id = 0
        self._data = {}


database = DataBase()
