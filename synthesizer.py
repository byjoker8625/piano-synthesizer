import numpy as numpy
import pygame as pygame

pygame.init()
pygame.mixer.init()

"""
Quellen:

https://de.wikipedia.org/wiki/Synthesizer
https://de.wikipedia.org/wiki/Frequenzen_der_gleichstufigen_Stimmung

"""


def mix_sound(frequency, duration=100, rate=44100):
    frames = int(duration * rate)
    synth = numpy.cos(2 * numpy.pi * frequency * numpy.linspace(0, duration, frames))
    synth = numpy.clip(synth*10, -1, 1) # 2nd
    # synth = numpy.cumsum(numpy.clip(arr*10, -1, 1)) # 3rd
    # synth = synth+numpy.sin(2*numpy.pi*frequency*numpy.linspace(0,duration, frames)) # 3rd
    synth = synth / max(numpy.abs(synth))  # 4
    sound = numpy.asarray([32767 * synth, 32767 * synth]).T.astype(numpy.int16)
    sound = pygame.sndarray.make_sound(sound.copy())

    return sound


octave = {
    "_C": 523.251,
    "H": 493.883,
    "A": 440,
    "G": 391.995,
    "F": 349.228,
    "E": 329.628,
    "D": 293.665,
    "C": 261.626,
    "_": 0
}

for note in octave.__reversed__():
    print(note)
    mix_sound(octave[note]).play().fadeout(100)
