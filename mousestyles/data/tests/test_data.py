"""Standard test data.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from numpy.testing import assert_equal

import mousestyles.data as data


def test_all_features_loader():
    all_features = data.load_all_features()
    assert_equal(all_features.shape, (21131, 13))
