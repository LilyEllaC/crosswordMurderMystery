import pygame


class AudioManager:
    def __init__(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        self.music_channel = pygame.mixer.music

        self.sfx_library = {}

    def play_theme(self, file_path):
        try:
            self.music_channel.load(file_path)
            self.music_channel.play(loops=-1)
            self.music_channel.set_volume(0.5)
        except Exception as e:
            print(f"Error loading theme: {e}")

    def stop_theme(self):
        self.music_channel.stop()

    def play_sfx(self, file_path, volume=1.0):
        if file_path not in self.sfx_library:
            try:
                self.sfx_library[file_path] = pygame.mixer.Sound(file_path)
            except Exception as e:
                print(f"Could not load SFX: {e}")
                return

        self.sfx_library[file_path].set_volume(volume)
        self.sfx_library[file_path].play()
