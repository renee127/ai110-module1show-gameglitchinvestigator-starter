from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_too_high_hint_says_go_lower():
    # Bug fix: a guess above the secret used to say "Go HIGHER!"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_hint_says_go_higher():
    # Bug fix: a guess below the secret used to say "Go LOWER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_compares_as_numbers_not_strings():
    # Bug fix: secret was turned into a string on even attempts, so "100" < "30"
    # alphabetically. As integers, 100 is higher than 30.
    outcome, message = check_guess(100, 30)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_difficulty_ranges():
    # Bug fix: Hard used to be 1-50, smaller than Normal's 1-100
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_harder_difficulty_has_bigger_range():
    # Each step up in difficulty should widen the range
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high
