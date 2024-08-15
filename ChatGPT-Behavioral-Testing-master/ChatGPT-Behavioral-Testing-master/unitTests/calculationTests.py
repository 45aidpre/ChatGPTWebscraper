import pytest
from ChatGPTScraper import ChatGpt


@pytest.fixture(scope="class")
def chatbot():
    """Fixture to initialize ChatGpt and open the chat session."""
    bot = ChatGpt()
    return bot


@pytest.mark.usefixtures("chatbot")
class TestCalculation:
    def test_arithmetic(self, chatbot):
        chatbot.openChatGpt()
        responseString = chatbot.sendFirstMessage("What is 4 * 4")
        assert responseString == "16"

        responseString = chatbot.sendConversationMessage(
            "Allen finds $109.43 while visiting Nevada. He wants to distribute his money evenly to his 4 friends. If $10.51 is lost on the way back to Denver, how much money will each of his friends receive when he returns?",
            5)
        assert responseString == "24.73"

        responseString = chatbot.sendConversationMessage("Which of these is a monomial?: 3x^2 or 5x^-3", 7)
        assert responseString == "3x^2"

        responseString = chatbot.sendConversationMessage("5/x+8 < 0 in interval notation", 9)
        assert responseString == "(-5/8, 0)"

        responseString = chatbot.sendConversationMessage("log base 2, 16", 11)
        assert responseString == "4"

        chatbot.stopScraper()