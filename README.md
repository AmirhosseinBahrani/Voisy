# Voisy

![Screen Shot 2022-03-02 at 11 06 38](https://user-images.githubusercontent.com/69673077/156316127-2c24cf13-b923-4300-9879-b64b8334c32a.png)

# How to install dependencies

Mac/Linux:

We have two ways to download ffmpeg :

1.1. With homebrew:
```ruby
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install ffmpeg
```

install from FFmpeg site
Install ffmpeg from this link
```ruby
cd ~/Downloads

ls /usr/local/bin

sudo mkdir -p /usr/local/bin

sudo cp ff* /usr/local/bin

sudo xattr -dr com.apple.quarantine /usr/local/bin/ff*
```

Windows:

1.1. Download latest version of ffmpeg from https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z

1.2. Unzip this file by using any file archiver such as Winrar or 7z.

1.3. Rename the extracted folder to ffmpeg and move it into the root of C: drive.

1.4. run cmd as an administrator and set the environment path variable for ffmpeg by running the following command:

```bash
setx /m PATH "C:\ffmpeg\bin;%PATH%"
```

1.5. Restart your computer and check installation by running the following command:
```bash
ffmpeg -version
```




2. install node modules:
```bash
cd ~/Voisy

npm install
```

3. install python modules:
```bash
pip install vosk, flask, wave, srt, shutil, uuid, pydub, googletrans
```

# Run program:

```bash
cd ~/Voisy

cd ~/src

electron main.js
```

if above commands got error, you need to run LocalApi manually:

1. run LocalApi:
```bash
cd ~/Voisy/src/Core

python3 LocalApi.py
```

2. run electron:
```
cd ~/Voisy/src

electron main.js
```

you can create executable file from LocalApi, after creating electron will recognize it and it will be running automatically. you need to install pyinstaller for creating exe file:


```bash
pip install pyinstaller

cd ~/Voisy/src/Core

pyinstaller LocalApi.py -w
```

# Notes

1- There is one executable file called LocalApi in ./Core/dist/LocalApi folder that electron will run this file for turning LocalApi on.

# Futures

you can Transcribe your audio files and video files easily with Voisy, also you can Translate them to your favorite language and the transcribing progress is fully offline. you can download or create your own models for any language you want and use it on Voisy, currently these languages are on the Voisy by defualt:

English, Persian, Germany, French, Spanish , Portugees, Italy, Russian, Chinese, Japanese, Turkey

Default models are low weight, if you want better result you need to download models from Export tab in the app. we recommend for transcribing, use first model on the export tabs from each part.


# License

MIT License

Copyright (c) 2021 Voisy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
