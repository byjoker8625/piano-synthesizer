import numpy as numpy
import pygame as pygame

from synthesizer import mix_sound

pygame.init()
pygame.mixer.init()
pygame.display.set_mode([600, 400])

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

cached = {
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

while running:
    for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE:
            break

        if event.type == pygame.KEYDOWN:
            key = str(event.unicode)

            if not octave.__contains__(key):
                continue

            playing[key] = cached[key]
            playing[key].play()
        elif event.type == pygame.KEYUP:
            key = str(event.unicode)

            if not playing.__contains__(key):
                continue

            playing[key].fadeout(100)

            playing.pop(key)
