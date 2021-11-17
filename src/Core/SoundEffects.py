from pysndfx import AudioEffectsChain
import librosa
fx = (
    AudioEffectsChain()
    .highshelf()
    .reverb()
    .phaser()
    .delay()
    .lowshelf()
)

infile = 'my_audio_file.wav'
outfile = 'my_processed_audio_file.ogg'

fx(infile, outfile)


y, sr = librosa.load(infile, sr=None)
y = fx(y)
y = fx(infile)
fx(x, outfile)