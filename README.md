# Voisy

# How to install dependencies

install model:
you can download model from this link:
https://alphacephei.com/vosk/models/vosk-model-en-us-0.21-compile.zip

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
