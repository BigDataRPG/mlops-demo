from src.generate import recommend_character


def test_recommend_character():
    result = recommend_character("Likes magic", "prompts/recommend.txt")
    assert result["class"] == "Mage"
