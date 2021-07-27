__version__ = '0.0.7'
debug = False
no_parallel = False
sound_set = [
    'Central_100ms.wav', 'Central_50ms.wav', 'left_22.5deg_100ms.wav',
    'left_22.5deg_50ms.wav', 'left_45deg_100ms.wav', 'left_45deg_50ms.wav',
    'left_67deg_100ms.wav', 'left_67deg_50ms.wav', 'left_90deg_100ms.wav',
    'left_90deg_50ms.wav', 'right_22.5deg_100ms.wav', 'right_22.5deg_50ms.wav',
    'right_45deg_100ms.wav', 'right_45deg_50ms.wav', 'right_67deg_100ms.wav',
    'right_67deg_50ms.wav', 'right_90deg_100ms.wav', 'right_90deg_50ms.wav'
]
sound_files = ['stimuli/' + s for s in sound_set]
classes = ['std' if '50ms' in s else 'dev' for s in sound_set]
counts = {
    'hvc': [145 if c == 'std' else 15 for c in classes],
    'lvc': [435 if c == 'std' else 45 for c in classes],
}
if debug:
    counts = {
        'hvc': [29 if c == 'std' else 3 for c in classes],
        'lvc': [87 if c == 'std' else 9 for c in classes]
    }

# Fix low variance condition counts (remove 67 and 90 degree sounds entirely)
for idx, snd in enumerate(sound_set):
    if '67deg' in snd or '90deg' in snd or '45deg' in snd:
        counts['lvc'][idx] = 0

soa_time = 0.5
code_length = 0.1
rest_time = 300
if debug:
    rest_time = 3
global_volume = 0.02
