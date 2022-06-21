import numpy as numpy
import pygame as pygame

pygame.init()
pygame.mixer.init()
pygame.display.set_mode([600, 400])


def mix_sound(frequency, duration=100, rate=44100):
    frames = int(duration * rate)
    synth = numpy.cos(2 * numpy.pi * frequency * numpy.linspace(0, duration, frames))
    synth = numpy.clip(synth * 10, -1, 1)  # 2nd
    # synth = numpy.cumsum(numpy.clip(arr*10, -1, 1)) # 3rd
    # synth = synth+numpy.sin(2*numpy.pi*frequency*numpy.linspace(0,duration, frames)) # 3rd
    synth = synth / max(numpy.abs(synth))  # 4
    sound = numpy.asarray([32767 * synth, 32767 * synth]).T.astype(numpy.int16)
    sound = pygame.sndarray.make_sound(sound.copy())
    print(sound)

    return sound


octave = {
    "C5": 523.251,
    "H4": 493.883,
    "A4": 440,
    "G4": 391.995,
    "F4": 349.228,
    "E4": 329.628,
    "D4": 293.665,
    "C4": 261.626
}

cache = {
    "c": mix_sound(octave["C5"]),
    "h": mix_sound(octave["H4"]),
    "a": mix_sound(octave["A4"]),
    "g": mix_sound(octave["G4"]),
    "f": mix_sound(octave["F4"]),
    "e": mix_sound(octave["E4"]),
    "d": mix_sound(octave["D4"]),
    "x": mix_sound(octave["C4"])
}

running = True
playing = {}

pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP])

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = str(event.unicode)

            if not cache.__contains__(key):
                continue

            playing[key] = cache[key]
            playing[key].play()
        elif event.type == pygame.KEYUP:
            key = str(event.unicode)

            if not playing.__contains__(key):
                continue

            playing[key].fadeout(100)

            playing.pop(key)
