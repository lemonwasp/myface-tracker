# backend/utils/emotion_processing.py (임시)
from collections import Counter

def process_emotion_text(free_text: str) -> dict:
    # 매우 단순 감정 분류 예시 (나중에 koNLPy 등으로 강화 필요)
    positive_words = ["좋다", "기쁘다", "행복", "신나다"]
    negative_words = ["우울", "힘들다", "짜증", "화난다"]

    tokens = free_text.split()  # 한글 토큰화 간단 처리 (실제론 형태소 분석기 추천)
    word_count = Counter(tokens)

    pos_count = sum(word_count[word] for word in positive_words if word in word_count)
    neg_count = sum(word_count[word] for word in negative_words if word in word_count)

    if pos_count > neg_count:
        final_emotion = "positive"
        sentiment_score = 0.7
    elif neg_count > pos_count:
        final_emotion = "negative"
        sentiment_score = -0.7
    else:
        final_emotion = "neutral"
        sentiment_score = 0.0

    return {
        "final_emotion": final_emotion,
        "emotion_score": sentiment_score,
        "keywords": list(word_count.keys())
    }
