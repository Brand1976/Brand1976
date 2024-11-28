class MediaFile:
    def __init__(self, name, file_location, size, creation_date, change_date, owner, file_extension):
        self.name = name
        self.file_location = file_location  # directory in local machine
        self.size = size                    # size in bytes
        self.creation_date = creation_date
        self.change_date = change_date
        self.owner = owner
        self.file_extension = file_extension
        self.metadata = {
            'title': None,
            'copyright_info': None,
            'language': None,
            'tags': None,
            'location': None
        }

    def get_from_url(self, url, directory):
        """copy file from web url to directory"""
        pass

    def get_from_ip(self, ip_addr):
        """copy file from given ip address"""
        pass

    def open_file(self, directory):
        """opens file in local directory"""
        pass

    def rename_file(self, new_name):
        """rename the file name"""
        pass

    def save_file_to(self, directory):
        """save file to the local directory"""
        pass

    def delete_file(self):
        """delete file"""
        pass

    def copy_file(self, directory):
        """copy file to directory"""
        pass

    def move_to(self, directory):
        """move file to directory"""
        pass

    def convert_size(self, prefix):
        """
        convert size from bytes to Kilo/Mega/Gigabytes
        receives required prefix from prefix
        """
        pass

    def ch_date(self, date):
        """editing date to date when file was edited"""
        pass

    def set_metadata(self):
        """writes all metadata of audio/video/image file to metadata"""
        pass


class AudioFile(MediaFile):
    def get_audio_duration(self):
        """shows given audio file's duration"""
        pass

    def audio_convert_to(self, extension):
        """
        converts audio file to given from extension
        convert to mp3, flac, wav, aiff, ape, ogg
        """
        pass


class VideoFile(MediaFile):
    def get_video_duration(self):
        """shows given video file's duration"""
        pass

    def get_frame_resolution(self):
        """Shows video's resolution"""
        pass

    def get_bit_rate(self):
        """Shows video and audio bit rate"""
        pass

    def get_fps(self):
        """Gives number of frames per second"""
        pass

    def extract_audio_track(self, directory):
        """Extract audiotrack and save to directory"""
        pass

    def extract_video_track(self, directory):
        """Extract video without audiotrack and save to directory"""
        pass

    def video_convert_to(self, extension):
        """
        converts video file to given from extension
        convert to mp4, wmv, flv, h264, mpeg, webm and other popular extensions
        """
        pass


class ImageFile(MediaFile):
    def convert_image_to(self, extension):
        """
            converts video file to given from extension
            convert to popular image extensions
            """
        pass

    def get_image_resolution(self):
        """shows image's resolution"""
        pass

    def resize_image(self, resolution):
        """resize resolution of the image"""
        pass

    def get_color_mode(self):
        """returns the color mode of the image (RGB, CMYK, etc.)"""
        pass

    def rotate_image(self, angle):
        """rotates an image by a specified angle"""
        pass

    def convert_to_grayscale(self):
        """converts an image to grayscale"""
        pass


file_1 = VideoFile('lesson_1',
                   '/dir/folder_1',
                   '1000',
                   '24.05.2024',
                   '25.05.2024',
                   'administrator',
                   'mp4'
                   )

file_2 = AudioFile(
    'audio_1',
    '/dir/folder_2',
    '20000',
    '24.05.2024',
    '25.05.2024',
    'user',
    'mp3'
)

file_1.metadata = {'title': 'main',
                   'copyright_info': 'copyright',
                   'language': 'eng',
                   'tags': 'some tags',
                   'location': 'country'
                   }

print(vars(MediaFile),'\n')
print(vars(ImageFile),'\n')
print(vars(AudioFile),'\n')
print(vars(VideoFile),'\n')
print(vars(file_1),'\n')
print(vars(file_2),'\n')
