from src.common.types.video import Video


class DataBase:
    """RAI for database."""

    def __init__(self):
        """Init database."""
        self.data = {}
        self.cur_video_id = 0

    def _set_video(self, video: Video):
        self.data[video.id] = video

    def insert_video(self, name: str, desc: str = "") -> int:
        """Insert new video to database.

        Args:
            name (str): video name
            desc (str, optional): video description. Defaults to "".

        Returns:
            int: new video id
        """
        self.cur_video_id += 1
        self._set_video(Video(self.cur_video_id, name, desc))
        return self.cur_video_id

    def update_video(self, video: Video) -> bool:
        """Update video in database if db contains it.

        Args:
            video (Video): video to update

        Returns:
            bool: true if video in db
        """
        if video.id in self.data:
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
        if video_id in self.data:
            del self.data[video_id]
            return True
        return False

    def get_video(self, video_id: str) -> Video | None:
        """Get video by id.

        Args:
            video_id (str)

        Returns:
            Video | None: video if it exists in db
        """
        if video_id in self.data:
            return self.data[video_id]
        return None


database = DataBase()
