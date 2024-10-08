# Media Downloader
Web video/audio downloader
<br><img src="screenshots/kde-plasma-light.png" width="700px"><br>
A simple qt6 frontend for [yt-dlp](https://github.com/yt-dlp/yt-dlp) written in Python using PySide6.
- Supports [hundreds of websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
- Supports downloading mp3 and mp4
- Supports downloading & embedding subtitles
- Allows you to download and work with multiple URLs at once
- Automatically embeds video chapters, thumbnails & metadata
- Supports cropping thumbnails / album arts to square shape (useful when downloading music)
## Installation
<a href="https://flathub.org/apps/com.markopejic.downloader"><img width="150" alt="Download from Flathub" src="https://dl.flathub.org/assets/badges/flathub-badge-en.png"></a><br>
<br><a href="https://github.com/markop404/media-downloader/releases"><img width="140" alt="Download for Windows" src="https://upload.wikimedia.org/wikipedia/commons/e/e2/Windows_logo_and_wordmark_-_2021.svg"></a><br>
## Dependencies
Apart from a few Python packages, listed in [requirements.txt](./requirements.txt), only [ffmpeg](https://ffmpeg.org) is required.
## Goals of This Project
This project aims to create an application that:
- automates things that would have to be done manually on other similar frontends
- only has the most used features
- has a powerful yet simple and streamlined user interface
- is lightweight and has a small amount of dependencies
## Contributing
Any contributions are appreciated, but they have to follow the app's goals.
## Donation
You can support this project by [donating](https://downloader.markopejic.com/donate) to the main developer.
## License
All versions above (including) 3.1.0 are licensed under [GPL version 3 or later](https://www.gnu.org/licenses/gpl-3.0.html). All versions below 3.1.0 are closed source and are not available in this repository.
## Additional Information
### Theming
The program uses the QT's Fusion theme. This setting is hard-coded, so the program does not respond to themes set globally in a system (apart from responding to light/dark theme).
### Translations
There is currently no interest in translating this program to other languages. Also, the current code is not written in a way that fully supports translating.
### Installation & Updates on Windows
This program currently has no update mechanism or installer for Windows. However, there are plans to add them in a future version.
## Disclaimer
The creator of Media Downloader is not responsible/liable for any misuse of this program that may violate local copyright/DMCA laws. Users use this application at their own risk.
