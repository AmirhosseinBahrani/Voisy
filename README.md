# Voisy
 
# How to install dependencies

Mac/Linux:

We have two ways to download ffmpeg in Mac:

1- With homebrew:
```ruby
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install ffmpeg
```

2- install from FFmpeg site
Install ffmpeg from this link
```ruby
cd ~/Downloads

ls /usr/local/bin

sudo mkdir -p /usr/local/bin

sudo cp ff* /usr/local/bin

sudo xattr -dr com.apple.quarantine /usr/local/bin/ff*
```

3- install node modules:
```bash
cd ~/Voisy

npm install
```

4- install python modules:
```bash
pip install vosk, flask, wave, srt, shutil, uuid, pydub, googletrans
```

# Run program:

```bash
cd ~/Voisy

cd ~/src

electron main.js
```

if above commands got error, you need to run LocalApi manually

1- run LocalApi:
```bash
cd ~/Voisy/src/Core

python3 LocalApi.py
```

2- run electron:
```
cd ~/Voisy/src

electron main.js
```


# Futures

you can Transcribe your audio files and video files easily with voisy, also you can Translate them to your favorite language and the transcribing procces is fully offline. you can download or create your own models for any language you want and use it on voicy, currently these languages will installed on voisy by defualt:

English
Persian
Germany
French
Arabic
Russian
Chinese

Default models are low weight, if you want better result you need to download models from Export tab in the app. we recommend for transcribing, use first model on the export tabs from each part.


# Notes

1- There is one executable file called LocalApi in Core folder that electron will run this file for turning LocalApi on


# License

MIT License

Copyright (c) 2021 AmirhosseinBahrani

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
