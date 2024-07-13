from pydub import AudioSegment
from pydub.silence import split_on_silence

def add_silence_between_sentences(input_file, output_file, silence_duration=3000):
    sound = AudioSegment.from_mp3(input_file)
    silence = AudioSegment.silent(duration=silence_duration)
    chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-40)
    output = AudioSegment.empty()
    for chunk in chunks:
        output += chunk + silence
    output.export(output_file, format="mp3")

input_file = "input.mp3"
output_file = "output_with_silence.mp3"
add_silence_between_sentences(input_file, output_file)
