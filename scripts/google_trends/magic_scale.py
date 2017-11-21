MAGIC_WORDS = [
    'chat',
    'lapin',
    'renard',
    'vipère',
    'cyclohexane'
]

MAGIC_SCALE = [
    {'from': 'lapin', 'to': 'chat', 'ratio': 4.2105263157894735},
    {'from': 'renard', 'to': 'lapin', 'ratio': 2.7142857142857144},
    {'from': 'vipère', 'to': 'renard', 'ratio': 15.333333333333334},
    {'from': 'cyclohexane', 'to': 'vipère', 'ratio': 4}
]

# TODO: can be largely optimized if required
def convert(from_unit, value):

    if from_unit == MAGIC_WORDS[0]:
        return value

    reversed_scale = list(reversed(MAGIC_SCALE))
    current_unit = from_unit
    i = next(index for index in range(len(reversed_scale)) if reversed_scale[index]['from'] == current_unit)

    while current_unit != MAGIC_WORDS[0]:
        conversion = reversed_scale[i]
        value /= conversion['ratio']
        current_unit = conversion['to']
        i += 1

    return value
