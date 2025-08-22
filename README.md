# Media Downloader

Web video/audio downloader
<br><img src="screenshots/kde-plasma-light.png" width="650px"><br>
A simple qt6 frontend for [yt-dlp](https://github.com/yt-dlp/yt-dlp) written in Python using PySide6.

- Supports [hundreds of websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
- Supports downloading mp3 and mp4
- Supports downloading & embedding subtitles
- Allows you to download and work with multiple URLs at once
- Automatically embeds video chapters, thumbnails & metadata
- Supports cropping thumbnails / album arts to square shape (useful when downloading music)

## Project Status

Development in this repository is currently **limited to maintenance and bug fixes only**. When I will have the time, I will do a complete rewrite of the app and implement some of the missing features / ideas I have.

The ```main``` branch contains an older codebase that is difficult to work with. The ```partial``` branch contains an unsuccessful partial rewrite.

## Installation

<a href="https://flathub.org/apps/com.markopejic.downloader"><img width="150" alt="Download from Flathub" src="https://dl.flathub.org/assets/badges/flathub-badge-en.png"></a><br>
<br><a href="https://github.com/markop404/media-downloader/releases"><img width="140" alt="Download for Windows" src="https://upload.wikimedia.org/wikipedia/commons/e/e2/Windows_logo_and_wordmark_-_2021.svg"></a><br>

## Dependencies

Apart from a few Python packages, listed in [requirements.txt](./requirements.txt), only [ffmpeg](https://ffmpeg.org) is required.

## Goals of this Project

This project aims to create an application that:

- automates things that would have to be done manually on other similar frontends
- only has the most used features
- has a powerful yet simple and streamlined user interface
- is lightweight and has a small amount of dependencies

## Contributing

Any contributions are appreciated, but they have to follow the app's goals.

## Support

The easiest way to support this project is to star it on GitHub. You can also support the developer by making a [donation](https://downloader.markopejic.com/donate).

## License

All versions above (including) 3.1.0 are licensed under [GPL version 3 or later](https://www.gnu.org/licenses/gpl-3.0.html). All versions below 3.1.0 are closed source and are not available in this repository.

## Missing features / TO DO

- Settings menu with more customization options
- Installer & automatic updates on Windows

## Disclaimer

The creator of Media Downloader is not responsible/liable for any misuse of this program that may violate local copyright/DMCA laws. Users use this application at their own risk.
