from konlpy.tag import Okt

positive_words = {"좋다", "행복", "즐겁다", "기쁘다", "설레다"}
negative_words = {"우울", "힘들다", "짜증", "화난다", "지친다"}

def process_emotion_text(text: str):
    okt = Okt()
    words = okt.morphs(text)

    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)

    emotion_score = pos_count - neg_count

    if emotion_score > 0:
        final_emotion = "긍정"
    elif emotion_score < 0:
        final_emotion = "부정"
    else:
        final_emotion = "중립"

    return {
        "final_emotion": final_emotion,
        "emotion_score": emotion_score,
        "keywords": words
    }
