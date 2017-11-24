import math
from statistics import mean

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

def find_precision_by_mean(precision_series, keyword_series):
    i = 0
    l = len(MAGIC_WORDS)
    p_mu = math.inf
    k_mu = -math.inf
    precision = MAGIC_WORDS[0]

    while p_mu > k_mu and i < l:
        p_mu = mean(precision_series[i])
        k_mu = mean(keyword_series[i])
        precision = MAGIC_WORDS[i]
        i += 1

    # Previous precision MAY be better if mean ratio is lower

    if k_mu > 0:
        prev_k_mu = mean(keyword_series[i-2])
        prev_p_mu = mean(precision_series[i-2])
        previous_ratio = max(prev_p_mu, prev_k_mu) / min(prev_p_mu, prev_k_mu)
        current_ratio = max(p_mu, k_mu) / min(p_mu, k_mu)
        if previous_ratio < current_ratio:
            precision = MAGIC_WORDS[i-2]

    return precision