# test_complaint_priority.py
import pytest
from complaint_priority import priority_score
 
def test_urgent_category_starts_high():
    assert priority_score("electrical", 0) == 3
 
def test_minor_category_starts_low():
    assert priority_score("furniture", 0) == 1
 
def test_score_escalates_with_days_open():
    assert priority_score("electrical", 2) == 5
 
def test_negative_days_open_raises():
    with pytest.raises(ValueError):
        priority_score("electrical", -1)
