from collections.abc import Sequence

def use_sequence(seq: Sequence):
    print(f'the type of this sequence is {type(seq)}')
    assert issubclass(type(seq), Sequence)
    print(f'it\'s length is {len(seq)}')
    print(f'it\'s repr is {repr(seq)}')
    print('here are it\'s items:')
    for seq_item in seq:
        print(seq_item)
    print('_' * 20)
    return