__version__ = '0.1.1'
debug = False
no_parallel = False
sound_set = [
    ('left_90deg_50ms.wav', 1),
    ('left_67deg_50ms.wav', 2),
    ('left_45deg_50ms.wav', 3),
    ('left_22.5deg_50ms.wav', 4),
    ('Central_50ms.wav', 5),
    ('right_22.5deg_50ms.wav', 6),
    ('right_45deg_50ms.wav', 7),
    ('right_67deg_50ms.wav', 8),
    ('right_90deg_50ms.wav', 9),
    ('left_90deg_100ms.wav', 11),
    ('left_67deg_100ms.wav', 12),
    ('left_45deg_100ms.wav', 13),
    ('left_22.5deg_100ms.wav', 14),
    ('Central_100ms.wav', 15),
    ('right_22.5deg_100ms.wav', 16),
    ('right_45deg_100ms.wav', 17),
    ('right_67deg_100ms.wav', 18),
    ('right_90deg_100ms.wav', 19)
]
sound_files = ['stimuli/' + s[0] for s in sound_set]
classes = ['std' if '50ms' in s[0] else 'dev' for s in sound_set]
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
for idx, (snd, code) in enumerate(sound_set):
    if '67deg' in snd or '90deg' in snd or '45deg' in snd:
        counts['lvc'][idx] = 0

soa_time = 0.5
code_length = 0.1
rest_time = 300
if debug:
    rest_time = 3
global_volume = 0.02
